<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contains specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# SqueezeBERT

This is the SqueezeBERT model, a bidirectional transformer similar to the BERT model. The key difference is that SqueezeBERT
uses grouped convolutions instead of fully-connected layers for the Q, K, V and FFN layers. This model was proposed in
[SqueezeBERT: What can computer vision teach NLP about efficient neural networks?](https://arxiv.org/abs/2006.11316) by Forrest N. Iandola,
Albert E. Shaw, Ravi Krishna, and Kurt W. Keutzer.

The SqueezeBERT code was contributed by [forresti](https://huggingface.co/forresti).

## Overview

The SqueezeBERT model is a bidirectional transformer similar to the BERT model. The key difference is that SqueezeBERT uses
grouped convolutions instead of fully-connected layers for the Q, K, V and FFN layers. This model was proposed in
[SqueezeBERT: What can computer vision teach NLP about efficient neural networks?](https://arxiv.org/abs/2006.11316) by Forrest N.
Iandola, Albert E. Shaw, Ravi Krishna, and Kurt W. Keutzer.

### Resources

- [Text classification task guide](../tasks/sequence_classification)
- [Token classification task guide](../tasks/token_classification)
- [Question answering task guide](../tasks/question_answering)
- [Masked language modeling task guide](../tasks/masked_language_modeling)
- [Multiple choice task guide](../tasks/multiple_choice)

## Usage tips

- SqueezeBERT is a model with absolute position embeddings, so it's usually advised to pad the inputs on the right rather
  than the left.
- SqueezeBERT is similar to BERT and therefore relies on the masked language modeling (MLM) objective. It is therefore
  efficient at predicting masked tokens and at NLU in general, but is not optimal for text generation. Models trained with
  a causal language modeling (CLM) objective are better in that regard.
- For best results when fine-tuning on sequence classification tasks, it is recommended to start with the
  *squeezebert/squeezebert-mnli-headless* checkpoint.

## Config

[[autodoc]] SqueezeBertConfig

## Tokenizer

The SqueezeBERT tokenizer is a PyTorch torch.nn.Module subclass. It inherits from the BertTokenizer class and overrides
the build_inputs_with_special_tokens, get_special_tokens_mask, create_token_type_ids_from_sequences, and save_vocabulary
methods.

[[autodoc]] SqueezeBertTokenizer
- build_inputs_with_special_tokens
- get_special_tokens_mask
- create_token_type_ids_from_sequences
- save_vocabulary

### Fast Tokenizer

[![autodoc]] SqueezeBertTokenizerFast

## Model

The SqueezeBERT model is a PyTorch torch.nn.Module subclass. It inherits from the BertModel class and overrides the forward
method.

[[autodoc]] SqueezeBertModel

## Masked Language Model

The SqueezeBERT masked language model is a PyTorch torch.nn.Module subclass. It inherits from the BertForMaskedLM class and
overrides the forward method.

[[autodoc]] SqueezeBertForMaskedLM

## Sequence Classification

The SqueezeBERT sequence classification model is a PyTorch torch.nn.Module subclass. It inherits from the BertForSequenceClassification
class and overrides the forward method.

[[autodoc]] SqueezeBertForSequenceClassification

## Multiple Choice

The SqueezeBERT multiple choice model is a PyTorch torch.nn.Module subclass. It inherits from the BertForMultipleChoice class
and overrides the forward method.

[[autodoc]] SqueezeBertForMultipleChoice

## Token Classification

The SqueezeBERT token classification model is a PyTorch torch.nn.Module subclass. It inherits from the BertForTokenClassification
class and overrides the forward method.

[[autodoc]] SqueezeBertForTokenClassification

## Question Answering

The SqueezeBERT question answering model is a PyTorch torch.nn.Module subclass. It inherits from the BertForQuestionAnswering
class and overrides the forward method.

[[autodoc]] SqueezeBertForQuestionAnswering
