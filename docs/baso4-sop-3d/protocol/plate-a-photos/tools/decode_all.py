"""Decode every photo in the release's zips in full, to check that none is cut short or damaged.
Usage: python -I decode_all.py <part.zip> [...]    (needs Pillow; reads the zips, extracts nothing to disk)
A photo fails if Pillow can't decode the whole image or warns while doing so. The phone (a Samsung) appends its
own trailer after the JPEG data, ending in 'SEFT'; Pillow ignores it, and the script counts the photos that have it.
"""
import sys, io, os, zipfile, warnings
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = False


def check(args):
    zpath, name = args
    warnings.simplefilter('error')
    with zipfile.ZipFile(zpath) as zf:
        data = zf.read(name)
    try:
        with Image.open(io.BytesIO(data)) as im:
            fmt, size = im.format, im.size
            im.load()
    except Exception as e:
        return name, None, None, False, f'{type(e).__name__}: {e}'
    return name, fmt, size, data.endswith(b'SEFT'), ''


def main():
    jobs = []
    for z in sys.argv[1:]:
        with zipfile.ZipFile(z) as zf:
            jobs += [(z, i.filename) for i in zf.infolist() if not i.is_dir()]
    bad, sizes, fmts, trailers = [], {}, {}, 0
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as ex:
        for name, fmt, size, trailer, problem in ex.map(check, jobs, chunksize=8):
            if problem:
                bad.append((name, problem))
            sizes[size] = sizes.get(size, 0) + 1
            fmts[fmt] = fmts.get(fmt, 0) + 1
            trailers += trailer
    print(f"photos decoded: {len(jobs)}; formats: {fmts}; pixel sizes: {sizes}; with the Samsung trailer: {trailers}")
    print(f"photos that failed: {len(bad)}")
    for b in bad[:20]:
        print('  ', b)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
