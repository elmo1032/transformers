pip install transformers bitsandbytes>=0.39.0 -q


generated_text = model.generate(
    inputs,
    max_length=20,
    num_beams=5,
    early_stopping=True,
)
tokenizer.decode(generated_text[0])
