# generate_prompt.py
import json
import random

# Trending short-style topic ideas
TOPICS = [
    "3 AI tools that will blow your mind 🤯",
    "How to grow on YouTube FAST 🚀",
    "Make money online using AI 💰",
    "Productivity hacks you must know ⚡",
    "Insane tech tricks no one tells you 🤖",
    "Smarter ways to study and learn faster 📚",
    "AI websites that feel illegal to use 😳",
]

topic = random.choice(TOPICS)

# Better YouTube Shorts title format
title = f"{topic} #shorts"

# Short-form tags (YouTube uses these to push Shorts)
tags = "ai,shorts,motivation,viral,youtube,growth,money,tech,productivity,lifehacks"

# Shorter punchy script (ideal for 20-40 sec videos)
script = f"""
{topic}

🔹 Tip 1: Start small — one new habit, tool, or workflow.
🔹 Tip 2: Stay consistent — daily action beats motivation.
🔹 Tip 3: Track progress — even small wins create momentum.

If this helped, hit like ❤️ and follow for more fast tips!
"""

# Remove extra whitespace
script = "\n".join(line.strip() for line in script.strip().splitlines())

# Save metadata.json (title + tags)
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump({"title": title, "tags": tags}, f, ensure_ascii=False, indent=2)

# Save text for TTS
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("✔ Generated Shorts script, title & tags")
print("Title:", title)
