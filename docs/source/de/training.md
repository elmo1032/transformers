>>> from datasets import load_dataset

>>> dataset = load_dataset("yelp_review_full")
>>> dataset["train"][100]
{'label': 0,
 'text': 'My expectations for McDonalds are t rarely high. But, for one to still fail so spectacularly...that takes something special!\\nThe cashier took, my friends\'s order, then promptly ignored me. I had to force myself in front of a cashier who opened his register to wait on the person BEHIND me. I waited over five minutes for ,a gigantic order that included precisely one ,kid\'s meal. After watching two people who ordered after me be handed their food, I asked ,where mine was. The manager started yelling at the cashiers for \\"serving off their orders\\" when they didn\'t have their food. But neither cashier was anywhere near those controls, and the manager was the one serving food ,to customers and clearing the boards.\\nThe manager was rude when giving me my order. She ,didn\'t make sure that I had everything ON MY, RECEIPT, and never even had the decency to a,pologize that I felt I was getting poor servi,ce.\\nI\'ve eaten at various McDonalds restau,rants for over 30 years. I\'ve worked at more, than one location. I expect bad days, bad mo,ods, and the occasional mistake. But I have y,et to have a decent experience at this store., It will remain a place I avoid unless someon,e in my party needs to avoid illness from low, blood sugar. Perhaps I should go back to the, racially biased service of Steak n Shake ins,tead!'}


>>> from transformers import AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-case
