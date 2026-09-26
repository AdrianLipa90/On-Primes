# ARPL Instantaneous Singular-Series Factorization — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact finite regression

For support
{5,7,11,13,17,19,23,29,31},
for h in {6,18,30,42,66},
and r=0..7:

direct product prod_p B_p(2^r h)
==
baseline product prod_p beta_p
times zero-lock correction over p|h
times special correction over p|(4^r h^2-4).

PASS for every tested case with exact rational arithmetic.

Local ratios were independently checked:

B_p(0)/beta_p = (p-2)/(p-4)
B_p(+/-2)/beta_p = (p-3)/(p-4)

for p in {5,7,11,13,17,19}.

## Universal background truncations

P<=100    : C_*(P) = 0.3109330901148510
P<=1000   : C_*(P) = 0.3077296754643222
P<=10000  : C_*(P) = 0.3075129921066124
P<=100000 : C_*(P) = 0.3074963589121366
P<=500000 : C_*(P) = 0.3074951410201474

The numerical values illustrate convergence only.

## Exact theorem

For h>=6, 6|h and r>=0:

S(H_{2^r h})
=
(27/2) C_* Z(h) R(4^r h^2-4).

All dynamic dependence is therefore carried by the finite prime-divisor set of
4^r h^2-4, equivalently by phase hits 2^r h == +/-2 mod p.

## Status

IDENTITY = PROVED
UNIVERSAL_BACKGROUND_CONVERGENCE = PROVED
NOVELTY = NOT_ESTABLISHED
HARDY_LITTLEWOOD_OCCURRENCE_ASYMPTOTIC = CONJECTURAL / NOT USED
