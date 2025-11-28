# generate_prompt.py
import json
import random

def get_trending_topics():
    # Example trending topics, you can later integrate Google Trends or YouTube trending API
    return [
        "AI video tools 2025",
        "Budget phones under 15000",
        "Fast home workouts",
        "Top 5 programming tips",
        "How to grow on YouTube"
    ]

def generate_script(topic):
    intro = f"Today we dive into {topic}. In this video, you'll learn the top 5 things."
    points = "\n".join([f"{i+1}. Key point about {topic}" for i in range(5)])
    outro = "Like and subscribe for more daily videos!"
    return f"{intro}\n\n{points}\n\n{outro}"

if __name__ == "__main__":
    topic = random.choice(get_trending_topics())
    script = generate_script(topic)
    data = {"topic": topic, "script": script}
    with open("script.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Script generated for topic:", topic)
                