# Crystalline Zeta Simple-Zero Certificate

Research repository for a crystalline-spectrum seven-point / six-gap finite certificate related to lower bounds for simple zeros of the Riemann zeta function on the critical line.

## Current status

The previously outstanding global six-gap interval problem has now been closed for the frozen candidate at the exact target

`299/50000 = 0.00598`.

The completed workflow used two independent execution routes:

1. a single-process exhaustive grid-250 collector;
2. an eight-shard exhaustive grid-250 collector plus merge/refinement.

Both routes found exactly **209 unresolved grid-250 terminal cells**. Those cells were tiled exactly into **13,376 grid-500 children**, and **all 13,376 children were rigorously pruned with zero unresolved cells**.

The resulting mixed-resolution status is:

`mixed_global_verified True`

with the complete domain covered by rigorous grid-250 pruning plus targeted grid-500 refinement.

The frozen deduction gives

`0.6733365118717639448847830598448671...`

with conservative rational reporting floor

**`0.6733364` = 67.33364%.**

This is **not a proof of the Riemann Hypothesis**. It is a computationally rigorous finite certificate inside the stated analytic framework. The repository does **not** claim an independently accepted literature record until the analytic reduction and implementation have been externally reviewed and replayed.

For the complete audit record, exact counts, hashes, workflow identifiers, and reproducibility procedure, see:

**[`CERTIFICATE_REPORT_2026-08-23.md`](CERTIFICATE_REPORT_2026-08-23.md)**

## Frozen crystalline spectrum

Let

`alpha = 8796791/1000000 = 8.796791`.

The candidate frequencies are

`sqrt(2), alpha, alpha*sqrt(3), 2*alpha, alpha*sqrt(7), 3*alpha, 2*alpha*sqrt(3)`.

The shell radicands `(1, 3, 4, 7, 9, 12)` are treated exactly through Arb algebraic square roots. Pair weights are exact rationals and reflection symmetric. The authoritative frozen specification is `verifier/crystal_design.py`.

## Global certificate summary

Main certificate workflow:

- workflow run: `32661204481`
- validated PR head: `17a7e9fe049ac206c08050a898b65f61423c6e4c`
- merged main commit: `f327c50b4251f86a76f53b525f386c5441278dc4`
- upstream verifier pin: `1610b97b7895ff34982260f8dcaf04a0f7b82cf7`
- Python: `3.13`
- `python-flint`: `0.9.0`

Grid 250:

- initial boxes: `64`
- nodes: `2,587,070`
- pruned: `1,293,358`
- splits: `1,293,503`
- unresolved terminal cells: `209`

Grid 250 hashes:

- `w_table_sha256 = 7f68585c533de55fcad254bb89d674a088f0959b63ce492311d4abee044d6002`
- `w_second_table_sha256 = 98cc22c7e26b4f5c03665a361fd7014150aa16d9aaf3c3d3fb9c942c6bfbffff`

Exact grid-500 refinement:

- parents: `209`
- children: `13,376`
- pruned: `13,376`
- unresolved: `0`
- splits: `0`

Grid 500 hashes:

- `w_table_sha256 = d504bb8c894f0a6e8f42da80a77b1526f11c35df750cabdff8d34e8cdf6a1cff`
- `w_second_table_sha256 = 95aba8d334eadcb03d8294a2d21c53b5570fa5545c82b016625935f604ed2640`

No grid-1000 fallback was required for the completed global certificate.

## Why the two-route replay matters

The single-process collector and the sharded collector independently reproduced the same global node/prune/split totals, the same table hashes, and the same **209** unresolved grid-250 cells. Each route then obtained zero unresolved cells after exact grid-500 refinement.

The sharded merge additionally refuses to proceed if a shard is missing, duplicated, uses a different target, or has inconsistent lower-bound table hashes.

## Repository layout

- `CERTIFICATE_REPORT_2026-08-23.md` — permanent audit report and replay checklist.
- `verifier/crystal_design.py` — exact frozen crystalline q=6 candidate.
- `verifier/crystal_verify.py` — rigorous fast and global interval drivers.
- `verifier/apply_algebraic_frequency.py` — fail-closed verifier extension for exact algebraic frequencies, supplied initial boxes, and terminal-cell collection.
- `verifier/grid250_collect_and_refine.py` — full exhaustive collector and exact refinement ladder.
- `verifier/grid250_shard.py` — disjoint grid-250 shard runner.
- `verifier/grid250_merge_and_refine.py` — shard integrity checks and targeted refinement.
- `verifier/FAST_GATE_RESULT.md` — rigorous fast-gate transcript.
- `verifier/GRID250_RESULT.md` — original fail-fast grid-250 diagnostic.
- `verifier/GRID500_TARGETED_RESULT.md` — earlier rigorous local refinement of the original troublesome parent.
- `docs/CHECKPOINT_2026-08-23.md` — research checkpoint and historical handoff state.
- `docs/ROADMAP.md` — certification path and stop/go criteria.
- `experiments/` — numerical and structural exploratory work.

## Scientific standard

Floating-point optimization is treated only as discovery evidence. Certification requires outward-rounded interval arithmetic, complete domain coverage, exact rational/algebraic parameters, fail-closed verifier behavior, and reproducible replay.

The present result closes the frozen six-gap finite inequality at target `0.00598`. The appropriate next step is independent mathematical and implementation review, not treating the result as accepted merely because CI is green.

## Upstream reference

This work builds on the public MIT-licensed finite-certificate line represented by `trmdy/zeta-simple-zeros-673137` and its cited predecessors. Upstream formulas and code are attributed where used.

External reproductions, audits, counterexamples, and independent derivations are welcome.