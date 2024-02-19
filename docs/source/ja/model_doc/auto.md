<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Auto Classes

In many cases, the class names and identifiers of pretrained models can be used to automatically detect and load 
the corresponding models and tokenizers. This functionality is provided by the following classes, which automatically 
discover the corresponding classes and models when you specify their names or identifiers.

[`AutoConfig`]: Automatically instantiate a config object from a pretrained model config name or identifier.

[`AutoModel`]: Automatically instantiate a model from a pretrained model name or identifier.

[`AutoTokenizer`]: Automatically instantiate a tokenizer from a pretrained tokenizer name or identifier.

## Customizing AutoClasses

You can add your own models and configs to the AutoClasses by using the following methods:




After registering your config and model, you can use them with the AutoClasses as usual!

<Tip warning={true}>

