<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Tokenizer

Tokenizers are used to provide input to models. They contain tokenizers for all models. Some parts of the tokenizer are
written in specific high-performance Python code and some parts are implemented in Rust in the ð¤ Tokenizers
library [ð¤ Tokenizers](https://github.com/huggingface/tokenizers). The following is possible with high-performance
tokenization:

1. High-speed subword tokenization for special cases
2. Adding padding between words (tokens) and subword pieces (e.g. adding spaces between tokens)

The base class [`PreTrainedTokenizer`] and [`PreTrainedTokenizerFast`] provide functionality for encoding and
decoding Python strings, and for saving and loading tokenizer files in the Python pickle format. The tokenizer classes
are initialized with a pre-trained tokenizer or a path to a tokenizer file. The tokenizer classes also include
functionality for handling special tokens.

The [`PreTrainedTokenizer`] and [`PreTrainedTokenizerFast`] classes implement the following functionality:

- Tokenization (splitting strings into subword tokens), encoding (converting strings or lists of strings to lists of
  token IDs), and decoding (converting lists of token IDs to strings)
- Adding new subwords to the vocabulary using custom methods (e.g. BPE, SentencePiece)
- Handling special tokens (e.g. adding new special tokens, accessing token properties)

The [`BatchEncoding`] class is a Python dictionary-like object that contains encoded data and metadata. It is created
using the `__call__`, `encode_plus`, or `batch_encode_plus` methods of a tokenizer class. In the case of a "fast"
tokenizer (HuggingFace [Tokenizers library](https://github.com/huggingface/tokenizers)), the `BatchEncoding` class
also contains word and token piece (e.g. subword) information.

## PreTrainedTokenizer

[[autodoc]] PreTrainedTokenizer
    - __call__
    - apply_chat_template
    - batch_decode
    - decode
    - encode
    - push_to_hub
    - all

## PreTrainedTokenizerFast

[`PreTrainedTokenizerFast`] relies on the ð¤ Tokenizers library. Pre-trained tokenizers obtained from the ð¤ Tokenizers
library can be easily compiled to ð¤ Transformers. More information on how to use the ð¤ Tokenizers library can be
found in the [Using tokenizers from ð¤ Tokenizers](../fast_tokenizers) tutorial.

[[autodoc]] PreTrainedTokenizerFast
    - __call__
    - apply_chat_template
    - batch_decode
    - decode
    - encode
    - push_to_hub
    - all

## BatchEncoding

[[autodoc]] BatchEncoding
