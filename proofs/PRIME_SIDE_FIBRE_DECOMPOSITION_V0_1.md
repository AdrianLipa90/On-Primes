# Fibre Decomposition of the Prime Side v0.1

Let
\[
p+1=a2^k,\qquad a\ \text{odd},\quad k=v_2(p+1).
\]
By uniqueness of the dyadic address, every prime belongs to exactly one pair \((a,k)\).

## Theorem 1 — finite exact reindexing

For every complex \(s\) for which the denominators below are nonzero and every finite prime cutoff \(P\),
\[
\sum_{p\le P}\frac{\log p}{p^s-1}
=
\sum_{\substack{a\ \mathrm{odd}\ge1}}
\sum_{\substack{k\ge0\\p=a2^k-1\le P\\p\in\mathbb P}}
\frac{\log p}{p^s-1}.
\]

**Proof.** The map \(p\mapsto(a,k)\) is bijective from primes \(p\le P\) to the set of prime-valued dyadic addresses satisfying the cutoff. The right-hand side is therefore a finite reindexing of the left-hand side. \(\square\)

## Theorem 2 — infinite fibre decomposition for Re(s) > 1

For \(\sigma=\Re(s)>1\),
\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{\substack{a\ \mathrm{odd}\ge1}}
\sum_{\substack{k\ge0\\a2^k-1\in\mathbb P}}
\frac{\log(a2^k-1)}{(a2^k-1)^s-1}
}
\]
with absolute convergence.

**Proof.** For \(\sigma>1\), the classical Euler-product logarithmic derivative gives
\[
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_p\sum_{m\ge1}(\log p)p^{-ms}
=
\sum_p\frac{\log p}{p^s-1}.
\]
The absolute values are dominated by a constant multiple of \((\log p)p^{-\sigma}\), whose prime sum converges for \(\sigma>1\). Therefore absolute convergence permits reindexing by the unique dyadic address of each prime. \(\square\)

## Corollary 2.1 — unique boundary term

The layer \(k=0\) contains only the prime \(2\). Therefore, for \(\Re(s)>1\),
\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
\frac{\log2}{2^s-1}
+
\sum_{\substack{a\ \mathrm{odd}\ge1}}
\sum_{\substack{k\ge1\\a2^k-1\in\mathbb P}}
\frac{\log(a2^k-1)}{(a2^k-1)^s-1}
}
\]

The appearance of \(\log2\) here is forced by the unique even prime on the dyadic boundary; it is not inserted as an external parameter.

## Theorem 3 — finite von Mangoldt prime-power reindexing

For every finite cutoff \(X\),
\[
\sum_{n\le X}\frac{\Lambda(n)}{n^s}
=
\sum_{\substack{a\ \mathrm{odd}\ge1}}
\sum_{\substack{k\ge0\\p=a2^k-1\in\mathbb P}}
\sum_{\substack{m\ge1\\p^m\le X}}
(\log p)p^{-ms}.
\]

**Proof.** The support of \(\Lambda\) is exactly the prime powers, with \(\Lambda(p^m)=\log p\). Reindex the underlying primes by their unique dyadic addresses. Since the cutoff is finite, no convergence issue occurs. \(\square\)

## Research boundary

These identities are exact coordinate decompositions. By themselves they do not provide new zero-free regions, a proof of RH, or a characterization of the prime masks. Their value is that every prime-side analytic quantity can now be separated into fibre contributions with a distinguished dyadic boundary term.
