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

- **Fire-and-forget trials**: start experiments, submit partial results to Ax as readings come in.
- Use `ax_client.complete_trial()` with intermediate metrics at each time point rather than waiting for the full 240-minute result.
- Pre-generate a batch of Ax trials (e.g., `max_parallelism=10` in the SOBOL phase) so the robot always has work queued while Ax fits in the background.

## Strategy 5: Mix-Then-Heat Workflow

Address the mixing question directly: mix solutions on the well plate at room temperature, then transfer the plate to the heater.

- Pipette all reagents into the plate first (fast, robot-controlled).
- Place the plate on the heater—all wells start heating simultaneously.
- This avoids per-well timing drift and simplifies the absorbance schedule since all wells in a batch share the same t=0.

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

def add_sample(sample_id, start_time):
    for offset in [60, 300, 900, 3600, 14400]:  # 1, 5, 15, 60, 240 min in seconds
        heapq.heappush(schedule, (start_time + offset, sample_id, "read_absorbance"))

while schedule:
    next_time, sample_id, action = heapq.heappop(schedule)
    wait = next_time - time.time()
    if wait > 0:
        # Use idle time: start new samples, change temperature, or run Ax
        handle_idle(wait)
    execute(action, sample_id)
```

This keeps complexity manageable while maximizing utilization of both the heater and the robot.
