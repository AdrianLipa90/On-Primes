# Fejér-Averaged High-Divisor Tail: Unconditional Long-Window Closure v0.1

Status: **PROVED_FROM_STANDARD_SAFFARI_VAUGHAN + EXACT_FEJER/CRT_LOW_BLOCK / SHORTER_WINDOWS_OPEN**

Date: 2026-09-26

Parents:
- \`proofs/FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1.md\`
- \`proofs/MOBIUS_CRT_LOW_DIVISOR_PHASE_BLOCK_V0_1.md\`

External standard input:
- B. Saffari and R. C. Vaughan, *On the fractional parts of \(x/n\) and related sequences. II*, Ann. Inst. Fourier 27(2) (1977), 1–30.
- The classical consequence used here is the unconditional short-interval mean-square estimate implying
  \[
  J(X,L)=o(XL^2)
  \]
  uniformly for \(L\ge X^{1/6+\varepsilon}\) in the standard long-window range.

## 1. Localized forward correlations

Fix a large \(X\) and an integer \(L=H+1\) with

\[
1\le L\le X.
\]

Define

\[
C_h^{[X,2X]}(X)
=
\sum_{X<n\le2X}
\Lambda(n)\Lambda(n+h),
\qquad
0\le h\le H.
\]

Define the normalized Fejér average

\[
\boxed{
\mathcal C_{X,H}
=
\frac1L
\left[
C_0^{[X,2X]}(X)
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
C_h^{[X,2X]}(X)
\right].
}
\]

This is the localized analogue of the shift average already used in the low-block theorem.

## 2. Sliding short-interval energy

For integers \(m\in[X,2X-1]\), define

\[
S_L(m)
=
\sum_{j=1}^{L}
\Lambda(m+j)
=
\psi(m+L)-\psi(m).
\]

Expanding the square gives

\[
\mathcal E_{X,L}
=
\sum_{m=X}^{2X-1}
S_L(m)^2.
\]

The coefficient of a displacement \(h\) in this expansion is \(L-|h|\), exactly the Fejér multiplicity.

Because the start interval in each shifted product is displaced by at most \(L\), comparison with the fixed-start correlations gives

\[
\boxed{
\mathcal E_{X,L}
=
L^2\mathcal C_{X,H}
+
O\!\left(
L^3\log^2(3X)
\right).
}
\]

Indeed every boundary product is bounded by \(\log^2(3X)\), and only \(O(L^3)\) boundary products differ.

Hence

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}
=
\frac{\mathcal E_{X,L}}{XL^2}
+
O\!\left(
\frac{L\log^2(3X)}{X}
\right).
}
\]

## 3. Short-interval mean-square input

Write

\[
S_L(m)=L+\Delta_L(m),
\]

where

\[
\Delta_L(m)
=
\psi(m+L)-\psi(m)-L.
\]

Then

\[
\mathcal E_{X,L}
=
XL^2
+
2L\sum_{m=X}^{2X-1}\Delta_L(m)
+
\sum_{m=X}^{2X-1}\Delta_L(m)^2.
\]

By Cauchy–Schwarz,

\[
\left|
\sum_{m=X}^{2X-1}\Delta_L(m)
\right|
\le
X^{1/2}
\left(
\sum_{m=X}^{2X-1}\Delta_L(m)^2
\right)^{1/2}.
\]

For integer \(L\), the function

\[
\psi(x+L)-\psi(x)-L
\]

is constant almost everywhere on each unit interval \([m,m+1)\). Therefore the discrete second moment is exactly the corresponding Selberg integral over integer endpoints:

\[
\sum_{m=X}^{2X-1}\Delta_L(m)^2
=
\int_X^{2X}
|\psi(x+L)-\psi(x)-L|^2\,dx
\]

up to measure-zero endpoints.

The Saffari–Vaughan long-window theorem gives, for every fixed \(\varepsilon>0\),

\[
\boxed{
X^{1/6+\varepsilon}\le L
\quad\Longrightarrow\quad
\sum_{m=X}^{2X-1}\Delta_L(m)^2
=
o(XL^2)
}
\]

in the standard uniform range.

Consequently

\[
\mathcal E_{X,L}
=
XL^2+o(XL^2).
\]

## 4. Full Fejér-averaged correlation

Assume in addition that

\[
L\log^2X=o(X).
\]

Then the boundary term in Section 2 is \(o(XL^2)\). Hence

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}
\to1
}
\]

unconditionally whenever

\[
\boxed{
X^{1/6+\varepsilon}\le L
\quad\text{and}\quad
L\log^2X=o(X).
}
\]

A convenient clean range is

\[
\boxed{
X^{1/6+\varepsilon}
\le
L
\le
X^{1-\delta}
}
\]

for fixed \(\varepsilon,\delta>0\).

This is an averaged correlation theorem. It does not imply the Hardy–Littlewood asymptotic for any fixed \(h\).

## 5. Localized low-divisor block

The Möbius–CRT low-block theorem localizes unchanged to an interval of length \(X\): each compatible CRT residue class contributes

\[
\frac{X}{\operatorname{lcm}(d,e)}
+
O(1)
\]

inside \((X,2X]\), with the same uniform \(O(1)\) counting error.

Therefore, with the same Fejér average,

\[
\frac{\mathcal C_{X,H,\le R}}{X}
\to1
\]

provided

\[
(R\log R)^2=o(X),
\qquad
R\log^2R=o(H^2),
\qquad
R\to\infty.
\]

Choose the explicit scale

\[
\boxed{
R=X^{1/3}.
}
\]

Then

\[
\frac{(R\log R)^2}{X}
=
X^{-1/3}\log^2X
\to0.
\]

If

\[
L=H+1\ge X^{1/6+\varepsilon},
\]

then

\[
\frac{R\log^2R}{H^2}
\ll
X^{-2\varepsilon}\log^2X
\to0.
\]

Thus the low block and full averaged correlation have the same asymptotic main term \(X\).

## 6. Unconditional averaged high-tail closure

Define the localized high-divisor tail by

\[
T_{h,R}^{[X,2X]}(X)
=
C_h^{[X,2X]}(X)
-
C_{h,\le R}^{[X,2X]}(X)
\]

and its Fejér average

\[
\mathcal T_{X,H,R}
=
\frac1L
\left[
T_{0,R}
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
T_{h,R}
\right].
\]

Since

\[
\mathcal T_{X,H,R}
=
\mathcal C_{X,H}
-
\mathcal C_{X,H,\le R},
\]

Sections 4 and 5 give the unconditional conclusion

\[
\boxed{
\mathcal T_{X,H,X^{1/3}}
=
o(X)
}
\]

uniformly in the declared long-window range

\[
\boxed{
X^{1/6+\varepsilon}
\le
H+1
\le
X^{1-\delta}.
}
\]

This closes the Fejér-averaged high-divisor tail in that range.

## 7. Why this does not prove twin primes

The statement is averaged in the additive displacement \(h\).

It does not imply

\[
T_{2,R}(X)=o(X)
\]

or

\[
\sum_{n\le X}\Lambda(n)\Lambda(n+2)
\sim
2C_2X.
\]

No fixed-shift Hardy–Littlewood occurrence asymptotic is derived.

The averaging is essential.

## 8. Consequence for phase spectroscopy

The arithmetic obstruction to the forced form-factor law is now range-dependent.

For additive shift windows satisfying

\[
H\gtrsim X^{1/6+\varepsilon},
\]

the high-divisor tail is asymptotically negligible after Fejér averaging, using standard unconditional prime-distribution input.

Therefore the unresolved phase-spectroscopy gate moves to shorter/more localized windows:

\[
\boxed{
H<X^{1/6+\varepsilon}
}
\]

or to window geometries not controlled by the classical Selberg-integral theorem.

This is much narrower than a general fixed-\(h\) prime-pair correlation problem.

## 9. Prior-art boundary

The key analytic estimate in Section 3 is standard external mathematics. This repository does not claim a new proof of the Saffari–Vaughan short-interval theorem.

The repository-specific contribution in this chain is the exact alignment:

\[
\text{Fejér spectral power}
\leftrightarrow
\text{shift average}
\leftrightarrow
\text{Möbius--CRT phase block}
\leftrightarrow
\text{high-divisor tail},
\]

which allows the standard short-interval theorem to close precisely the averaged tail needed by the phase-spectroscopy route in its valid range.

Goldston–Montgomery's classical pair-correlation/short-interval equivalence remains the broader external context.

## 10. New frontier

### OP-F29 — shorter-window averaged tail

Extend

\[
\mathcal T_{X,H,X^{1/3}}=o(X)
\]

below the classical unconditional threshold

\[
H\ge X^{1/6+\varepsilon},
\]

or adapt the proof to the exact smooth/logarithmic window induced by the \(q(T)\)-scaled explicit formula.

Admissible tools include:
- sharper zero-density estimates;
- large-sieve/dispersion estimates;
- Vaughan or Heath–Brown identities;
- smooth Selberg-integral variants;
- an operator identity avoiding direct short-interval estimates.

Any RH-dependent improvement must be typed explicitly and cannot be used circularly if RH is itself the target.

## 11. Compact theorem

### Theorem — unconditional long-window averaged-tail closure

Let \(L=H+1\) and fix \(\varepsilon,\delta>0\). Suppose

\[
X^{1/6+\varepsilon}
\le
L
\le
X^{1-\delta}.
\]

Set

\[
R=X^{1/3}.
\]

Using the standard unconditional Saffari–Vaughan short-interval mean-square theorem and the exact Fejér/Möbius–CRT low-block theorem,

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}\to1,
\qquad
\frac{\mathcal C_{X,H,\le R}}{X}\to1,
}
\]

and hence

\[
\boxed{
\frac{\mathcal T_{X,H,R}}{X}\to0.
}
\]

No fixed-shift prime-pair asymptotic is assumed or proved. Q.E.D. from the stated standard input.
