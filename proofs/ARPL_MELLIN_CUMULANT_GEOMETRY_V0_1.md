# ARPL Mellin Law and Cumulant Geometry v0.1

Status: exact consequences of the entire limiting transform.

## 1. Positive limiting law

Let

\[
\nu_h
\]

be the limiting law of

\[
Y_r(h)=\log\mathfrak S(H_{2^rh})
\]

from OP-D099.

Define the pushforward under exponentiation

\[
\boxed{
\mu_h=(\exp)_*\nu_h.
}
\]

Then \(\mu_h\) is the limiting probability law on \((0,\infty)\) of the singular-series amplitudes

\[
\mathfrak S(H_{2^rh}).
\]

Indeed, weak convergence of the logarithmic empirical measures and continuity of \(e^y\) imply

\[
\frac1T\sum_{r<T}\delta_{\mathfrak S(H_{2^rh})}
\Rightarrow
\mu_h.
\]

## 2. Entire Mellin transform — OP-D103

The entire phase transform satisfies

\[
\mathcal M_h(z)
=
\int_{\mathbb R}e^{zy}\,d\nu_h(y).
\]

Changing variables \(x=e^y\) gives

\[
\boxed{
\mathcal M_h(z)
=
\int_{(0,\infty)}x^z\,d\mu_h(x)
\qquad(z\in\mathbb C).
}
\]

Thus \(\mathcal M_h\) is the bilateral Mellin transform of the limiting positive singular-series law.

Special values recover the earlier observables:

\[
\mathcal M_h(0)=1,
\]

\[
\mathcal M_h(1)=\mathcal A(h),
\]

and

\[
\left.\frac{d}{dz}\mathcal M_h(z)\right|_{z=0}
=
\mathcal L(h).
\]

## 3. Local cumulant-generating function — OP-D104

Since

\[
\mathcal M_h(0)=1
\]

and \(\mathcal M_h\) is entire, there exists a disk

\[
|z|<r_h
\]

on which \(\mathcal M_h(z)\ne0\).

Choose the analytic logarithm normalized by

\[
K_h(0)=0
\]

and define

\[
\boxed{
K_h(z)=\log\mathcal M_h(z).
}
\]

Then \(K_h\) is analytic near zero and has the cumulant expansion

\[
\boxed{
K_h(z)
=
\sum_{n=1}^\infty
\kappa_n(h)\frac{z^n}{n!},
}
\]

where

\[
\boxed{
\kappa_n(h)=K_h^{(n)}(0).
}
\]

All logarithmic cumulants therefore exist and are finite.

## 4. Recovery of the earlier mean and variance — OP-D105

Because \(\mathcal M_h\) is the moment-generating transform of \(Y\sim\nu_h\),

\[
\boxed{
\kappa_1(h)
=
\int y\,d\nu_h(y)
=
\mathcal L(h).
}
\]

Similarly,

\[
\boxed{
\kappa_2(h)
=
\int
(y-\mathcal L(h))^2\,d\nu_h(y)
=
\mathcal V(h).
}
\]

Thus the previously proved global logarithmic mean and global \(B^2\) variance are precisely the first two derivatives of one analytic cumulant geometry.

Higher derivatives give the higher connected log-amplitude cumulants.

## 5. Raw log moments — OP-D106

Because the bilateral Laplace transform is entire, differentiation under the integral is valid at every finite order:

\[
\boxed{
\mathcal M_h^{(n)}(0)
=
\int y^n\,d\nu_h(y)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\left(
\log\mathfrak S(H_{2^rh})
\right)^n.
}
\]

Hence every polynomial moment of the logarithmic phase-amplitude field exists.

The moment sequence determines \(\nu_h\) uniquely because its moment-generating function is finite in a neighborhood of zero; here it is stronger, extending to an entire bilateral Laplace transform.

## 6. Chernoff bounds for the limiting log law — OP-D107

For every \(s>0\) and threshold \(y\in\mathbb R\),

\[
\nu_h([y,\infty))
=
\Pr(Y\ge y)
\le
e^{-sy}\mathcal M_h(s).
\]

Optimizing,

\[
\boxed{
\Pr(Y\ge y)
\le
\inf_{s>0}
\exp\bigl(K_h(s)-sy\bigr).
}
\]

Likewise, for \(s<0\),

\[
\Pr(Y\le y)
\le
e^{-sy}\mathcal M_h(s),
\]

so

\[
\boxed{
\Pr(Y\le y)
\le
\inf_{s<0}
\exp\bigl(K_h(s)-sy\bigr).
}
\]

These are exact transform bounds for the limiting law.

## 7. Chernoff bounds for singular-series amplitude — OP-D108

For

\[
X=e^Y\sim\mu_h
\]

and \(x>0\),

\[
\Pr(X\ge x)
=
\Pr(Y\ge\log x).
\]

Therefore

\[
\boxed{
\mu_h([x,\infty))
\le
\inf_{s>0}
\frac{\mathcal M_h(s)}{x^s}.
}
\]

Similarly,

\[
\boxed{
\mu_h((0,x])
\le
\inf_{s<0}
\frac{\mathcal M_h(s)}{x^s}.
}
\]

The earlier fixed-\(s\) Markov bounds are special cases; the entire transform permits optimization over all real exponents.

## 8. Dyadic invariance of cumulant geometry — OP-D109

The full law satisfies

\[
\nu_{2^kh}=\nu_h.
\]

Hence

\[
\boxed{
\mathcal M_{2^kh}(z)=\mathcal M_h(z),
}
\]

and therefore, near zero,

\[
\boxed{
K_{2^kh}(z)=K_h(z).
}
\]

Every cumulant is consequently a dyadic-orbit invariant:

\[
\boxed{
\kappa_n(2^kh)=\kappa_n(h)
\qquad(n\ge1).
}
\]

This includes the already known invariance of the log mean and variance.

## 9. Analytic rate function

Define the convex transform

\[
\boxed{
I_h(y)
=
\sup_{s\in\mathbb R}
\{sy-K_h(s)\}.
}
\]

Since \(\mathcal M_h(s)\) is finite for every real \(s\), \(K_h(s)\) is finite and convex on the whole real axis.

The Chernoff upper bound can be written

\[
\boxed{
\Pr(Y\ge y)
\le
e^{-I_h(y)}
}
\]

when the optimizing branch is on \(s\ge0\), with the corresponding lower-tail statement for \(s\le0\).

This is a transform-derived concentration envelope. It is not, by itself, a large-deviation principle in a scaling parameter.

## 10. Boundary

Closed:

- limiting law \(\nu_h\);
- positive amplitude law \(\mu_h\);
- entire Mellin/Laplace transform;
- all logarithmic moments;
- all cumulants;
- optimized Chernoff envelopes;
- dyadic invariance of the entire cumulant tower.

Not established here:

- absolute continuity or atomlessness of \(\nu_h\);
- a density formula;
- a large-deviation principle with an external scaling limit;
- Hardy--Littlewood occurrence asymptotics for actual prime quadruplets.
