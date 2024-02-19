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

# Big Transfer (BiT)

## Overview

Big Transfer (BiT) is a model proposed by Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Joan Puigcerver, Jessica Yung, and Sylvain Gelly in their paper [Big Transfer (BiT): General Visual Representation Learning](https://arxiv.org/abs/1912.11370). It is a simple pre-processing method for transfer learning using ResNet (specifically ResNetv2). This method significantly improves the efficiency of transfer learning, allowing for more effective fine-tuning of models for specific tasks.

The main points of the paper are:

- By using pre-processing that includes wide ResNetv2 models with stem and group normalization, the model is able to achieve high performance on a variety of tasks with limited data.
- The authors fine-tune the models on 20 different datasets, and then evaluate their performance on a held-out set. They find that the BiT models outperform other methods on these tasks.
- The BiT models are able to achieve high performance on a variety of tasks, including image classification, object detection, and semantic segmentation.

## Usage tips

- BiT models are ResNetv2 models with the following differences:
  1) All batch normalization layers are replaced with group normalization and weight standardization.
  2) Weight standardization is used in the convolutional layers.
  3) The models are trained with a larger batch size and longer training time.

These changes improve the performance of transfer learning.

- This model was contributed by nielsr.
- The source code for the model can be found [here](https://github.com/google-research/big_transfer).

## Resources

