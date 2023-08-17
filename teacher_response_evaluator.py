## This class needs to load the ground truth data and parse the teacher responses
## to evaluate the teacher responses and update the metadata file accordingly.
from typing import Dict
import numpy as np
from teacher_response_parser import ANLITeacherResponseParser, CQATeacherResponseParser, ESNLITeacherResponseParser, SVAMPTeacherResponseParser

import importlib

dsbs_data_utils = importlib.import_module("distilling-step-by-step.data_utils")
dsbs_metrics = importlib.import_module("distilling-step-by-step.metrics")


class TeacherResponseEvaluator():
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

    def get_label_accuracy(self, split: str, parsed_responses: Dict) -> float: 
        response_labels = [response[0] for response in parsed_responses.values()]
        ground_truth_labels = self.ground_truth[split]["label"]

        ground_truth_labels = np.take(ground_truth_labels, [idx for idx in parsed_responses.keys()]) 

        if self.dataset_name in ["anli1", "esnli", "cqa"]:
            acc = dsbs_metrics.compute_text_acc(response_labels, ground_truth_labels)
        elif self.dataset_name in ["svamp"]:
            acc = dsbs_metrics.compute_equation_acc(response_labels, ground_truth_labels)

        return acc
    
    def get_explanation_characteristics(self, split: str, parsed_responses: Dict) -> [int, int]:
        response_explanations = [response[1] for response in parsed_responses.values()]

        n_none_responses = response_explanations.count(None)
        total_repsonses = len(response_explanations)
        total_length_of_explanations = sum([len(explanation) for explanation in response_explanations if explanation is not None])

        ## TODO: Add more explanation characteristics like coherence and fluency

        return n_none_responses, total_repsonses, total_length_of_explanations

    def evaluate_responses(self, split: str, prompt_template_id: int) -> Dict:
        parsed_responses = self.parser.parse_response_batch(split, prompt_template_id)

        label_acc = self.get_label_accuracy(split, parsed_responses)
        explanation_characteristics = self.get_explanation_characteristics(split, parsed_responses)


        
        

