from typing import Dict, Union
import yaml
import os


class Metadata:
    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name
        self.current_metadata = self.load_current_metadata()

    def load_current_metadata(self) -> Dict:
        yaml_file = f"./prompt-metadata/{self.dataset_name}.yaml"
        if not os.path.exists(yaml_file):
            return {}
        with open(yaml_file, "r") as yf:
            try:
                return yaml.safe_load(yf)
            except yaml.YAMLError as exc:
                print(exc)

    def save_updated_metadata(self, metadata: Dict) -> None:
        yaml_file = f"./prompt-metadata/{self.dataset_name}.yaml"
        with open(yaml_file, "w") as yf:
            try:
                yaml.dump(metadata, yf)
            except yaml.YAMLError as exc:
                print(exc)

    def update_field(self, prompt_id: int, category: str, field: str, value: Union[int, float]) -> None:
        if prompt_id not in self.current_metadata:
            self.current_metadata[prompt_id] = {}
        if category not in self.current_metadata[prompt_id]:
            self.current_metadata[prompt_id][category] = {}
        self.current_metadata[prompt_id][category][field] = (
            self.current_metadata[prompt_id][category].get(field, 0) + value
        )

    def update_from_callback(
        self, prompt_id: int, total_prompt_tokens: int, total_completion_tokens: int, total_costs: float, n: int
    ):
        # update current_metadata
        self.current_metadata = self.load_current_metadata()

        self.update_field(prompt_id, "costs", "total_performed_queries", n)
        self.update_field(prompt_id, "costs", "total_tokens_sent", total_prompt_tokens)
        self.update_field(prompt_id, "costs", "total_tokens_received", total_completion_tokens)
        self.update_field(prompt_id, "costs", "total_accumulated_costs", total_costs)

        # save updated metadata
        self.save_updated_metadata(self.current_metadata)
