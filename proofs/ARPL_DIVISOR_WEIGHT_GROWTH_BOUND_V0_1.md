# ARPL Divisor-Weight Growth Bound v0.1

Status: exact comparison theorem + standard totient growth bound.

## 1. Dynamic divisor weight

Recall

\[
R(N)
=
\prod_{\substack{p\mid N\\p\ge5}}
\frac{p-3}{p-4}.
\]

For every prime \(p\ge5\),

\[
\frac{p-3}{p-4}
=
\frac{p}{p-1}
\left(
1+\frac{3}{p(p-4)}
\right).
\]

Therefore define

\[
C_R
=
\prod_{p\ge5}
\left(
1+\frac{3}{p(p-4)}
\right).
\]

Because the local defect is \(O(p^{-2})\),

\[
\boxed{
0<C_R<\infty.
}
\]

Numerically \(C_R\approx2.0656\), but the numerical value is not used.

## 2. Totient comparison — OP-D072

For every nonzero integer \(N\),

\[
\begin{aligned}
R(N)
&=
\prod_{\substack{p\mid N\\p\ge5}}
\frac{p}{p-1}
\prod_{\substack{p\mid N\\p\ge5}}
\left(
1+\frac{3}{p(p-4)}
\right)\\
&\le
C_R
\prod_{p\mid N}\frac{p}{p-1}.
\end{aligned}
\]

Since

\[
\frac{|N|}{\varphi(|N|)}
=
\prod_{p\mid N}\frac{p}{p-1},
\]

we obtain the exact universal comparison

\[
\boxed{
R(N)
\le
C_R\,\frac{|N|}{\varphi(|N|)}.
}
\]

## 3. Standard growth consequence — OP-D073

The classical maximal-order bound for Euler's totient ratio gives

\[
\frac{N}{\varphi(N)}
\ll
\log\log N
\]

for \(N\ge3\).

Hence

\[
\boxed{
R(N)\ll\log\log |N|.
}
\]

This bound is pointwise and uniform in \(N\).

## 4. Dyadic orbit consequence — OP-D074

For fixed admissible \(h\ge6\), set

\[
N_r=4^rh^2-4.
\]

Then

\[
\log |N_r|
=
r\log4+O_h(1),
\]

so

\[
\log\log |N_r|
=
\log(r+2)+O_h(1).
\]

Therefore

\[
\boxed{
R(4^rh^2-4)
\ll_h
\log(r+2).
}
\]

Using the exact instantaneous factorization,

\[
\mathfrak S(H_{2^rh})
=
\frac{27}{2}C_*Z(h)R(4^rh^2-4),
\]

we obtain

\[
\boxed{
\mathfrak S(H_{2^rh})
\ll_h
\log(r+2).
}
\]

Thus the dyadic singular-series orbit has at most logarithmic pointwise growth.

## 5. Relation to earlier exponential-sequence divisor work

This estimate is consistent with classical work of Erdős on reciprocal divisor sums of \(2^n-1\), and with later work of Everest--Shparlinski on divisor sums of generalized exponential polynomials.

No novelty claim is made for logarithmic-type divisor bounds themselves.

## 6. Boundary

The pointwise logarithmic bound does not prove that

\[
\frac1T\sum_{r<T}R(4^rh^2-4)
\]

converges.

It only rules out faster-than-logarithmic pointwise growth and supplies a deterministic envelope for the remaining arithmetic-mean problem.
