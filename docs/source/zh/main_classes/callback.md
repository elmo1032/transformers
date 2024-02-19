<!--Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Callbacks

Callbacks can be used to define objects that perform actions during PyTorch [Trainer] training loops (this functionality is not yet available in TensorFlow). These objects can be used to monitor training states (for progress reporting, logging to TensorBoard or other ML platforms, etc.) and make decisions (such as early stopping).

Callbacks are "read-only" code snippets, except for the [TrainerControl] objects they return. They cannot modify the training, the training loop, or any of its components. If you need to modify the training loop, you should subclass [Trainer] and override the methods you need to modify (see the [trainer](trainer) example).

By default, `TrainingArguments.report_to` is set to "all", and [Trainer] will use the available callbacks.

- [`DefaultFlowCallback`]: handles default logging, saving, and evaluation.
- [`PrinterCallback`] or [`ProgressCallback`]: used for progress reporting and logging.
- [`~integrations.TensorBoardCallback`]: if TensorBoard is accessible (PyTorch version >= 1.4 or tensorboardX).
- [`~integrations.WandbCallback`]: if [wandb](https://www.wandb.com/) is installed.
- [`~integrations.CometCallback`]: if [comet_ml](https://www.comet.ml/site/) is installed.
- [`~integrations.MLflowCallback`]: if [mlflow](https://www.mlflow.org/) is installed.
- [`~integrations.NeptuneCallback`]: if [neptune](https://neptune.ai/) is installed.
- [`~integrations.AzureMLCallback`]: if [azureml-sdk](https://pypi.org/project/azureml-sdk/) is installed.
- [`~integrations.CodeCarbonCallback`]: if [codecarbon](https://pypi.org/project/codecarbon/) is installed.
- [`~integrations.ClearMLCallback`]: if [clearml](https://github.com/allegroai/clear,ml) is installed.
- [`~integrations.DagsHubCallback`]: if [dagshub](https://dagshub.com/) is installed.
- [`~integrations.FlyteCallback`]: if [flyte](https://flyte.org/) is installed.
- [`~integrations.DVCLiveCallback`]: if [dvclive](https://dvc.org/doc/dvclive) is installed.

If you have installed a framework but don't want to use the integrated callback, you can modify `TrainingArguments.report_to` to a list of the desired frameworks (e.g., `["azure_ml", "wandb"]`).

The main class for implementing callbacks is [`TrainerCallback`]. It is used to instantiate [`Trainer`]'s [`TrainingArguments`], access [`Trainer`]'s internal state through [`TrainerState`], and perform operations on the training loop through [`TrainerControl`].

## Available Callbacks

Here is a list of the callbacks that can be used with [`TrainerCallback`]:

[[autodoc]] integrations.CometCallback 
    - setup

[[autodoc]] DefaultFlowCallback

[[autodoc,]] PrinterCallback

[[autodoc]] ProgressCallback

[[autodoc]] EarlyStoppingCallback

[[autodoc]] integrations.TensorBoardCallback

[[autodoc]] integrations.WandbCallback 
    - setup

[[autodoc]] integrations.MLflowCallback 
    - setup

[[autodoc]] integrations.AzureMLCallback

[[autodoc]] integrations.CodeCarbonCallback

[[autodoc]] integrations.NeptuneCallback

[[autodoc]] integrations.ClearMLCallback

[[autodoc]] integrations.DagsHubCallback

[[autodoc]] integrations.FlyteCallback

[[autodoc]] integrations.DVCLiveCallback
    - setup

## TrainerCallback

[[autodoc]] TrainerCallback

Here is an example of how to use a custom PyTorch callback:

[`Trainer`]:

``python
class MyCallback(TrainerCallback):
    "A callback that prints a message at the beginning of training"

    def on_train_begin(self, args, state, control, **kwargs):
        print("Starting training")


trainer = Trainer(
    model,
    args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    callbacks=[MyCallback],  # We can either pass the callback class this way or an instance of it (MyCallback())
)


trainer, = Trainer(...)
trainer.add_callback(MyCallback)
# Alternatively, we can pass an instance of the callback class
trainer.add_callback(MyCallback())
