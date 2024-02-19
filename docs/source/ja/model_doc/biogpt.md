<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# BioGPT

## Overview

BioGPT model is a generative pre-trained transformer for biomedical text generation and mining, based on the paper "[BioGPT: generative pre-trained transformer for biomedical text generation and mining](https://academic.oup.com/bib/advance-article/doi/10.1093/bib/bbac409/6713511?guestAccessKey=a66d9b5d-4f83-4017-bb52-405815c907b9)" by Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, and Tie-Yan Liu. BioGPT is a generative pre-trained transformer model that has been fine-tuned on 1,500 million PubMed abstracts for biomedical text generation and mining.

## Usage tips

- BioGPT takes left padded input, so it is recommended to pad the input on the right side.
- BioGPT is a causal language model (CLM) trained for generation, so it is good at understanding the next token given the previous tokens. The `run_generation.py` script can be used to check this feature, where BioGPT can generate coherent and fluent text given a prompt.
- The model takes `past_key_values` as input, which are the previous hidden states and attention scores of the model. Using this input allows the model to condition its predictions on its previous hidden states, without re-computing them, which speeds up the generation process. For more details on how to use `past_key_values`, refer to the `BioGptForCausalLM.forward()` method.

This model was contributed by [kamalkraj](https://huggingface.co/kamalkraj). The source code is available [here](https://github.com/microsoft/BioGPT).

## Documentation resources

- [Language Modeling task description](../tasks/language_modeling)

## BioGptConfig

[[autodoc]] BioGptConfig

## BioGptTokenizer

[[auto,doc]] BioGptTokenizer
- `save_vocabulary`

## BioGptModel

[[autodoc]] BioGptModel
- `forward`

## BioGptForCausalLM

[[autodoc]] BioGptForCausalLM
- `forward`

## BioGptForTokenClassification

[[autodoc]] BioGptForTokenClassification
- `forward`

## BioGptForSequenceClassification

[[autodoc]] BioGptForSequenceClassification
- `forward`
