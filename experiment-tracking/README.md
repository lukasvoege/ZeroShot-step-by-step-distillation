## Experiment Tracking

This folder contains the experiment tracking for the experiments conducted for this project. All experiments are defined in `experiment_tracking.csv` by the parameters used to finetune and distill the T5 models. `experiment_tracking.py` can be used to update the tracking file with the results of experiments from the `../results/` directory and to generate bash scripts to run the defined experiments that have not yet been run.

### Experiment Tracking File

Experiments are defined by the exact set of parameters used to finetune and distill the T5 models. The parameters are defined in the following columns, whereas each row represents a single experiment. Not all parameters are used for all experiments, e.g. the `prompt_mix` column is only used for experiments with `gpt35` as the teacher model (`llm`) and a teacher model is itself irrelevant for standard finetuning experiments for example. Parameters that are of no relevance for a specific experiment should be left at their default value or `None` to avoid confusion.

- `dataset`: the dataset to use (`anli1`, `cqa`, `svamp`, `esnli`)
- `model`: the pretrained google/t5-v1_1 model to finetune
- `mode`: `task_prefix` for step-by-step method, else `standard`
- `llm`: the teacher model used for distillation (should be `None` for standard finetuning experiments)
- `subsample`: float between `0` and `1` to subsample the dataset
- `prompt_mix`: the prompt mix used for `llm` labels and potentially explanations (mode: task_prefix) (only relevant if `llm` is `gpt35`, else should be `0`)
- `label_type`: `gt` for ground truth labels (Finetuning), `llm` for teacher model predicted labels (Distillation)

The remaining fields were not changed during the experiments of this project but should be self-explanatory. Refer to to the [README](../distilling-step-by-step/README.md) of the `distilling-step-by-step` submodule also.


### Usage of `experiment_tracking.py`

#### Update Experiment Tracking File

To update the experiment tracking file with the results of experiments from the `../results/` directory, run the following command:

```bash
python ./experiment-tracking/experiment_tracking.py --update_tracking
```
This will update `train_duration`, `train_steps`, `test_acc`, `eval_acc` fields according to the results found in `../results/`. Results that are from experiments that are not defined in `experiment_tracking.csv` will be appended to the file.

#### Generate Bash Scripts

To generate bash scripts to run the defined experiments that have not yet been run (`None` in `train_duration`, `train_steps`, `test_acc` or `eval_acc`), run with the `--generate_missing_experiments_script` parameter and a file name. Filter for any of the aforementioned relevant parameters and/or a custom `experiment_group`.

For example, to generate a bash script, called "anli_modelsize.sh", to run all experiments that have not yet been run with the `experiment_group` "Model Size" and `mode` "standard", run the following command from the root directory of the project:

```bash
python .\experiment-tracking\experiment_tracking.py --generate_missing_experiments anli_modelsize --experiment_group "Model Size" --mode standard
```

To generate a bash script, called "cqa_gpt35.sh", to run all experiments that have not yet been run with the `dataset` "cqa" and `llm` "gpt35", run the following command from the root directory of the project. Arbitrary params can be passed through to the generated commands with the `--passthrough` parameter.

```bash
python .\experiment-tracking\experiment_tracking.py --generate_missing_experiments cqa_gpt35 --dataset cqa --llm gpt35 --passthrough "--parallelize --es_threshold 0.0001 --es_patience 10"
```

Resulting bash scripts will be saved in the `./experiment-tracking/scripts/` directory.