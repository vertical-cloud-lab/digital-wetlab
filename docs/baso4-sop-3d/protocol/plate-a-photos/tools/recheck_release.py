"""Check a fresh download of the draft release plate-a-photos against the lists committed in this folder.
Usage: python3 -I recheck_release.py <SHA256SUMS.txt> <photos.csv> <download dir>
Standard library only. Checks that the release's own SHA256SUMS.txt and photos.csv are the same as git's,
that each zip's sha256 matches, that each zip passes its CRC test, and that every photo's sha256, size and
part match, with none missing, extra or duplicated. Exits 1 on any problem.
"""
import sys, os, csv, hashlib, zipfile

git_sums, git_csv, dl = sys.argv[1:4]


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''):
            h.update(b)
    return h.hexdigest()


zips, photos, section = {}, {}, None
for line in open(git_sums):
    if line.startswith('#'):
        section = 'zips' if 'zips' in line else 'photos'
        continue
    h, name = line.split(maxsplit=1)
    (zips if section == 'zips' else photos)[name.strip()] = h
rows = list(csv.DictReader(open(git_csv)))
sizes = {r['file']: int(r['bytes']) for r in rows}
part_of = {r['file']: r['part'] for r in rows}
print(f"lists in git: {len(zips)} zips, {len(photos)} photos; photos.csv rows: {len(rows)}")

ok = True
for side, gitp in (('SHA256SUMS.txt', git_sums), ('photos.csv', git_csv)):
    same = sha_file(os.path.join(dl, side)) == sha_file(gitp)
    print(f"release {side} the same as git's: {same}")
    ok &= same

present = sorted(f for f in os.listdir(dl) if f.endswith('.zip'))
print(f"zips downloaded: {len(present)}; names as listed: {set(present) == set(zips)}")
ok &= set(present) == set(zips)

seen, nbytes = {}, 0
for z in present:
    zh = sha_file(os.path.join(dl, z))
    print(f"{z}: sha256 {'OK' if zh == zips[z] else 'MISMATCH ' + zh}")
    ok &= zh == zips[z]
    with zipfile.ZipFile(os.path.join(dl, z)) as zf:
        bad = zf.testzip()
        print(f"  CRC test: {'OK' if bad is None else 'BAD at ' + bad}")
        ok &= bad is None
        n = 0
        for info in zf.infolist():
            if info.is_dir():
                continue
            name = os.path.basename(info.filename)
            assert info.filename == 'ot-2 experiment pics/' + name, info.filename
            assert name not in seen, 'duplicate ' + name
            h = hashlib.sha256()
            with zf.open(info) as f:
                for b in iter(lambda: f.read(1 << 22), b''):
                    h.update(b)
            seen[name] = (h.hexdigest(), info.file_size, z)
            nbytes += info.file_size
            n += 1
        print(f"  photos in it: {n}")

missing = sorted(set(photos) - set(seen))
extra = sorted(set(seen) - set(photos))
bad_sha = sorted(n for n in seen if n in photos and seen[n][0] != photos[n])
bad_size = sorted(n for n in seen if n in sizes and seen[n][1] != sizes[n])
bad_part = sorted(n for n in seen if n in part_of and '_' + part_of[n] + '_' not in seen[n][2])
print(f"photos: {len(seen)} found, {len(missing)} missing, {len(extra)} extra")
print(f"sha256 mismatches: {len(bad_sha)}; size mismatches: {len(bad_size)}; in the wrong part: {len(bad_part)}")
print(f"photo bytes: {nbytes:,}")
ok &= not (missing or extra or bad_sha or bad_size or bad_part)
print('ALL OK' if ok else 'PROBLEMS FOUND')
sys.exit(0 if ok else 1)
