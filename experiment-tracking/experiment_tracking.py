import pandas as pd
import os
import json

# Read csv and have all dtypes as object
experiments = pd.read_csv("experiment-tracking/experiment_tracking.csv", sep=";", dtype=object)
# replace nan with "None"
experiments = experiments.fillna("None")


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
        ]
    )


# add id column
experiments["id"] = experiments.apply(lambda row: get_identifier(row.to_dict()), axis=1)

for root, dirs, files in os.walk("results"):
    if files:
        params = get_params_from_path(root)
        for file in files:
            if file == "train_results.txt":
                with open(os.path.join(root, file)) as f:
                    train_results = f.read().split("metrics=")[1][:-1]
                train_results = train_results.replace("'", '"')
                params["train_duration"] = json.loads(train_results)["train_runtime"]
            elif file == "eval_results.txt":
                eval_reults = open(os.path.join(root, file)).read()
                eval_reults = eval_reults.replace("'", '"')
                params["eval_acc"] = json.loads(eval_reults)["eval_accuracy"]
            elif file == "test_results.txt":
                test_results = open(os.path.join(root, file)).read()
                test_results = test_results.replace("'", '"')
                params["test_acc"] = json.loads(test_results)["eval_accuracy"]
        ## check if params are in experiments
        if params["id"] in experiments["id"].values:
            ## update experiments
            experiments.loc[experiments["id"] == params["id"], "train_duration"] = params["train_duration"]
            experiments.loc[experiments["id"] == params["id"], "eval_acc"] = params["eval_acc"]
            experiments.loc[experiments["id"] == params["id"], "test_acc"] = params["test_acc"]
            print(f"updated {params['id']}")
        else:
            # concat to experiments
            experiments = pd.concat([experiments, pd.DataFrame(params, index=[0])])
            print(f"added {params['id']}")

# save experiments to csv again
experiments.drop("id", axis=1).to_csv("experiment-tracking/experiment_tracking.csv", sep=";", index=False)
