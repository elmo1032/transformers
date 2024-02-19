<!-- Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contains specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# CodeLlama

## Overview

The Code Llama model is a large language model for code, introduced in the paper [Code Llama: Open Foundation Models for Code](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/). It is a code-focused variant of the Llama 2 model and provides several features such as high-quality completions, code search, code translation, and code refinement. It offers several pretrained models, including a general model (Code Llama), a Python-specific model (Code Llama - Python), and several instruction-tuned models (Code Llama - Instruct) with different model sizes.

You can find the model card for each pretrained model on the [Hugging Face Model Hub](https://huggingface.co/models?search=code_llama).

This code is provided by [ArthurZucker](https://huggingface.co/ArthurZ) and is based on the [Llama model](https://github.com/facebookresearch/llama).

## Usage tips and examples

<Tip warning={true}>

The `Llama2` model uses `bfloat16` by default, but we recommend using `float16` for better performance.

* `float32`: When initializing a model in PyTorch, the model's precision is set to `float32` by default. The `transformers` library also uses this precision for compatibility with PyTorch. However, you can change the precision to `float16` or `bfloat16` by specifying the `torch_dtype` parameter when initializing the model.
* `bfloat16`: The Llama model is optimized for this precision, so we recommend using it for training and inference.
* `float16`: We recommend using this precision for inference, as it is generally faster than `bfloat16` and provides similar accuracy. However, you can also use `bfloat16` for inference. We recommend comparing the results of both precisions after inference.

</Tip>

### Converting Llama weights to Hugging Face format

To convert Llama weights to the Hugging Face format, you can use the following command:




### Using the Code Llama model

To use the Code Llama model, you can follow these steps:

1. Import the necessary modules:




2. Load the pretrained model and tokenizer:




3. Prepare the input sequence:




4. Generate a completion:




### Using the pipeline

You can also use the `pipeline` function to generate completions:




### Tokenization

The Code Llama tokenizer uses SentencePiece with BPE to tokenize code. One feature of the tokenizer is that it does not split tokens that are already in the vocabulary, even if they are part of a larger token. For example, if the tokenizer encounters the word "Banana" and "Banana" is already in the vocabulary, it will not split it into "Ba" and "nana".

<Tip>

The Code Llama models use the same API as the `Llama2` models. For more information on the API, see the [Llama2 documentation](llama2).

</Tip>

## CodeLlamaTokenizer

[[autodoc]] CodeLlamaTokenizer
   - build_inputs_with_special_tokens
    - get_special_tokens_mask
    - create_token_type_ids_from_sequences
    - save_vocabulary

## CodeLlamaTokenizerFast

[[autodoc]] CodeLlamaTokenizerFast
    - build_inputs_with_special_tokens
    - get_special_tokens_
