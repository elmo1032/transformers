pip install transformers datasets evaluate seqeval


from huggingface_hub import notebook_login
notebook_login()


from datasets import load_dataset

wnut = load_dataset("wnut_17")


wnut["train"][0]


label_list = wnut["train"].features["ner_tags"].feature.names
label_list


from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)

    label_ids = []
    for i, label in enumerate(examples[f"ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)  # Map tokens to their respective word.
        previous_word_idx = None
        label_id = []
        for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_id.append(-100)
            elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                label_id.append(label[word_idx])
            else:
                label_id.append(-100)
            previous_word_idx = word_idx
        label_ids.append(label_id)

    tokenized_inputs["labels"] = label_ids
    return tokenized_inputs

tokenized_wnut = wnut.map(tokenize_and_align_labels, batched=True)


from transformers import DataCollatorForTokenClassification

data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)


import evaluate

seqeval = evaluate.load("seqeval")


import numpy as np

def compute_metrics(p):
    predictions, labels = p
    predi
ctions = np.argmax(predictions, axis=2)

    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    results = seqeval.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }


from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="my_awesome_wnut_model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    evaluation_strategy="epoch",

