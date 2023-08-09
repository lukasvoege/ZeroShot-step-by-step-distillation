from typing import Dict
import importlib

dsbs = importlib.import_module("distilling-step-by-step.data_utils")

dataloader = dsbs.ANLI1DatasetLoader()


datasets = dataloader.load_from_json()


class TeacherResponseParser():
    def __init__(self, dataset_name: str, ):
        self.dataset_name = dataset_name


    def parse_response(self, response: str, prompt_template_id: int) -> Dict:
        raise NotImplementedError