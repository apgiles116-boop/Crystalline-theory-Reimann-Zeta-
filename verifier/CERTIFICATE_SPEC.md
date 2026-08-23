# Crystalline-spectrum seven-point candidate

This is **not yet a theorem**. The decisive missing step is a successful Arb
interval run over all \(g\in[0,\infty)^6\).

Exact spectrum:
\[
\sqrt2,\quad
\alpha,\alpha\sqrt3,2\alpha,\alpha\sqrt7,3\alpha,2\alpha\sqrt3,
\qquad
\alpha=\frac{8796791}{10^6}.
\]

Window perturbation coefficients (denominator \(10^9\)):
\[
321105,\ 2731970,\ -18049287,\ 27754300,\ -24732331,\ 10205774.
\]

Certificate constants:
\[
p=\frac1{1980},\qquad
\varepsilon=\frac{299}{50000},\qquad
H(v)\ge\frac{6723743}{10^7}.
\]

The pair weights in `crystal_design.py` have denominator \(10^6\);
every span-capacity sum is exactly \(2\).

For the seven-point refined deduction with \(m=177\), these conservative
inputs give
\[
B\approx0.67333651187176394488478,
\]
and the bundle asks only for the rational floor
\[
B\ge 0.6733364.
\]

## Numerical analytic precheck

Independent high-precision floating evaluation gives:

- `H(v) ~= 0.67237436160013992775`, margin over `H_CERT` about `6.16e-8`;
- `min v ~= 0.76290304453184`, comfortably above `3/4`;
- `max(v'(s)/s) ~= -0.0194998` on a dense grid, consistent with monotonicity;
- refined bound `~= 0.67333651187176394488`.

These are discovery/reproduction checks only. The Arb verifier remains the
load-bearing step.
