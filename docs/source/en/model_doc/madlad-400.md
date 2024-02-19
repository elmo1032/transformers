<!--
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contains specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# MADLAD-400

This is the documentation for the MADLAD-400 models, which were released in the paper [MADLAD-400: A Multilingual And Document-Level Large Audited Dataset](https://arxiv.org/abs/2301.02342).

## Overview

MADLAD-400 is a manually audited, general domain 3T token monolingual dataset based on CommonCrawl, spanning 419 languages. The limitations revealed by self-auditing MADLAD-400 and the role data auditing had in the dataset creation process are discussed in the paper. A 10.7B-parameter multilingual machine translation model was trained and released, which is competitive with models that are significantly larger. An 8B-parameter language model was also trained and assessed for few-shot translation.

This model was added by [Juarez Bochi](https://huggingface.co/jbochi). The original checkpoints can be found [here](https://github.com/google-research/google-research/tree/master/madlad_400).

## Usage

You can directly use MADLAD-400 weights without finetuning the model:




Google has released the following variants:

- [google/madlad400-3b-mt](https://huggingface.co/google/madlad400-3b-mt)
- [google/madlad400-7b-mt](https://huggingface.co/google/madlad400-7b-mt)
- [google/madlad400-7b-mt-bt](https://huggingface.co/google/madlad400-7b-mt-bt)
- [google/madlad400-10b-mt](https://huggingface.co/google/madlad400-10b-mt)

The original checkpoints can be found [here](https://github.com/google-research/google-research/tree/master/madlad_400).

<Tip>

Refer to [T5's documentation page](https://huggingface.co/docs/transformers/model_doc/t5) for all API references, code examples, and notebooks. For more details regarding training and evaluation of the MADLAD-400, refer to the model card.

</Tip>
