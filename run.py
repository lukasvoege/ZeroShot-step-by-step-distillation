from typing import List, Dict

import argparse
import numpy as np
import json

from src.teacher_response_evaluator import TeacherResponseEvaluator

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
    print_c(f"PHASE 1: Loading prompt mix {prompt_mix} and setting seed...", c="green")

    prompt_mix_info = read_yaml(f"./prompt-mixes/{prompt_mix}.yaml")

    dataloader = dataLoaderFactory(dataset_name)
    datsets = dataloader.load_from_json()

    np.random.seed(prompt_mix_info["seed"])

    print(f"Seed set to {prompt_mix_info['seed']}.")
    print_c(f"PHASE 1: Done.", c="green")
    print_c(f"PHASE 2: Sampling idxs and querying Teacher Model...", c="green")

    for split in splits:
        print_c(f"{split.upper()}", c="blue")
        if n_samples == None or n_samples > len(datsets[split]):
            n_samples = len(datsets[split])
            ## hier muss jz das bisschen komplizierte sampling hin...
            ## dann querying von den idxs
            ## dann dataset writer


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
