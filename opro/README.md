## OPRO

This folder contains code to find optimal prompts for a dataset/task, by using a very recent technique proposed by researchers in a paper called LARGE [LANGUAGE MODELS AS OPTIMIZERS](https://arxiv.org/abs/2309.03409), called OPRO.

Finding an optimal prompt is very difficult, because prompts are discrete and the search space is huge. Optimization by PROmpting
(OPRO), is a simple and effective approach to leverage large language models (LLMs) as optimizers, where the optimization task is described in natural language. In each optimization step, the LLM generates new solutions from the prompt that contains previously generated solutions with their values, then the new solutions are evaluated and added to the prompt for the next optimization step.

The approach here is largly based on OPRO, but adapted to the nature of the specifc task at hand.