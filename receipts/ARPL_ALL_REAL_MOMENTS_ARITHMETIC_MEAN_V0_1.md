# ARPL All Real Moments / Arithmetic Mean — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## External theorem provenance

Erdős--Murty, Theorem 3:
for fixed a>1 there exist alpha, delta>0 such that

ord_p(a) >= sqrt(p) exp((log p)^delta)

for all but O(x/(log x)^(1+alpha)) primes p<=x.

ARPL uses a=2. This is STANDARD external mathematics and is not credited as an ARPL theorem.

## Finite direct-clock versus CRT-subset checks at h=6

Support {5,7,11}

s=-2.0 : 0.5088297526041667 == 0.5088297526041667
s=-0.5 : 0.8049021501834347 == 0.8049021501834347
s= 0.0 : 1.0000000000000000 == 1.0000000000000000
s= 1.0 : 1.7142857142857144 ~= 1.7142857142857142
s= 2.0 : 3.3408919123204837 ~= 3.3408919123204830
s= 4.0 : 16.685811638840466 == 16.685811638840466

Support {5,7,11,13}

s=-2.0 : 0.47864746093750005 == 0.47864746093750005
s=-0.5 : 0.7964598439492185 ~= 0.7964598439492184
s= 0.0 : 1.0000000000000000 == 1.0000000000000000
s= 1.0 : 1.7333333333333334 == 1.7333333333333334
s= 2.0 : 3.382380112538842 == 3.382380112538842
s= 4.0 : 16.785505700589663 == 16.785505700589663

Support {7,13,19}

s=-2.0 : 0.8103233506944445 ~= 0.8103233506944444
s=-0.5 : 0.9433513060501780 ~= 0.9433513060501781
s= 0.0 : 1.0000000000000000 == 1.0000000000000000
s= 1.0 : 1.1374485596707820 == 1.1374485596707820
s= 2.0 : 1.3154580094497790 == 1.3154580094497790
s= 4.0 : 1.8488276542875353 ~= 1.8488276542875355

Differences marked ~= are floating roundoff.

## Proven endpoint mechanism

1. The Erdős--Murty exceptional primes have finite reciprocal mass.
2. Their entire absolute subset contribution is therefore finite.
3. On nonexceptional primes, ord_p(4) inherits a sqrt(p)*stretched-exponential lower bound.
4. Grouping subsets by their largest good prime makes the full all-orders absolute subset sum convergent.
5. The finite-time endpoint term vanishes using the previously proved divisor-weight growth bound.

## Verdict

RAW_ARITHMETIC_MEAN_S_EQ_1 = PROVED
ALL_FIXED_REAL_MOMENTS = PROVED
DYADIC_INVARIANCE = PROVED
HARDY_LITTLEWOOD_OCCURRENCE_ASYMPTOTIC = NOT_PROVED
TWIN_PRIME_INFINITY = OPEN
NOVELTY = NOT_ESTABLISHED

Full repository test suite remains NOT_RUN because container DNS cannot resolve github.com. No CI PASS is claimed.
