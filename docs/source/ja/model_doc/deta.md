<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# DETA Model

This file contains the code for the DETA model, which is a detection transformer with assignment. It is based on the
[NMS Strikes Back](https://arxiv.org/abs/2212.06137) paper by Jeffrey Ouyang-Zhang, Jang Hyun Cho, Xingyi Zhou, and Philipp KrÃ¤henbÃ¼hl.
DETA improves upon the Deformable DETR model by using one-to-many 2D spatial correspondences and a learnable assignment
module. It also uses non-maximum suppression (NMS) to improve the accuracy of object detection.

## DetaConfig

The `DetaConfig` class contains configuration information for the DETA model.

[[autodoc]], DetaConfig

## DetaImageProcessor

The `DetaImageProcessor` class contains methods for processing input images and post-processing the output of the
DETA model.

[[autodoc]], DetaImageProcessor
- `preprocess`: Preprocesses the input image.
- `post_process_object_detection`: Post-processes the output of the DETA model to extract object detection results.

## DetaModel

