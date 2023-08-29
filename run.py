import argparse
import yaml
import numpy as np

from teacher_query_tools import ANLITeacherQuerier, CQATeacherQuerier, ESNLITeacherQuerier, SVAMPTeacherQuerier


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

    yaml_file = f"./prompt-templates/{dataset_name}.yaml"
    with open(yaml_file, "r") as yf:
        prompt_templates = yaml.safe_load(yf)["templates"]

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
    print("PHASE 1: Querying samples...")
    for i, prompt_template in enumerate(prompt_templates):
        print(f"Querying prompt template {prompt_template} ({i+1}/{N_PROMPT_TEMPLATE})...")
        teacher_querier._batch_query(
            split="train", idxs=test_idx, prompt_template_id=prompt_template, dont_save=False, force_query=False
        )
    print("PHASE 1: Done.")
    print("PHASE 2: Evaluating responses...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--experiment", action="store_true")
    parser.add_argument("--dataset", type=str)
    parser.add_argument("--test_size", type=float)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    # set seed for the whole script
    np.random.seed(args.seed)

    if args.experiment:
        run_experiment(args.dataset, args.test_size)
