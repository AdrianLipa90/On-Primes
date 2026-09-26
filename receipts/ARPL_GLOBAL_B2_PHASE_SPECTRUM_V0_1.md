# ARPL Global B2 Phase Spectrum — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Independent finite checks

At h=6:

1. Direct common-period variance versus exact density/covariance formula

Support {5,7,11}
- common period: 60
- direct variance: 0.14135748246573873
- density/covariance variance: 0.14135748246573873
- PASS

Support {5,7,11,13,17,19}
- common period: 360
- direct variance: 0.12689949458587008
- density/covariance variance: 0.12689949458587008
- PASS

2. Finite Fourier--Bohr Parseval

Prime cutoff 20:
- variance: 0.12689949458587008
- aggregated nonzero rational-frequency power: 0.12689949458587008
- PASS

Prime cutoff 50:
- variance: 0.12852640186696918
- aggregated nonzero rational-frequency power: 0.12852640186696918
- PASS

3. Variance truncations at h=6

P<=50   : 0.12852640186696918
P<=100  : 0.12856744369147408
P<=200  : 0.12872268022266680
P<=500  : 0.12876255535933653
P<=1000 : 0.12876890801442376

These truncations illustrate the proved mean-square convergence; they are not the proof.

## Proven control

The actual logarithmic tail A_P(r)=sum_{p>P} w_p E_p(r) satisfies

lim_{P->infinity} limsup_{T->infinity}
(1/T) sum_{r<T} A_P(r)^2 = 0.

The proof uses:
- <=2 hit classes per local period d_p;
- <=4 simultaneous hit classes modulo lcm(d_p,d_q);
- w_p = O(1/p);
- d_p >= log_2(p+1);
- reciprocal-prime Mertens bounds;
- pi(x)=O(x/log x);
- finite-horizon endpoint control through the divisor set of
  prod_{r<T}(4^r h^2-4).

## Status

GLOBAL_B2_LOG_FIELD = PROVED
GLOBAL_LOG_VARIANCE = PROVED_FINITE
PURE_POINT_RATIONAL_PHASE_SPECTRUM = PROVED/STANDARD_B2
PARSEVAL_POWER_IDENTITY = PROVED/STANDARD_B2
ARITHMETIC_MEAN_OF_RAW_SINGULAR_SERIES = OPEN
NOVELTY = NOT_ESTABLISHED

## Runtime test boundary

A full repository checkout/test run was attempted again on 2026-09-26 and failed before checkout because the container could not resolve github.com:

Could not resolve host: github.com

GitHub connector reads/writes remained operational.

FULL_REPO_TEST_SUITE_AFTER_LATEST_COMMITS = NOT_RUN
No CI PASS is claimed.
