<!-- Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# KOSMOS-2

This script contains the KOSMOS-2 model for conditional generation, which is a Transformer-based causal language model
trained on a web-scale dataset of grounded image-text pairs. The model is capable of handling various multimodal and
language understanding and generation tasks.

## Overview

The KOSMOS-2 model is proposed in the paper "[Kosmos-2: Grounding Multimodal Large Language Models to the World](https://arxiv.org/abs/2306.14824)". It is a Transformer-based causal language model that is trained using the next-word prediction task on a dataset of grounded image-text pairs. The spatial coordinates of the bounding boxes in the dataset are converted to a sequence of location tokens, which are appended to the respective entity text spans. The data format is similar to "hyperlinks" that connect the object regions in an image to their text span in the corresponding caption.

The abstract from the paper is as follows:

*We introduce Kosmos-2, a Multimodal Large Language Model (MMLM), enabling new capabilities of perceiving, object descriptions (e.g., bounding boxes) and grounding text to the visual world. Specifically, we represent refer expressions as links in Markdown, i.e., `[text span](bounding boxes)`, where object descriptions are sequences of location tokens. Together with multimodal corpora, we construct large-scale data of grounded image-text pairs (called GrIT) to train the model. In addition to the existing capabilities of MMLMs (e.g., perceiving general modalities, following instructions, and performing in-context learning), Kosmos-2 integrates the grounding capability into downstream applications. We evaluate Kosmos-2 on a wide range of tasks, including (i) multimodal grounding, such as referring expression comprehension, and phrase grounding, (ii) multimodal referring, such as referring expression generation, (iii) perception-language tasks, and (iv) language understanding and generation. This work lays out the foundation for the development of Embodiment AI and sheds light on the big convergence of language, multimodal perception, action, and world modeling, which is a key step toward artificial general intelligence. Code and pretrained models are available at https://aka.ms/kosmos-2.*

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/kosmos_2_overview.jpg"
alt="drawing," width="600"/>

<small> Overview of tasks that KOSMOS-2 can handle. Taken from the <a href="https://arxiv.org/abs/2306.14824">original paper</a>. </small>

## Example

The following example demonstrates how to use the KOSMOS-2 model for conditional generation.




This model was contributed by [Yi-Dar SHIEH](https://huggingface.co/ydshieh). The original code can be found [here](https://github.com/microsoft/unilm/tree/master/kosmos-2).

## Kosmos2Config

[[autodoc]] Kosmos2Config

## Kosmos2ImageProcessor

## Kosmos2Processor

[[autodoc]] Kosmos2Processor
    - **`__call__`**

## Kosmos2Model

[[autodoc]] Kosmos2Model
    - **`forward`**

## Kosmos2ForConditionalGeneration

[[autodoc]] Kosmos2ForConditionalGeneration
    - **`forward`**
