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

Current development branch: feat/arithmetic-relational-phase-law-v0.1.

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


## Arithmetic Relational Phase Law

The ARPL v0.1 theorem pack adds an exact phase-coordinate layer for integer separations. For

\[
\Delta=y-x,
\qquad
\chi_{q,a}(n)=e^{2\pi ian/q},
\]

the relative phase obeys

\[
\chi_{q,a}(y)\overline{\chi_{q,a}(x)}=\chi_{q,a}(\Delta).
\]

A complete prime-power residue signature

\[
\Phi_\infty(\Delta)=(\Delta\bmod p^j)_{p,\,j\ge1}
\]

is injective on integers. Therefore an anchor plus the ordered gap stream of any increasing integer sequence can be represented exactly by its complete modular phase signatures.

For the existing dyadic map \(T(x)=2x+1\), separations obey

\[
\Delta\mapsto2\Delta,
\]

so each modular character evolves by exact phase squaring:

\[
\chi_{q,a}(\Delta(T^rx,T^ry))
=
\chi_{q,a}(\Delta(x,y))^{2^r}.
\]

For the fibre \(x_{a,k}=a2^k-1\), modular divisor obstructions are equivalently finite phase-orbit hits. For twin-prime starts above 3, consecutive start gaps are exactly locked to \(0\pmod6\), giving locked mod-2 and mod-3 phase channels.

See proofs/ARITHMETIC_RELATIONAL_PHASE_LAW_V0_1.md and tests/test_phase_law.py.

Prior-art firewall: Fourier/CRT/profinite character machinery, Wiener--Khintchine duality, Ramanujan sums, and earlier Ramanujan--Fourier work on prime-pair correlations are established mathematics. ARPL v0.1 does not claim a zeta-zero equivalence, a twin-prime proof, or RH.


### Singular-series phase bridge

ARPL now closes the local Hardy--Littlewood bridge. For a prime-pair gap \(h\),

\[
\mathfrak S_P(h)
=
\prod_{p\in P}
\left(1+\frac{c_p(h)}{(p-1)^2}\right)
\]

is exactly determined by the finite modular phase state \((h\bmod p)_{p\in P}\), and equals the corresponding finite squarefree Ramanujan expansion.

For two twin pairs separated by \(h\), the four-point pattern

\[
H_h=\{0,2,h,h+2\}
\]

has local factor

\[
B_p(h)=
\frac{1-\nu_p(H_h)/p}{(1-1/p)^4}.
\]

The \(p=2\) and \(p=3\) channels are jointly nonzero exactly when

\[
h\equiv0\pmod6.
\]

Higher prime channels modulate the local factor through \(h\bmod p\). Under the existing dyadic transport \(h\mapsto2h\), these channel states evolve by

\[
u\mapsto2u\pmod p.
\]

See proofs/ARPL_SINGULAR_SERIES_PHASE_BRIDGE_V0_1.md and receipts/ARPL_SINGULAR_SERIES_REVERSE_TEST_V0_1.md.


### Canonical global phase space

The complete ARPL modular state lives naturally in the profinite completion

\[
\widehat{\mathbb Z}
\cong
\prod_p\mathbb Z_p,
\]

whose Pontryagin dual is

\[
\mathbb Q/\mathbb Z.
\]

The dyadic gap operator is multiplication by two on \(\widehat{\mathbb Z}\). It is invertible on every odd \(p\)-adic component and injective/non-surjective on the \(2\)-adic component. On the dual frequency side it acts by

\[
r\mapsto2r\pmod1
\]

with kernel exactly

\[
\{0,1/2\}.
\]

Ramanujan sums are exact-order denominator-shell character sums in this dual phase space. See proofs/ARPL_PROFINITE_PHASE_SPACE_V0_1.md.

The finite odd-prime channel dynamics \(u\mapsto2u\bmod p\) has cycle length \(d_p=\operatorname{ord}_p(2)\). The corresponding transfer operator has \(d_p\)-th roots of unity as eigenmodes. For the two-twin-pair local factor, the equal defects at \(u=\pm2\) produce an exact odd-mode cancellation whenever \(d_p\) is even. See proofs/ARPL_DYADIC_TRANSFER_SPECTRUM_V0_1.md.


### Dyadic cross-channel resonance

For finite odd-prime support \(P\), define the common-clock twin-factor observable

\[
B_P(r;h)=\prod_{p\in P}B_p(2^rh).
\]

Its exact period divides

\[
L_P(h)=\operatorname{lcm}_{p\in P}d_p(h),
\]

with \(d_p(h)=1\) when \(p\mid h\), otherwise \(d_p(h)=\operatorname{ord}_p(2)\).

After local Fourier decomposition, the global mean keeps exactly those mode tuples obeying

\[
\sum_{p\in P}\frac{m_p}{d_p(h)}\in\mathbb Z.
\]

This yields the exact resonance correction

\[
\mathcal C_P(h)
=
\left\langle\prod_{p\in P}B_p\right\rangle
-
\prod_{p\in P}\langle B_p\rangle.
\]

If the effective local periods are pairwise coprime, then

\[
\mathcal C_P(h)=0
\]

exactly. Shared period factors can support nonzero coupling, subject to the local mode-selection rules.

For fixed \(h\), subsets of prime channels with nonzero \(\mathcal C_J(h)\) define the ARPL dyadic resonance hypergraph.

See proofs/ARPL_DYADIC_CROSS_CHANNEL_RESONANCE_V0_1.md and receipts/ARPL_DYADIC_RESONANCE_REVERSE_TEST_V0_1.md.
