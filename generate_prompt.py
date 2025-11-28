import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

topic = "AI video tools 2025"

prompt = f"""
Generate a YouTube package for: {topic}
Return output as JSON with the following keys:
"title", "tags", "script"
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

data = json.loads(response["choices"][0]["message"]["content"])

# Save script.txt
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(data["script"])

# Save title and tags for upload stage
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump({"title": data["title"], "tags": data["tags"]}, f)

print("Script + Metadata generated!")
