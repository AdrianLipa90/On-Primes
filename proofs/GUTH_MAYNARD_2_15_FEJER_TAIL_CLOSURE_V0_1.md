# Guth–Maynard 2/15 Fejér-Averaged Tail Closure v0.1

Status: **PROVED_FROM_STANDARD_GUTH_MAYNARD_2026 + EXACT_FEJER/MOBIUS_CRT / UNCONDITIONAL_RANGE_CLOSED**

Date: 2026-09-26

Parents:
- \`proofs/FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1.md\`
- \`proofs/FEJER_AVERAGED_HIGH_TAIL_LONG_WINDOW_V0_1.md\`
- \`proofs/MOBIUS_CRT_LOW_DIVISOR_PHASE_BLOCK_V0_1.md\`

External standard input:
- Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), 623--675, DOI 10.4007/annals.2026.203.2.6.
- Their Corollary 1.4 gives the prime number theorem in almost all short intervals for
  \[
  y\ge X^{2/15+\varepsilon}.
  \]
- More importantly for this repository, Section 13.2 proves the corollary through a von-Mangoldt \(L^2\) estimate of the required short-interval error.

No RH is assumed in this external input.

## 1. Guth–Maynard mean-square input

Let

\[
L=y
\]

with

\[
\boxed{
X^{2/15+\varepsilon}
\le
L
\le
X^{0.99}.
}
\]

The proof of Guth–Maynard Corollary 1.4 supplies a bound of the form

\[
\boxed{
\int_X^{2X}
\left|
\sum_{x\le n<x+L}\Lambda(n)-L
\right|^2
dx
=
o(XL^2),
}
\]

indeed with a stretched-exponential saving in their stated range.

This is already a \(\Lambda/\psi\) statement. No theta-to-psi transfer is required for the modern lane.

## 2. Discrete sliding-window energy

For integer \(L\), away from measure-zero endpoints the function

\[
x\mapsto
\sum_{x<n\le x+L}\Lambda(n)
\]

is constant on each unit interval \([m,m+1)\), equal to

\[
S_L(m)
=
\sum_{j=1}^{L}\Lambda(m+j).
\]

Therefore

\[
\boxed{
\sum_{m=X}^{2X-1}
|S_L(m)-L|^2
=
\int_X^{2X}
|\psi(x+L)-\psi(x)-L|^2\,dx
}
\]

up to endpoint conventions of measure zero.

Hence Guth–Maynard yields

\[
\boxed{
\sum_{m=X}^{2X-1}
|S_L(m)-L|^2
=
o(XL^2).
}
\]

## 3. Full Fejér correlation average

As in the previous long-window theorem, define

\[
\mathcal C_{X,H}
=
\frac1L
\left[
C_0^{[X,2X]}(X)
+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)
C_h^{[X,2X]}(X)
\right],
\qquad
L=H+1.
\]

The exact sliding-window expansion gives

\[
\mathcal E_{X,L}
=
L^2\mathcal C_{X,H}
+
O(L^3\log^2(3X)),
\]

where

\[
\mathcal E_{X,L}
=
\sum_{m=X}^{2X-1}S_L(m)^2.
\]

The Guth–Maynard mean-square bound gives

\[
\mathcal E_{X,L}
=
XL^2+o(XL^2).
\]

Since

\[
L\le X^{0.99},
\]

we also have

\[
\frac{L^3\log^2X}{XL^2}
=
\frac{L\log^2X}{X}
=o(1).
\]

Thus

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}
\to1
}
\]

uniformly in every fixed-\(\varepsilon\) subrange

\[
X^{2/15+\varepsilon}
\le
H+1
\le
X^{0.99}.
\]

## 4. Low-divisor block at the new threshold

The Fejér/Möbius–CRT theorem requires

\[
(R\log R)^2=o(X)
\]

and

\[
R\log^2R=o(H^2).
\]

At the old \(1/6\) threshold one convenient choice was \(R=X^{1/3}\).

For the Guth–Maynard threshold choose instead

\[
\boxed{
R=X^{1/4}.
}
\]

Then

\[
\frac{(R\log R)^2}{X}
=
X^{-1/2}\log^2X
\to0.
\]

Moreover, for

\[
H+1\ge X^{2/15+\varepsilon},
\]

\[
\frac{R\log^2R}{H^2}
\ll
X^{1/4-4/15-2\varepsilon}\log^2X
=
X^{-1/60-2\varepsilon}\log^2X
\to0.
\]

Hence

\[
\boxed{
\frac{\mathcal C_{X,H,\le X^{1/4}}}{X}
\to1.
}
\]

## 5. Averaged high-tail closure down to \(2/15+\varepsilon\)

Define

\[
\mathcal T_{X,H,R}
=
\mathcal C_{X,H}
-
\mathcal C_{X,H,\le R}.
\]

Sections 3 and 4 imply

\[
\boxed{
\frac{
\mathcal T_{X,H,X^{1/4}}
}{X}
\to0
}
\]

unconditionally in the range

\[
\boxed{
X^{2/15+\varepsilon}
\le
H+1
\le
X^{0.99}.
}
\]

This strictly improves the previous \(X^{1/6+\varepsilon}\) closure.

## 6. What is and is not closed

### Closed

- exact Fejér shift averaging;
- exact Möbius–CRT low-block phase representation;
- low-block mean asymptotic;
- full Fejér correlation mean in the Guth–Maynard range;
- Fejér-averaged high-divisor tail \(o(X)\) in that range.

### Still open

- shorter windows
  \[
  H<X^{2/15+\varepsilon};
  \]
- the exact smooth/logarithmic window family produced by every desired \(q(T)\)-scaled test function;
- full zeta local-process/CAR occupancy binding;
- Montgomery plateau as a zeta theorem without importing the conjecture.

No fixed-\(h\) Hardy–Littlewood correlation is proved.

## 7. Why this is not a twin-prime shortcut

The theorem concerns the weighted shift average

\[
\frac1L
\left[
C_0+
2\sum_{h=1}^{H}
\left(1-\frac hL\right)C_h
\right].
\]

It does not isolate \(h=2\).

Therefore it does not imply a positive asymptotic for

\[
\sum_{n\le X}\Lambda(n)\Lambda(n+2)
\]

and makes no twin-prime claim.

## 8. Updated frontier

### OP-F30 — below-\(2/15\) or exact-test-function closure

The current unconditional averaged-tail barrier is now the modern Guth–Maynard almost-all scale.

The next valid targets are:

1. extend the averaged high-tail closure below
   \[
   H=X^{2/15+\varepsilon};
   \]
2. transfer the \(2/15\) result from triangular Fejér windows to the exact smooth/logarithmic test-function family required by the phase-spectroscopy explicit formula;
3. bypass short-interval estimates entirely through a zero-list-free operator/trace identity.

Any improvement using RH, density hypotheses stronger than currently proved, or Montgomery pair correlation must be typed as conditional validation rather than independent proof input.

## 9. Compact theorem

### Theorem — Guth–Maynard range averaged-tail closure

Fix \(\varepsilon>0\) and let

\[
X^{2/15+\varepsilon}
\le
L=H+1
\le
X^{0.99}.
\]

Set

\[
R=X^{1/4}.
\]

Then the standard Guth–Maynard 2026 von-Mangoldt mean-square input together with the exact Fejér/Möbius–CRT low-block theorem gives

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}\to1,
\qquad
\frac{\mathcal C_{X,H,\le R}}{X}\to1,
}
\]

and therefore

\[
\boxed{
\frac{\mathcal T_{X,H,R}}{X}\to0.
}
\]

Q.E.D. from the declared standard input.
