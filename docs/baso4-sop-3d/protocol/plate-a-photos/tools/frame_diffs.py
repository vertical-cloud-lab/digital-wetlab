"""Mean absolute difference between consecutive photos (grayscale, 1/8 scale) to find moves.
Usage: python3 -E -P frame_diffs.py <photo_dir> <inventory_csv> <out_csv>
"""
import csv, sys
import numpy as np
from PIL import Image, ImageOps
d, inv, out = sys.argv[1:4]
rows = list(csv.DictReader(open(inv)))
prev = None; res = []
for r in rows:
    im = Image.open(f"{d}/{r['file']}"); im.draft('L', (im.width // 8, im.height // 8))
    a = np.asarray(ImageOps.exif_transpose(im).convert('L').resize((216, 288)), dtype=np.float32)
    res.append((r['file'], r['taken_local'], float(np.abs(a - prev).mean()) if prev is not None else '', float(a.mean())))
    prev = a
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['file', 'taken_local', 'mad_vs_previous', 'mean_gray']); w.writerows(res)
v = [x[2] for x in res[1:]]
print("median MAD", np.median(v), "p99", np.percentile(v, 99))
for x in sorted(res[1:], key=lambda x: -x[2])[:12]:
    print(f"  {x[0]}  MAD={x[2]:.2f}  mean={x[3]:.1f}")
