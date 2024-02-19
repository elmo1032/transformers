<!-- Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# BertGeneration

## Overview

BertGeneration is a model that can be used for text generation tasks by fine-tuning a pre-trained BERT model.
It is based on the `EncoderDecoderModel` architecture, which is proposed in the paper "[Leveraging Pre-trained Checkpoints for Sequence Generation Tasks](https://arxiv.org/abs/1907.12461)" by Sascha Rothe, Sishi Nagayan, and Aliaksei Severyn.

The idea is to utilize the power of large-scale pre-trained language models for natural language processing tasks, without the need for task-specific training data. This allows for faster experimentation and prototyping, as well as enabling the use of the same model for multiple NLP tasks.

In this document, we will focus on the use case of text generation, where the pre-trained BERT model is fine-tuned for this specific task. We will demonstrate how to use the `BertGenerationEncoder` and `BertGenerationDecoder` classes to create a fine-tuned BERT model for text generation.

## Usage examples and tips

- You can use the `BertGenerationEncoder` and `BertGenerationDecoder` classes to create a fine-tuned BERT model for text generation by instantiating them and then fine-tuning them on your specific task.




- You can also use a pre-fine-tuned `EncoderDecoderModel` as a standalone model.




### Notes

- The `BertGenerationEncoder` and `BertGenerationDecoder` classes are designed to be used together as an `EncoderDecoder` model.
- Any special tokens, such as those used for sentence segmentation, token classification, or tokenization, are not required. However, it is recommended to add an EOS token to the end of the input sequence.

This model was contributed by [patrickvonplaten](https://huggingface.co/patrickvonplaten). You can find the original code [here](https://tfhub.dev/s?module-type=text-generation&subtype=module-placeholder).

## BertGenerationConfig

[[autodoc]] BertGenerationConfig

## BertGenerationTokenizer

[[autodoc]] BertGenerationTokenizer
    - save_vocabulary

## BertGenerationEncoder

[[autodoc]] BertGenerationEncoder
    - forward

## BertGenerationDecoder

[[autodoc]] BertGenerationDecoder
    - forward
