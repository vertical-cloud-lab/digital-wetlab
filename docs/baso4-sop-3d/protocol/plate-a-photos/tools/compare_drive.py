"""Compare every file in Tim's Drive zip with the release's four zips: name, bytes (sha256) and the date stored in the zip.
Usage: python3 -I compare_drive.py <drive.zip> <part.zip> [...]
Standard library only. Exits 1 if any file in either is missing from the other, or differs.
"""
import sys, zipfile, hashlib


def entries(path):
    out, dirs = {}, []
    with zipfile.ZipFile(path) as z:
        for i in z.infolist():
            if i.is_dir():
                dirs.append(i.filename)
                continue
            h = hashlib.sha256()
            with z.open(i) as f:
                for b in iter(lambda: f.read(1 << 22), b''):
                    h.update(b)
            assert i.filename not in out, 'duplicate ' + i.filename
            out[i.filename] = (h.hexdigest(), i.file_size, i.date_time)
    return out, dirs


drive, ddirs = entries(sys.argv[1])
rel = {}
for p in sys.argv[2:]:
    e, _ = entries(p)
    assert not set(e) & set(rel), 'a file in two parts'
    rel.update(e)
kinds = {}
for n in drive:
    base = n.rsplit('/', 1)[-1]
    k = base.rsplit('.', 1)[-1].lower() if '.' in base else '(none)'
    kinds[k] = kinds.get(k, 0) + 1
print(f"Drive zip: {len(drive)} files {kinds}, folders {ddirs}; release parts: {len(rel)} files")
missing = sorted(set(drive) - set(rel))
extra = sorted(set(rel) - set(drive))
diff = sorted(n for n in drive if n in rel and drive[n][0] != rel[n][0])
dt = sorted(n for n in drive if n in rel and drive[n][2] != rel[n][2])
print(f"in Drive but not in the release: {len(missing)} {missing[:5]}")
print(f"in the release but not in Drive: {len(extra)} {extra[:5]}")
print(f"different bytes: {len(diff)}; different date in the zip: {len(dt)}")
print(f"bytes in the Drive zip's files: {sum(v[1] for v in drive.values()):,}")
ok = not (missing or extra or diff)
print('EVERY FILE IN THE DRIVE ZIP IS IN THE RELEASE, BYTE FOR BYTE' if ok else 'PROBLEMS FOUND')
sys.exit(0 if ok else 1)
