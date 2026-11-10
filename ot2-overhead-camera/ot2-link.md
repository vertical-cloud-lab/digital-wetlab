# The OT-2's network link

The camera Pi is also the OT-2's only network link. The robot sits on a private Ethernet cable to
the Pi and answers only on its link-local address, `http://169.254.51.252:31950`, so every OT-2 API
call (protocol uploads, `ot2ctl.py`, the colour-sensor runs, the camera Pi's reboot check) runs **on
that Pi**. The Pi reaches the internet (MQTT, MongoDB, YouTube) and the lab's tailnet over Wi-Fi.

Collected from byu-vcl `main` at `d378b16`
([`wireless-color-sensor/ot2/README.md`](https://github.com/vertical-cloud-lab/byu-vcl/blob/d378b16/wireless-color-sensor/ot2/README.md),
[`opentrons-calibration.md`](https://github.com/vertical-cloud-lab/byu-vcl/blob/d378b16/wireless-color-sensor/ot2/opentrons-calibration.md),
[`ot2_link_recover.sh`](pi-tools/ot2_link_recover.sh)) and from the NetworkManager profiles and
boot command line copied off the first Pi on 2026-11-10.

## The robot's side

- **One RJ45 jack on the back, and nothing else for a host.** This OT-2 has no USB-B port. The four
  USB-A ports inside the enclosure are for Opentrons modules. Opentrons' first-run guide: "Connect
  the Ethernet cable to the OT-2 and your computer. If your computer does not have an Ethernet
  port, use the provided Ethernet-to-USB dongle." That dongle is for the computer's end.
- **Link-local only.** With no DHCP server on the cable, the robot gives itself a `169.254/16`
  address, so the host on the other end must too. A host profile left on DHCP never gets an address
  and never sees the robot.
- One jack means one host, unless there is a switch (below).

## Recommended: the robot's cable straight into the Pi's own Ethernet port

The Pi 5's built-in `eth0` is unused (the Pi is on Wi-Fi), so it can take the robot's cable
directly, with **no USB-Ethernet adapter**. The first Pi had a link-local profile for exactly this,
`ot2-eth0`:

```bash
sudo nmcli connection add type ethernet con-name ot2-eth0 ifname eth0 \
  ipv4.method link-local ipv6.method ignore \
  connection.autoconnect yes connection.autoconnect-priority 10
```

The priority of 10 makes it win over Raspberry Pi OS's stock `netplan-eth0` (DHCP, priority 0).
To put `eth0` back on a real network later: `sudo nmcli connection delete ot2-eth0`.

Check it, by pinging the robot rather than by the interface's state:

```bash
ip -4 -br addr show eth0                        # 169.254.x.y/16
ping -c 3 169.254.51.252
curl -s -H 'Opentrons-Version: 3' http://169.254.51.252:31950/health    # read-only; robot_serial, name
```

`GET /health` is safe. Anything under `/maintenance_runs` or `/runs` moves the robot
([`pi-tools/ot2ctl.py`](pi-tools/ot2ctl.py)).

Parts: one Cat6 patch cable, e.g. Cable Matters 10 ft snagless, 24 AWG copper
([5-pack B00C2CA3N8](https://www.amazon.com/dp/B00C2CA3N8) or [single B0B57T23M3](https://www.amazon.com/dp/B0B57T23M3)).
Skip anything listed as CCA, and Cat 7/8, which buy nothing on a gigabit link.

## Optional: a switch, so a laptop and the Pi can both reach the robot

Calibrating in the Opentrons OT-2 App needs a computer on the robot's cable, which otherwise means
unplugging the Pi. A small **unmanaged** gigabit switch between them lets both hold the robot at
once: link-local addressing works normally across a switch. Suggested in byu-vcl on 2026-09-25,
not yet tested there: TP-Link [TL-SG105](https://www.amazon.com/dp/B00A128S24) (avoid the
managed `TL-SG105E`) or Netgear [GS305](https://www.amazon.com/dp/B07S98YLHM), plus two more
patch cables. On the laptop, the wired adapter needs `ipv4.method link-local` too, and on Windows
the lowest interface metric, or Tailscale's own `169.254` addresses steal the traffic.

## If an RTL8153 USB-Ethernet adapter is used anyway

The first Pi used a Realtek RTL8153 dongle (`0bda:8153`) as `eth1` from 2026-08 to 2026-09, and it
failed repeatedly. Avoid it if `eth0` is free. If one has to be used:

- **Use a black USB 2.0 port, not a blue USB 3 one.** On USB 3 the adapter wedged with
  `r8152 … eth1: Stop submitting intr, status -71`, and the time between wedges fell from minutes to
  18 s; once it failed to probe at all after a cold boot. On a USB 2.0 port (480 Mbit/s, about 48
  times what this link carries) it answered thousands of pings in a row.
- **Judge the link by a ping to the robot, never by `carrier`.** After the fault, `eth1` kept
  `carrier=1`, `operstate=up` and its address for eight hours while carrying nothing; `ethtool`
  read garbage. Don't `ip link set eth1 down/up`: that issues a USB reset the wedged adapter cannot
  complete, and `eth1` disappears.
- [`pi-tools/ot2_link_recover.sh`](pi-tools/ot2_link_recover.sh) checks (`--check`, no root) and
  repairs (`sudo`, three stages: the `NO_LPM` quirk, a USB re-configure, and a port power cycle with
  `uhubctl`, from `sudo apt-get install -y uhubctl`). A 15 s power-off worked where 6 s did not.
- The `NO_LPM` quirk it sets is runtime only. **On the first Pi it was never made permanent**: the
  boot command line copied off it on 2026-11-10 had no `usbcore.quirks` entry. To make it permanent,
  append `usbcore.quirks=0bda:8153:k` to the single line in `/boot/firmware/cmdline.txt` (a typo
  there stops the Pi booting). It reduced the faults but did not prevent them.
- Some of these adapters boot as a fake driver CD (`0bda:8151`) and never become `eth1`.
  [`pi-tools/40-ot2-usb-ethernet-cdrom-fix.rules`](pi-tools/40-ot2-usb-ethernet-cdrom-fix.rules)
  flips them with `usb_modeswitch`.
- Its profile on the first Pi was `ot2-usb`, the twin of `ot2-eth0` on `eth1`:

  ```bash
  sudo nmcli connection add type ethernet con-name ot2-usb ifname eth1 \
    ipv4.method link-local ipv6.method ignore connection.autoconnect yes
  ```

## What the first Pi had, as copied off it on 2026-11-10

| | `ot2-eth0` | `ot2-usb` |
|---|---|---|
| `connection.interface-name` | `eth0` | `eth1` |
| `connection.autoconnect` | yes | yes |
| `ipv4.method` | `link-local` | `link-local` |
| `ipv6.method` | `ignore` | `ignore` |
| `802-3-ethernet.mac-address` | not pinned | not pinned |

Boot command line, apart from the root device: `console=serial0,115200 console=tty1 rootfstype=ext4
fsck.repair=yes rootwait cfg80211.ieee80211_regdom=US`. The last entry sets the Wi-Fi regulatory
domain to the US. No `usbcore.quirks`.

## Reboots and the link

The camera Pi reboots at 05:00, 13:00 and 21:00 local time
([`lid-mount/camera/stream/README.md`](lid-mount/camera/stream/README.md#reboots)), which takes
the robot link down for about 30 s. `stream-reboot.sh` waits while the robot has a maintenance run
or a protocol running, and while anything holds a `systemd-inhibit --what=shutdown` lock, so long
jobs on the robot are safe. Release maintenance runs when done (`ot2ctl.py delete`).
