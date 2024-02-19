# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
# rendered properly in your Markdown viewer.

# ---- ëê·,ëª¨ ì¸ì´ ëª¨ë¸ë¡ ìì±íê¸° ----

# [[open-in-colab]]

# LLM is a type of language model that is trained to generate text based on a given prompt. It can be fine-tuned on a
# specific task, such as generating a response to a user input, by training it on a dataset that is relevant to the task.
# By fine-tuning a pre-trained language model, we can create a model that is specialized for a particular task while
# still benefiting from the general language understanding capabilities of the pre-trained model.

# To use the `generate` method from the `GenerationMixin` class in Transformers, we need to first create an instance of a
# model that inherits from this class. The `AutoModelForCausalLM` class is one such class that can be used for causal
# language modeling tasks.

# We can then use the `from_pretrained` method to load a pre-trained model and fine-tune it on a specific task. In this
# example, we will load the `mistralai/Mistral-7B-v0.1` model and fine-tune it on a text generation task.

# We also need to install the `bitsandbytes` library, which is required for 4-bit quantization. This is a technique for
# reducing the memory usage of the model by storing its weights in a lower-precision format.

# Before we can start generating text, we need to install the necessary libraries. We can do this by running the following
# command:

# ```
# pip install transformers bitsandbytes>=0.39.0 -q
# ```

# ---- íºì´ ëª¨ë ,ë¼ì´ë¸ë¬ë¦¬ ----

# [ì¸ê³¼ì  ì¸ì´, ëª¨ë¸ë§(causal language modeling)](tasks/l,anguage_modeling)ì ëª©ì ì¼ë¡ íìµë ì,¸ì´ ëª¨ë¸ì ì¼ë ¨ì íºì´ ì
ë ¥,ê°ì ì ê³µí í, ê·¸ ê²°ê³¼ë¡ ë¤,ì ì
ë ¥,ê°ì´ ëª,¨ë¸ì ì
ë ¥ì¼ë¡ ì¬ì©íì¬ ë°ë³µì ì,¼ë¡ í¸ì¶íë ì¶ë¡  ê³¼ì ìëë¤.

# <!-- [GIF 1 -- FWD PASS] -->
# <figure class="image table text-center m-0 w-full">
#     <video
#         style="max-width: 90%; m,argin: auto;"
#         autoplay loop muted pla,ysinline
#         src="https://huggingface.co/,datasets/huggingface/documentation-images/res,olve/main/blog/assisted-generation/gif_1_1080,p.mov"
#     ></video>
#     <figcaption>"LLMì ,ì ë°© í¨ì¤"</figcaption>
# </figure>

# LLMê³¼, ìê·°íê· ìì±ì í¨ê» ì¬ì©í  ë, ìë¤ë©´, ììíê¸° ì ì ìë¤ë©´ ì
ë ¥,ê°ì ì ê³µíë ì ë°© í¨ì¤ë¥¼ ì ë ì ê³µë©ëë¤. ê·¸ë¬ë ì ë°© í¨ì¤ì ë¤ì ì
ë ¥,ê°ì´ ëª,¨ë¸ì ì ê³µíë ì ë°© í¨ì¤ë¥¼ ì ë ì ê³µë©ëë¤. ì ë°© í¨ì¤ì ì ê³µíë ì ë°© í¨ì¤ë¥¼ ì ë ì ê³µë©ëë¤. ì ë°© í¨ì¤ì ì ê³µíë ì ë°© í¨ì¤ë¥¼ ì ë ì ê³µë©ëë¤. ì ë°© í¨ì
