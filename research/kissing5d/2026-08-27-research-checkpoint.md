# 5D Kissing Number Research Checkpoint

**Date:** 2026-08-27  
**Branch:** `kissing5d-compute`  
**Problem:** Determine the kissing number in dimension 5. Current published status remains `40 <= tau_5 <= 44`.

## 1. Current objective

Target the hypothetical cases `N = 41, 42, 43, 44` separately, rather than only optimizing the global upper bound. The working strategy now has four interacting layers:

1. lifted Levenshtein / one-point LP calculations,
2. three-point SDP calibration,
3. second-Lasserre / four-point SDP calculations,
4. direct structural analysis of best-known numerical 41--44 point codes.

The main goal is a rigorous obstruction for at least `N=41`; once 41 is excluded, the kissing number is 40 and all larger cases fall automatically.

---

## 2. Local projection / 23-point slab lemma

For a unit vector in `R^5`, write

`x_i = (sqrt(1-z_i^2) u_i, z_i)`, with `u_i in S^3`.

The kissing constraint gives

`x_i . x_j <= 1/2`, hence

`u_i . u_j <= G(z_i,z_j)`

with

`G(z,w) = (1/2 - zw)/(sqrt(1-z^2)sqrt(1-w^2))`.

For positive `0 < a <= z,w <= b < 1`,

`dG/dw = (w/2-z)/(sqrt(1-z^2)(1-w^2)^(3/2))`.

Thus the maximum over a rectangle occurs at corners. Setting `G(a,b)=1/2` gives

`a^2 + b^2 - 4ab + 3a^2 b^2 = 0`,

so the larger endpoint is

`b = a(2 + sqrt(3(1-a^2)))/(1+3a^2)`.

On such a slab all projected pairwise inner products are at most `1/2`.

Using the modern theorem of de Laat--Leijenhorst--de Muinck Keizer that the D4 root system / 24-cell is an optimal 24-point spherical code in `S^3`, together with uniqueness of the optimal 4D kissing configuration, the endpoint case can be sharpened: if 24 projected points existed at equality, the contact edges would force opposite slab endpoints, making the D4 contact graph bipartite, but D4 contains triangles. Therefore this local slab has at most 23 points, including the boundary case.

**Status:** local lemma appears rigorous; it is not yet a global proof of `tau_5=40`.

---

## 3. User-provided Levenshtein document and second-level lift

Source used: Boyvalenkov--Dragnev--Hardin--Saff--Stoyanova, *Bounds for Spherical Codes: The Levenshtein Framework Lifted*.

Key facts reproduced from the defining quadrature equations for `n=5`:

- for the principal second-level branch, the largest quadrature node continues smoothly beyond the paper's published `N=40` table;
- computed values:

| N | largest lifted node beta_4 |
|---:|---:|
| 41 | ~0.48762 |
| 42 | ~0.50373 |
| 43 | ~0.51885 |
| 44 | ~0.53230 |

The node crosses the kissing threshold `1/2` near

`N_cross ~= 41.7654428885`.

However, positive definiteness fails earlier. The degree-8 Gegenbauer coefficient changes sign near

`N ~= 37.9303`.

At the threshold crossing, in normalization `g(1)=1`, the only bad modes found were approximately

`g_8 = -0.147210151`,
`g_9 = -0.041038438`,

and

`g_0 = 1/N_cross ~= 0.02394324`.

Therefore the principal `{8,9}` second-level polynomial cannot directly prove the 5D kissing bound for 42 or lower.

A broad search over alternative two-harmonic one-variable lifts, including pairs through degree 16 such as `{9,10}`, `{8,11}`, etc., did not find a polynomial simultaneously positive-definite and nonpositive on the kissing interval with a bound of 42, 43, or 44.

**Conclusion:** ordinary one-variable LP is exhausted as a route to `<=40`; the obstruction must use genuine multi-point structure.

---

## 4. Three-point SDP calibration

Public implementation used: `nanleij/ClusteredLowRankSolver.jl`, especially `examples/ThreePointBound.jl`.

The solver pipeline is operational on GitHub Actions.

Verified checkpoints:

- degree 4: bound `48.000000000000000...`
- degree 8: bound `45.53288761247117`

At degree 8 the primal and dual agreed to about `5e-19`, giving a strong numerical pipeline check.

Published calibration target for degree 14 is approximately

`44.99899685...`

which is the classical three-point result yielding the integer upper bound 44.

At checkpoint time, the degree-11 and degree-14 calibration jobs were still running.

**Workflow:** `.github/workflows/kissing5d-threepoint.yml` or equivalent three-point workflow already present on this branch.

---

## 5. Second Lasserre / four-point SDP

Released code/data source recovered from 4TU dataset containing the `LasserreSphericalCodes` Julia package and verification machinery.

The actual `las2` routine is operational for the 5D `60 degree` problem.

Equal-degree calibration:

- `d1=d2=delta=4`: bound about `90`
- `d1=d2=delta=6`: bound `48.00000000000004`
- `d1=d2=delta=8`: bound `48.0000000000000214`

For `d=8`, primal and dual agree to about `2.3e-16`.

Important correction: these equal-degree tests are not the serious regime used for the strongest published second-Lasserre bounds. The high-strength computations use larger mixed degrees (for example `d1=14`, `d2=delta=16` in the D4-type certificate computations). The published dimension-5 second-Lasserre bound is around `44.36`, so the hierarchy is known to descend below the three-point `44.97...` level.

### Mixed-degree jobs launched

Workflow:

`.github/workflows/kissing5d-las2-mixed.yml`

Configurations launched:

- `(d1,d2,delta)=(8,10,10)`
- `(10,10,10)`
- `(10,12,12)`

**Checkpoint status:** all three were actively inside the LAS2 solver. Results should be retrieved from GitHub Actions on the next research session.

---

## 6. Best-known 41-point numerical code: contact structure

Coordinates analyzed from Neil Sloane's public 5D packing table `pack.5.41.txt`.

Numerical quality:

- `N=41`
- maximum pairwise inner product:
  `0.5149946526970505`
- minimum angle:
  `59.00290243419058 degrees`
- centroid norm:
  `0.20948831848882504`

### Limiting contact graph

At tolerance `1e-8` through `5e-3`, the graph is unchanged:

- 153 limiting edges,
- 160 contact triangles,
- connected component sizes: `35,1,1,1,1,1,1`,
- six isolated vertices,
- active 35-point core degree distribution:
  - 18 vertices of degree 8,
  - 10 vertices of degree 9,
  - 6 vertices of degree 10,
  - 1 vertex of degree 12.
- core graph automorphism count found: 12.

The six slack indices are

`[5, 6, 7, 11, 34, 40]`.

Four of them are safely beyond 60 degrees from the core; two (`34` and `40`) are the near-violators:

- max shell-to-core inner product for each: about `0.50125694`,
- corresponding angle: about `59.91680662 degrees`.

---

## 7. New 35+6 decomposition: approximately a 4+2 shell

The six slack points do **not** form a regular 5-simplex.

Their Gram structure is approximately:

- four points with mutual inner products around `-0.290`;
- two points (`34,40`) with inner product
  `-0.999959152686615`,
  i.e. almost exactly antipodal;
- those two are almost orthogonal to the four-point block, with cross inner products around `0`.

So the 41-point near-code behaves approximately as

**35-point active core + four tetrahedral/simplex-like anchors + one near-antipodal pair.**

This is more useful than the raw 41-point coordinates.

The two near-antipodal points are also the only shell points that produce inner products above `1/2` with the core; each has seven core neighbors above `0.5`.

### Promising analytic model

Replace the near-antipodal pair by an exact pair `+e,-e`.

Then every other point `x=(sqrt(1-z^2)u,z)` must satisfy

`|z| <= 1/2`.

The four additional shell anchors impose four further cap inequalities in the orthogonal 4-space. A possible route is to prove that no 35-point core can satisfy all five anchor constraints simultaneously.

This is currently the most geometrically tailored route to killing `N=41`.

---

## 8. Harmonic moment spectra

For any code define

`S_k = sum_{i,j} P_k^(5)(<x_i,x_j>) >= 0`.

A diagnostic workflow computed moments through degree 14 for exact D5 (`N=40`) and Sloane's best-known 41--44 point numerical codes.

### Exact D5, N=40

Selected values:

- `S_1=0`
- `S_2~0`
- `S_3=0`
- `S_4=7.5`
- `S_5=0`
- `S_6=103.984375`
- `S_7=0`
- `S_8=126.064453125`
- `S_9=0`

Odd moments vanish by antipodal symmetry.

### Sloane near-codes

Selected `(S8,S9)` values:

- N=41: `(53.97685447, 23.40692798)`
- N=42: `(40.01929210, 13.41253903)`
- N=43: `(40.83392908, 18.21106568)`
- N=44: `(55.65183440, 8.83987217)`

The lifted LP failure at degrees 8 and 9 identifies the correct harmonic directions for a multi-point certificate, but the raw moment inequality at the crossing is too weak by itself to exclude 42--44.

For a hypothetical N-point 60-degree code, the crossing polynomial gives the necessary condition

`0.147210151*S8 + 0.041038438*S9 >= N(N-N_cross)/N_cross`,

with `N_cross ~= 41.7654428885`.

This is useful as a diagnostic/constraint, not a standalone proof.

---

## 9. Fixed-cardinality Lasserre idea

A stronger route is to stop optimizing the global cardinality bound and impose the cardinality directly.

At a Lasserre level, one may impose cardinality constraints of the form

`lambda(I_=i) = binomial(N,i)`.

Then choose a nonnegative violation potential that is zero for pairwise inner product `<=1/2` and positive above `1/2`.

If the fixed-N relaxation proves strictly positive minimum violation energy for `N=41`, then a 41-point kissing code is impossible.

The thesis supports such fixed-cardinality constraints conceptually. Inspection of the released `LasserreSphericalCodes` package found no obvious high-level energy driver, but the package does expose the relevant cardinality-bound and exact-verification infrastructure in `las2.jl` and `verification.jl`. A custom fixed-N energy formulation may need to be built from the existing SDP components.

**This is a high-priority next direction.**

---

## 10. Files/workflows already saved on `kissing5d-compute`

The branch contains the computational harnesses used in this session, including:

- three-point SDP workflow(s),
- `.github/workflows/kissing5d-las2-mixed.yml`,
- `.github/workflows/kissing5d-analyze-41candidate.yml`,
- `.github/workflows/kissing5d-shell-structure.yml`,
- `.github/workflows/kissing5d-harmonic-moments.yml`,
- `.github/workflows/kissing5d-inspect-energy.yml`.

`main` was intentionally left untouched.

---

## 11. Exact next steps

1. Retrieve the completed mixed-degree LAS2 results for `(8,10,10)`, `(10,10,10)`, `(10,12,12)`.
2. Retrieve degree-11 and degree-14 three-point calibration outputs and confirm agreement with the published benchmarks.
3. Push LAS2 to the first mixed degree where the bound drops below 48, then map the descent toward the published ~44.36 value.
4. Formulate the exact-antipodal-pair + four-anchor model suggested by the 41-point `35+4+2` decomposition.
5. Derive a cap/slab occupancy bound for the 35-point core under those five anchor constraints.
6. In parallel, adapt the released Lasserre code to impose fixed cardinality `N=41` and minimize a violation potential supported on inner products `>1/2`.
7. Use degree-8/9 harmonic moment constraints as side constraints in that fixed-N SDP.
8. If `N=41` is ruled out rigorously, conclude `tau_5=40`; there is no need to separately rule out 42--44 after that.

---

## 12. Current assessment

No proof of `tau_5=40` has been reached yet.

The strongest genuinely new information from this session is structural rather than a numerical upper-bound improvement:

- the one-variable lift has been extended and its exact failure mechanism identified;
- the public three- and four-point SDP machinery is operational;
- the best-known 41-point near-code has a stable 35-point active core and a highly structured six-point shell;
- that shell splits approximately into a four-point simplex-like block and an almost exact antipodal pair;
- this suggests a much lower-dimensional constrained-core model for attacking the `N=41` case directly.

That constrained 35-point core is the most promising analytic target currently identified.
