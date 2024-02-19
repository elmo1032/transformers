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

# Semantic segmentation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/semantic_segmentation.ipynb)

<Youtube id="dKE8SIt9C-w"/>

Semantic segmentation is the process of dividing a digital image into multiple segments or pixels, where each segment or pixel is assigned a class label. Semantic segmentation models have various applications, such as autonomous driving, medical imaging, and satellite imagery.

This notebook demonstrates how to fine-tune a pre-trained SegFormer model on the SceneParse150 dataset using the ð¤ Transformers library. The SceneParse150 dataset contains 150 scene categories, and the goal is to train a model that can accurately predict the scene category for each pixel in a given image.

Before getting started, make sure to install the required packages:




Next, log in to the Hugging Face hub to push the trained model:




## Load SceneParse150 dataset

First, load the SceneParse150 dataset's small subset using the ð¤ Datasets library:

