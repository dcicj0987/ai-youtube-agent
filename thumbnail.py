from PIL import Image, ImageDraw, ImageFont
import json

# Load title for thumbnail
with open("metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

title = data["title"]

# Create thumbnail canvas
img = Image.new("RGB", (1280, 720), "#222831")  # dark background
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 80)

# Title text centered
w, h = draw.textsize(title, font=font)
draw.text(((1280-w)/2, (720-h)/2), title, fill="white", font=font)

img.save("thumbnail.jpg")
print("Thumbnail created: thumbnail.jpg")
