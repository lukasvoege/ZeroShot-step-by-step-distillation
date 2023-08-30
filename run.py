import argparse
import yaml
import numpy as np

from src.teacher_query_tools import ANLITeacherQuerier, CQATeacherQuerier, ESNLITeacherQuerier, SVAMPTeacherQuerier
from src.teacher_response_evaluator import TeacherResponseEvaluator

from src.utils import read_yaml_prompts, print_c


def run_experiment(dataset_name: str, test_size: float):
    """
    Run an experiment in the form of querieng test_size random samples with each available prompt
    and subsequent evaluation of the results to update metadata files and find the best performing
    prompt for each dataset.
    """
    if dataset_name == "anli1":
        teacher_querier = ANLITeacherQuerier()
    elif dataset_name == "cqa":
        teacher_querier = CQATeacherQuerier()
    elif dataset_name == "esnli":
        teacher_querier = ESNLITeacherQuerier()
    elif dataset_name == "svamp":
        teacher_querier = SVAMPTeacherQuerier()

    evaluator = TeacherResponseEvaluator(dataset_name)

    yaml_file = f"./prompt-templates/{dataset_name}.yaml"
    prompt_templates = read_yaml_prompts(yaml_file)["templates"]

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
            split="train", idxs=test_idx, prompt_template_id=prompt_template, dont_save=False, force_query=False, verbosity=1
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
    print(f"Total prompt tokens: {total_prompt_tokens}\nTotal completion tokens: {total_completion_tokens}\nTotal costs: ${total_costs}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--experiment", action="store_true")
    parser.add_argument("--test_size", type=float)

    parser.add_argument("--generate_trainingdata", action="store_true")
    parser.add_argument("--splits", type=str, nargs="+")

    parser.add_argument("--dataset", type=str)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    # set seed for the whole script
    np.random.seed(args.seed)

    if args.experiment:
        run_experiment(args.dataset, args.test_size)

    print(args.splits)
