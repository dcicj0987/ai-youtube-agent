from gtts import gTTS

with open("script.txt", "r", encoding="utf-8") as f:
    text = f.read()

tts = gTTS(text)
tts.save("audio.mp3")

print("✔ Voice Generated!")
