# ARPL Instantaneous Singular-Series Factorization v0.1

Status: exact specialization of the standard Hardy--Littlewood local factors to the dyadic two-twin-pair orbit.

## 1. Setup

Let

\[
H_x=\{0,2,x,x+2\},
\]

with \(x\ge6\) and \(6\mid x\). Its standard Hardy--Littlewood singular series is

\[
\mathfrak S(H_x)
=
\prod_p
\left(1-\frac{\nu_p(H_x)}p\right)
\left(1-\frac1p\right)^{-4}.
\]

For \(p\ge5\), define

\[
\alpha_p=\frac{p^3}{(p-1)^4},
\qquad
\beta_p=\frac{p^3(p-4)}{(p-1)^4}.
\]

Then the local factor is exactly

\[
B_p(x)
=
\beta_p+
\alpha_p
\left(
2\mathbf1_{p\mid x}
+
\mathbf1_{p\mid x-2}
+
\mathbf1_{p\mid x+2}
\right).
\]

For \(p\ge5\), the three divisibility events are mutually exclusive.

## 2. Three exact local levels

If \(p\nmid x(x^2-4)\),

\[
B_p(x)=\beta_p.
\]

If \(p\mid x\),

\[
B_p(x)
=
\beta_p+2\alpha_p
=
\beta_p\frac{p-2}{p-4}.
\]

If \(p\mid x^2-4\),

\[
B_p(x)
=
\beta_p+\alpha_p
=
\beta_p\frac{p-3}{p-4}.
\]

Therefore define the finite correction functions

\[
Z(x)
=
\prod_{\substack{p\mid x\\p\ge5}}
\frac{p-2}{p-4}
\]

and

\[
R(N)
=
\prod_{\substack{p\mid N\\p\ge5}}
\frac{p-3}{p-4}.
\]

Only distinct prime divisors matter.

## 3. Universal background constant — OP-D064

Define

\[
\boxed{
C_*=
\prod_{p\ge5}\beta_p
=
\prod_{p\ge5}
\frac{p^3(p-4)}{(p-1)^4}.
}
\]

For \(p\ge5\),

\[
1-\beta_p
=
\frac{6p^2-4p+1}{(p-1)^4}
=
O(p^{-2}).
\]

Since

\[
\sum_p p^{-2}<\infty,
\]

the product converges absolutely in logarithmic form and

\[
\boxed{
0<C_*<\infty.
}
\]

Numerically, finite truncations approach approximately \(0.307495\); this numerical value is not used in the proof.

## 4. Instantaneous factorization theorem — OP-D065

For every integer \(x\ge6\) divisible by \(6\),

\[
\prod_{p\ge5}B_p(x)
=
C_*\,Z(x)\,R(x^2-4).
\]

Proof: outside the finite set of prime divisors of \(x(x^2-4)\), the local factor is exactly \(\beta_p\). At primes dividing \(x\), divide the generic background by the ratio \((p-2)/(p-4)\); at primes dividing \(x^2-4\), use \((p-3)/(p-4)\). The exceptional sets are disjoint for \(p\ge5\).

## 5. Restoring the carrier channels

For \(6\mid x\),

\[
\nu_2(H_x)=1,
\qquad
\nu_3(H_x)=2.
\]

Hence

\[
B_2(x)
=
\frac{1-1/2}{(1-1/2)^4}
=
8
\]

and

\[
B_3(x)
=
\frac{1-2/3}{(1-1/3)^4}
=
\frac{27}{16}.
\]

Therefore

\[
B_2(x)B_3(x)=\frac{27}{2}.
\]

The full singular series is exactly

\[
\boxed{
\mathfrak S(H_x)
=
\frac{27}{2}\,
C_*\,Z(x)\,R(x^2-4).
}
\]

This is an exact Euler-product factorization, not an asymptotic.

## 6. Dyadic orbit form — OP-D066

Now fix a twin-admissible base separation

\[
h\ge6,
\qquad
6\mid h,
\]

and set

\[
x_r=2^rh.
\]

The odd prime divisors of \(x_r\) are exactly the odd prime divisors of \(h\), so

\[
Z(x_r)=Z(h).
\]

Also

\[
x_r^2-4
=
4^r h^2-4.
\]

Therefore the entire dyadic singular-series orbit satisfies

\[
\boxed{
\mathfrak S(H_{2^rh})
=
\frac{27}{2}\,
C_*\,Z(h)\,
R(4^rh^2-4).
}
\]

Thus all time dependence is carried by the finite set of odd prime divisors of

\[
4^rh^2-4
=
(2^rh-2)(2^rh+2).
\]

The infinitely many generic prime channels have been compressed into the single universal constant \(C_*\).

## 7. Phase-hitting interpretation

For a prime \(p\ge5\),

\[
p\mid 4^rh^2-4
\]

iff

\[
2^rh\equiv\pm2\pmod p.
\]

Equivalently, the dyadic phase orbit hits one of the two special residues \(\pm2\).

Hence the finite correction factor \(R(4^rh^2-4)\) is exactly the product of amplitudes contributed by the special phase-hit channels at time \(r\).

Likewise \(Z(h)\) records the permanently zero-locked odd-prime channels.

## 8. Structural compression

The full instantaneous state of the standard two-twin-pair singular-series observable can therefore be written as

\[
\boxed{
\text{universal background}
\times
\text{static zero locks}
\times
\text{dynamic }\pm2\text{ phase hits}.
}
\]

Explicitly,

\[
\boxed{
\mathfrak S(H_{2^rh})
=
\underbrace{\frac{27}{2}C_*}_{\text{universal}}
\underbrace{Z(h)}_{\text{static}}
\underbrace{R(4^rh^2-4)}_{\text{dynamic}}.
}
\]

This is a lossless compression of the Euler product for this dyadic orbit.

## 9. Prior-art boundary

The Hardy--Littlewood singular series and its local factors are standard. The proof above is an exact algebraic specialization and factorization of those standard factors.

A targeted search has not established whether this precise dyadic factorized form has appeared previously. Therefore:

- mathematical identity: PROVED;
- literature novelty: NOT ESTABLISHED.

## 10. No-go

This theorem concerns the singular-series local-density weight. It does not prove that the corresponding prime quadruplets occur with the Hardy--Littlewood predicted asymptotic, nor does it prove infinitely many twin primes.
