# Numerical Receipt — Fixed-Channel Mean Valuations at X = 10^6

Status: `NUMERICAL`, compared against the proved fixed-channel limit.

For primes `p <= 1,000,000`, compute

\[
\overline v_r(X)=\frac1{\pi(X)}\sum_{p\le X}v_r(p+1).
\]

| r | finite mean | theorem limit `r/(r-1)^2` | ratio |
|---:|---:|---:|---:|
| 2 | 2.00295549 | 2.00000000 | 1.00148 |
| 3 | 0.75105098 | 0.75000000 | 1.00140 |
| 5 | 0.31204617 | 0.31250000 | 0.99855 |
| 7 | 0.19447629 | 0.19444444 | 1.00016 |
| 11 | 0.11013019 | 0.11000000 | 1.00118 |
| 13 | 0.09019338 | 0.09027778 | 0.99907 |
| 17 | 0.06615455 | 0.06640625 | 0.99621 |
| 19 | 0.05935183 | 0.05864198 | 1.01210 |

The finite data are consistent with the fixed-channel theorem. No statement about uniformity in growing `r` is inferred.