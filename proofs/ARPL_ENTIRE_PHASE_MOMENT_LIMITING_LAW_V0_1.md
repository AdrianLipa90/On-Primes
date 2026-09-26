# ARPL Entire Phase-Moment Transform and Limiting Law v0.1

Status: exact complex-moment theorem + limiting-distribution theorem for the dyadic two-twin-pair singular-series orbit. Standard analytic/probability machinery is explicitly separated from the ARPL specialization.

## 1. Setup

Fix an admissible separation

\[
h\ge6,\qquad 6\mid h.
\]

Write the already proved instantaneous factorization as

\[
\mathfrak S_r(h)
:=
\mathfrak S(H_{2^rh})
=
A(h)\,R_r(h),
\]

where

\[
A(h)=\frac{27}{2}C_*Z(h)>0
\]

and

\[
R_r(h)
=
\prod_{p\ge5}s_p^{E_p(r;h)},
\qquad
s_p=\frac{p-3}{p-4}>1.
\]

For each active odd-prime channel,

\[
E_p(r;h)
=
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}},
\qquad
e_p=\operatorname{ord}_p(4).
\]

Inactive channels have \(E_p\equiv0\).

For a finite compatible active set \(J\),

\[
\delta_J(h)
=
\frac1{\operatorname{lcm}_{p\in J}e_p},
\]

and incompatible \(J\) have \(\delta_J(h)=0\).

## 2. Complex channel multiplier — OP-D096

For

\[
z\in\mathbb C
\]

define

\[
\boxed{
b_p(z)
=
s_p^z-1
=
\exp(z\log s_p)-1,
}
\]

using the real logarithm of the positive number \(s_p\).

For every compact set \(K\subset\mathbb C\),

\[
\boxed{
\sup_{z\in K}|b_p(z)|
\ll_K \frac1p.
}
\]

Proof: if \(a_p=\log s_p\), then \(a_p=O(1/p)\), and

\[
|e^{za_p}-1|
\le
|z|a_p e^{|z|a_p}.
\]

Thus the bound is uniform on bounded \(z\)-sets.

## 3. Standard multiplicative-order input

Use the quantitative multiplicative-order theorem already recorded in the repository: there exist constants

\[
\alpha,\delta>0
\]

such that, outside a prime set with counting function

\[
O\!\left(\frac{x}{(\log x)^{1+\alpha}}\right),
\]

one has

\[
\operatorname{ord}_p(2)
\ge
p^{1/2}\exp((\log p)^\delta).
\]

Consequently

\[
e_p=\operatorname{ord}_p(4)
\ge
\frac12 p^{1/2}\exp((\log p)^\delta)
\]

on the good primes.

The exceptional/bad primes have finite reciprocal mass.

This is standard external number theory, not an ARPL result.

## 4. Locally uniform all-orders subset summability — OP-D097

Define formally

\[
F_h(z)
=
1+
\sum_{\varnothing\ne J}
\delta_J(h)
\prod_{p\in J}b_p(z).
\]

We prove that the series converges absolutely and uniformly on every compact \(K\subset\mathbb C\).

For the bad primes,

\[
\sum_{p\ {\rm bad}}
\sup_{z\in K}|b_p(z)|
<\infty,
\]

hence

\[
C_{\rm bad}(K)
=
\prod_{p\ {\rm bad}}
\left(
1+\sup_{z\in K}|b_p(z)|
\right)
<\infty.
\]

For a nonempty good subset \(G\), let

\[
q=\max G.
\]

For every bad addition \(B\),

\[
\delta_{G\cup B}(h)
\le
\frac1{e_q}
\ll
q^{-1/2}
\exp(-(\log q)^\delta).
\]

Also, uniformly on \(K\),

\[
|b_q(z)|\ll_K\frac1q
\]

and

\[
\prod_{\substack{p<q\\p\ {\rm good}}}
\left(1+\sup_{z\in K}|b_p(z)|\right)
\ll_K
(\log q)^{C_K}
\]

for some finite \(C_K\).

Thus the total contribution of subsets whose largest good prime is \(q\) is

\[
\ll_K
\frac{(\log q)^{C_K}}
{q^{3/2}}
\exp(-(\log q)^\delta),
\]

which is summable over primes \(q\).

Therefore

\[
\boxed{
\sum_{J\ne\varnothing}
\delta_J(h)
\sup_{z\in K}
\left|
\prod_{p\in J}b_p(z)
\right|
<\infty.
}
\]

By the Weierstrass theorem,

\[
\boxed{
F_h(z)\ \text{is entire}.
}
\]

## 5. Entire Cesaro phase-moment transform — OP-D098

For finite time \(T\), only primes dividing

\[
M_T(h)
=
\prod_{r=0}^{T-1}(4^rh^2-4)
\]

can occur.

For every complex \(z\),

\[
R_r(h)^z
=
\prod_p
\left(1+b_p(z)E_p(r;h)\right),
\]

and at each fixed \(r\) this product is finite.

The finite-horizon subset expansion has the standard endpoint error \(1/T\). On a compact disk \(|z|\le R\),

\[
1+|s_p^z-1|
\le
s_p^{|z|}
\le
s_p^R,
\]

because

\[
|e^w-1|\le e^{|w|}-1.
\]

Hence

\[
\prod_{p\mid M_T(h)}
\left(1+|b_p(z)|\right)
\le
R(M_T(h))^R.
\]

The divisor-weight bound gives

\[
R(M_T(h))
\ll_h
\log\log |M_T(h)|
\ll_h
\log(T+2),
\]

so the endpoint contribution is uniformly

\[
O_{h,R}\!\left(
\frac{(\log T)^R}{T}
\right)
\to0.
\]

Together with OP-D097 this gives locally uniform convergence in \(z\):

\[
\boxed{
\mathcal M_h(z)
=
\lim_{T\to\infty}
\frac1T
\sum_{r=0}^{T-1}
\mathfrak S_r(h)^z
}
\]

for every \(z\in\mathbb C\), with

\[
\boxed{
\mathcal M_h(z)
=
A(h)^z
\left[
1+
\sum_{\varnothing\ne J}
\delta_J(h)
\prod_{p\in J}(s_p^z-1)
\right].
}
\]

The convergence is locally uniform on \(\mathbb C\), so

\[
\boxed{
\mathcal M_h:\mathbb C\to\mathbb C
\text{ is entire}.
}
\]

On the real axis this extends OP-D092--OP-D094.

## 6. Limiting distribution — OP-D099

Define

\[
Y_r(h)=\log\mathfrak S_r(h)
\]

and the empirical probability measures

\[
\nu_{T,h}
=
\frac1T
\sum_{r=0}^{T-1}
\delta_{Y_r(h)}.
\]

Their characteristic functions are

\[
\phi_{T,h}(t)
=
\int e^{ity}\,d\nu_{T,h}(y)
=
\frac1T
\sum_{r<T}\mathfrak S_r(h)^{it}.
\]

By OP-D098,

\[
\phi_{T,h}(t)
\longrightarrow
\boxed{
\phi_h(t)=\mathcal M_h(it).
}
\]

Because \(\mathcal M_h\) is entire,

\[
\phi_h(0)=1
\]

and \(\phi_h\) is continuous at \(0\).

The standard Lévy continuity theorem therefore yields a unique probability measure

\[
\boxed{
\nu_h
}
\]

such that

\[
\boxed{
\nu_{T,h}\Rightarrow\nu_h
}
\]

weakly as \(T\to\infty\).

Thus the logarithmic dyadic singular-series orbit has a genuine limiting probability distribution.

## 7. Bilateral Laplace transform of the limit law — OP-D100

For every real \(\sigma\), OP-D094 supplies finite Cesaro moments of order \(\sigma\). Hence the limiting law has finite exponential moments of every real order.

More explicitly, for fixed \(z=\sigma+it\), choose \(\varepsilon>0\).

If \(\sigma>0\), the positive tail of \(e^{\sigma y}\) is uniformly controlled by the already bounded \((\sigma+\varepsilon)\)-moment.

If \(\sigma<0\), the negative tail is uniformly controlled by the \((\sigma-\varepsilon)\)-moment.

If \(\sigma=0\), the integrand has modulus one.

Therefore \(e^{zy}\) is uniformly integrable along the empirical measures, and weak convergence can be upgraded to

\[
\boxed{
\mathcal M_h(z)
=
\int_{\mathbb R}e^{zy}\,d\nu_h(y)
\qquad(z\in\mathbb C).
}
\]

Thus \(\mathcal M_h\) is the entire bilateral Laplace transform / moment transform of the limiting logarithmic law.

In particular,

\[
\boxed{
\phi_h(t)=
\int e^{ity}\,d\nu_h(y)
}
\]

is its characteristic function.

## 8. Canonical procyclic phase hull — OP-D101

Let \(\mathcal A_h\) be the active odd-prime channels and define

\[
\mathbb T_h^{\rm arith}
=
\prod_{p\in\mathcal A_h}
\mathbb Z/e_p\mathbb Z.
\]

Let

\[
g=(1\bmod e_p)_{p\in\mathcal A_h}
\]

and define the closed cyclic subgroup

\[
\boxed{
K_h
=
\overline{\{rg:r\in\mathbb Z\}}
\subset
\mathbb T_h^{\rm arith}.
}
\]

This is a compact procyclic group.

For every finite channel set \(J\), its projection has exactly

\[
L_J=\operatorname{lcm}_{p\in J}e_p
\]

points, with uniform Haar measure.

Let

\[
\rho(h)=(\rho_p(h))_p.
\]

For a finite \(J\),

\[
m_{K_h}
\{x:x_p=\rho_p(h)\ \forall p\in J\}
=
\delta_J(h).
\]

Indeed, the cylinder is empty when the generalized CRT system is incompatible, and otherwise it is one point in the finite projected orbit of size \(L_J\).

Define the measurable phase field

\[
\boxed{
\mathcal Y_h(x)
=
\log A(h)
+
\sum_{p\in\mathcal A_h}
\log s_p\,
\mathbf1_{\{x_p=\rho_p(h)\}}.
}
\]

Since

\[
\sum_p
\delta_p(h)\log s_p<\infty,
\]

Tonelli gives

\[
\mathcal Y_h(x)<\infty
\]

for Haar-almost every \(x\).

The limiting law is exactly the Haar pushforward

\[
\boxed{
\nu_h
=
(\mathcal Y_h)_*m_{K_h}.
}
\]

Hence the dyadic phase process has a canonical compact arithmetic probability space.

## 9. Dyadic-orbit invariance of the full law — OP-D102

Replace \(h\) by

\[
h'=2^kh.
\]

Then

\[
(h')^2=4^kh^2,
\]

so every active phase shifts by

\[
\boxed{
\rho_p(h')\equiv\rho_p(h)-k\pmod{e_p}.
}
\]

The static factor \(A(h)\) is unchanged because \(Z(2^kh)=Z(h)\).

Thus the phase field for \(2^kh\) is obtained from the phase field for \(h\) by translation by \(kg\) on the compact group \(K_h\).

Haar measure is translation invariant. Therefore

\[
\boxed{
\nu_{2^kh}=\nu_h.
}
\]

Equivalently,

\[
\boxed{
\mathcal M_{2^kh}(z)=\mathcal M_h(z)
\qquad
(z\in\mathbb C).
}
\]

So the **entire limiting distribution**, not merely its individual moments, is an invariant of the dyadic orbit.

## 10. Relation to the earlier \(B^2\) spectrum

The centered logarithmic field was already proved to lie in Besicovitch \(B^2\) with a rational pure-point phase spectrum.

The present theorem adds:

1. all complex Cesaro moments;
2. an entire moment transform;
3. weak convergence of the empirical value distribution;
4. a canonical procyclic Haar model;
5. full-law dyadic invariance.

Classical theory already connects Besicovitch almost-periodic functions with limiting distributions. The direct complex-transform proof here makes the specific ARPL limiting law explicit and does not rely on a novelty claim for that general principle.

## 11. Prior-art boundary

Standard ingredients used here:

- quantitative multiplicative-order bounds;
- generalized CRT;
- locally uniform convergence of holomorphic series;
- Lévy's continuity theorem;
- compact procyclic groups and Haar measure;
- classical limiting-distribution theory for almost-periodic functions.

Relevant general literature includes the theory of probabilistic aspects of Besicovitch/limit-periodic arithmetic functions and modern work on almost-periodic stochastic processes.

The project-specific object is the explicit ARPL phase law for the dyadic singular-series orbit and its transform

\[
\mathcal M_h(z)
=
A(h)^z
\left[
1+
\sum_J
\delta_J(h)\prod_{p\in J}(s_p^z-1)
\right].
\]

Literature novelty of this exact specialization remains NOT ESTABLISHED.

## 12. No-go

This limiting law is a law for the Hardy--Littlewood singular-series weight along the dyadic family of patterns

\[
\{0,2,2^rh,2^rh+2\}.
\]

It does not prove that those prime quadruplets occur with the conjectured Hardy--Littlewood asymptotic, does not prove infinitely many twin primes, and does not imply RH.
