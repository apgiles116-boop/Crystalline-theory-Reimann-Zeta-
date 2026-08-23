# Targeted refinement of the grid-250 unresolved cell — VERIFIED

Date: 2026-08-23

This result concerns only the exact grid-250 terminal cell recorded in `GRID250_RESULT.md`:

```text
((494,494),(263,263),(499,499),(499,499),(263,263),(494,494))
```

It does **not** by itself prove the global six-gap inequality, because the original grid-250 run stopped at its first unresolved terminal cell.

## Exact coverage

At grid 500, every parent coordinate cell `[i/250,(i+1)/250]` is tiled exactly by the two closed cells with indices `2i` and `2i+1`. Thus the six-dimensional parent box is tiled by exactly

```text
2^6 = 64
```

children.

The targeted runner now checks this tiling algebraically in integer grid coordinates before invoking the verifier and fails closed if the count or either endpoint does not agree.

At grid 1000, each parent coordinate is tiled by four children, giving

```text
4^6 = 4096
```

finer boxes covering the identical parent region.

## First rigorous grid-500 run

GitHub Actions run: `32660182889`
Job: `97245058938`
Upstream verifier commit: `1610b97b7895ff34982260f8dcaf04a0f7b82cf7`
Python: `3.13.15`
`python-flint==0.9.0`
Exact target: `299/50000 = 0.00598`

Output:

```text
targeted_grid 500
targeted_ratio 2
targeted_boxes 64
target 299/50000
use_tangent True
verified=True
target=F >= 299/50000
grid=500
nodes=64
pruned=64
splits=0
maximum_depth=0
initial_boxes=64
interval_pruned=0
pressure_pruned=0
tangent_pruned=64
w_second_table_sha256=95aba8d334eadcb03d8294a2d21c53b5570fa5545c82b016625935f604ed2640
w_table_sha256=d504bb8c894f0a6e8f42da80a77b1526f11c35df750cabdff8d34e8cdf6a1cff
targeted_verified True
```

Every child closed rigorously with the Arb-validated convex-tangent/Hessian pruner.

## Recheck with exact tiling assertions and grid-1000 cross-check

GitHub Actions run: `32660323674`
Job: `97245419018`
PR merge-ref commit used by CI: `7662a428bcb72118ea44a01a29633800573e494c`
Head commit: `291c8d167f041fcc50af009dc364d48a21ef64f4`
Upstream verifier commit: `1610b97b7895ff34982260f8dcaf04a0f7b82cf7`
Python: `3.13.15`
`python-flint==0.9.0`

### Grid 500 repeat

```text
targeted_grid 500
targeted_ratio 2
targeted_boxes 64
target 299/50000
verified=True
nodes=64
pruned=64
splits=0
initial_boxes=64
interval_pruned=0
pressure_pruned=0
tangent_pruned=64
w_second_table_sha256=95aba8d334eadcb03d8294a2d21c53b5570fa5545c82b016625935f604ed2640
w_table_sha256=d504bb8c894f0a6e8f42da80a77b1526f11c35df750cabdff8d34e8cdf6a1cff
targeted_verified True
```

This exactly reproduced the first grid-500 certificate, including both table hashes.

### Grid 1000 cross-check

```text
targeted_grid 1000
targeted_ratio 4
targeted_boxes 4096
target 299/50000
use_tangent True
verified=True
target=F >= 299/50000
grid=1000
nodes=4096
pruned=4096
splits=0
maximum_depth=0
initial_boxes=4096
interval_pruned=256
pressure_pruned=0
tangent_pruned=3840
w_second_table_sha256=59b9d6a7166f1e1efa18bccab33f6857796a7078d93b7a2e1aea8207dfaaa185
w_table_sha256=51c566e8cb23b53e8be9c259d41b01f0d96316ebf8e1262a56f74f196992baed
targeted_verified True
```

All 4096 finer children closed rigorously. In contrast to grid 500, 256 were already closed by the direct interval bound; the remaining 3840 were closed by the validated tangent/Hessian bound.

## Interpretation

The originally unresolved grid-250 parent cell is now rigorously certified at both grid 500 and grid 1000. The repeated grid-500 result is bit-for-bit consistent at the level of the lower-bound table hashes, and the finer grid-1000 tiling independently closes the same region.

Therefore the recorded grid-250 failure in this parent region is attributable to insufficient local enclosure sharpness at grid 250, not to a violation of `F >= 299/50000` inside this box.

The remaining task is global: determine whether any other grid-250 terminal cells require refinement, or run the global certificate at grid 500 or finer resolution.
