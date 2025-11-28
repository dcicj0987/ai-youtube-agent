import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Generate a YouTube short idea and return this in JSON format:
{
"title": "...",
"tags": "...",
"script": "..."
}
The content should be engaging, short, viral and trending.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.8
)

result = response.choices[0].message.content

# Extract clean JSON
clean = result[result.find("{") : result.rfind("}") + 1]

with open("metadata.json", "w", encoding="utf-8") as f:
    f.write(clean)

data = json.loads(clean)

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(data["script"])

print("✔ Generated Title, Tags & Script")
