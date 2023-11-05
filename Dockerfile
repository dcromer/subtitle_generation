
# Use the latest stable version of the Python image
FROM python:3.10-slim

# Install ffmpeg which is required by moviepy for audio extraction
RUN apt-get update     && apt-get install -y ffmpeg     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install moviepy openai-whisper

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY transcribe_video.py .

# Set the entry point to the Python script
ENTRYPOINT ["python", "./transcribe_video.py"]
