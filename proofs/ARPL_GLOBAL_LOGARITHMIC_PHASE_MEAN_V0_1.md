# ARPL Global Logarithmic Phase Mean v0.1

Status: exact existence theorem for the infinite-channel dyadic-time logarithmic/geometric mean.

## 1. Starting point

For an admissible twin separation

\[
h\ge6,
\qquad
6\mid h,
\]

the instantaneous factorization already proved is

\[
\mathfrak S(H_{2^rh})
=
\frac{27}{2}C_*Z(h)R(4^rh^2-4),
\]

where

\[
R(N)
=
\prod_{\substack{p\mid N\\p\ge5}}
s_p,
\qquad
s_p=\frac{p-3}{p-4}=1+\frac1{p-4}.
\]

Define the special-hit indicator

\[
E_p(r;h)
=
\mathbf1_{\{2^rh\equiv\pm2\pmod p\}}.
\]

Then

\[
\log R(4^rh^2-4)
=
\sum_{p\ge5}E_p(r;h)\log s_p.
\]

For each fixed \(r\), the sum is finite because the contributing primes divide the nonzero integer \(4^rh^2-4\).

## 2. Exact local hit density — OP-D067

Fix \(p\ge5\).

If \(p\mid h\), the orbit is zero-fixed and never reaches \(\pm2\), so

\[
\delta_p(h)=0.
\]

Assume \(p\nmid h\), and set

\[
d_p=\operatorname{ord}_p(2).
\]

The residue sequence \(2^rh\bmod p\) runs around one \(d_p\)-cycle.

If that orbit contains neither \(+2\) nor \(-2\),

\[
\delta_p(h)=0.
\]

If \(d_p\) is odd and the orbit is special, it contains exactly one of \(+2,-2\), so

\[
\delta_p(h)=\frac1{d_p}.
\]

If \(d_p\) is even and the orbit is special, \(+2\) and \(-2\) both occur, half an orbit apart, so

\[
\delta_p(h)=\frac2{d_p}.
\]

Thus in all cases

\[
\boxed{
0\le\delta_p(h)\le\frac2{d_p}.
}
\]

This \(\delta_p(h)\) is the exact natural density of special phase hits in dyadic time.

## 3. Absolute convergence of the logarithmic correction — OP-D068

For \(p\ge5\),

\[
0<\log s_p
=
\log\left(1+\frac1{p-4}\right)
\ll\frac1p.
\]

Also

\[
d_p\ge\log_2(p+1).
\]

Therefore

\[
\delta_p(h)\log s_p
\ll
\frac1{p\log p}.
\]

The prime sum

\[
\sum_p\frac1{p\log p}
\]

converges, for example by partial summation from the standard prime-counting upper bound
\(\pi(x)\ll x/\log x\).

Hence

\[
\boxed{
\sum_{p\ge5}
\delta_p(h)\log s_p
<\infty.
}
\]

## 4. Tail control in Cesaro mean

Let

\[
Y_P(r)
=
\sum_{\substack{p>P\\p\ge5}}
E_p(r;h)\log s_p.
\]

For a single channel of period \(d_p\), the number of hits among \(0\le r<T\) is at most

\[
2\left(\frac{T}{d_p}+1\right).
\]

Only primes dividing

\[
M_T(h)
=
\prod_{r=0}^{T-1}(4^rh^2-4)
\]

can contribute at least one hit before time \(T\).

Therefore

\[
\frac1T\sum_{r<T}Y_P(r)
\le
2\sum_{p>P}\frac{\log s_p}{d_p}
+
\frac2T
\sum_{\substack{p\mid M_T(h)\\p>P}}
\log s_p.
\]

Using \(\log s_p\ll1/p\) and Mertens,

\[
\sum_{p\mid M_T(h)}\log s_p
\ll
\sum_{p\le |M_T(h)|}\frac1p
\ll
\log\log |M_T(h)|.
\]

Since

\[
\log|M_T(h)|=O_h(T^2),
\]

the endpoint term is

\[
O_h\left(\frac{\log T}{T}\right)
\to0.
\]

Consequently

\[
\limsup_{T\to\infty}
\frac1T\sum_{r<T}Y_P(r)
\le
2\sum_{p>P}\frac{\log s_p}{d_p},
\]

and the right-hand side tends to zero as \(P\to\infty\).

Thus finite periodic channel truncations approximate the full logarithmic observable in Cesaro \(L^1\).

## 5. Global logarithmic mean theorem — OP-D069

The Cesaro mean

\[
\boxed{
\mathcal L(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r=0}^{T-1}
\log\mathfrak S(H_{2^rh})
}
\]

exists and equals

\[
\boxed{
\mathcal L(h)
=
\log\left(\frac{27}{2}C_*Z(h)\right)
+
\sum_{p\ge5}
\delta_p(h)
\log\frac{p-3}{p-4}.
}
\]

The series is absolutely convergent.

Define the global dyadic geometric mean

\[
\boxed{
\mathcal G(h)=e^{\mathcal L(h)}.
}
\]

Then

\[
0<\mathcal G(h)<\infty.
\]

Equivalently,

\[
\boxed{
\mathcal G(h)
=
\frac{27}{2}C_*Z(h)
\prod_{p\ge5}
\left(\frac{p-3}{p-4}\right)^{\delta_p(h)}.
}
\]

The exponents are exactly \(0\), \(1/d_p\), or \(2/d_p\).

## 6. Dyadic invariance — OP-D070

Multiplying \(h\) by a power of two does not change:

- its odd prime divisors;
- the doubling orbit occupied by \(h\bmod p\);
- the hit density \(\delta_p(h)\).

Therefore

\[
\boxed{
\mathcal L(2^kh)=\mathcal L(h)
}
\]

and

\[
\boxed{
\mathcal G(2^kh)=\mathcal G(h)
}
\]

for every \(k\ge0\).

Thus the global geometric phase mean is another exact invariant of the dyadic orbit.

## 7. Jensen lower bound for the unresolved arithmetic mean — OP-D071

For every finite \(T\), positivity and Jensen's inequality give

\[
\frac1T\sum_{r<T}\mathfrak S(H_{2^rh})
\ge
\exp\left(
\frac1T\sum_{r<T}\log\mathfrak S(H_{2^rh})
\right).
\]

Taking lower limits and using OP-D069,

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\sum_{r<T}\mathfrak S(H_{2^rh})
\ge
\mathcal G(h)>0.
}
\]

This does not prove that the arithmetic Cesaro mean exists, but it provides a rigorous positive lower bound for any limiting behavior.

## 8. Numerical illustration for \(h=6\)

Finite prime-channel truncations of the geometric mean give approximately:

\[
\begin{array}{c|c}
P & \exp(\mathcal L_P(6))\\
\hline
100 & 6.9762412859\\
500 & 6.9259593096\\
1000 & 6.9216269294\\
5000 & 6.9184692865\\
10000 & 6.9181530932
\end{array}
\]

These numbers illustrate the convergent theorem; they are not used in its proof.

## 9. Relation to the all-orders cluster problem

Taking logarithms exactly linearizes the channel product. Therefore the logarithmic/geometric global observable closes without needing all connected cumulant orders.

The unresolved object remains the arithmetic mean

\[
\lim_{T\to\infty}
\frac1T\sum_{r<T}\mathfrak S(H_{2^rh}),
\]

whose existence depends on multiplicative cross-channel effects that the logarithm removes.

## 10. Prior-art boundary

The proof uses standard:

- multiplicative-order periodicity;
- Cesaro averaging of periodic sequences;
- Mertens bounds;
- prime-counting upper bounds;
- Jensen's inequality.

The ARPL-specific object is the dyadic singular-series orbit and its exact phase-hit decomposition.

Literature novelty is not established.
