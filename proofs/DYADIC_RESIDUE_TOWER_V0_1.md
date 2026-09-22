# Dyadic Residue Tower v0.1

For every prime \(p\), let
\[
k_p=v_2(p+1).
\]

## Theorem 1 — valuation as nested residue count

\[
\boxed{
k_p
=
\sum_{j\ge1}
\mathbf 1_{\{p\equiv-1\pmod{2^j}\}}.
}
\]

**Proof.** The congruence \(p\equiv-1\pmod{2^j}\) is equivalent to \(2^j\mid p+1\). This holds exactly for \(j=1,\dots,v_2(p+1)\). \(\square\)

## Corollary 1.1 — finite dyadic moment tower

For every finite prime cutoff \(P\),
\[
\boxed{
\sum_{p\le P}\frac{v_2(p+1)}{p^s-1}
=
\sum_{j\ge1}
\sum_{\substack{p\le P\\p\equiv-1\ (\mathrm{mod}\ 2^j)}}
\frac{1}{p^s-1}.
}
\]
The outer sum is finite because \(2^j\le p+1\le P+1\).

## Theorem 2 — infinite tower for Re(s) > 1

For \(\Re(s)>1\),
\[
\boxed{
K(s)
=
\sum_{j\ge1}
\sum_{p\equiv-1\ (\mathrm{mod}\ 2^j)}
\frac{1}{p^s-1},
}
\]
where
\[
K(s)=\sum_p\frac{v_2(p+1)}{p^s-1}.
\]

Absolute convergence follows from
\[
v_2(p+1)\le\log_2(p+1)
\]
and comparison with \(\sum_p (\log p)p^{-\sigma}\) for \(\sigma>1\). Hence the order of summation can be exchanged.

## Consequence for the prime-side decomposition

Combining with
\[
-\frac{\zeta'}{\zeta}(s)
=(\log2)K(s)+A(s)-D(s)
\]
gives an exact representation in which the coefficient \(\log2\) multiplies a nested hierarchy of prime residue classes modulo powers of two.

## Research boundary

Distribution of primes in these residue classes belongs to classical analytic number theory. This identity alone does not improve known error terms or prove RH. Its role is to identify the dyadic moment with a concrete arithmetic-progression observable rather than an abstract coordinate.
