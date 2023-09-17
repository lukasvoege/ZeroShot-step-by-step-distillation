# (Model Size) standard Finetuning: anli1 - t5-v1_1-large - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) standard Finetuning: anli1 - t5-v1_1-large - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# (Model Size) standard Finetuning: anli1 - t5-v1_1-xl - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) standard Finetuning: anli1 - t5-v1_1-xl - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-xl --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# (Model Size) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) standard Distillation: anli1 - t5-v1_1-large - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-large --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

# (Model Size) standard Distillation: anli1 - t5-v1_1-xl - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(Model Size) standard Distillation: anli1 - t5-v1_1-xl - standard - llm label_type - palm llm - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-xl --dataset anli1 --model_type standard --label_type llm --llm palm --subsample 1.0 --alpha 0.5 --parallelize --es_threshold 0.0001 --es_patience 10

