from typing import List, Dict, Union, Tuple
import datetime
import json
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback, OpenAICallbackHandler
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessage,
    SystemMessagePromptTemplate,
    HumanMessage,
    HumanMessagePromptTemplate,
)
import yaml
from datasets import load_dataset, DatasetDict

from dotenv import load_dotenv

load_dotenv()


class TeacherQuerier:
    def __init__(self, chat_model: str, dataset_name: str, has_valid: bool):
        self.chat_model = ChatOpenAI(model=chat_model)
        self.prompt_templates_folder = "./prompt-templates"
        self.dataset_folder = "../data/dsbs-datasets/datasets"
        self.queries_save_folder = "./querie-results"

        self.dataset_name = dataset_name
        self.has_valid = has_valid

        self.datasets = self.load_data_from_json()

    def load_data_from_json(self) -> DatasetDict:
        data_files = {
            "train": f"{self.dataset_folder}/{self.dataset_name}/{self.dataset_name}_train.json",
            "test": f"{self.dataset_folder}/{self.dataset_name}/{self.dataset_name}_test.json",
        }

        if self.has_valid:
            data_files.update({"valid": f"{self.dataset_folder}/{self.dataset_name}/{self.dataset_name}_valid.json"})

        datasets = load_dataset("json", data_files=data_files)
        datasets = self._post_process_data(datasets)

        return datasets

    def read_yaml_prompts(self, yaml_file: str = None) -> Dict:
        if not yaml_file:
            yaml_file = f"{self.prompt_templates_folder}/{self.dataset_name}.yaml"
        with open(yaml_file, "r") as yf:
            try:
                return yaml.safe_load(yf)
            except yaml.YAMLError as exc:
                print(exc)

    def save_querie_results(
        self,
        queries: List[Dict[str, Union[str, int]]],
        split: str,
        prompt_template_id: int,
        save_location: str = None,
        save_name: str = None,
    ) -> None:
        if save_location is None:
            save_location = f"{self.queries_save_folder}/{self.dataset_name}/{split}/{prompt_template_id}"

        if not os.path.exists(save_location):
            os.makedirs(save_location)

        if save_name == "timestamp":
            save_name = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        else:
            save_name = f"responses.json"

        with open(f"{save_location}/{save_name}", "a") as f:
            for query in queries:
                json.dump(query, f)
                f.write("\n")

    def show_example(self, split: str = "train", idx: int = 0) -> None:
        print(self.datasets[split][idx])

    def build_chain_from_prompt_template(self, prompt_template_id: int) -> LLMChain:
        prompt_template = self.read_yaml_prompts()["templates"][prompt_template_id]

        system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template["system_message"])
        human_message_prompt = HumanMessagePromptTemplate.from_template(prompt_template["user_message"])
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

        chain = LLMChain(llm=self.chat_model, prompt=chat_prompt)

        return chain

    def stringify_prompt(self, formatted_chat_prompt: List[Union[SystemMessage, HumanMessage]]) -> str:
        return f"{formatted_chat_prompt[0].content}\n{formatted_chat_prompt[1].content}"

    def run_chain_with_callback(
        self, chain: LLMChain, template_args: Dict[str, str]
    ) -> Tuple[str, OpenAICallbackHandler]:
        with get_openai_callback() as callback:
            response = chain.run(template_args)
        return response, callback

    def calculate_batch_query_metrics(self, callbacks: List[OpenAICallbackHandler]) -> Tuple[int, int, float]:
        total_prompt_tokens = sum([callback.prompt_tokens for callback in callbacks])
        total_completion_tokens = sum([callback.completion_tokens for callback in callbacks])
        total_costs = sum([callback.total_cost for callback in callbacks])

        return total_prompt_tokens, total_completion_tokens, total_costs

    def get_already_stored_results(self, split: str, prompt_template_id: int) -> set:
        stored_results = set()
        save_location = f"{self.queries_save_folder}/{self.dataset_name}/{split}/{prompt_template_id}"

        if os.path.exists(f"{save_location}/responses.json"):
            with open(f"{save_location}/responses.json", "r") as f:
                saved_results = [json.loads(line) for line in f]
            for result in saved_results:
                stored_results.add(f"{result['split']}_{result['idx']}_{result['prompt_template_id']}")

        return stored_results

    def batch_query(
        self,
        split: str,
        n: int,
        prompt_template_id: int,
        template_tuple: List[Tuple[str, str]],
        dont_save: bool = False,
        force_query: bool = False,
    ) -> None:
        if n > 100:
            n = 10

        # build prompt template and chain
        chain = self.build_chain_from_prompt_template(prompt_template_id)

        # get examples from dataset split
        examples = self.datasets[split].select(range(n))
        responses = []
        callbacks = []

        # get already stored results
        stored_results = self.get_already_stored_results(split, prompt_template_id)
        skipped = []
        for idx, example in enumerate(examples):
            if f"{split}_{idx}_{prompt_template_id}" not in stored_results or force_query:
                print(f"QUERYING EXAMPLE {idx + 1}/{n}...", end="\r")
                response, callback = self.run_chain_with_callback(
                    chain,
                    {tup[0]: example[tup[1]] for tup in template_tuple}
                    # chain, {"premise": example["premise"], "hypothesis": example["hypothesis"]}
                )
                responses.append(response)
                callbacks.append(callback)
            else:
                print(f"SKIPPING EXAMPLE {idx + 1}/{n}...", end="\r")
                responses.append(None)  # to keep the same length as examples
                skipped.append(idx)
        print(f"QUERYING EXAMPLE {n}/{n}...")

        # save results
        if not dont_save and len(responses) > 0:
            self.save_querie_results(
                queries=[
                    {
                        "split": split,
                        "idx": idx,
                        "prompt_template_id": prompt_template_id,
                        "complete_prompt": self.stringify_prompt(
                            chain.prompt.format_messages(**{tup[0]: example[tup[1]] for tup in template_tuple})
                        ),
                        "response": responses[idx],
                    }
                    for idx, example in enumerate(examples)
                    if idx not in skipped
                ],
                split=split,
                prompt_template_id=prompt_template_id,
            )

        total_prompt_tokens, total_completion_tokens, total_costs = self.calculate_batch_query_metrics(callbacks)
        print(
            f"Batch Query completed! (Skipped {len(skipped)} queries as they were already queried and stored.)\nTotal Prompt Tokens: {total_prompt_tokens}\nTotal Completion Tokens: {total_completion_tokens}\nTotal Costs: ${total_costs}"
        )

    def query(
        self,
        split: str,
        idx: int,
        prompt_template_id: int,
        template_tuple: List[Tuple[str, str]],
        dont_save: bool = False,
    ) -> None:
        # build prompt template and chain
        chain = self.build_chain_from_prompt_template(prompt_template_id)

        # get example from dataset split
        example = self.datasets[split][idx]
        print(
            self.stringify_prompt(chain.prompt.format_messages(**{tup[0]: example[tup[1]] for tup in template_tuple}))
        )
        response = chain.run({tup[0]: example[tup[1]] for tup in template_tuple})
        print(f"RESPONSE:\n{response}")

        # save results
        if not dont_save:
            self.save_querie_results(
                queries=[
                    {
                        "split": split,
                        "idx": idx,
                        "prompt_template_id": prompt_template_id,
                        "complete_prompt": self.stringify_prompt(
                            chain.prompt.format_messages(**{tup[0]: example[tup[1]] for tup in template_tuple})
                        ),
                        "response": response,
                    }
                ],
                split=split,
                prompt_template_id=prompt_template_id,
            )

    def _batch_query(
        self, split: str, n: int, prompt_template_id: int, dont_save: bool = False, force_query: bool = False
    ) -> None:
        raise NotImplementedError

    def _query(self, split: str, prompt_template_id: int, dont_save: bool = False) -> None:
        raise NotImplementedError

    def _post_process_data(self, datasets) -> DatasetDict:
        raise NotImplementedError


class ANLITeacherQuerier(TeacherQuerier):
    def __init__(self, chat_model: str = "gpt-3.5-turbo"):
        dataset_name = "anli1"
        has_valid = True
        super().__init__(chat_model, dataset_name, has_valid)

    def _batch_query(
        self, split: str, n: int, prompt_template_id: int, dont_save: bool = False, force_query: bool = False
    ) -> None:
        template_tuple = [("premise", "premise"), ("hypothesis", "hypothesis")]
        self.batch_query(split, n, prompt_template_id, template_tuple, dont_save, force_query)

    def _query(self, split: str, idx: int, prompt_template_id: int, dont_save: bool = False) -> None:
        template_tuple = [("premise", "premise"), ("hypothesis", "hypothesis")]
        self.query(split, idx, prompt_template_id, template_tuple, dont_save)

    def _post_process_data(self, datasets) -> DatasetDict:
        def label_idx2text(example):
            if example["label"] == 0:
                example["label"] = "entailment"
            elif example["label"] == 1:
                example["label"] = "neutral"
            elif example["label"] == 2:
                example["label"] = "contradiction"
            return example

        datasets = datasets.map(label_idx2text)
        datasets = datasets.remove_columns(["reason"])

        return datasets


class CQATeacherQuerier(TeacherQuerier):
    def __init__(self, chat_model: str = "gpt-3.5-turbo"):
        dataset_name = "cqa"
        has_valid = False
        super().__init__(chat_model, dataset_name, has_valid)

    def _batch_query(
        self, split: str, n: int, prompt_template_id: int, dont_save: bool = False, force_query: bool = False
    ) -> None:
        template_tuple = [
            ("question", "question"),
            ("choice_a", "c_0"),
            ("choice_b", "c_1"),
            ("choice_c", "c_2"),
            ("choice_d", "c_3"),
            ("choice_e", "c_4"),
        ]
        self.batch_query(split, n, prompt_template_id, template_tuple, dont_save, force_query)

    def _query(self, split: str, idx: int, prompt_template_id: int, dont_save: bool = False) -> None:
        template_tuple = [
            ("question", "question"),
            ("choice_a", "c_0"),
            ("choice_b", "c_1"),
            ("choice_c", "c_2"),
            ("choice_d", "c_3"),
            ("choice_e", "c_4"),
        ]
        self.query(split, idx, prompt_template_id, template_tuple, dont_save)

    def _post_process_data(self, datasets):
        def prepare_input(example):
            example["c_0"] = example["choices"][0]
            example["c_1"] = example["choices"][1]
            example["c_2"] = example["choices"][2]
            example["c_3"] = example["choices"][3]
            example["c_4"] = example["choices"][4]

            return example

        datasets = datasets.map(prepare_input)
        datasets = datasets.remove_columns(["abstractive_explanation", "extractive_explanation"])

        return datasets


class ESNLITeacherQuerier(TeacherQuerier):
    def __init__(self, chat_model: str = "gpt-3.5-turbo"):
        dataset_name = "esnli"
        has_valid = True
        super().__init__(chat_model, dataset_name, has_valid)

    def _batch_query(
        self, split: str, n: int, prompt_template_id: int, dont_save: bool = False, force_query: bool = False
    ) -> None:
        template_tuple = [("premise", "premise"), ("hypothesis", "hypothesis")]
        self.batch_query(split, n, prompt_template_id, template_tuple, dont_save, force_query)

    def _query(self, split: str, idx: int, prompt_template_id: int, dont_save: bool = False) -> None:
        template_tuple = [("premise", "premise"), ("hypothesis", "hypothesis")]
        self.query(split, idx, prompt_template_id, template_tuple, dont_save)

    def _post_process_data(self, datasets):
        def label_idx2text(example):
            if example["label"] == 0:
                example["label"] = "entailment"
            elif example["label"] == 1:
                example["label"] = "neutral"
            elif example["label"] == 2:
                example["label"] = "contradiction"

            return example

        datasets = datasets.map(label_idx2text)
        datasets = datasets.remove_columns(["explanation_1", "explanation_2", "explanation_3"])

        return datasets


class SVAMPTeacherQuerier(TeacherQuerier):
    def __init__(self, chat_model: str = "gpt-3.5-turbo"):
        dataset_name = "svamp"
        has_valid = False
        super().__init__(chat_model, dataset_name, has_valid)

    def _batch_query(
        self, split: str, n: int, prompt_template_id: int, dont_save: bool = False, force_query: bool = False
    ) -> None:
        template_tuple = [("question", "input")]
        self.batch_query(split, n, prompt_template_id, template_tuple, dont_save, force_query)

    def _query(self, split: str, idx: int, prompt_template_id: int, dont_save: bool = False) -> None:
        template_tuple = [("question", "input")]
        self.query(split, idx, prompt_template_id, template_tuple, dont_save)

    def _post_process_data(self, datasets):
        return datasets
