"""Build photos.csv (one row per photo) and SHA256SUMS.txt for plate A's photos.
Usage: python3 -E -P manifest.py <inventory_csv> <photo_sha256_list> <parts_sha256> <part_dir> <frame_diffs_csv> <out_dir>
"""
import csv, sys, os, zipfile
from datetime import datetime
inv, shalist, partsha, partdir, diffs, out = sys.argv[1:7]
rows = list(csv.DictReader(open(inv)))
sha = {l.split()[1]: l.split()[0] for l in open(shalist)}
part_of = {}
for p in sorted(os.listdir(partdir)):
    with zipfile.ZipFile(os.path.join(partdir, p)) as z:
        for i in z.infolist():
            if not i.is_dir():
                part_of[os.path.basename(i.filename)] = p
mad = {r['file']: r['mad_vs_previous'] for r in csv.DictReader(open(diffs))}
t0 = datetime.fromisoformat(rows[1]['taken_local'])   # first photo of the plate
notes = {
    '20261116_214509.jpg': 'test shot of a bench, not the plate (no UTC offset in its EXIF)',
    '20261116_214935.jpg': 'first photo of the plate; no plastic wrap yet',
    '20261116_215131.jpg': 'no plastic wrap yet; phone re-aimed',
    '20261116_215531.jpg': 'first with the plastic wrap on; phone closer',
    '20261117_022931.jpg': 'last before a 10.6 h gap with no photos',
    '20261117_130531.jpg': 'first after the 10.6 h gap',
    '20261117_170532.jpg': 'last before a 15.9 h gap with no photos',
    '20261118_085731.jpg': 'first after the 15.9 h gap',
    '20261119_221331.jpg': 'last of the 2-minute series',
    '20261120_135140.jpg': 'taken on 11-20 after the plastic wrap came off; not part of the 2-minute series',
}
fields = ['file', 'part', 'bytes', 'sha256', 'taken_local', 'taken_utc', 'hours_since_first_plate_photo',
          'exposure_s', 'iso', 'view_jump', 'note']
with open(os.path.join(out, 'photos.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
    for r in rows:
        t = datetime.fromisoformat(r['taken_local'])
        m = mad.get(r['file'], '')
        jump = 'yes' if (m not in ('', None) and float(m) >= 5.0 and r['file'] not in (rows[0]['file'], rows[1]['file'])) else ''
        w.writerow(dict(file=r['file'], part=part_of[r['file']].split('_')[1], bytes=r['bytes'], sha256=sha[r['file']],
                        taken_local=r['taken_local'] + (r['utc_offset'] or ''),
                        taken_utc=r['taken_utc'], hours_since_first_plate_photo=f"{(t - t0).total_seconds() / 3600:.3f}",
                        exposure_s=f"{float(r['exposure_s']):.6f}", iso=r['iso'], view_jump=jump,
                        note=notes.get(r['file'], '')))
with open(os.path.join(out, 'SHA256SUMS.txt'), 'w') as f:
    f.write('# The four zips in the draft release plate-a-photos\n')
    f.writelines(open(partsha).readlines())
    f.write('# Every photo (the same bytes as in the Drive zip and in the parts)\n')
    f.writelines(open(shalist).readlines())
print('rows', len(rows), 'parts', sorted(set(v.split('_')[1] for v in part_of.values())))
