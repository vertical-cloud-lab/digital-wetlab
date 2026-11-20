"""Preview images for the PR (EXIF-rotated, downscaled, saved without any metadata).
Usage: python3 -E -P previews.py <photo_dir> <inventory_csv> <out_dir>
"""
import csv, sys, os
from PIL import Image, ImageOps, ImageDraw, ImageFont
d, inv, out = sys.argv[1:4]
rows = list(csv.DictReader(open(inv)))
try:
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
    Fs = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
except OSError:
    F = Fs = ImageFont.load_default()

def load(name, maxpx):
    im = Image.open(os.path.join(d, name)); im.draft('RGB', (im.width // 2, im.height // 2))
    im = ImageOps.exif_transpose(im).convert('RGB'); im.thumbnail((maxpx, maxpx)); return im

def pair(a, b, la, lb, dst, maxpx=1100):
    A, B = load(a, maxpx), load(b, maxpx)
    W = A.width + B.width + 12; H = max(A.height, B.height) + 80
    s = Image.new('RGB', (W, H), 'white'); dr = ImageDraw.Draw(s)
    s.paste(A, (0, 0)); s.paste(B, (A.width + 12, 0))
    for x, lab in ((6, la), (A.width + 18, lb)):
        for k, line in enumerate(lab.split('\n')):
            dr.text((x, max(A.height, B.height) + 8 + 32 * k), line, fill='black', font=F)
    s.save(dst, quality=82, optimize=True); print(dst, s.size, os.path.getsize(dst))

pair('20261116_214935.jpg', '20261120_135140.jpg',
     '11-16 21:49 (04:49 UTC 11-17)\nafter the fill, no wrap yet',
     '11-20 13:51 (20:51 UTC)\nwrap off, after the 72 h',
     os.path.join(out, 'before_after_no_wrap.jpg'))
pair('20261116_220131.jpg', '20261119_221331.jpg',
     '11-16 22:01, under the wrap\n(the 2-minute series starts here)',
     '11-19 22:13, under the wrap\n(the last photo of the series)',
     os.path.join(out, 'series_first_last.jpg'))

# contact sheet: every 24th photo of the plate (48 min apart), plus the last two
sel = rows[1::24]
for r in rows[-2:]:
    if r not in sel: sel.append(r)
tw = 150; thumbs = []
for r in sel:
    im = Image.open(os.path.join(d, r['file'])); im.draft('RGB', (im.width // 8, im.height // 8))
    im = ImageOps.exif_transpose(im).convert('RGB'); im.thumbnail((tw, 2 * tw))
    thumbs.append((im, r['taken_local'][5:16].replace('T', ' ')))
th = max(t[0].height for t in thumbs) + 18; cols = 12; rws = -(-len(thumbs) // cols)
s = Image.new('RGB', (cols * (tw + 4), rws * (th + 4)), 'white'); dr = ImageDraw.Draw(s)
for k, (im, lab) in enumerate(thumbs):
    x, y = (k % cols) * (tw + 4), (k // cols) * (th + 4); s.paste(im, (x, y))
    dr.text((x + 2, y + im.height + 2), lab, fill='black', font=Fs)
dst = os.path.join(out, 'contact_sheet.jpg'); s.save(dst, quality=80, optimize=True)
print(dst, s.size, len(thumbs), os.path.getsize(dst))
