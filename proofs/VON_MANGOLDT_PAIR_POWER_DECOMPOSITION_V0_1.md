# Windowed von Mangoldt Pair-Power Decomposition v0.1

Status: **EXACT_FINITE_ARITHMETIC_DECOMPOSITION / EXPLICIT_FORMULA_CROSSWALK / HARDY_LITTLEWOOD_OCCURRENCE_GATE_OPEN**

Date: 2026-09-26

Parents:
- \`proofs/PHASE_BANK_FORM_FACTOR_DUALITY_V0_1.md\`
- \`SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1.md\`
- existing ARPL singular-series phase bridge.

## 1. Purpose

The previous phase-bank/form-factor theorem closed the exact frequency coordinate

\[
\tau_q(T)=\frac{\log q}{\log(T/2\pi)}
\]

and the finite identity

\[
K_{\Gamma,T}(\tau_q)=N|R_q|^2.
\]

The next question is what appears on the arithmetic side when a smoothed explicit-formula amplitude is squared to obtain pair power.

The answer is exact at finite cutoff: the off-diagonal term is a shifted von Mangoldt correlation.

## 2. Finite arithmetic amplitude

Let \(Q\ge2\) be a finite cutoff and let

\[
b_n=b(n;\omega,w)
\]

be any complex analysis weight. For the explicit-formula application one may take schematically

\[
b_n
=
\frac{\Lambda(n)}{\sqrt n}\,
W_\omega(\log n),
\]

where \(W_\omega\) is a shifted Fourier window obtained from a modulated test function.

Define

\[
A_Q=\sum_{n\le Q} b_n.
\]

Then

\[
|A_Q|^2
=
\sum_{n,m\le Q}
b_n\overline{b_m}.
\]

## 3. Exact diagonal/off-diagonal split

Separate \(m=n\) from \(m\ne n\):

\[
\boxed{
|A_Q|^2
=
D_Q+O_Q,
}
\]

where

\[
D_Q
=
\sum_{n\le Q}|b_n|^2
\]

and

\[
O_Q
=
\sum_{\substack{n,m\le Q\\n\ne m}}
b_n\overline{b_m}.
\]

For the von Mangoldt weights,

\[
D_Q
=
\sum_{n\le Q}
\frac{\Lambda(n)^2}{n}
|W_\omega(\log n)|^2.
\]

This is the arithmetic diagonal.

## 4. Shift decomposition

Group the off-diagonal by the additive displacement

\[
h=m-n.
\]

Then exactly

\[
\boxed{
O_Q
=
2\Re
\sum_{h=1}^{Q-1}
\sum_{n\le Q-h}
b_n\overline{b_{n+h}}.
}
\]

For

\[
b_n
=
\frac{\Lambda(n)}{\sqrt n}W_\omega(\log n),
\]

this becomes

\[
\boxed{
O_Q
=
2\Re
\sum_{h=1}^{Q-1}
\sum_{n\le Q-h}
\frac{\Lambda(n)\Lambda(n+h)}
{\sqrt{n(n+h)}}
W_\omega(\log n)
\overline{W_\omega(\log(n+h))}.
}
\]

Thus the full pair power is controlled by weighted shifted correlations of the von Mangoldt function.

No Hardy--Littlewood asymptotic has been assumed.

## 5. Explicit-formula interpretation

For a smooth test function \(g\), the smoothed explicit formula linearly relates a zero-side spectral sum to the prime-power measure

\[
\sum_n\frac{\Lambda(n)}{\sqrt n}\,
g(\log n)
\]

plus the declared pole/trivial-zero/archimedean terms.

Modulating the zero-side test by a phase \(e^{i\omega t}\) shifts the Fourier window on the prime side. Consequently, when the corresponding spectral amplitude is squared, the prime-side quadratic contribution necessarily contains the exact shifted-von-Mangoldt kernel of Section 4, together with the squared/crossed archimedean and pole terms.

Therefore the transition

\[
\text{linear explicit formula}
\longrightarrow
\text{spectral pair power}
\]

is not closed by the one-point prime-power spectrum alone. It requires arithmetic two-point control.

## 6. Montgomery scaling

The previous crosswalk gives

\[
\omega
\sim
\tau\log(T/2\pi).
\]

A window localized near \(\omega\) therefore selects prime powers with

\[
\log n\approx\omega,
\qquad
n\approx(T/2\pi)^\tau.
\]

This is precisely why fixed \(n\) / fixed \(q\) Landau asymptotics cannot by themselves determine a fixed nonzero point of the form-factor ramp.

The relevant arithmetic regime moves with \(T\).

## 7. Relation to the classical Montgomery obstruction

In Montgomery's original pair-correlation analysis, the subcritical range is accessible because the troublesome nondiagonal terms remain below the main term in the relevant regime. Beyond that range, multiplying out the prime-side Dirichlet-polynomial expression exposes sums of the type

\[
\sum_{n\le y}\Lambda(n)\Lambda(n+h).
\]

The finite identity above identifies the same structural obstruction without importing the target form factor.

This is a crosswalk to standard prior art, not a novelty claim for the diagonal/off-diagonal algebra.

## 8. ARPL contribution

ARPL already supplies an exact phase representation of the Hardy--Littlewood **local factor** for a prime-pair displacement \(h\):

\[
h
\mapsto
(h\bmod p)_p
\mapsto
c_p(h)
\mapsto
\mathfrak S_P(h).
\]

Therefore the local singular-series weight associated with a displacement is already representable inside the phase algebra.

But this does not prove the occurrence asymptotic

\[
\sum_{n\le x}
\Lambda(n)\Lambda(n+h)
\sim
\mathfrak S(h)x.
\]

For \(h=2\), such a positive main-term asymptotic is already far stronger than anything presently proved about twin primes.

Hence the singular-series phase representation and the shifted von Mangoldt occurrence theorem must remain separate.

## 9. Exact no-go

The following shortcut is invalid:

\[
\boxed{
\text{ARPL represents }\mathfrak S(h)
\;\not\Rightarrow\;
\sum_{n\le x}\Lambda(n)\Lambda(n+h)
\sim\mathfrak S(h)x.
}
\]

Representing the expected local density is not the same as proving that the arithmetic sequence realizes that density.

Likewise,

\[
\boxed{
\text{forced projector ramp}
\;\not\Rightarrow\;
\text{zeta plateau}
}
\]

until the shifted arithmetic correlation or an equivalent noncircular operator theorem is supplied.

## 10. Refined research gate

### OP-F25 — smoothed shifted-von-Mangoldt correlation closure

Construct, for the \(q(T)\)-scaled window required by the form-factor coordinate, a rigorous asymptotic for

\[
C_{T,h}
=
\sum_n
\frac{\Lambda(n)\Lambda(n+h)}
{\sqrt{n(n+h)}}
W_T(\log n)
\overline{W_T(\log(n+h))}
\]

with:
- explicit smoothing;
- explicit support growth;
- uniform tail control;
- separation of prime powers from primes where needed;
- no insertion of the Hardy--Littlewood main term as an assumption;
- exact tracking of every RH-dependent step.

A weaker sufficient closure is any zero-list-free operator identity that controls the same off-diagonal pair power without evaluating each \(C_{T,h}\) separately.

## 11. Compact theorem

### Theorem — finite von Mangoldt pair-power decomposition

For any finite cutoff \(Q\) and weights

\[
b_n=\frac{\Lambda(n)}{\sqrt n}W(\log n),
\]

one has exactly

\[
\boxed{
\left|\sum_{n\le Q}b_n\right|^2
=
\sum_{n\le Q}|b_n|^2
+
2\Re
\sum_{h=1}^{Q-1}
\sum_{n\le Q-h}
b_n\overline{b_{n+h}}.
}
\]

Therefore the off-diagonal arithmetic content of a squared explicit-formula amplitude is a weighted shifted von Mangoldt correlation. Q.E.D.

The algebraic identity is exact. Any asymptotic replacement of the inner correlation by a Hardy--Littlewood singular-series main term remains an independent analytic number-theory claim.
