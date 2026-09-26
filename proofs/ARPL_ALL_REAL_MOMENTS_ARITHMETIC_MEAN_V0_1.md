# ARPL All Real Moments and Arithmetic Mean v0.1

Status: exact mean-value theorem using the ARPL base-4 phase clock plus a standard quantitative theorem of Erdős--Murty on multiplicative orders.

## 1. Observable and moment expansion

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
A(h)=\frac{27}{2}C_*Z(h)
\]

and

\[
R_r(h)
=
R(4^rh^2-4)
=
\prod_{p\ge5}s_p^{E_p(r;h)},
\qquad
s_p=\frac{p-3}{p-4}>1.
\]

The quadratic phase-clock theorem gives, for every active channel,

\[
E_p(r;h)
=
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}},
\qquad
e_p=\operatorname{ord}_p(4).
\]

Fix any finite real number \(s\). Define

\[
b_{p,s}=s_p^s-1.
\]

Then

\[
R_r(h)^s
=
\prod_{p\ge5}(1+b_{p,s}E_p(r;h)).
\]

For each fixed \(s\),

\[
\boxed{
|b_{p,s}|\ll_s\frac1p.
}
\]

## 2. Standard multiplicative-order input

Let

\[
d_p=\operatorname{ord}_p(2).
\]

A quantitative theorem of Erdős and M. Ram Murty implies that there exist constants

\[
\alpha>0,\qquad\delta>0
\]

such that

\[
\boxed{
d_p
\ge
p^{1/2}\exp((\log p)^\delta)
}
\]

for all but

\[
\boxed{
O\left(\frac{x}{(\log x)^{1+\alpha}}\right)
}
\]

primes \(p\le x\).

This is a standard external theorem and is not an ARPL result.

Because

\[
e_p
=
\operatorname{ord}_p(4)
=
\frac{d_p}{\gcd(d_p,2)},
\]

every nonexceptional prime satisfies

\[
\boxed{
e_p
\ge
\frac12
p^{1/2}\exp((\log p)^\delta).
}
\]

Call these primes **good** and the exceptional primes **bad**.

## 3. Reciprocal mass of bad primes — OP-D090

Let \(B(x)\) count bad primes up to \(x\). Then

\[
B(x)
\ll
\frac{x}{(\log x)^{1+\alpha}}.
\]

Partial summation gives

\[
\sum_{\substack{p\le X\\p\ {\rm bad}}}\frac1p
=
\frac{B(X)}X
+
\int_2^X\frac{B(t)}{t^2}\,dt
+O(1),
\]

and the integral converges because

\[
\int^\infty
\frac{dt}{t(\log t)^{1+\alpha}}
<\infty.
\]

Hence

\[
\boxed{
\sum_{p\ {\rm bad}}\frac1p<\infty.
}
\]

Since \(|b_{p,s}|\ll_s1/p\),

\[
\boxed{
\sum_{p\ {\rm bad}}|b_{p,s}|<\infty,
}
\]

and consequently

\[
\boxed{
C_{\rm bad}(s)
=
\prod_{p\ {\rm bad}}
(1+|b_{p,s}|)
<\infty.
}
\]

## 4. Absolute all-orders endpoint summability — OP-D091

For a finite phase-compatible set \(J\), let

\[
\delta_J(h)=\frac1{L_J},
\qquad
L_J=\operatorname{lcm}_{p\in J}e_p,
\]

and set \(\delta_J=0\) for incompatible sets.

We prove

\[
\boxed{
\sum_{\substack{J\subset\mathbb P_{\ge5}\\
J\ {\rm finite},\,J\ne\varnothing}}
\delta_J(h)
\prod_{p\in J}|b_{p,s}|
<\infty
}
\]

for every fixed real \(s\).

Split

\[
J=G\sqcup B
\]

into good and bad primes.

### All-bad subsets

Using only \(\delta_J\le1\),

\[
\sum_{\varnothing\ne B\subset\mathcal B}
\delta_B
\prod_{p\in B}|b_{p,s}|
\le
C_{\rm bad}(s)-1
<\infty.
\]

### Subsets containing a good prime

Fix a nonempty good subset \(G\), and let

\[
q=\max G.
\]

Since

\[
L_G\ge e_q,
\]

the good-prime order bound gives

\[
\delta_{G\cup B}
\le
\frac1{L_G}
\le
2q^{-1/2}
\exp(-(\log q)^\delta)
\]

for every bad subset \(B\).

Summing over all bad additions costs at most the finite factor \(C_{\rm bad}(s)\).

Now sum good subsets by their maximal prime \(q\). Since

\[
|b_{q,s}|\ll_s\frac1q
\]

and

\[
\prod_{\substack{p<q\\p\ {\rm good}}}
(1+|b_{p,s}|)
\le
\prod_{p<q}(1+O_s(1/p))
\ll_s
(\log q)^{C_s}
\]

for some finite constant \(C_s\), the total contribution is bounded by

\[
\ll_s
\sum_q
\frac{(\log q)^{C_s}}
{q^{3/2}}
\exp(-(\log q)^\delta),
\]

which converges.

Thus the full all-orders absolute subset sum is finite for every real \(s\).

## 5. Cesaro mean for every real moment — OP-D092

For a finite time window \(0\le r<T\), only primes dividing

\[
M_T(h)
=
\prod_{r=0}^{T-1}(4^rh^2-4)
\]

can contribute.

Expanding over the finite set of seen primes gives

\[
\frac1T\sum_{r<T}R_r(h)^s
=
1+
\sum_J
\left(\prod_{p\in J}b_{p,s}\right)
\frac{N_J(T)}T.
\]

For every compatible \(J\),

\[
\frac{N_J(T)}T
\le
\frac1{L_J}+\frac1T.
\]

The \(1/L_J\) contribution is dominated by the absolutely convergent series OP-D091.

For the endpoint term, note that for every \(x>1\) and real \(s\),

\[
1+|x^s-1|
\le
x^{|s|}.
\]

Therefore

\[
\prod_{p\mid M_T(h)}
(1+|b_{p,s}|)
\le
R(M_T(h))^{|s|}.
\]

The divisor-weight growth theorem gives

\[
R(M_T(h))
\ll
\log\log|M_T(h)|
\]

and

\[
\log|M_T(h)|=O_h(T^2).
\]

Hence the endpoint contribution is

\[
O_{h,s}\left(
\frac{(\log T)^{|s|}}T
\right)
\to0.
\]

It follows that the Cesaro mean

\[
\boxed{
\mathcal M_s^R(h)
=
\lim_{T\to\infty}
\frac1T\sum_{r<T}R_r(h)^s
}
\]

exists and is finite for every real \(s\), and equals the absolutely convergent CRT expansion

\[
\boxed{
\mathcal M_s^R(h)
=
1+
\sum_{\varnothing\ne J}
\delta_J(h)
\prod_{p\in J}b_{p,s}.
}
\]

## 6. Arithmetic mean closed — OP-D093

At

\[
s=1,
\qquad
b_{p,1}=\frac1{p-4},
\]

so the previously open arithmetic mean exists:

\[
\boxed{
\mathcal M_1^R(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
R(4^rh^2-4)
<\infty.
}
\]

Therefore the full two-twin-pair singular-series orbit has the finite arithmetic Cesaro mean

\[
\boxed{
\mathcal A(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh})
=
A(h)\mathcal M_1^R(h).
}
\]

Explicitly,

\[
\boxed{
\mathcal A(h)
=
\frac{27}{2}C_*Z(h)
\left[
1+
\sum_{\varnothing\ne J}
\frac{
\mathbf1_{\rm CRT\ compatible}(J;h)
}{
\operatorname{lcm}_{p\in J}\operatorname{ord}_p(4)
}
\prod_{p\in J}\frac1{p-4}
\right].
}
\]

The displayed all-orders series is absolutely convergent.

## 7. All real moments of the full singular series — OP-D094

Since the static factor \(A(h)>0\),

\[
\boxed{
\mathcal M_s^{\mathfrak S}(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh})^s
=
A(h)^s\mathcal M_s^R(h)
}
\]

exists and is finite for every real

\[
\boxed{s\in\mathbb R.}
\]

Thus the previous subcritical theorem \(0<s<1\) is strictly strengthened.

## 8. Dyadic invariance — OP-D095

Replacing \(h\) by \(2^kh\) rotates the base-4 phase classes but preserves:

- the periods \(e_p\);
- all CRT compatibility relations;
- all finite joint densities;
- the static factor \(Z(h)\).

Therefore

\[
\boxed{
\mathcal M_s^{\mathfrak S}(2^kh)
=
\mathcal M_s^{\mathfrak S}(h)
}
\]

for every real \(s\) and \(k\ge0\).

In particular,

\[
\boxed{
\mathcal A(2^kh)=\mathcal A(h).
}
\]

## 9. Epistemic boundary

The decisive large-order estimate is not new and must be credited to Erdős--Murty.

What is established here is the deduction that this quantitative exceptional-set theorem removes the \(s=1\) obstruction in the ARPL phase-subset expansion.

This result concerns the Hardy--Littlewood singular-series weight along a dyadic family of gap patterns. It does not prove that those prime quadruplets occur with the conjectured asymptotic.

## 10. Remaining gate

The arithmetic mean of the singular-series orbit is no longer open.

The next natural analytic object is the full limiting distribution / complex moment transform of

\[
\log\mathfrak S(H_{2^rh}),
\]

which can now be approached using the same good/bad channel split and the already proved \(B^2\) phase spectrum.
