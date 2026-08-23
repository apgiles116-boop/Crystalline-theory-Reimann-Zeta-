# Research checkpoint — 2026-08-23

This file records the exact state of the crystalline-spectrum simple-zero project so work can resume without reconstructing the session.

## Scientific status

This project is **not a proof of the Riemann Hypothesis**. The current leading object is a computer-assisted candidate for improving the public reproducible simple-zero lower-bound checkpoint.

Public reference checkpoint:

- `trmdy/zeta-simple-zeros-673137`: approximately `0.6733127422722459...`.

Current crystalline-spectrum seven-point candidate, conditional on the remaining global six-gap inequality:

- refined Arb deduction: `0.6733365118717639448847830598448670987780...`;
- conservative rational floor stored in the verifier: `0.6733364`;
- excess over the public checkpoint: approximately `0.00002377` in proportion, or `0.00238` percentage points.

The exact candidate is frozen in `verifier/crystal_design.py`.

## Frozen q=6 candidate

Crystalline scale:

`alpha = 8796791 / 1000000 = 8.796791`.

Frequencies:

`sqrt(2), alpha, alpha*sqrt(3), 2*alpha, alpha*sqrt(7), 3*alpha, 2*alpha*sqrt(3)`.

Crystalline shell radicands: `(1, 3, 4, 7, 9, 12)`.

Window coefficient numerators, denominator `10^9`:

`(1000000000, 321105, 2731970, -18049287, 27754300, -24732331, 10205774)`.

Certificate constants:

- `p = 1/1980`;
- `target = 299/50000 = 0.00598`;
- `H_cert = 6723743/10000000 = 0.6723743`;
- window minimum requirement `3/4`;
- refined block length `m = 177`;
- proposed rational final floor `6733364/10000000`.

Exact pair weights are stored in `verifier/crystal_design.py`; every span-capacity sum is exactly `2`, and the weights are reflection symmetric.

## Rigorous fast gate — PASSED

GitHub Actions run `32621696800`, fast job `97150682500`, passed the upstream regression suite plus the crystalline tests: **23 tests passed**.

Rigorous Arb output included:

- window minimum `0.7628364729014017... > 3/4`;
- monotonicity factor `-0.0175643579251023... < 0`;
- `H = 0.6723743616001399277... > H_cert`;
- final conditional bound `0.6733365118717639448847830598448671...`.

See `verifier/FAST_GATE_RESULT.md` for the full Arb enclosures.

Therefore the exact frequencies, exact capacities, symmetry, window positivity, monotonicity, certified window functional, and final deduction arithmetic are rigorously established **conditional on the global finite-gap inequality**.

## Sole remaining mathematical gate

We must prove

`F(g1,...,g6) >= 299/50000` for every `gi >= 0`.

Here

`F = (1/1980) * sum(gi) + sum_{0<=i<j<=6} a_ij * w(y_j-y_i)`,

with `y_j = g1+...+g_j` and `w=(K/K(0))^2`.

Because `w >= 0`, pressure alone proves the inequality whenever

`sum(gi) >= target/p = 11.8404`.

Thus the global problem reduces to the compact simplex

`gi >= 0`, `sum(gi) < 11.8404`.

The upstream `verify_general` machinery is fail-closed: it uses pressure pruning, rigorous interval lower bounds for the pair-energy terms, and an Arb-validated convex-tangent/Hessian pruner. Any unresolved terminal cell causes failure rather than false certification.

## Numerical adversarial evidence

Extensive floating searches found no violation of the target. The best known floating minimum is

`F_min ~= 0.005989552075279514`,

with margin above target

`~ 9.55207528e-6`.

Representative minimizing gaps:

`(1.039637978309537, 1.983372509848868, 1.044559829360473, 2.927502540173843, 1.043442852256447, 1.029969455148929)`.

At that point the numerical Hessian eigenvalues are approximately

`(0.1809517, 0.26883482, 0.54431061, 0.61601053, 0.9962556, 1.49782885)`.

All are positive; the basin is isolated rather than nearly flat. The gradient infinity norm was approximately `1.63e-9`, with Hessian condition number about `8.28`.

## Grid-250 global interval attempt — UNRESOLVED, NOT A COUNTEREXAMPLE

The single-worker grid-250 verifier run `32622361840`, job `97152392234`, reached a terminal cell that its interval bounds could not certify:

```text
box=((494,494),(263,263),(499,499),(499,499),(263,263),(494,494))
lower=0.005841208384501174
```

This corresponds to

```text
g1 in [1.976,1.980]
g2 in [1.052,1.056]
g3 in [1.996,2.000]
g4 in [1.996,2.000]
g5 in [1.052,1.056]
g6 in [1.976,1.980]
```

The exact raw result and artifact identifiers are preserved in `verifier/GRID250_RESULT.md`.

Numerical diagnostics inside this exact cell do **not** indicate a target violation:

- midpoint `(1.978,1.054,1.998,1.998,1.054,1.978)` gives `F ~= 0.006011802310648076...`;
- bounded floating search in the cell found `F ~= 0.005992617682563697` near its lower corner;
- this is still approximately `1.26177e-5` above the target.

Therefore the current interpretation is interval over-enclosure at grid 250, not a numerical counterexample. The next natural global resolution is grid 500, or targeted refinement of this symmetric `2,1,2,2,1,2` cell.

## CI reporting bug found and fixed

The first grid-250 GitHub job badge was misleadingly shown as `success` because the command was piped through `tee` without shell `pipefail`; Python raised a `RuntimeError`, but the shell returned the exit code of `tee`.

The workflow on both `main` and `ci/crystal-fast-gate` has now been corrected to use `set -o pipefail` for interval commands. Pre-fix interval job badges must not be treated as proof results without reading their logs.

## Multiprocessing correctness fix

While preparing the interval campaign, a separate infrastructure bug was found: the upstream parallel verifier serialized `KernelSpec` but originally omitted the new `algebraic_omegas` field. Any multi-worker crystalline run would therefore have lost the crystalline frequencies during worker reconstruction.

`verifier/apply_algebraic_frequency.py` now also patches `parallel.py` so `algebraic_omegas` is serialized/deserialized exactly as `(numerator, denominator, radicand)` triples.

`verifier/test_crystal_design.py` contains a regression test verifying that the parallel primitive round-trip preserves `crystal_design.KERNEL` and its algebraic frequencies. The fast CI gate passed after this fix.

## Interval campaign

Resolution ladder remains

`250 -> 500 -> 1000 -> 2000 -> 4000`.

Grid 250 is now classified as **insufficiently sharp** because of the unresolved terminal cell above. Do not interpret it as a falsification of the candidate.

An eight-worker grid-250 run `32622511225` / job `97152765163` had also been started after the multiprocessing fix. Its workflow version predates the `pipefail` correction, so its final GitHub badge alone is not authoritative; inspect its verifier log before using it.

## Earlier branches and dead ends

### Direct-defect 21-point branch

A floating candidate near `0.6733396564` was discovered at `p=0.0026`, but rigorous certification only established a direct-defect floor corresponding to roughly `0.673269`, below the public checkpoint. Therefore the earlier 21-point number is **not** a surviving record candidate.

A later 35-point floating experiment near `67.34416%` remained uncertified. A 19-point candidate failed adversarial composition.

### q=20 uniform finite-gap branch

A q=20 uniform-weight candidate initially looked promising, but exhaustive binary-word search exposed an adversarial repeating `112112...` motif and continuous relaxation fell to approximately `F=0.01112203`, below the proposed target `0.0115`. This branch is recorded as **falsified** in `experiments/q20_uniform_probe.py`.

### 673/1000 crystalline obstruction

The exact balanced mechanical word

`g_i = 1 + floor((i+1)327/673) - floor(i*327/673)`

reproduces the known pure-pair-energy frontier obstruction. Its periodic pair energy was independently reproduced at approximately `0.00352350665949`, agreeing with the upstream ceiling `< 0.003523506664`.

The coarse defect interpretation gives 327 paired units, 19 phase defects, cells of lengths 35/37 with fifteen 35-cells and four 37-cells, and long-cell spacings `5,5,5,4` up to rotation. Continued fraction: `673/1000 = [0;1,2,17,4,1,3]`.

## Repository cleanup at checkpoint

- obsolete malformed `verifier/algebraic_frequency.patch` removed;
- source-shape-checked `verifier/apply_algebraic_frequency.py` is the supported extension mechanism;
- root README updated to the current q=6 candidate hierarchy;
- roadmap updated to the current global interval stage;
- grid-250 failure details preserved in `verifier/GRID250_RESULT.md`.

## Resume procedure

1. Inspect the final raw log of the eight-worker grid-250 run if useful; ignore its badge unless the verifier output itself says `verified=True`.
2. Run the conservative target at grid 500 with corrected `pipefail` and the validated multiprocessing serialization.
3. If grid 500 still leaves terminal cells, collect them and refine them directly or proceed to grid 1000.
4. Preserve exact failed cells, lower bounds, table hashes, node counts, and artifacts from every rigorous run.
5. Do not raise the target above `0.00598` until the conservative target is globally certified.
6. Only after certification consider the numerical stretch target `0.005984`, which would project to approximately `0.6733391070` but currently has only about `5.55e-6` floating margin to the observed minimum.

## Claims policy

Until the global six-gap interval proof succeeds, `0.673336511871...` must be described as a **candidate conditional bound**, not a new theorem, published record, or proof of the Riemann Hypothesis.
