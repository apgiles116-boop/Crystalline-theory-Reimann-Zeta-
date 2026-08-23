# Rigorous fast-gate result

The frozen crystalline-spectrum seven-point candidate passed the complete
non-global Arb gate on GitHub Actions on 2026-08-23.

CI context:

- workflow: `crystalline-seven-point-certificate`
- successful run id: `32621696800`
- fast job id: `97150682500`
- CI pull request: #1 (`Run crystalline seven-point fast gate`)
- pinned dependency: `python-flint==0.9.0` through upstream
  `trmdy/zeta-simple-zeros-673137`

The run executed the upstream regression tests plus the crystalline-specific
tests: **23 tests passed**.

## Arb enclosures

```text
min_v
[0.7628364729014017165276972942677957689738832414150238037109375000000000000000 +/- 3.41e-77]

max_vprime_over_s
[-0.01756435792510229868004841091873549065218655764649120616736287809880040370873 +/- 4.83e-78]

c1
[0.753224381238422306286363997603102685295679375230973831112470354010358151263 +/- 9.03e-76]

H
[0.67237436160013992774910053480589771719373910450488093246065463295641886769 +/- 2.61e-75]

A
[1.022580000000000000000000000000000000000000000000000000000000000000000000000 +/- 4.40e-77]

Phi
[1.022510004054494338279068763211832640320860297264854901712002807562467721488 +/- 2.72e-76]

bound
[0.6733365118717639448847830598448670987780447239557214145721773252654640966696 +/- 6.73e-77]
```

Every requested inequality in the fast gate returned `True`, ending with
`fast_parts_verified True`.

## What remains

This result rigorously establishes the exact algebraic frequencies, exact span
capacities, reflection symmetry, window lower bound, monotonicity, certified
window functional, and final deduction arithmetic **conditional on the finite
gap inequality**.

The sole load-bearing missing step is now to prove with outward-rounded
interval arithmetic

\[
F(g_1,\dots,g_6)\ge \frac{299}{50000}
\qquad \text{for every }g_i\ge0.
\]

Until that global interval subdivision succeeds, the projected
`0.673336511871...` remains a candidate rather than a certified lower bound.
