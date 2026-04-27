#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

def make_icon(size):
    img = Image.new('RGB', (size, size), '#0f0f0f')
    draw = ImageDraw.Draw(img)

    pad = size // 7
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=size // 5,
        fill='#7fff7f'
    )

    fs = int(size * 0.42)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', fs)
    except:
        font = ImageFont.load_default()

    text = 'M'
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) // 2 - bbox[0]
    y = (size - th) // 2 - bbox[1]
    draw.text((x, y), text, fill='#0f0f0f', font=font)

    img.save(f'icons/icon-{size}.png')
    print(f'  icon-{size}.png 作成完了')

print('アイコンを生成中...')
make_icon(192)
make_icon(512)
print('完了！')
