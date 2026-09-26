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


## Profinite completion and Pontryagin duality

The global ARPL phase space uses standard structure:

\[
\widehat{\mathbb Z}
=
\varprojlim_n\mathbb Z/n\mathbb Z
\cong
\prod_p\mathbb Z_p,
\]

and the Pontryagin dual of \(\widehat{\mathbb Z}\) is the discrete torsion group

\[
\mathbb Q/\mathbb Z.
\]

This is established harmonic-analysis/profinite theory and is not claimed as novel.

Useful references:

- nLab, *profinite completion of the integers* and *Pontryagin duality for torsion abelian groups*.
- Jordan Bell, *The Pontryagin duals of Q/Z and Q and the adeles*.
- Standard treatments of harmonic analysis on number fields and locally compact abelian groups.

In this language, the ARPL characters

\[
e^{2\pi ian/q}
\]

are the finite-order characters indexed by \(a/q\pmod1\), and Ramanujan sums are sums over characters of exact order \(q\). The project-specific layer is the integration of this standard duality with the On-Primes dyadic operator and singular-series observables.


## Divisor weights on exponential sequences

The current ARPL arithmetic-mean frontier has been reduced to the divisor-weight sequence

\[
R(4^rh^2-4).
\]

There is classical prior art on divisor sums and prime divisors of exponential sequences, so this lane must not be treated as unexplored.

Relevant references include:

- P. Erdős, *On the sum \(\sum_{d\mid 2^n-1}d^{-1}\)*, Israel Journal of Mathematics 9 (1971), 43--48. Erdős proves an upper bound of order \(\log\log n\) for the reciprocal-divisor sum of \(2^n-1\).
- G. R. Everest and I. E. Shparlinski, *Divisor sums of generalized exponential polynomials*, Canadian Mathematical Bulletin 39 (1996), 35--46.
- Florian Luca, *On the sum of divisors of the Mersenne numbers*, Mathematica Slovaca 53(5) (2003), 457--466.
- J. von zur Gathen, A. Knopfmacher, F. Luca, L. G. Lucht, I. E. Shparlinski, *Average order in cyclic groups*, Journal de Théorie des Nombres de Bordeaux 16 (2004), 107--123.

These works are relevant to growth bounds, divisor statistics, and multiplicative-order averages. They do not, from the targeted search performed on 2026-09-26, directly establish the specific Cesaro mean of

\[
R(4^rh^2-4)
=
\prod_{\substack{p\mid 4^rh^2-4\\p\ge5}}
\frac{p-3}{p-4}.
\]

That absence of a direct match is not a novelty proof.


## Shift-averaged correlations and primes in short intervals

The current Fejér-averaged phase-spectroscopy lane uses standard prior art on mean-square prime distribution in short intervals.

- B. Saffari and R. C. Vaughan, *On the fractional parts of \(x/n\) and related sequences. II*, Ann. Inst. Fourier (Grenoble) 27(2) (1977), 1–30. Their short-interval mean-square machinery supplies the external unconditional long-window input used in \`FEJER_AVERAGED_HIGH_TAIL_LONG_WINDOW_V0_1.md\`.
- P. X. Gallagher, *On the distribution of primes in short intervals*, Mathematika 23 (1976), 4–9. This is part of the classical mean/normal-density context and of the literature on averages of singular series.
- D. A. Goldston and H. L. Montgomery, *On pair correlations of zeros and primes in short intervals*, in *Analytic Number Theory and Diophantine Problems* (1987), 183–203. This is the standard pair-correlation/short-interval bridge.

No novelty claim is made here for Fejér kernels, Wiener--Khintchine, Selberg integrals, large-sieve/dispersion methods, or the external short-interval theorems. The repository-specific result is their exact alignment with the existing Möbius--CRT phase decomposition and its low/high divisor split.
