## This class needs to load the ground truth data and parse the teacher responses
## to evaluate the teacher responses and update the metadata file accordingly.
from typing import Dict
import numpy as np
import os
from teacher_response_parser import (
    ANLITeacherResponseParser,
    CQATeacherResponseParser,
    ESNLITeacherResponseParser,
    SVAMPTeacherResponseParser,
)
from utils import Metadata

import importlib

dsbs_data_utils = importlib.import_module("distilling-step-by-step.data_utils")
dsbs_metrics = importlib.import_module("distilling-step-by-step.metrics")


class TeacherResponseEvaluator:
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name

        if dataset_name == "anli1":
            dataloader = dsbs_data_utils.ANLI1DatasetLoader()
            parser = ANLITeacherResponseParser()
        elif dataset_name == "cqa":
            dataloader = dsbs_data_utils.CQADatasetLoader()
            parser = CQATeacherResponseParser()
        elif dataset_name == "esnli":
            dataloader = dsbs_data_utils.ESNLIDatasetLoader()
            parser = ESNLITeacherResponseParser()
        elif dataset_name == "svamp":
            dataloader = dsbs_data_utils.SVAMPDatasetLoader()
            parser = SVAMPTeacherResponseParser()

        self.ground_truth = dataloader.load_from_json()
        self.parser = parser
        self.metadata = Metadata(dataset_name)

    def get_label_accuracy(self, split: str, parsed_responses: Dict) -> float:
        response_labels = [response[0] for response in parsed_responses.values()]
        ground_truth_labels = self.ground_truth[split]["label"]

        ground_truth_labels = np.take(ground_truth_labels, [idx for idx in parsed_responses.keys()])

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

    def get_explanation_characteristics(self, split: str, parsed_responses: Dict) -> [int, int]:
        response_explanations = [response[1] for response in parsed_responses.values()]

        n_none_responses = response_explanations.count(None)
        total_repsonses = len(response_explanations) - n_none_responses
        total_length_of_explanations = sum(
            [len(explanation) for explanation in response_explanations if explanation is not None]
        )

        ## TODO: Add more explanation characteristics like coherence and fluency

        return n_none_responses, total_repsonses, total_length_of_explanations

    def evaluate_responses_split(self, split: str, prompt_template_id: int) -> Dict:
        parsed_responses = self.parser.parse_response_batch(split, prompt_template_id)
        if parsed_responses == {}:
            return {}
        acc, n_correct, n_wrong = self.get_label_accuracy(split, parsed_responses)
        n_none_responses, total_repsonses, total_length_of_explanations = self.get_explanation_characteristics(
            split, parsed_responses
        )

        return {
            "accuracy": acc,
            "n_correct": n_correct,
            "n_wrong": n_wrong,
            "n_none_responses": n_none_responses,
            "total_reponses": total_repsonses,
            "total_length_of_explanations": total_length_of_explanations,
        }

    def evaluate_train(self) -> None:
        evals = {}
        split = "train"
        for prompt_template_id in os.listdir(f"./querie-results/{self.dataset_name}/{split}/"):
            # evaluate the responses and update the metadata file
            evaluation_results = self.evaluate_responses_split(split, int(prompt_template_id))
            if evaluation_results == {}:  # no responses found for this prompt template
                continue
            self.metadata.update_from_evaluator(
                int(prompt_template_id),
                evaluation_results["total_reponses"],
                evaluation_results["n_none_responses"],
                evaluation_results["total_length_of_explanations"],
                evaluation_results["n_correct"],
                evaluation_results["n_wrong"],
            )
            evals[prompt_template_id] = evaluation_results

        best_prompt_template_id = max(evals, key=lambda x: evals[x]["accuracy"])

        print(f"Best prompt template for {self.dataset_name} is {best_prompt_template_id}, with accuracy: {evals[best_prompt_template_id]['accuracy']}")
