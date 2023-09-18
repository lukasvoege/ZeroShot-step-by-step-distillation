# (Model Size) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# (Model Size) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# (Model Size) step-by-step Distillation: anli1 - t5-v1_1-large - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) step-by-step Distillation: anli1 - t5-v1_1-large - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

