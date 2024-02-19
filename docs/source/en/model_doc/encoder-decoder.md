>>> from transformers import BertConfig, EncoderDecoderConfig, EncoderDecoderModel

>>> config_encoder = BertConfig()
>>> config_decoder = BertConfig()

>>> config = EncoderDecoderConfig.from_encoder_decoder_configs(config_encoder, config_decoder)
>>> model = EncoderDecoderModel(config=config)


>>> from transformers import EncoderDecoderModel, BertTokenizer

>>> tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-uncased")
>>> model = EncoderDecoderModel.from_encoder_decoder_pretrained("google-bert/bert-base-uncased", "google-bert/bert-base-uncased")


>>> from transformers import AutoTokenizer, EncoderDecoderModel

>>> # load a fine-tuned seq2seq model and corresponding tokenizer
>>> model = EncoderDecoderModel.from_pretrained("patrickvonplaten/bert2bert_cnn_daily_mail")
>>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/bert2bert_cnn_daily_mail")

>>> # let's perform inference on a long piece of text
>>> ARTICLE_TO_SUMMARIZE = (
...     "PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."
... )
>>> input_ids = tokenizer(ARTICLE_TO_SUMMARIZE, return_tensors="pt").input_ids

>>> # autoregressively generate summary (uses greedy decoding by default)
>>> generated_ids = model.generate(input_ids)
>>> generated_text = tokenizer.decode(generated_ids[0])
>>> print(generated_text)
nearly 800,000 customers were affected by the shutoffs. the aim is to reduce the risk of wildfires. nearly 800,000 customers were expected to be affected by high winds amid dry conditions. pg & e said it scheduled the blackouts to last through at least midday tomorrow.
