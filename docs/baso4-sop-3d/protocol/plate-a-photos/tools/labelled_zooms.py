"""Labelled close-ups of the 11-20 photo (no EXIF). Well centres were read by eye from the
plate's moulded labels and checked against the empty wells (D1, D2, C3, D4, F3).
Usage: python3 -E -P labelled_zooms.py <photo_20261120_135140.jpg> <hand_fill_drops.csv> <out_dir>
"""
import csv, sys, os
from PIL import Image, ImageOps, ImageDraw, ImageFont
p, mapcsv, out = sys.argv[1:4]
m = {r['well']: r for r in csv.DictReader(open(mapcsv))}
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
STRONG = {'E1', 'F4', 'G5', 'A6', 'G2', 'B5', 'D11', 'E4', 'D6', 'B10', 'D12', 'B12', 'C2', 'C4', 'F12', 'E5'}
CTRL = {'D5', 'C7', 'G8', 'A9'}
views = {
  'final_zoom_D-H_3-6.jpg': ((1300, 2500, 3100, 3750), 1600, {
     'D6': (100, 230), 'E6': (350, 195), 'F6': (610, 165), 'G6': (870, 150), 'H6': (1145, 130),
     'D5': (110, 490), 'E5': (380, 465), 'F5': (640, 440), 'G5': (900, 420), 'H5': (1185, 385),
     'D4': (150, 760), 'E4': (415, 730), 'F4': (680, 700), 'G4': (945, 680), 'H4': (1225, 650),
     'D3': (180, 1000), 'E3': (445, 985), 'F3': (705, 960), 'G3': (970, 945), 'H3': (1250, 925)}),
  'final_zoom_A-F_1-6.jpg': ((350, 2450, 2350, 4450), 1500, {
     'A1': (290, 1330), 'B1': (500, 1315), 'C1': (715, 1300), 'D1': (925, 1290), 'E1': (1135, 1280), 'F1': (1355, 1265),
     'A2': (265, 1135), 'B2': (480, 1125), 'C2': (690, 1115), 'D2': (900, 1100), 'E2': (1115, 1090), 'F2': (1335, 1075),
     'A3': (240, 930), 'B3': (450, 920), 'C3': (660, 905), 'D3': (870, 890), 'E3': (1090, 875), 'F3': (1310, 860),
     'A4': (215, 715), 'B4': (425, 700), 'C4': (630, 685), 'D4': (845, 670), 'E4': (1060, 650), 'F4': (1280, 640),
     'A5': (190, 500), 'B5': (400, 485), 'C5': (600, 470), 'D5': (815, 455), 'E5': (1035, 435), 'F5': (1250, 415),
     'A6': (160, 295), 'B6': (370, 275), 'C6': (580, 255), 'D6': (795, 235), 'E6': (1010, 215), 'F6': (1230, 195)}),
}
for name, (box, size, wells) in views.items():
    c = im.crop(box); c.thumbnail((size, size)); dr = ImageDraw.Draw(c)
    for w, (x, y) in wells.items():
        if w not in m: col, lab = (170, 170, 170), f'{w} empty'
        elif w in CTRL: col, lab = (255, 255, 255), f'{w} control'
        elif w in STRONG: col, lab = (255, 150, 0), w
        else: col, lab = (90, 200, 255), w
        tx, ty = x - 40, y - 78
        bb = dr.textbbox((tx, ty), lab, font=F)
        dr.rectangle((bb[0] - 3, bb[1] - 2, bb[2] + 3, bb[3] + 2), fill=(0, 0, 0))
        dr.text((tx, ty), lab, fill=col, font=F)
    dst = os.path.join(out, name); c.save(dst, quality=85, optimize=True); print(dst, c.size, os.path.getsize(dst))
