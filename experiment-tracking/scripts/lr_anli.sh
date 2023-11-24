export TOKENIZERS_PARALLELISM=true

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.125 --alpha 0.5 --batch_size 32 --run 5 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.25 --alpha 0.5 --batch_size 32 --run 5 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --alpha 0.5 --batch_size 32 --run 5 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --batch_size 32 --run 5 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.125 --alpha 0.5 --batch_size 32 --run 6 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.25 --alpha 0.5 --batch_size 32 --run 6 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --alpha 0.5 --batch_size 32 --run 6 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --batch_size 32 --run 6 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.125 --alpha 0.5 --batch_size 32 --run 7 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.25 --alpha 0.5 --batch_size 32 --run 7 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --alpha 0.5 --batch_size 32 --run 7 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --batch_size 32 --run 7 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.125 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.125 --alpha 0.5 --batch_size 32 --run 8 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.25 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.25 --alpha 0.5 --batch_size 32 --run 8 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 0.5 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 0.5 --alpha 0.5 --batch_size 32 --run 8 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

# (LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha
echo '##################################################'
echo '(LR Subsampling ANLI1) standard Finetuning: anli1 - t5-v1_1-base - standard - gt label_type - 0 prompt_mix - 1.0 subsample - 0.5 alpha'
python distilling-step-by-step/run.py --from_pretrained google/t5-v1_1-base --dataset anli1 --model_type standard --label_type gt --subsample 1.0 --alpha 0.5 --batch_size 32 --run 8 --lr 0.00002 --bf16 --tf32 --es_threshold 0.0001 --es_patience 30 --parallelize --no_save

