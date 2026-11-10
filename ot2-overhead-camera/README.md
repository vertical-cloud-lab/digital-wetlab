# OT-2 overhead camera

A **Raspberry Pi HQ Camera (IMX477) with an 8–50 mm C-mount zoom**, looking straight down through
the OT-2's top window at one 96-well plate, on a printed mount with a **Raspberry Pi 5** on top.
The Pi streams the deck to YouTube, serves full-resolution stills while it streams, and is also
**the OT-2's network link**: the robot's Ethernet cable goes to this Pi, and everything that talks
to the robot runs on it.

**Status, 2026-11-10: to be rebuilt.** The first Pi 5, HQ Camera and zoom lens were given to the
Borys lab at the University of Utah on 2026-11-10. This folder holds what is needed to build the
replacement from new parts. The rebuild is tracked in an issue in this repo, "Rebuild the OT-2
overhead camera and network-link Pi", with the parts list and checkboxes.

## Where this came from

| From | What |
|---|---|
| byu-vcl [PR 234](https://github.com/vertical-cloud-lab/byu-vcl/pull/234) at [`49677cf`](https://github.com/vertical-cloud-lab/byu-vcl/tree/49677cf/ot2-overhead-camera/lid-mount) (2026-09-25 to 2026-10-30) | [`lid-mount/`](lid-mount/): the mount's design, CAD, exports, slicing, fasteners, stream set-up, and the focusing lessons |
| byu-vcl [PR 84](https://github.com/vertical-cloud-lab/byu-vcl/pull/84) (the camera choice and the first order) | The parts and prices, and the bring-up steps below |
| byu-vcl `main` at [`d378b16`](https://github.com/vertical-cloud-lab/byu-vcl/tree/d378b16/wireless-color-sensor/ot2) | [`ot2-link.md`](ot2-link.md) and [`pi-tools/ot2_link_recover.sh`](pi-tools/ot2_link_recover.sh) |
| The first Pi, copied off it on 2026-11-10 | [`pi-tools/`](pi-tools/README.md): `ot2ctl.py`, `ytframes/grab.py`, a udev rule; the NetworkManager profiles in [`ot2-link.md`](ot2-link.md) |

Left in byu-vcl, to keep this repo small or because they can't be redistributed: the MP4 and GIF
videos, the C–H test spacers (a 49 MB plate), the Onshape scripts and evidence, the slicer and
printer evidence, and the stills and frames from the first camera. McMaster-Carr's STEP models
and Opentrons' OT-2 model carry no redistribution licence; the CAD scripts fetch them at run time.

## Contents

| Path | What |
|---|---|
| [`lid-mount/README.md`](lid-mount/README.md) | The mount: parts, assembly, where on the lid, phase 1 (tape) and phase 2 (drill), design checks |
| [`lid-mount/shopping-list.md`](lid-mount/shopping-list.md) | Fasteners, with McMaster part numbers |
| [`lid-mount/exports/`](lid-mount/exports/) | STL and STEP for every printed part, the 1:1 drill template (PDF, DXF, SVG), the A and B C–CS spacer rings |
| [`lid-mount/slice/lid_mount_A1mini_PLA.3mf`](lid-mount/slice/) | Sliced for the Bambu Lab A1 mini, PLA |
| [`lid-mount/cad/`](lid-mount/cad/) | The CadQuery model and checks (`pip install -r requirements.txt`) |
| [`lid-mount/camera/README.md`](lid-mount/camera/README.md) | **Read before fitting the lens.** The lens stack, the rings, lining up over the plate |
| [`lid-mount/camera/stream/`](lid-mount/camera/stream/README.md) | `install.sh` and everything it installs: the YouTube stream, stills, watchdog, scheduled reboots |
| [`ot2-link.md`](ot2-link.md) | The robot's Ethernet link to the Pi |
| [`pi-tools/`](pi-tools/README.md) | `ot2ctl.py` (maintenance-run wrapper), link recovery, YouTube archive frames |

## Parts

From ME Order 12704 (approved 2026-05-08, $240.19 in all), plus what the first build learned.
Prices are from May to October 2026; recheck them before ordering.

| Item | Where | Qty | Last price |
|---|---|---|---|
| Raspberry Pi HQ Camera, **CS-mount** (SC1220). Comes with a C–CS adapter | [PiShop](https://www.pishop.us/product/raspberry-pi-hq-camera-cs/) | 1 | $55.00 |
| Raspberry Pi 5, 4 GB (SC1111) | [PiShop](https://www.pishop.us/product/raspberry-pi-5-4gb) | 1 | $110.00 |
| Raspberry Pi 27 W USB-C power supply (SC1153). Use this one: the first Pi logged under-voltage | [DigiKey](https://www.digikey.com/en/products/detail/raspberry-pi/SC1153/21658276) | 1 | $12.95 |
| microSD card, 32 GB | [PiShop](https://www.pishop.us/product/microsd-card-32-gb-class-10-blank/) | 1 | $14.95 |
| Waveshare 8–50 mm zoom lens for the HQ Camera (C-mount) | [Waveshare](https://www.waveshare.com/8-50mm-Zoom-Lens-for-Pi.htm) | 1 | $34.99 |
| Camera cable for Raspberry Pi 5, **200 mm** (the one in the camera box does not fit a Pi 5) | [PiShop](https://www.pishop.us/product/camera-cable-for-raspberry-pi-5/) | 1 | $1.35 |
| Raspberry Pi Active Cooler | [PiShop](https://www.pishop.us/product/raspberry-pi-active-cooler/) | 1 | $10.95 |
| 5 mm C-to-CS spacer ring, aluminium, pack of 2 | [Amazon B09STVLLVY](https://www.amazon.com/dp/B09STVLLVY) | 1 | $6.99 |
| Cat6 patch cable, robot to the Pi's own Ethernet port. **No USB-Ethernet adapter** | [Amazon B00C2CA3N8](https://www.amazon.com/dp/B00C2CA3N8) (5-pack) or [B0B57T23M3](https://www.amazon.com/dp/B0B57T23M3) | 1 | $19.99 / $8.99 |
| Fasteners (M3 × 10 + nuts; M4 × 18, nuts and nylon washers only if drilling) and the nylon M2.5 kit | [`lid-mount/shopping-list.md`](lid-mount/shopping-list.md) | | cents each |
| Printed base, deck, spacers, C–CS ring A/B: about 124 g of black PLA or PETG | lab printer | | |

## Bring-up, in order

**1. Print and assemble the mount** per [`lid-mount/README.md` §1–2](lid-mount/README.md#1-whats-in-the-box).
Fit the lens as in [`lid-mount/camera/README.md`](lid-mount/camera/README.md#the-lens-stack-fit-one-5-mm-ccs-spacer):
camera → knurled back-focus ring → **one 5 mm C–CS spacer** → lens. Without the spacer this lens
never focuses on the deck. Connect the camera with the **Pi 5 camera cable** (22-pin end on the
Pi, 15-pin on the camera; either CAM port), with the Pi off. Clip on the Active Cooler.

**2. Flash Raspberry Pi OS Lite (64-bit)** with [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
The first Pi ran Debian 13 (trixie) with no desktop. In the Imager's OS customisation, set a
new hostname, a user and password, SSH, the lab Wi-Fi, and Wi-Fi country US. Boot it on the
27 W supply, then `sudo apt update && sudo apt full-upgrade -y`.

**3. Join the lab tailnet**, so lab members and `@claude` runs can reach it:
`curl -fsSL https://tailscale.com/install.sh | sh`, then `sudo tailscale up --ssh` and log in with
the lab's tailnet account. An admin then tags the device as in `vertical-cloud-lab/tailscale-policy`
(the camera Pis use the stream-cam tag) and updates the repo secrets that name the Pi
(`RPI_STREAM_CAM_HOSTNAME` and `RPI_STREAM_CAM_PASSWORD` in byu-vcl, and their equivalent here if
this repo's runs should reach it). Never commit the hostname, the tailnet name or an address.

**4. Check the camera**: `sudo apt install -y python3-picamera2 rpicam-apps`, then
`rpicam-hello --list-cameras` should list `imx477`. If not, power off, reseat both ends of the
cable, and try again.

**5. Cable the robot** to the Pi's own Ethernet port and give it the link-local profile in
[`ot2-link.md`](ot2-link.md). Done when `curl -s -H 'Opentrons-Version: 3'
http://169.254.51.252:31950/health` answers.

**6. Set up the stream.** Copy [`lid-mount/camera/stream/`](lid-mount/camera/stream/) to the Pi and
run `bash install.sh` (it reads the sudo password from stdin, with no prompt). Then, in
`~/ac-training-lab/src/ac_training_lab/picam/my_secrets.py`, set:

- `LAMBDA_FUNCTION_URL`: copy it from another lab stream cam's `my_secrets.py` **over SSH, Pi to
  Pi**, so it never appears in a terminal log, comment or commit.
- `CAM_NAME` and `WORKFLOW_NAME`. The Lambda files each broadcast into the first playlist whose
  title contains `WORKFLOW_NAME` (case-insensitive substring), so don't pick a name another camera
  uses. `"OT2 overhead"` reuses the existing *OT2 overhead Livestreams Playlist*.
- `PRIVACY_STATUS`: `"public"`, `"unlisted"` or `"private"`. Decide before the first start.

Start it with `sudo systemctl start stream-watchdog.timer stream-reboot.timer device.service`.

**7. Put the mount on the lid** (phase 1, tape) over the plate's slot, and line it up and focus it
from the stream ([`lid-mount/camera/README.md`](lid-mount/camera/README.md#lining-it-up-over-the-plate-slide-zoom-focus-centre-and-square-lock)).
Then set `SETUP_OVERLAY = False` and restart `device.service` once.

**8. Record the final settings** in the rebuild issue: zoom, iris and focus positions, the knurled
ring's turns, which spacer, and a photo of the barrel. The first build never recorded these.

**9. Robot tools as needed**: [`pi-tools/ot2ctl.py`](pi-tools/README.md#ot2ctlpy) and the
colour-sensor venv. **CubOS is not needed**: it ran on the first Pi only for the CubXL gantry,
which has its own Pi. `pi-tools/ytframes/grab.py` needs a host with a residential IP, which a
campus Pi is and a GitHub runner is not.
