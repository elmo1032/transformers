<!--
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Autoformer

## ä»çt

Autoformer model is proposed in the paper "[Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting](https://arxiv.org/abs/2106.13008)" by Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long.

This model is a Transformer-based model that can decompose a time series into components and patterns, and learn the auto-correlation of the time series in a sequential manner.

The main idea of the paper is as follows:

* In many real-world applications such as anomaly detection in time series data, long-term forecasting of electricity load, etc., it is important to model long-term dependencies in time series data. Previous Transformer-based models have used complex attention mechanisms to capture long-term dependencies, but they suffer from high computational cost and are not suitable for long sequences. Autoformer addresses this problem by using a decomposition-based approach that can effectively capture long-term dependencies in time series data.
* Autoformer uses a novel auto-correlation mechanism that can capture the temporal dependencies in time series data. This mechanism is based on the idea of decomposing the time series into several components and calculating the auto-correlation of each component. This allows Autoformer to effectively capture the temporal dependencies in time series data, even for long sequences.
* Autoformer also uses a novel series-wise decomposition method that can effectively capture the patterns in time series data. This method is based on the idea of decomposing the time series into several components and calculating the correlation between each component. This allows Autoformer to effectively capture the patterns in time series data, even for long sequences.

Overall, Autoformer is a powerful model for time series forecasting that can effectively capture long-term dependencies and patterns in time series data.

## å®éçä½¿çt

Autoformer model can be used for time series forecasting tasks. Here is an example of how to use Autoformer for univariate time series forecasting:


In this example, we first load the Autoformer model and config from the pre-trained weights. We then prepare the input data, which should be a tensor of shape (batch\_size, sequence\_length, num\_features). The input data should be a univariate time series, i.e., num\_features should be 1.

We then perform a forward pass through the model, which returns a tuple (last\_hidden\_states, past\_key\_values). The last\_hidden\_states tensor contains the hidden states of the model for the input data, and the past\_key\_values tensor contains the key-value pairs that can be used for generating the output for the next time step.

## åèè³æ

For more information about Autoformer, please refer to the following resources:

* [Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting](https://arxiv.org/abs/2106.13008)
* [Hugging Face blog post on Autoformer](https://huggingface.co/blog/autoformer)
* [Autoformer model card on Hugging Face Model Hub](https://huggingface.co/elisim/autoformer-base)

If you have any questions or feedback, please feel free to open a GitHub issue or pull request. We welcome any contributions to improve the documentation and code!
