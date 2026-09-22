# Type E — exact HHL rank-five Gram reduction

**Date:** 2026-09-22

**Status discipline:** statements below are labelled PROVED, CONDITIONAL, NUMERICAL, or OPEN.

## Setup

For an HHL safe triangle take

\[
a_1=a_2=\frac14,\qquad a_3=t,
\]

and write, for each deep edge,

\[
P_i=m_i+z_i,\qquad N_i=m_i-z_i,
\]

so \(m_i\perp z_i\), \(\|m_i\|^2=a_i\), and \(\|z_i\|^2=1-a_i\).

For a pair \((i,j)\), put

\[
u=m_i\cdot m_j,\quad p=m_i\cdot z_j,\quad q=z_i\cdot m_j,\quad r=z_i\cdot z_j.
\]

The four endpoint constraints are the four linear inequalities

\[
|u\pm p\pm q\pm r|\le\frac12
\]

with the signs arising from the choices of endpoints.

## Two saturated adjacent projective correlations

### PROVED
If \(|z_i\cdot z_j|=1/2\) for a safe pair, the four endpoint inequalities force

\[
u=p=q=0.
\]

Assume the two adjacent pairs \((1,2)\) and \((2,3)\) have projective correlation \(+1/2\). After the saturation lemma, their only nonzero cross moment is

\[
z_1\cdot z_2=z_2\cdot z_3=\frac12.
\]

For the remaining pair \((3,1)\), retain four variables

\[
u=m_3\cdot m_1,\quad p=m_3\cdot z_1,\quad q=z_3\cdot m_1,\quad r=z_3\cdot z_1.
\]

In the ordered basis

\[
(m_1,z_1,m_2,z_2,m_3,z_3),
\]

the exact Gram matrix is

\[
G=\begin{pmatrix}
1/4&0&0&0&u&q\\
0&3/4&0&1/2&p&r\\
0&0&1/4&0&0&0\\
0&1/2&0&3/4&0&1/2\\
u&p&0&0&t&0\\
q&r&0&1/2&0&1-t
\end{pmatrix}.
\]

Because these six vectors lie in \(\mathbb R^5\),

\[
\det G=0.
\]

Direct exact expansion gives the finite polynomial constraint

\[
\boxed{
48p^2q^2+12p^2t-8p^2-96pqru+32pqu-20q^2t
-12r^2t+48r^2u^2+8rt-32ru^2
-5t^2+20tu^2+2t-8u^2=0.
}
\]

Thus, once two adjacent projective correlations saturate, the HHL problem is reduced exactly to a four-variable semialgebraic problem in \((u,p,q,r)\), with four endpoint inequalities, Gram PSD, and the displayed rank-five equation. No generic SDP is required for this branch.

## Observed HHL active face

### NUMERICAL
The deterministic full-endpoint JuMP/Ipopt scan identifies the remaining pair with

\[
u=s,\qquad p=-s,\qquad q=s,\qquad r=\frac12-s.
\]

At \(t=5/504\), it gives

\[
s\approx0.039260518892,
\]

with independent feasibility residual below \(10^{-10}\), and the six-vector Gram matrix has one zero eigenvalue and five positive eigenvalues to numerical precision.

### CONDITIONAL EXACT
Substituting the observed active face into the exact determinant yields

\[
\boxed{
\det G=-\frac{20s^2-4st+5t^2-3t}{256}.
}
\]

Hence rank five forces

\[
20s^2-4st+5t^2-3t=0.
\]

The two algebraic roots are

\[
s_\pm(t)=\frac{t\pm\sqrt{3t(5-8t)}}{10}.
\]

For \(0<t<3/5\), the minus root is negative. On this active face the safe constraint \(r\le1/2\), together with \(r=1/2-s\), requires \(s\ge0\). Therefore the admissible rank-five root is uniquely

\[
\boxed{
s(t)=\frac{t+\sqrt{3t(5-8t)}}{10}.
}
\]

This root selection is exact; it does not depend on numerical optimization once the active face is assumed.

The squared-correlation objective on the triangle is

\[
F=\frac14+\frac14+\left(\frac12-s\right)^2,
\]

so the local loss is

\[
\boxed{L=s-s^2.}
\]

At the terminal Type-E scale \(t=5/504\),

\[
\boxed{
s=\frac1{1008}+\frac{\sqrt{93}}{252}}
\]

and

\[
\boxed{
L=-\frac{481}{1016064}+\frac{503\sqrt{93}}{127008}
\approx0.037719130549095.
}
\]

## What is now genuinely open

### OPEN
The missing theorem is no longer the algebra on the observed face. It is the **active-face theorem**: prove that a global HHL maximizer of

\[
F=(z_1\cdot z_2)^2+(z_2\cdot z_3)^2+(z_3\cdot z_1)^2
\]

must either lie on this face or on another boundary face with no larger value.

After assuming two adjacent saturated projective correlations, the exact four-variable polynomial above makes this a small finite semialgebraic/KKT problem. The next proof target is therefore:

1. enumerate endpoint-active patterns for \((u,p,q,r)\);
2. impose the rank-five determinant equation and PSD principal minors;
3. maximize \(|r|\) on each pattern;
4. show the observed pattern \((u,p,q,r)=(s,-s,s,1/2-s)\) dominates all admissible competitors for the relevant \(t\)-interval, especially \(0<t\le5/504\).

Only after this active-face theorem is proved should the remaining global Type-E deficit of about \(0.01023215114\) be attacked via a second forced triangle or the non-scalar \(Q\)-kernel relations.
