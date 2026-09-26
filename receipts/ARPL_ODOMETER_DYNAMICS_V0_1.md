# ARPL Odometer Dynamics — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Closed structural identification

The active base-4 clock tower is

K_h = inverse_limit Z/L_N Z,

with

L_N = lcm(e_{p_1},...,e_{p_N}),
e_p = ord_p(4),

and dynamics given by +1 on every finite quotient.

Therefore the global ARPL phase clock is a procyclic odometer / adding machine.

## Consequences

- minimality: PROVED / standard compact-group rotation consequence
- unique ergodicity: PROVED / Haar is the unique invariant probability
- equicontinuity: PROVED
- topological entropy: 0
- Haar Kolmogorov-Sinai entropy: 0
- Koopman spectrum: pure point
- eigenvalue-frequency module:
  union_N (1/L_N) Z/Z
- original integer dyadic time:
  orbit of the topological generator

## Interpretation firewall

The finite quotient Shannon information

H_N = log L_N

can diverge while the dynamical entropy rate remains zero.

Therefore H_N is phase-resolution information, not entropy production.

## Boundary

ODOMETER_THEORY = STANDARD
ARPL_PERIOD_DATA = PROJECT_SPECIFIC
OBSERVABLE_SPECTRAL_SUPPORT = SUBSET_OF_SYSTEM_SPECTRUM
FULL_PUSHFORWARD_ATOMLESSNESS = OPEN
