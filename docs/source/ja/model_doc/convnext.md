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

# ConvNeXt

## Overview

ConvNeXT is a convolutional neural network (ConvNet) proposed in "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)" by Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feichtenhofer, Trevor Darrell, and Saining Xie. It is a ConvNet that achieves state-of-the-art performance by incorporating ideas from recent transformer models while maintaining the simplicity and efficiency of traditional ConvNets.

The main ideas of the paper are as follows:

- The superiority of ConvNets over transformers in computer vision tasks is not due to their inductive biases, but rather their ability to model local interactions and maintain translation equivariance.
- Recent transformer models have shown that depthwise and zeropadding operations can be used to model local interactions in a way that is competitive with convolutions.
- By combining the strengths of ConvNets and transformers, it is possible to build a model that achieves state-of-the-art performance while maintaining the simplicity and efficiency of ConvNets.

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/convnext_architecture.jpg" alt="Diagram" width="600"/>

<small> ConvNeXT architecture. <a href="https://arxiv.org/abs/2201.03545">Paper</a>.</small>

This model was contributed by [nielsr](https://huggingface.co/nielsr) and is based on the original implementation by [ariG23498](https://github.com/ariG23498). The TensorFlow version of the model was contributed by [gante](https://github.com/gante) and [sayakpaul](https://github.com/sayakpaul).

## Resources

- [Hugging Face documentation](https://huggingface.co/docs/transformers/model_doc/convnext)
- [Model card on Hugging Face Model Hub](https://huggingface.co/facebook/convnext-base)
- [Official GitHub repository](https://github.com/facebookresearch/ConvNeXt)

## Model architecture

The ConvNeXT model is a convolutional neural network that consists of a stem layer, several stages, and a head. Each stage contains multiple residual blocks, which are composed of depthwise and pointwise convolutions. The stem layer is a $3{\times}3$ convolution that reduces the spatial resolution of the input and increases the number of channels. The head is a linear layer that produces the output logits.

The main difference between ConvNeXT and traditional ConvNets is the use of depthwise and pointwise convolutions in the residual blocks. Depthwise convolutions apply a single filter to each input channel, while pointwise convolutions combine the output of the depthwise convolutions using a $1{\times}1$ convolution. This allows ConvNeXT to model local interactions in a way that is similar to transformers, while maintaining the efficiency and simplicity of ConvNets.

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/convnext_block.jpg" alt="Block diagram" width="600"/>

<small> ConvNeXT block. <a href="https://arxiv.org/abs/2201.03545">Paper</a>.</small>

## Training

The ConvNeXT model was trained on the ImageNet-21k dataset, which contains 14 million images and 21,841 classes. The model was trained using the AdamW optimizer with a batch size of 256 and a learning rate of 1e-3. The model was trained for 90 epochs, with a linear learning rate warmup for the first 10 epochs and a cosine learning rate decay for the remaining epochs.

## Usage

The ConvNeXT model can be used for image classification tasks. It can be fine-tuned on a downstream task by adding a classification head on top of the pre-trained model and training it on the downstream dataset.

Here is an example of how to use the ConvNeXT model for image classification in PyTorch:




The `logits` tensor will contain the raw predictions for each class. To get the predicted class, you can use the `argmax` function:




## Limitations

The ConvNeXT model has the following limitations:

- It was trained on the ImageNet-21k dataset, which may not be representative of other datasets.
- It may not perform well on tasks that require a high level of abstraction or global context.
- It may not be robust to adversarial attacks or data corruption.

## Ethical considerations

The ConvNeXT model should be used responsibly and ethically. It should not be used for any
