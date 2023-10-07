from typing import Dict
import yaml

def add_prompt_to_yaml(yaml_file: str, prompt: str, label_parse: str, expl_parse: str) -> None:
    highest_id = max(read_yaml(yaml_file)["templates"].keys())

    append = f"\n\n  {highest_id+1}:\n    id: {highest_id+1}\n    system_message: ''\n    user_message: '{prompt}'\n    label_parse: '{label_parse}'\n    explanation_parse: '{expl_parse}'"
    with open(yaml_file, "a") as yf:
        yf.write(append)

def read_yaml(yaml_file: str) -> Dict:
    with open(yaml_file, "r") as yf:
        try:
            return yaml.safe_load(yf)
        except yaml.YAMLError as exc:
            print(exc)


## custom print function to print in color
def print_c(text: str, c: str = None) -> None:
    if c == "green":
        print("\033[92m" + text + "\033[0m")
    elif c == "red":
        print("\033[91m" + text + "\033[0m")
    elif c == "yellow":
        print("\033[93m" + text + "\033[0m")
    elif c == "blue":
        print("\033[94m" + text + "\033[0m")
    else:
        print(text)
