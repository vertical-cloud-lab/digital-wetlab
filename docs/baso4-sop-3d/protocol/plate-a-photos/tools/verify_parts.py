"""Check every photo in the downloaded parts against the sha256 list made from the Drive zip.
Usage: python3 -E -P verify_parts.py <sha256_list> <part.zip> [...]
"""
import sys, zipfile, hashlib, os
want = {}
for line in open(sys.argv[1]):
    h, name = line.split(maxsplit=1)
    want[name.strip()] = h
seen = {}
for p in sys.argv[2:]:
    with zipfile.ZipFile(p) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            h = hashlib.sha256()
            with z.open(info) as f:
                for b in iter(lambda: f.read(1 << 20), b''):
                    h.update(b)
            name = os.path.basename(info.filename)
            assert info.filename == 'ot-2 experiment pics/' + name, info.filename
            assert name not in seen, 'duplicate ' + name
            seen[name] = h.hexdigest()
missing = sorted(set(want) - set(seen)); extra = sorted(set(seen) - set(want))
bad = sorted(n for n in seen if n in want and seen[n] != want[n])
print(f"in list: {len(want)}  in parts: {len(seen)}  missing: {len(missing)}  extra: {len(extra)}  sha256 mismatches: {len(bad)}")
sys.exit(1 if (missing or extra or bad) else 0)
