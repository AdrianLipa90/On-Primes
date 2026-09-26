# ARPL Quadratic Clock and Subcritical Fractional Moments — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Quadratic clock checks at h=6

For p in {5,7,11,13,17,19,23,29,31,37,41,43}:

- ord_p(4) == ord_p(2)/gcd(ord_p(2),2): PASS.
- the old +/-2 hit residues modulo ord_p(2) collapse to either:
  - one residue modulo ord_p(4), or
  - no residue for an inactive channel.
- exact compressed hit density is 1/ord_p(4) on active channels.
- pair joint densities from the compressed one-phase CRT formula match the previous direct signed-clock densities.

Examples at h=6:
p=5:  ord_2=4,  ord_4=2,  old hits {1,3} -> phase 1 mod 2.
p=7:  ord_2=3,  ord_4=3,  old hit {1}   -> phase 1 mod 3.
p=11: ord_2=10, ord_4=5,  old hits {2,7} -> phase 2 mod 5.
p=13: ord_2=12, ord_4=6,  old hits {2,8} -> phase 2 mod 6.

## Fractional finite-support reverse test

Direct common-clock means were compared with the subset/CRT expansion.

Support {5,7,11}:
s=0.25 -> 1.1294280016576699 vs 1.1294280016576697
s=0.50 -> 1.2868819646960488 vs 1.2868819646960488
s=0.90 -> 1.6144016739595406 vs 1.6144016739595400

Support {5,7,11,13}:
s=0.25 -> 1.1339065520117204 vs 1.1339065520117202
s=0.50 -> 1.2960218842142541 vs 1.2960218842142541
s=0.90 -> 1.6314027001744138 vs 1.6314027001744134

Support {7,13,19}:
s=0.25 -> 1.0311363888588900 vs 1.0311363888588903
s=0.50 -> 1.0643247779970393 vs 1.0643247779970393
s=0.90 -> 1.1220604870363344 vs 1.1220604870363344

All differences are floating roundoff.

## Proven global theorem

For every fixed admissible h and every 0<s<1:

- the all-orders compatible-subset series converges absolutely;
- the Cesaro mean of R(4^r h^2-4)^s exists;
- the Cesaro mean of the full singular series^s exists and is finite;
- the result is invariant under h -> 2^k h.

The proof uses the exact one-phase base-4 clock, CRT density 1/lcm(e_p),
the divisibility product bound prod_{p in J} p | 4^L-1, and an integral
majorant whose small-t behavior is t^{-c} with s<c<1.

## Critical endpoint

At s=1 the same unconditional majorant becomes t^{-1}; therefore this proof
does not settle the raw arithmetic mean.

SUBCRITICAL_ALL_ORDERS = PROVED
S_EQ_1_ARITHMETIC_MEAN = OPEN
NOVELTY = NOT_ESTABLISHED

## Runtime boundary

The connected GitHub app remained operational.
A full container checkout/test suite remains blocked by DNS resolution for github.com.
No CI PASS is claimed.
