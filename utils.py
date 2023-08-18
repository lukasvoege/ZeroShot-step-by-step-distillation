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

    def write_filed(self, prompt_id: int, category: str, field: str, value: Union[int, float]) -> None:
        if prompt_id not in self.current_metadata:
            self.current_metadata[prompt_id] = {}
        if category not in self.current_metadata[prompt_id]:
            self.current_metadata[prompt_id][category] = {}
        self.current_metadata[prompt_id][category][field] = value

    def calculate_and_and_update_averages(self, prompt_id: int, category: str) -> None:
        if category == "costs":
            avg_cost_per_query = (
                self.current_metadata[prompt_id][category]["total_accumulated_costs"]
                / self.current_metadata[prompt_id][category]["total_performed_queries"]
            )
            self.write_filed(prompt_id, category, "avg_cost_per_query", avg_cost_per_query)

            avg_nr_tokens_sent = (
                self.current_metadata[prompt_id][category]["total_tokens_sent"]
                / self.current_metadata[prompt_id][category]["total_performed_queries"]
            )
            self.write_filed(prompt_id, category, "avg_nr_tokens_sent", avg_nr_tokens_sent)

            avg_nr_tokens_received = (
                self.current_metadata[prompt_id][category]["total_tokens_received"]
                / self.current_metadata[prompt_id][category]["total_performed_queries"]
            )
            self.write_filed(prompt_id, category, "avg_nr_tokens_received", avg_nr_tokens_received)

        elif category == "characteristics":
            try:
                avg_len_of_explanations = self.current_metadata[prompt_id][category]["total_length_of_explanations"] / (
                    self.current_metadata[prompt_id][category]["total_reponses"]
                )
            except ZeroDivisionError:
                avg_len_of_explanations = 0
            self.write_filed(prompt_id, category, "avg_len_of_explanations", avg_len_of_explanations)

        elif category == "performance":
            accuracy = self.current_metadata[prompt_id][category]["n_correct"] / (
                self.current_metadata[prompt_id][category]["n_correct"]
                + self.current_metadata[prompt_id][category]["n_wrong"]
            )
            self.write_filed(prompt_id, category, "accuracy", accuracy)

    def update_from_callback(
        self, prompt_id: int, total_prompt_tokens: int, total_completion_tokens: int, total_costs: float, n: int
    ):
        # update current_metadata
        self.current_metadata = self.load_current_metadata()

        self.update_field(prompt_id, "costs", "total_performed_queries", n)
        self.update_field(prompt_id, "costs", "total_tokens_sent", total_prompt_tokens)
        self.update_field(prompt_id, "costs", "total_tokens_received", total_completion_tokens)
        self.update_field(prompt_id, "costs", "total_accumulated_costs", total_costs)

        # update averages
        self.calculate_and_and_update_averages(prompt_id, "costs")

        # save updated metadata
        self.save_updated_metadata(self.current_metadata)

    def update_from_evaluator(
        self,
        prompt_id: int,
        total_reponses: float,
        n_none_responses: int,
        total_length_of_explanations: int,
        n_correct: int,
        n_wrong: int,
    ):
        # update current_metadata
        self.current_metadata = self.load_current_metadata()

        self.write_filed(prompt_id, "characteristics", "total_reponses", total_reponses)
        self.write_filed(prompt_id, "characteristics", "n_none_responses", n_none_responses)
        self.write_filed(prompt_id, "characteristics", "total_length_of_explanations", total_length_of_explanations)

        self.update_field(prompt_id, "performance", "n_correct", n_correct)
        self.update_field(prompt_id, "performance", "n_wrong", n_wrong)

        # update averages
        self.calculate_and_and_update_averages(prompt_id, "characteristics")
        self.calculate_and_and_update_averages(prompt_id, "performance")

        # save updated metadata
        self.save_updated_metadata(self.current_metadata)
