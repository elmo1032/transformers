<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing
permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contains specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ð¤ Transformers Overview

â¹ï¸ The Hugging Face Transformers library is a state-of-the-art library for Natural Language Processing (NLP) and Machine Learning (ML) tasks. It provides thousands of pre-trained models to perform tasks on texts such as classification, information extraction, summarization, translation, text generation, and more.

This file lists all the models supported by the Transformers library. Each model has its own README file with detailed documentation.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Models](#models)
3. [Tokenizers](#tokenizers)
4. [Pipelines](#pipelines)
5. [Examples](#examples)
6. [Advanced Topics](#advanced-topics)

## Getting Started

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Basic Usage](#basic-usage)
- [Benchmarks](#benchmarks)
- [Frequently Asked Questions](#frequently-asked-questions)

### Installation

To install the Transformers library, you can use `pip`:




You can also install the library from source if you want to modify it or use the latest features:




### Quickstart

Here is a minimal working example that shows how to use the Transformers library:




### Basic Usage

The Transformers library provides a simple and consistent interface to interact with pre-trained models. Here are the main classes and functions you will use:

- `AutoTokenizer`: a class that automatically selects the correct tokenizer for a given model.
- `AutoModel`: a class that automatically selects the correct model for a given model name or task.
- `AutoModelForSequenceClassification`: a class that automatically selects the correct model for sequence classification tasks.
- `AutoModelForTokenClassification`: a class that automatically selects the correct model for token classification tasks.
- `AutoModelForQuestionAnswering`: a class that automatically selects the correct model for question answering tasks.
- `AutoModelForMultipleChoice`: a class that automatically selects the correct model for multiple choice tasks.
- `AutoModelForSeq2SeqLM`: a class that automatically selects the correct model for sequence-to-sequence language modeling tasks.
- `AutoModelForSeq2SeqCA`: a class that automatically selects the correct model for sequence-to-sequence causal language modeling tasks.
- `pipeline`: a function that creates a pipeline for a given task and automatically selects the correct model and tokenizer.

### Benchmarks

The Transformers library provides benchmarks to compare the performance of different models on various tasks. You can find the benchmarks [here](#).

### Frequently Asked Questions

You can find the frequently asked questions [here](#).

## Models

This section lists all the models supported by the Transformers library. Each model has its own README file with detailed documentation.

### ALBERT

- [README](model_doc/albert)

### AltCLIP

- [README](model_doc/altclip)

### Audio Spectrogram Transformer

- [README](model_doc/audio-spectrogram-transformer)

### BART

- [README](model_doc/bart)

### BARTpho

- [README](model_doc/bartpho)

### BEiT

- [README](model_doc/beit)

### BERT

- [README](model_doc/bert)

### BERT For Sequence Generation

- [README](model_doc/bert-generation)

### BERTweet

- [README](model_doc/bertweet)

### BigBird-Pegasus

- [README](model_doc/bigbird_pegasus)

### BigBird-RoBERTa

- [README](model_doc/big_bird)

### BioGpt

- [README](model_doc/biogpt)

### BiT

- [README](model_doc/bit)

### Blenderbot

- [README](model_doc/blenderbot)

### BlenderbotSmall

- [README](model_doc/blenderbot-small)

### BLIMP

- [README](model_doc/blimp)

### BLOOM

- [README](model_doc/bloom)

### BORT

- [README](model_doc/bort)

### ByT5

- [README](model_doc/byt5)

### CamemBERT

- [README](model_doc/camembert)

### CANINE


