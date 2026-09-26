# RH-Conditional Fejér Averaged-Tail Validation Envelope v0.1

Status: **STANDARD_RH_CONDITIONAL_INPUT / VALIDATION_ONLY / NOT_ADMISSIBLE_AS_RH_PROOF_PREMISE**

Date: 2026-09-26

Parents:
- \`proofs/FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1.md\`
- \`proofs/FEJER_AVERAGED_HIGH_TAIL_LONG_WINDOW_V0_1.md\`
- \`proofs/MELLIN_ADDITIVE_WINDOW_AUTOCORRELATION_BRIDGE_V0_1.md\`

## 1. External conditional input

A classical Saffari–Vaughan/Selberg short-interval mean-square bound under the Riemann Hypothesis has the form

\[
\boxed{
\frac1X
\int_0^X
\left|
\sum_{x<n\le x+H}\Lambda(n)-H
\right|^2dx
\ll
H\left(
1+\log\frac{X}{H}
\right)^2
}
\]

uniformly in the standard range \(1\le H\le X\).

Equivalently,

\[
J(X,H)
\ll
XH
\left(
1+\log\frac{X}{H}
\right)^2.
\]

This is standard external mathematics and is not reproved here.

## 2. Condition for relative mean-square decay

Divide by the square main scale \(XH^2\):

\[
\frac{J(X,H)}{XH^2}
\ll
\frac{
(1+\log(X/H))^2
}{H}.
\]

Therefore

\[
\boxed{
\frac{H}{
(1+\log(X/H))^2
}
\to\infty
}
\]

implies

\[
J(X,H)=o(XH^2).
\]

A simple sufficient condition is

\[
H/\log^2X\to\infty.
\]

## 3. Full Fejér correlation under RH

The finite Fejér/sliding-window crosswalk from the unconditional theorem remains exact.

If additionally

\[
H\log^2X=o(X),
\]

the boundary mismatch is \(o(XH^2)\).

Hence under RH,

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}\to1
}
\]

whenever

\[
\frac{H}{
(1+\log(X/H))^2
}
\to\infty
\]

and

\[
H\log^2X=o(X).
\]

## 4. Low block on the same scale

Choose

\[
\boxed{
R=H^{1/2}.
}
\]

Then

\[
R\to\infty
\]

whenever \(H\to\infty\), and

\[
\frac{
R\log^2R
}{
H^2
}
=
O\!\left(
\frac{\log^2H}{H^{3/2}}
\right)
\to0.
\]

Also

\[
\frac{
(R\log R)^2
}{
X
}
=
O\!\left(
\frac{H\log^2H}{X}
\right).
\]

Thus under the same sublinear boundary condition

\[
H\log^2X=o(X),
\]

the Fejér-averaged Möbius–CRT low block satisfies

\[
\boxed{
\frac{\mathcal C_{X,H,\le H^{1/2}}}{X}\to1.
}
\]

## 5. Conditional high-tail closure

Subtracting the low block from the full averaged correlation gives

\[
\boxed{
\frac{
\mathcal T_{X,H,H^{1/2}}
}{
X
}
\to0
}
\]

under RH provided

\[
\boxed{
\frac{H}{
(1+\log(X/H))^2
}
\to\infty,
\qquad
H\log^2X=o(X).
}
\]

For example, every regime

\[
\log^{2+\eta}X
\le
H
\le
\frac{X}{\log^{2+\eta}X},
\qquad
\eta>0,
\]

lies safely inside this validation envelope for large \(X\).

## 6. Meaning for the forced phase-spectroscopy law

The internal projector/CAR cage already forces the sine-kernel/ramp pair without RH.

The theorem here says that, **if RH is assumed externally**, classical short-interval arithmetic is consistent with the averaged-tail vanishing needed to transfer that form-factor structure down to polylogarithmic additive windows.

This is strong validation of compatibility.

It is not an independent derivation of RH.

## 7. Hard firewall

If RH is the target theorem, the implication

\[
\text{RH}
\Longrightarrow
\mathcal T=o(X)
\]

cannot be used in the reverse direction without an independently proved equivalence whose converse hypotheses are explicitly checked.

Therefore this entire document is tagged:

\[
\boxed{
\texttt{RH\_CONDITIONAL\_VALIDATION\_ONLY}.
}
\]

It may be used to:
- benchmark the framework;
- verify normalization and scaling;
- compare conditional predictions;
- identify which short-window regime remains genuinely difficult.

It may not be used as a premise in a claimed proof of RH.

## 8. Refined frontier

Unconditionally, the current averaged high-tail closure begins at

\[
H\ge X^{1/6+\varepsilon}.
\]

Conditionally on RH, the validation envelope extends to

\[
H\gg(1+\log(X/H))^2.
\]

Thus the noncircular analytic target is sharply separated from the conditional validation region.

## 9. Compact conditional theorem

### Theorem — RH-conditional averaged-tail validation range

Assume RH and the standard Saffari–Vaughan short-interval mean-square bound. If

\[
\frac{H}{
(1+\log(X/H))^2
}
\to\infty
\]

and

\[
H\log^2X=o(X),
\]

then with \(R=H^{1/2}\),

\[
\boxed{
\frac{\mathcal C_{X,H}}{X}\to1,
\qquad
\frac{\mathcal C_{X,H,\le R}}{X}\to1,
\qquad
\frac{\mathcal T_{X,H,R}}{X}\to0.
}
\]

This conclusion is conditional validation only. Q.E.D. from the stated RH input.
