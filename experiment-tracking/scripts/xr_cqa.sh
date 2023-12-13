export TOKENIZERS_PARALLELISM=true

# (XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 73 --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 73 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 15 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 73 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 73 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 74 --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 74 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 50 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 74 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 74 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 75 --subsample 1.0 --alpha 0.5 --batch_size 32 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 75 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 1 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(XR 85 CQA GPT35) step-by-step Finetuning: cqa - t5-v1_1-base - task_prefix - gt label_type - gpt35 llm - 75 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset cqa --model_type task_prefix --label_type gt --llm gpt35 --prompt_mix 75 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

