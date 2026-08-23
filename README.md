# Crystalline Theory / Riemann Zeta Experiments

Experimental research repository for testing whether crystalline, quasicrystalline, and defect-lattice structure can improve the finite gap inequalities used in current lower-bound candidates for simple zeros of the Riemann zeta function on the critical line.

## Status

This is an exploratory numerical project, not a proof of the Riemann Hypothesis and not yet a certified improvement to the published/public candidate bounds.

Current reference checkpoint:

- upstream reproducibly certified public candidate: **0.6733127422722459...** (67.3312742272%) in `trmdy/zeta-simple-zeros-673137`;
- our earlier unconstrained 21-point crystalline/quasicrystalline search produced a numerical candidate near **0.6733396564** (67.33396564%), but it is **not certified**;
- the current objective is to determine whether that numerical gain corresponds to a real finite-gap certificate or is only a floating-point/search artifact.

## First reproduced checkpoints

The repository now independently reproduces, in ordinary floating-point arithmetic, two upstream numerical objects before attempting any new optimization:

1. **Nine-point obstruction.** The public q=8 objective evaluated at its reported floating minimizer is `0.00610273048185719...`, agreeing with the upstream value `0.006102730481857188` to binary64 accuracy. The certified target is `15211/2500000 = 0.0060844`.
2. **Balanced 673/1000 crystal.** The exact lower mechanical word of slope `327/673`, converted to gaps `1 + bit`, has 673 gaps of total length 1000 (346 one-gaps and 327 two-gaps). Periodizing that configuration and evaluating the public squared kernel gives pair energy approximately **0.00352350665949**, below the upstream stated ceiling `0.003523506664`.

The second check is especially important: the Sturmian/Christoffel geometry is not merely a visual analogy. It is the explicit pure-pair-energy obstruction already sitting at the known method frontier.

## Working geometric hypothesis

The exact frontier configuration is

`g_i = 1 + floor((i+1)327/673) - floor(i*327/673)`.

It is a balanced Christoffel/Sturmian period with 673 points over length 1000. The earlier defect-lattice decomposition remains an exploratory coarse-graining of this exact word:

- continued fraction `673/1000 = [0; 1, 2, 17, 4, 1, 3]`;
- a 19-cell coarse pattern with fifteen 35-cells and four 37-cells;
- the four 37-cells have cyclic separations `5, 5, 5, 4` up to rotation;
- this suggests a hierarchy dimer -> phase slip -> Sturmian/Christoffel superstructure.

The decisive question is whether this organization can be exploited by a finite certificate richer than pure pair energy, not merely whether it minimizes a pair-energy functional.

## Research program

1. Reproduce the reference finite-gap objective and known certified candidate. **Done for the numerical objective.**
2. Reproduce the exact 673/1000 balanced obstruction and its pair energy. **Done numerically.**
3. Recover/reconstruct the earlier 21-point crystalline candidate and evaluate it against the exact public objective family.
4. Search 21-point and larger blocks using balanced words plus controlled phason/phase-slip defects.
5. Compare crystalline candidates with random/noncrystalline controls at identical gap counts and span.
6. Inspect Hessian soft modes, Toeplitz/Fourier spectra, and shell-wise second differences of the kernel.
7. Rationalize any surviving improvement and run a fail-closed interval certificate.

## Layout

- `src/crystalline_zeta/geometry.py` — balanced words, defect cells, continued fractions.
- `src/crystalline_zeta/finite_gap.py` — floating reproduction of the public q=8 finite-gap objective.
- `src/crystalline_zeta/spectral.py` — generic Gram/spectral diagnostics.
- `experiments/reproduce_crystalline_obstruction.py` — reproduces both upstream numerical checkpoints.
- `experiments/probe_673_1000.py` — defect-lattice geometry probe.
- `docs/ROADMAP.md` — certification path and stop/go criteria.

## Scientific standard

A better floating-point score is only a discovery signal. A claimed mathematical improvement requires a finite certificate with outward-rounded interval arithmetic, explicit asymptotic bookkeeping, and independent replay.

## Upstream reference

This work builds on the public MIT-licensed finite-certificate line represented by `trmdy/zeta-simple-zeros-673137` and its cited predecessors. Constants or formulas transcribed from upstream are identified in source comments and attribution will be preserved as the project grows.
