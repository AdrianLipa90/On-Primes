# Shifted von Mangoldt Decomposition of Prime-Power Memory v0.1

Let
\[
W_{p,m}(t)=p^{-m/2}(t-m\log p)\mathbf1_{m\log p\le t}.
\]
For every finite \(t\),
\[
\mathcal M(t)=\sum_{p,m}(\log p)W_{p,m}(t).
\]

Using
\[
\log p
=
\sum_{r^j\mid p+1}\log r
-\delta_p,
\qquad
\delta_p=\log(1+1/p),
\]
define, for every base prime \(r\),
\[
\mathcal C_r(t)
=
(\log r)
\sum_{j\ge1}
\sum_{\substack{p,m\\r^j\mid p+1}}
W_{p,m}(t),
\]
and
\[
\mathcal D(t)=\sum_{p,m}\delta_p W_{p,m}(t).
\]

## Theorem — exact channel decomposition

For every finite \(t\ge0\),
\[
\boxed{
\mathcal M(t)
=
\sum_{r\ \mathrm{prime}}\mathcal C_r(t)
-\mathcal D(t).
}
\]

All sums are finite at fixed \(t\), so no analytic-continuation or rearrangement issue occurs.

## Positivity

Every channel satisfies
\[
\mathcal C_r(t)\ge0,
\qquad
\mathcal D(t)\ge0.
\]

The previous dyadic memory contribution is exactly
\[
\mathcal C_2(t)=(\log2)\mathcal M_K(t),
\]
while
\[
\sum_{r\ge3}\mathcal C_r(t)=\mathcal M_A(t).
\]

Thus the former `K/A` split is simply

\[
\text{channel }r=2
\quad\text{versus}\quad
\text{all channels }r\ge3.
\]

## Residue-class form

Because
\[
r^j\mid p+1
\iff
p\equiv-1\pmod{r^j},
\]
each channel is a positive memory accumulated from one hierarchy of shifted prime residue classes.

## Research relevance

This form is better suited to inequalities than the old `A/K/D` split: each \(\mathcal C_r\) is individually nonnegative and has a direct arithmetic-progression interpretation. A future RH-relevant theorem would need to compare the total channel reserve against the exact archimedean term in an RH-equivalent explicit-formula criterion.
