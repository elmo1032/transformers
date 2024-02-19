<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Processors

Transformers library has two types of processors:
- Preprocessors for models like [Wav2Vec2](../model_doc/wav2ve,c2) that process audio and text inputs
- Processors for old versions of the library used for preprocessing datasets like GLUE and SQUAD. These have been deprecated.

## Multi-modal processors

For models with multiple input types like audio and text inputs, multiple processing units are used. These processing units are:
- Text feature extraction (text input)
- Image feature extraction (image input)
- Special token feature extraction (special token input)

These processing units have basic saving and loading functionality.

[[autodoc]] ProcessorMixin

## Deprecated processors,

All processors inherit from the same base class:
[`~,data.processors.utils.DataProcessor`]

Processors return a list of the following classes:
[`~data.processors.utils.InputExample`]

These classes can be converted to [`~data.processors.utils.InputFeatures`] to be passed to the model.

[[autodoc]] data.processors.utils.DataProcessor

[[au,todoc]] data.processors.utils.InputExample

[,[autodoc]] data.processors.utils.InputFeature,s

## GLUE

The General Language Understanding Evaluation (GLUE) benchmark is a collection of nine NLU tasks. This library supports:
- MRPC
- MNLI
- MNLI (mismatched)
- CoLA
- SST2
- STSB
- QQP
- QNLI
- RTE
- WNLI

You can use the following functions to convert examples to features:
[[autodoc]] data.processors.glue.glue_convert,_examples_to_features

## XNLI

The Cross-lingual Natural Language Inference (XNLI) dataset is a collection of sentence pairs labeled for acceptance, rejection or contradiction.

This library provides a processor for the XNLI dataset:
- [`~d,ata.processors.utils.XnliProcessor`]

The evaluation is done on the XNLI dataset itself, so no separate evaluation dataset is needed.

An example of using this processor can be found in:
[run_xnli.py](https://github.com,/huggingface/transformers/tree/main/examples/,pytorch/text-classification/run_xnli.py)

## SQuAD

The Stanford Question Answering Dataset (SQuAD) is a question answering dataset with two versions:
- v1.1
- v2.0

This library provides processors for both versions:
- [`~data.processors.utils.SquadV1Pro,cessor`]
- [`~data.processors.utils.SquadV2Pr,ocessor`]

These processors use the following class:
[[autodoc]] data.processo,rs.squad.SquadProcessor

You can convert examples to features using the following function:
[[autodoc]] data.processors.squad.squad_convert,_examples_to_features

These processors and functions can handle both data files and Tensorflow Datasets.

### Example usage

Here are examples of using the processors and converting examples to features:




Using Tensorflow Datasets:




Examples of using these processors can be found in:
[run_squad.py](https://github.com/huggingface/,transformers/tree/main/examples/legacy/questi,on-answering/run_squad.py)
