# ARPL Fixed-Order Connected Summability — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact finite checks

For h=6, the new resonance moment bound and connected-cumulant bound were checked on:

- pairs: {5,7}, {7,13}, {13,19}
- triples: {7,13,19}, {5,7,11}
- quadruple: {7,13,19,37}

All tested exact-rational values satisfied

|M_X(J;h)| <= 2^|J| * prod(alpha_p) / lcm(d_p)

and

|K(J;h)| <= Bell(|J|)(|J|-1)! 2^|J| prod(alpha_p) / max(d_p).

An inactive channel was also verified to force the corresponding centered joint moment to zero.

## Additional finite layer scans at h=6

Connected 2-body partial sums:

P<=30  : -0.005611162187224146
P<=50  : -0.005771085469184211
P<=70  : -0.005876875031301710
P<=100 : -0.005833633470080615

Connected 3-body partial sums:

P<=30 : 0.000310113106718209
P<=50 : 0.000250824473747904
P<=70 : 0.000283552102017796

These scans are illustrative only; convergence is established by the analytic bound, not by numerical stabilization.

## Proof ingredients

- exact local Fourier defect amplitudes;
- exact resonance-kernel size prod(d_p)/lcm(d_p);
- moment-cumulant Möbius inversion;
- alpha_p = O(1/p);
- ord_p(2) >= log_2(p+1);
- Mertens bound sum_{p<=x} 1/p = O(log log x);
- standard prime-counting upper bound pi(x) = O(x/log x).

## Verdict

FIXED_ORDER_N_BODY_GLOBAL_LAYER = ABSOLUTELY_CONVERGENT for every fixed n>=2
ALL_ORDERS_CLUSTER_SUM = OPEN
NOVELTY = NOT_ESTABLISHED
