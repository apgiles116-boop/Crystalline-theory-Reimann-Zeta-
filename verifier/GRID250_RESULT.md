# Grid-250 interval result — fail-closed unresolved cell

Date: 2026-08-23

The first single-worker global six-gap interval attempt at grid 250 did **not** certify the target. This was a legitimate fail-closed verifier result, not a mathematical counterexample.

CI context:

- workflow run: `32622361840`
- coarse interval job: `97152392234`
- PR merge commit used by the run: `171f4f586e08035f6c47e049838c149e4ae5d6d0`
- upstream commit: `1610b97b7895ff34982260f8dcaf04a0f7b82cf7`
- Python: `3.13.15`
- `python-flint==0.9.0`
- command: `python crystal_verify.py main --grid 250 --workers 1`
- uploaded artifact id: `9488808117`

## Exact fail-closed message

```text
RuntimeError: certificate failed at a terminal cell:
box=((494, 494), (263, 263), (499, 499), (499, 499), (263, 263), (494, 494)),
lower=0.005841208384501174
```

At grid 250, `closed_cell(i,250)` is the interval `[i/250,(i+1)/250]`. Therefore the unresolved cell is

```text
g1 in [1.976, 1.980]
g2 in [1.052, 1.056]
g3 in [1.996, 2.000]
g4 in [1.996, 2.000]
g5 in [1.052, 1.056]
g6 in [1.976, 1.980]
```

It is reflection symmetric and has an approximate `2,1,2,2,1,2` crystalline motif.

The interval lower bound `0.005841208384501174` is below the target `0.00598`, so the verifier correctly refused to certify this cell.

## Numerical diagnostic of the unresolved cell

These values are discovery diagnostics only, not rigorous bounds.

Cell midpoint:

```text
(1.978, 1.054, 1.998, 1.998, 1.054, 1.978)
```

High-precision floating evaluation at the midpoint:

```text
F(midpoint) ~= 0.00601180231064807619522146904636
```

Margin over target:

```text
~ 3.1802310648e-5
```

A bounded floating differential-evolution search restricted to this exact cell found approximately

```text
F ~= 0.005992617682563697
at (1.976, 1.052, 1.996, 1.996, 1.052, 1.976)
```

which remains about

```text
1.2617682564e-5
```

above the target. Thus the grid-250 failure is currently consistent with interval over-enclosure rather than a numerical violation.

## Important CI reporting issue discovered

The GitHub job was initially shown as `success` even though Python raised the `RuntimeError`, because the workflow used

```bash
python ... 2>&1 | tee output.txt
```

without `set -o pipefail`. The shell therefore returned the exit status of `tee` rather than the verifier.

The workflow must use `set -o pipefail` (or an equivalent mechanism) before any verifier command piped through `tee`. Job badges from runs before that correction must not be interpreted as certificate success without reading the verifier log.

## Next step

Move to grid 500 and/or targeted refinement around this cell. The target remains `299/50000 = 0.00598`; do not raise it until the conservative global certificate closes.
