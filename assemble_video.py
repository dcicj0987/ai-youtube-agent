import ffmpeg

image = ffmpeg.input("thumbnail.png", loop=1, t=20)
audio = ffmpeg.input("audio.mp3")

output = ffmpeg.output(
    image, audio, "output.mp4",
    vcodec="libx264", acodec="aac", pix_fmt="yuv420p"
).run()

print("✔ Video Created!")
