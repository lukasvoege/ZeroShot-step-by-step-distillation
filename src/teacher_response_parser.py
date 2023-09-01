from typing import Dict, Tuple
import yaml
import json
import re

from src.utils import read_yaml

class TeacherResponseParser:
    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name
        self.prompt_templates_folder = "./prompt-templates"
        self.queries_save_folder = "./querie-results"
        self.yaml_prompts = read_yaml(f"{self.prompt_templates_folder}/{self.dataset_name}.yaml")

    def clean_explanation(self, explanation: str) -> str:
        explanation = re.sub(r"explanation[\.:\-,\s]*", "", explanation, flags=re.IGNORECASE)
        explanation = re.sub(r"\. Answer[\.:\-,\s]*", "", explanation)
        explanation = re.sub(r"^[^\w]+", "", explanation)  # remove leading non-word characters like .,;:- etc.
        explanation = re.sub(r"<<(.+)>>\d+", r"\1", explanation)  # remove math expression formatting
        explanation = re.sub(r"\\+\w+{|}", "", explanation, flags=re.IGNORECASE)  # remove math expression formatting
        explanation = re.sub(r"\s+", " ", explanation)
        explanation = explanation.strip()
        ## vllt noch pruning wenn hier so arschlange erklärungen kommen
        if len(explanation.split()) < 6:
            explanation = None
        return explanation

    def get_pattern_from_template(self, prompt_template_id: int, prompt_values: Dict = None) -> re.Pattern:
        prompt_template = self.yaml_prompts["templates"][prompt_template_id]
        parse_pattern = prompt_template["label_parse"] + prompt_template["explanation_parse"]
        if prompt_values:
            parse_pattern = parse_pattern.format(**prompt_values)
        pattern = re.compile(parse_pattern, re.IGNORECASE | re.DOTALL)
        return pattern

    def parse_response_batch(self, split: str, prompt_template_id: int) -> Dict[int, Tuple[str, str]]:
        yaml_file = f"{self.prompt_templates_folder}/{self.dataset_name}.yaml"
        self.yaml_prompts = read_yaml(yaml_file)  # reload yaml prompts in case they were changed
        parsed_responses = {}
        try:
            with open(
                f"{self.queries_save_folder}/{self.dataset_name}/{split}/{prompt_template_id}/responses.json", "r"
            ) as f:
                for line in f:
                    response = json.loads(line)
                    if response["idx"] not in parsed_responses:
                        pattern = self.get_pattern_from_template(prompt_template_id, response["prompt_values"])
                        parsed_responses[response["idx"]] = self.parse_response(response["response"], pattern=pattern)
        except FileNotFoundError:
            print(f"No responses found for prompt template {prompt_template_id} in split {split}")

        return parsed_responses

    def parse_response(
        self, response: str, prompt_template_id: int = None, pattern: re.Pattern = None
    ) -> Tuple[str, str]:
        if not pattern:
            pattern = self.get_pattern_from_template(prompt_template_id)
        match = pattern.search(response)

        label = None
        explanation = None
        try:
            if len(match.groups()) > 0:
                label = match.group(1)
                label = self.conform_label(label)
            if len(match.groups()) > 1:
                explanation = match.group(2)
                explanation = self.clean_explanation(explanation)
        except (IndexError, AttributeError):
            print(f"Could not parse '{response}' with pattern '{pattern}'")

        return label, explanation


class ANLITeacherResponseParser(TeacherResponseParser):
    def __init__(
        self,
    ):
        dataset_name = "anli1"
        super().__init__(dataset_name)

    def conform_label(self, label: str) -> str:
        label = label.lower().strip()
        if label in ["contradiction", "false"]:
            label = "contradiction"
        elif label in ["neutral", "inconclusive"]:
            label = "neutral"
        elif label in ["entailment", "true"]:
            label = "entailment"
        return label


class CQATeacherResponseParser(TeacherResponseParser):
    def __init__(
        self,
    ):
        dataset_name = "cqa"
        super().__init__(dataset_name)

    def conform_label(self, label: str) -> str:
        return label.lower().strip()


class ESNLITeacherResponseParser(TeacherResponseParser):
    def __init__(
        self,
    ):
        dataset_name = "esnli"
        super().__init__(dataset_name)

    def conform_label(self, label: str) -> str:
        label = label.lower().strip()
        if label in ["contradiction", "false"]:
            label = "contradiction"
        elif label in ["neutral", "inconclusive"]:
            label = "neutral"
        elif label in ["entailment", "true"]:
            label = "entailment"
        return label


class SVAMPTeacherResponseParser(TeacherResponseParser):
    def __init__(
        self,
    ):
        dataset_name = "svamp"
        super().__init__(dataset_name)

    def conform_label(self, label: str) -> str:
        return label.lower().strip()

    def get_pattern_from_template(self, prompt_template_id: int, prompt_values: Dict = None) -> re.Pattern:
        prompt_template = self.yaml_prompts["templates"][prompt_template_id]
        parse_pattern = prompt_template["explanation_parse"] + prompt_template["label_parse"]
        if prompt_values:
            pass  # Prompt values are not used for SVAMP
        pattern = re.compile(parse_pattern, re.IGNORECASE | re.DOTALL)
        return pattern

    def parse_response(
        self, response: str, prompt_template_id: int = None, pattern: re.Pattern = None
    ) -> Tuple[str, str]:
        if not pattern:
            pattern = self.get_pattern_from_template(prompt_template_id)
        match = pattern.search(response)

        label = None
        explanation = None
        try:
            if len(match.groups()) > 0:
                explanation = match.group(1)
                explanation = self.clean_explanation(explanation)
            if len(match.groups()) > 1:
                label = match.group(2)
                label = self.conform_label(label)
        except (IndexError, AttributeError):
            print(f"Could not parse '{response}' with pattern '{pattern}'")

        return label, explanation
