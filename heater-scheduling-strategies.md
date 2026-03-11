# Heater Scheduling Strategies

Strategies for managing the single-temperature heater constraint during parallel experimentation with timed absorbance measurements.

## Core Problem

The heater holds one temperature at a time. Samples may need different temperatures, and absorbance readings are required at 1, 5, 15, 60, and 240 minutes. With a 19-dimensional Ax search space, parameterization time adds further scheduling pressure.

## Strategy 1: Temperature-Batched Scheduling

Group experiments by temperature, then run all same-temperature samples together.

- **Pre-sort** Ax-suggested trials into temperature bins before execution.
- Run all samples in a bin while the heater is at that temperature.
- Stagger start times within a batch so absorbance windows don't all overlap.
- **Trade-off**: Delays feedback to Ax (batch rather than sequential updates), but maximizes throughput.

## Strategy 2: Interleaved Time-Window Pipeline

Exploit the gaps between absorbance reads (especially the 60→240 min gap) to run other work.

```
Sample A: start → read@1m → read@5m → read@15m → [idle 45 min] → read@60m → [idle 3h] → read@240m
                                                     ↑ run Sample B here
```

- Use a **priority queue** ordered by next-required-action time.
- Between reads, change temperature and start/service other samples.
- Each sample tracks its own `start_time` and list of pending read times.

## Strategy 3: Constrain Ax Search Space on Temperature

Reduce scheduling complexity by limiting temperature variation.

- Fix temperature or discretize to a small set (e.g., 25 °C, 50 °C, 75 °C).
- Use temperature as a **batch-level** parameter rather than per-trial, running all trials at one temperature before moving to the next.
- Ax supports categorical/ordered-choice parameters—encode temperature as one to enable batch-aware optimization.

## Strategy 4: Asynchronous Ax Updates

Decouple Ax fitting from experiment execution to avoid blocking.

- **Fire-and-forget trials**: start experiments, and as readings come in, log intermediate data to Ax for running trials (e.g., via `ax_client.log_trial_data(...)` or updating trial data without completing it).
- Call `ax_client.complete_trial()` only once per trial when the final (e.g., 240-minute) measurements are available, optionally submitting all timepoint metrics together at that point, or model each timepoint as a separate metric and report them on completion.
- Pre-generate a batch of Ax trials (e.g., `max_parallelism=10` in the SOBOL phase) so the robot always has work queued while Ax fits in the background.

## Strategy 5: Mix-Then-Heat Workflow

Address the mixing question directly: mix solutions on the well plate at room temperature, then transfer the plate to the heater.

- Pipette all reagents into the plate first (fast, robot-controlled).
- Place the plate on the heater—all wells start heating simultaneously.
- This avoids per-well timing drift and simplifies the absorbance schedule since all wells in a batch share the same t=0.

## Consideration: When to Apply Heat

The timing of heating relative to mixing matters and depends on what is being measured:

- **Early heating (mix on the heater)**: The reaction starts at the target temperature from t=0. This is important when the goal is to measure temperature-dependent kinetics (e.g., nucleation rate, initial precipitation speed) since those early moments are the most temperature-sensitive. However, it requires the plate to already be at temperature before pipetting, which means one-at-a-time well filling and per-well timing drift.

- **Late heating (mix at room temp, then heat)**: The reaction begins at ambient temperature during mixing and ramp-up. Early kinetics (1 and 5 min reads) reflect room-temperature behavior, not the target temperature. This is acceptable when temperature primarily affects equilibrium (e.g., final solubility, precipitate morphology at steady state) rather than initial rates. It also simplifies scheduling since all wells in a batch share the same t=0.

- **Practical middle ground**: Pre-heat the plate to the target temperature *before* pipetting, then pipette directly onto the hot plate. The thermal mass of a 200 µL well is small enough that it equilibrates within seconds. This captures temperature-dependent early kinetics while still allowing batch starts. The trade-off is that reagent stocks are at room temperature, so there is a brief thermal transient on contact.

Which approach to choose depends on whether the 1-minute and 5-minute absorbance reads are meant to capture temperature-dependent kinetics or simply early-stage precipitation at whatever conditions. If temperature effects on early kinetics are a key variable in the 19-dim search space, pre-heating the plate before pipetting is the recommended path.

## Recommended Approach

Combine **Strategy 1 + 2 + 4**:

1. **Batch by temperature** to minimize heater transitions.
2. **Interleave samples within a batch** using a time-window scheduler to keep the robot busy during idle gaps.
3. **Run Ax asynchronously** with pre-generated trial batches so parameterization latency doesn't block execution.

A simple event-loop scheduler would look like:

```python
import heapq, time

# Each entry: (next_action_time, sample_id, action)
schedule = []

# `start_time` should be obtained from `time.monotonic()` so it
# uses the same clock domain as the scheduler loop below.
def add_sample(sample_id, start_time):
    for offset in [60, 300, 900, 3600, 14400]:  # 1, 5, 15, 60, 240 min in seconds
        heapq.heappush(schedule, (start_time + offset, sample_id, "read_absorbance"))

while schedule:
    next_time, sample_id, action = heapq.heappop(schedule)
    wait = next_time - time.monotonic()
    if wait > 0:
        # Use idle time: start new samples, change temperature, or run Ax
        handle_idle(wait)
    execute(action, sample_id)
```

This keeps complexity manageable while maximizing utilization of both the heater and the robot.
