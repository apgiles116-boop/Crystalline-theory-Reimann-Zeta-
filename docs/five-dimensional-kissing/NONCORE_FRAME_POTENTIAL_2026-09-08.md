# Sixteen-noncore projector frame potential

**Date:** 2026-09-08

## PROVED — rank-14 frame-potential floor

Let the sixteen normalized noncore projective representatives be

\[
u_i=\frac{z_i}{\|z_i\|}\in S^4,
\]

and define normalized traceless projectors

\[
\widetilde Q_i=u_i u_i^T-\frac15I.
\]

Then

\[
\widetilde Q_i\in\operatorname{Sym}_0(5),
\qquad \dim\operatorname{Sym}_0(5)=14,
\qquad \|\widetilde Q_i\|_F^2=\frac45.
\]

Let \(K\) be their \(16\times16\) Gram matrix,

\[
K_{ij}=\langle \widetilde Q_i,\widetilde Q_j\rangle
=(u_i\cdot u_j)^2-\frac15.
\]

Since \(K\succeq0\) and \(\operatorname{rank}K\le14\),

\[
\operatorname{tr}(K^2)
\ge
\frac{(\operatorname{tr}K)^2}{14}.
\]

Now

\[
\operatorname{tr}K=16\cdot\frac45=\frac{64}{5},
\]

so

\[
\operatorname{tr}(K^2)\ge\frac{2048}{175}.
\]

The diagonal contribution is

\[
\sum_i K_{ii}^2
=16\left(\frac45\right)^2
=\frac{256}{25}
=\frac{1792}{175}.
\]

Therefore

\[
2\sum_{i<j}K_{ij}^2
\ge
\frac{256}{175},
\]

and hence

\[
\boxed{
\sum_{i<j}
\left((u_i\cdot u_j)^2-\frac15\right)^2
\ge
\frac{128}{175}.
}
\]

This is unconditional for the sixteen normalized noncore Type-E projective representatives.

## PROOF-STATUS CORRECTION — circuit forcing is too strong

A previous strategy attempted to force a support-minimal eight-line Hadamard/\(D_4\) projector circuit inside every sixteen-line noncore subset.

That statement is false even in the exact \(D_5\) template.

There are exactly 240 four-line deletions from the twenty exact \(D_5\) projective lines for which the remaining sixteen contain no surviving rectangle/Hadamard circuit. These are precisely the deletions obtained by choosing one projective sign-line on each edge of a \(C_4\subset K_5\).

Thus mere nullity/circuit counting cannot be the primary unconditional route.

## Current role

The rank-14 frame-potential floor is stronger as an unconditional invariant because it applies to every sixteen-noncore configuration regardless of the support size or combinatorial form of its kernel dependencies.

The next target is to combine

\[
\sum_{i<j}
\left((u_i\cdot u_j)^2-\frac15\right)^2
\ge\frac{128}{175}
\]

with:

- the noncore raw-safe cap;
- the improved homogeneous positive-defect ceiling;
- the global squared-correlation floor;
- and the exact \(D_5\) template dichotomy between surviving rectangle circuits and the exceptional positive \(D_3\oplus D_2\) kernel structure.

The goal is a quantitative stability theorem that identifies which zero-cost model is approached without assuming a small-support circuit a priori.
