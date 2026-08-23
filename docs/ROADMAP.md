# Roadmap: crystalline signal to certified six-gap inequality

## Objective

Determine whether the frozen crystalline-spectrum seven-point candidate yields a strict, reproducible, certifiable improvement over the public reproducible checkpoint `0.6733127422722459...` for the proportion of simple zeros on the critical line.

This project is not a proof of the Riemann Hypothesis.

## Stage A — reproduce the baseline — DONE

- Reproduced the public q=8 floating finite-gap objective at its reported minimizer.
- Reproduced the exact balanced 673/1000 Sturmian/Christoffel obstruction numerically.
- Periodic pair energy reproduced at approximately `0.00352350665949`, agreeing with the upstream ceiling `< 0.003523506664`.

The crystalline geometry is therefore not merely visual analogy; it is present in the known pure-pair-energy obstruction.

## Stage B — exploratory crystalline branches — DONE / TRIAGED

### Direct-defect 21-point branch

A numerical candidate near `0.6733396564` appeared at `p=0.0026`, but rigorous certification only supported a floor near `0.673269`, below the public checkpoint.

**Status: rejected as a record-breaking candidate.**

### q=20 uniform finite-gap branch

A candidate target `0.0115` was defeated by an adversarial repeating `112112...` motif; continuous relaxation reached approximately `0.01112203`.

**Status: falsified.**

### Crystalline-spectrum seven-point branch

An exact q=6 candidate was frozen with algebraic shell frequencies based on radicands `(1,3,4,7,9,12)` and exact rational weights saturating all span capacities.

**Status: current lead.**

## Stage C — rigorous non-global gate — DONE

GitHub Actions run `32621696800` passed all fast Arb gates and 23 tests.

Established rigorously:

- exact algebraic crystalline frequencies;
- exact span capacities;
- reflection symmetry;
- window positivity;
- monotonicity condition;
- certified `H` lower bound;
- refined deduction arithmetic.

Conditional refined value:

`0.6733365118717639448847830598448671...`.

See `verifier/FAST_GATE_RESULT.md`.

## Stage D — global six-gap interval certificate — CURRENT

The sole remaining mathematical gate is

`F(g1,...,g6) >= 299/50000 = 0.00598`

for all `g_i >= 0`.

Pressure alone closes the region `sum(g_i) >= 11.8404`, reducing the search to a compact simplex.

The verifier is fail-closed and uses:

1. one-body coordinate pruning;
2. pressure pruning;
3. outward-rounded interval pair-energy lower bounds;
4. Arb-validated positive-definite Hessian / convex-tangent pruning;
5. recursive subdivision of unresolved boxes.

Resolution ladder:

`250 -> 500 -> 1000 -> 2000 -> 4000`.

### Grid 250 result

Grid 250 did **not** close globally. The single-worker verifier stopped at

```text
((494,494),(263,263),(499,499),(499,499),(263,263),(494,494))
```

with interval lower bound `0.005841208384501174`.

This is an unresolved terminal cell, not a counterexample. Numerical diagnostics inside the same cell remained above target: midpoint `F ~= 0.006011802310648076`, and bounded floating search found approximately `0.005992617682563697`.

Full details: `verifier/GRID250_RESULT.md`.

**Next step:** grid 500 and/or targeted subdivision of the symmetric `2,1,2,2,1,2` cell.

### CI hardening

Two infrastructure issues were found and corrected:

- multi-worker serialization now preserves `algebraic_omegas` exactly, with a regression test;
- interval commands piped through `tee` now use `set -o pipefail`, so a verifier exception correctly fails the GitHub job.

Pre-fix green interval badges are not proof results unless the raw verifier output itself says verification succeeded.

## Stage E — hardening after first global success

If the conservative target `0.00598` certifies:

1. record full verifier report, node counts, maximum depth, table hashes, and exact environment;
2. repeat at a finer resolution where practical;
3. attempt a `use_tangent=False` re-verification or other independent hardening route where computational cost permits;
4. preserve artifacts and logs in the repository;
5. distinguish computational certification from peer review/publication.

Only after the conservative target is certified should a higher target be explored.

A possible later stretch target is `0.005984`, projecting to approximately `0.6733391070`, but its observed floating margin is only about `5.55e-6`; it is not currently a claim.

## Stage F — mathematical interpretation

After certification, investigate why the shell family and minimizing gap patterns work. Candidate themes:

- reciprocal-lattice / shell-spectrum interpretation of squared norms `1,3,4,7,9,12`;
- rearrangement inequalities for kernel shells;
- Sturmian extremality under fixed density;
- defect/soliton spacing from continued-fraction approximants;
- Fourier/Toeplitz bounds for almost-periodic Gram structures;
- analytical explanation of the observed minimizing motifs.

A structural theorem would be more valuable than a tiny numerical gain because it could reduce the global search space and support longer finite blocks.

## Claims policy

Use the following terms distinctly:

- **numerical candidate** — floating evidence only;
- **conditional candidate bound** — all gates except the stated remaining condition are rigorous;
- **computationally certified bound** — complete outward-rounded global certificate succeeds;
- **published/peer-reviewed theorem** — only after external mathematical review and publication.

Do not describe the current candidate as a proof of the Riemann Hypothesis or as a certified new record until Stage D succeeds.

See `docs/CHECKPOINT_2026-08-23.md` for the detailed handoff state and run IDs.
