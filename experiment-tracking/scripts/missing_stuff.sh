export TOKENIZERS_PARALLELISM=true

# (Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.125 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.25 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

# (Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Subsampling ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 20

