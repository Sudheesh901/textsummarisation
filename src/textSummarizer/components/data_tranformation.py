from textSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
import os
from datasets import load_dataset,load_from_disk

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encodings=self.tokenizer(example_batch['dialogue'], max_length=512, truncation=True,padding='max_length',return_tensors='pt')

        with self.tokenizer.as_target_tokenizer():
            target_encodings=self.tokenizer(example_batch['summary'], max_length=64, truncation=True, padding='max_length', return_tensors='pt')
        return{
            'input_ids' : input_encodings['input_ids'],
            'attention_maks' : input_encodings['attention_mask'],
            'labels' : target_encodings['input_ids']
        }
    def convert(self):
        dataset_samsum=load_from_disk(self.config.data_path)
        dataset_samsum_pt=dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))