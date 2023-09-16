# step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 0.125 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 0.25 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm palm --subsample 0.125 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm palm --subsample 0.25 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo 'step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm palm --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

