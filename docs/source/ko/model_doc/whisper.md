<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Whisper  [[whisper]]

## ê°ì [[overview]]

The Whisper model, proposed in [Robust Speech Recognition via Large-Scale Weak Supervision](https://cdn.openai.com/papers/whisper.pdf), is a robust automatic speech recognition model that aims to transcribe speech from any domain or language with high accuracy. It is trained on a large dataset of 68 hours of diverse audio data with multitask supervision, achieving state-of-the-art results on several benchmarks. The model is fully-supervised, but it can also be fine-tuned with limited or no supervision.

Key features:

- Can transcribe speech in multiple languages with high accuracy.
- Trained on a large and diverse dataset with multitask supervision.
- Can be fine-tuned with limited or no supervision.
- Supports streaming recognition.

## Model architecture [[model-architecture]]

The Whisper model consists of a series of Transformer encoder layers that take in a sequence of audio features and output a sequence of hidden states. The audio features are extracted using a convolutional neural network (CNN) and then transformed into a sequence of tokens using a quantizer. The model is trained using a combination of connectionist temporal classification (CTC) and cross-entropy loss.

## Training procedure [[training-procedure]]

The Whisper model is trained on a large dataset of 68 hours of diverse audio data with multitask supervision. The dataset includes audio data from various sources, such as podcasts, lectures, and meetings, in multiple languages. The model is trained using a combination of connectionist temporal classification (CTC) and cross-entropy loss.

## Usage [[usage]]

The Whisper model can be used for various tasks, such as speech recognition, translation, and synthesis. It can be fine-tuned on a specific task or domain with limited or no supervision.

## Example [[example]]

Here is an example of how to use the Whisper model for speech recognition:




## Limitations [[limitations]]

The Whisper model has some limitations. For example, it may not perform well on noisy or accented speech. It is also a large model, which may require significant computational resources to fine-tune.

## Citation [[citation]]

If you use the Whisper model in your research, please cite the following paper:

Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). Robust Speech Recognition via Large-Scale Weak Supervision. arXiv preprint arXiv:2204.05297.

## References [[references]]

For more information, please see the following resources:

- [Whisper model card](https://huggingface.co/transformers/model_doc/whisper.html)
- [Whisper model hub](https://huggingface.co/models?search=whisper)
- [Whisper paper](https://cdn.openai.com/papers/whisper.pdf)
- [Whisper implementation](https://github.com/openai/whisper)
