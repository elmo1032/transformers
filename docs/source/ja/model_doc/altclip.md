<!-- Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# AltCLIP Model

The AltCLIP model is a variant of the CLIP model that uses XLM-R as the language model instead of the original Transformer model.
This allows AltCLIP to handle multiple languages and achieve performance close to the original CLIP model.

This code block demonstrates how to use the AltCLIP model to compute the similarity score between a given text and an image.




<Tip>

You can use the `AltCLIPModel` just like the `CLIPModel`, with the difference that the input text is passed as a list of strings instead of a single string.

</Tip>

## AltCLIPConfig

The `AltCLIPConfig` class is used to configure the AltCLIP model. It has the following methods:

- `from_text_vision_configs`: Creates a new `AltCLIPConfig` instance by combining the configuration of a text model and a vision model.

## AltCLIPTextConfig

The `AltCLIPTextConfig` class is used to configure the text model used in AltCLIP. It has the following methods:

- `from_pretrained`: Loads the configuration of a pre-trained text model.

## AltCLIPVisionConfig

The `AltCLIPVisionConfig` class is used to configure the vision model used in AltCLIP. It has the following methods:

- `from_pretrained`: Loads the configuration of a pre-trained vision model.

## AltCLIPProcessor

The `AltCLIPProcessor` class is used to preprocess the input data before it is passed to the model. It has the following methods:

- `__call__`: Preprocesses the input data.
- `get_text_features`: Extracts features from the input text.
- `get_image_features`: Extracts features from the input image.

## AltCLIPModel

The `AltCLIPModel` class is the main class used to compute the similarity score between the input text and the input image.
It has the following methods:

- `__call__`: Computes the similarity score between the input text and the input image.
- `get_text_features`: Extracts features from the input text.
- `get_image_features`: Extracts features from the input image.

## AltCLIPTextModel

The `AltCLIPTextModel` class is a variant of the `AltCLIPModel` class that only takes text as input. It has the following methods:

- `__call__`: Extracts features from the input text.

## AltCLIPVisionModel

The `AltCLIPVisionModel` class is a variant of the `AltCLIPModel` class that only takes images as input. It has the following methods:

- `__call__`: Extracts features from the input image.
