# Pi tools for the OT-2 link Pi

Helpers that ran on the first OT-2 camera Pi. `ot2ctl.py`, `ytframes/grab.py` and the udev rule
existed only on that Pi, and were copied off it on 2026-11-10 before it left. They are unchanged,
except that the udev rule gained a comment header. `ot2_link_recover.sh` comes from byu-vcl `main`
at [`d378b16`](https://github.com/vertical-cloud-lab/byu-vcl/blob/d378b16/wireless-color-sensor/ot2/ot2_link_recover.sh).

None of them holds a credential. The robot address `169.254.51.252:31950` is the OT-2's
link-local address on its private cable ([`../ot2-link.md`](../ot2-link.md)); check yours with
byu-vcl's [`find_ot2.sh`](https://github.com/vertical-cloud-lab/byu-vcl/blob/d378b16/wireless-color-sensor/ot2/find_ot2.sh)
if a different robot is used.

| File | Goes to | What |
|---|---|---|
| [`ot2ctl.py`](ot2ctl.py) | `~/ot2ctl.py` | A thin wrapper over the OT-2 HTTP API's **maintenance runs**, which move the gantry directly with no protocol. Keeps its run ID and pipette ID in `~/ot2_ymin2/state.json` (`mkdir -p ~/ot2_ymin2` first). **Moves real hardware.** |
| [`ot2_link_recover.sh`](ot2_link_recover.sh) | anywhere on the Pi | Checks the robot link by pinging the robot, and repairs a wedged RTL8153 USB-Ethernet adapter in three stages. Only matters if the robot is cabled through such an adapter |
| [`40-ot2-usb-ethernet-cdrom-fix.rules`](40-ot2-usb-ethernet-cdrom-fix.rules) | `/etc/udev/rules.d/` | Flips an RTL8153 that enumerates as a fake CD drive (`0bda:8151`) into network mode. Same caveat |
| [`ytframes/grab.py`](ytframes/grab.py) | `~/ytframes/grab.py` | Pulls single frames out of a YouTube livestream archive by video offset |

## `ot2ctl.py`

Run it on the Pi that holds the robot's cable; nothing else can reach the robot. Every request
sends `Opentrons-Version: 3`. Coordinates are deck coordinates in mm, for a `p300_single_gen2` on
the left mount (edit `init` for another pipette).

```bash
mkdir -p ~/ot2_ymin2
python3 ~/ot2ctl.py init                     # new maintenance run, load the pipette, home
python3 ~/ot2ctl.py move X Y Z [MIN_Z] [direct]   # moveToCoordinates; MIN_Z "-" for none
python3 ~/ot2ctl.py savepos                  # print where the pipette is
python3 ~/ot2ctl.py home
python3 ~/ot2ctl.py droptip                  # dropTipInPlace
python3 ~/ot2ctl.py delete                   # end the maintenance run: always do this last
```

`GET /health` is read-only and safe; anything under `/maintenance_runs` moves the robot. While a
maintenance run exists, the camera Pi's `stream-reboot.sh` holds off its scheduled reboot, so
don't leave one open.

## `ytframes/grab.py`

Reads `[{"video_id": "...", "offset": 22228, "name": "frame.jpg"}, ...]` on stdin and writes the
frames to `~/ytframes/out/`. It needs:

- **A residential IP.** YouTube refuses player extraction from datacenter addresses ("Sign in to
  confirm you're not a bot") on every GitHub Actions runner. Listing a channel or playlist works
  from anywhere; fetching the video does not. The first Pi on campus Wi-Fi worked.
- `yt-dlp` in `~/.venvs/ytframes` (`python3 -m venv ~/.venvs/ytframes && ~/.venvs/ytframes/bin/pip install yt-dlp`)
  and Node for its JS runtime (`--js-runtimes node`).
- A static `ffmpeg` and `ffprobe` in `~/ytframes/bin`. A static build cannot resolve DNS, which is
  why the script fetches segments itself and only ever hands ffmpeg a local file.

The archive timeline is video offset, not wall clock: offset 0 is the broadcast's
`release_timestamp`, and the timestamp burned into the top left of every frame is the clock to
trust.

## Not salvaged

- `~/.venvs/xscan` (the colour-sensor X-scan venv). The recipe is in byu-vcl's
  [`wireless-color-sensor/ot2/README.md`](https://github.com/vertical-cloud-lab/byu-vcl/blob/d378b16/wireless-color-sensor/ot2/README.md):
  `python3 -m venv ~/.venvs/xscan && ~/.venvs/xscan/bin/pip install paho-mqtt pymongo requests`.
- `~/.venvs/mpremote`, used to flash the Pico W colour sensor over USB.
- `~/CubOS` and `cubos.service`. **Not needed for the rebuild**: by 2026-10-19 the CubXL gantry it
  served had moved to its own Pi, and the service ran with nothing attached.
- The stream's live `my_secrets.py`. Start from `../lid-mount/camera/stream/my_secrets_example.py`
  and copy the streaming Lambda URL from another lab stream cam over SSH, so it never passes
  through a terminal log or a commit.
