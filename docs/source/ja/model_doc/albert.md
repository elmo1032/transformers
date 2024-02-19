<!--Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# ALBERT

<div class="flex flex-wrap space-x-1">
<a href="https://huggingface.co/models?filter=albert">ALBERT models</a>
<a href="https://huggingface.co/spaces/docs-demos/albert-base-v2">Hugging Face Spaces</a>
</div>

## æ¦è¦

ALBERT model is proposed in the paper "[ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942)" by Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. The main ideas of the paper are:

- Sentence-level layer normalization: split the input sentence into multiple chunks and apply layer normalization per chunk.
- Cross-layer parameter sharing: share the parameters across different layers.

The main claim of the paper is that these techniques reduce the memory footprint and increase the training speed of BERT, while maintaining the performance.

## ä½¿ç¨ä¸ã®ãã³ã

- ALBERT is a model that uses relative position embeddings, so it is recommended to input the data with the right padding on the left side and the actual data on the right side.
- ALBERT uses hidden states from multiple layers, so the memory footprint is smaller than BERT, but the computational cost is similar if the number of layers is the same.
- The hidden size E is different from the sequence length H, but this is because the hidden states are computed per token, while the sequence length is the total number of tokens. The effective sequence length is H >> E, so the memory footprint is smaller.
- The model is divided into multiple layers, each of which has its own parameters. The next sentence prediction task is implemented as follows: given two sentences A and B, predict whether B follows A or not.

## åèè³æ

- [Sequence Classification](../tasks/sequence_classification)
- [Token Classification](../tasks/token_classification)
- [Question Answering](../tasks/question_answering)
- [Masked Language Modeling](../tasks/masked_language_modeling)
- [Multiple Choice](../tasks/multiple_choice)

## AlbertConfig

[[autodoc]] AlbertConfig

## AlbertTokenizer

[[autodoc]] AlbertTokenizer
- build_inputs_with_special_tokens
- get_special_tokens_mask
- create_token_type_ids_from_sequences
- save_vocabulary

## AlbertTokenizerFast

[[autodoc]] AlbertTokenizerFast

## Albert specific outputs

[[autodoc]] models.albert.modeling_albert.AlbertForPreTrainingOutput

[[autodoc]] models.albert.modeling_tf_albert.TFAlbertForPreTrainingOutput

<frameworkcontent>
<pt>

## AlbertModel

[[autodoc]] AlbertModel
- forward

## AlbertForPreTraining

[[autodoc]] AlbertForPreTraining
- forward

## AlbertForMaskedLM

[[autodoc]] AlbertForMaskedLM
- forward

## AlbertForSequenceClassification

[[autodoc]] AlbertForSequenceClassification
- forward

## AlbertForMultipleChoice

[[autodoc]] AlbertForMultipleChoice

## AlbertForTokenClassification

[[autodoc]] AlbertForTokenClassification
- forward

## AlbertForQuestionAnswering

[[autodoc]] AlbertForQuestionAnswering
- forward

</pt>

<tf>

## TFAlbertModel

[[autodoc]] TFAlbertModel
- call

## TFAlbertForPreTraining

[[autodoc]] TFAlbertForPreTraining
- call

## TFAlbertForMaskedLM

[[autodoc]] TFAlbertForMaskedLM
- call

## TFAlbertForSequenceClassification

[[autodoc]] TFAlbertForSequenceClassification
- call

## TFAlbertForMultipleChoice

[[autodoc]] TFAlbertForMultipleChoice
- call

## TFAlbertForTokenClassification

[[autodoc]] TFAlbertForTokenClassification
- call

## TFAlbertForQuestionAnswering

[[autodoc]] TFAlbertForQuestionAnswering
- call

</tf>
<jax>

## FlaxAlbertModel

[[autodoc]] FlaxAlbertModel
- __call__

## FlaxAlbertForPreTraining

[[autodoc]] FlaxAlbertForPreTraining
- __call__

## FlaxAlbertForMaskedLM

[[autodoc]] FlaxAlbertForMaskedLM
- __call__

## FlaxAlbertForSequenceClassification

[[autodoc]] FlaxAlbertForSequenceClassification
- __call__

## FlaxAlbertForMultipleChoice

[[autodoc]] FlaxAlbertForMultipleChoice
- __call__

## FlaxAlbertForTokenClassification

[[autodoc]] FlaxAlbertForTokenClassification
- __call__

## FlaxAlbertForQuestionAnswering

[[autodoc]] FlaxAlbertForQuestionAnswering
- __call__

</jax>
</frameworkcontent>
