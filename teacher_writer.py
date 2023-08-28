## parsedet und schreibt die teacher responses als liste in eine json datei wie die andern llm responses
## kann split und eine prompt Id oder ein mix an prompt ids kriegen

from typing import Dict

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

    def write_teacher_responses(self, split: str, prompt_template_id_mix: Dict, n: int = None) -> None:
        parsed_responses = {id: self.parser.parse_response_batch(split, id) for id in prompt_template_id_mix.keys()}

        write_location = f"./datasets/{self.dataset_name}/gpt_35_turbo/"
        if not os.path.exists(write_location):
            os.makedirs(write_location)

        """
        to_write = []
        for idx in range(n):
            to_write.append({"label": teacher_responses[idx][0], "explanation": teacher_responses[idx][1]})
        with open(f"{write_location}/{split}_CoT.json", "w") as f:
            json.dump(to_write, f)
        """
        return parsed_responses
