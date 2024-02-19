<!-- Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Perplexity of fixed-length models

[[open-in-colab]],

Perplexity (PPL) is one of the most common metrics for evaluating language models. Before diving in, we should note
that the metric applies specifically to classical language models (sometimes called autoregressive or causal language
models) and is not well defined for masked language models like BERT (see [summary of the models](model_summary)).

Perplexity is defined as the exponentiated average negative log-likelihood of a sequence. If we have a tokenized
sequence X = (x0, x1, ..., xt), then the perplexity of X is,

$$\text{PPL}(X) = \exp \left\{ {-\frac{1}{t}\sum_i^t \log p_{heta} (x_i|x_{<i}) } \right\}$$

where $\log p_{heta} (x_i|x_{<i})$ is the log-likelihood of the ith token conditioned on the preceding tokens x_{<i}, according to our model. Intuitively, it can be thought of as an evaluation of the model's ability to predict uniformly among the set of, specified tokens in a corpus. Importantly, this means that the tokenization procedure has a direct impact on a model's perplexity which should always be taken into consideration when comparing different models.

This is also equivalent to the exponentiation of the cross-entropy between the data and model predictions. For more
intuition about perplexity and its relationship to Bits Per Character (BPC) and data compression, check out this
[fantastic blog post on The Gradient](https://thegradient.pub/understanding-evaluation-metrics-for-language-models/).

## Calculating PPL with fixed-length models

If we weren't limited by a model's context size, we would evaluate the model's perplexity by autoregressively factoring a sequence and conditioning on the entire preceding subsequence at each step, as shown below.

<img width="600" alt="Full decomposition of a sequence with unlimited context length" src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/ppl_full.gif"/>

When working with approximate models, however, we typically have a constraint on the number of tokens the model can process. The largest version of [GPT-2](model,_doc/gpt2), for example, has a fixed length of 1024 tokens, so we cannot calculate p_{heta}(xt|x_{<t}) directly when t is greater than 1024.

Instead, the sequence is typically broken into subsequences equal to the model's maximum input size. If a model's max input size is k, we then approximate the likelihood of a token xt by conditioning only on the k-1 tokens that precede it rather than the entire context. When evaluating the model's perplexity of a sequence, a tempting but suboptimal approach is to break the sequence into disjoint chunks and add up the decomposed log-likelihoods of each segment independently.

<img width="600" alt="Suboptimal PPL not taking advantage of full available context" src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/ppl_chunked.gif"/>

This is quick to compute since the perplexity of each segment can be computed in one forward pass, but serves as a poor approximation of the fully-factorized perplexity and will typically yield a higher (worse) PPL because the model will have less context at most of the prediction steps.

Instead, the PPL of fixed-length models should be evaluated with a sliding-window strategy. This involves repeatedly sliding the context window so that the model has more context when making each prediction.

<img width="600" alt="Sliding window PPL taking advantage of all available context" src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/ppl_sliding.gif"/>

This is a closer approximation to the true decomposition of the sequence probability and will typically yield a more favorable score. The downside is that it requires a separate forward pass for each token in the corpus. A good practical compromise is to employ a strided sliding window, moving the context by larger strides rather than sliding by 1 token at a time. This allows computation to proceed much faster while still giving the model a large context to make predictions at each step.

## Example: Calculating perplexity with GPT-2 in ð¤ Transformers

Let's demonstrate this process with GPT-2.




We'll load in the WikiText-2 dataset and evaluate the perplexity using a few different sliding-window strategies. Since this dataset is small and we're just doing one forward pass over the set, we can just load and encode the entire dataset in memory.

