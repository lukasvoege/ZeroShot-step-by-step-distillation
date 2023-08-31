# Zero-Shot step-by-step Distillation

**Type:** Master's Thesis

**Author:** Lukas Vöge

**1st Examiner:** Prof. Dr. Stefan Lessmann

**2nd Examiner:** KP 

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

## Working with the repo

### Setup

Clone this repository and initialize the submodule
```bash
git clone .
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
 - `--dataset`: `esnli`, `anli1`, `cqa`, `svamp`
 - `--test_size`: float between 0 and 1 to specify the test set size based on the train set size, or an integer to specify the test set size in absolute numbers
 - `--seed`: random seed to use

 #### Run a Prompt experiment
 The following command runs a Prompt experiment on the CQA dataset with a test set size of 100 samples and a random seed of 42. It will query and evaluate the same 100 random samples for all available prompt templates for the CQA dataset.
 ```bash
python run.py --experiment --dataset cqa --test_size 100 --seed 42
```