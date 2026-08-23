# Crystalline Theory / Riemann Zeta Experiments

Experimental research repository for testing whether crystalline, quasicrystalline, and defect-lattice structure can improve the finite gap inequalities used in current lower-bound candidates for simple zeros of the Riemann zeta function on the critical line.

## Status

This is an exploratory numerical project, not a proof of the Riemann Hypothesis and not yet a certified improvement to the published/public candidate bounds.

Current reference checkpoint:

- upstream reproducibly certified public candidate: **0.6733127422722459...** (67.3312742272%) in `trmdy/zeta-simple-zeros-673137`;
- our earlier unconstrained 21-point crystalline/quasicrystalline search produced a numerical candidate near **0.6733396564** (67.33396564%), but it is **not certified**;
- the current objective is to determine whether that numerical gain corresponds to a real finite-gap certificate or is only a floating-point/search artifact.

## Working geometric hypothesis

The obstruction near density `673/1000` appears to admit a defect-lattice description:

- 327 paired/dimerized short-gap units;
- 19 excess short-gap phase defects;
- defect-cell lengths concentrated at 35 and 37;
- a representative decomposition has fifteen 35-cells and four 37-cells;
- the four 37-cells occur with separations `5, 5, 5, 4`;
- continued fraction `673/1000 = [0; 1, 2, 17, 4, 1, 3]` suggests a hierarchical dimer -> soliton/phase-slip -> Sturmian/Christoffel organization.

This repo will test that hypothesis against direct Gram/spectral-defect calculations rather than treating the geometry as evidence by itself.

## Research program

1. Reproduce the reference finite-gap objective and known certified candidate.
2. Generate balanced/mechanical (Sturmian/Christoffel) binary gap words and controlled phase slips.
3. Search 21-point and larger blocks for low direct spectral defect plus pressure.
4. Compare crystalline candidates with random/noncrystalline controls at identical gap counts and span.
5. Inspect Toeplitz/Fourier spectra and shell-wise second differences of the kernel.
6. Turn any improvement into rational parameters and interval-certify the global inequality.

## Layout

- `src/crystalline_zeta/geometry.py` — balanced words, defect cells, continued fractions.
- `src/crystalline_zeta/spectral.py` — generic Gram/spectral diagnostics.
- `experiments/probe_673_1000.py` — first defect-lattice experiment.
- `docs/ROADMAP.md` — certification path and stop/go criteria.

## Scientific standard

A better floating-point score is only a discovery signal. A claimed mathematical improvement requires a finite certificate with outward-rounded interval arithmetic, explicit asymptotic bookkeeping, and independent replay.

## Upstream reference

This work builds on the public finite-certificate line represented by `trmdy/zeta-simple-zeros-673137` and its cited predecessors. We will preserve attribution as upstream code or formulas are imported.
