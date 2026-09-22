# Finite Fibre Sieve Theorem v0.1

Fix an odd positive fibre label \(a\) and a finite set \(R\) of odd primes.
For each \(r\in R\) for which a modular obstruction exists, write
\[
k\equiv k_r\pmod{d_r},
\qquad d_r=\operatorname{ord}_r(2).
\]

Define
\[
L_R=\operatorname{lcm}_{r\in R} d_r.
\]

## Theorem 1 — exact finite-sieve periodicity

The union of all modular obstruction classes induced by \(R\) is periodic modulo \(L_R\).

**Proof.** Each obstruction set is a congruence class modulo \(d_r\), hence is invariant under translation by every multiple of \(d_r\). Since \(L_R\) is a common multiple of all \(d_r\), every obstruction set, and therefore their union, is invariant under translation by \(L_R\). \(\square\)

## Corollary 1.1 — exact survivor density

Let \(S_R(a)\subset\{0,\dots,L_R-1\}\) be the residue classes not removed by any obstruction in \(R\). Then the periodic survivor set has exact natural density
\[
\boxed{
\delta_R(a)=\frac{|S_R(a)|}{L_R}.
}
\]

No independence assumption between divisibility conditions is used; overlaps are handled exactly by the union of residue classes.

## Theorem 2 — eventual compositeness on removed classes

For a removed residue class associated with a prime \(r\in R\), every fibre value
\[
x_{a,k}=a2^k-1
\]
in that class is divisible by \(r\). Once \(x_{a,k}>r\), it is composite.

Thus the finite sieve has two logically separate outputs:

1. an exact periodic set of indices removed by modular divisibility;
2. finitely many small equality exceptions where \(x_{a,k}=r\).

## Interpretation

The finite sieve does not characterize primes. It produces an exact periodic **necessary condition** for primality within a fibre. Increasing \(R\) can only remove survivor classes; it cannot create false compositeness certificates when the proper-divisor check is retained.
