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
