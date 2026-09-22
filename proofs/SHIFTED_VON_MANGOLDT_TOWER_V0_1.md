# Shifted von Mangoldt Tower on `p+1` v0.1

For every integer \(n\ge1\), the classical divisor identity is
\[
\log n=\sum_{d\mid n}\Lambda(d).
\]
Since \(\Lambda(d)\) is nonzero exactly at prime powers, for every prime \(p\),
\[
\boxed{
\log(p+1)
=
\sum_{r\ \mathrm{prime}}
\sum_{j\ge1}
(\log r)\,\mathbf 1_{\{r^j\mid p+1\}}.
}
\]

Equivalently,
\[
r^j\mid p+1
\iff
p\equiv-1\pmod{r^j}.
\]

## Theorem 1 — exact shifted tower for the prime side

For \(\Re(s)>1\),
\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{r\ \mathrm{prime}}
\sum_{j\ge1}
(\log r)
\sum_{p\equiv-1\ (\mathrm{mod}\ r^j)}
\frac1{p^s-1}
-D(s),
}
\]
where
\[
D(s)=\sum_p\frac{\log(1+1/p)}{p^s-1}.
\]

**Proof.** Use
\[
\log p=\log(p+1)-\log(1+1/p)
\]
inside the absolutely convergent prime-side identity
\[
-\zeta'/\zeta(s)=\sum_p\frac{\log p}{p^s-1}.
\]
Then apply the finite divisor identity to \(p+1\). Absolute convergence for \(\Re(s)>1\) permits regrouping by \((r,j)\). \(\square\)

## Corollary 1.1 — dyadic sector as one base-prime channel

The previously defined dyadic contribution is exactly the \(r=2\) channel:
\[
\boxed{
(\log2)K(s)
=
(\log2)
\sum_{j\ge1}
\sum_{p\equiv-1\ (\mathrm{mod}\ 2^j)}
\frac1{p^s-1}.
}
\]

The fibre-label contribution is the complementary sum over odd base primes:
\[
\boxed{
A(s)
=
\sum_{r\ge3\ \mathrm{prime}}
\sum_{j\ge1}
(\log r)
\sum_{p\equiv-1\ (\mathrm{mod}\ r^j)}
\frac1{p^s-1}.
}
\]

Thus the earlier split
\[
(\log2)K+A
\]
is not a split between unrelated mechanisms. It is the decomposition of the single shifted-von-Mangoldt tower into its base-prime \(r=2\) channel and all odd base-prime channels.

## Theorem 2 — character decomposition at every modulus

For each prime power \(q=r^j\), the class \(-1\pmod q\) is reduced. Hence Dirichlet-character orthogonality gives
\[
\mathbf1_{\{p\equiv-1\pmod q\}}
=
\frac1{\varphi(q)}
\sum_{\chi\ (\mathrm{mod}\ q)}
\overline{\chi(-1)}\chi(p)
\]
for primes \(p\nmid q\). Since the target class is \(-1\), such a prime automatically satisfies \(p\nmid q\). Therefore every channel of the shifted tower admits a standard Dirichlet-character decomposition.

## Interpretation

This identifies the entire non-defect prime-log weight with a hierarchy of shifted residue classes modulo **all prime powers**, not only powers of two.

The numerical dominance of the old `A` sector is therefore expected structurally: it aggregates all odd base-prime channels.

## Research boundary

This is still an exact reindexing/transform in the half-plane of absolute convergence. A new RH-relevant result requires a nontrivial cancellation, positivity, or continuation theorem for the combined tower, not merely the identity itself.
