from typing import Dict
import yaml
import re
import importlib

dsbs = importlib.import_module("distilling-step-by-step.data_utils")


class ANLITeacherResponseParser():
    def __init__(self):
        self.dataset_name = "anli1"
        self.prompt_templates_folder = "./prompt-templates"
        self.queries_save_folder = "./querie-results"

    def read_yaml_prompts(self, yaml_file: str = None) -> Dict:
        if not yaml_file:
            yaml_file = f"{self.prompt_templates_folder}/{self.dataset_name}.yaml"
        with open(yaml_file, "r") as yf:
            try:
                return yaml.safe_load(yf)
            except yaml.YAMLError as exc:
                print(exc)


    def parse_response(self, response: str, prompt_template_id: int) -> Dict:
        prompt_template = self.read_yaml_prompts()["templates"][prompt_template_id]
        pattern = re.compile(prompt_template["label_parse"] + prompt_template["explanation_parse"], re.IGNORECASE)
        print(pattern)
        match = pattern.search(response)
        print(match)