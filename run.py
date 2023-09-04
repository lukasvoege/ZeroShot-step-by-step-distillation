from typing import List, Dict

import argparse
import numpy as np
import json

from src.teacher_response_evaluator import TeacherResponseEvaluator
from src.teacher_writer import TeacherWriter

from src.utils import read_yaml, print_c
from src.factories import teacherQuerierFactory, dataLoaderFactory


def run_experiment(dataset_name: str, test_size: float) -> None:
    """
    Run an experiment in the form of querieng test_size random samples with each available prompt
    and subsequent evaluation of the results to update metadata files and find the best performing
    prompt for each dataset.
    """

    teacher_querier = teacherQuerierFactory(dataset_name)
    evaluator = TeacherResponseEvaluator(dataset_name)

    yaml_file = f"./prompt-templates/{dataset_name}.yaml"
    prompt_templates = read_yaml(yaml_file)["templates"]

    N_PROMPT_TEMPLATE = len(prompt_templates)
    DATASET_SIZE = len(teacher_querier.datasets["train"])

    if test_size < 1:
        test_size = test_size * DATASET_SIZE
    TEST_SIZE = int(test_size)

    test_idx = np.random.choice(DATASET_SIZE, TEST_SIZE, replace=False)
    test_idx = [int(i) for i in test_idx]

    print(
        f"Running prompt experiment on {dataset_name} with {TEST_SIZE} samples for {N_PROMPT_TEMPLATE} prompt templates."
    )
    print("-" * 40)
    print_c("PHASE 1: Querying samples...", c="green")
    total_prompt_tokens, total_completion_tokens, total_costs = 0, 0, 0
    for i, prompt_template in enumerate(prompt_templates):
        print(f"Querying prompt template {prompt_template} ({i+1}/{N_PROMPT_TEMPLATE})...")
        callbacks = teacher_querier._batch_query(
            split="train",
            idxs=test_idx,
            prompt_template_id=prompt_template,
            dont_save=False,
            force_query=False,
            verbosity=1,
        )
        total_prompt_tokens += callbacks[0]
        total_completion_tokens += callbacks[1]
        total_costs += callbacks[2]
    print_c("PHASE 1: Done.", c="green")
    print_c("PHASE 2: Evaluating responses and writing prompt metadata...", c="green")
    best_prompt = evaluator.evaluate_train()
    print_c("PHASE 2: Done.", c="green")
    print("-" * 40)
    print_c(f"Best prompt template for {dataset_name} is {best_prompt}.", c="blue")
    print("Experiment finished with the following costs:")
    print(
        f"Total prompt tokens: {total_prompt_tokens}\nTotal completion tokens: {total_completion_tokens}\nTotal costs: ${total_costs}"
    )


def generate_trainingdata(dataset_name: str, splits: List[str], prompt_mix: int, n_samples: int) -> None:
    print(f"Generating training data for {dataset_name}...")
    print_c(f"PHASE 1: Loading Prompt-Mix {prompt_mix} and seed...", c="green")

    prompt_mix_info = read_yaml(f"./prompt-mixes/{prompt_mix}.yaml")

    dataloader = dataLoaderFactory(dataset_name)
    datsets = dataloader.load_from_json()

    teacher_querier = teacherQuerierFactory(dataset_name)
    teacher_writer = TeacherWriter(dataset_name)

    print(f"Using seed {prompt_mix_info['seed']}.")
    print_c(f"PHASE 1: Done.", c="green")
    print_c(f"PHASE 2: Sampling idxs and querying Teacher Model...", c="green")

    total_prompt_tokens, total_completion_tokens, total_costs = 0, 0, 0

    complete_idxs_mix = {split: {} for split in splits}

    for split in splits:
        print_c(f"{split.upper()}", c="blue")
        if n_samples == None or n_samples > len(datsets[split]):
            n_samples = len(datsets[split])
            
        for part in ["label", "explanation"]:
            # shuffle idxs for each part with the same seed to maximize overlap of idxs for label and explanation
            # to minimize querying
            idxs = list(range(n_samples))
            np.random.seed(prompt_mix_info["seed"])
            np.random.shuffle(idxs)

            # determin how many samples to query for each prompt and correct for rounding errors
            sizes = {key: int(percentage * n_samples) for key, percentage in prompt_mix_info[part].items()}
            sizes[list(sizes.keys())[-1]] += n_samples - sum(sizes.values())

            prompt_idxs = {key: [] for key in prompt_mix_info[part].keys()}
            start = 0
            for key, size in sizes.items():
                end = start + size
                prompt_idxs[key] = idxs[start:end]
                start = end

            # check if all idxs were assigned to a prompt
            assert sum([len(v) for v in prompt_idxs.values()]) == n_samples
            print(f"Sampled and assigned all idxs according to Prompt-Mix ({part}).")

            complete_idxs_mix[split][part] = prompt_idxs

            print_c(f"Querying Teacher Model...", c="yellow")
            for i, prompt_template in enumerate(prompt_idxs.keys()):
                print_c(f"Querying prompt template {prompt_template} ({i+1}/{len(prompt_idxs)})...", c="yellow")
                callbacks = teacher_querier._batch_query(
                    split=split,
                    idxs=prompt_idxs[prompt_template],
                    prompt_template_id=prompt_template,
                    dont_save=False,
                    force_query=False,
                    verbosity=1,
                )
                total_prompt_tokens += callbacks[0]
                total_completion_tokens += callbacks[1]
                total_costs += callbacks[2]

    print_c(f"PHASE 2: Done.", c="green")
    print(
        f"Total prompt tokens: {total_prompt_tokens}\nTotal completion tokens: {total_completion_tokens}\nTotal costs: ${total_costs}"
    )
    print_c(f"PHASE 3: Writing training file(s)...", c="green")
    for split in splits:
        print_c(f"{split.upper()}", c="blue")

        ## TODO: needs to save with prompt mix id
        teacher_writer.write_teacher_responses(split=split, prompt_template_id_mix=complete_idxs_mix[split])
        
    print_c(f"PHASE 3: Done.", c="green")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--experiment", action="store_true")
    parser.add_argument("--test_size", type=float)

    parser.add_argument("--generate_trainingdata", action="store_true")
    parser.add_argument("--splits", type=str, nargs="+")
    parser.add_argument("--prompt_mix", type=int)
    parser.add_argument("--samples", type=int)

    parser.add_argument("--dataset", type=str)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    # set seed for the whole script
    np.random.seed(args.seed)

    if args.experiment:
        run_experiment(args.dataset, args.test_size)
    elif args.generate_trainingdata:
        generate_trainingdata(args.dataset, args.splits, args.prompt_mix, args.samples)
