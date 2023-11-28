export TOKENIZERS_PARALLELISM=true

# (LONG X LRG GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(LONG X LRG GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 8 --subsample 0.5 --alpha 0.5 --batch_size 8 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 8 --subsample 0.5 --alpha 0.5 --batch_size 8 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 8 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 8 --subsample 0.5 --alpha 0.5 --batch_size 8 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (LONG X LRG GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(LONG X LRG GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 9 --subsample 1.0 --alpha 0.5 --batch_size 8 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 9 --subsample 1.0 --alpha 0.5 --batch_size 8 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN LONG X LRG ANLI1 GPT35 LABEL GIVEN) step-by-step Finetuning: anli1 - t5-v1_1-large - task_prefix - gt label_type - gpt35 llm - 9 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 9 --subsample 1.0 --alpha 0.5 --batch_size 8 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save
