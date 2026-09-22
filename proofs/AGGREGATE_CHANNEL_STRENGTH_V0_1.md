# Aggregate Fixed-Channel Strength v0.1

For a prime base channel \(r\), the fixed-channel mean theorem gives
\[
c_r=\frac{r\log r}{(r-1)^2}.
\]
Define the aggregate strength up to \(R\) by
\[
C(R)=\sum_{r\le R\atop r\ \mathrm{prime}}c_r.
\]

## Theorem

\[
\boxed{
C(R)=\log R+O(1).
}
\]

### Proof

We have
\[
\frac{r}{(r-1)^2}
=
\frac1r
+
\left(
\frac{r}{(r-1)^2}-\frac1r
\right).
\]
The difference is
\[
\frac{2r-1}{r(r-1)^2}
=O(r^{-2}).
\]
Hence
\[
\sum_r
(\log r)
\left|
\frac{r}{(r-1)^2}-\frac1r
\right|
<\infty.
\]
Therefore
\[
C(R)
=
\sum_{r\le R}\frac{\log r}{r}
+O(1).
\]
The classical Mertens prime-sum estimate gives
\[
\sum_{r\le R}\frac{\log r}{r}
=
\log R+O(1),
\]
which proves the claim. \(\square\)

## Corollary — no finite-channel closure

For every fixed finite set of base-prime channels, the asymptotic mean logarithmic contribution is finite. But the aggregate channel strength required as the channel cutoff grows is unbounded, with logarithmic growth.

Thus no theorem that keeps only a fixed finite list of base primes \(r\) can asymptotically reconstruct the full shifted weight
\[
\log(p+1)
=
\sum_r v_r(p+1)\log r.
\]

## Iterated-limit statement

For fixed \(R\), the fixed-channel mean theorem yields
\[
\lim_{x\to\infty}
\frac1{\pi(x)}
\sum_{p\le x}
\sum_{r\le R}v_r(p+1)\log r
=
C(R).
\]
Hence
\[
\lim_{R\to\infty}
\frac1{\log R}
\left(
\lim_{x\to\infty}
\frac1{\pi(x)}
\sum_{p\le x}
\sum_{r\le R}v_r(p+1)\log r
\right)
=1.
\]

## Scope firewall

This is an **iterated** limit. It does not supply a uniform theorem for a channel cutoff \(R=R(x)\) growing with \(x\). Establishing useful joint uniformity would require stronger distribution estimates for primes in arithmetic progressions across many prime-power moduli.
