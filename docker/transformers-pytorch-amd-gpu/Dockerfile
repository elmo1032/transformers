# Use ROCm dev image for Ubuntu 20.04 with ROCm version 5.6 as the base image
FROM rocm/dev-ubuntu-20.04:5.6

# Set the maintainer to Hugging Face
LABEL maintainer="Hugging Face"

# Define arguments for the base Python packages and ROCm version
ARG DEBIAN_FRONTEND=noninteractive
ARG PYTORCH='2.1.0'
ARG TORCH_VISION='0.16.0'
ARG TORCH_AUDIO='2.1.0'
ARG ROCM='5.6'

# Update package lists and install required dependencies
RUN apt update && \
    apt install -y --no-install-recommends git libsndfile1-dev tesseract-ocr espeak-ng python3 python3-dev python3-pip ffmpeg && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Install PyTorch, torchvision, and torchaudio with the specified versions
RUN python3 -m pip install torch==$PYTORCH torchvision==$TORCH_VISION torchaudio==$TORCH_AUDIO --index-url https://download.pytorch.org/whl/rocm$ROCM

# Install required packages for the project
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools ninja git+https://github.com/facebookresearch/detectron2.git pytesseract "itsdangerous<2.1.0"

# Set the working directory to the root directory
ARG REF=main
WORKDIR /

# Fetch the latest version of the transformers repository
ADD https://api.github.com/repos/huggingface/transformers/git/refs/heads/main version.json

# Checkout the specified reference of the transformers repository
RUN git clone https://github.com/huggingface/transformers && cd transformers && git checkout $REF

# Install the transformers package in editable mode with the required extras
RUN python3 -m pip install --no-cache-dir -e ./transformers[dev-torch,testing,video]

# Uninstall TensorFlow and Flax
