# Numerical Receipt — Fibre `a = 3` finite modular sieve

Status: `NUMERICAL`.

The exact theorem guarantees periodicity for any fixed finite divisor set. The values below are finite computations of the exact residue union and are **not** asymptotic statements about primes.

| Odd prime divisors used | Exact period `L` | Removed residues | Survivor residues | Survivor density |
|---:|---:|---:|---:|---:|
| first 3: 3..7 | 12 | 3 | 9 | 0.7500000000 |
| first 5: 3..13 | 60 | 25 | 35 | 0.5833333333 |
| first 8: 3..23 | 3960 | 1960 | 2000 | 0.5050505051 |
| first 12: 3..41 | 27720 | 15080 | 12640 | 0.4559884560 |
| first 15: 3..53 | 8288280 | 4778840 | 3509440 | 0.4234219886 |

Reproduction:

```bash
python experiments/fibre_sieve_profile.py --a 3 --prime-limit 53
```

Interpretation firewall: decreasing finite-sieve survivor density does not prove that the true prime mask has any limiting density in `k`, nor that the sieve closes all composite classes.
