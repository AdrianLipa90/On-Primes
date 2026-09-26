# ARPL Subcritical Fractional Moment Theorem v0.1

Status: exact existence theorem for all dyadic-time moments of order \(0<s<1\) of the dynamic singular-series weight.

## 1. Base-4 pulse representation

For an admissible separation \(h\ge6\), \(6\mid h\), write

\[
\mathfrak S(H_{2^rh})
=
A(h)\,R(4^rh^2-4),
\]

where

\[
A(h)=\frac{27}{2}C_*Z(h)
\]

is independent of \(r\), and

\[
R(4^rh^2-4)
=
\prod_{p\ge5}
s_p^{E_p(r;h)},
\qquad
s_p=\frac{p-3}{p-4}.
\]

By the quadratic phase-clock theorem, every active channel has

\[
E_p(r;h)
=
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}},
\qquad
e_p=\operatorname{ord}_p(4),
\]

and every inactive channel has \(E_p\equiv0\).

## 2. Fractional channel weights

Fix

\[
0<s<1.
\]

Define

\[
b_{p,s}
=
s_p^s-1
=
\left(1+\frac1{p-4}\right)^s-1.
\]

Then

\[
R(4^rh^2-4)^s
=
\prod_{p\ge5}
\left(1+b_{p,s}E_p(r;h)\right).
\]

For each fixed \(r\), this product contains only finitely many nontrivial factors.

Also

\[
p\,b_{p,s}\to s
\]

as \(p\to\infty\).

Therefore for every number \(c\) with

\[
s<c<1
\]

there exists \(P_0=P_0(s,c)\) such that

\[
\boxed{
b_{p,s}\le\frac{c}{p}
\qquad(p>P_0).
}
\]

## 3. Exact finite-subset densities

For a finite active prime set \(J\), the simultaneous phase system is

\[
r\equiv\rho_p(h)\pmod{e_p},
\qquad p\in J.
\]

By generalized CRT, it is either incompatible, in which case its density is zero, or compatible, in which case there is exactly one residue class modulo

\[
L_J=\operatorname{lcm}_{p\in J}e_p.
\]

Thus

\[
\boxed{
\delta_J(h)
=
\begin{cases}
1/L_J,&\text{CRT-compatible},\\
0,&\text{otherwise}.
\end{cases}
}
\]

For \(J=\varnothing\), set \(\delta_\varnothing=1\).

## 4. Arithmetic size forces clock size — OP-D084

If \(J\) is compatible and nonempty, then every \(e_p\mid L_J\). Hence

\[
4^{L_J}\equiv1\pmod p
\qquad(p\in J).
\]

Since the primes are distinct,

\[
\prod_{p\in J}p
\mid
4^{L_J}-1.
\]

Therefore

\[
\prod_{p\in J}p<4^{L_J},
\]

so

\[
\boxed{
L_J
>
\frac1{\log4}
\sum_{p\in J}\log p.
}
\]

Consequently

\[
\boxed{
\delta_J(h)
\le
\frac{\log4}{\sum_{p\in J}\log p}.
}
\]

This bound is independent of phase compatibility; incompatible sets have density zero.

## 5. Absolute all-orders subset summability — OP-D085

Consider

\[
\Sigma_s(h)
=
\sum_{\substack{J\subset\mathbb P_{\ge5}\\
J\ \mathrm{finite},\,J\ne\varnothing}}
\delta_J(h)
\prod_{p\in J}b_{p,s}.
\]

We prove that this series converges.

The finitely many primes \(p\le P_0\) contribute only a finite multiplicative constant, so it is enough to sum subsets of primes \(p>P_0\).

Using OP-D084 and \(b_{p,s}\le c/p\),

\[
\Sigma_s(h)
\ll_{s,h}
\sum_{\varnothing\ne J\subset\{p>P_0\}}
\frac{
\prod_{p\in J}(c/p)
}{
\sum_{p\in J}\log p
}.
\]

Use

\[
\frac1{\sum_{p\in J}\log p}
=
\int_0^\infty
\prod_{p\in J}p^{-t}\,dt.
\]

All terms are nonnegative, so Tonelli gives

\[
\sum_{J\ne\varnothing}
\frac{\prod_{p\in J}(c/p)}{\sum_{p\in J}\log p}
=
\int_0^\infty
\left[
\prod_{p>P_0}
\left(1+\frac{c}{p^{1+t}}\right)
-1
\right]dt.
\]

For \(0<t\le1\),

\[
\log
\prod_{p>P_0}
\left(1+\frac{c}{p^{1+t}}\right)
\le
c\sum_p p^{-1-t}
\le
c\log\frac1t+O_c(1),
\]

using the standard reciprocal-prime/Mertens estimate. Hence the integrand is

\[
O_c(t^{-c}),
\]

which is integrable at \(0\) because \(c<1\).

For \(t\ge1\), the prime sum is exponentially small in \(t\), so the integral also converges at infinity.

Therefore

\[
\boxed{
\Sigma_s(h)<\infty
\qquad(0<s<1).
}
\]

This sums all interaction orders simultaneously.

## 6. Fractional Cesaro mean — OP-D086

Define

\[
F_s(r;h)
=
R(4^rh^2-4)^s.
\]

At each fixed \(r\),

\[
F_s(r;h)
=
\sum_{J\ \mathrm{finite}}
\left(\prod_{p\in J}b_{p,s}\right)
\prod_{p\in J}E_p(r;h),
\]

and the pointwise expansion is finite.

For a finite time window \(0\le r<T\), only primes dividing

\[
M_T(h)
=
\prod_{r=0}^{T-1}(4^rh^2-4)
\]

can occur.

For every compatible \(J\),

\[
\frac1T
\#\{r<T:E_p(r)=1\ \forall p\in J\}
\le
\frac1{L_J}+\frac1T.
\]

The sum of the \(1/L_J\) terms is controlled by OP-D085.

The finite-horizon endpoint contribution satisfies

\[
\frac1T
\sum_{J\subset D_T}
\prod_{p\in J}b_{p,s}
=
\frac1T
\prod_{p\in D_T}(1+b_{p,s}),
\]

where \(D_T\) is the finite set of dynamic primes seen before time \(T\).

Since \(D_T\) is contained in the prime-divisor set of \(M_T(h)\),

\[
\prod_{p\in D_T}(1+b_{p,s})
\le
R(M_T(h))^s.
\]

The divisor-weight growth theorem gives

\[
R(M_T(h))
\ll
\log\log |M_T(h)|.
\]

Since

\[
\log |M_T(h)|=O_h(T^2),
\]

the endpoint term is

\[
O_{h,s}\left(\frac{(\log T)^s}{T}\right)
\to0.
\]

Finite subset means converge to \(\delta_J(h)\), while OP-D085 gives an absolutely summable dominating family. Hence

\[
\boxed{
\mathcal M_s^R(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r=0}^{T-1}
R(4^rh^2-4)^s
}
\]

exists and equals the absolutely convergent expansion

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

## 7. Fractional moments of the full singular series — OP-D087

Because the static factor \(A(h)\) is independent of \(r\),

\[
\boxed{
\mathcal M_s^{\mathfrak S}(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh})^s
=
A(h)^s
\mathcal M_s^R(h)
}
\]

exists and is finite for every

\[
\boxed{0<s<1.}
\]

Thus the full dyadic singular-series orbit has all positive subunit Cesaro moments.

## 8. Dyadic invariance — OP-D088

Replacing \(h\) by \(2^kh\) shifts/rotates every local phase class and leaves:

- \(Z(h)\);
- the observable periods \(e_p\);
- CRT compatibility;
- all joint densities \(\delta_J\);

unchanged.

Therefore

\[
\boxed{
\mathcal M_s^{\mathfrak S}(2^kh)
=
\mathcal M_s^{\mathfrak S}(h)
\qquad(0<s<1).
}
\]

## 9. Tail-density consequence — OP-D089

For every \(X>0\), Markov's inequality gives

\[
\boxed{
\limsup_{T\to\infty}
\frac1T
\#\{r<T:\mathfrak S(H_{2^rh})\ge X\}
\le
\frac{\mathcal M_s^{\mathfrak S}(h)}{X^s}
}
\]

for every \(0<s<1\).

Thus the raw singular-series spikes have controlled upper density at every subcritical power.

## 10. Why s=1 is the critical endpoint of this proof

At large \(p\),

\[
b_{p,s}\sim\frac{s}{p}.
\]

The all-orders majorant near \(t=0\) behaves like

\[
t^{-s}.
\]

It is integrable for \(s<1\).

At \(s=1\), the same unconditional majorant becomes the borderline

\[
t^{-1},
\]

whose integral diverges logarithmically.

Therefore the proof mechanism closes every \(0<s<1\) but does not close \(s=1\).

This is a limitation of the current bound, not a proof that the arithmetic mean at \(s=1\) diverges.

## 11. Status

Closed:

\[
\boxed{
\text{all interaction orders for every fixed }0<s<1.
}
\]

Open:

\[
\boxed{
s=1:
\quad
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh}).
}
\]

The raw arithmetic mean is now isolated as a genuine critical endpoint rather than an unspecified infinite-channel problem.
