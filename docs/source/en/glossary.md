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

# Glossary

This glossary defines general machine learning and ð¤ Transformers terms to help you better understand the documentation.

## A

### attention mask

The attention mask is an optional argument used when batching sequences, together. This argument indicates to the model which tokens should be attended to, and which should not.

For example, consider these two sequences:




The encoded versions have different lengths:




Therefore, we can't put them together in the same tensor as-is. The first sequence needs to be padded up to the length of the second one, or the second one needs to be truncated down to the length of the first one.

In the first case, the list of IDs will be extended by the padding indices. We can pass a list to the tokenizer and ask it to pad like this:




We can see that 0s have been added on the right of the first sentence, to make it the same length as the second one:




This can then be converted into a tensor in PyTorch or TensorFlow. The attention mask is a binary tensor indicating the position of the padded indices so that the model does not attend to them. For the [`BertTokenizer`], `1` indicates a value that should be attended to, while `0` indicates a padded value. This attention mask is in the dictionary returned by the tokenizer under the key "attention\_mask":




### autoencoding models

See [encoder models](#encoder-models) and [masked language modeling](#masked-language-modeling-mlm)

### autoregressive models

See [causal language modeling](#causal-language-modeling) and [decoder models](#decoder-models)

## B

### backbone

The backbone is the network (embeddings and layers) that outputs the raw hidden states or features. It is usually connected to a [head](#head) which accepts the features as its input to make a prediction. For example, [`ViTModel`] is a backbone without a specific head on top. Other models can also use [`VitModel`] as a backbone such as [DPT](mode_doc/dpt).

## C

### causal language modeling

A pretraining task where the model reads the texts in order and has to predict the next word. It's usually done by reading the whole sentence but using a mask inside the model to hide the future tokens at a certain timestep.

### channel

Color images are made up of some combination of values in three channels: red, green, and blue (RGB) and grayscale images only have one channel. In ð¤ Transformers, the channel can be the first or last dimension of an image's tensor: [`n_channels`, `height`, `width`] or [`height`, `width`, `n_channels`].

### connectionist temporal classification (CTC)

An algorithm that allows a model to learn without knowing exactly how the input and output are aligned; CTC calculates the distribution of all possible outputs for a given input and chooses the most likely output from it. CTC is commonly used in speech recognition tasks because speech doesn't always cleanly align with the transcript for a variety of reasons such as a speaker's different speech rates.

### convolution

A type of layer in a neural network where the input matrix is
