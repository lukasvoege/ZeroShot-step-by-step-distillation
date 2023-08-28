## parsedet und schreibt die teacher responses als liste in eine json datei wie die andern llm responses
## kann split und eine prompt Id oder ein mix an prompt ids kriegen

from typing import Dict, List

import os
import json
from teacher_response_parser import (
    ANLITeacherResponseParser,
    CQATeacherResponseParser,
    ESNLITeacherResponseParser,
    SVAMPTeacherResponseParser,
)


class TeacherWriter:
    def __init__(self, dataset_name: str) -> None:
        self.dataset_name = dataset_name

        if dataset_name == "anli1":
            parser = ANLITeacherResponseParser()
        elif dataset_name == "cqa":
            parser = CQATeacherResponseParser()
        elif dataset_name == "esnli":
            parser = ESNLITeacherResponseParser()
        elif dataset_name == "svamp":
            parser = SVAMPTeacherResponseParser()

        self.parser = parser

    # TODO: add layer to prompt_template_id_mix to specify different templates for label and explanation

    def write_teacher_responses(self, split: str, prompt_template_id_mix: Dict[int, List[int]]) -> None:
        parsed_responses = {id: self.parser.parse_response_batch(split, id) for id in prompt_template_id_mix.keys()}
        # get overall highest value in the dict
        max_idx = max([max(v) for v in prompt_template_id_mix.values()])

        write_location = f"./datasets/{self.dataset_name}/gpt_35_turbo/"
        if not os.path.exists(write_location):
            os.makedirs(write_location)

        to_write = [None for _ in range(max_idx + 1)]
        for prompt_id, idxs in prompt_template_id_mix.items():
            for idx in idxs:
                to_write[idx] = {
                    "label": parsed_responses[prompt_id][idx][0],
                    "explanation": parsed_responses[prompt_id][idx][1],
                }

        # check if and where there are still None values in the list
        none_idxs = [i for i, x in enumerate(to_write) if x == None]
        if none_idxs:
            raise ValueError(f"No responses given for indices {none_idxs}")

        with open(f"{write_location}/{split}_CoT.json", "w") as f:
            for line in to_write:
                json.dump(line, f)
                f.write("\n")
