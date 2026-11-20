"""Repack the Drive zip's photos, byte for byte, into N stored (uncompressed) zips.
Keeps each entry's name (folder included) and date_time, so extracting all parts
into one place gives back the same folder as the Drive zip.
Usage: python3 -E -P make_parts.py <drive.zip> <out_dir> <n_parts>
"""
import sys, zipfile, os, math
src, out, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
z = zipfile.ZipFile(src)
files = sorted((i for i in z.infolist() if not i.is_dir()), key=lambda i: i.filename)
per = math.ceil(len(files) / n)
for k in range(n):
    chunk = files[k * per:(k + 1) * per]
    a = os.path.basename(chunk[0].filename)[:15].replace('_', '-')
    b = os.path.basename(chunk[-1].filename)[:15].replace('_', '-')
    name = f"plate-a-photos_part{k+1}of{n}_{a}_to_{b}.zip"
    with zipfile.ZipFile(os.path.join(out, name), 'w', compression=zipfile.ZIP_STORED, allowZip64=True) as dst:
        for info in chunk:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.compress_type = zipfile.ZIP_STORED
            zi.external_attr = info.external_attr
            with z.open(info) as s, dst.open(zi, 'w', force_zip64=True) as d:
                while True:
                    buf = s.read(1 << 20)
                    if not buf: break
                    d.write(buf)
    print(name, len(chunk), os.path.getsize(os.path.join(out, name)))
