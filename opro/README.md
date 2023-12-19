## OPRO

This folder contains code to find optimal prompts for a dataset/task, by using a very recent technique proposed by researchers in a paper called LARGE [LANGUAGE MODELS AS OPTIMIZERS](https://arxiv.org/abs/2309.03409), called OPRO.

Finding an optimal prompt is very difficult because prompts are discrete and the search space is huge. Optimization by PROmpting (OPRO), is a simple and effective approach to leverage large language models (LLMs) as optimizers, where the optimization task is described in natural language. In each optimization step, the LLM generates new solutions from the prompt that contains previously generated solutions with their values, then the new solutions are evaluated and added to the prompt for the next optimization step.

The approach here is largely based on OPRO, but adapted to the nature of the specific task at hand.

### Usage

To run OPRO, run the following command from the root directory of the project:

```bash
python .\opro\opro.py --dataset anli1 --n_prev_best 15 --test_size 25 --iterations 20
```

This will run 20 iterations of OPRO on the ANLI1 dataset, where each round will produce up to 8 new candidate prompts that will be evaluated on a test set of 25 samples. The meta prompt will include the 15 best prompts that have been found so far.