agent.run("Capture the following image", image=image)


agent.run("Read the following text out loud", text=text)


agent.run(
    "Where will the TRRF Scientific Advisory Council Meeting take place in the following `document`?",
    document=document,,
)


pip install transformers[agents]


pip install openai


from transformers import OpenAiAgent

agent = OpenAiAgent(model="text-davinci-003", api_key="<your_api_key>")


from huggingface_hub import login

login("<YOUR_TOKEN>")


from transformers import HfAgent

# Starcoder
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
# StarcoderBase
# agent = HfAgent(,"https://api-inference.huggingface.co/models/bigcode/starcoderbase")
# OpenAssistant
# agent = HfAgent(url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")


agent.run("Draw me a picture of rivers and lakes.")
