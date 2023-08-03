# Hugging Face demo

```sh
pip install transformers
```

tokennizer -> model -> post processing

tokennizer: 文本变向量


```sh
$ python3 main.py
Downloading (…)solve/main/vocab.txt: 100%|████████| 110k/110k [00:00<00:00, 173kB/s]
Downloading (…)okenizer_config.json: 100%|████████| 29.0/29.0 [00:00<00:00, 152kB/s]
Downloading (…)lve/main/config.json: 100%|█████████| 624/624 [00:00<00:00, 1.96MB/s]
Downloading model.safetensors: 100%|█████████████| 412M/412M [00:59<00:00, 6.90MB/s]
Some weights of the model checkpoint at bert-base-chinese were not used when initializing BertModel: ['cls.predictions.transform.dense.bias', 'cls.seq_relationship.weight', 'cls.predictions.transform.dense.weight', 'cls.predictions.transform.LayerNorm.weight', 'cls.seq_relationship.bias', 'cls.predictions.bias', 'cls.predictions.transform.LayerNorm.bias']
- This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
[101, 4495, 3833, 4638, 4696, 6465, 3221, 5401, 1469, 4263, 102]
{'input_ids': [101, 4495, 3833, 4638, 4696, 6465, 3221, 5401, 1469, 4263, 102, 6432, 4638, 1922, 1962, 749, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
{'input_ids': [[101, 5381, 5317, 2128, 1059, 2458, 1355, 1146, 711, 676, 702, 2231, 5277, 102], [101, 6756, 6775, 5143, 5320, 2231, 5277, 5381, 5317, 2128, 1059, 2458, 1355, 102], [101, 6756, 6775, 1216, 5543, 2231, 5277, 5381, 5317, 2128, 1059, 2458, 1355, 102], [101, 6756, 6775, 7439, 6956, 816, 2231, 5277, 5381, 5317, 2128, 1059, 2458, 1355, 102], [101, 3844, 6407, 1730, 7339, 3418, 2945, 6756, 6775, 5381, 5317, 2128, 1059, 4680, 3403, 1169, 2137, 3844, 6407, 2825, 3318, 6206, 3724, 1350, 3844, 6407, 6369, 1153, 102], [101, 3844, 6407, 1730, 7339, 1762, 5381, 5317, 2128, 1059, 1730, 7339, 4638, 3118, 2898, 678, 8024, 2130, 2768, 4802, 6371, 3844, 6407, 2400, 5356, 1169, 3844, 6407, 2845, 1440, 102], [101, 1762, 6756, 6775, 4802, 6371, 5310, 3362, 4638, 1825, 4794, 677, 8024, 1825, 754, 1394, 4415, 4638, 4415, 4507, 8024, 4802, 6371, 1762, 6392, 6369, 1469, 2458, 1355, 7348, 3667, 6399, 1166, 1139, 4638, 2792, 3300, 7599, 7372, 1772, 2347, 6158, 2970, 1358, 102]], 'token_type_ids': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]}
{'input_ids': [101, 5381, 5317, 2128, 1059, 2458, 1355, 1146, 711, 676, 702, 2231, 5277, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
```