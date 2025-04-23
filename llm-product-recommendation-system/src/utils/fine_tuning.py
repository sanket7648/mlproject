from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from transformers import AutoTokenizer
import torch
import pandas as pd

class FineTuner:
    def __init__(self, model_name, train_data, eval_data):
        self.model_name = model_name
        self.train_data = train_data
        self.eval_data = eval_data
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)  # Assuming 5 labels for ratings

    def tokenize_data(self, data):
        return self.tokenizer(data['text'].tolist(), padding=True, truncation=True, return_tensors='pt')

    def prepare_dataset(self):
        train_encodings = self.tokenize_data(self.train_data)
        eval_encodings = self.tokenize_data(self.eval_data)

        train_dataset = torch.utils.data.TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'], torch.tensor(self.train_data['label'].tolist()))
        eval_dataset = torch.utils.data.TensorDataset(eval_encodings['input_ids'], eval_encodings['attention_mask'], torch.tensor(self.eval_data['label'].tolist()))

        return train_dataset, eval_dataset

    def train(self):
        train_dataset, eval_dataset = self.prepare_dataset()

        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=3,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./logs',
            evaluation_strategy="epoch",
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
        )

        trainer.train()

    def evaluate(self):
        _, eval_dataset = self.prepare_dataset()
        trainer = Trainer(model=self.model)
        eval_results = trainer.evaluate(eval_dataset)
        return eval_results

    def save_model(self, path):
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)