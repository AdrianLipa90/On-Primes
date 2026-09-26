# ARPL Entire Phase-Moment and Limiting-Law Receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Provenance audit

The quantitative multiplicative-order input used to close the all-real endpoint was rechecked against external literature.

- Erdos--Murty, On the Order of a (mod p), Theorem 5(2), contains the quantitative rank-one form needed by ARPL.
- Later literature also attributes the fixed-base bound
  ord_p(a) >= sqrt(p) exp((log p)^delta)
  outside O(x/log^(1+alpha) x) primes
  to Pappalardi.

The earlier CLAIMS/PRIOR_ART reference to "Theorem 3" was corrected.

## Independent finite complex checks

For h=6 and supports

{5,7}
{7,13}
{7,13,19}
{5,7,11,13}

the direct finite common-clock complex mean was compared with the generalized-CRT subset expansion at

z = 0.5 + 0.7 i
z = 2.3 i
z = -1.2 + 0.4 i
z = 2

Maximum observed absolute discrepancy:
6.69e-16

This is floating-point roundoff scale.

Additional checks encoded in tests/test_phase_law.py:

- conjugate symmetry M(-it)=conjugate(M(it)) on the imaginary axis;
- complex transform restricted to the real axis equals the existing real-moment implementation;
- finite phase-hull cardinality equals lcm of the base-4 channel periods.

Example finite hull sizes at h=6:

support {5,7,13}: periods {2,3,6}, hull size 6
support {7,13,19}: periods {3,6,9}, hull size 18
support {5,7,11,13}: periods {2,3,5,6}, hull size 30

## Theorem status

COMPLEX_SUBSET_SERIES_LOCAL_UNIFORM_CONVERGENCE = PROVED
ENTIRE_CESARO_MOMENT_TRANSFORM = PROVED
EMPIRICAL_LOG_LAW_WEAK_CONVERGENCE = PROVED
BILATERAL_LAPLACE_TRANSFORM_IDENTITY = PROVED
PROCYCLIC_HAAR_PHASE_MODEL = PROVED
FULL_LIMIT_LAW_DYADIC_INVARIANCE = PROVED
LITERATURE_NOVELTY = NOT_ESTABLISHED

## Runtime boundary

The targeted identities were independently recomputed in-session.
The new Python tests were written to the branch.
A full repository test suite was not executed from a checkout in this step, so no new full-CI PASS is claimed.
