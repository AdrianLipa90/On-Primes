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

See [CLAIMS.md](CLAIMS.md) and [PRIOR_ART.md](PRIOR_ART.md).

## Development

Reference implementation is standard-library Python.

```bash
python -m unittest discover -s tests -v
```

Current development branch: `feat/dyadic-prime-fibres-v0.1`.
