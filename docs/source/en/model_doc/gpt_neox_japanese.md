<!-- Copyright 2022 The HuggingFace Team. All rights reserved. -->

# GPT-NeoX-Japanese

## Overview

This is an autoregressive language model for Japanese, trained on top of [https://github.com/EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox). Japanese is a unique language with its large vocabulary and a combination of hiragana, katakana, and kanji writing scripts. To address this distinct structure of the Japanese language, we use a special sub-word tokenizer (<https://github.com/tanreinama/Japanese-BPEEncoder_V2>). We are very grateful to tanreinama for open-sourcing this incredibly helpful tokenizer. Following the recommendations from Google's research on PaLM (<https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html>), we have removed bias parameters from transformer blocks, achieving better model performance. Please refer to this article (<https://medium.com/ml-abeja/training-a-better-gpt-2-93b157662ae4>) for more details.

## Usage example

