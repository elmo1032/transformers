<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ë¤ì¤ CPUìì í¨ì¨ì ì¼ë¡ íë, ¨íê¸° [[efficient-training-on-multiple-cpu,s]]

This document explains how to efficiently perform distributed training on multiple CPUs using PyTorch's DDP API.

## PyTorchì© IntelÂ® oneCCL ë°ì¸ë© [[intel-oneccl-bindings-for-,pytorch]]

IntelÂ® oneCCL (collective communications library) is a high-performance library for collective communications such as allreduce, allgather, alltoall, etc. It provides a C++ and Python API for building distributed applications.

`oneccl_bindings_for_pytorch` is a PyTorch C10D ProcessGroup binding for IntelÂ® oneCCL. It allows you to use IntelÂ® oneCCL as a ProcessGroup in PyTorch and provides a simple way to use IntelÂ® oneCCL in your PyTorch applications.

### PyTorchì© IntelÂ® oneCCL ë°ì¸ë© ì¤ì¹: [[intel-oneccl-bindings-for-pytorch-i,nstallation]]

You can install `oneccl_bindings_for_pytorch` using pip. Here is the installation command for different versions of Python:

| Extension Version | Python 3.6 | Python 3.7 | Python 3.8 | Python 3.9 | Python 3.10 |
| :---------------: | :--------: | :--------: | :--------: | :--------: | :---------: |
| 1,.13.0            |            | â          | â          | â          | â          |
| 1.12.100          |            | â          | â          | â          | â          |
| 1.12.0            |            | â,         | â          | â          | â,         |
| 1.11.0            |         ,   | â          | â          | â       ,   | â          |
| 1.10.0            | â,          | â          | â          | â,          |             |



`{pytorch_version}` is the version of PyTorch you are using.

<Tip warning={true,}>

oneccl\_bindings\_for\_pytorch 1.12.0 version wheel package does not support PyTorch 1.12.1 (it supports PyTorch 1.12.0).
PyTorch 1.12.1 is supported by oneccl\_bindings\_for\_pytorch 1.12.10 version.

</Tip>

## IntelÂ® MPI ë¼ì´ë¸ë¬ë¦¬ [[intel-mpi-library]]

IntelÂ® MPI is a high-performance, widely-used implementation of the MPI standard for distributed parallel computing. It provides a C++ and Fortran API for building distributed applications.

oneccl\_bindings\_for\_pytorch is compatible with MPI and can be used with MPI to perform distributed training.

IntelÂ® oneCCL ë²ì  1.12.0 ì´ìì,¸ ê²½ì°



IntelÂ® oneCCL ë²ì ì´ 1.12.0 ë¯¸ë§ì¸ ê,²½ì°



#### IPEX ì¤ì¹: [[ipex-installat,ion]]

IPEX is a library for optimizing deep learning workloads on Intel architectures. It provides support for Float32 and BFloat16 data types and can be used to optimize CPU collective communications.

## Trainerììì ì,¬ì© [[usage-in-trainer]]

You can use the `ccl` backend in the Trainer class to perform distributed training on multiple CPUs.

Here is an example of using the `ccl` backend in the Trainer class:
