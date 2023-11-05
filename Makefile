# Define the Docker image name
IMAGE_NAME := video_transcriber

# Path to the video file
VIDEO_FILE ?= video_file.mp4

.PHONY: build run shell

# Target to build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Target to run the transcribe_video function
run:
	docker run --rm --gpus all -v $(PWD):/app/files $(IMAGE_NAME) files/$(VIDEO_FILE)

# Target to open a new container with an interactive shell
shell:
	docker run --rm -it --gpus all --entrypoint /bin/bash -v $(PWD):/app $(IMAGE_NAME)
