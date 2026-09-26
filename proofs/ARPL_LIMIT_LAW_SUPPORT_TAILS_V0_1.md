# ARPL Limiting-Law Support and Rapid Tails v0.1

Status: exact consequences of the instantaneous factorization and the all-real/entire moment theorem.

## 1. Positive amplitude law

For admissible

\[
h\ge6,\qquad 6\mid h,
\]

write

\[
\mathfrak S(H_{2^rh})
=
A(h)R_r(h),
\]

where

\[
A(h)
=
\frac{27}{2}C_*Z(h)>0
\]

and

\[
R_r(h)
=
\prod_{p\ge5}
\left(\frac{p-3}{p-4}\right)^{E_p(r;h)}.
\]

Every local dynamic multiplier is at least \(1\), hence

\[
\boxed{
R_r(h)\ge1
}
\]

for every \(r\).

## 2. Hard lower support edge — OP-D118

For every dyadic time,

\[
\boxed{
\mathfrak S(H_{2^rh})\ge A(h).
}
\]

Let \(\mu_h\) be the limiting amplitude law and \(\nu_h\) the limiting law of the logarithm.

Since every empirical amplitude measure is supported on the closed set

\[
[A(h),\infty),
\]

weak convergence gives

\[
\boxed{
\mu_h([A(h),\infty))=1.
}
\]

Equivalently,

\[
\boxed{
\nu_h([\log A(h),\infty))=1.
}
\]

Thus the limiting log-amplitude law has a finite hard lower edge.

No statement is made here about whether the lower edge itself is an atom or belongs to the topological support.

## 3. Faster-than-any-power upper tail — OP-D119

For every real \(s>0\), the entire moment theorem gives

\[
\mathcal M_h(s)
=
\int x^s\,d\mu_h(x)
<\infty.
\]

Markov's inequality therefore gives

\[
\boxed{
\mu_h([x,\infty))
\le
\frac{\mathcal M_h(s)}{x^s}
\qquad(x>0).
}
\]

Since \(s\) is arbitrary, for every \(N>0\),

\[
\boxed{
\mu_h([x,\infty))
=
O_{h,N}(x^{-N})
\qquad(x\to\infty).
}
\]

Thus the amplitude tail is smaller than every fixed inverse power.

This is a tail-probability statement. It does not assert existence or rapid decay of a probability density.

## 4. Faster-than-any-fixed-exponential log tail — OP-D120

For

\[
Y=\log X\sim\nu_h,
\]

the event \(Y\ge y\) equals \(X\ge e^y\). Hence, for every \(N>0\),

\[
\boxed{
\nu_h([y,\infty))
\le
\mathcal M_h(N)e^{-Ny}.
}
\]

Therefore

\[
\boxed{
\nu_h([y,\infty))
=
O_{h,N}(e^{-Ny})
\qquad(y\to\infty)
}
\]

for every fixed \(N>0\).

Equivalently, the upper log tail decays faster than any prescribed fixed exponential rate.

Again, this does not assert a large-deviation principle or a density asymptotic.

## 5. Negative moments

Because

\[
X\ge A(h)>0,
\]

all negative amplitude moments obey the elementary bound

\[
X^{-s}\le A(h)^{-s}
\qquad(s>0).
\]

Thus finiteness of negative real moments is also immediate from the hard lower edge, independently of the stronger entire-transform theorem.

## 6. Dyadic invariance

The entire limiting law and the static factor \(A(h)\) are invariant under

\[
h\mapsto2^kh.
\]

Therefore the hard lower edge and every rapid-tail family above are dyadic-orbit invariants.

## 7. What remains open

These results do not determine whether \(\mu_h\) or \(\nu_h\) is:

- atomic;
- non-atomic;
- absolutely continuous;
- singular-continuous.

They sharply constrain the possible law without deciding its measure type.
