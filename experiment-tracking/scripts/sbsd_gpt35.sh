export TOKENIZERS_PARALLELISM=true

# (Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.125 --alpha 0.5 --batch_size 32 --es_threshold 0.0001 --es_patience 30

# (Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.25 --alpha 0.5 --batch_size 32 --es_threshold 0.0001 --es_patience 30

# (Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.5 --alpha 0.5 --batch_size 32 --es_threshold 0.0001 --es_patience 30

# (Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) step-by-step Distillation: anli1 - t5-v1_1-base - task_prefix - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type llm --llm gpt35 --prompt_mix 6 --subsample 1.0 --alpha 0.5 --batch_size 32 --es_threshold 0.0001 --es_patience 30
