from PIL import Image, ImageDraw, ImageFont
import json

with open("metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

title = data["title"]

img = Image.new("RGB", (1280, 720), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()

draw.text((50, 350), title[:35], font=font, fill=(255,255,255))

img.save("thumbnail.png")

print("✔ Thumbnail Created!")
