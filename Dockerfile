# Use an NVIDIA CUDA base image
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu20.04

# TZ shit
ENV DEBIAN_FRONTEND noninteractive

# Set a working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies
RUN pip3 install -U torch torchaudio moviepy openai-whisper==20230918

# Copy the Python script
COPY transcribe_video.py /app/

# Set the entry point to the Python script
ENTRYPOINT ["python3", "./transcribe_video.py"]
