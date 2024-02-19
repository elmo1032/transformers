<!--Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Donut Model

This file contains the code for the Donut model, which is a model for document understanding tasks. It consists of an image Transformer encoder and an autoregressive text Transformer decoder. The Donut model is used for document image classification, form understanding, and visual question answering.

## Overview

The Donut model was proposed in [OCR-free Document Understanding Transformer](https://arxiv.org/abs/2111.15664) by Geewook, Kim, Teakgyu Hong, Moonbin Yim, Jeongyeon Nam, Jinyoung Park, Jinyeong Yim, Wonseok Hwang, Sangdoo Yun, Dongyoon Han, and Seunghyun Park. The Donut model is an OCR-free visual document understanding (VDU) model that performs document understanding tasks such as document image classification, form understanding, and visual question answering using only the raw image as input.

The Donut model is a conceptually simple yet effective model that consists of an image Transformer encoder and an autoregressive text Transformer decoder. The image Transformer encoder encodes the image into a sequence of visual features, and the autoregressive text Transformer decoder generates the target text autoregressively based on the visual features and the task prompt.

The Donut model is trained using a cross-entropy loss function and can be fine-tuned on various document understanding tasks. The Donut model achieves state-of-the-art performances on various VDU tasks in terms of both speed and accuracy.

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/donut_architecture.jpg" alt="drawing" width="600"/>

<small> Donut high-level overview. Taken from the <a href="https://arxiv.org/abs/2111.15664">original paper</a>. </small>

This model was contributed by [nielsr](https://huggingface.co/nielsr). The original code can be found [here](https://github.com/clovaai/donut).

## Usage tips

- The quickest way to get started with Donut is by checking the [tutorial notebooks](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Donut), which show how to use the model at inference time as well as fine-tuning on custom data.
- Donut is always used within the [VisionEncoderDecoder](vision-encoder-decoder) framework.

## Inference examples

Donut's [`VisionEncoderDecoder`] model accepts images as input and makes use of [`~generation.GenerationMixin.generate`] to autoregressively generate text given the input image.

The [`DonutImageProcessor`] class is responsible for preprocessing the input image, and [`XLM RobertaTokenizer`/`XLMRobertaTokenizerFast`] decodes the generated target tokens to the target string. The [`DonutProcessor`] wraps [`DonutImageProcessor`] and [`XLM RobertaTokenizer`/`XLMRobertaTokenizerFast`] into a single instance to both extract the input features and decode the predicted token ids.

### Step-by-step Document Image Classification

