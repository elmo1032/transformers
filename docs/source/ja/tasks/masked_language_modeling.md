from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilroberta-base")

text = "The Milky Way is a <mask> galaxy."
inputs = tokenizer(text, return_tensors="pt")
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]


from transformers import AutoModelForMaskedLM

model = AutoModelForMaskedLM.from_pretrained("distilbert/distilroberta-base")
logits = model(**inputs).logits
mask_token_logits = logits[0, mask_token_index, :]


top_3_tokens = torch.topk(mask_token_logits, 3, dim=1).indices[0].tolist()

for token in top_3_tokens:
    print(text.replace(tokenizer.mask_token, tokenizer.decode([token])))


The Milky Way is a spiral galaxy.
The Milky Way is a massive galaxy.
The Milky Way is a small galaxy.


pip install transformers datasets evaluate


from datasets import load_dataset

eli5 = load_dataset("eli5", split="train_asks[:5000]")
eli5 = eli5.train_test_split(test_size=0.2)

eli5 = eli5.flatten()
eli5["train"][0]


from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilroberta-base")

def preprocess_function(examples):
    return tokenizer([" ".join(x) for x in examples["answers.text"]])

tokenized_eli5 = eli5.map(
    preprocess_function,
    batched=True,
    num_proc=4,
    remove_columns=eli5["train"].column_names,
)


block_size = 128

def group_texts(examples):
    # Concatenate all texts.
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])

    # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can customize this part to your needs.
    if total_length >= block_size:
        total_length = (total_length // block_size) * block_size

    # Split by chunks, of block_size.
    result = {
        k: [t[i : i + block_size] for i
