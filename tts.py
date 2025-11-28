from gtts import gTTS
import os

def create_voiceover(text, output_path="voice.mp3"):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(output_path)
    print("Voiceover saved:", output_path)

if __name__ == "__main__":
    # Load script from the text file created by generate_prompt.py
    with open("script.txt", "r", encoding="utf-8") as f:
        article = f.read()
        
    create_voiceover(article)
