from transformers import DebertaTokenizer, DebertaForSequenceClassification, Trainer, TrainingArguments

# Load the pre-trained DeBERTa model and tokenizer
model = DebertaForSequenceClassification.from_pretrained("microsoft/DeBERTa-v3-base")
tokenizer = DebertaTokenizer.from_pretrained("microsoft/DeBERTa-v3-base")

# Prepare the training data
train_texts = [...]  # list of training texts
train_labels = [...]  # list of training labels
train_encodings = tokenizer(train_texts, truncation=True, padding=True)

# Define the training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs",
)

# Create the Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_encodings,
)

# Fine-tune the model
trainer.train()


# Prepare the input data
input_text = "This is a sample input text"
input_encodings = tokenizer(input_text, return_tensors="pt")

# Make predictions
with torch.no_grad():
    outputs = model(**input_encodings)
    logits = outputs.logits
    probabilities = softmax(logits, dim=1)
    predicted_label = torch.argmax(probabilities)

# Print the predicted label
print(predicted_label.item())
