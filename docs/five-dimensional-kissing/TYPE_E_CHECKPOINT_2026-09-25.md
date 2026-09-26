# Five-dimensional kissing number — Type E checkpoint

**Date:** 2026-09-25  
**Repository:** `apgiles116-boop/Crystalline-theory-Reimann-Zeta-`  
**Proof-status discipline:** every substantive statement below is labelled **PROVED / EXACT**, **CONDITIONAL**, **NUMERICAL**, **OPEN**, or **CORRECTION**.

## 1. Global status

### PROVED / EXACT

The current global bound remains

[
oxed{40le 	au_5le44}.
]

For a hypothetical 41-point kissing configuration, the deep graph (G) is triangle-free and satisfies

[
alpha(G)le20,qquad e(G)ge23.
]

For an isolated center (x_0), with (H=G-x_0),

[
|V(H)|=40,qquad alpha(H)le19,qquad e(H)ge25.
]

The exact (e=25) and (e=26) types A and B are eliminated.

### CONDITIONAL

The sparse (e=23,e=24) classification still depends on proving

[
delta(G)ge1.
]

### OPEN

Types C, D, E and the generic (ege27) branch remain open.

---

## 2. Type E mass state

Type E is

[
H=16K_2sqcup F_3.
]

### PROVED / EXACT

Current exact Type-E bounds are:

[
	ext{star theorem:}qquad sum_{	ext{star}}lerac{70}{3},
]

[
M(F_3)le89,
]

and among the three perfect matchings of (F_3), some matching (P) satisfies

[
M(P)ge rac S2-rac{28}{3}.
]

The twenty distinguished disjoint deep edges have total mass

[
gerac{2137}{6}.
]

Writing

[
x_i^pm=m_ipm z_i,qquad m_iperp z_i,
]

[
a_i=|m_i|^2,qquad A=sum_{i=1}^{20}a_i,
]

one has

[
oxed{Ale A_*:=rac{383}{504}}.
]

For each distinguished deep edge,

[
0le a_ilerac14.
]

### CORRECTION

Do not regress to the obsolete bounds

[
M(F_3)le94,qquad M(P)ge S/2-343/32.
]

---

## 3. Zero-midpoint boundary

### PROVED / EXACT

Musin, *Proc. Steklov Inst. Math.* 263 (2008), Sec. 5, states that for antipodal spherical codes in dimension (5), the SDP0 bound (42) is improved using integrality of the distance distribution to

[
cle40,
]

citing Boyvalenkov, “Nonexistence of certain symmetric spherical codes,” *Designs Codes Cryptogr.* 3 (1993), 69–74.

Therefore at most 20 projective lines in (mathbb{RP}^4) can have coherence at most (1/2). Hence the 21-line zero-midpoint boundary is rigorously excluded independently of any uniqueness/optimality claim for the (D_5) 20-line packing.

---

## 4. Exact global Q/frame identity

Define

[
Q_i=z_i z_i^T-rac{|z_i|^2}{5}I,
]

and

[
F_z=sum_i z_i z_i^T,qquad
V:=left|F_z-rac{20-A}{5}Iight|_F^2
=left|sum_iQ_iight|_F^2ge0.
]

Let

[
B:=sum_i a_i^2,
qquad
S_z:=sum_{i<j}(z_icdot z_j)^2.
]

### PROVED / EXACT

The exact identity is

[
oxed{
S_z=
30-3A+rac{A^2}{10}-rac12B+rac12V.
}
]

Thus the universal inequality is obtained by dropping (V/2).

Under

[
0le a_ilerac14,qquad sum_i a_i=A,
]

the maximum possible (B) is obtained by concentration. At

[
A=A_*=rac{383}{504}
=rac34+rac5{504},
]

the extremal pattern is

[
left(rac14,rac14,rac14,rac5{504},0^{16}ight)
]

up to permutation, giving

[
B_{max}
=
rac3{16}
+left(rac5{504}ight)^2.
]

Therefore

[
oxed{
S_zge
rac{8790283}{317520}
approx27.6841868228773.
}
]

This is the strongest current universal Type-E (Q)-floor.

### CORRECTION

A weaker cap-only estimate

[
sum_i a_i^2lerac A4
]

gives only (S_zge27.682995953ldots). It is valid but is **not** the strongest current bound and must not replace the exact concentration floor above.

---

## 5. Exact second-order midpoint concentration stability

For

[
rac34le Ale A_*,
]

the exact concentrated maximum is

[
B_{max}(A)
=
rac3{16}
+left(A-rac34ight)^2.
]

Define the concentration deficit

[
Delta:=B_{max}(A)-Bge0.
]

### PROVED / EXACT

Then

[
oxed{
S_z
ge
rac{237}{8}
-rac94A
-rac25A^2
+rac12Delta+rac12V.
}
]

Writing

[
t=A_*-A,
]

this becomes

[
oxed{
S_z
ge
rac{8790283}{317520}
+rac{3601}{1260}t
-rac25t^2
+rac12Delta+rac12V.
}
]

Thus moving below the terminal midpoint-energy bound forces a first-order increase in the projective squared-correlation floor, while midpoint deconcentration and frame anisotropy add the nonnegative penalties (Delta/2) and (V/2).

---

## 6. Six-exception localization

Among the 190 distinguished-edge pairings, only six core pairings can violate

[
|z_icdot z_j|lerac12.
]

For an exceptional pair write

[
|g_e|=rac12+d_e,qquad d_e>0.
]

### PROVED / EXACT

The current raw-defect bound is

[
D:=sum_e d_e
le
D_0:=
rac{1780062775}{4032758016}
<0.441401.
]

The homogeneous positive-defect bound is

[
D_{m hom}
le
rac{5792292955405}{4129544208384}
approx1.402647038781.
]

Since (|E|le6),

[
sum_{ein E}g_e^2
=
rac{|E|}{4}+D+sum_e d_e^2
le
rac32+D_0+D_0^2
<2.136235542.
]

Combining with the strongest (Q)-floor gives

[
oxed{
S_{m safe}
:=
sum_{|g_{ij}|le1/2}g_{ij}^2
>
25.54795128168835.
}
]

Consequently there are at least 103 nonorthogonal safe pairings. The safe graph lies three edges above Mantel's 100-edge threshold, and the previously established Lovasz-Simonovits consequence remains

[
T_{m safe}ge30.
]

---

## 7. Endpoint diamond and threshold ledger

For one pair define

[
p=m_icdot m_j,qquad
g=z_icdot z_j,
]

[
r=m_icdot z_j,qquad
s=z_icdot m_j.
]

Orient so (gge0), and put

[
h=r+s,qquad k=r-s.
]

### PROVED / EXACT

The four endpoint constraints imply

[
p+g+|h|lerac12,
]

and, in the sign-free formulation,

[
p+|g|+left|r+operatorname{sgn}(g)sight|lerac12.
]

Hence, defining

[
delta_{ij}:=rac14-g_{ij}^2,
]

one has

[
oxed{
delta_{ij}
ge
p_{ij}-p_{ij}^2+h_{ij}^2.
}
]

For an exceptional pair (g=1/2+d),

[
oxed{
-pge d+|h|.
}
]

Thus raw exceptional defect and charged mixed energy must both be financed by negative midpoint correlation.

---

## 8. Midpoint determinant budget

Let

[
F_m=sum_i m_i m_i^T.
]

For each pair define

[
D_{m,ij}:=a_i a_j-p_{ij}^2.
]

### PROVED / EXACT

Summing over all pairs,

[
oxed{
sum_{i<j}D_{m,ij}
=
rac{A^2-|F_m|_F^2}{2}.
}
]

Since (F_msucceq0) is (5	imes5) with trace (A),

[
|F_m|_F^2gerac{A^2}{5},
]

so

[
oxed{
sum_{i<j}D_{m,ij}
le
rac{2A^2}{5}
le
rac{146689}{635040}
approx0.230991748551.
}
]

This remains one of the smallest global budgets available in the Type-E reduction.

---

## 9. Full four-vector Gram determinant

For a pair let

[
a=a_i,qquad b=a_j,qquad
D_m=ab-p^2,
]

[
D_z=(1-a)(1-b)-g^2,
qquad
L=a+b-2ab.
]

The local Gram matrix on

[
(m_i,z_i,m_j,z_j)
]

is

[
mathcal G_{ij}
=
egin{pmatrix}
a&0&p&r\
0&1-a&s&g\
p&s&b&0\
r&g&0&1-b
end{pmatrix}succeq0.
]

### PROVED / EXACT

In charged/uncharged coordinates

[
h=r+s,qquad k=r-s,
]

its determinant is exactly

[
oxed{
detmathcal G_{ij}
=
D_mD_z
+rac{(h^2-k^2)^2}{16}
-rac14mathcal Q(h,k),
}
]

where

[
oxed{
mathcal Q(h,k)
=
(L+2pg)h^2
+
(L-2pg)k^2
-
2(a-b)hk.
}
]

The coefficient matrix of (mathcal Q) is positive semidefinite. Its determinant is

[
oxed{
4left[
ab(1-a)(1-b)-p^2g^2
ight]ge0.
}
]

Define its smaller eigenvalue

[
oxed{
lambda_-
=
L-sqrt{(a-b)^2+4p^2g^2}.
}
]

Then

[
oxed{
lambda_-ge0
}
]

and Gram positivity implies

[
oxed{
lambda_-(h^2+k^2)
le
4D_mD_z+rac{(h^2-k^2)^2}{4}.
}
]

Away from zero-energy boundary cases, (lambda_-=0) requires simultaneous Cauchy saturation

[
p^2=ab,
qquad
g^2=(1-a)(1-b).
]

This is the current exact local spectral obstruction for the uncharged mixed channel.

---

## 10. Safe-pair spectral envelope

### PROVED / EXACT

For a safe pair,

[
|g|lerac12,
]

so

[
p^2g^2lerac14ab.
]

Since

[
lambda_+lambda_-
=
4left[ab(1-a)(1-b)-p^2g^2ight]
]

and

[
lambda_+le2L=2(a+b-2ab),
]

one obtains, whenever (L>0),

[
oxed{
lambda_-
ge
rac{
2ableft((1-a)(1-b)-1/4ight)
}{
a+b-2ab
}.
}
]

For equal midpoint energies (a=b=qle1/8), the exact safe envelope sharpens to

[
oxed{
lambda_-ge q(1-2q).
}
]

For an arbitrary pair in the same equal-energy range,

[
oxed{
lambda_-ge q(1-4q),
}
]

with the bad branch driven toward

[
p=-q,qquad g=rac12+q.
]

Thus spectral degeneration in the small-energy regime migrates toward the exceptional-pair budget.

---

## 11. Seventeen-index controlled core

Choose any threshold

[
t>rac{A_*}{4}
=
rac{383}{2016}
approx0.189980159.
]

Then at most three midpoint energies can satisfy (a_ige t). Hence at least 17 indices satisfy (a_i<t).

There are at most

[
3cdot17+inom32=54
]

pairs touching the at-most-three outside indices.

### PROVED / EXACT

Since every safe pair contributes at most (1/4),

[
oxed{
S_{m core,safe}
>
25.54795128168835-rac{54}{4}
=
12.04795128168835.
}
]

The 17-index core contains 136 pairs, at most six of which can be exceptional, so at least

[
oxed{130}
]

core pairs are safe.

Moreover, at least 19 safe core pairs satisfy

[
oxed{
|z_icdot z_j|>rac14.
}
]

Indeed, if only (N) safe core pairs had (g_{ij}^2>1/16), then

[
S_{m core,safe}
le
rac N4+rac{136-N}{16},
]

and the lower bound above forces (N>18.92).

For the convenient rational choice

[
t=rac{191}{1000},
]

every safe core pair also obeys

[
oxed{
lambda_-
>
0.808962,
rac{ab}{a+b-2ab}.
}
]

No (D_5) labeling is used in this core localization.

---

## 12. Complete-hiding determinant slice

### PROVED / EXACT

If the charged channel vanishes,

[
h=0,
]

then (s=-r). Writing (x=r^2),

[
oxed{
detmathcal G_{ij}
=
x^2-Kx+D_mD_z,
}
]

where

[
K=a(1-b)+b(1-a)-2pg.
]

On the connected PSD branch containing (x=0),

[
oxed{
xle
rac{K-sqrt{K^2-4D_mD_z}}{2}
}
]

whenever the displayed discriminant is nonnegative.

Thus perfectly hidden mixed energy consumes both midpoint and projected determinant deficits.

---

## 13. HHL theorem retained from 2026-09-22

For the HHL midpoint pattern

[
a_1=a_2=rac14,qquad a_3=t,qquad 0<tlerac5{504},
]

the 2026-09-22 checkpoint proved the following under the single additional hypothesis that one safe projective correlation saturates.

### PROVED / EXACT under one-saturation hypothesis

If, after orientation,

[
z_1cdot z_2=rac12,
]

then the rank-five determinant reduction yields

[
oxed{
D=d_1+d_2
ge
s(t):=
rac{t+sqrt{3t(5-8t)}}{10}.
}
]

The local squared-correlation loss satisfies

[
oxed{
Lge s(t)(1-s(t)).
}
]

Equality forces

[
d_1d_2=0,
]

so a second safe correlation saturates at equality.

At

[
t=rac5{504},
]

[
s=
rac1{1008}+rac{sqrt{93}}{252},
]

and

[
L=
-rac{481}{1016064}
+rac{503sqrt{93}}{127008}
approx0.037719130549095.
]

### OPEN

The remaining local HHL theorem is to prove that a global HHL maximizer must possess at least one saturated safe correlation.

---

## 14. D5/Q structure

### PROVED / EXACT structural data

For the exact (D_5) 20-line template

[
z_{ij}^{pm}=(e_ipm e_j)/sqrt2,
]

the (Q)-Gram matrix has rank 14 and nullity 6. The kernel decomposes into one global tight-frame relation and five local support-sum cycle relations.

### CAUTION

The numerical coincidence between this six-dimensional kernel and the six exceptional projective pairings is only a clue. No one-to-one identification has been proved.

The Cohn–Jiao–Kumar–Torquato infinitesimal rigidity of (D_5) via (A_2/D_4)-type embeddings remains a candidate source of second-order control, but no quantitative perturbative theorem has yet been imported into the Type-E proof.

---

## 15. Current proof-status ledger

### PROVED / EXACT

- (40le	au_5le44).
- Type-E star/broom/matching bounds listed above.
- (Ale383/504) and (0le a_ile1/4).
- rigorous 21-line zero-midpoint exclusion.
- exact global (Q)/frame identity.
- strongest universal Type-E (Q)-floor
  [
  S_zge8790283/317520approx27.6841868228773.
  ]
- exact second-order concentration/frame-variance refinement.
- at most six exceptional projective pairings.
- safe squared-correlation mass
  [
  S_{m safe}>25.54795128168835.
  ]
- midpoint determinant budget
  [
  sum D_mle146689/635040<0.231.
  ]
- full (4	imes4) Gram determinant identity in ((h,k)).
- safe-pair spectral envelope.
- 17-index controlled core with
  [
  S_{m core,safe}>12.04795128168835.
  ]
- at least 130 safe pairs in that core.
- at least 19 core-safe pairs with (|g|>1/4).
- HHL one-saturation theorem from the 2026-09-22 checkpoint.

### CONDITIONAL

- full HHL envelope still requires proving existence of the first saturated safe correlation at a global HHL maximizer.

### NUMERICAL

- deterministic endpoint-model reconnaissance from the 2026-09-22 checkpoint remains useful evidence for the active HLL/HHL faces, but is not used as proof.

### OPEN

- Type E elimination.
- proof that a global HHL optimizer has one safe saturation.
- conversion of the 17-core (Q)-mass plus the (<0.231) midpoint determinant budget into a global mixed-channel contradiction.
- justification of a (D_5)-type labeling/contact structure sufficient to use the five local (Q)-cycle kernel relations.
- Type C exhaustive/boundary proof.
- Type D.
- generic (ege27).
- proof of (delta(G)ge1) for unconditional sparse (e=23,24) classification.

---

## 16. Highest-value next exact target

The most promising scalar route is now:

1. keep the exact second-order global ledger
   [
   S_z
   ge
   rac{8790283}{317520}
   +rac{3601}{1260}(A_*-A)
   -rac25(A_*-A)^2
   +rac12Delta+rac12V;
   ]

2. use the six-exception theorem to keep more than (12.04795) units of safe squared-correlation mass inside a 17-index low-midpoint core;

3. combine the safe-pair spectral lower envelope with the tiny global midpoint determinant budget
   [
   sum D_m<0.231;
   ]

4. control the remaining uncharged mixed channel via the exact (4	imes4) determinant identity;

5. if the scalar route stalls, return to the five local (D_5) (Q)-kernel cycle relations, but only after a (D_5)-type contact labeling is justified.

The target is a quantitative second-order contradiction forcing

[
A>rac{383}{504},
]

which would eliminate Type E.

No such contradiction is claimed yet.
