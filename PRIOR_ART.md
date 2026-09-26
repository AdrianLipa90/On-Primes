# Prior Art and Terminology

## Riesel sequences

For a fixed odd positive integer `a`, the fibre

\[
\mathcal F_a=\{a2^k-1:k\ge 0\}
\]

is the classical minus-sign exponential family underlying **Riesel numbers**.
A Riesel number is an odd integer `a` for which `a*2^k - 1` is composite for every positive integer `k`.

This repository therefore does **not** claim novelty for the bare family `a*2^k - 1`, nor for the use of modular covering sets to certify compositeness across all exponents.

## Covering sets

A finite set of primes `R` is a covering set for a Riesel-type sequence when every exponent is covered by at least one divisibility congruence. In the fibre-index language used here, each prime `r` contributes an obstruction class

\[
k\equiv k_r\pmod{\operatorname{ord}_r(2)},
\]

when such a class exists. A finite union that covers every residue modulo the common period is exactly a covering-set certificate.

Example from OEIS A206430: `509203` has covering set

`{3, 5, 7, 13, 17, 241}`.

## What On-Primes adds as a research coordinate system

The project-specific layer is the simultaneous use of:

1. the unique address `n+1 = a*2^k` for all positive integers;
2. the interpretation of `T(x)=2x+1` as the exact shift `(a,k)->(a,k+1)`;
3. the prime-mask view `M_a(k)` over all fibres, not only fibres already known to be Riesel;
4. the half-boundary lemma and the distinguished boundary fibre `a=3`;
5. the exact log coordinate `log(n+1)=log(a)+k*log(2)` and its prime-log defect;
6. later comparison of these masks/fibres with prime-side analytic objects, with no claim yet that this yields new zeta theorems.

## Sources

- Wolfram MathWorld, *Riesel Number*: https://mathworld.wolfram.com/RieselNumber.html
- OEIS A206430, covering sets for `k*2^m - 1`: https://oeis.org/A206430
- OEIS A258154, covering-set modulus data: https://oeis.org/A258154

These references are used for terminology and known examples; the elementary proofs in this repository are self-contained.

## Prime-zeta analytic continuation

The ordinary prime zeta function

\[
P(s)=\sum_p p^{-s}
\]

converges absolutely for `Re(s)>1` and has the classical Möbius-inversion representation

\[
P(s)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(ks).
\]

Standard references describe analytic continuation into `0 < Re(s) <= 1`, with singularities inherited from zeta zeros/poles and a natural-boundary obstruction at `Re(s)=0`. This is directly relevant to the On-Primes character-prime bridge: separated prime sums should be expected to develop logarithmic singular structure even when the full `-zeta'/zeta` combination is meromorphic.

Reference:
- Wolfram MathWorld, *Prime Zeta Function*: https://mathworld.wolfram.com/PrimeZetaFunction.html

## Shifted-prime divisor problems

The general study of divisors of shifted primes is classical. The Titchmarsh divisor problem studies sums such as

\[
\sum_{p\le x}\tau(p-l)
\]

for fixed nonzero `l`; the case `l=-1` includes divisors of `p+1`. Modern treatments connect such questions to the dispersion method, large sieve, Bombieri-Vinogradov type results, and distribution of primes in arithmetic progressions.

The On-Primes identity

\[
\log(p+1)=\sum_{d\mid p+1}\Lambda(d)
\]

is much simpler than the divisor-counting problem because the von Mangoldt divisor sum collapses exactly to `log(p+1)`. No novelty is claimed for that classical arithmetic identity or for the general theory of shifted-prime divisors.

References:
- Encyclopedia of Mathematics, *Titchmarsh problem*: https://encyclopediaofmath.org/wiki/Titchmarsh_problem
- Encyclopedia of Mathematics, *Brun-Titchmarsh theorem*: https://encyclopediaofmath.org/wiki/Brun-Titchmarsh_theorem
- Encyclopedia of Mathematics, *Bombieri prime number theorem*: https://encyclopediaofmath.org/wiki/Bombieri_prime_number_theorem


## Arithmetic phase coordinates, Ramanujan--Fourier series, and prime-pair correlations

The ARPL v0.1 layer uses standard additive characters

\[
\chi_{q,a}(n)=e^{2\pi ian/q},
\]

exact residue coordinates, the Chinese remainder theorem, and finite Fourier/Wiener--Khintchine identities. These ingredients are classical and are not claimed as novel.

Ramanujan sums

\[
c_q(n)=
\sum_{\substack{1\le a\le q\\(a,q)=1}}
e^{2\pi ian/q}
\]

are likewise classical arithmetic harmonic modes. There is direct prior art connecting Ramanujan--Fourier expansions and autocorrelation to prime-pair questions:

- H. G. Gadiyar and R. Padma, *Ramanujan--Fourier series, the Wiener--Khintchine formula and the distribution of prime pairs*, Physica A 269 (1999), 503--510. DOI: 10.1016/S0378-4371(99)00171-5.
- H. G. Gadiyar and R. Padma, *Ramanujan-Fourier series and the conjecture D of Hardy and Littlewood*, Czechoslovak Mathematical Journal 64(1) (2014), 251--267. DOI: 10.1007/s10587-014-0098-5.

The 2014 paper explicitly describes its Hardy--Littlewood prime-pair argument as heuristic because an interchange of limits is not justified. On-Primes therefore does not promote that heuristic to a theorem.

The project-specific ARPL contribution is the unified exact coordinate package that connects:

1. ordered integer separations to complete prime-power residue/phase signatures;
2. exact sequence reconstruction from an anchor plus ordered gaps;
3. the existing dyadic map \(T(x)=2x+1\) to phase squaring;
4. the existing fibre obstruction classes to finite phase-orbit hitting.

Whether this packaging yields a genuinely new distribution theorem is an open research question and requires a broader literature audit.


## Prime-pair and k-tuple singular series

The prime-pair singular series has the standard Ramanujan-series and Euler-product forms

\[
\mathfrak S(h)
=
\sum_{q\ge1}
\frac{\mu(q)^2}{\varphi(q)^2}c_q(h)
=
\prod_p
\left(
1+\frac{c_p(h)}{(p-1)^2}
\right).
\]

Goldston, Ngotiaoco, and Ziegler Hunts discuss this representation and the tail of the singular series in:

- D. A. Goldston, T. Ngotiaoco, J. Ziegler Hunts, *The Tail of the Singular Series for the Prime Pair and Goldbach Problems*, Functiones et Approximatio Commentarii Mathematici 56(1) (2017), 117--141; arXiv:1409.2151.

For a finite \(k\)-tuple \(H\), the standard Hardy--Littlewood singular series is

\[
\mathfrak S(H)
=
\prod_p
\left(1-\frac{\nu_p(H)}p\right)
\left(1-\frac1p\right)^{-|H|},
\]

where \(\nu_p(H)\) counts distinct residues of \(H\) modulo \(p\). This standard formulation appears throughout the modern prime-tuples literature; see, for example:

- J. Pintz, *On the singular series in the prime k-tuple conjecture*, arXiv:1004.1084.

ARPL does not claim these formulas as new. Its project-specific use is to treat the local factors as observables of modular phase coordinates and to transport them under the already existing dyadic map \(T(x)=2x+1\).
