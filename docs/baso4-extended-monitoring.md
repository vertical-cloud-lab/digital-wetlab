# Barium sulfate plates: monitoring and documenting a run over days

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) by
@timothy-commins on 2026-11-02. The plan is to run more barium chloride and sodium sulfate plates,
like Sam and Sterling's first OT-2 plate in March. The goal is to show that the lab can monitor and
document an experiment over an extended period. This page gives the next steps.

Everything here comes from the written record in this repo and in
[byu-vcl](https://github.com/vertical-cloud-lab/byu-vcl). Nothing was checked in the lab.

## What Sam and Sterling did in March

**Start here:** [issue 1](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1) has the
run as it happened, and [PR 3](https://github.com/vertical-cloud-lab/digital-wetlab/pull/3) has the
plan and the questions asked along the way.

| what | where |
| --- | --- |
| The plan (experiment 002): 80 Latin hypercube conditions with barium 0.1–50 mM, sulfate 0.1–50 mM and NaCl 0–3 molal, plus 16 controls; 1.0 M stocks; images planned at 5, 15, 60 and 240 min | [`experiments/002-baso4-precipitation/README.md`](https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/002-baso4-precipitation/README.md) in PR 3 |
| The protocol that ran, with the P20. The file is named AgCl, but it's the barium sulfate plate | [`Experiment_1__AgCl_Precipitation_V1.py`](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cded249/Experiment_1__AgCl_Precipitation_V1.py) in [PR 8](https://github.com/vertical-cloud-lab/digital-wetlab/pull/8) |
| Stocks to make in the polishing lab | [issue 1, 03-05](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4001238369) |
| Dry run with water. It went well, but the camera stopped recording after about 1.5 h | [issue 1, 03-05](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4005965449) |
| Photos of the setup | [issue 1, 03-05](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4007991511) |
| Photos of the finished plate, about 5:30 pm on 03-05 | [issue 1, 03-06](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4008876464) |
| Videos: two of the stock prep and three of the plate | [issue 1, 03-06](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4014564410) |
| PHREEQC: every one of the 80 conditions was supersaturated (saturation index 2.6–5.8) | [PR 3, 03-06](https://github.com/vertical-cloud-lab/digital-wetlab/pull/3#issuecomment-4010148599) |

What the record shows about that plate:

- **It mapped how strongly barium sulfate precipitates, not where the boundary is.** Every
  designed well was supersaturated.
- **16 of the 80 conditions got no barium or no sulfate.** The protocol set any dose under 1 µL to
  zero ([lines 170–176](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cded249/Experiment_1__AgCl_Precipitation_V1.py#L170-L176)).
  With 1.0 M stocks, that dropped every dose under 5 mM. The wells are listed in the
  [10-30 check](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/baso4-checks/results.txt).
- **The Na₂SO₄ tip went back into its stock tube after touching wells that held barium.** So the
  March sulfate stock may hold barium sulfate seeds. Don't reuse the March tubes.
- **Nothing ties images to the time points.** I found no stills for 5, 15, 60 and 240 min and no
  per-well scores, only the photos and videos above. Filling that gap is what this project is for.

## The goal, and how long "extended" should be

The goal is a plate whose whole run is on record:

- what went into each well, and when;
- a still every few minutes for days, all taken with the same camera settings and light;
- the temperature and humidity around the plate;
- anything that happened during the run (a door opened, a reboot, a missed still);
- a result that someone who wasn't there can rebuild from the stored files.

**Why go past March's 4 hours.** The PRF reviewer's main objection on timing was that a precipitate
seen within four hours doesn't show solubility. When a well first turns cloudy depends on how long
you watch and how faint a precipitate you can see
([review digest](https://github.com/vertical-cloud-lab/digital-wetlab/blob/7f49607/grants/acs-prf/REVIEW_2026.md),
paraphrased, in [PR 82](https://github.com/vertical-cloud-lab/digital-wetlab/pull/82)). How fast
barium sulfate nucleates depends on supersaturation and on the NaCl
([He, Oddo and Tomson 1995](https://doi.org/10.1006/jcis.1995.1397)). Near the boundary, wells can
stay clear long after 4 hours. A record over days is also what
[direction 4 in PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/blob/2fb7592/grants/ot2-new-directions/README.md#4-nucleation-statistics-and-crystallisation-inhibitors-the-current-setup-re-aimed)
(distributions of nucleation times) would need.

**Suggested lengths:**
1. A dry run with water and dye, for 24–48 h.
2. The first barium sulfate plate, for 72 h.
3. A week, once the 72 h run works.

72 h covers nine of the Pi's scheduled reboot times, three day-night cycles in the building, and
roughly 18 times the length of March's planned record.

## What is already in place

| piece | state | source |
| --- | --- | --- |
| **Overhead (lid) camera** | Raspberry Pi HQ Camera with an 8–50 mm zoom, on the OT-2's top window over slot 7, run by a Pi 5. Michael reported it in clear focus on 10-30 (posted 11-01). | byu-vcl [PR 234](https://github.com/vertical-cloud-lab/byu-vcl/pull/234#issuecomment-6564024999) |
| Stills | Full resolution (4056 × 3040) in about 0.3 s, while the stream runs: `curl -s localhost:8081/still` on the Pi. Each still comes with its exposure, gain, colour gains and light level. Zoomed to the plate, a well is about 202 px across. | [stream README](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/stream/README.md#operating-it), [camera README](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/README.md#where-it-is-looking-now) |
| Live stream | 1920 × 1440 at 3 fps with a timestamp, public, in the [OT2 overhead playlist](https://www.youtube.com/playlist?list=PLM4VC4X_7XKQ). It is a continuous video record of the deck. | [stream README](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/stream/README.md) |
| **Light** | The OT-2's rail lights are the light source: the camera saw 6 lux from the room alone and 104 lux with the rail lights on. They're switched from the Pi, and in October a timer turned them off at 17:00. | [camera README](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/README.md#2026-10-22-2046-utc-live-far-out-of-focus) |
| Blackout | The OT-2's sides were blacked out on 09-30, with cardboard and wood over the rest from 10-01. **Check** that fitting the lid camera didn't open a gap. | byu-vcl [colour-sensor README](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/README.md) |
| **Pi reboots** | At 05:00, 13:00 and 21:00 local, so no broadcast runs past YouTube's 12 h archive limit. Each one takes the stream, the tailnet and the OT-2's link down for under a minute. A reboot waits while a protocol runs or a `systemd-inhibit` lock is held. After 3 h of waiting it restarts only the stream. | [stream README, Reboots](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/stream/README.md#reboots) |
| **Pi power** | `Undervoltage detected!` on 10-30, at 4.81 V while streaming. Raspberry Pi specifies its 27 W, 5.1 V USB-C supply for a Pi 5. | [stream README](https://github.com/vertical-cloud-lab/byu-vcl/blob/49677cf/ot2-overhead-camera/lid-mount/camera/stream/README.md#operating-it) |
| OT-2 link | Only through the same Pi, over USB-Ethernet. On 09-10 the adapter wedged and the robot was unreachable for 8 h. `ot2_link_recover.sh` checks the link and repairs it. | byu-vcl [colour-sensor README](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/README.md#run-it) |
| OT-2 | A P300 single GEN2 only; the P20 is on the CubXL. No tip-length or pipette-offset calibration. The deck calibration dates from 01-27, before the robot was moved. | [10-30 lead plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#ot-2-plates) |
| Chemicals | Barium chloride, anhydrous sodium sulfate and sodium chloride are on hand. The March recipe assumed barium chloride dihydrate, so check the label. Fresh DI water is free from Chem Stores. | byu-vcl [15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15), [10-30 lead plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#chemicals) |
| Database | MongoDB `digital-wetlab`. The colour sensor already writes its readings to `sensor-data` there. | byu-vcl [colour-sensor README](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/README.md) |

## Decisions before the first run

1. **How long each run lasts.** Suggested above: 24–48 h dry, 72 h with barium sulfate, then a week.
2. **Which plate.**
   - **A (suggested): the practice plate from 10-30.** Barium against sulfate at 0.01, 0.1, 1 and
     3 mM each, in 1 molal NaCl and without it, with blanks and controls (below). Unlike March, it
     crosses the boundary. So some wells change in minutes, some slowly and some never, which is
     what makes a record over days worth having.
   - **B: March's 80 conditions again,** with the dose and tip fixes. This compares directly with
     March. But every designed well is far above the boundary (saturation index 2.6–5.8), so most
     wells should precipitate early and change little over the following days.
   - **C: a few conditions near the boundary with 12 or more replicates each,** for the
     nucleation-time distributions in direction 4. This suits a later run.
3. **Seal.** Use a clear adhesive seal, put on right after the last addition. Over days an open
   well loses water, which concentrates both salts. A well that loses 10% of its water has its ion
   product raised 23% (saturation index +0.09). A late cloudiness could then come from evaporation
   rather than slow nucleation. Check in the dry run that the seal doesn't fog.
4. **Mixing after the sulfate.** Either dispense the sulfate from above the liquid with no mixing,
   or use a new tip per well and mix gently. Do the same in every well and write it down, since
   mixing changes nucleation.
5. **Where the stills go, and who checks the run.** Seventy-two hours at the schedule below is about
   400 full-size stills, too many for git. They could go to AWS (Seth had AWS ready for this camera
   in June, [byu-vcl 34](https://github.com/vertical-cloud-lab/byu-vcl/issues/34#issuecomment-4791750994)),
   Box or Drive.
   Someone should check the run once a day.

## Next steps

### 1. Camera and record-keeping, with no chemicals

1. **Fix the Pi 5's power.** Use the official 27 W supply before any multi-day run. Undervoltage can
   crash a Pi or corrupt its SD card.
2. **Fix the camera settings for the run.** `picam_source.py` sets only the frame rate, so exposure,
   gain and white balance are automatic. As wells turn white, auto exposure can darken the clear
   wells. Turn the rail lights on, let it settle, read the exposure, gain and colour gains from
   `localhost:8081/status`, then lock them for the run. This needs a small change in byu-vcl
   (picamera2's `AeEnable` and `AwbEnable` off, with `ExposureTime`, `AnalogueGain` and
   `ColourGains` set). At this zoom a colour card doesn't fit in the frame. Instead, photograph one
   in the plate's place before and after each run, with the same settings.
3. **Keep the rail lights on for the whole run,** with no off timer. Switching them per still
   depends on the OT-2's link, which has failed before. The capture job (next step) should check
   each still's light level and switch the lights back on if they've gone off.
4. **Write the capture job.** It runs on the Pi 5 as a systemd service. It:
   - takes a still from `localhost:8081/still`:
     - every minute from the first sulfate addition until 30 min after the last;
     - every 5 min until 6 h;
     - every 15 min after that;
   - names each still by run ID, UTC time and time since start, and saves the still's metadata
     next to it;
   - retries every 30 s when a still fails (the stream restarts at each reboot time), and logs the
     gap;
   - holds a `systemd-inhibit --what=shutdown` lock, so the Pi doesn't reboot mid-run. The stream
     still restarts after the 3 h wait, so broadcasts stay under 12 h;
   - copies stills off the Pi as it goes and writes one MongoDB record per still;
   - pings a dead-man's switch after each still, so someone hears when stills stop. The stream
     watchdog already supports a Healthchecks.io URL (`HEALTHCHECK_URL`). A daily post of the newest
     still to the run's GitHub issue would also keep the run visible, which Sterling liked in
     [issue 12](https://github.com/vertical-cloud-lab/digital-wetlab/issues/12);
   - leaves the robot alone.
5. **Log temperature and humidity** next to the plate every 5 min. Use a small sensor on the Pi or a
   standalone logger. The AirGradient is in the powder enclosure.
6. **Check the clocks.** The Pi keeps network time. The OT-2 is reachable only over its link to the
   Pi, so it probably has no time source of its own. The robot server reports and sets its time at
   `/system/time`. Compare it with the Pi's before each run, because each well's start time comes
   from the robot's log.
7. **Dry run for 24–48 h.** Use a sealed plate of water with a few wells of food dye, in slot 7,
   with everything above running. Weigh it at the start and the end. It passes if:
   - every planned still exists, or its gap is logged with a reason;
   - the water wells' brightness stays steady (pick a limit, such as ±2%);
   - the seal stays clear;
   - the plate loses little water by weight (pick a limit, such as 1%);
   - someone who wasn't there can tell what happened at any hour, from the stills index, the
     event log and the stream videos.

   This run already shows the monitoring and record-keeping, with no chemicals at all.

### 2. Robot, protocol and stocks

8. **Book the OT-2 for the whole run.** Nothing else can use the robot or touch the deck. Take the
   colour-sensor rig off the deck, after the
   [README's](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/README.md)
   "one controller at a time" check, and put a sign on the robot.
9. **Calibrate:** deck, tip length, pipette offset, then Labware Position Check. Then weigh a plate
   of water to check the volumes.
10. **Write the protocol** for plate A, starting from the March protocol:
    - the plate in slot 7, under the camera, on black paper;
    - sulfate last, as decided in decision 4;
    - no tip goes back into a stock after touching a well;
    - a dose the P300 can't make (under 20 µL) stops the protocol instead of becoming zero;
    - a pause for the seal, and the rail lights on at the end;
    - well positions shuffled, so replicates don't share an edge or a row.

    Run it through `opentrons_simulate` before it touches liquid. Afterwards, each well's start time
    comes from the run's command list on the robot (`/runs/<id>/commands`).
11. **Make fresh stocks** on the day, with fresh DI water
    ([why](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cb98aa9/docs/di-water-storage.md)).
    Log the lot, mass, volume, time and person for each. Wear gloves and goggles: barium chloride is
    toxic if swallowed. Add its SDS to the binder, since it was missing in October.

    | tube | recipe |
    | --- | --- |
    | 0.1 M barium chloride | 366.4 mg barium chloride dihydrate (BaCl₂·2H₂O), made up to 15 mL |
    | 0.1 M sodium sulfate | 213.1 mg anhydrous sodium sulfate (Na₂SO₄), made up to 15 mL |
    | 10, 1 and 0.1 mM of each | dilute tenfold three times: 1.5 mL made up to 15 mL, or by weight on the balance |
    | 5 M sodium chloride | 4.383 g NaCl, made up to 15 mL |
    | DI water | fresh |

    That's 10 tubes. The March rack holds 6, so use two racks or a larger one. Filtering the stocks
    through 0.2 µm removes dust that can seed nucleation. That's optional for this run, but needed
    for option C.

### 3. The run

12. **Start the capture job before the first dispense,** so the record covers the dispensing too.
    Seal the plate at the pause, weigh it, close the doors, and note the times in the event log.
    Start on a weekday morning, so people are around for the first hours.
13. **Check the run once a day.** Look at the stream and the heartbeat, and write anything that
    happened in the event log.
14. **At the end:** take a last still, weigh the plate, and photograph it on black with a phone,
    as in March. The wells, leftover stocks and rinses go in a barium waste container, which the
    [10-30 list](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#waste)
    still had to get.

### 4. Documentation and analysis

15. **Store the run:**
    - stills and their metadata in the chosen storage;
    - one record per still, and one per well, in MongoDB `digital-wetlab`;
    - the small files in this repo, under `experiments/004-baso4-monitoring/<run-id>/`: the run
      record (below), the plate map, the stock log, each well's start time, the stills index, the
      environment log, the event log, and the stream videos that cover the run.
16. **Analyse:**
    - the brightness of each well's centre in every still, minus the water wells', plotted against
      time since that well's sulfate went in;
    - when each well first rises above its blank's spread;
    - how much the blanks drift over the run;
    - the water lost, from the weights.
17. **Write it up briefly:** stills taken against planned, the gaps, the curves, a time-lapse, a
    grid of well crops at a few times, and what went wrong. Go over it with Sterling, then decide
    on the week-long run, option C, or moving to lead.

## Plate A

From the [10-30 practice plate](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#barium-sulfate-practice-plate),
200 µL per well:

- all 16 pairs of barium and sulfate at 0.01, 0.1, 1 and 3 mM each, in 1 molal NaCl, in triplicate:
  48 wells;
- the same 16 pairs once without NaCl: 16 wells;
- barium only and sulfate only at each level;
- water and NaCl blanks;
- 10 mM + 10 mM positive controls, from 20 µL of each 0.1 M stock.

20 µL of the 0.1, 1 or 10 mM stock gives 0.01, 0.1 or 1 mM, and 60 µL of the 10 mM stock gives
3 mM. All of these suit the P300, whose smallest volume is 20 µL.

PHREEQC (pitzer.dat, 25 °C) gives these saturation indices in 1 molal NaCl. Below 0 nothing can
precipitate ([script and output](https://github.com/vertical-cloud-lab/digital-wetlab/tree/127e1db/docs/baso4-checks)):

| barium (mM) \ sulfate (mM) | 0.01 | 0.1 | 1 | 3 |
| --- | --- | --- | --- | --- |
| 0.01 | −2.0 | −1.0 | 0.0 | +0.5 |
| 0.1 | −1.0 | 0.0 | +1.0 | +1.5 |
| 1 | 0.0 | +1.0 | +2.0 | +2.5 |
| 3 | +0.5 | +1.5 | +2.5 | +2.9 |

Without NaCl the same pairs are 1.4–1.8 units higher. The wells between 0 and about +1 are the ones
that may take hours or days, or never visibly precipitate; that is where the long record earns its
keep. At 0.1 mM a well can form only about 5 µg of barium sulfate, so they also test how faint a
precipitate the camera can pick up.

## What to record for each run

Copy this into `experiments/004-baso4-monitoring/<run-id>/run.yaml` and fill it in as you go.

```yaml
run_id: baso4-YYYYMMDD-01
purpose: dry run, or plate A
people: []                       # GitHub logins
protocol: {file: , commit: }
robot:
  pipette: P300 single GEN2, left mount
  calibrated: {deck: , tip_length: , pipette_offset: , labware_position_check: }
  clock_minus_pi_s:              # robot clock minus Pi clock, before the run
plate:
  type: NEST 96 flat, 200 uL
  slot: 7
  background: black paper
  seal: {product: , applied_utc: }
  mass_g: {start: , end: }
stocks:                          # one entry per tube
  - {name: , conc: , mass_mg: , made_up_to_mL: 15, lot: , made_utc: , by: }
files:
  plate_map: plate_map.csv       # well, Ba mM, SO4 mM, NaCl molal, replicate, role
  well_times: well_times.csv     # well, sulfate dispensed (UTC), from the robot's run commands
  stills: stills.csv             # planned UTC, actual UTC, file, exposure, gain, lux, ok
  environment: env.csv           # UTC, deg C, %RH
  events: events.md              # UTC, what happened, who
camera:
  zoom_mm:
  focus_score:
  locked: {exposure_us: , analogue_gain: , colour_gains: }
  colour_card_stills: [before, after]
lights: {on_utc: , off_utc: }
stream_videos: []                # YouTube IDs that cover the run
waste: {container: , volume_mL: }
notes:
```

## Not done here

- I didn't write the capture job, the protocol or the analysis script. Any of them can be the
  next session.
- I didn't check the lab, the Pi or the robot. The camera's state comes from byu-vcl PR 234 up to
  11-01, and the robot's from the 10-30 lead plan.
- I read only the title and listing of He, Oddo and Tomson (1995), not the paper.
