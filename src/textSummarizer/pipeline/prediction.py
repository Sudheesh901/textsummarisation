from textSummarizer.config.confuiguration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class PredictionPipeline:
    def __init__(self):
        config = ConfigurationManager().get_model_evaluation_config()

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path)

        # Load trained model (not data_path!)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(config.model_path)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

        # Generation settings (same as eval stage)
        self.gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 4,         # faster than 8
            "max_length": 128
        }

    def predict(self, text: str):
        inputs = self.tokenizer(
            [text],
            max_length=512,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )

        outputs = self.model.generate(
            input_ids=inputs["input_ids"].to(self.device),
            attention_mask=inputs["attention_mask"].to(self.device),
            **self.gen_kwargs
        )

        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return summary

'''
from textSummarizer.config.confuiguration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        get_kwargs={"length_penalty":0.8,"num_beams":8, "max_length":128}

        pipe=pipeline("summarization",model=self.config.data_path, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **get_kwargs)[0]["summary_text"]
        print("\nModel Summary")
        print(output)

        return output
    
'''

