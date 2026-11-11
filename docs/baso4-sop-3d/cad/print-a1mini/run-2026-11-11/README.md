# Print run, 2026-11-11: sent to the wrong A1 mini, stopped before layer 1

@timothy-commins asked for one vial holder on "the A1 mini" with the print trigger on
[PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84) (19:16 UTC) and approved the run himself. The run
logged in to the lab's Bambu account in Bambu Studio on the runner and sent the PETG file to **"Thumbelina, the A1
Mini"** at 21:04:38 UTC. At 21:09 he wrote that the A1 mini was unplugged, but Thumbelina was on and printing, so the
plate he had checked wasn't Thumbelina's. **The run stopped the print at 21:11:01 UTC, still at layer 0**, during Bambu's
start routine. Nothing was printed. He then asked for the H2D, but the H2D had a 0.6 mm nozzle in, which this repo
doesn't allow, so nothing was sent there either.

**Three printers are on the account:** "Thumbelina, the A1 Mini", **"Tinkerbell"** (a second A1 mini) and "BYU VCL
H2D - Théoden". A request has to name the printer by its Studio name, and the person giving the go has to be looking at
that printer.

## Timeline (UTC)

| Time | What |
| --- | --- |
| 19:16:24 | Request; approved by the requester |
| 19:20 | Studio 02.08.02.61 up on the runner (byu-vcl `bambu/studio/setup_runner.sh`, pinned) |
| 19:35:56–19:36:14 | Login: password, then Bambu asked for the authenticator code and the first `bambu-totp` code worked. Nobody posted anything |
| 19:36:40 | Device page: Thumbelina idle. Last job "Bottom (1)" finished. Heaters 21 °C |
| 19:37–21:01 | **Thumbelina's camera never loaded.** Every try ended "Loading failed. Please check the network and try again. [2:2]", including after installing `gstreamer1.0-x` and restarting Studio. Outbound UDP worked (STUN). The H2D's and Tinkerbell's cameras played in the same session, so the failure is Thumbelina's camera path, not the runner |
| 19:39:54 | Thumbelina's nozzle: **0.4 mm** stainless, standard flow ([`nozzle_printer_parts_1939Z.png`](nozzle_printer_parts_1939Z.png)) |
| 19:45 | HMS page empty ([`hms_empty_1945Z.png`](hms_empty_1945Z.png)); AMS Lite: A1 dark blue PLA, A2 empty, A3 black PLA, A4 PETG |
| 19:46:03 | No frame, so the run asked a person to check the plate (the plate rule's "can't tell" case) |
| 19:47–19:50 | The committed PETG file opened in Studio with the stock process (wall loops 2, no elephant-foot compensation, auto brim); the three changes set back and sliced in Studio |
| 19:50 | **The committed command-line G-code had a generic start sequence**: `G28`, `M970` lines, `G29`, and two prime lines at X 10 from Y 20 to **Y 200**, off the A1 mini's 180 mm bed, at 205 °C. Studio's slice had Bambu's A1 mini start and end G-code, with the same 115 layers (113 within 0.05 mm of filament, all within 0.8 mm). Studio's slice is what was sent |
| 21:02:52 | "plate clear" (timothy-commins) |
| 21:03:21 | Device page again: Thumbelina idle, no HMS ([`device_page_pre_send_2103Z.png`](device_page_pre_send_2103Z.png)) |
| 21:04:38 | **Send**: job `vial_holder_20ml_x6_A1mini_PETG_0.4.gcode`, PETG from A4, Textured PEI, timelapse off, levelling and flow calibration on ([`send_dialog_2104Z.png`](send_dialog_2104Z.png)) |
| 21:04:48 | Downloading; heating by 21:05:48 (nozzle 203/245 °C, bed 37/70 °C) |
| 21:09:58 | "print from the h2d, the a1 mini is currently unplugged" (timothy-commins) |
| 21:10:31 | Thumbelina still on and printing: 4 %, layer 0/115, nozzle 152/245 °C, bed 68/70 °C ([`device_page_printing_2110Z.png`](device_page_printing_2110Z.png)) |
| 21:10:51–21:11:01 | **Stop**, confirmed. Job cleared, heater targets 0 ([`device_page_after_stop_2111Z.png`](device_page_after_stop_2111Z.png)) |
| 21:12:49 | H2D: idle, last job finished, heaters at room temperature. HMS: a maintenance reminder only (clean and lubricate the rails). Plate: textured, no parts, faint light rectangle outlines in the middle ([`h2d_camera_2112Z.png`](h2d_camera_2112Z.png)) |
| 21:13 | H2D nozzles: **left 0.4 mm** hardened steel, standard; **right 0.6 mm** hardened steel, TPU high flow ([`h2d_nozzles_2113Z.png`](h2d_nozzles_2113Z.png)). Studio's *Switch diameter* prompt named the sides |
| 21:14 | Tinkerbell: printing someone's 3DBenchy; nozzle 0.4 mm stainless, standard ([`tinkerbell_nozzle_2114Z.png`](tinkerbell_nozzle_2114Z.png)). Not touched |
| 21:25:00 | "h2d" (timothy-commins). Asked for the right nozzle to be swapped to 0.4 mm |
| 21:25:12, 21:37:37, 21:52:12 | H2D nozzles re-read: still 0.4 and 0.6 mm ([`h2d_nozzles_2125Z.png`](h2d_nozzles_2125Z.png)) |
| 22:10:00 | H2D nozzles: still 0.4 and 0.6 mm. No reply by the stated 22:15 cutoff, so nothing was sent to the H2D |
| 22:15:34 | Thumbelina: idle, nozzle and bed at 23 °C, no HMS alert, filament loaded in the toolhead ([`device_page_final_2215Z.png`](device_page_final_2215Z.png)) |
| 22:16:06 | Signed out of the Bambu account; Studio closed, its config (with the printers' access codes) deleted, and the raw screen recording deleted |

## Files

- [`vial_holder_20ml_x6_A1mini_PETG_0.4_sent.gcode.3mf`](vial_holder_20ml_x6_A1mini_PETG_0.4_sent.gcode.3mf): Studio's
  slice as exported before Send (plate G-code MD5 `cc7090fe188e2142aacce4834935776e`), with the account's
  `DesignerUserId` blanked. Nothing changed in the project between the export and Send.
- [`send_to_stop_2102-2112Z_4x.mp4`](send_to_stop_2102-2112Z_4x.mp4): the screen recording from 21:02:30 to 21:12:05 UTC at
  4× (pre-send check, Send, the start routine, Stop), cut from the recorder's segments by wall-clock time. The login
  and the other printers' camera views are outside it.
- The screenshots linked above. None shows the login, a serial number or a person.

## What to change next time

- **Name the printer by its Studio name** in the request ("Thumbelina", "Tinkerbell" or the H2D), and have the person
  giving the go stand at that printer.
- **The `.gcode.3mf` files in `../` are re-sliced** with `slice_a1mini.py` fixed to load the profiles' `include`
  templates (Bambu's start and end G-code). Their start, end and filament-change G-code now match Studio's slice.
- **Thumbelina's camera** didn't load from the runner, while the H2D's and Tinkerbell's did. Check its liveview
  settings on the printer (for example LAN-only liveview) before relying on it in a print run.
