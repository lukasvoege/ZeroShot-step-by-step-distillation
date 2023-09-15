# standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo 'standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 0.125 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 8

# standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo 'standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 0.25 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 8

# standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo 'standard Distillation: anli1 - t5-v1_1-base - standard - llm label_type - palm llm - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 0.5 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 8

