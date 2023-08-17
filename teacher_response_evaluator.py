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

        self.ground_truth = dataloader.load_from_json(dataset_name)
        self.parser = parser


    def evaluate_responses(self, split: str, prompt_template_id: int) -> Dict:
        parsed_responses = self.parser.parse_response_batch(split, prompt_template_id)
        response_labels = [response[0] for response in parsed_responses.values()]
        ground_truth_labels = self.ground_truth[split]["label"]

        ground_truth_labels = np.take(ground_truth_labels, [idx for idx in parsed_responses.keys()])

        if self.dataset_name in ["anli1", "esnli", "cqa"]:
            acc = dsbs_metrics.compute_text_acc(response_labels, ground_truth_labels)
        elif self.dataset_name in ["svamp"]:
            acc = dsbs_metrics.compute_equation_acc(response_labels, ground_truth_labels)

        return acc


        
        

