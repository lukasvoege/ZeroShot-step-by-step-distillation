# %%
import pandas as pd
import os
import json

# dataset | from_pretrained | model_type | llm | subsample | prompt_mix | label_type | alpha | max_input_length | grad_steps*args.batch_size | optimizer_name | lr | run'

# Read csv and have all dtypes as object
experiments = pd.read_csv("experiment_tracking.csv", sep=";", dtype=object)
# replace nan with "None"
experiments = experiments.fillna("None")

# %%
def get_params_from_path(path: str):
    params = {}
    path = os.path.normpath(path)
    split = path.split(os.path.sep)
    params["dataset"] = split[2]
    params["model"] = split[3]
    params["mode"] = split[4]
    params["llm"] = split[5]
    params["subsample"] = split[6]
    params["prompt_mix"] = split[7]
    params["label_type"] = split[8]
    params["alpha"] = split[9]
    params["max_input_length"] = split[10]
    params["batch_size"] = split[11]
    params["optimizer"] = split[12]
    params["lr"] = split[13]
    params["run"] = split[14]

    params["id"] = get_identifier(params)

    category = "step-by-step " if params["mode"] == "task_prefix" else "standard "
    category += "distillation" if params["label_type"] == "llm" else "finetuning"
    params["category"] = category

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

# %%

for root, dirs, files in os.walk("../results"):
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

# %%
