<!--
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Export to ONNX

ð¤ Transformers models can be exported to ONNX format to be used in specific environments such as production. ð¤ Optimum provides exporters to convert PyTorch or TensorFlow models to ONNX or TFLite format. ð¤ Optimum also provides optimization tools to improve the performance of the models in inference.

In this notebook, we will show how to export a ð¤ Transformers model to ONNX format and how to use it with ONNX Runtime. We will also show how to convert the model to TFLite format.

## Export to ONNX

[ONNX](http://onnx.ai) is an open format built to represent machine learning models. ONNX defines a common set of operators - the building blocks of machine learning and deep learning models - and a common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes, and compilers.

ONNX models can be executed in many different runtimes such as ONNX Runtime, TensorRT, Core ML, and others.

### Exporting a ð¤ Transformers model to ONNX

To export a ð¤ Transformers model to ONNX format, you can use the `pipeline` API or the `save_model` method.

#### Using the `pipeline` API

The `pipeline` API is a high-level interface to use ð¤ Transformers models. It automatically handles the tokenization, the encoding and the decoding of the inputs and outputs.

Here is an example of how to export a ð¤ Transformers model to ONNX format using the `pipeline` API:




#### Using the `save_model` method

The `save_model` method allows you to save a ð¤ Transformers model to disk. You can use it to save the model to ONNX format.

Here is an example of how to export a ð¤ Transformers model to ONNX format using the `save_model` method:




### Using the ONNX model

Once the model is exported to ONNX format, you can use it with any runtime that supports ONNX. Here is an example of how to use the ONNX model with ONNX Runtime:




You can also use the ONNX model with other runtimes such as TensorRT, Core ML, and others.

## Export to TFLite

To convert the ONNX model to TFLite format, you can use the `tf2onnx` and `tensorflow` libraries.

Here is an example of how to convert the ONNX model to TFLite format:




Once the model is converted to TFLite format, you can use it with any runtime that supports TFLite such as TensorFlow Lite, TensorFlow Lite for Microcontrollers, and others.

