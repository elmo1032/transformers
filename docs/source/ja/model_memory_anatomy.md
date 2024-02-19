<!---
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache, License, Version 2.0 (the "License");
you may not use this file except in compliance with, the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/,LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS, IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS ,OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Model training anatomy

# In order to understand how to improve the inference speed of a model,
# it is important to understand how a GPU is used and how the throughput
# changes depending on the operations performed during training.

# First, let's look at an example and gather some evidence. The following
# dependencies are required:

# ```bash
# pip install transformers datasets accelerate nvidia-ml-py3
# ```
#
# `nvidia-ml-py3` library allows to get the GPU usage from Python.

# Next, we create some datasets. We use 100 to 30000 random integers as
# input_ids and labels with 512 sequence length. The data is then converted
# to PyTorch tensors and wrapped in a `Dataset` object.

import numpy as np
from datasets import Dataset

seq_len, dataset_size = 512, 512
dummy_data = {
    "input_ids": np.random.randint(100, 30000, (dataset_size, seq_len)),
    "labels": np.random.randint(0, 1, (dataset_size)),
}
ds = Dataset.from_dict(dummy_data)
ds.set_format("pt")

# We will use the `Trainer` class to train the model and get some metrics
# about the GPU utilization and throughput. First, we define two helper
# functions:

import pynvml

def print_gpu_utilization():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    print(f"GPU memory occupied: {info.used//1024**2} MB.")

def print_summary(result):
    print(f"Time: {result.metrics['train_runtime']:.2f}")
    print(f"Samples/second: {result.metrics['train_samples_per_second']:.2f}")
    print_gpu_utilization()

# Let's check if the GPU is free before starting:

print_gpu_utilization()

# Before training the model, let's move it to the GPU:

import torch

model = torch.ones((1, 1)).to("cuda")
print_gpu_utilization()

# Now, let's check if the model is using the GPU correctly by checking
# which tensors are on the GPU.

# ## Model's Operations Anatomy
#
# Transformer models consist of three main operations:
#
# 1. Matrix multiplication
# 2. Layer normalization
# 3. Activation functions
#
# Understanding how these operations affect memory and compute is crucial
# to optimize the model's performance.
#
# ## Model's Memory Anatomy
#
# When a model is run on a GPU, it uses several types of memory:
#
# 1. Model parameters
# 2. Optimizer state
# 3. Gradient accumulation
# 4. Activation checkpointing
# 5. Cache
# 6. Persistent layers
#
# Let's look at each of them in detail.
#
# ### Model parameters
#
# Model parameters take up the most memory in a model. They can be stored
# in either float32 or float16 format. The number of parameters depends
# on the model architecture.
#
# ### Optimizer state
#
# The optimizer state includes the momentum and learning rate for each
# parameter. It typically takes up a small fraction of the memory
# compared to the model parameters.
#
# ### Gradient accumulation
#
# Gradient accumulation is a technique used to train large models that
# do not fit in memory. The gradients are accumulated over multiple
# mini-batches before performing a weight update. This increases the
# memory requirements but reduces the number of weight updates.
#
# ### Activation checkpointing
#
# Activation checkpointing is a technique used to reduce memory usage
# during backpropagation. Instead of storing all activations for a model,
# only a subset of them is stored, and the rest are recomputed during
# backpropagation. This reduces memory usage but increases the compute
# requirements.
#
# ### Cache
#
# The cache is a small amount of memory used to speed up matrix
# multiplications. It is typically used in the self-attention layer.
#
# ### Persistent layers
#
# Persistent layers are layers that are kept in memory between forward
# passes. This can speed up training by avoiding the need to recompute
# the layer's parameters. However, it increases memory usage.
#
# Understanding how these different types of memory are used is crucial
# to optimize the model's performance.
