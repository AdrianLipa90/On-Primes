# ARPL Connected Resonance Expansion — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact checks

1. Pair cumulant identity:
   for supports {5,7}, {7,13}, {13,19} at h=6,
   K({p,q};h) == dyadic resonance correction.
   PASS.

2. Period-component factorization:
   support {7,13,31}, h=6
   effective periods: 3,12,5
   components: {7,13} and {31}
   M({7,13,31};6) == M({7,13};6) * M({31};6)
   PASS.

3. Genuine connected three-channel term:
   K({7,13,19};6)
   = -5168743489 / 457019805007872
   != 0.
   PASS.

4. Control triple:
   K({5,7,11};6) = 0.
   PASS.

All arithmetic above is exact rational arithmetic.

## Structural result

The period-overlap graph gives an exact pruning rule:
a connected resonance cumulant cannot span distinct connected components of
p ~ q iff gcd(d_p(h), d_q(h)) > 1.

The graph is an upper envelope only. Local Fourier mode filters can make
connected weights vanish inside a component.

## Epistemic status

FINITE_CONNECTED_EXPANSION = PROVED
COMPONENT_FACTORIZATION = PROVED
INFINITE_CLUSTER_CONVERGENCE = OPEN
NOVELTY = NOT_ESTABLISHED

Full repository suite after latest commits remains NOT_RUN because container DNS cannot resolve github.com.
