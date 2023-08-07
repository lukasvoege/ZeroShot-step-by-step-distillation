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

1. Clone this repository

2. Create a virtual environment and activate it (Python 3.8.10)
```bash
python -m venv .venv
```
On Linux
```bash
source thesis-env/bin/activate
```
On Windows
```
.\.venv\Scripts\activate
```

3. Install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
