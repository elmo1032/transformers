>>> from transformers import pipeline

>>> generator = pipeline(task="automatic-speech-recognition")


>>> generator("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
{'text': 'I HAVE A DREAM BUT ONE DAY THIS NATION WILL RISE UP LIVE OUT THE TRUE MEANING OF ITS TREE'}

