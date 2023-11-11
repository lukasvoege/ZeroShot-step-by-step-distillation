import pandas as pd
import os
import json
import argparse

DEFAULT_PASSTHROUGH = "--bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save"

def get_experiments_df():
    # Read csv and have all dtypes as object
    experiments = pd.read_csv("experiment-tracking/experiment_tracking.csv", sep=",", dtype=object)
    # replace nan with "None"
    return experiments.fillna("None")


def get_params_from_path(path: str):
    params = {}
    path = os.path.normpath(path)
    split = path.split(os.path.sep)
    params["dataset"] = split[1]
    params["model"] = split[2]
    params["mode"] = split[3]
    params["llm"] = split[4]
    params["subsample"] = split[5]
    params["prompt_mix"] = split[6]
    params["label_type"] = split[7]
    params["alpha"] = split[8]
    params["max_input_length"] = split[9]
    params["batch_size"] = split[10]
    params["optimizer"] = split[11]
    params["lr"] = split[12]
    params["run"] = split[13]

    params["id"] = get_identifier(params)

    category = "step-by-step " if params["mode"] == "task_prefix" else "standard "
    category += "Distillation" if params["label_type"] == "llm" else "Finetuning"
    params["category"] = category

    params["train_duration"] = "None"
    params["train_steps"] = "None"
    params["eval_acc"] = "None"
    params["test_acc"] = "None"

    return params


def get_identifier(params: dict):
    return "_".join(
        [
            params["dataset"],
            params["model"],
            params["mode"],
            params["llm"],
            params["subsample"],
            params["prompt_mix"],
            params["label_type"],
            params["alpha"],
            params["max_input_length"],
            params["batch_size"],
            params["optimizer"],
            params["lr"],
            params["run"],
        ]
    )

def command_from_row(row: dict, pass_through: str = None):
    info = f"({row['experiment_group']}) {row['category']}: {row['dataset']} - {row['model']} - {row['mode']}"
    for field in ["label_type", "llm", "prompt_mix", "subsample", "alpha"]:
        if row[field] != "None":
            info += f" - {row[field]} {field}"

    echo = "echo '" + '#' * 50 + "'\n"
    echo += "echo '" + info + "'"

    python = "python distilling-step-by-step/run.py"
    python += f" --from_pretrained google/{row['model']}"
    python += f" --dataset {row['dataset']}"
    python += f" --model_type {row['mode']}"
    for field in ["label_type", "llm", "prompt_mix", "subsample", "alpha", "batch_size", "run"]:
        if row[field] not in ["None", "0"]:
            python += f" --{field} {row[field]}"

    if pass_through:
        python += f" {pass_through}"

    command = "# " + info + "\n" + echo + "\n" + python + "\n\n"
    return command

def update_experiment_tracking():
    experiments = get_experiments_df()
    # add id column
    experiments["id"] = experiments.apply(lambda row: get_identifier(row.to_dict()), axis=1)

    for root, _, files in os.walk("results"):
        if files:
            params = get_params_from_path(root)
            for file in files:
                if file == "train_results.txt":
                    with open(os.path.join(root, file)) as f:
                        train_results = f.read().split("metrics=")

                    train_results_dict = train_results[1][:-1].replace("'", '"')
                    params["train_duration"] = round(json.loads(train_results_dict)["train_runtime"], 0)
                    params["train_steps"] = train_results[0].split("global_step=")[-1].split(",")[0]
                elif file == "eval_results.txt":
                    eval_reults = open(os.path.join(root, file)).read()
                    eval_reults = eval_reults.replace("'", '"')
                    params["eval_acc"] = round(json.loads(eval_reults)["eval_accuracy"], 3)
                elif file == "test_results.txt":
                    test_results = open(os.path.join(root, file)).read()
                    test_results = test_results.replace("'", '"')
                    params["test_acc"] = round(json.loads(test_results)["eval_accuracy"], 3)
            ## check if params are in experiments
            if params["id"] in experiments["id"].values:
                ## update experiments
                experiments.loc[experiments["id"] == params["id"], "train_duration"] = params["train_duration"]
                experiments.loc[experiments["id"] == params["id"], "train_steps"] = params["train_steps"]
                experiments.loc[experiments["id"] == params["id"], "eval_acc"] = params["eval_acc"]
                experiments.loc[experiments["id"] == params["id"], "test_acc"] = params["test_acc"]
                print(f"updated {params['id']}")
            else:
                # concat to experiments
                experiments = pd.concat([experiments, pd.DataFrame(params, index=[0])])
                print(f"added {params['id']}")

    # save experiments to csv again
    experiments.drop("id", axis=1).to_csv("experiment-tracking/experiment_tracking.csv", sep=",", index=False)


def generate_missing_experiments(args):
    experiments = get_experiments_df()
    ## remove all experiments that already have train_duration, eval_acc and test_acc
    experiments = experiments[
        (experiments["train_duration"] == "None")
        | (experiments["eval_acc"] == "None")
        | (experiments["test_acc"] == "None")
        | (experiments["train_steps"] == "None")
    ]
    ## select experiments that match the args for all args that are not None
    for arg in vars(args):
        if getattr(args, arg) != None and arg not in ["update_tracking", "generate_missing_experiments_script", "passthrough"]:
            experiments = experiments[experiments[arg] == str(getattr(args, arg))]
    
    ## generate commands for all experiments
    bash_script = "export TOKENIZERS_PARALLELISM=true\n\n"
    for _, row in experiments.iterrows():
        bash_script += command_from_row(row, args.passthrough)

    ## save bash script
    with open(f"experiment-tracking/scripts/{args.generate_missing_experiments_script}.sh", "w") as f:
        f.write(bash_script)
    
    print(f"Generated bash script: experiment-tracking/scripts/{args.generate_missing_experiments_script}.sh with {len(experiments)} experiments.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--update_tracking", action="store_true")

    parser.add_argument("--generate_missing_experiments_script", type=str)
    parser.add_argument("--experiment_group", type=str)
    parser.add_argument("--dataset", type=str)
    parser.add_argument("--model", type=str)
    parser.add_argument("--mode", type=str)
    parser.add_argument("--llm", type=str)
    parser.add_argument("--subsample", type=float)
    parser.add_argument("--prompt_mix", type=int)
    parser.add_argument("--label_type", type=str)
    parser.add_argument("--alpha", type=float)

    parser.add_argument("--passthrough", type=str, default=DEFAULT_PASSTHROUGH)

    args = parser.parse_args()

    if args.update_tracking:
        update_experiment_tracking()
    elif args.generate_missing_experiments_script:
        generate_missing_experiments(args)
