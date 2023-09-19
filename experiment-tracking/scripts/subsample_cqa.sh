# (Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type gt --subsample 0.125 --alpha 0.5

# (Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type gt --subsample 0.25 --alpha 0.5

# (Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type gt --subsample 0.5 --alpha 0.5

# (Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Finetuning: cqa - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type gt --subsample 1.0 --alpha 0.5

# (Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm palm --subsample 0.125 --alpha 0.5

# (Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm palm --subsample 0.25 --alpha 0.5

# (Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm palm --subsample 0.5 --alpha 0.5

# (Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm palm --subsample 1.0 --alpha 0.5

# (Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type llm --llm palm --subsample 0.125 --alpha 0.5

# (Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type llm --llm palm --subsample 0.25 --alpha 0.5

# (Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type llm --llm palm --subsample 0.5 --alpha 0.5

# (Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) standard Distillation: cqa - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5

# (Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type llm --llm palm --subsample 0.125 --alpha 0.5

# (Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type llm --llm palm --subsample 0.25 --alpha 0.5

# (Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type llm --llm palm --subsample 0.5 --alpha 0.5

# (Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling CQA) step-by-step Distillation: cqa - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type llm --llm palm --subsample 1.0 --alpha 0.5

