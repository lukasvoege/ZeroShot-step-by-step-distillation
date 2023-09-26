## This class needs to load the ground truth data and parse the teacher responses
## to evaluate the teacher responses and update the metadata file accordingly.
from typing import Dict, List
import numpy as np
import os
from src.factories import teacherResponseParserFactory, dataLoaderFactory
from src.metadata import Metadata

from readability import Readability
from readability.exceptions import ReadabilityException

import importlib

dsbs_metrics = importlib.import_module("distilling-step-by-step.metrics")


class TeacherResponseEvaluator:
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name

        dataloader = dataLoaderFactory(dataset_name)
        self.ground_truth = dataloader.load_from_json()
        self.parser = teacherResponseParserFactory(dataset_name)
        self.metadata = Metadata(dataset_name)

    def get_label_accuracy(self, split: str, parsed_responses: Dict) -> float:
        response_labels = [response[0] for response in parsed_responses.values()]
        ground_truth_labels = self.ground_truth[split]["label"]

        ground_truth_labels = np.take(ground_truth_labels, list(parsed_responses.keys()))

        if self.dataset_name in ["svamp"]:
            response_labels = [dsbs_metrics.eval_equation(response_label) for response_label in response_labels]
            ground_truth_labels = [
                dsbs_metrics.eval_equation(ground_truth_label) for ground_truth_label in ground_truth_labels
            ]

        n_correct = sum(
            [
                1
                for response_label, ground_truth_label in zip(response_labels, ground_truth_labels)
                if response_label == ground_truth_label
            ]
        )
        n_wrong = len(response_labels) - n_correct
        acc = n_correct / (n_correct + n_wrong)

        return acc, n_correct, n_wrong

    def get_explanation_characteristics(self, parsed_responses: Dict) -> [int, int]:
        response_explanations = [response[1] for response in parsed_responses.values()]

        n_none_responses = response_explanations.count(None)
        total_repsonses = len(response_explanations) - n_none_responses

        # number of sentences
        total_number_of_sentences = sum(
            [len(explanation.split(". ")) for explanation in response_explanations if explanation is not None]
        )
        # number of words
        total_number_of_words = sum(
            [len(explanation.split()) for explanation in response_explanations if explanation is not None]
        )
        # number of characters
        total_length_of_explanations = sum(
            [len(explanation) for explanation in response_explanations if explanation is not None]
        )

        # Flesch reading ease of all explanations combined
        readability = Readability(
            " ".join([explanation for explanation in response_explanations if explanation is not None])
        )
        try:
            flesch_reading_ease = readability.flesch().score
        except ReadabilityException:
            flesch_reading_ease = 0

        return (
            n_none_responses,
            total_repsonses,
            total_length_of_explanations,
            total_number_of_sentences,
            total_number_of_words,
            flesch_reading_ease,
        )

    def evaluate_responses_split(
        self, split: str, prompt_template_id: int, idxs: List = None, verbose: bool = False
    ) -> Dict:
        parsed_responses = self.parser.parse_response_batch(split, prompt_template_id, verbose=verbose)
        # filter for idxs if provided
        if idxs:
            parsed_responses = {idx: parsed_responses[idx] for idx in idxs if idx in parsed_responses}
        if parsed_responses == {}:
            return {}
        n_parse_errors = [response[0] for response in parsed_responses.values()].count(None)
        acc, n_correct, n_wrong = self.get_label_accuracy(split, parsed_responses)
        (
            n_none_responses,
            total_repsonses,
            total_length_of_explanations,
            total_number_of_sentences,
            total_number_of_words,
            flesch_reading_ease,
        ) = self.get_explanation_characteristics(parsed_responses)

        return {
            "accuracy": acc,
            "n_correct": n_correct,
            "n_wrong": n_wrong,
            "n_parse_errors": n_parse_errors,
            "n_none_responses": n_none_responses,
            "total_responses": total_repsonses,
            "total_length_of_explanations": total_length_of_explanations,
            "total_number_of_sentences": total_number_of_sentences,
            "total_number_of_words": total_number_of_words,
            "flesch_reading_ease": flesch_reading_ease,
        }

    def evaluate_train(self, idxs: List = None, verbose: bool = False) -> int:
        evals = {}
        split = "train"
        for prompt_template_id in os.listdir(f"./querie-results/{self.dataset_name}/{split}/"):
            # evaluate the responses and update the metadata file
            evaluation_results = self.evaluate_responses_split(
                split, int(prompt_template_id), idxs=idxs, verbose=verbose
            )
            # dont update if no responses were found for this prompt template or we are only evaluating a subset of the data
            if evaluation_results == {}:
                continue
            if not idxs:
                self.metadata.update_from_evaluator(
                    int(prompt_template_id),
                    evaluation_results["total_responses"],
                    evaluation_results["n_none_responses"],
                    evaluation_results["total_length_of_explanations"],
                    evaluation_results["n_correct"],
                    evaluation_results["n_wrong"],
                    evaluation_results["n_parse_errors"],
                    evaluation_results["total_number_of_sentences"],
                    evaluation_results["total_number_of_words"],
                    evaluation_results["flesch_reading_ease"],
                )
            evals[prompt_template_id] = evaluation_results

        best_prompt_template_id = max(evals, key=lambda x: evals[x]["accuracy"])

        print(
            f"Best prompt template for {self.dataset_name} is {best_prompt_template_id}, with accuracy: {evals[best_prompt_template_id]['accuracy']}"
        )

        return best_prompt_template_id
