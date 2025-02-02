<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Dilated Neighborhood Attention Transformer

This is the Dilated Neighborhood Attention Transformer (DiNAT) model implemented in PyTorch. DiNAT is a transformer model that utilizes dilated neighborhood attention and is used for image classification tasks.

## Overview

DiNAT is a transformer model that utilizes dilated neighborhood attention and is used for image classification tasks. It is based on the Neighborhood Attention Transformer (NATTEN) and is a modification of the standard transformer model. DiNAT utilizes dilated convolutions to increase the receptive field of the attention mechanism, allowing it to capture longer-range dependencies in the input data. This makes it well-suited for image classification tasks, where the model must be able to capture dependencies between pixels that are far apart in the image.

The following is a brief overview of the components of the DiNAT model:

- **Dilated Neighborhood Attention**: This is the core attention mechanism used in the DiNAT model. It is a modification of the standard self-attention mechanism that utilizes dilated convolutions to increase the receptive field of the attention mechanism. This allows the model to capture longer-range dependencies in the input data.

- **Transformer Encoder**: The transformer encoder is a stack of transformer layers that are used to process the input data. Each transformer layer consists of a multi-head self-attention mechanism and a position-wise feed-forward network. The transformer encoder is responsible for processing the input data and generating a set of hidden states that can be used for downstream tasks.

- **Classification Head**: The classification head is a linear layer that is used to perform the final image classification. It takes the hidden states generated by the transformer encoder and maps them to a set of class probabilities.

## Usage tips

DiNAT can be used as a standard transformer model by specifying the appropriate configuration and initialization parameters. Here are some tips for using DiNAT:

- When initializing the model, set the `output_hidden_states` parameter to `True` if you want to output the hidden states and reshaped hidden states. The `hidden_states` and `reshaped_hidden_states` will be returned if `output_hidden_states` is set to `True`. The `reshaped_hidden_states` has a different shape than `hidden_states`, so be sure to take this into account when using the model.

- DiNAT relies on the NATTEN library for the dilated neighborhood attention mechanism. You can install NATTEN using pip or by downloading the Linux binary from the NATTEN website. Note that NATTEN is not currently available for Windows.

- Currently, only convolution size 4 is supported.

## Resources

To get started using DiNAT, check out the following Hugging Face resources:

<PipelineTag pipeline="image-classification"/>

- [`DinatForImageClassification`] is a PyTorch implementation of DiNAT for image classification. It can be used with the following example script and Colab notebook:
  - [Example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/image-classification)
  - [Colab notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/image_classification.ipynb)

For more information on image classification, see the [image classification task guide](../tasks/image_classification).

## DinatConfig

[[autodoc]] DinatConfig

This is the configuration class for the DiNAT model. It contains all the configuration parameters for the model, including the number of transformer layers, the hidden size, and the number of attention heads.

## DinatModel

[[autodoc]] DinatModel
    - forward

This is the main model class for DiNAT. It contains the transformer encoder and classification head, and implements the forward pass for the model.

## DinatForImageClassification

[[autodoc]] DinatForImageClassification
    - forward

This is a PyTorch module that wraps the DiNAT model and adds a classification head for image classification tasks. It implements the forward pass for the model and returns the class probabilities.
