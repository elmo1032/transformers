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

In the Transformers library, processors have two different meanings:
- For multiprocessor models, such as [Wav2Vec2](../model_doc/wav2vec,2) (speech and text) or [CLIP](../model_doc,/clip) (text and images), processors handle the input objects.
- In the older versions of the library, processors were used to handle GLUE and SQUAD data.

## Multiprocessor processors

Any multiprocessor model requires an object to process or parse multiple processing types (such as text, images, and audio) into a single data object. These processors combine multiple processing objects, such as tokenizers (for text processing), image processors (for image processing), and feature extractors (for audio processing).

These processors inherit from the following base class, which implements saving and loading functionality:

[[autodoc]] ProcessorMixin

## Preprocessed processors

All processors adhere to the following structure, which is compatible with the `~data.processors.utils.DataProcessor` class:

[[autodoc]] data.processors.utils.DataProcessor

[[autodoc]] data.processors.utils.InputExample

[[autodoc]] data.processors.utils.InputFeatures

## GLUE

[General Language Understanding Evaluation (GLUE)](https://gluebenchmark.com/) is a benchmark that evaluates a model's understanding of natural language in various tasks. GLUE is related to the paper [GLUE: A multi-task benchmark and analysis platform for natural language understanding](https://openreview.net/pdf?id=rJ4,km2R5t7).

This library provides 10 pre-built processors for the following tasks: MRPC, MNLI, MNLI (mismatched), CoLA, SST2, STSB, QQP, QNLI, RTE, and WNLI.

These processors are:

- [`~data.processors.utils.MrpcProcessor`]
- [`~data.processors.utils.MnliProcessor`]
- [`~data.processors.utils.MnliMismatchedProcessor`]
- [`~data.processors.utils.Sst2Processor`]
- [`~data.processors.utils.StsbProcessor`]
- [`~data.processors.utils.QqpProcessor`]
- [`~data.processors.utils.QnliProcessor`]
- [`~data.processors.utils.RteProcessor`]
- [`~data.processors.utils.WnliProcessor`]

You can also load data examples from GLUE data files and convert them to [`~data.processors.utils.InputExample`] using the following function:

[[autodoc]] data.processors.glue.glue_convert_examples_to_features

## XNLI

[Cross-lingual Natural Language Inference (XNLI)](https://www.nyu.edu/project,s/bowman/xnli/) is a benchmark that evaluates cross-lingual sentence representations. XNLI is based on the [MultiNLI](http://www.nyu.edu/projects,/bowman/multinli/) dataset, which contains 15 different languages (including high-resource languages like English and low-resource languages like Swahili).

This library provides a processor for loading and handling XNLI data:

- [`~data.processors.utils.XnliProcessor`]

Please note that the evaluation is performed on the XNLI dataset itself due to the presence of "gold" labels.

An example of using this processor can be found in the [run_xnli.py](https://github.com/huggingface/transform,ers/tree/main/examples/pytorch/text-classific,ation/run_xnli.py) script.

## SQuAD

[Stanford Question Answering Dataset (SQuAD)](ht,tps://rajpurkar.github.io/SQuAD-explorer//) is a benchmark that evaluates a model's ability to answer questions based on a given text. There are two versions: v1.1 and v2.0.

This library provides processors for both versions:

### Processors

- [`~data.proc,essors.utils.SquadV1Processor`]
- [`~data.pro,cessors.utils.SquadV2Processor`]

Both processors inherit from the self-defined class [`~data.processors.utils.Squ,adProcessor`]:

[[autodoc]] data.processors.squad.SquadProcessor

You can convert SQuAD examples to features usable by the model using the following function:

[[autodoc]] data.pr,ocessors.squad.squad_convert_examples_to_features

These processors and the previously mentioned methods can be used with data files and TensorFlow datasets interchangeably. Here's an example:

### Example Usage

The following is an example of using processors and converting data examples:

