<!--
Copyright 2021 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# BigBird-Pegasus

## Overview

BigBird is a transformer model proposed in the paper ["Big Bird: Transformers for Longer Sequences"](https://arxiv.org/abs/2007.14062). It addresses the issue of long-range dependencies in transformer models by introducing a new attention mechanism that can handle longer sequences. BigBird has a combination of local, random, and global attention, allowing it to capture different types of dependencies in the input sequence.

The main features of BigBird are:

- Local attention: similar to the standard transformer attention, it focuses on a fixed-size window of tokens.
- Random attention: it attends to a random subset of tokens in the sequence, allowing it to capture long-range dependencies.
- Global attention: it attends to a fixed number of tokens at the beginning and end of the sequence, which are often important for understanding the context.

BigBird is designed to be a drop-in replacement for the standard transformer models, and can be used in the same way as BERT, RoBERTa, or DistilBERT. It can handle sequences of up to 8,192 tokens, which is a significant improvement over the standard transformer models that can only handle sequences of up to 1,024 tokens.

## Usage tips

- For a detailed explanation of how BigBird works and how to use it, please refer to this [blog post](https://huggingface.co/blog/big-bird).
- BigBird has two versions: **original\_full** and **block\_sparse**. Use **block\_sparse** when the sequence length is greater than 1024.
- The code is structured in three main files and two smaller files.
- The sequence length is controlled by the maximum sequence length parameter.
- Currently, only the ITC variant is supported.
- By default, **num\_random\_blocks = 0**.
- BigBirdPegasus uses [PegasusTokenizer](https://github.com/huggingface/transformers/blob/main/src/transformers/models/pegasus/tokenization_pegasus.py) for tokenization.
- BigBird is a relative positional encoding model, so it's recommended to input the data from right to left.

The code for BigBird is available [here](https://github.com/google-research/bigbird).

## Tasks

- [Sequence Classification](../tasks/sequence_classification)
- [Question Answering](../tasks/question_answering)
- [Language Modeling](../tasks/language_modeling)
- [Translation](../tasks/translation)
- [Summarization](../tasks/summarization)

## BigBirdPegasusConfig

[[autodoc]] BigBirdPegasusConfig
    - all

## BigBirdPegasusModel

[[autodoc]] BigBirdPegasusModel
    - forward

#,# BigBirdPegasusForConditionalGeneration

[[autodoc]] BigBirdPegasusForConditionalGeneration
    - forward

## BigBirdPegasusForSequenceClassification

[[autodoc]] BigBirdPegasusForSequenceClassification
    - forward

## BigBirdPegasusForQuestionAnswering

[[autodoc]] BigBirdPegasusForQuestionAnswering
    - forward

## BigBirdPegasusForCausalLM

[[autodoc]] BigBirdPegasusForCausalLM
    - forward
