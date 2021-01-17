# Results 

## Perceptron

You can see the result in perceptron_result.txt.

We use this program whis 50000 world (50000 first line of train.txt) (30000 to learn and 20000 to test)
We can do with more world because of lack of RAM.

### To use

    python perceptron.py
    

## XML_roberta_NER

We use this program with the 3 files (train.txt 100000 line, valid.txt 100000 lines and test.txt with 1000000 lines)

### To use

    python3 main.py --data_dir=/home/elliot/SMAA2020/data/       --task_name=ner         --output_dir=model_dir/         --max_seq_length=16         --num_train_epochs 1        --do_eval       --warmup_proportion=0.1       --pretrained_path pretrained_models/xlmr.$PARAM_SET/       --learning_rate 0.00007       --do_train       --eval_on test       --train_batch_size 4       --no_cuda   --dropout 0.2

Be careful to use the good the data_dir
