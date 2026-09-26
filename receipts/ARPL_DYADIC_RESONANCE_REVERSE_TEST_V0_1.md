# ARPL Dyadic Resonance Reverse Test v0.1 — receipt

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact finite checks performed in-session

For h=6:

1. P={5,7}
   - local periods: 4,3
   - pairwise coprime: yes
   - resonance correction: exactly 0
   - global mean / product(local means): exactly 1

2. P={7,13}
   - local periods: 3,12
   - pairwise coprime: no
   - resonance correction:
     -753571 / 483729408
   - global mean / product(local means):
     549 / 550

3. P={7,13,19}
   - common period: 36
   - resonance correction:
     -222255970027 / 114254951251968
   - global mean / product(local means):
     18657 / 18700

4. P={5,13,17}
   - common period: 24
   - resonance correction:
     -17540024125 / 4174708211712
   - global mean / product(local means):
     164 / 165

All values above were computed with exact rational arithmetic.

## Result

PASS for the finite theorem:

- a shared dyadic clock can create exact cross-channel coupling between local singular-series observables;
- pairwise-coprime local periods force exact factorization;
- shared period factors are necessary but not sufficient for coupling because local Fourier mode support also matters;
- the correction is deterministic and phase-resonant, not an empirical covariance.

## Runtime validation boundary

The new identities were independently recomputed in-session with exact rational arithmetic.

A full repository checkout/test run could not be performed from the container because DNS resolution for github.com failed. GitHub repository writes and reads through the connected GitHub app succeeded. Therefore:

NEW_MATH_REVERSE_TEST = PASS
FULL_REPO_TEST_SUITE_AFTER_LATEST_COMMITS = NOT_RUN
FAILURE_REASON = container DNS resolution for github.com

No CI PASS is claimed.
