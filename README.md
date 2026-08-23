# Crystalline Theory / Riemann Zeta Experiments

Experimental research repository testing whether crystalline, quasicrystalline, and defect-lattice structure can improve finite-gap inequalities used in lower-bound candidates for simple zeros of the Riemann zeta function on the critical line.

## Current status

This is **not a proof of the Riemann Hypothesis** and the current result is **not yet a certified new lower bound**.

Public reproducible reference checkpoint:

- `trmdy/zeta-simple-zeros-673137`: approximately **0.6733127422722459...** (67.3312742272%).

Current leading candidate:

- crystalline-spectrum seven-point / six-gap certificate;
- exact frozen parameters in `verifier/crystal_design.py`;
- rigorous non-global Arb gate: **PASSED**;
- conditional refined bound: **0.6733365118717639448847830598448671...**;
- conservative rational floor: **0.6733364**;
- sole remaining mathematical gate: prove

  `F(g1,...,g6) >= 299/50000`

  for every nonnegative six-gap vector.

The pressure term alone covers `sum(g_i) >= 11.8404`, so the remaining global proof is a compact six-dimensional interval problem. A staged fail-closed interval campaign is in progress.

See `docs/CHECKPOINT_2026-08-23.md` for the complete handoff state, exact CI run IDs, numerical minimizer, Hessian data, interval strategy, and resume procedure.

## Frozen crystalline spectrum

Let

`alpha = 8796791/1000000 = 8.796791`.

The candidate frequencies are

`sqrt(2), alpha, alpha*sqrt(3), 2*alpha, alpha*sqrt(7), 3*alpha, 2*alpha*sqrt(3)`.

The shell radicands `(1, 3, 4, 7, 9, 12)` are treated exactly through Arb algebraic square roots. Pair weights are exact rationals, reflection symmetric, and every span-capacity sum is exactly 2.

## Rigorous fast gate

GitHub Actions run `32621696800`, job `97150682500`, passed the full upstream regression set plus crystalline-specific tests: **23 tests passed**.

The Arb checks rigorously established, conditional only on the global six-gap inequality:

- exact crystalline frequencies;
- span capacities and reflection symmetry;
- window positivity;
- window monotonicity;
- certified `H` lower bound;
- final deduction arithmetic.

Full enclosures are recorded in `verifier/FAST_GATE_RESULT.md`.

## Numerical global evidence

Extensive adversarial floating searches found a best known minimum

`F_min ~= 0.005989552075279514`,

above the certified target `0.00598` by approximately `9.55e-6`.

Representative minimizing gaps:

`(1.039637978309537, 1.983372509848868, 1.044559829360473, 2.927502540173843, 1.043442852256447, 1.029969455148929)`.

The numerical Hessian there is positive definite, with eigenvalues approximately

`(0.1809517, 0.26883482, 0.54431061, 0.61601053, 0.9962556, 1.49782885)`.

This is evidence only; the outward-rounded global interval proof remains load-bearing.

## Interval campaign

The verifier uses pressure pruning, rigorous lower tables for the pair kernel, and an Arb-validated convex-tangent/Hessian pruner. It is fail-closed: unresolved terminal cells cause failure rather than false certification.

Planned resolution ladder:

`250 -> 500 -> 1000 -> 2000 -> 4000`.

The repository also contains a multiprocessing correctness fix: the crystalline `algebraic_omegas` field is now preserved through worker serialization/deserialization, with a regression test.

## Earlier branches / dead ends

- The earlier direct-defect 21-point floating candidate near **0.6733396564** did **not** survive rigorous certification; its certified floor was only about **0.673269**, below the public checkpoint.
- A q=20 uniform-weight candidate was **falsified** by an adversarial repeating `112112...` motif; see `experiments/q20_uniform_probe.py`.
- The exact balanced 673/1000 Sturmian/Christoffel obstruction was independently reproduced with periodic pair energy approximately **0.00352350665949**, confirming that crystalline geometry is genuinely present at the known pure-pair-energy frontier.

## Repository layout

- `verifier/crystal_design.py` — exact frozen crystalline q=6 candidate.
- `verifier/crystal_verify.py` — rigorous fast and global interval drivers.
- `verifier/apply_algebraic_frequency.py` — fail-closed extension of the pinned upstream verifier for exact algebraic crystalline frequencies and multiprocessing transport.
- `verifier/test_crystal_design.py` — exact candidate/regression tests.
- `verifier/FAST_GATE_RESULT.md` — successful rigorous fast-gate transcript.
- `docs/CHECKPOINT_2026-08-23.md` — current complete research checkpoint and resume procedure.
- `docs/ROADMAP.md` — certification path and stop/go criteria.
- `src/crystalline_zeta/geometry.py` — balanced words, defect cells, continued fractions.
- `src/crystalline_zeta/finite_gap.py` — floating reproduction of the public finite-gap objective.
- `src/crystalline_zeta/spectral.py` — spectral diagnostics.
- `experiments/reproduce_crystalline_obstruction.py` — reference and 673/1000 reproductions.

## Scientific standard

A better floating-point score is only a discovery signal. A mathematical improvement requires an explicit finite certificate with outward-rounded interval arithmetic, complete asymptotic bookkeeping, and independent replay. Until the six-gap global verifier succeeds, the `0.673336511871...` value is a **candidate conditional bound** only.

## Upstream reference

This work builds on the public MIT-licensed finite-certificate line represented by `trmdy/zeta-simple-zeros-673137` and its cited predecessors. Upstream formulas and code are attributed where used.
