"""Read the EXIF of every photo in a directory and write a CSV inventory.

Usage: python3 -I exif_inventory.py <photo_dir> <out_csv>
"""
import csv, os, sys
from datetime import datetime, timedelta, timezone
from PIL import Image, ExifTags

photo_dir, out_csv = sys.argv[1:3]
IFD = ExifTags.IFD
rows = []
gps_any = 0
makes = set()
for name in sorted(os.listdir(photo_dir)):
    p = os.path.join(photo_dir, name)
    with Image.open(p) as im:
        w, h = im.size
        ex = im.getexif()
        sub = ex.get_ifd(IFD.Exif)
        gps = ex.get_ifd(IFD.GPSInfo)
        if gps:
            gps_any += 1
        makes.add((ex.get(271), ex.get(272)))
        dto = sub.get(36867)            # DateTimeOriginal
        ss = sub.get(37521, '')         # SubSecTimeOriginal
        off = sub.get(36881, '')        # OffsetTimeOriginal
        orient = ex.get(274)
        exp = sub.get(33434); iso = sub.get(34855); fnum = sub.get(33437)
        wb = sub.get(41987); flen = sub.get(37386)
    t = datetime.strptime(dto, '%Y:%m:%d %H:%M:%S')
    if ss:
        t = t + timedelta(milliseconds=int(str(ss).strip()[:3].ljust(3, '0')))
    if off:
        sign = 1 if off[0] == '+' else -1
        hh, mm = off[1:].split(':')
        tz = timezone(sign * timedelta(hours=int(hh), minutes=int(mm)))
        t_utc = t.replace(tzinfo=tz).astimezone(timezone.utc)
    else:
        t_utc = None
    rows.append(dict(file=name, bytes=os.path.getsize(p), width=w, height=h, orientation=orient,
                     taken_local=t.isoformat(timespec='milliseconds'), utc_offset=off,
                     taken_utc=t_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' if t_utc else '',
                     exposure_s=float(exp) if exp else '', iso=iso, f_number=float(fnum) if fnum else '',
                     focal_mm=float(flen) if flen else '', white_balance=wb))
with open(out_csv, 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    wr.writeheader(); wr.writerows(rows)
print("photos:", len(rows), "with GPS IFD:", gps_any, "make/model:", makes)
