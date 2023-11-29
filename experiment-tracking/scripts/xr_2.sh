export TOKENIZERS_PARALLELISM=true

# (XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 12 --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 12 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 12 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 12 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save