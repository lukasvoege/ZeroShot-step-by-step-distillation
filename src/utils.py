from typing import Dict, Union
import yaml



def read_yaml_prompts(yaml_file: str) -> Dict:
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