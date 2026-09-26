# On Primes

**Dyadic fibres, prime masks, and the half-boundary structure**

This repository studies the exact decomposition
\[
n+1=a\,2^k,\qquad a\ \text{odd},\qquad k=v_2(n+1),
\]
and the induced fibres
\[
\mathcal F_a=\{a2^k-1:k\ge 0\}.
\]

The affine map
\[
T(x)=2x+1
\]
acts inside a fibre by
\[
T(a2^k-1)=a2^{k+1}-1.
\]

For primes, the indicator
\[
M_a(k)=\mathbf 1_{\mathbb P}(a2^k-1)
\]
is called the **prime mask** of the fibre. Consecutive 1-runs in a fibre are Cunningham chains of the first kind.

## Exact starting point

The v0.1 theorem pack records only elementary statements that follow directly from integer factorisation and the definition of \(T\):

1. unique dyadic address of every integer \(n\ge 1\);
2. exact fibre-shift law under \(T\);
3. uniqueness of the prime on the \(k=0\) boundary;
4. the half-boundary lemma
   \[
   x\in \tfrac12+\mathbb Z_{\ge0},\quad T(x)\in\mathbb P
   \iff x=\tfrac12;
   \]
5. exact logarithmic lattice
   \[
   \log(n+1)=\log a+k\log2;
   \]
6. exact prime-log defect
   \[
   \log p=\log(p+1)-\log(1+1/p).
   \]

## Research question

The decomposition itself is **not** a characterization of primes. The open question is whether the masks \(M_a(k)\), their modular obstructions, correlations, or transforms expose useful structure that is obscured in the usual ordering of primes.

A later research lane will test whether the fibre decomposition gives a useful re-expression of the prime side of
\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad \Re(s)>1,
\]
without assuming any unproved statement about prime distribution or the Riemann Hypothesis.

## Epistemic firewall

- `PROVED`: follows from definitions or a supplied proof.
- `STANDARD`: established external mathematics used in its ordinary domain.
- `NUMERICAL`: finite computation only.
- `CONJECTURE`: explicitly conjectural.
- `OPEN`: not proved.
- No numerical pattern is promoted to a theorem.
- No claim that \(1/2\) is a prime number is made.
- No claim of a proof of the Riemann Hypothesis is made.

See [CLAIMS.md](CLAIMS.md), [PRIOR_ART.md](PRIOR_ART.md), and [RESEARCH_FRONTIER.md](RESEARCH_FRONTIER.md).

## Development

Reference implementation is standard-library Python.

```bash
python -m unittest discover -s tests -v
```

Current development branch: `feat/dyadic-prime-fibres-v0.1`.

## Shifted von Mangoldt tower

The current branch also records the exact identity

\[
\log(p+1)=\sum_{r^j\mid p+1}\log r,
\]

so the previous split into a dyadic term and an odd fibre-label term is unified as one hierarchy of base-prime channels `r`. Each channel is supported on shifted residue classes

\[
p\equiv-1\pmod{r^j}.
\]

For fixed `r,j`, the exact valuation shell `v_r(p+1)=j` is a union of `r-1` reduced classes modulo `r^(j+1)`. The classical prime number theorem in arithmetic progressions then gives the fixed-shell asymptotic `Li(x)/r^j`.

See the shifted Mangoldt and valuation-shell proofs in `proofs/`.

## Centered-hexagonal channel

A second exact coordinate lane uses

\[
H_n=1+3n(n+1).
\]

Every \(H_n\) is \(1\pmod6\), and more strongly every prime divisor of every \(H_n\) is itself \(1\pmod6\). For prime \(q>3\), divisibility \(q\mid H_n\) occurs in exactly two residue classes of \(n\pmod q\) when \(q\equiv1\pmod6\), and never when \(q\equiv5\pmod6\).

The same values are Eisenstein norms,

\[
H_n=N((n+1)-n\omega),
\]

which makes the hexagonal lattice connection exact rather than metaphorical. This does not characterize primes; it supplies another rigorously defined modular obstruction family for future cross-sieve tests with the dyadic fibres.

See `proofs/CENTERED_HEXAGONAL_PRIME_CHANNEL_V0_1.md`.


## Skewes–Euler–Hilbert–Collatz bridge

The additive research note [SKEWES_EULER_HILBERT_COLLATZ_BRIDGE_V0_1.md](SKEWES_EULER_HILBERT_COLLATZ_BRIDGE_V0_1.md) derives an exact common dyadic log-phase clock across the existing (2x+1) fibres, Hilbert-Hotel shift operators, zeta-zero phase factors, and accelerated odd-Collatz reverse fibres. Its finite algebraic validator is `experiments/validate_skewes_euler_hilbert_collatz_bridge_v0_1.py`.

The bridge is explicitly typed as exact representation plus open spectral programme; it does not promote RH, Collatz, or the first Skewes crossing to solved status.
