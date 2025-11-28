# tts.py
import pyttsx3
import json

with open("script.json", "r", encoding="utf-8") as f:
    data = json.load(f)

script = data["script"]

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.save_to_file(script, 'voice.mp3')
engine.runAndWait()

print("Voice saved as voice.mp3")
