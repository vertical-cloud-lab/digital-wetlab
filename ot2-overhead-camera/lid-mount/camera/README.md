# Focusing and lining up the lid camera

The lessons from the first build, trimmed from the full log in byu-vcl
([`camera/README.md` at `49677cf`](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/README.md),
908 lines, 2026-10-15 to 2026-10-30, with stills and measurements). Getting that camera sharp took
two weeks. Almost all of that time went into one mistake: **no 5 mm spacer between the camera and
the lens.** Read [The lens stack](#the-lens-stack-fit-one-5-mm-ccs-spacer) before fitting the lens.

| File | What |
|---|---|
| [`preview_server.py`](preview_server.py) | Live MJPEG preview in a browser over the tailnet, with a focus score, using the whole sensor. Needs the stream stopped (`sudo systemctl stop device.service`). `python3 preview_server.py --minutes 90` |
| [`measure_still.py`](measure_still.py) | Turns a full-resolution still into how far to slide and turn the mount: fits the deck rails to the slot pitch, or `--plate 7` fits a 96-well plate's wells. Needs `opencv-python` and `numpy` |
| [`stream/`](stream/README.md) | The YouTube stream, which also serves full-resolution stills on the Pi while it runs: `curl -s localhost:8081/still > still.jpg` |

## The lens stack: fit one 5 mm C–CS spacer

From the deck down, the stack is: the camera board; the camera's mount with its knurled
**back-focus ring** (held by a small **lock screw**); **one 5 mm C–CS spacer**; then the lens.

- The Waveshare 8–50 mm is a **C-mount** lens and the HQ Camera is a **CS-mount** body. A C-mount
  lens needs 17.53 mm from its flange to the sensor; CS-mount is 12.5 mm. The knurled ring alone
  moves the lens only about 5 mm (5.5 turns of about 0.9 mm), so it cannot make up the difference.
  Raspberry Pi's [product brief](https://datasheets.raspberrypi.com/hq-camera/hq-camera-product-brief.pdf)
  gives 12.5–22.4 mm of back focus *including* the adapter.
- The CS-mount HQ Camera ships with a C–CS adapter, and Waveshare lists one in this lens's box. In
  the first build it was never fitted. The lens was screwed straight into the knurled ring, and
  focus ran out at the NEAR end at every zoom.
- **What worked (2026-10-30, sharp on 2026-11-01):** camera → knurled ring → 5 mm spacer → lens.
  The spacer was a printed ring, [`../exports/c_cs_spacer_A.stl`](../exports/c_cs_spacer_A.stl) or
  `_B.stl` (made by [`../cad/c_cs_spacer.py`](../cad/c_cs_spacer.py), 1"-32 UN threads both ends:
  A tighter, one notch on the rim; B looser, two notches). An aluminium ring,
  [Amazon B09STVLLVY](https://www.amazon.com/dp/B09STVLLVY) (two for $6.99), was ordered to
  replace it. Use the adapter from the box, or the aluminium ring, in preference to a printed one:
  PLA creeps when warm and the lens hangs from this thread next to the Pi.
- **The printed ring has a roof.** It prints lens face down, with a 0.4 mm disc bridged across the
  bore to build the threaded end on. Cut the disc out with a hobby knife before fitting it.
- **The knurled ring comes off with the lens** if you unscrew the lens without holding the ring.
  That is what made the printed spacer seem the wrong size on 2026-10-30: the knurled ring was on
  the lens, not in the camera. Tighten the lock screw, or hold the knurled ring, before taking the
  lens off.
- **Only about 6 mm more fits under the deck.** With one 5 mm spacer and the knurled ring all the
  way out, the lens front is about 1.6 mm above the window. Two spacers would push on the window.
  If more spacing is ever needed, raise the deck on printed risers first. After any change, set
  the mount down gently: if the base rocks, the lens is touching the window.

### Putting the stack together

Keep the camera pointing down while it is open, so dust can't fall onto the sensor's filter glass.
"Clockwise" means as you look up into the camera; every thread here is right-handed. Support the
lens throughout.

1. Screw the knurled ring into the camera, threaded end first, by finger: counter-clockwise until
   the thread drops into place, then clockwise until it stops. If it stiffens within the first turn
   it is cross-threaded; back it out and start again. Leave the lock screw loose.
2. Screw the spacer's narrow threaded end into the knurled ring, clockwise, until its flange meets
   the ring.
3. Screw the lens into the spacer's wide side, clockwise, until its silver rim meets the spacer or
   it stops. Don't force it: aluminium threads gall, and printed ones strip.
4. Focus as below. If the plate is sharpest with the focus ring at NEAR and still soft, turn the
   knurled ring out a turn at a time (about 0.9 mm each), refocusing each time; if sharpest at FAR,
   turn it in. Tighten the lock screw at the end.

**Touching the ribbon cable or taking the camera board off the deck:** shut the Pi down and unplug
it first (one short press of the Pi 5's power button, wait for the red LED, unplug USB-C).
Stopping `device.service` is not enough; the connector stays powered. Lens-side work can be done
with everything running.

**Record the final settings.** The first build reached sharp focus on 2026-11-01, but nobody
wrote down the zoom, iris and focus positions, the knurled ring's turns or which spacer was in.
Photograph the barrel and note them in the rebuild issue when this one is done.

## Setting the zoom, iris and focus rings

From the camera down the rings are **focus** (NEAR / FAR), **iris** (OPEN / CLOSE) and **zoom**
(TELE / WIDE), the big ribbed ring just above the window. Each thumbscrew rides between the two
words printed on the barrel, which read upside down because the lens hangs front-down. Loosen a
thumbscrew about a turn (don't take it out), push it toward the word you want, and retighten it
finger tight. The stream runs 5–20 s behind the lens, so make one small move, then wait.

1. **Zoom to the WIDE end first.** Focus is easiest to find there.
2. **Iris about halfway** (about f/4), not fully open. Fully open, the sharp zone is so thin that a
   stream running 5–20 s behind skips past it.
3. **Focus in small nudges:** 1–2 mm at the thumbscrew, then wait about 20 s. Keep going while the
   picture and the focus number get better; when they get worse, go back one nudge.
4. **Zoom in a little, refocus, repeat:** this lens is varifocal, so every zoom move throws focus
   away. Go a few millimetres toward TELE at a time, refocusing as in 3, until the plate fills the
   orange box (about 27–28 mm).
5. **Iris to about f/8, then tighten all three thumbscrews.** At f/8 the depth of field is about
   24 mm, enough for the wells' rims and the liquid below them.
6. **Never sharp, even at WIDE?** No ring can fix that: check [the lens stack](#the-lens-stack-fit-one-5-mm-ccs-spacer).

Don't close the iris to hide blur while focusing. It makes the sharp point harder to find and
drives the camera to its gain limit, where the picture and the focus score are noise. Turn the
room lights and the OT-2's rail lights on first; under room light alone the camera sat at maximum
exposure and gain.

## Use the whole sensor

The live view must cover the same field as a still, or slots at the edges look cut off when they
aren't. A 16:9 output makes libcamera crop the IMX477 to `ScalerCrop (108, 440, 3840, 2160)`,
71 % of the sensor's height, which at 8 mm zoom hides the front and back 52 mm of the deck.
`preview_server.py` here forces the 2028 × 1520 binned mode (`ScalerCrop (2, 0, 4052, 3040)`), and
the stream uses 4:3 outputs (1920 × 1440 from the full 4056 × 3040 readout) for the same reason.

## Lining it up over the plate: slide, zoom, focus, centre and square, lock

**The goal is one plate, close up**, not the whole deck: about 27.7 mm of zoom over the plate being
measured, which gives 29.4 px/mm and about 200 px across a well in a 4056 × 3040 still, with about
5 mm of deck either side of the plate. The first build used the plate in **slot 7**; the mount fits
over slots 4–11 ([`../README.md` §3](../README.md#3-where-on-the-lid)).

With `SETUP_OVERLAY = True` in `my_secrets.py` the stream shows an **orange cross** through the
middle of the picture, an **orange box** (`SETUP_BOX = (0.927, 0.828)`) where a 96-well plate's
outline lands at the target zoom, and `focus N (best M in 2 min)` under the timestamp.

1. **Slide the mount over the plate** until the cross lands on the middle of the plate (between
   wells D6, D7, E6 and E7), within about 5 mm. Keep the arrow on the base pointing at the door.
2. **Zoom in until the plate fills the box**, refocusing as you go
   ([the rings](#setting-the-zoom-iris-and-focus-rings)). If the plate runs out of the box on one
   side as it grows, slide the mount that way.
3. **Focus**, then close the iris to about f/8.
4. **Centre and square.** Nudge the mount until the plate sits evenly in the box, then turn it until
   the plate's edges run parallel to the box's. At this zoom 1 mm of deck is 14 px on the stream.
5. **Lock and check.** Tighten the thumbscrews and tape the base down
   ([phase 1](../README.md#4-install-phase-1-tape-no-cutting)). Take a still and run
   `python measure_still.py still.jpg --plate 7`: done when the plate's centre is within about
   2 mm of the picture's centre and the rotation is under 0.5°. Then set
   `SETUP_OVERLAY = False` and restart the stream once.

[`../cad/setup_video.py`](../cad/setup_video.py) renders a labelled video of these steps from a
measured still (`--slot` for another slot). The first build's video is in byu-vcl
([`setup_steps.mp4`](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/renders/setup_steps.mp4)),
along with a lens-ring video ([`lens_rings.mp4`](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/renders/lens_rings.mp4)).
