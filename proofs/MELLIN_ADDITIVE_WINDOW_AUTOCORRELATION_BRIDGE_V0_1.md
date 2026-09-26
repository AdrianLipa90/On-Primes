# Mellin Pullback and Additive-Window Autocorrelation Bridge v0.1

Status: **EXACT_WINDOW_COORDINATE_BRIDGE / EXACT_TRANSLATION_AUTOCORRELATION / SHORT-SCALE_ANALYTIC_BOUND_OPEN**

Date: 2026-09-26

Parents:
- \`proofs/PHASE_BANK_FORM_FACTOR_DUALITY_V0_1.md\`
- \`proofs/FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1.md\`
- \`proofs/FEJER_AVERAGED_HIGH_TAIL_LONG_WINDOW_V0_1.md\`

## 1. Problem

The explicit formula naturally samples prime powers through a function of the logarithmic coordinate

\[
t=\log n,
\]

whereas the short-interval / shifted-correlation analysis is naturally written in the additive integer coordinate \(n\).

This section shows that there is no representational obstruction between these windows.

## 2. Exact Mellin pullback

Let

\[
v:(0,\infty)\to\mathbb C
\]

be a smooth arithmetic window for which the following transforms are admissible; in particular \(v\in C_c^\infty((0,\infty))\) is sufficient.

Define the logarithmic window

\[
\boxed{
G_v(t)
=
e^{t/2}v(e^t).
}
\]

Then for every integer \(n\ge1\),

\[
\boxed{
\frac{1}{\sqrt n}
G_v(\log n)
=
v(n).
}
\]

Therefore the standard prime-side explicit-formula coefficient

\[
\frac{\Lambda(n)}{\sqrt n}G_v(\log n)
\]

is exactly

\[
\boxed{
\Lambda(n)v(n).
}
\]

Thus any declared smooth additive arithmetic window can be pulled back exactly to a logarithmic explicit-formula test weight.

No approximation is involved in this coordinate identity.

If the explicit-formula convention places the prime weight at \(\widehat h(\log n/2\pi)\), one simply uses the rescaled transform

\[
\widehat h(u)
=
G_v(2\pi u).
\]

For compactly supported smooth \(G_v\), the inverse Fourier transform \(h\) is Schwartz, so the construction lies in the usual smooth test-function setting.

## 3. Translated/scaled additive windows

Let

\[
V\in L^2(\mathbb R)
\]

and define

\[
v_{Q,L}(x)
=
V\!\left(
\frac{x-Q}{L}
\right),
\qquad
L>0.
\]

The corresponding logarithmic test is

\[
G_{Q,L}(t)
=
e^{t/2}
V\!\left(
\frac{e^t-Q}{L}
\right).
\]

Hence

\[
\frac{\Lambda(n)}{\sqrt n}
G_{Q,L}(\log n)
=
\Lambda(n)
V\!\left(
\frac{n-Q}{L}
\right).
\]

This is an exact explicit-formula realization of an additive window centered at \(Q\) with scale \(L\).

## 4. Exact translation-averaged pair kernel

Define the window autocorrelation

\[
\boxed{
K_V(s)
=
\int_{\mathbb R}
V(u)\overline{V(u+s)}\,du.
}
\]

For any \(n,m>0\),

\[
\int_{\mathbb R}
v_{Q,L}(n)
\overline{v_{Q,L}(m)}
\,dQ
\]

equals, after the change of variable

\[
u=\frac{n-Q}{L},
\]

the exact expression

\[
\boxed{
L
K_V\!\left(
\frac{m-n}{L}
\right).
}
\]

Therefore, for any finite arithmetic coefficients \(a_n\),

\[
\boxed{
\int_{\mathbb R}
\left|
\sum_n
a_n
V\!\left(
\frac{n-Q}{L}
\right)
\right|^2
dQ
=
L
\sum_{n,m}
a_n\overline{a_m}
K_V\!\left(
\frac{m-n}{L}
\right).
}
\]

Grouping by the additive shift \(h=m-n\),

\[
\boxed{
=
L
\sum_h
K_V(h/L)
\sum_n
a_n\overline{a_{n+h}}.
}
\]

For

\[
a_n=\Lambda(n),
\]

the right-hand side is precisely a smooth weighted average of shifted von Mangoldt correlations.

Thus the windowed explicit-formula pair power and the additive-shift correlation are joined by an exact translation-autocorrelation identity.

## 5. Positivity

By Wiener–Khintchine,

\[
\boxed{
\widehat{K_V}(\xi)
=
|\widehat V(\xi)|^2
\ge0
}
\]

under the matching Fourier convention.

Hence every kernel obtained in this way is positive definite and is naturally a spectral-power weighting.

This is exactly the structural property required by the phase-spectroscopy form-factor observable.

## 6. Fejér kernel as the rectangular-window limit

Take formally

\[
V_\square(u)=\mathbf1_{[0,1]}(u).
\]

Then

\[
\boxed{
K_{V_\square}(s)
=
(1-|s|)_+.
}
\]

Thus

\[
K_{V_\square}(h/L)
=
\left(
1-\frac{|h|}{L}
\right)_+,
\]

which is the Fejér triangular shift weight.

The sharp rectangle is not the preferred smooth explicit-formula test, but it can be approximated by smooth windows.

## 7. Uniform smooth approximation of the Fejér shift kernel

Let

\[
V_\eta\in C_c^\infty(\mathbb R)
\]

satisfy

\[
\|V_\eta-V_\square\|_2\to0.
\]

For any \(V,W\in L^2\),

\[
K_V(s)-K_W(s)
=
\langle V,\tau_s V\rangle
-
\langle W,\tau_s W\rangle.
\]

Add and subtract \(\langle V,\tau_s W\rangle\). By Cauchy–Schwarz and unitarity of translation,

\[
\boxed{
\|K_V-K_W\|_\infty
\le
(\|V\|_2+\|W\|_2)
\|V-W\|_2.
}
\]

Therefore

\[
\boxed{
K_{V_\eta}(s)
\to
(1-|s|)_+
}
\]

uniformly in \(s\).

So the exact Fejér shift kernel is the uniform autocorrelation limit of admissible smooth explicit-formula windows.

## 8. Gaussian witness

For the smooth Gaussian

\[
V_G(u)=e^{-u^2/2},
\]

one has exactly

\[
\boxed{
K_{V_G}(s)
=
\sqrt\pi\,e^{-s^2/4}.
}
\]

Thus a Gaussian explicit-formula window produces a Gaussian additive-shift correlation kernel with no coordinate approximation.

This is useful for numerical and analytic spectroscopy where a smooth window is preferable to a sharp interval.

## 9. Consequence for the current frontier

The distinction

\[
\text{logarithmic explicit-formula window}
\quad\text{vs}\quad
\text{additive short-interval window}
\]

is now closed at the representation level.

Any smooth additive window can be encoded exactly through the Mellin/log pullback, and its translated pair power produces its exact additive autocorrelation kernel.

Therefore the remaining OP-F29 difficulty is not window coordinates. It is the analytic estimate for the corresponding averaged prime correlation at short scale.

The long-window Saffari–Vaughan closure applies directly to the sharp Fejér model and, after the appropriate stability estimate, to sufficiently close smooth approximants in its valid scale range.

## 10. Firewall

This theorem does not:
- prove a new explicit formula;
- improve the Saffari–Vaughan short-interval exponent;
- prove fixed-shift Hardy–Littlewood;
- prove the zeta plateau;
- prove RH.

It closes only the exact coordinate/window bridge.

## 11. New frontier

### OP-F30 — smooth short-window mean-square extension

For the exact smooth kernel \(K_V(h/L)\) induced by a declared explicit-formula test \(V\), prove the required averaged high-tail estimate below the current unconditional long-window threshold.

A successful theorem should state:
- regularity and support/decay of \(V\);
- the scale \(L=L(X)\);
- uniformity in spectral modulation;
- the prime-power terms;
- the relevant Selberg/dispersion norm;
- every conditional assumption.

## 12. Compact theorem

### Theorem — Mellin/additive window equivalence

Let \(v\in C_c^\infty((0,\infty))\) and define

\[
G_v(t)=e^{t/2}v(e^t).
\]

Then

\[
\boxed{
\Lambda(n)n^{-1/2}G_v(\log n)
=
\Lambda(n)v(n)
}
\]

for every \(n\ge1\).

For

\[
v_{Q,L}(x)=V((x-Q)/L),
\]

translation averaging gives

\[
\boxed{
\int_{\mathbb R}
\left|
\sum_n a_n v_{Q,L}(n)
\right|^2dQ
=
L
\sum_h
K_V(h/L)
\sum_n
a_n\overline{a_{n+h}},
}
\]

where

\[
K_V(s)=\int V(u)\overline{V(u+s)}\,du.
\]

Moreover,

\[
\widehat K_V=|\widehat V|^2\ge0.
\]

For the rectangular limit \(V=\mathbf1_{[0,1]}\),

\[
K_V(s)=(1-|s|)_+,
\]

the Fejér shift kernel. Q.E.D.
