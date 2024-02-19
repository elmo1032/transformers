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

# Logging

ð¤ Transformers has a logging framework that allows you to easily configure the level of detail of the logs output by the library.

The current default log level is `WARNING`.

To increase the log level of detail, you can simply use a setter as shown below. For example, here's how to change the log level to INFO:




You can also use the `TRANSFORMERS_VERBOosity` environment variable to override the default log level. You can set it to one of the following levels: `debug`, `info`, `warning`, `error`, `critical`. For example:




Additionally, you can set the `TRANSFORMERS_NO_ADVISORY_WARNINGS` environment variable to `true` (e.g. `1`) to disable certain warnings. This will disable any advisory warnings logged using [`logger.warning_advice`]. For example:




Here's an example of how to use the logger in your own module or script:




This logging module provides the following methods, which can be used for logging as shown below:

- [`logging.get_verbosity`] is used to get the current log level of the logger.
- [`logging.set_verbosity`] is used to set the log level of the logger to the specified level.
- [`logging.get_logger`] is used to get the logger object.
- [`logging.disable_default_handler`] is used to disable the default handler.

By default, a progress bar is displayed when a model is loaded. You can use [`logging.disable_progress_bar`] and [`logging.enable_progress_bar`] to disable or enable the progress bar, respectively.

## `logging` vs `warnings`

Python has two commonly used logging frameworks: `logging`, which is a general-purpose logging framework, and `warnings`, which is used to perform more fine-grained classification of warnings in specific buckets, such as `FutureWarning` for deprecated features or paths, and `DeprecationWarning` for deprecated code.

In `transformers`, we use both of these frameworks simultaneously. We have modified the `logging` framework's `captureWarning` method to allow us to manage these warnings using the more detailed logging levels described above.

For library developers, this means that you should prefer to use `warnings` over `logging`, while `logging` should be used for general-purpose logging in your own projects.

Here is an example of how to use the `captureWarning` method:

[[autodoc]] logging.captureWarnings

## Base setters

These methods are used to set the log level of the logger.

[[autodoc]] logging.set_verbosity_error

[[autodoc]] logging.set_verbosity_warning

[[autodoc]] logging.set_verbosity_info

[[autodoc]] logging.set_verbosity_debug

## Other functions

These methods provide additional functionality for the logger.

[[autodoc]] logging.get_verbosity

[[autodoc]] logging.set_verbosity

[[autodoc]] logging.get_logger

[[autodoc]] logging.enable_default_handler

[[autodoc]] logging.disable_default_handler

[[autodoc]] logging.enable_explicit_format

[[autodoc]] logging.reset_format

[[autodoc]] logging.enable_progress_bar

[[autodoc]] logging.disable_progress_bar

