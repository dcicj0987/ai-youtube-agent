# assemble_video.py
import json
import os
from PIL import Image, ImageDraw

import subprocess

# Load script
with open("script.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = [l.strip() for l in data["script"].splitlines() if l.strip()][:6]

# Create slides folder
os.makedirs("slides", exist_ok=True)

# Create slide images
for i, text in enumerate(lines):
    img = Image.new('RGB', (1280, 720), color=(40, 40, 40))
    d = ImageDraw.Draw(img)
    d.text((60, 60), text, fill=(255, 255, 255))
    img.save(f"slides/slide_{i:02d}.png")

# Build ffmpeg input list
with open("frames.txt", "w") as f:
    for frame in sorted(os.listdir("slides")):
        if frame.endswith(".png"):
            f.write(f"file 'slides/{frame}'\nduration 2\n")
    f.write(f"file 'slides/{frame}'\n")  # last frame extra duration

# Create video from images
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "frames.txt",
    "-vsync", "vfr", "-pix_fmt", "yuv420p", "slides_video.mp4"
])

# Combine with audio
subprocess.run([
    "ffmpeg", "-y", "-i", "slides_video.mp4", "-i", "voice.mp3",
    "-c:v", "copy", "-c:a", "aac", "-shortest", "final_video.mp4"
])

print("Final video created: final_video.mp4")
