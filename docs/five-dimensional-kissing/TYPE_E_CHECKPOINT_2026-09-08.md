# Five-dimensional kissing number — Type E checkpoint

**Date:** 2026-09-08  
**Proof-status discipline:** every statement below is labelled **PROVED**, **CONDITIONAL**, **NUMERICAL**, or **OPEN**.  
**Global proved range:**

\[
\boxed{40\le \tau_5\le 44}.
\]

## 1. Global deep-graph state

### PROVED
For a hypothetical 41-point kissing configuration in \(S^4\), the deep graph \(G\) is triangle-free and satisfies

\[
\alpha(G)\le 20,\qquad e(G)\ge 23.
\]

### CONDITIONAL
The sparse \(e=23\) and \(e=24\) classifications are conditional on proving

\[
\delta(G)\ge1.
\]

## 2. Isolated-center branch

Let \(x_0\) be an isolated center and put \(H=G-x_0\). Then:

### PROVED

\[
|V(H)|=40,\qquad \alpha(H)\le19,\qquad e(H)\ge25.
\]

The exact \(e=25\) and \(e=26\) types A and B are eliminated.

### OPEN
Types C, D, E and the generic \(e\ge27\) branch remain.

## 3. Type E graph and mass bounds

Type E has

\[
H=16K_2\sqcup F_3,
\]

with the ten-edge core \(F_3\).

### PROVED
The current exact bounds are:

- star theorem: local star mass \(\le 70/3\);
- broom theorem:
  \[
  M(F_3)\le89;
  \]
- among the three perfect matchings of \(F_3\), some matching \(P\) satisfies
  \[
  M(P)\ge \frac{S}{2}-\frac{28}{3};
  \]
- the twenty distinguished disjoint deep edges have total mass
  \[
  \ge \frac{2137}{6};
  \]
- with midpoint energies
  \[
  a_i=\|m_i\|^2,\qquad A=\sum_{i=1}^{20}a_i,
  \]
  one has
  \[
  \boxed{A\le\frac{383}{504}}.
  \]

**Do not regress to the obsolete bounds** \(M(F_3)\le94\) or \(M(P)\ge S/2-343/32\).

## 4. Zero-midpoint projective boundary

### PROVED — source audited
Musin, *Proc. Steklov Inst. Math.* 263 (2008), Sec. 5, states that for antipodal spherical codes in dimension \(5\), the \(SDP_0\) bound gives 42 points, while integrality of the distance distribution improves this to 40, citing Boyvalenkov, “Nonexistence of certain symmetric spherical codes,” *Designs, Codes and Cryptography* 3 (1993), 69–74.

Therefore at most twenty projective lines in \(\mathbb{RP}^4\) can have coherence \(\le1/2\). In particular the 21-line zero-midpoint boundary is rigorously excluded.

This exclusion does **not** depend on assuming optimality/uniqueness of the putative \((5,20)\) \(D_5\) line packing.

## 5. Distinguished-pair defect structure

### PROVED
Among the 190 distinguished-edge pairings, only the six pairings among the four selected core edges can violate the raw projective threshold.

The earlier exact convex tightening gives raw positive defect

\[
P_{\rm raw}\le
\frac{1780062775}{4032758016}<0.441401.
\]

A later exact bookkeeping refinement improves the homogeneous positive-defect ceiling from the older

\[
1.402647038781\ldots
\]

to

\[
\boxed{
P_h\le
\frac{5765499347725}{4129544208384}
=1.3961587663886985\ldots
}.
\]

The improvement is obtained by retaining the favorable product term \(-a_i a_j/16\) on nonexceptional core–noncore pairs.

## 6. Uniform two-sided three-point SDP

### PROVED NUMERICAL SATURATION / ROUTE CLOSED AS PRIMARY METHOD
At coherence \(\mu=1/2\), the uniform two-sided three-point SDP saturates the value 21 through degree pairs

\[
(4,4),\ (5,5),\ (6,6).
\]

It is therefore closed as the primary Type-E route unless qualitatively new constraints are added.

## 7. Global \(Q\)-operator route

For

\[
Q_i=z_i z_i^T-\frac{\|z_i\|^2}{5}I,
\qquad
\|z_i\|^2=1-a_i,
\]

### PROVED
PSD of

\[
\left\|\sum_i Q_i\right\|^2
\]

gives

\[
\sum_{i<j}(z_i\cdot z_j)^2
\ge
30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2.
\]

Using the sharp convex concentration allowed by

\[
0\le a_i<\frac14,
\qquad
A\le\frac{383}{504},
\]

gives the stronger unconditional Type-E floor

\[
\boxed{
\sum_{i<j}(z_i\cdot z_j)^2
>
\frac{8790283}{317520}
=27.6841868228773\ldots
}.
\]

Exact \(D_5\) has value 30, so Type E retains strictly more than

\[
\boxed{92.28062\%}
\]

of the \(D_5\) total squared-correlation mass.

This is the sharp consequence of the present scalar \(Q\)-identity using only the total midpoint-energy ceiling and the individual bound \(a_i<1/4\).

## 8. Universal rank-14 \(Q\)-frame inequality

The traceless symmetric matrices lie in

\[
\operatorname{Sym}_0(5),\qquad \dim=14.
\]

### PROVED
If

\[
K_{ij}=\langle Q_i,Q_j\rangle
=(z_i\cdot z_j)^2-\frac15q_iq_j,
\qquad q_i=\|z_i\|^2,
\]

then \(K\succeq0\), \(\operatorname{rank}K\le14\), and hence

\[
\boxed{
\sum_{i<j}
\left((z_i\cdot z_j)^2-\frac15q_iq_j\right)^2
\ge
\frac{4W^2}{175}-\frac{8Z}{25}
}
\]

where

\[
W=\sum_iq_i^2,\qquad Z=\sum_iq_i^4.
\]

### PROOF-STATUS CORRECTION
A six-dimensional nullspace by itself is **not** special to \(D_5\): twenty \(Q_i\)'s in a 14-dimensional ambient space always have nullity at least six. What is special to exact \(D_5\) is the explicit structure of its kernel.

## 9. Exact \(D_5\) kernel classification

For the exact twenty-line template

\[
z_{ij}^{\pm}=\frac{e_i\pm e_j}{\sqrt2},
\qquad1\le i<j\le5,
\]

### PROVED
Any kernel relation

\[
\sum_{i<j}\left(c_{ij}^+Q_{ij}^+ + c_{ij}^-Q_{ij}^-\right)=0
\]

must satisfy

\[
\boxed{c_{ij}^+=c_{ij}^-=:x_{ij}}.
\]

Writing

\[
T=\sum_{i<j}x_{ij},
\]

the diagonal equations become

\[
\boxed{
\sum_{j\ne i}x_{ij}=\frac{2T}{5}
\qquad(i=1,\dots,5).
}
\]

Thus the exact \(D_5\) \(Q\)-kernel is canonically identified with the edge-weight space on \(K_5\) having equal weighted degree at all five vertices. Its dimension is six.

### PROVED
The five-dimensional local subspace is generated by alternating four-cycle (“rectangle”) relations on \(K_5\). Together with the global tight-frame relation, these span the full six-dimensional kernel.

There are exactly fifteen \(K_5\) four-cycles, each giving an eight-line \(4\)-vs-\(4\) Hadamard/\(D_4\) projector circuit.

## 10. Four-side projector relations

Suppose

\[
R=\sum_{i=1}^4A_i u_i u_i^T
 =\sum_jB_jv_jv_j^T,
\qquad
\sum A_i=\sum B_j=1,
\]

and

\[
t_{ij}=(u_i\cdot v_j)^2,
\qquad
T=\operatorname{tr}(R^2).
\]

### PROVED — exact stability identity

\[
D_{AB}:=
\sum_{i,j}A_iB_j\,t_{ij}\left(t_{ij}-\frac14\right)
=
\operatorname{Var}_{A\otimes B}(t)
+T\left(T-\frac14\right).
\]

Moreover

\[
\boxed{
T-\frac14
=
\sum_{i=1}^4\left(A_i-\frac14\right)^2
+2\sum_{i<k}A_iA_k(u_i\cdot u_k)^2.
}
\]

Hence small four-side defect quantitatively forces equal weights and same-side orthogonality.

### PROVED — zero-defect classification
Zero defect forces the four-side vectors to be an orthonormal basis with weights \(1/4\), while all opposite-side vectors lie among the eight projective hypercube sign-lines

\[
\frac12(\pm u_1\pm u_2\pm u_3\pm u_4).
\]

The opposite-side probability weights have the exact Fourier form

\[
\boxed{
p_{abc}=\frac18(1+\theta abc),\qquad -1\le\theta\le1.
}
\]

Therefore the opposite support has size only 4 or 8; exact zero-defect supports of sizes 5, 6, or 7 are impossible.

Every support-minimal zero-defect four-side circuit is exactly \(4\)-vs-\(4\) Hadamard/\(D_4\).

## 11. Three-side and rank-deficient four-side charges

Let the sixteen noncore distinguished edges carry total midpoint energy

\[
A_{\rm out}=A-A_c<\frac{131}{504}.
\]

Then for noncore pairs

\[
q_iq_j>\frac{373}{504}.
\]

### PROVED
If a noncore projector dependency has a three-element sign side, its positive homogeneous cross-defect satisfies

\[
\boxed{
P_h^{\rm noncore}>
\frac{139129}{3048192}
=0.0456431222180\ldots
}.
\]

### PROVED
If a four-side relation has rank at most three, then

\[
\boxed{
P_h^{\rm cross}>
\frac{139129}{9144576}
\approx0.015214.
}
\]

So genuinely cheap four-side circuits must span four dimensions and lie quantitatively near the Hadamard/\(D_4\) equality structure.

## 12. Exact overlapping \(D_4\) blocks

### PROVED — warning
Three shared orthogonal projective lines do **not** by themselves force two Hadamard circuits into one common \(D_5\) coordinate system; continuous families exist.

### PROVED
Two distinct zero-defect circuits sharing an entire orthonormal tetrad generate the twelve projective lines of an exact \(D_4\) root configuration (the projective form of the 24-cell).

### PROVED
If two exact \(D_4\) root blocks in \(\mathbb R^5\) share a common \(D_3\) root subsystem and all cross-pairs are raw-safe, their two transverse directions must be orthogonal.

Consequently the union is exactly an 18-line \(D_5\) skeleton: all projective \(D_5\) root lines except the two lines joining the two transverse coordinate directions.

This is an exact mechanism that **produces** \(D_5\) geometry once the requisite overlapping \(D_4\) blocks are justified; it does not assume \(D_5\) beforehand.

## 13. Sixteen-noncore exact-template obstruction

A previous strategy hoped to force a Hadamard rectangle circuit inside any sixteen-line subset of exact \(D_5\). This is false.

### PROVED — exact \(D_5\) template
A sixteen-line subset contains no surviving rectangle/Hadamard circuit **iff** the four omitted projective lines lie one-per-edge on a \(C_4\subset K_5\), with an arbitrary sign choice on each deleted edge.

There are

\[
15\cdot2^4=240
\]

such exceptional deletions.

### PROVED — exact template dichotomy
For every sixteen-line subset of exact \(D_5\), either

1. a surviving \(4\)-vs-\(4\) rectangle/Hadamard circuit exists; or
2. the four omitted lines have the exceptional \(C_4\) deletion pattern, and the remaining sixteen-line kernel contains two positive \(D_3\oplus D_2\)-type relations.

Thus there is no kernel-empty exceptional case.

### IMPORTANT STATUS LIMIT
This dichotomy is **PROVED only for the exact \(D_5\) template**. It has not yet been transferred to arbitrary Type-E noncore projectors.

## 14. Current highest-priority research target

### OPEN
The main task is to prove a quantitative stability/identification theorem for arbitrary Type-E noncore projectors:

\[
\text{small kernel/defect cost}
\Longrightarrow
\begin{cases}
\text{near a Hadamard/}D_4\text{ rectangle},\\
\text{or}\\
\text{near the exceptional positive }D_3\oplus D_2\text{ model}.
\end{cases}
\]

The preferred route remains exact algebra, frame-operator variance, kernel perturbation identities, integrality/equality-case arguments, or a small finite polynomial/KKT problem before any new generic SDP.

The ultimate Type-E objective remains a quantitative second-order contradiction forcing

\[
A>\frac{383}{504},
\]

against the proved midpoint-energy ceiling.

## 15. Other open branches

### Type C — OPEN
For the \(C_7\) branch:

- equi-edge branches are eliminated exactly with objective below 69;
- the nonsymmetric rank-four local maximum is numerically
  \[
  65.7322986552,
  \]
  with an exact reflection/KKT reduction;
- exhaustive global/boundary proof remains open.

### Type D — OPEN
No complete elimination yet.

### Generic \(e\ge27\) — OPEN
No complete elimination yet.

---

## Ledger summary

The rigorous global theorem remains

\[
\boxed{40\le\tau_5\le44}.
\]

The strongest current Type-E route is no longer the uniform three-point SDP. It is the combined defect/frame/kernel program:

\[
\text{large global squared-correlation floor}
\to
\text{small allowed projective defect}
\to
\text{restricted projector-kernel geometry}
\to
\text{quantitative }D_4\!/\!(D_3\oplus D_2)\text{ stability}
\to
\text{second-order contradiction in }A.
\]
