# ARPL Global Dyadic Orbit Invariant — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact identities checked

For primes p in {5,7,11,13,17,19,23,29,31,37,41,43} and h in {6,12,18,30,42}:

- closed-form local orbit mean == direct exact orbit average: PASS
- local class belongs to {zero-fixed, special-even, special-odd, ordinary}: PASS

For finite support
{5,7,11,13,17,19,23,29,31}
and h in {6,18,30,42,66}:

- I_P(2^k h) == I_P(h) for k=0..7: PASS
- arithmetic used exact fractions

## Convergence illustration for h=6

Prime cutoff -> finite product of local orbit means

100   -> 0.5548091709609418
200   -> 0.5520054504165318
500   -> 0.5508141210259084
1000  -> 0.5504696762697121
2000  -> 0.5503050937246090
5000  -> 0.5502185828395376
10000 -> 0.5501934372310352

The numerical trend is not used to prove convergence.

## Proof basis

For all but finitely many p (namely p not dividing fixed nonzero h):

|mu_p(h)-1|
<= O(1/p^2) + O(1/(p*ord_p(2))).

Since p divides 2^ord_p(2)-1,

ord_p(2) >= log_2(p+1).

Therefore

|mu_p(h)-1|
<= O(1/p^2) + O(1/(p log p)),

and the corresponding prime sums converge.

## Verdict

GLOBAL_INDEPENDENT_ORBIT_BASELINE = PROVED_CONVERGENT
DYADIC_INVARIANCE = PROVED
FULLY_COUPLED_INFINITE_COMMON_CLOCK_LIMIT = OPEN

Full repository suite after the latest commits remains NOT_RUN because the container cannot resolve github.com for checkout. No CI PASS is claimed.
