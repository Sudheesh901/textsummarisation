from transformers import (
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
    AutoModelForSeq2SeqLM,
    AutoTokenizer
)
from datasets import load_from_disk
import torch
import os
import os
from textSummarizer.logging import logger
from textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):

        device = "cpu"   # <<< force CPU (T5-small can handle)
        print("Training on:", device)

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

        model = model.to(device)

        # Load dataset
        data_samsum_pt = load_from_disk(self.config.data_path)

        # Collator
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Training Args (CPU-safe)
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            fp16=False,         
            report_to=[],      
            no_cuda=True        # <<< VERY IMPORTANT
        )

        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=data_samsum_pt["test"],   # <<< choosed Test data for CPU
            eval_dataset=data_samsum_pt["validation"]
        )
        
        trainer.train()

        # Save model & tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "t5_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
