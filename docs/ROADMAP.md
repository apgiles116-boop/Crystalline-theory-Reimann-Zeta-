# Roadmap: from crystalline signal to certified inequality

## Objective

Test whether a balanced crystalline/quasicrystalline organization of gap blocks yields a **strict, reproducible, certifiable** improvement over the current 67.3312742272% public simple-zero candidate.

## Stage A — reproduce the baseline

- Import or independently reimplement the upstream finite-gap objective.
- Reproduce its published candidate to at least 10 stable decimal digits in ordinary high precision.
- Reproduce the same result under a second implementation where practical.
- Record all parameter vectors and objective decompositions.

**Stop condition:** if we cannot reproduce the reference result, do not interpret any apparent improvement.

## Stage B — test the crystalline hypothesis

Candidate families:

1. lower mechanical / Christoffel words of rational slope;
2. cyclic rotations of those words;
3. controlled phase slips / discommensurations;
4. 19-cell supercells with 15 short cells and 4 long cells;
5. larger lifts generated from the continued-fraction hierarchy of 673/1000.

For every candidate, compare against matched controls with identical counts, span, and admissibility constraints.

Metrics:

- complete finite-gap objective;
- objective split into pressure/penalty/Gram terms;
- smallest spectral margin in the finite certificate;
- sensitivity to perturbations;
- Toeplitz-symbol minima on a dense grid;
- kernel shell second differences;
- high-precision stability.

**Go condition:** an improvement survives arbitrary-precision recomputation and matched controls.

## Stage C — attack the 21-point candidate

The earlier search reported a numerical value near `0.6733396564` using a 21-point crystalline/quasicrystalline arrangement.

Required checks:

- recover the exact parameter vector;
- recompute with >= 100 decimal digits;
- verify every constraint directly;
- perturb each parameter in both directions;
- identify the active constraints and smallest slack;
- compare with randomized and optimized noncrystalline 21-point controls;
- rationalize parameters without losing the gain.

**Stop condition:** if the excess above baseline disappears with precision, perturbation, or full constraint evaluation, classify it as numerical overfit.

## Stage D — interval certificate

A genuine improved candidate must be converted into a replayable certificate:

1. rational or exactly encoded parameters;
2. outward-rounded interval evaluation of every transcendental quantity;
3. explicit finite grid and derivative/Lipschitz bounds between grid points;
4. interval-positive semidefinite / determinant / eigenvalue bounds as required;
5. explicit asymptotic and truncation error accounting;
6. final interval for the claimed lower bound lying strictly above the reference value.

The repository should contain one command that independently verifies the certificate from committed data.

## Stage E — mathematical interpretation

Only after a robust numerical gain is established should we try to prove a structural theorem explaining it. Candidate themes include:

- rearrangement inequalities for convex/concave kernel shells;
- balanced words minimizing a pair-energy functional;
- Sturmian extremality under fixed density;
- defect/soliton spacing forced by continued-fraction approximants;
- Fourier/Toeplitz lower bounds for almost-periodic Gram matrices.

A structural theorem would be more valuable than a tiny numerical improvement because it could reduce the search space and potentially permit longer finite blocks with controlled certification cost.

## Claims policy

Do not describe an uncertified numerical candidate as a proof, a solution of the Riemann Hypothesis, or a rigorous new percentage. Use the terms `candidate`, `numerical signal`, and `certified bound` distinctly.
