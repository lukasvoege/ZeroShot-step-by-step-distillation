from typing import Dict, List

import os
import json
import numpy as np
from src.factories import teacherResponseParserFactory


class TeacherWriter:
    def __init__(self, dataset_name: str) -> None:
        self.dataset_name = dataset_name
        self.parser = teacherResponseParserFactory(dataset_name)

    # prompt_template_id_mix = {"label": {1: [1, 2, 5], 2: [0, 3, 4]}, "explanation": {1: [0, 1, 2], 2: [3, 4, 5]}}

    def write_teacher_responses(self, split: str, prompt_template_id_mix: Dict[int, List[int]], prompt_mix_id: int, subsam_expl_rate: float = None) -> None:
        all_used_Prompt_ids = set([id for ids in prompt_template_id_mix.values() for id in ids])
        parsed_responses = {id: self.parser.parse_response_batch(split, id) for id in all_used_Prompt_ids}

        # get overall highest value in the dict
        max_idx = max([max(ids[id]) for ids in prompt_template_id_mix.values() for id in ids])

        write_location = f"./datasets/{self.dataset_name}/gpt_35_turbo/{prompt_mix_id}/"
        if not os.path.exists(write_location):
            os.makedirs(write_location)

        to_write = [None for _ in range(max_idx + 1)]
        for i, field in enumerate(["label", "explanation"]):
            for prompt_id, idxs in prompt_template_id_mix[field].items():
                for idx in idxs:
                    if to_write[idx] is None:
                        to_write[idx] = {field: parsed_responses[prompt_id][idx][i]}
                    else:
                        to_write[idx][field] = parsed_responses[prompt_id][idx][i]

        # check if and where there are still None values in the list
        none_idxs = [i for i, x in enumerate(to_write) if x == None]
        if none_idxs:
            raise ValueError(f"No responses given for indices {none_idxs}")
        
        # calculate the explanation rate as (1-None explanations)/len(to_write)
        if split == "train":
            explanation_rate = 1 - sum([1 for x in to_write if x["explanation"] == None]) / len(to_write)
            print(f"Explanation rate in train split: {explanation_rate}")
            if subsam_expl_rate is not None and 0.0 < subsam_expl_rate < 1.0 and subsam_expl_rate < explanation_rate:
                print(f"Subsampling to {subsam_expl_rate} explanation rate.")
                # change random explanations to None to match the desired explanation rate
                for i, x in enumerate(to_write):
                    if x["explanation"] is not None and np.random.random() < subsam_expl_rate * explanation_rate:
                        to_write[i]["explanation"] = None

                # check if the explanation rate is correctly subsampled
                explanation_rate = 1 - sum([1 for x in to_write if x["explanation"] == None]) / len(to_write)
                print(f"NEW Explanation rate in train split: {explanation_rate}")

        with open(f"{write_location}/{split}_CoT.json", "w") as f:
            for line in to_write:
                json.dump(line, f)
                f.write("\n")
