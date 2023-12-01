export TOKENIZERS_PARALLELISM=true

# (RERUN Model Size ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN Model Size ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 2 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save

# (RERUN Model Size ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(RERUN Model Size ANLI1 GPT35) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - gpt35 llm - 6 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type llm --llm gpt35 --prompt_mix 6 --subsample 1.0 --alpha 0.5 --batch_size 32 --run 3 --bf16 --tf32 --es_threshold 0.0001 --es_patience 20 --parallelize --no_save
