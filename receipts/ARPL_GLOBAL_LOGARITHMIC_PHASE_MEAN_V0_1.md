# ARPL Global Logarithmic Phase Mean — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact local checks

For p in {5,7,11,13,17,19,23,29,31}
and h in {6,18,30,42,66}:

- direct exact-period mean of log B_p(2^r h)
  == closed-form log(beta_p) + delta_p(h) log((p-3)/(p-4)),
  with the zero-fixed correction used when p|h.
- PASS to 12 decimal places.

Special-hit densities were checked against direct orbit counting:
delta_p(h) in {0, 1/d_p, 2/d_p}.
PASS.

Finite-support geometric log means were checked under h -> 2^k h:
PASS for k=0..5.

## Numerical illustration for h=6

Prime cutoff -> geometric mean truncation

100   -> 6.976241285900126
500   -> 6.925959309575955
1000  -> 6.921626929352987
5000  -> 6.918469286505420
10000 -> 6.918153093210670

These numbers are illustrative only.

## Proven theorem

The Cesaro mean

L(h) = lim_{T->infinity} (1/T) sum_{r<T} log S(H_{2^r h})

exists and is finite.

The geometric mean G(h)=exp(L(h)) is positive, finite and invariant under h -> 2^k h.

Jensen gives the unconditional lower bound

liminf_T (1/T) sum_{r<T} S(H_{2^r h}) >= G(h) > 0.

## Status

GLOBAL_LOG_MEAN = PROVED
GLOBAL_GEOMETRIC_MEAN = PROVED
ARITHMETIC_MEAN_EXISTENCE = OPEN
NOVELTY = NOT_ESTABLISHED
