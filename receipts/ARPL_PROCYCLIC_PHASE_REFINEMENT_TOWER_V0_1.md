# ARPL Procyclic Phase Refinement Tower — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact finite tower example at h=6

Channels added in order:
5, 7, 11, 13, 19, 31, 37

Their base-4 observable periods e_p=ord_p(4):

p=5  -> e_p=2
p=7  -> e_p=3
p=11 -> e_p=5
p=13 -> e_p=6
p=19 -> e_p=9
p=31 -> e_p=5
p=37 -> e_p=18

Cumulative refinement clocks L_N=lcm(e_1,...,e_N)
and exact branching b_N=L_N/L_{N-1}:

p=5  : L=2,  b=2
p=7  : L=6,  b=3
p=11 : L=30, b=5
p=13 : L=30, b=1
p=19 : L=90, b=3
p=31 : L=90, b=1
p=37 : L=90, b=1

The b=1 cases demonstrate exact channel redundancy at the clock-resolution level:
the new channel can add a new pulse target/weight without refining the global time quotient.

## Encoded regression

tests/test_phase_law.py now checks:

- L_N = lcm(L_{N-1}, e_p);
- b_N = L_N/L_{N-1};
- b_N = e_p/gcd(e_p,L_{N-1});
- finite phase-hull cardinality = final L_N.

## Structural status

FINITE_DIAGONAL_GROUP = PROVED
INVERSE_LIMIT_PHASE_HULL = PROVED
UNIFORM_HAAR_REFINEMENT = PROVED
DUAL_RATIONAL_FREQUENCY_MODULE = PROVED
REFINEMENT_GRAPH_BOUNDARY = PROVED

METRIC_FRACTAL_DIMENSION = NOT_DEFINED / NOT_CLAIMED
PUSHFORWARD_LAW_ATOMLESSNESS = OPEN
