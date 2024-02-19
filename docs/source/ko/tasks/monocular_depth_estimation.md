<!--
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ë¨ì¼ ìì ê¸°ë° ê¹ì´ ì¶ì [[depth-estimation,-pipeline]]

This script demonstrates how to perform depth estimation by using the `pipeline` API.
It loads a pre-trained model that estimates the depth of objects in an image.

Depth estimation is a process of estimating the distance of objects in a 3D scene from an image.
It can be used for various applications such as 3D reconstruction, robotics, and augmented reality.

<Tip>
For more information about the available models, please refer to the following:

- [DPT](../model_doc/dpt), [GLPN](../model_doc/glpn)

<!--End of the generated tip-->
</Tip>

To perform depth estimation, follow these steps:

1. Load the depth estimation pipeline:




## ê¹ì´ ì¶ì  íì´íë¼ì,¸[[depth-estimation-inference-by-hand]]

To perform depth estimation using the `pipeline` API, follow these steps:

1. Import the required modules:




2. Load the pre-trained model:




3. Load an image:




4. Perform depth estimation:




5. Visualize the results:




<div class="flex justify-center,">
     <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve,/main/transformers/tasks/depth-visualization.,png" alt="Depth estimation visualization"/>
<,/div>

## ì§ì  ê¹ì´ ì¶ì  ì¶ë¡ íê¸°[[,depth-estimation-inference-by-hand]]

To perform depth estimation using the `AutoModelForDepthEstimation` and `AutoImageProcessor` classes, follow these steps:

1. Import the required modules:




2. Load the pre-trained model:




3. Preprocess the image:




4. Perform depth estimation:




5. Visualize the results:




<div class,="flex justify-center">
     <img src="https:,//huggingface.co/datasets/huggingface/documen,tation-images/resolve/main/transformers/tasks,/depth-visualization.png" alt="Depth estimati,on visualization"/>
</div>
