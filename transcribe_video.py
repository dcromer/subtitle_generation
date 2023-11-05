
# transcribe_video.py
import sys
from pathlib import Path
from moviepy.editor import VideoFileClip
import whisper

# Ensure there is a command line argument
if len(sys.argv) < 2:
    print("Usage: python transcribe_video.py <video_path>")
    sys.exit(1)

# Parse the video file path from the command line
video_file_path = sys.argv[1]
video_path = Path(video_file_path)

# Step 1: Extract audio from video
print("Step 1: Extract audio from video")
video = VideoFileClip(video_file_path)
audio_path = video_path.with_suffix('.wav')
video.audio.write_audiofile(audio_path, verbose=False, logger=None)  # Suppress verbose output and logging

# Step 2: Transcribe audio with Whisper
print("Step 2: Transcribe audio with Whisper")
model = whisper.load_model("base.en")
result = model.transcribe(str(audio_path))

# Helper function to format timestamps for SRT
def format_timestamp(seconds):
    """Convert seconds to SRT timestamp format."""
    millisec = int((seconds % 1) * 1000)
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03}"

# Step 3: Generate SRT from transcription
print("Step 3: Generate SRT from transcription")
srt_content = []
for i, segment in enumerate(result['segments']):
    start = segment['start']
    end = segment['end']
    text = segment['text']

    if text is not None:
        text = text.strip()

    start_time = format_timestamp(start)
    end_time = format_timestamp(end)
    
    srt_content.append(f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n")

# Step 4: Save SRT content to file
print("Step 4: Save SRT content to file")
srt_output_path = video_path.with_suffix('.srt')
with open(srt_output_path, 'w') as file:
    file.write("".join(srt_content))

# Cleanup the temporary audio file
audio_path.unlink()
