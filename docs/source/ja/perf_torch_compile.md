from transformers import AutoModelForImageClassification

model = AutoModelForImageClassification.from_pretrained(MODEL_ID).to("cuda")
model = torch.compile(model)
