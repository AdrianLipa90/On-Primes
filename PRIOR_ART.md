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


## Besicovitch mean-square almost-periodic sequences

The ARPL global logarithmic spectrum now uses the standard Besicovitch \(B^2\) framework: closure of trigonometric/periodic sequences in a mean-square seminorm, Fourier--Bohr coefficients, and Parseval/harmonic synthesis.

This framework is established prior art and is not claimed as new.

Useful references include:

- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge University Press (1932), for the classical \(B^2\) theory and Parseval/Riesz--Fischer framework.
- Encyclopedia of Mathematics, *Almost-periodic function* and *Fourier series of an almost-periodic function*, for mean values, Fourier--Bohr coefficients, and \(B^2\) Parseval.
- Modern discrete-sequence treatments define Besicovitch-\(p\) almost-periodic sequences as mean-\(p\) limits of trigonometric polynomials.

The project-specific statement is not the existence of Besicovitch theory. It is the proved embedding of the ARPL logarithmic twin-singular-series orbit into the discrete \(B^2\) class with explicit rational frequencies

\[
\lambda=\frac{m}{\operatorname{ord}_p(2)}\pmod1
\]

and number-theoretically controlled prime-channel tails.

No literature novelty claim is made for this specialization without a dedicated audit.


## Quantitative multiplicative-order input: Erdős--Murty

The closure of the raw \(s=1\) arithmetic mean uses a standard external theorem, not an ARPL-internal estimate.

P. Erdős and M. Ram Murty, *On the Order of \(a\) (mod \(p\))*,
in *Number Theory (Ottawa, ON, 1996)*, CRM Proceedings and Lecture Notes 19,
American Mathematical Society (1999), 87--97.

Their Theorem 5(2), specialized to rank one, gives the quantitative form needed here: for fixed \(a>1\) there exist constants
\(\alpha,\delta>0\) such that

\[
\operatorname{ord}_p(a)
\ge
\sqrt p\,\exp((\log p)^\delta)
\]

for all but

\[
O\!\left(\frac{x}{(\log x)^{1+\alpha}}\right)
\]

primes \(p\le x\).

ARPL applies this theorem with \(a=2\). Since

\[
\operatorname{ord}_p(4)
=
\frac{\operatorname{ord}_p(2)}
{\gcd(\operatorname{ord}_p(2),2)},
\]

the same lower bound holds up to a factor \(1/2\) on the nonexceptional prime channels.

The exceptional counting bound implies by partial summation that the exceptional primes have finite reciprocal mass. This is the decisive external input that upgrades the elementary \(0<s<1\) fractional-moment theorem to all fixed real \(s\), including the arithmetic endpoint \(s=1\).

Later literature also attributes the fixed-base quantitative formulation to F. Pappalardi; Kurlberg--Pomerance explicitly cite Pappalardi for the same exceptional-set scale. ARPL therefore treats the estimate strictly as external prior art and does not claim priority for it.


## Limiting distributions and almost-periodic phase laws

The passage from periodic/limit-periodic arithmetic sequences to limiting distributions is classical and is not claimed as an ARPL invention.

Relevant general prior art includes:

- A. S. Besicovitch, *Almost Periodic Functions* (1932), for mean almost-periodic spaces and Fourier--Bohr theory.
- Work on limit-periodic and Besicovitch almost-periodic arithmetic functions showing existence of limiting distributions.
- A. Iksanov, Z. Kabluchko, A. Marynych, *Almost periodic stochastic processes with applications to analytic number theory* (2025), for a modern probabilistic formulation of asymptotic distributions of Besicovitch almost-periodic functions.

Standard tools used by the ARPL limiting-law theorem also include Lévy's continuity theorem, compact procyclic groups, Haar measure, and locally uniform convergence of holomorphic series.

The project-specific object is the explicit phase-clock transform for the dyadic two-twin-pair singular-series orbit,

\[
\mathcal M_h(z)
=
A(h)^z
\left[
1+
\sum_{J\ne\varnothing}
\delta_J(h)
\prod_{p\in J}
\left(
\left(\frac{p-3}{p-4}\right)^z-1
\right)
\right],
\]

together with its number-theoretic clock periods \(e_p=\operatorname{ord}_p(4)\) and generalized-CRT compatibility relation. A targeted search has not established literature novelty for this exact specialization.


## Prime divisors of non-degenerate linear recurrences

The proof that the ARPL active channel set is infinite uses a classical theorem and does not claim novelty for that input.

For an integer linear recurrence whose distinct characteristic roots have no quotient that is a root of unity, there are infinitely many distinct prime divisors among the sequence values. This result goes back to:

- G. Pólya, *Arithmetische Eigenschaften der Reihenentwicklungen rationaler Funktionen*, Journal für die reine und angewandte Mathematik 151 (1921), 99--100.

A modern discussion is:

- H. Roskam, *Prime divisors of linear recurrences and Artin's primitive root conjecture for number fields*, Journal de Théorie des Nombres de Bordeaux 13(1) (2001), 303--314.

Roskam explicitly notes that Pólya's 1921 result already gives infinitude of prime divisors for every non-degenerate integer linear recurrence of order at least two.

ARPL applies this classical theorem to

\[
U_r=(h/2)^2 4^r-1,
\]

whose characteristic roots are \(4\) and \(1\). Since \(6\mid h\), every prime divisor of \(U_r\) is different from \(2\) and \(3\), hence is an active ARPL channel \(p\ge5\).

This prior-art input establishes active-channel infinitude only. The subsequent procyclic/Haar lower-edge atom criterion is the project-specific specialization.


## Odometers / adding machines and compact group rotations

The dynamical-system properties used by the ARPL phase clock are standard and are not claimed as novel.

An odometer (adding machine) can be realized as an inverse limit of finite cyclic rotations. Classical odometers are:

- minimal and uniquely ergodic;
- equicontinuous;
- zero-entropy;
- pure-point systems whose rational point spectrum is the Pontryagin dual of the odometer group.

Useful modern references include:

- T. Downarowicz, *Survey of odometers and Toeplitz flows*, for the classical inverse-limit/addition picture and rational point spectrum.
- Standard compact-group rotation theory; minimal rotations are uniquely ergodic when the generating orbit is dense, and compact abelian rotations have pure point spectrum.
- Modern pure-point dynamical-spectrum treatments of minimal compact group rotations.

ARPL specializes this standard framework to the arithmetic clock tower

\[
L_N=\operatorname{lcm}_{j\le N}\operatorname{ord}_{p_j}(4),
\]

with prime-channel pulse phases \(\rho_{p_j}(h)\) and singular-series weights. The identification of this arithmetic phase clock with an odometer does not make odometer theory itself new.


## Covering systems, second-moment bounds, and phase cylinders

The lower-edge atom problem is related to classical covering systems of congruences, but the ARPL family is an infinite arithmetic system generated by multiplicative-order clocks rather than an arbitrary finite covering system.

Classical covering-system literature includes:

- J. H. Jordan, *Covering Classes of Residues*, Canadian Journal of Mathematics 19 (1967).
- Z.-W. Sun, *On m-covers and m-systems*, Bulletin of the Australian Mathematical Society 81 (2010), 223--235.
- M. Filaseta, K. Ford, S. Konyagin, C. Pomerance, G. Yu, *Sieving by large integers and covering systems of congruences*, arXiv:math/0507374.

For a finite collection of residue classes, the covering function has average equal to the sum of reciprocal moduli. ARPL uses the stronger exact generalized-CRT intersection kernel because its residue classes live on a common procyclic phase hull with highly structured overlaps.

The weighted bound

\[
m\!\left(\bigcup_i C_i\right)
\ge
\frac{(w^\top d)^2}{w^\top G w}
\]

is a direct Hilbert-space / second-moment consequence of Cauchy--Schwarz and is standard. The project-specific ingredient is the arithmetic Gram matrix

\[
G_{pq}
=
m(C_p\cap C_q)
\]

built from the active periods \(\operatorname{ord}_p(4)\) and target phases \(\rho_p(h)\).

Infinite survival products and hazard criteria are likewise standard analysis/probability. ARPL's nonstandard data are the exact decomposition

\[
\eta_N=\frac{c_N}{b_N}
\]

and the multiplicative-order phase-refinement geometry that determines \(b_N\) and \(c_N\).
