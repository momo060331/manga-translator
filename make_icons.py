#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

def make_icon(size):
    img = Image.new('RGB', (size, size), '#0a0a0a')
    draw = ImageDraw.Draw(img)

    # Background rounded square feel - draw accent rectangle
    margin = size // 8
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size // 6,
        fill='#e8ff47'
    )

    # Draw "M" letter
    font_size = int(size * 0.45)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()

    text = 'M'
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) // 2 - bbox[0]
    y = (size - th) // 2 - bbox[1]
    draw.text((x, y), text, fill='#0a0a0a', font=font)

    img.save(f'icons/icon-{size}.png')
    print(f'Created icon-{size}.png')

make_icon(192)
make_icon(512)
print('Icons created successfully!')
