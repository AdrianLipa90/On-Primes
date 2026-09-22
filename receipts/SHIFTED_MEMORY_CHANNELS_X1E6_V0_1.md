# Numerical Receipt — Shifted Mangoldt Memory Channels at X = 10^6

Status: `NUMERICAL`.

Using
\[
\mathcal M_X
=
\sum_{p^m\le X}
(\log p)p^{-m/2}(\log X-m\log p)
\]
with `X = 1,000,000`, the direct total is

`3959.1526089937784`.

The shifted-channel sum before defect subtraction is

`3979.105146991203`,

and the defect memory is

`19.95253799741499`,

so

`3979.105146991203 - 19.95253799741499 = 3959.1526089937884`,

agreeing with the direct memory to floating-point precision.

Top base-prime channels:

| r | channel contribution | fraction of direct memory |
|---:|---:|---:|
| 2 | 631.4445903415 | 0.15948983 |
| 3 | 391.6271444021 | 0.09891691 |
| 5 | 206.2167469538 | 0.05208608 |
| 7 | 161.3936597100 | 0.04076470 |
| 11 | 109.1023131833 | 0.02755699 |
| 13 | 90.7982904299 | 0.02293377 |
| 19 | 75.0875159298 | 0.01896555 |
| 17 | 74.4892048289 | 0.01881443 |
| 23 | 57.1819524215 | 0.01444298 |
| 31 | 48.7402499973 | 0.01231078 |
| 29 | 46.7597500304 | 0.01181054 |
| 37 | 40.7043679351 | 0.01028108 |
| 41 | 36.7537656918 | 0.00928324 |
| 43 | 35.0258037446 | 0.00884679 |
| 47 | 32.7606747237 | 0.00827467 |

The `r=2` channel is the largest single channel, but the aggregate of odd channels is dominant. The top 20 channels together account for about `0.54678` of the direct memory.

Interpretation firewall: this is a finite weighted-memory profile, not a limiting distribution theorem.