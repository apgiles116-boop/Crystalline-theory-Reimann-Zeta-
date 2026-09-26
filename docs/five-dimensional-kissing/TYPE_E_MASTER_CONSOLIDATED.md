# Five-dimensional kissing number — Type E master consolidated state

**Authoritative working state.** This file consolidates the recent ChatGPT Type-E research threads into one current continuation point. Older dated checkpoint files remain as historical snapshots and should not override this file.

**Last consolidated:** 2026-09-25

---

# Five-dimensional kissing number — Type E checkpoint

**Date:** 2026-09-25  
**Repository:** \`apgiles116-boop/Crystalline-theory-Reimann-Zeta-\`  
**Proof-status discipline:** every substantive statement below is labelled **PROVED / EXACT**, **CONDITIONAL**, **NUMERICAL**, **OPEN**, or **CORRECTION**.

## 1. Global status

### PROVED / EXACT

The current global bound remains

\[
\boxed{40\le \tau_5\le44}.
\]

For a hypothetical 41-point kissing configuration, the deep graph \(G\) is triangle-free and satisfies

\[
\alpha(G)\le20,\qquad e(G)\ge23.
\]

For an isolated center \(x_0\), with \(H=G-x_0\),

\[
|V(H)|=40,\qquad \alpha(H)\le19,\qquad e(H)\ge25.
\]

The exact \(e=25\) and \(e=26\) types A and B are eliminated.

### CONDITIONAL

The sparse \(e=23,e=24\) classification still depends on proving

\[
\delta(G)\ge1.
\]

### OPEN

Types C, D, E and the generic \(e\ge27\) branch remain open.

---

## 2. Type E mass state

Type E is

\[
H=16K_2\sqcup F_3.
\]

### PROVED / EXACT

Current exact Type-E bounds are

\[
\text{star theorem:}\qquad \sum_{\text{star}}\le\frac{70}{3},
\]

\[
M(F_3)\le89,
\]

and among the three perfect matchings of \(F_3\), some matching \(P\) satisfies

\[
M(P)\ge \frac S2-\frac{28}{3}.
\]

The twenty distinguished disjoint deep edges have total mass

\[
\ge\frac{2137}{6}.
\]

Writing

\[
x_i^\pm=m_i\pm z_i,\qquad m_i\perp z_i,
\]

\[
a_i=\|m_i\|^2,\qquad A=\sum_{i=1}^{20}a_i,
\]

one has

\[
\boxed{A\le A_*:=\frac{383}{504}}.
\]

For each distinguished deep edge,

\[
0\le a_i\le\frac14.
\]

### CORRECTION

Do not regress to the obsolete bounds

\[
M(F_3)\le94,\qquad M(P)\ge S/2-343/32.
\]

---

## 3. Zero-midpoint boundary

### PROVED / EXACT

Musin, *Proc. Steklov Inst. Math.* 263 (2008), Sec. 5, states that for antipodal spherical codes in dimension \(5\), the SDP0 bound \(42\) is improved using integrality of the distance distribution to

\[
c\le40,
\]

citing Boyvalenkov, “Nonexistence of certain symmetric spherical codes,” *Designs Codes Cryptogr.* 3 (1993), 69–74.

Therefore at most 20 projective lines in \(\mathbb{RP}^4\) can have coherence at most \(1/2\). Hence the 21-line zero-midpoint boundary is rigorously excluded independently of any uniqueness/optimality claim for the \(D_5\) 20-line packing.

---

## 4. Exact global Q/frame identity

Define

\[
Q_i=z_i z_i^T-\frac{\|z_i\|^2}{5}I,
\]

and

\[
F_z=\sum_i z_i z_i^T,\qquad
V:=\left\|F_z-\frac{20-A}{5}I\right\|_F^2
=\left\|\sum_iQ_i\right\|_F^2\ge0.
\]

Let

\[
B:=\sum_i a_i^2,\qquad
S_z:=\sum_{i<j}(z_i\cdot z_j)^2.
\]

### PROVED / EXACT

The exact identity is

\[
\boxed{
S_z=
30-3A+\frac{A^2}{10}-\frac12B+\frac12V.
}
\]

Thus the universal inequality is obtained by dropping \(V/2\).

Under

\[
0\le a_i\le\frac14,\qquad \sum_i a_i=A,
\]

the maximum possible \(B\) is obtained by concentration. At

\[
A=A_*=\frac{383}{504}
=\frac34+\frac5{504},
\]

the extremal pattern is

\[
\left(\frac14,\frac14,\frac14,\frac5{504},0^{16}\right)
\]

up to permutation, giving

\[
B_{\max}
=
\frac3{16}
+\left(\frac5{504}\right)^2.
\]

Therefore

\[
\boxed{
S_z\ge
\frac{8790283}{317520}
\approx27.6841868228773.
}
\]

This is the strongest current universal Type-E \(Q\)-floor.

### CORRECTION

The weaker cap-only estimate \(\sum_i a_i^2\le A/4\) gives only \(S_z\ge27.682995953\ldots\). It is valid but is not the strongest current bound and must not replace the exact concentration floor above.

---

## 5. Exact second-order midpoint concentration stability

For

\[
\frac34\le A\le A_*,
\]

the exact concentrated maximum is

\[
B_{\max}(A)
=
\frac3{16}
+\left(A-\frac34\right)^2.
\]

Define the concentration deficit

\[
\Delta:=B_{\max}(A)-B\ge0.
\]

### PROVED / EXACT

Then

\[
\boxed{
S_z
\ge
\frac{9483}{320}
-\frac94A
-\frac25A^2
+\frac12\Delta+\frac12V.
}
\]

Writing

\[
t=A_*-A,
\]

this becomes

\[
\boxed{
S_z
\ge
\frac{8790283}{317520}
+\frac{3601}{1260}t
-\frac25t^2
+\frac12\Delta+\frac12V.
}
\]

Thus moving below the terminal midpoint-energy bound forces a first-order increase in the projective squared-correlation floor, while midpoint deconcentration and frame anisotropy add the nonnegative penalties \(\Delta/2\) and \(V/2\).

---

## 6. Six-exception localization

Among the 190 distinguished-edge pairings, only six core pairings can violate

\[
|z_i\cdot z_j|\le\frac12.
\]

For an exceptional pair write

\[
|g_e|=\frac12+d_e,\qquad d_e>0.
\]

### PROVED / EXACT

The current raw-defect bound is

\[
D:=\sum_e d_e
\le
D_0:=
\frac{1780062775}{4032758016}
<0.441401.
\]

The homogeneous positive-defect bound is

\[
D_{\rm hom}
\le
\frac{5792292955405}{4129544208384}
\approx1.402647038781.
\]

Using \(|E|\le6\),

\[
\sum_{e\in E}g_e^2
=
\frac{|E|}{4}+D+\sum_e d_e^2
\le
\frac32+D_0+D_0^2
<2.136235542.
\]

Combining this with the strongest \(Q\)-floor gives

\[
\boxed{
S_{\rm safe}
>
25.54795128168835.
}
\]

Hence there are at least 103 nonorthogonal safe pairings. The safe graph lies three edges above Mantel's 100-edge threshold, and the previously established Lovasz-Simonovits consequence remains

\[
T_{\rm safe}\ge30.
\]

---

## 7. Endpoint diamond and threshold ledger

For one pair define

\[
p=m_i\cdot m_j,\qquad
g=z_i\cdot z_j,
\]

\[
r=m_i\cdot z_j,\qquad
s=z_i\cdot m_j.
\]

Orient so \(g\ge0\), and put

\[
h=r+s,\qquad k=r-s.
\]

### PROVED / EXACT

The four endpoint constraints imply

\[
p+g+|h|\le\frac12.
\]

Hence, with

\[
\delta_{ij}:=\frac14-g_{ij}^2,
\]

one has

\[
\boxed{
\delta_{ij}
\ge
p_{ij}-p_{ij}^2+h_{ij}^2.
}
\]

For an exceptional pair \(g=1/2+d\),

\[
\boxed{
-p\ge d+|h|.
}
\]

Thus raw exceptional defect and charged mixed energy must both be financed by negative midpoint correlation.

---

## 8. Midpoint determinant budget

Let

\[
F_m=\sum_i m_i m_i^T,
\]

and for each pair define

\[
D_{m,ij}:=a_i a_j-p_{ij}^2.
\]

### PROVED / EXACT

Summing over all pairs,

\[
\boxed{
\sum_{i<j}D_{m,ij}
=
\frac{A^2-\|F_m\|_F^2}{2}.
}
\]

Since \(F_m\succeq0\) is \(5\times5\) with trace \(A\),

\[
\|F_m\|_F^2\ge\frac{A^2}{5},
\]

so

\[
\boxed{
\sum_{i<j}D_{m,ij}
\le
\frac{2A^2}{5}
\le
\frac{146689}{635040}
\approx0.230991748551.
}
\]

---

## 9. Full four-vector Gram determinant

For a pair let

\[
a=a_i,\qquad b=a_j,\qquad
D_m=ab-p^2,
\]

\[
D_z=(1-a)(1-b)-g^2,
\qquad
L=a+b-2ab.
\]

The local Gram matrix on \((m_i,z_i,m_j,z_j)\) is

\[
\mathcal G_{ij}
=
\begin{pmatrix}
a&0&p&r\\
0&1-a&s&g\\
p&s&b&0\\
r&g&0&1-b
\end{pmatrix}\succeq0.
\]

### PROVED / EXACT

In charged/uncharged coordinates

\[
h=r+s,\qquad k=r-s,
\]

its determinant is exactly

\[
\boxed{
\det\mathcal G_{ij}
=
D_mD_z
+\frac{(h^2-k^2)^2}{16}
-\frac14\mathcal Q(h,k),
}
\]

where

\[
\boxed{
\mathcal Q(h,k)
=
(L+2pg)h^2
+
(L-2pg)k^2
-
2(a-b)hk.
}
\]

The coefficient matrix of \(\mathcal Q\) is positive semidefinite. Its determinant is

\[
\boxed{
4\left[
ab(1-a)(1-b)-p^2g^2
\right]\ge0.
}
\]

Define its smaller eigenvalue

\[
\boxed{
\lambda_-
=
L-\sqrt{(a-b)^2+4p^2g^2}.
}
\]

Then

\[
\boxed{\lambda_-\ge0}
\]

and Gram positivity implies

\[
\boxed{
\lambda_-(h^2+k^2)
\le
4D_mD_z+\frac{(h^2-k^2)^2}{4}.
}
\]

Away from zero-energy boundary cases, \(\lambda_-=0\) requires simultaneous Cauchy saturation

\[
p^2=ab,\qquad
g^2=(1-a)(1-b).
\]

---

## 10. Safe-pair spectral envelope

### PROVED / EXACT

For a safe pair,

\[
|g|\le\frac12,
\]

so

\[
p^2g^2\le\frac14ab.
\]

Since

\[
\lambda_+\lambda_-
=
4\left[ab(1-a)(1-b)-p^2g^2\right]
\]

and

\[
\lambda_+\le2(a+b-2ab),
\]

one obtains

\[
\boxed{
\lambda_-
\ge
\frac{
2ab\left((1-a)(1-b)-1/4\right)
}{
a+b-2ab
}
}
\]

whenever the denominator is positive.

For equal midpoint energies \(a=b=q\le1/8\), the exact safe envelope sharpens to

\[
\boxed{\lambda_-\ge q(1-2q)}.
\]

For an arbitrary pair in the same equal-energy range,

\[
\boxed{\lambda_-\ge q(1-4q)}.
\]

The bad branch is driven toward

\[
p=-q,\qquad g=\frac12+q,
\]

so spectral degeneration in the small-energy regime migrates toward the exceptional-pair budget.

---

## 11. Seventeen-index controlled core

Choose any threshold

\[
t>\frac{A_*}{4}
=
\frac{383}{2016}
\approx0.189980159.
\]

Then at most three midpoint energies can satisfy \(a_i\ge t\), hence at least 17 indices satisfy \(a_i<t\).

There are at most

\[
3\cdot17+\binom32=54
\]

pairs touching the at-most-three outside indices.

### PROVED / EXACT

Since every safe pair contributes at most \(1/4\),

\[
\boxed{
S_{\rm core,safe}
>
25.54795128168835-\frac{54}{4}
=
12.04795128168835.
}
\]

The 17-index core contains 136 pairs, at most six of which can be exceptional, so at least

\[
\boxed{130}
\]

core pairs are safe.

Moreover at least 19 safe core pairs satisfy

\[
\boxed{|z_i\cdot z_j|>\frac14}.
\]

For the convenient rational choice

\[
t=\frac{191}{1000},
\]

every safe core pair obeys

\[
\boxed{
\lambda_-
>
0.808962\,
\frac{ab}{a+b-2ab}.
}
\]

No \(D_5\) labeling is used in this core localization.

---

## 12. Complete-hiding determinant slice

### PROVED / EXACT

If the charged channel vanishes,

\[
h=0,
\]

then \(s=-r\). Writing \(x=r^2\),

\[
\boxed{
\det\mathcal G_{ij}
=
x^2-Kx+D_mD_z,
}
\]

where

\[
K=a(1-b)+b(1-a)-2pg.
\]

On the connected PSD branch containing \(x=0\),

\[
\boxed{
x\le
\frac{K-\sqrt{K^2-4D_mD_z}}{2}
}
\]

whenever the displayed discriminant is nonnegative.

Thus perfectly hidden mixed energy consumes both midpoint and projected determinant deficits.

---

## 13. HHL theorem retained from 2026-09-22

For the HHL midpoint pattern

\[
a_1=a_2=\frac14,\qquad a_3=t,\qquad 0<t\le\frac5{504},
\]

the 2026-09-22 checkpoint proved the following under the single additional hypothesis that one safe projective correlation saturates.

### PROVED / EXACT under one-saturation hypothesis

If, after orientation,

\[
z_1\cdot z_2=\frac12,
\]

then the rank-five determinant reduction yields

\[
\boxed{
D=d_1+d_2
\ge
s(t):=
\frac{t+\sqrt{3t(5-8t)}}{10}.
}
\]

The local squared-correlation loss satisfies

\[
\boxed{
L\ge s(t)(1-s(t)).
}
\]

Equality forces \(d_1d_2=0\), so a second safe correlation saturates at equality.

At

\[
t=\frac5{504},
\]

\[
s=
\frac1{1008}+\frac{\sqrt{93}}{252},
\]

and

\[
L=
-\frac{481}{1016064}
+\frac{503\sqrt{93}}{127008}
\approx0.037719130549095.
\]

### OPEN

The remaining local HHL theorem is to prove that a global HHL maximizer must possess at least one saturated safe correlation.

---

## 14. D5/Q structure

### PROVED / EXACT structural data

For the exact \(D_5\) 20-line template

\[
z_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2,
\]

the \(Q\)-Gram matrix has rank 14 and nullity 6. The kernel decomposes into one global tight-frame relation and five local support-sum cycle relations.

### CAUTION

The numerical coincidence between this six-dimensional kernel and the six exceptional projective pairings is only a clue. No one-to-one identification has been proved.

The Cohn–Jiao–Kumar–Torquato infinitesimal rigidity of \(D_5\) remains a candidate source of second-order control, but no quantitative perturbative theorem has yet been imported into the Type-E proof.

---

## 15. Current proof-status ledger

### PROVED / EXACT

- \(40\le\tau_5\le44\).
- Type-E star/broom/matching bounds listed above.
- \(A\le383/504\) and \(0\le a_i\le1/4\).
- rigorous 21-line zero-midpoint exclusion.
- exact global \(Q\)/frame identity.
- strongest universal Type-E \(Q\)-floor:
  \[
  S_z\ge8790283/317520\approx27.6841868228773.
  \]
- exact second-order concentration/frame-variance refinement.
- at most six exceptional projective pairings.
- safe squared-correlation mass:
  \[
  S_{\rm safe}>25.54795128168835.
  \]
- midpoint determinant budget:
  \[
  \sum D_m\le146689/635040<0.231.
  \]
- full \(4\times4\) Gram determinant identity in \((h,k)\).
- safe-pair spectral envelope.
- 17-index controlled core with
  \[
  S_{\rm core,safe}>12.04795128168835.
  \]
- at least 130 safe pairs in that core.
- at least 19 core-safe pairs with \(|g|>1/4\).
- HHL one-saturation theorem from the 2026-09-22 checkpoint.

### CONDITIONAL

- full HHL envelope still requires proving existence of the first saturated safe correlation at a global HHL maximizer.

### NUMERICAL

- deterministic endpoint-model reconnaissance from the 2026-09-22 checkpoint remains useful evidence for the active HLL/HHL faces, but is not used as proof.

### OPEN

- Type E elimination.
- proof that a global HHL optimizer has one safe saturation.
- conversion of the 17-core \(Q\)-mass plus the \(<0.231\) midpoint determinant budget into a global mixed-channel contradiction.
- justification of a \(D_5\)-type labeling/contact structure sufficient to use the five local \(Q\)-cycle kernel relations.
- Type C exhaustive/boundary proof.
- Type D.
- generic \(e\ge27\).
- proof of \(\delta(G)\ge1\) for unconditional sparse \(e=23,24\) classification.

---

## 16. Highest-value next exact target

The most promising scalar route is now:

1. keep the exact second-order global ledger
   \[
   S_z
   \ge
   \frac{8790283}{317520}
   +\frac{3601}{1260}(A_*-A)
   -\frac25(A_*-A)^2
   +\frac12\Delta+\frac12V;
   \]

2. use the six-exception theorem to keep more than \(12.04795\) units of safe squared-correlation mass inside a 17-index low-midpoint core;

3. combine the safe-pair spectral lower envelope with the tiny global midpoint determinant budget
   \[
   \sum D_m<0.231;
   \]

4. control the remaining uncharged mixed channel via the exact \(4\times4\) determinant identity;

5. if the scalar route stalls, return to the five local \(D_5\) \(Q\)-kernel cycle relations, but only after a \(D_5\)-type contact labeling is justified.

The target is a quantitative second-order contradiction forcing

\[
A>\frac{383}{504},
\]

which would eliminate Type E.

No such contradiction is claimed yet.


---

## 17. 2026-09-25 continuation: sharpened exception energy and 17-line subframe theorem

This section **supersedes the weaker safe-mass/localization constants in §§6 and 11**. Those earlier inequalities remain valid but are no longer the strongest current values.

Let

\[
A_*=\frac{383}{504},
\qquad
D_0=\frac{1780062775}{4032758016}.
\]

### PROVED / EXACT — improved global exceptional squared-mass cap

For every exceptional pair,

\[
|g_e|=\frac12+d_e,\qquad
0<d_e\le\sqrt{a_i a_j}\le\frac14.
\]

Since

\[
\sum_e d_e\le D_0,
\qquad
\frac14<D_0<\frac12,
\]

convexity of \(x^2\) gives

\[
\boxed{
\sum_e d_e^2
\le
\frac1{16}
+
\left(D_0-\frac14\right)^2.
}
\]

Therefore, using at most six exceptional pairings,

\[
\boxed{
\sum_{e\in E}g_e^2
\le
\frac32+D_0+\frac1{16}
+\left(D_0-\frac14\right)^2
=
D_0^2+\frac{D_0}{2}+\frac{13}{8}.
}
\]

Numerically,

\[
\boxed{
\sum_{e\in E}g_e^2
\le
2.040535121285547.
}
\]

Combining with the strongest universal \(Q\)-floor,

\[
S_z\ge
\frac{8790283}{317520}
\approx27.6841868228773,
\]

gives the improved global safe mass

\[
\boxed{
S_{\rm safe}\ge25.643651701591754.
}
\]

This replaces the previous weaker \(25.54795128168835\) value.

Consequently

\[
S_{\rm safe}-25
\ge
0.643651701591754.
\]

The lower bound of 103 nonorthogonal safe pairings is unchanged, but its weighted excess above the triangle-free \(25\)-capacity is substantially larger.

### PROVED / EXACT — existence of a 17-index low-midpoint block

Put

\[
t_0:=\frac{A_*}{4}
=
\frac{383}{2016}.
\]

Since four indices with \(a_i>t_0\) would have total midpoint energy exceeding \(A_*\), there exists a set \(L\) of 17 indices satisfying

\[
\boxed{
a_i\le t_0
\qquad(i\in L).
}
\]

Write

\[
A_L=\sum_{i\in L}a_i,
\qquad
B_L=\sum_{i\in L}a_i^2,
\]

\[
F_L=\sum_{i\in L} z_i z_i^T,
\qquad
V_L=
\left\|
F_L-\frac{17-A_L}{5}I
\right\|_F^2,
\]

and

\[
S_L=
\sum_{\{i,j\}\subset L}(z_i\cdot z_j)^2.
\]

The rank-five frame identity gives exactly

\[
\boxed{
S_L
=
\frac{102}{5}
-\frac{12}{5}A_L
+\frac{A_L^2}{10}
-\frac12B_L
+\frac12V_L.
}
\]

Since \(a_i\le t_0\),

\[
B_L\le t_0A_L.
\]

The resulting scalar lower envelope is decreasing on \(0\le A_L\le A_*\), so

\[
\boxed{
S_L
\ge
\frac{37719859}{2032128}
\approx18.56175349190602.
}
\]

### PROVED / EXACT — second-order stability inside the 17-index block

Define

\[
R_L:=t_0A_L-B_L
=
\sum_{i\in L}a_i(t_0-a_i)\ge0,
\]

and

\[
u:=A_*-A_L\ge0.
\]

Then the preceding identity refines exactly to

\[
\boxed{
S_L
=
\frac{37719859}{2032128}
+
\frac{3149}{1344}u
+
\frac{u^2}{10}
+
\frac12R_L
+
\frac12V_L.
}
\]

Thus the 17-line projected frame pays a quantitative penalty whenever:

- midpoint energy escapes from the block (\(u>0\));
- midpoint energies fail to concentrate at the cap \(t_0\) (\(R_L>0\));
- the projected frame fails to be tight (\(V_L>0\)).

### PROVED / EXACT — exceptional mass inside the 17-index block

For an exceptional pair entirely inside \(L\),

\[
d_e\le\sqrt{a_i a_j}\le t_0.
\]

Moreover

\[
2t_0<D_0<3t_0.
\]

Hence convexity gives

\[
\boxed{
\sum_{e\subset L}d_e^2
\le
2t_0^2+(D_0-2t_0)^2.
}
\]

Therefore the total exceptional squared-correlation mass inside \(L\) is at most

\[
\boxed{
E_L
\le
\frac32+D_0
+2t_0^2+(D_0-2t_0)^2
\approx2.017360699015280.
}
\]

Subtracting from the 17-line frame floor yields

\[
\boxed{
S_{L,\rm safe}
\ge
16.54439279289074.
}
\]

This is the strongest current localization of safe projective squared-correlation mass.

### PROVED / EXACT — combinatorial consequences inside \(L\)

Because every safe pair contributes at most \(1/4\),

\[
\boxed{
\text{at least 67 safe pairings in }L
\text{ are nonorthogonal}.
}
\]

If \(N_{1/16}\) denotes the number of safe \(L\)-pairs with

\[
g_{ij}^2>\frac1{16},
\]

then

\[
S_{L,\rm safe}
\le
\frac{N_{1/16}}4
+
\frac{136-N_{1/16}}{16},
\]

so

\[
\boxed{
N_{1/16}\ge43.
}
\]

Equivalently, at least 43 safe pairs in \(L\) satisfy

\[
\boxed{
|z_i\cdot z_j|>\frac14.
}
\]

Likewise, at least 20 safe pairs in \(L\) satisfy

\[
\boxed{
(z_i\cdot z_j)^2>\frac1{10},
\qquad
|z_i\cdot z_j|>\frac1{\sqrt{10}}.
}
\]

The graph of the 43 pairs with \(|g|>1/4\) has 17 vertices and 43 edges, so some vertex has degree at least 6 in this strong-correlation graph.

Also,

\[
\frac{2S_{L,\rm safe}}{17}
\ge
1.946399152104793,
\]

so some index \(i\in L\) has safe incident squared-correlation mass at least

\[
\boxed{
\sum_{\substack{j\in L\\ ij\ {\rm safe}}}
(z_i\cdot z_j)^2
\ge1.946399152104793.
}
\]

### CURRENT DIAGNOSIS

The 17-index low-midpoint sector is substantially more constrained than the earlier \(12.04795\)-mass estimate suggested:

\[
\boxed{
S_{L,\rm safe}\ge16.54439279289074.
}
\]

However, 67 guaranteed nonorthogonal safe edges are still below the Mantel threshold

\[
\left\lfloor\frac{17^2}{4}\right\rfloor=72,
\]

so the subframe theorem alone does **not** yet force a safe triangle inside \(L\).

The next exact target is therefore local: exploit the guaranteed strong star (at least six safe neighbors with \(|g|>1/4\) for some vertex) together with the endpoint diamond and the \(4\times4\) spectral determinant to force either:

1. additional midpoint determinant expenditure beyond the global \(<0.231\) budget; or
2. a rigid \(D_5\)-type local contact pattern to which the \(Q\)-kernel cycle relations can be applied.

No Type-E elimination is claimed yet.
