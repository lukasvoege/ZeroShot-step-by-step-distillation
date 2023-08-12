from typing import Dict, Tuple
import yaml
import json
import re
import importlib

dsbs = importlib.import_module("distilling-step-by-step.data_utils")


class ANLITeacherResponseParser:
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

    def clean_explanation(self, explanation: str) -> str:
        explanation = re.sub(r"explanation[\.:\-,\s]*", "", explanation, flags=re.IGNORECASE)
        explanation = re.sub(r"^[^\w]+", "", explanation) # remove leading non-word characters like .,;:- etc.
        explanation = re.sub(r"\s+", " ", explanation)
        explanation = explanation.strip()
        ## vllt noch pruning wenn hier so arschlange erklärungen kommen
        return explanation

    def get_pattern_from_template(self, prompt_template_id: int) -> re.Pattern:
        prompt_template = self.read_yaml_prompts()["templates"][prompt_template_id]
        pattern = re.compile(
            prompt_template["label_parse"] + prompt_template["explanation_parse"], re.IGNORECASE | re.DOTALL
        )
        return pattern

    def parse_response_batch(self, split: str, prompt_template_id: int) -> Dict[int, Tuple[str, str]]:
        pattern = self.get_pattern_from_template(prompt_template_id)
        parsed_responses = {}
        with open(
            f"{self.queries_save_folder}/{self.dataset_name}/{split}/{prompt_template_id}/responses.json", "r"
        ) as f:
            for line in f:
                response = json.loads(line)
                if response["idx"] not in parsed_responses:
                    parsed_responses[response["idx"]] = self.parse_response(response["response"], pattern=pattern)

        return parsed_responses

    def parse_response(
        self, response: str, prompt_template_id: int = None, pattern: re.Pattern = None
    ) -> Tuple[str, str]:
        if not pattern:
            pattern = self.get_pattern_from_template(prompt_template_id)
        match = pattern.search(response)

        label = None
        explanation = None
        if match:
            try:
                label = match.group(1)
                explanation = match.group(2)
                ## Clean up
                label = label.lower().strip()
                explanation = self.clean_explanation(explanation)
            except IndexError:
                print(f"Could not fully parse '{response}' with pattern '{pattern}'")
        else:
            print(f"Could not parse '{response}' with pattern '{pattern}'")

        return label, explanation
