import sys
import importlib
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

sys.path.append("../ZeroShot-step-by-step-distillation")
run = importlib.import_module("run")
utils = importlib.import_module("src.utils")

load_dotenv()

DATASET = "anli1"
N_PRV_BEST = 15
TEST_SIZE = 50

# 1.) evaluate all prompts
run.run_experiment(DATASET, test_size=TEST_SIZE, model="gpt-3.5-turbo", seed=42)

# 2.) load all prompts, and get their performance
prompt_templates = utils.read_yaml(f"prompt-templates/{DATASET}.yaml")["templates"]
prompt_metadata = utils.read_yaml(f"prompt-metadata/{DATASET}.yaml")

# 3.) build previous best
id_acc = [(id, meta["performance"]["accuracy"]) for id, meta in prompt_metadata.items()]
id_acc.sort(key=lambda x: x[1])
if len(id_acc) > N_PRV_BEST:
    id_acc = id_acc[len(id_acc) - N_PRV_BEST:]

previous_best = ""
for id, acc in id_acc:
    previous_best += "PRT:\n"
    previous_best += prompt_templates[id]['user_message'] + "\n"
    previous_best += "Score:\n"
    previous_best += str(round(acc*100)) + "\n\n"

# (4.) load data to generate examples)

# 5.) prompt meta prompt 8 times and build prompt templates

with open("opro/meta-prompts/anli1.txt", "r") as f:
    meta_prompt = f.read()

meta_prompt = meta_prompt.replace("<[PREVIOUS_BEST]>", previous_best)

print("#" * 75)
print(meta_prompt)
print("#" * 75)

chat_model = ChatOpenAI(model = "gpt-3.5-turbo", temperature=1.1, max_tokens=200)

i = 0
while i < 8:
    print(f"Querying {i+1}/8...")
    response = chat_model.predict(meta_prompt)
    #print(response)
    if all([x in response for x in ["{premise}", "{hypothesis}", "<PRT>", "</PRT>"]]):
        i += 1
        response = response.split("<PRT>")[1].split("</PRT>")[0]
        response = response.strip("\n")
        utils.add_prompt_to_yaml(f"prompt-templates/{DATASET}.yaml", response)
        print(response)
    else:
        i += 0.5

        

# check for premise and hypothesis placeholder

# 6.) determine the label parse