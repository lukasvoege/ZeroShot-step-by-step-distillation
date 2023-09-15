# standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.125 subsample
echo "####################"
echo "standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.125 subsample"
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.125 --batch_size 64 --parallelize --es_threshold 0.001 --es_patience 8

# standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.25 subsample
echo "####################"
echo "standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.25 subsample"
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.25 --batch_size 64 --parallelize --es_threshold 0.001 --es_patience 8

# standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.5 subsample
echo "####################"
echo "standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 0.5 subsample"
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --batch_size 64 --parallelize --es_threshold 0.001 --es_patience 8

# standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 1.0 subsample
echo "####################"
echo "standard Finetuning: anli1 - t5-v1_1-base - standard - gt - 1.0 subsample"
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --batch_size 64 --parallelize --es_threshold 0.001 --es_patience 8