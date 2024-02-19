<!--Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# æ©å±èªå®ä¹æ¨¡å

ð¤ Transformers library is designed to be easily extendable. Each model's code is in its own sub-directory, with no 
further compilation required, so you can easily copy and paste model files and modify them as needed.

If you want to write your own model, starting from scratch might be easier. In this tutorial, we will show you how 
to write your own custom model, how to initialize it, how to push it to the ð¤ Transformers model hub, and how to 
share it with the community (even if it's not in the ð¤ Transformers library).

We will use the ResNet model as an example, and show you how to take a model from the timm library and convert it 
into a  [`PreTrainedModel`].

