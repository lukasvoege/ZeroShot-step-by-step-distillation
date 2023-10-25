export TOKENIZERS_PARALLELISM=true

# (Model Size ANLI1) standard Finetuning: anli1 - t5-v1_1-large - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size ANLI1) standard Finetuning: anli1 - t5-v1_1-large - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize

# (Model Size ANLI1) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size ANLI1) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize

# (Model Size ANLI1) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size ANLI1) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm palm --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize

# (Model Size ANLI1) step-by-step Distillation: anli1 - t5-v1_1-large - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size ANLI1) step-by-step Distillation: anli1 - t5-v1_1-large - task_prefix - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize

