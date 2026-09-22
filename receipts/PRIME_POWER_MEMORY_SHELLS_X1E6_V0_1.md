# Numerical Receipt — Prime-Power Memory by Exact Dyadic Shell

Status: `NUMERICAL`.

For cutoff `X = 1,000,000`, using

\[
\mathcal M_X
=
\sum_{p^m\le X}
(\log p)p^{-m/2}(\log X-m\log p),
\]

the total computed memory is approximately

`3959.1526089937784`.

Contribution grouped by exact shell `k=v2(p+1)`:

| k | contribution | fraction of total |
|---:|---:|---:|
| 0 | 19.1627243673 | 0.00484011 |
| 1 | 1948.0701150087 | 0.49204219 |
| 2 | 1002.8210314045 | 0.25329184 |
| 3 | 500.3806912657 | 0.12638581 |
| 4 | 247.6924796102 | 0.06256199 |
| 5 | 125.1293236044 | 0.03160508 |
| 6 | 56.1888164694 | 0.01419213 |
| 7 | 33.0375132421 | 0.00834459 |
| 8 | 13.1798566427 | 0.00332896 |

The near-halving pattern for the first shells is consistent with the classical distribution of primes among fixed reduced residue classes modulo powers of two. This receipt is not a proof of a limiting shell law and gives no uniform-in-k asymptotic.

The same computation gives component ratios:

| component | fraction of total memory |
|---|---:|
| `(log 2) M_K` | 0.15948983 |
| `M_A` | 0.84554976 |
| `M_D` (subtracted) | 0.00503960 |

Thus at this cutoff the defect is small, while the fibre-label component is numerically dominant. This is evidence only.
