<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# DeBERTa Model

This is the DeBERTa model implementation in PyTorch and TensorFlow.

## Overview

DeBERTa is a model proposed in the paper ["DeBERTa: Decoding-enhanced BERT with Disentangled Attention"](https://arxiv.org/abs/2006.03654) by Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. It is an improved version of the BERT model, which was proposed in the paper ["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"](https://arxiv.org/abs/1810.04805) by Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.

DeBERTa improves BERT by using two new techniques:

1. **Disentangled Attention**: This technique modifies the self-attention mechanism used in BERT to better capture the relationships between words in a sentence. It does this by separating the attention scores for each head into two parts: one that captures the relationships between words in the same sentence, and another that captures the relationships between words in different sentences.
2. **Enhanced Decoding**: This technique uses a new decoding method that improves the performance of the model on downstream tasks. It does this by using a combination of absolute and relative position embeddings, which allows the model to better understand the order of words in a sentence.

## Resources

- [DeBERTa model card](https://huggingface.co/microsoft/DeBERTa-v3-base): This model card provides information about the DeBERTa model, including its architecture, performance, and usage.
- [DeBERTa model hub](https://huggingface.co/models?other=DeBERTa): This page lists all the DeBERTa models available in the Hugging Face model hub.
- [DeBERTa tutorial](https://huggingface.co/course/chapter7/1?fw=pt): This tutorial provides an overview of the DeBERTa model and its features.
- [DeBERTa PyTorch example](https://github.com/huggingface/transformers/tree/main/examples/pytorch/text-classification): This example shows how to use the DeBERTa model in PyTorch for text classification.
- [DeBERTa TensorFlow example](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/text-classification): This example shows how to use the DeBERTa model in TensorFlow for text classification.

<PipelineTag pipeline="text-classification" />

- [`DebertaForSequenceClassification`] is a PyTorch class that wraps the DeBERTa model for sequence classification. It can be used to classify text into multiple categories.
- [`TFDebertaForSequenceClassification`] is a TensorFlow class that wraps the DeBERTa model for sequence classification. It can be used to classify text into multiple categories.
- [Text classification task](../tasks/sequence_classification): This page provides more information about text classification and how to use the DeBERTa model for this task.

<PipelineTag pipeline="token-classification" />

- [`DebertaForTokenClassification`] is a PyTorch class that wraps the DeBERTa model for token classification. It can be used to label each token in a sentence with a specific category.
- [`TFDebertaForTokenClassification`] is a TensorFlow class that wraps the DeBERTa model for token classification. It can be used to label each token in a sentence with a specific category.
- [Token classification task](../tasks/token_classification): This page provides more information about token classification and how to use the DeBERTa model for this task.

<PipelineTag pipeline="fill-mask" />

- [`DebertaForMaskedLM`] is a PyTorch class that wraps the DeBERTa model for masked language modeling. It can be used to predict missing words in a sentence.
- [`TFDebertaForMaskedLM`] is a TensorFlow class that wraps the DeBERTa model for masked language modeling. It can be used to predict missing words in a sentence.
- [Masked language modeling task](../tasks/masked_language_modeling): This page provides more information about masked language modeling and how to use the DeBERTa model for this task.

<PipelineTag pipeline="question-answering" />

- [`DebertaForQuestionAnswering`] is a PyTorch class that wraps the DeBERTa model for question answering. It can be used to answer questions about a given text.
- [`TFDebertaForQuestionAnswering`] is a TensorFlow class that wraps the DeBERTa model for question answering. It can be used to answer questions about a given text.
- [Question answering task](../tasks/question_answering): This page provides more information about question answering and how to use the DeBERTa model for this task.

## DebertaConfig

[[autodoc]] DebertaConfig

This class contains the configuration for the DeBERTa model. It can be used to specify the architecture, training, and other parameters for the model.

## DebertaTokenizer

[[autodoc]] DebertaTokenizer

This class contains the tokenizer for the DeBERTa model. It can be used to convert text into a format that can be input into the model.

- `build
