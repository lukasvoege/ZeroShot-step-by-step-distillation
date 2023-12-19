# Zero-Shot step-by-step Distillation

**Type:** Master's Thesis

**Author:** Lukas Vöge

**1st Examiner:** Prof. Dr.  Lessmann

**2nd Examiner:** Prof. Dr. Akbik

## Table of Content

- [Summary](#summary)
- [Working with the repo](#Working-with-the-repo)
    - [Setup](#Setup)
- [Reproducing results](#Reproducing-results)
    - [Training code](#Training-code)
    - [Evaluation code](#Evaluation-code)
    - [Pretrained models](#Pretrained-models)
- [Results](#Results)
- [Project structure](-Project-structure)

## Summary

(Short summary of motivation, contributions and results)

**Keywords**: NLP, LLMs, Distillation, Finetuning, Chain of Thought Prompting

**Full text**: [include a link that points to the full text of your thesis]
*Remark*: a thesis is about research. We believe in the [open science](https://en.wikipedia.org/wiki/Open_science) paradigm. Research results should be available to the public. Therefore, we expect dissertations to be shared publicly. Preferably, you publish your thesis via the [edoc-server of the Humboldt-Universität zu Berlin](https://edoc-info.hu-berlin.de/de/publizieren/andere). However, other sharing options, which ensure permanent availability, are also possible. <br> Exceptions from the default to share the full text of a thesis require the approval of the thesis supervisor.  

## Overview

This repository contains the code to perform Zero-Shot step-by-step Distillation on top of `distilling-step-by-step` by Hsieh et al. (2023).



## Working with the repo

### Setup

Clone this repository and initialize the submodule
```bash
git clone https://github.com/lukasvoege/ZeroShot-step-by-step-distillation.git
cd ZeroShot-step-by-step-distillation
git submodule update --init
```

Unzip the `datasets.zip` file in the root directory
```bash
# on Linux / Mac / WSL on Windows
unzip datasets.zip

# on Windows
Expand-Archive .\datasets.zip .
```	

Create a virtual environment and activate it (Python 3.8.10)
```bash
python -m venv .venv

# on Linux / Mac / WSL on Windows
source .venv/bin/activate

# on Windows
.\.venv\Scripts\activate
```

Install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` file in the root directory and add the following variable
```.env
OPENAI_API_KEY="your-openai-api-key"
```

### Usage
#### Args usages
 - `--experiment`: run a Prompt experiment
 - `--test_size`: float between `0` and `1` to specify the test set size based on the train set size, or an integer to specify the test set size in absolute numbers
 - `--evaluate`: run prompt evaluation of all query results for a given dataset to update the prompt metadata file
 - `--generate_trainingdata`: generate training data for a given dataset and prompt mix
 - `--subsam_expl_rate`: downsample the explanation rate to a given value between `0` and `1`, musst be smaller than the actual explanation rate of the prompt mix
 - `--splits`: `train`, `valid`, `test`
 - `--prompt_mix`: Integer that refers to a prompt mix yaml in the `./prompt_mixes` directory
 - `--include_prompts`: list of integers that refers to a prompt yaml in the `./prompts` directory, to only include specific prompts in an experiment. All if not specified.
 - `--samples`: Integer, the number of samples to generate
 - `--dataset`: `esnli`, `anli1`, `cqa`, `svamp`
 - `--seed`: random seed to use

 #### Run a Prompt experiment
 The following command runs a Prompt experiment on the CQA dataset with a test set size of 100 samples and a random seed of 42. It will query and evaluate the same 100 random samples for all available prompt templates for the CQA dataset.
 ```bash
python run.py --experiment --dataset cqa --test_size 100 --seed 42
```

#### Run prompt evaluation
The following command runs prompt evaluation on the SVAMP dataset. This will evaluate all available query results across all prompt templates for the SVAMP dataset and update the prompt metadata file `./prompt_metadata/svamp.yaml`.

```bash
python run.py --evaluate --dataset anli1
```

#### Generate training data
The following command generates training data for the CQA dataset using the `2.yaml` prompt mix. It will query the first 500 samples of the train and test split using prompt templates in a mix defined in `./prompt_mixes/2.yaml`. The query results will be parsed and dataset files ready for model finetuning will be saved to `./datasets/esnli/gpt_35_turbo/2/`.

```bash
python run.py --generate_trainingdata --dataset cqa --splits train test --prompt_mix 2 --samples 500
```

To generate the full training testing and evaluation data for the ANLI1 dataset using the `6.yaml` prompt mix and downsample the explanation rate to 0.5, run the following command:

```bash
python run.py --generate_trainingdata --dataset anli1 --splits train test valid --prompt_mix 6 --subsam_expl_rate 0.5
```