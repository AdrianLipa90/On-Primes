# Shifted von Mangoldt CRT–Phase Decomposition v0.1

Status: **EXACT_FINITE_IDENTITY / EXACT_CRT_PHASE_GATE / ASYMPTOTIC_CANCELLATION_OPEN**

Date: 2026-09-26

Parents:
- \`proofs/VON_MANGOLDT_PAIR_POWER_DECOMPOSITION_V0_1.md\`
- ARPL modular phase law and CRT signature.
- ARPL singular-series phase bridge.

## 1. Starting identity

For every integer \(n\ge1\),

\[
\boxed{
\Lambda(n)
=
-\sum_{d\mid n}\mu(d)\log d.
}
\]

This is the standard Möbius inversion of

\[
\log n=\sum_{d\mid n}\Lambda(d).
\]

Fix \(X\ge1\) and an integer shift \(h\ge0\). Define the finite shifted correlation

\[
C_h(X)
=
\sum_{n\le X}
\Lambda(n)\Lambda(n+h).
\]

## 2. Exact double-divisor expansion

Substituting the Möbius representation twice gives

\[
C_h(X)
=
\sum_{n\le X}
\sum_{d\mid n}
\sum_{e\mid n+h}
\mu(d)\mu(e)\log d\log e.
\]

All sums are finite, so the order may be exchanged exactly:

\[
\boxed{
C_h(X)
=
\sum_{d\le X}
\sum_{e\le X+h}
\mu(d)\mu(e)\log d\log e\,
N_{d,e}(X;h),
}
\]

where

\[
N_{d,e}(X;h)
=
\#\{
1\le n\le X:
d\mid n,\ e\mid n+h
\}.
\]

No prime-pair conjecture is used.

## 3. CRT compatibility gate

The congruence system is

\[
n\equiv0\pmod d,
\qquad
n\equiv-h\pmod e.
\]

Let

\[
g=\gcd(d,e).
\]

By the generalized Chinese remainder theorem, this system is solvable iff

\[
0\equiv-h\pmod g,
\]

i.e.

\[
\boxed{
g\mid h.
}
\]

If \(g\nmid h\), then

\[
N_{d,e}(X;h)=0.
\]

If \(g\mid h\), the solution is one residue class modulo

\[
\ell=\operatorname{lcm}(d,e).
\]

Let \(r_{d,e}(h)\in\{1,\ldots,\ell\}\) be its least positive representative. Then

\[
\boxed{
N_{d,e}(X;h)
=
\max\left(
0,
1+\left\lfloor
\frac{X-r_{d,e}(h)}{\ell}
\right\rfloor
\right).
}
\]

Thus the entire finite shifted von Mangoldt correlation is an exact weighted sum over compatible modular relation pairs.

## 4. ARPL phase form of the compatibility gate

For \(g\ge1\), define the canonical additive character

\[
\chi_g(h)
=
e^{2\pi i h/g}.
\]

Since \(h\in\mathbb Z\),

\[
\chi_g(h)=1
\iff
g\mid h.
\]

Therefore the CRT solvability condition is exactly the ARPL phase-lock condition

\[
\boxed{
\chi_{\gcd(d,e)}(h)=1.
}
\]

This is the direct zero-list-free bridge:

\[
\boxed{
\Lambda(n)\Lambda(n+h)
\longrightarrow
(d,e)
\longrightarrow
\gcd(d,e)\mid h
\longleftrightarrow
\text{phase lock}.
}
\]

The phase layer is not an analogy; it is the character representation of the exact CRT compatibility condition.

## 5. Exact periodicity of each divisor-pair channel

For fixed \(d,e\), the compatibility indicator

\[
\mathbf1_{\gcd(d,e)\mid h}
\]

is periodic in \(h\) modulo \(\gcd(d,e)\).

When compatible, the CRT residue \(r_{d,e}(h)\) depends only on \(h\bmod \ell\), where

\[
\ell=\operatorname{lcm}(d,e).
\]

Hence every individual divisor-pair contribution is a finite modular phase channel.

The full finite correlation is therefore a superposition of explicitly weighted modular channels.

## 6. Why this is stronger than the singular-series crosswalk

The earlier ARPL bridge represented the standard Hardy--Littlewood local singular factor as a function of the residue state of \(h\).

The present theorem begins instead from the **actual finite von Mangoldt correlation** and decomposes it exactly into CRT-compatible divisor channels.

This removes one representational gap:

\[
\text{actual }\Lambda\Lambda\text{ correlation}
\to
\text{exact modular relation sum}
\]

is now closed at finite \(X\).

What remains open is the asymptotic cancellation among the signed Möbius-weighted channels as \(X\to\infty\).

## 7. Main-term temptation and no-go

For a compatible pair one has

\[
N_{d,e}(X;h)
=
\frac{X}{\operatorname{lcm}(d,e)}
+
O(1).
\]

Formally inserting only the density term suggests a double arithmetic series

\[
X
\sum_{\gcd(d,e)\mid h}
\frac{
\mu(d)\mu(e)\log d\log e
}{
\operatorname{lcm}(d,e)
}.
\]

But this expression cannot be promoted by termwise absolute estimates: the Möbius signs and the growing divisor ranges carry essential cancellation.

Thus the shortcut

\[
N_{d,e}
\rightsquigarrow
X/\operatorname{lcm}(d,e)
\]

inside the full growing double sum requires an independent uniform truncation/cancellation theorem.

It is not supplied by CRT or phase representation alone.

## 8. Relation to the Hardy–Littlewood singular series

The condition

\[
\gcd(d,e)\mid h
\]

is the exact modular skeleton from which the shift dependence arises.

After appropriate analytic resummation/sieving one expects the familiar prime-pair local factors. However, identifying the full asymptotic coefficient with the Hardy--Littlewood singular series is a separate theorem/conjecture-level step.

For \(h=2\), any proof of a positive linear main term for

\[
C_2(X)
=
\sum_{n\le X}
\Lambda(n)\Lambda(n+2)
\]

would have major consequences for twin-prime occurrence.

Accordingly this repository does not replace the exact finite CRT sum by a conjectural asymptotic.

## 9. Refined gate

### OP-F26 — Möbius–CRT cancellation theorem

Starting from

\[
C_h(X)
=
\sum_{d,e}
\mu(d)\mu(e)\log d\log e\,
N_{d,e}(X;h),
\]

derive a controlled asymptotic by proving sufficient cancellation/uniformity in the growing \((d,e)\) domain.

A successful theorem must specify:
- truncation scales in \(d,e\);
- treatment of the \(O(1)\) counting remainder;
- uniformity in the shift range relevant to \(q(T)\)-scaled form-factor windows;
- how prime powers are handled;
- every use of zero-free regions, RH, sieve estimates, or distribution hypotheses.

A no-go theorem showing that a proposed absolute-majorant route cannot close the sum is also a valid result.

## 10. Compact theorem

### Theorem — finite shifted von Mangoldt CRT–phase decomposition

For integers \(X\ge1\) and \(h\ge0\),

\[
\boxed{
\sum_{n\le X}\Lambda(n)\Lambda(n+h)
=
\sum_{d\le X}
\sum_{e\le X+h}
\mu(d)\mu(e)\log d\log e\,
N_{d,e}(X;h),
}
\]

where \(N_{d,e}(X;h)\) counts the simultaneous congruences

\[
n\equiv0\pmod d,
\qquad
n\equiv-h\pmod e.
\]

Moreover,

\[
\boxed{
N_{d,e}(X;h)>0
\implies
\gcd(d,e)\mid h,
}
\]

and the congruence system is solvable iff

\[
\boxed{
\chi_{\gcd(d,e)}(h)=1.
}
\]

Thus the finite shifted von Mangoldt correlation has an exact modular-phase decomposition. Q.E.D.
