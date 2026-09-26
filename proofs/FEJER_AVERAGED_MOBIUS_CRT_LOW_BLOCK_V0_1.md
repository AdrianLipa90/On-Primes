# Fejér-Averaged Möbius–CRT Low Block v0.1

Status: **EXACT_SHIFT_AVERAGE / EXACT_PHASE_GATE_AVERAGE / LOW_BLOCK_MEAN_ASYMPTOTIC_FROM_STANDARD_PNT / AVERAGED_HIGH_TAIL_OPEN**

Date: 2026-09-26

Parents:
- \`proofs/SHIFTED_VON_MANGOLDT_CRT_PHASE_V0_1.md\`
- \`proofs/MOBIUS_CRT_LOW_DIVISOR_PHASE_BLOCK_V0_1.md\`
- \`proofs/PHASE_BANK_FORM_FACTOR_DUALITY_V0_1.md\`

## 1. Why average over the shift

The fixed-shift problem

\[
C_h(X)=\sum_{n\le X}\Lambda(n)\Lambda(n+h)
\]

is too strong a target for the form-factor programme if demanded uniformly for every fixed \(h\). In particular, \(h=2\) touches the twin-prime correlation barrier.

The phase/form-factor observable is naturally quadratic and Fourier averaged. Therefore introduce the Fejér shift weights

\[
w_H(h)
=
\begin{cases}
1-\dfrac{|h|}{H+1},&|h|\le H,\\
0,&|h|>H.
\end{cases}
\]

Write

\[
L=H+1.
\]

Then

\[
\sum_{h=-H}^{H}w_H(h)=L.
\]

For any even shift observable \(F(h)=F(-h)\), define

\[
\langle F\rangle_H
=
\frac1L
\sum_{h=-H}^{H}
w_H(h)F(h).
\]

Equivalently,

\[
\langle F\rangle_H
=
\frac1L
\left[
F(0)+
2\sum_{h=1}^{H}
\left(1-\frac{h}{L}\right)F(h)
\right].
\]

## 2. Exact finite Fejér/Wiener–Khintchine identity

For any finite complex sequence \(a_n\), extended by zero outside its declared support, define

\[
A(\alpha)=\sum_n a_n e^{2\pi i n\alpha}
\]

and

\[
R_a(h)=\sum_n a_n\overline{a_{n+h}}.
\]

Then

\[
\boxed{
\sum_{h=-H}^{H}
w_H(h)R_a(h)
=
\int_0^1
|A(\alpha)|^2
F_H(\alpha)\,d\alpha,
}
\]

where

\[
\boxed{
F_H(\alpha)
=
\frac1L
\left(
\frac{\sin(\pi L\alpha)}
{\sin(\pi\alpha)}
\right)^2
}
\]

is the Fejér kernel.

Hence the symmetric weighted shift average is a nonnegative spectral-power observable.

This identity is exact finite Fourier algebra and uses no prime conjecture.

## 3. Exact average of the CRT phase gate

The previous Möbius–CRT theorem uses the compatibility gate

\[
\mathbf1_{g\mid h},
\qquad
g=\gcd(d,e).
\]

Define its normalized Fejér average

\[
Q_H(g)
=
\left\langle
\mathbf1_{g\mid h}
\right\rangle_H.
\]

Let

\[
r_g=L\bmod g,
\qquad
0\le r_g<g.
\]

Then

\[
\boxed{
Q_H(g)
=
\frac1g
+
\frac{r_g(g-r_g)}{gL^2}.
}
\]

### Proof

Let

\[
M=\left\lfloor\frac{H}{g}\right\rfloor.
\]

The multiples of \(g\) in \([-H,H]\) are \(kg\), \(|k|\le M\), so

\[
LQ_H(g)
=
1+
2\sum_{k=1}^{M}
\left(
1-\frac{kg}{L}
\right)
=
1+2M-\frac{gM(M+1)}{L}.
\]

Writing \(L=qg+r_g\) gives the stated closed form after elementary simplification.

Consequently

\[
\boxed{
Q_H(g)\ge\frac1g
}
\]

and

\[
\boxed{
0
\le
Q_H(g)-\frac1g
\le
\frac{g}{4L^2}.
}
\]

If \(g\mid L\), the correction vanishes exactly.

## 4. Fejér average of the low-divisor density coefficient

Recall

\[
M_{h,R}
=
\sum_{\substack{d,e\le R\\\gcd(d,e)\mid h}}
\frac{
\mu(d)\mu(e)\log d\log e
}{
\operatorname{lcm}(d,e)
}.
\]

Define

\[
\overline M_{H,R}
=
\langle M_{\cdot,R}\rangle_H.
\]

Put

\[
S_R
=
\sum_{d\le R}
\frac{\mu(d)\log d}{d}.
\]

Using

\[
\gcd(d,e)\operatorname{lcm}(d,e)=de
\]

and the exact formula for \(Q_H(g)\),

\[
\boxed{
\overline M_{H,R}
=
S_R^2
+
\mathcal B_{H,R},
}
\]

where

\[
\boxed{
\mathcal B_{H,R}
=
\frac1{L^2}
\sum_{d,e\le R}
\frac{
\mu(d)\mu(e)\log d\log e
}{
de
}
\,r_g(g-r_g),
\qquad
g=\gcd(d,e).
}
\]

The leading Fejér-averaged CRT density therefore factorizes exactly into the square of a one-dimensional Möbius sum.

No Hardy–Littlewood singular-series asymptotic is inserted.

## 5. Explicit bound for the finite-\(H\) edge correction

Since

\[
r_g(g-r_g)\le\frac{g^2}{4},
\]

we have

\[
|\mathcal B_{H,R}|
\le
\frac1{4L^2}
\sum_{d,e\le R}
\frac{
|\mu(d)\mu(e)|\log d\log e
}{
de
}
\gcd(d,e)^2.
\]

Write

\[
d=ga,\qquad e=gb.
\]

Dropping the coprimality restriction on \(a,b\) only enlarges the absolute sum. Hence

\[
|\mathcal B_{H,R}|
\le
\frac{\log^2R}{4L^2}
\sum_{g\le R}
\left(
\sum_{a\le R/g}\frac1a
\right)^2.
\]

Using

\[
\sum_{a\le y}\frac1a\le1+\log y
\]

and the monotone-integral bound

\[
\sum_{g\le R}
\left(
1+\log\frac{R}{g}
\right)^2
\le
5R+(1+\log R)^2,
\]

we obtain the explicit estimate

\[
\boxed{
|\mathcal B_{H,R}|
\le
\frac{
\log^2R
}{
4L^2
}
\left[
5R+(1+\log R)^2
\right].
}
\]

In particular,

\[
\boxed{
R\log^2R=o(H^2)
\Longrightarrow
\mathcal B_{H,R}=o(1).
}
\]

## 6. Standard PNT input and the mean low-block coefficient

A classical consequence of the prime number theorem is

\[
\boxed{
\sum_{n=1}^{\infty}
\frac{\mu(n)\log n}{n}
=
-1
}
\]

in the conditionally convergent sense.

Therefore

\[
S_R\to-1
\]

and hence

\[
S_R^2\to1.
\]

Combining this with Section 5 gives

\[
\boxed{
\overline M_{H,R}\to1
}
\]

whenever

\[
R\to\infty,
\qquad
H\to\infty,
\qquad
R\log^2R=o(H^2).
\]

This is an averaged low-block density theorem. It does not prove any fixed-shift Hardy–Littlewood asymptotic.

## 7. Averaged low-divisor correlation

The previous low-block theorem gives, uniformly in \(h\),

\[
C_{h,\le R}(X)
=
XM_{h,R}
+
E_{h,R}(X)
\]

with

\[
|E_{h,R}(X)|
\le
(R\log R)^2.
\]

Take the Fejér average:

\[
\overline C_{H,R}(X)
=
\frac1L
\left[
C_{0,\le R}(X)
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
C_{h,\le R}(X)
\right].
\]

Because the normalized positive weights sum to one,

\[
\boxed{
\overline C_{H,R}(X)
=
X\overline M_{H,R}
+
\overline E_{H,R}(X),
}
\]

with

\[
\boxed{
|\overline E_{H,R}(X)|
\le
(R\log R)^2.
}
\]

Therefore

\[
\boxed{
\frac{\overline C_{H,R}(X)}{X}
=
S_R^2
+
\mathcal B_{H,R}
+
O\!\left(
\frac{(R\log R)^2}{X}
\right).
}
\]

Consequently, under the two-scale conditions

\[
\boxed{
(R\log R)^2=o(X),
\qquad
R\log^2R=o(H^2),
}
\]

and \(R\to\infty\),

\[
\boxed{
\frac{\overline C_{H,R}(X)}{X}
\to1.
}
\]

This is rigorous for the declared low-divisor block and uses only the exact CRT decomposition plus the standard PNT Möbius limit.

## 8. Boundary relation to the positive spectral Fejér average

For the full von Mangoldt sequence define the zero-extended truncated correlation

\[
C_h^\circ(X)
=
\sum_{1\le n,\ n+h\le X}
\Lambda(n)\Lambda(n+h).
\]

Then Section 2 gives exactly

\[
\boxed{
C_0^\circ(X)
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
C_h^\circ(X)
=
\int_0^1
\left|
\sum_{n\le X}
\Lambda(n)e^{2\pi in\alpha}
\right|^2
F_H(\alpha)\,d\alpha.
}
\]

The original forward correlation

\[
C_h(X)
=
\sum_{n\le X}
\Lambda(n)\Lambda(n+h)
\]

differs only by the right boundary

\[
C_h(X)-C_h^\circ(X)
=
\sum_{X-h<n\le X}
\Lambda(n)\Lambda(n+h).
\]

For \(H\le X\),

\[
|C_h(X)-C_h^\circ(X)|
\le
h\,\log X\,\log(X+H).
\]

Hence the normalized Fejér averages differ by at most

\[
\boxed{
\frac{H(H+2)}{3(H+1)}
\log X\log(X+H).
}
\]

Thus if

\[
H\log^2(X+H)=o(X),
\]

the forward-correlation Fejér average and the positive spectral Fejér average differ by \(o(X)\).

## 9. What this changes in the Montgomery–Dyson programme

The fixed-\(h\) high-tail gate is stronger than necessary for form-factor purposes.

The phase-spectroscopy observable naturally asks for a weighted average over shifts. The low-divisor block of that averaged observable is now asymptotically closed:

\[
\boxed{
\overline C_{H,R}(X)
\sim X
}
\]

under the declared two-scale conditions.

Therefore the remaining arithmetic obstruction can be narrowed to the **Fejér-averaged high-divisor tail**

\[
\boxed{
\overline T_{H,R}(X)
=
\frac1L
\left[
T_{0,R}(X)
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
T_{h,R}(X)
\right].
}
\]

For the form-factor programme it is sufficient to control this averaged tail in the required moving window. One does not need to prove the Hardy–Littlewood asymptotic separately for every fixed \(h\).

This is a strictly weaker and more naturally spectral target.

## 10. Prior-art boundary

The use of shift averages, mean squares of primes in short intervals, and their relation to zeta pair correlation is classical. In particular:

- P. X. Gallagher, *On the distribution of primes in short intervals*, Mathematika 23 (1976), 4–9.
- D. A. Goldston and H. L. Montgomery, *On pair correlations of zeros and primes in short intervals*, in *Analytic Number Theory and Diophantine Problems* (1987), 183–203.
- Classical large-sieve/dispersion methods provide the standard analytic context for averaged arithmetic correlations.

The exact finite CRT-phase gate average and its integration into the current ARPL/Möbius low-block decomposition are repository-specific packaging. No novelty claim is made for Fejér kernels, Wiener–Khintchine, PNT, or classical short-interval theory.

## 11. New focused gate

### OP-F28 — Fejér-averaged high-divisor tail closure

Instead of demanding

\[
T_{h,R}(X)=o(X)
\]

for every fixed \(h\), prove the weaker spectral statement

\[
\boxed{
\overline T_{H,R}(X)=o(X)
}
\]

in the \(q(T)\)-scaled window required by the form-factor programme.

The theorem must specify:
- the joint growth of \(X,H,R\);
- smoothing/window normalization;
- boundary correction;
- diagonal subtraction;
- prime-power contributions;
- every RH or zero-density assumption;
- whether the result is pointwise in the form-factor frequency or integrated against a test function.

A large-sieve, dispersion, Vaughan/Heath-Brown identity, or zero-list-free operator route is admissible.

## 12. Compact theorem

### Theorem — Fejér-averaged low Möbius–CRT block

Let

\[
L=H+1,
\qquad
w_H(h)=1-\frac{|h|}{L}
\quad(|h|\le H).
\]

Then for every \(g\ge1\),

\[
\boxed{
\frac1L
\sum_{\substack{|h|\le H\\g\mid h}}
w_H(h)
=
\frac1g
+
\frac{r_g(g-r_g)}{gL^2},
\qquad
r_g=L\bmod g.
}
\]

Consequently,

\[
\boxed{
\overline M_{H,R}
=
\left(
\sum_{d\le R}
\frac{\mu(d)\log d}{d}
\right)^2
+
\mathcal B_{H,R},
}
\]

with

\[
\boxed{
|\mathcal B_{H,R}|
\le
\frac{\log^2R}{4L^2}
\left[
5R+(1+\log R)^2
\right].
}
\]

Together with

\[
|E_{h,R}(X)|\le(R\log R)^2
\]

and the standard PNT limit

\[
\sum_{d\le R}\frac{\mu(d)\log d}{d}\to-1,
\]

this gives

\[
\boxed{
\frac{\overline C_{H,R}(X)}{X}\to1
}
\]

provided

\[
(R\log R)^2=o(X),
\qquad
R\log^2R=o(H^2),
\qquad
R\to\infty.
\]

Q.E.D.
