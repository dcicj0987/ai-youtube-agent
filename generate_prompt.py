import os, json
import requests

API_KEY = os.getenv("DEEPSEEK_API_KEY")

prompt = """
Create a viral YouTube Shorts content plan in JSON format:

{
"title": "catchy short title",
"tags": "tag1,tag2,tag3",
"script": "Short 20-30 second narration script"
}

Make it based on trending technology, AI, money making, motivation or viral useful hacks.
"""

response = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
)

# Handle API response safely
try:
    raw = response.json()["choices"][0]["message"]["content"]
except:
    print("❌ API Error:", response.text)
    raise SystemExit()

# Extract clean JSON from response
clean = raw[raw.find("{") : raw.rfind("}")+1]
data = json.loads(clean)

# Save metadata
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump({"title": data["title"], "tags": data["tags"]}, f)

# Script for TTS
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(data["script"])

print("✔ Metadata + Script Generated Successfully (DeepSeek)")
