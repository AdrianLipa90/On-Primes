# Möbius–CRT Low-Divisor Phase Block v0.1

Status: **EXACT_TRUNCATED_DECOMPOSITION / UNIFORM_LOW_BLOCK_ERROR / HIGH_DIVISOR_TAIL_OPEN**

Date: 2026-09-26

Parent:
- \`proofs/SHIFTED_VON_MANGOLDT_CRT_PHASE_V0_1.md\`

## 1. Truncated divisor block

For

\[
C_h(X)=\sum_{n\le X}\Lambda(n)\Lambda(n+h),
\]

the exact CRT expansion is

\[
C_h(X)
=
\sum_{d\le X}
\sum_{e\le X+h}
\mu(d)\mu(e)\log d\log e\,
N_{d,e}(X;h).
\]

Fix \(R\le X\) and define the low-divisor block

\[
C_{h,\le R}(X)
=
\sum_{d\le R}
\sum_{e\le R}
\mu(d)\mu(e)\log d\log e\,
N_{d,e}(X;h).
\]

## 2. Density coefficient

For

\[
g=\gcd(d,e),
\qquad
\ell=\operatorname{lcm}(d,e),
\]

the channel is compatible iff \(g\mid h\).

Define

\[
\boxed{
M_{h,R}
=
\sum_{\substack{d,e\le R\\ \gcd(d,e)\mid h}}
\frac{
\mu(d)\mu(e)\log d\log e
}{
\operatorname{lcm}(d,e)
}.
}
\]

This is a finite arithmetic quantity.

## 3. Uniform counting error

For every compatible residue class modulo \(\ell\),

\[
N_{d,e}(X;h)
=
\frac{X}{\ell}
+
\varepsilon_{d,e},
\qquad
|\varepsilon_{d,e}|\le1.
\]

Therefore

\[
C_{h,\le R}(X)
=
X M_{h,R}
+
E_{h,R}(X),
\]

with

\[
|E_{h,R}(X)|
\le
\sum_{d,e\le R}
|\mu(d)\mu(e)|\log d\log e.
\]

Using \(|\mu|\le1\),

\[
\sum_{d\le R}|\mu(d)|\log d
\le
\sum_{d\le R}\log d
=
\log(R!)
\le
R\log R
\]

for \(R\ge2\). Hence

\[
\boxed{
|E_{h,R}(X)|
\le
(R\log R)^2.
}
\]

This bound is uniform in \(h\).

## 4. Sub-square-root closure

If \(R=R(X)\) satisfies

\[
R\log R=o(\sqrt X),
\]

then

\[
(R\log R)^2=o(X)
\]

and therefore

\[
\boxed{
C_{h,\le R}(X)
=
X M_{h,R}
+
o(X)
}
\]

uniformly in \(h\) for the declared low block.

In particular, for every fixed \(\varepsilon>0\),

\[
R=X^{1/2-\varepsilon}
\]

gives

\[
|E_{h,R}(X)|
=
O\!\left(
X^{1-2\varepsilon}\log^2X
\right)
=
o(X).
\]

No Möbius cancellation is needed for this low-divisor block.

## 5. Exact ARPL character form

The compatibility indicator has the exact finite character representation

\[
\boxed{
\mathbf1_{g\mid h}
=
\frac1g
\sum_{a=0}^{g-1}
e^{2\pi i a h/g}.
}
\]

Therefore

\[
\boxed{
M_{h,R}
=
\sum_{d,e\le R}
\frac{
\mu(d)\mu(e)\log d\log e
}{
\operatorname{lcm}(d,e)
}
\frac1{\gcd(d,e)}
\sum_{a=0}^{\gcd(d,e)-1}
e^{2\pi i a h/\gcd(d,e)}.
}
\]

Thus the complete low-divisor density coefficient is an explicit finite ARPL Fourier observable.

No heuristic singular series is inserted.

## 6. Exact tail split

Define

\[
T_{h,R}(X)
=
C_h(X)-C_{h,\le R}(X).
\]

Then

\[
\boxed{
C_h(X)
=
X M_{h,R}
+
E_{h,R}(X)
+
T_{h,R}(X),
}
\]

where

\[
|E_{h,R}(X)|\le(R\log R)^2.
\]

All unresolved arithmetic difficulty is therefore concentrated in the high-divisor tail

\[
T_{h,R}(X),
\]

which contains terms with

\[
d>R
\quad\text{or}\quad
e>R.
\]

## 7. Interpretation for the form-factor programme

For a sub-square-root divisor cutoff, the low modular phase block is already controlled to \(o(X)\).

The remaining \(q(T)\)-scaled Montgomery/explicit-formula problem is not a failure of CRT or phase representation. It is a tail theorem:

\[
\boxed{
T_{h,R}(X)
\ \text{must be controlled uniformly in the moving window/shift regime.}
}
\]

This is substantially sharper than asking for an undifferentiated "prime-pair correlation theorem."

## 8. No-go against absolute treatment of the full range

If one takes \(R\) comparable to \(X\), the elementary bound becomes

\[
(R\log R)^2
\asymp
X^2\log^2X,
\]

far above the expected \(O(X)\) scale.

Therefore a full-range proof cannot be obtained by applying the same termwise \(O(1)\) residue-count error and summing absolute values.

Cancellation, a different decomposition, a sieve/large-sieve estimate, or an operator identity is necessary for the high-divisor sector.

## 9. New gate

### OP-F27 — high-divisor tail closure

Choose a sub-square-root scale \(R(X)\), for example

\[
R=X^{1/2-\varepsilon},
\]

and prove a uniform estimate

\[
T_{h,R}(X)=o(X)
\]

in the shift/window regime needed by the scaled form-factor problem, or derive the correct nonzero main contribution if the high-divisor tail carries part of it.

A valid proof must not assume the Hardy--Littlewood correlation asymptotic it is intended to establish.

## 10. Compact theorem

### Theorem — controlled low-divisor ARPL block

For every \(R\ge2\),

\[
\boxed{
C_{h,\le R}(X)
=
X M_{h,R}
+
E_{h,R}(X),
\qquad
|E_{h,R}(X)|\le(R\log R)^2.
}
\]

Moreover \(M_{h,R}\) is exactly a finite sum of ARPL additive characters through

\[
\mathbf1_{\gcd(d,e)\mid h}
=
\frac1{\gcd(d,e)}
\sum_{a=0}^{\gcd(d,e)-1}
e^{2\pi i a h/\gcd(d,e)}.
\]

Hence for \(R\log R=o(\sqrt X)\), the low-divisor phase block is asymptotically controlled at \(o(X)\) error. Q.E.D.
