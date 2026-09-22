# Five-dimensional kissing number — Type E checkpoint

**Date:** 2026-09-22  
**Proof-status discipline:** every substantive statement below is labelled **PROVED**, **CONDITIONAL**, **NUMERICAL**, or **OPEN**.  
**Global proved range:**

\[
\boxed{40\le \tau_5\le 44}.
\]

## 1. Global graph state

### PROVED
For a hypothetical 41-point kissing configuration, the deep graph \(G\) is triangle-free and satisfies

\[
\alpha(G)\le 20,\qquad e(G)\ge 23.
\]

For an isolated center \(x_0\), with \(H=G-x_0\),

\[
|V(H)|=40,\qquad \alpha(H)\le19,\qquad e(H)\ge25.
\]

The exact \(e=25\) and \(e=26\) types A and B are eliminated.

### CONDITIONAL
The sparse \(e=23\), \(e=24\) classification still depends on proving \(\delta(G)\ge1\).

### OPEN
Types C, D, E and the generic \(e\ge27\) branch remain open.

## 2. Type E mass and midpoint state

Type E is

\[
H=16K_2\sqcup F_3.
\]

### PROVED
Current exact bounds:

- star theorem: local star mass \(\le70/3\);
- broom theorem:
  \[
  M(F_3)\le89;
  \]
- among the three perfect matchings of \(F_3\), some \(P\) satisfies
  \[
  M(P)\ge S/2-28/3;
  \]
- the twenty distinguished disjoint deep edges have total mass
  \[
  \ge2137/6;
  \]
- if \(a_i=\|m_i\|^2\) and \(A=\sum_i a_i\), then
  \[
  \boxed{A\le383/504}.
  \]

Do not regress to the obsolete \(M(F_3)\le94\) or \(S/2-343/32\) matching bounds.

## 3. Zero-midpoint boundary

### PROVED
Musin (Proc. Steklov Inst. Math. 263 (2008), Sec. 5) states that for antipodal spherical codes in dimension 5 the SDP0 bound 42 is improved, using integrality of the distance distribution and Boyvalenkov (1993), to \(c\le40\).

Therefore at most 20 projective lines in \(\mathbb{RP}^4\) can have coherence \(\le1/2\). Hence the 21-line zero-midpoint boundary is rigorously excluded without assuming optimality of the \((5,20)\) \(D_5\) packing.

## 4. Universal Q-floor

Write

\[
Q_i=z_i z_i^T-\frac{\|z_i\|^2}{5}I.
\]

### PROVED
Using PSD of \(\|\sum_iQ_i\|^2\),

\[
R:=\sum_{i<j}(z_i\cdot z_j)^2
\ge
30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2.
\]

Using the box constraint \(0\le a_i\le1/4\) and \(A\le383/504\) gives the strengthened global floor

\[
\boxed{
R\ge\frac{8790283}{317520}
\approx27.6841868228773.
}
\]

Combined with the six-exception raw-defect bound

\[
D\le
\frac{1780062775}{4032758016},
\]

this gives

\[
R_{\rm safe}\ge25.54795128168835\ldots
\]

and therefore at least 103 nonorthogonal safe pairings.

### PROVED
Consequences:

\[
m_{\rm safe}\ge103.
\]

Hence the safe graph lies three edges above Mantel's 100-edge threshold, so its triangle edge-transversal number is at least 3.

Using the Lovasz-Simonovits supersaturation theorem at \(n=20,q=3\),

\[
T_{\rm safe}\ge30.
\]

The excess over triangle-free safe squared-correlation capacity is

\[
\boxed{
\Delta_{\rm safe}
=
R_{\rm safe}-25
\ge0.54795128168835\ldots
}
\]

and after deleting two arbitrary safe pairings, the residual excess is

\[
\boxed{
\varepsilon
=
\Delta_{\rm safe}-\frac12
\ge0.04795128168835\ldots
}
\]

This is the local-loss threshold for the two-worst-pair deletion strategy.

## 5. Raw triangle relaxation is insufficient

### PROVED ABOUT THE RELAXATION
The raw three-vector \(z\)-Gram problem with only

\[
|z_i\cdot z_j|\le1/2
\]

has no positive local loss: the objective

\[
F=x^2+y^2+z^2
\]

can remain at \(3/4\) throughout the midpoint cube. Thus midpoint energy alone does not create a gap unless the original two-sided endpoint constraints are retained.

This route is closed as a proof mechanism.

## 6. Full two-sided endpoint triangle model

For three distinguished deep edges, write endpoints

\[
P_i=m_i+z_i,\qquad N_i=m_i-z_i,
\]

with

\[
\|P_i\|=\|N_i\|=1,
\qquad
P_i\cdot N_i=2a_i-1.
\]

For a fully safe nonedge pairing impose all four two-sided constraints

\[
-\frac12
\le
(P_i^{\sigma})\cdot(P_j^{\tau})
\le
\frac12,
\qquad
\sigma,\tau\in\{+,-\}.
\]

### PROVED local saturation lemma
For one safe pair put

\[
u=m_i\cdot m_j,\quad
p=m_i\cdot z_j,\quad
q=z_i\cdot m_j,\quad
r=z_i\cdot z_j.
\]

If \(|r|=1/2\), then the four two-sided endpoint inequalities force

\[
\boxed{u=p=q=0}.
\]

This gives the rank-five obstruction behind the local loss when three midpoint energies are positive.

## 7. Deterministic numerical reconnaissance

A deterministic JuMP/Ipopt scan with warm continuation and independent feasibility auditing was run on the full two-sided endpoint model.

### NUMERICAL
All accepted solutions had maximum independent feasibility residual approximately \(5\times10^{-11}\) to \(8\times10^{-11}\).

Representative losses:

\[
\begin{array}{c|c}
(a_1,a_2,a_3) & L=3/4-F_{\max}\\
\hline
(.05,.05,.05) & 0.047500000\ldots\\
(.10,.10,.10) & 0.0814173009\ldots\\
(.25,.25,.25) & 0.1443749998\ldots\\
(.25,.25,5/504) & 0.03771913037\ldots\\
(.25,.05,.05) & 0.047500000\ldots
\end{array}
\]

## 8. Low-energy HLL/symmetric active face

### CONDITIONAL EXACT
On the active face found by the deterministic solver, two safe correlations saturate at \(1/2\), while for the third pair

\[
u=-t,\qquad p=q=0,\qquad r=\frac12-t.
\]

Therefore

\[
F(t)=\frac12+\left(\frac12-t\right)^2
=
\frac34-t+t^2,
\]

so the local loss is

\[
\boxed{L(t)=t(1-t)}.
\]

At \(t=.05\),

\[
L=.0475,
\]

which misses the global residual threshold \(\varepsilon\) by only

\[
0.00045128168835\ldots
\]

### OPEN
It remains to prove that this observed active face is globally optimal over the full rank-five six-endpoint feasible region on the relevant parameter interval.

## 9. HHL rank-five branch

Take

\[
a_1=a_2=\frac14,\qquad a_3=t.
\]

The deterministic scan shows an HHL branch with two saturated safe correlations and one nonsaturated pair.

For the nonsaturated pair define

\[
s=u=-p=q=\frac12-r.
\]

At the terminal Type-E scale \(t=5/504\), the solver gives

\[
s\approx0.039260518892,
\qquad
r\approx0.460739481182.
\]

The six-vector Gram matrix has one eigenvalue zero to numerical precision and five positive eigenvalues, confirming a rank-five boundary face.

### CONDITIONAL EXACT
On the observed active set, rank five reduces to

\[
\boxed{
20s^2-4st+5t^2-3t=0.
}
\]

The positive branch is

\[
\boxed{
s(t)=\frac{t+\sqrt{3t(5-8t)}}{10}.
}
\]

At

\[
t=\frac5{504},
\]

this simplifies to

\[
\boxed{
s=
\frac1{1008}+\frac{\sqrt{93}}{252}.
}
\]

The corresponding local loss is

\[
L=s-s^2
=
\boxed{
-\frac{481}{1016064}
+
\frac{503\sqrt{93}}{127008}
}
\]

with numerical value

\[
L\approx0.037719130549095.
\]

The deterministic Ipopt value was \(0.037719130372903\), agreeing within solver tolerance.

The remaining gap to the global residual threshold is approximately

\[
\boxed{0.01023215114}.
\]

### OPEN
The key missing theorem is global optimality of this HHL active branch. Once proved, the remaining Type-E task is to recover the missing \(\sim0.01023215\) loss from either:

1. a second forced safe triangle after deleting the two worst safe pairings;
2. a non-scalar \(Q\)-kernel relation;
3. a quantitative frame/rigidity coupling between overlapping triangles.

## 10. D5/Q direction

### PROVED structural data
For the exact \(D_5\) 20-line template

\[
z_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2,
\]

the \(Q\)-Gram matrix has rank 14 and nullity 6, decomposing into one global tight-frame relation plus five support-sum cycle relations.

### CAUTION
The numerical coincidence between the six-dimensional kernel and the six exceptional pairings is only a clue. No one-to-one identification theorem has been proved.

## 11. Current proof-status ledger

### PROVED
- \(40\le\tau_5\le44\).
- Type-E exact mass bounds listed above.
- \(A\le383/504\).
- rigorous zero-midpoint 21-line exclusion.
- strengthened universal \(Q\)-floor.
- at least 103 safe nonorthogonal pairings.
- at least 30 safe triangles.
- triangle edge-transversal at least 3.
- two-sided endpoint saturation lemma.

### CONDITIONAL EXACT
- low-energy HLL/symmetric face: \(L=t(1-t)\).
- HHL active face:
  \[
  20s^2-4st+5t^2-3t=0.
  \]

### NUMERICAL
- deterministic full-endpoint branch reconnaissance with residuals below \(10^{-10}\).

### OPEN
- global optimality of the HLL and HHL active faces;
- conversion of the remaining HHL deficit into a contradiction;
- Type C, Type D, Type E and generic \(e\ge27\);
- proof of \(\delta(G)\ge1\) needed for unconditional sparse \(e=23,24\) classification.

## 12. Next exact target

The highest-value next step is to write the HHL active-set Gram matrix explicitly, prove that every feasible optimizer can be reduced to this face, and use principal minors plus the rank-five determinant condition to establish the exact envelope

\[
s(t)=\frac{t+\sqrt{3t(5-8t)}}{10}.
\]

Only after that proof should the argument spend effort on the remaining \(0.01023215114\ldots\) global deficit.
