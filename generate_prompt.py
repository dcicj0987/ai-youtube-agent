# generate_prompt.py
import json
import random

# Simple offline topics – you can edit these anytime
TOPICS = [
    "3 AI tools that can save you hours every day",
    "How to grow a YouTube channel from zero",
    "Fast ways to make money online using AI",
    "Productivity hacks for students",
    "Simple tech tricks most people don't know",
]

topic = random.choice(TOPICS)

title = f"{topic} (in 60 seconds)"
tags = "ai,technology,productivity,youtube,growth,tips"

script = f"""
Welcome to this quick video! Today we’re talking about: {topic}.

Tip 1: Start small and focus on one tool or habit at a time.
Tip 2: Be consistent every day, even if it’s just 10–15 minutes.
Tip 3: Track your progress so you can see real improvement.

If you found this helpful, like the video and subscribe for more short, useful tips!
"""

# Clean up whitespace
script = "\n".join(line.strip() for line in script.strip().splitlines())

# Save metadata.json (for title & tags)
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump({"title": title, "tags": tags}, f, ensure_ascii=False, indent=2)

# Save script.txt (for TTS)
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("✔ Offline script + title + tags generated")
print("Title:", title)
