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


### Global dyadic orbit invariant

For \(p\ge5\), let

\[
\mu_p(h)
\]

be the average of the local two-twin-pair factor \(B_p(2^rh)\) over one complete local doubling orbit. Then

\[
\mu_p(2^kh)=\mu_p(h)
\]

exactly.

For every fixed nonzero \(h\), the infinite product

\[
\boxed{
\mathcal I(h)=\prod_{p\ge5}\mu_p(h)
}
\]

converges to a finite positive nonzero value. The proof uses

\[
1-\beta_p=O(p^{-2}),
\qquad
\alpha_p=O(p^{-1}),
\qquad
\operatorname{ord}_p(2)\ge\log_2(p+1),
\]

which gives

\[
|\mu_p(h)-1|
=
O(p^{-2})+O((p\log p)^{-1})
\]

outside the finite set of prime divisors of \(h\).

Therefore

\[
\boxed{
\mathcal I(2^kh)=\mathcal I(h)
}
\]

for every \(k\ge0\). On positive integers, \(\mathcal I\) depends only on the odd part of \(h\).

This is the first controlled infinite-channel ARPL observable. It is the independently averaged baseline; the fully coupled infinite common-clock resonance limit remains open.

See proofs/ARPL_GLOBAL_DYADIC_ORBIT_INVARIANT_V0_1.md.


### Connected resonance expansion

Finite common-clock moments now admit an exact connected expansion. For a finite prime subset \(J\),

\[
K(J;h)
=
\sum_{\pi\in\Pi(J)}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{A\in\pi}M(A;h),
\]

with the inverse partition reconstruction of \(M(J;h)\).

For two channels, \(K\) is exactly the previously defined resonance correction. Higher \(K\) isolate irreducible multi-channel couplings.

The period-overlap graph

\[
p\sim q
\iff
\gcd(d_p(h),d_q(h))>1
\]

provides an exact compression rule: moments factor across its connected components, and every connected cumulant spanning more than one component is zero.

At \(h=6\),

\[
K(\{7,13,19\};6)
=
-\frac{5168743489}{457019805007872}\ne0,
\]

while

\[
K(\{5,7,11\};6)=0.
\]

See proofs/ARPL_CONNECTED_RESONANCE_EXPANSION_V0_1.md.


### Fixed-order global connected layers

For the centered local channel

\[
X_p(r;h)=B_p(2^rh)-\mu_p(h),
\]

every nonzero local Fourier coefficient obeys

\[
|\widehat X_p(m)|
\le
\frac{2\alpha_p}{d_p},
\qquad
d_p=\operatorname{ord}_p(2).
\]

For finite \(J\),

\[
|M_X(J;h)|
\le
\frac{2^{|J|}}{\operatorname{lcm}_{p\in J}d_p}
\prod_{p\in J}\alpha_p.
\]

This yields a connected-cumulant bound

\[
|K(J;h)|
\le
B_n(n-1)!2^n
\frac{\prod_{p\in J}\alpha_p}{\max_{p\in J}d_p},
\qquad n=|J|\ge2.
\]

Using

\[
\alpha_p\ll\frac1p,
\qquad
d_p\ge\log_2(p+1),
\]

together with the classical reciprocal-prime Mertens bound and \(\pi(x)\ll x/\log x\), one obtains

\[
\boxed{
\sum_{\substack{J\subset\mathbb P_{\ge5}\\|J|=n}}
|K(J;h)|<\infty
}
\]

for every fixed nonzero \(h\) and every fixed \(n\ge2\).

Thus every fixed \(n\)-body connected ARPL layer exists globally. The remaining open problem is convergence after summing over \(n\to\infty\).

See proofs/ARPL_FIXED_ORDER_CONNECTED_SUMMABILITY_V0_1.md.


### Instantaneous singular-series compression

For the two-twin-pair pattern

\[
H_x=\{0,2,x,x+2\},
\qquad x\ge6,\quad 6\mid x,
\]

define

\[
C_*=
\prod_{p\ge5}\frac{p^3(p-4)}{(p-1)^4},
\]

\[
Z(x)=
\prod_{\substack{p\mid x\\p\ge5}}
\frac{p-2}{p-4},
\qquad
R(N)=
\prod_{\substack{p\mid N\\p\ge5}}
\frac{p-3}{p-4}.
\]

Then the full standard Hardy--Littlewood singular series factorizes exactly as

\[
\boxed{
\mathfrak S(H_x)
=
\frac{27}{2}\,
C_*\,Z(x)\,R(x^2-4).
}
\]

Along the dyadic orbit \(x=2^rh\), \(6\mid h\),

\[
\boxed{
\mathfrak S(H_{2^rh})
=
\frac{27}{2}\,
C_*\,Z(h)\,R(4^rh^2-4).
}
\]

Thus every instantaneous infinite Euler product is compressed into a universal background constant, static odd-prime locks from \(h\), and a finite dynamic correction from the prime divisors of \(4^rh^2-4\).

See proofs/ARPL_INSTANTANEOUS_SINGULAR_SERIES_FACTORIZATION_V0_1.md.


### Global logarithmic phase mean

For admissible \(h\ge6\), define the exact special-hit density

\[
\delta_p(h)
=
\operatorname{dens}\{r:2^rh\equiv\pm2\pmod p\}.
\]

It is exactly \(0\), \(1/d_p\), or \(2/d_p\), where
\(d_p=\operatorname{ord}_p(2)\).

Because

\[
\delta_p(h)\le\frac2{d_p},
\qquad
d_p\ge\log_2(p+1),
\]

the logarithmic correction

\[
\sum_{p\ge5}
\delta_p(h)\log\frac{p-3}{p-4}
\]

converges absolutely.

Hence the full infinite-channel Cesaro mean

\[
\boxed{
\mathcal L(h)
=
\lim_{T\to\infty}
\frac1T\sum_{r<T}
\log\mathfrak S(H_{2^rh})
}
\]

exists and equals

\[
\mathcal L(h)
=
\log\left(\frac{27}{2}C_*Z(h)\right)
+
\sum_{p\ge5}
\delta_p(h)\log\frac{p-3}{p-4}.
\]

The geometric mean

\[
\boxed{
\mathcal G(h)=e^{\mathcal L(h)}
}
\]

is finite, positive and dyadically invariant.

Jensen also gives

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\sum_{r<T}\mathfrak S(H_{2^rh})
\ge
\mathcal G(h)>0.
}
\]

The arithmetic Cesaro mean itself remains open.

See proofs/ARPL_GLOBAL_LOGARITHMIC_PHASE_MEAN_V0_1.md.


### Pointwise growth control

The dynamic divisor weight also satisfies the exact comparison

\[
R(N)
\le
C_R\frac{N}{\varphi(N)},
\qquad
C_R=
\prod_{p\ge5}
\left(1+\frac{3}{p(p-4)}\right)
<\infty.
\]

Hence the classical bound \(N/\varphi(N)\ll\log\log N\) gives

\[
R(N)\ll\log\log N.
\]

Along the dyadic orbit,

\[
\boxed{
\mathfrak S(H_{2^rh})
\ll_h
\log(r+2).
}
\]

So the unresolved arithmetic-mean problem has a deterministic logarithmic pointwise envelope; faster spikes are excluded.

See proofs/ARPL_DIVISOR_WEIGHT_GROWTH_BOUND_V0_1.md.


### Global B2 phase spectrum

For the centered logarithmic field

\[
Y_h(r)
=
\log\mathfrak S(H_{2^rh})-\mathcal L(h),
\]

finite prime truncations are periodic and converge to the actual field in the discrete Besicovitch mean-square seminorm:

\[
\boxed{
\|Y_h-Y_{h,P}\|_{B^2}\to0.
}
\]

The global variance therefore exists:

\[
\boxed{
\mathcal V(h)
=
\lim_{T\to\infty}
\frac1T\sum_{r<T}|Y_h(r)|^2
<\infty.
}
\]

It has an absolutely convergent local/joint hit-density representation.

The Fourier--Bohr spectrum is pure point and rational:

\[
\Lambda_h
\subset
\bigcup_{p\ge5}
\left\{
\frac{m}{\operatorname{ord}_p(2)}
\pmod1
\right\}
\subset\mathbb Q/\mathbb Z.
\]

With aggregated coefficients \(a_h(\lambda)\), Besicovitch Parseval gives

\[
\boxed{
\mathcal V(h)
=
\sum_{\lambda\in\Lambda_h}|a_h(\lambda)|^2.
}
\]

The autocorrelation is correspondingly

\[
\boxed{
C_h(k)
=
\sum_{\lambda\in\Lambda_h}
|a_h(\lambda)|^2e^{2\pi i\lambda k}.
}
\]

This is the rigorous logarithmic phase-power spectrum of the dyadic two-twin-pair singular-series orbit.

See proofs/ARPL_GLOBAL_B2_PHASE_SPECTRUM_V0_1.md.


### Quadratic phase clock and subcritical all-orders moments

For the twin observable, the sign pair \(+2,-2\) quotients the base-2 clock to

\[
\boxed{
e_p=\operatorname{ord}_p(4)
=
\frac{\operatorname{ord}_p(2)}
{\gcd(\operatorname{ord}_p(2),2)}.
}
\]

Every active channel becomes exactly one pulse train,

\[
E_p(r;h)
=
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}}.
\]

Thus joint phase hits are governed by ordinary CRT on one phase class per prime.

For a compatible finite set \(J\),

\[
L_J=\operatorname{lcm}_{p\in J}e_p
\]

satisfies

\[
\prod_{p\in J}p\mid4^{L_J}-1,
\]

and hence

\[
L_J>
\frac{\sum_{p\in J}\log p}{\log4}.
\]

This yields an all-orders theorem below the critical exponent. For every

\[
0<s<1,
\]

the Cesaro moment

\[
\boxed{
\mathcal M_s^{\mathfrak S}(h)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh})^s
}
\]

exists and is finite.

The compatible-subset expansion converges absolutely at every \(s<1\). The current unconditional majorant becomes logarithmically critical at \(s=1\), so the raw arithmetic mean remains open.

See proofs/ARPL_QUADRATIC_PHASE_CLOCK_V0_1.md and proofs/ARPL_SUBCRITICAL_FRACTIONAL_MOMENTS_V0_1.md.


### Arithmetic mean endpoint closed

The earlier elementary all-orders argument closed every \(0<s<1\) but stopped at the critical endpoint \(s=1\). A standard quantitative theorem of Erdős--Murty supplies the missing order growth.

For fixed \(a=2\), outside an exceptional set of primes with counting function

\[
O\!\left(\frac{x}{(\log x)^{1+\alpha}}\right),
\]

one has

\[
\operatorname{ord}_p(2)
\ge
\sqrt p\,e^{(\log p)^\delta}
\]

for some \(\alpha,\delta>0\). The exceptional set has finite reciprocal-prime mass.

Combining this with the quadratic clock

\[
e_p=\operatorname{ord}_p(4)
\]

makes the full compatible-subset expansion absolutely convergent for every fixed real moment exponent \(s\).

In particular, the raw arithmetic Cesaro mean now exists:

\[
\boxed{
\mathcal A(h)
=
\lim_{T\to\infty}
\frac1T\sum_{r<T}
\mathfrak S(H_{2^rh})
<\infty.
}
\]

Its exact all-orders representation is

\[
\boxed{
\mathcal A(h)
=
\frac{27}{2}C_*Z(h)
\left[
1+
\sum_{\varnothing\ne J}
\frac{\mathbf1_{\rm CRT\ compatible}(J;h)}
{\operatorname{lcm}_{p\in J}\operatorname{ord}_p(4)}
\prod_{p\in J}\frac1{p-4}
\right].
}
\]

The displayed series is absolutely convergent.

More generally,

\[
\boxed{
\lim_{T\to\infty}
\frac1T\sum_{r<T}
\mathfrak S(H_{2^rh})^s
}
\]

exists and is finite for every real \(s\).

This closes the raw-amplitude mean problem for the standard singular-series weight. It does not prove the Hardy--Littlewood occurrence asymptotic or twin-prime infinitude.

See proofs/ARPL_ALL_REAL_MOMENTS_ARITHMETIC_MEAN_V0_1.md.


### Entire phase transform and limiting law

The real-moment theorem extends to the whole complex plane. For

\[
b_p(z)
=
\left(\frac{p-3}{p-4}\right)^z-1,
\]

the compatible-subset expansion

\[
F_h(z)
=
1+
\sum_{\varnothing\ne J}
\delta_J(h)
\prod_{p\in J}b_p(z)
\]

converges absolutely and locally uniformly on \(\mathbb C\). Therefore

\[
\boxed{
\mathcal M_h(z)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
\mathfrak S(H_{2^rh})^z
=
A(h)^zF_h(z)
}
\]

exists for every \(z\in\mathbb C\) and is entire.

On the imaginary axis,

\[
\phi_h(t)=\mathcal M_h(it)
\]

is the limiting characteristic function of

\[
Y_r(h)=\log\mathfrak S(H_{2^rh}).
\]

Hence the empirical measures of \(Y_r(h)\) converge weakly to a probability law \(\nu_h\), and

\[
\boxed{
\mathcal M_h(z)
=
\int_{\mathbb R}e^{zy}\,d\nu_h(y)
}
\]

for every complex \(z\).

The law has a canonical compact arithmetic realization. If

\[
e_p=\operatorname{ord}_p(4),
\]

then the closure of the diagonal clock

\[
K_h=
\overline{
\{r(1\bmod e_p)_p:r\in\mathbb Z\}
}
\]

is a compact procyclic phase hull. The limiting law is the Haar pushforward of the ARPL pulse field on \(K_h\).

Moreover,

\[
\boxed{
\nu_{2^kh}=\nu_h
}
\]

for every \(k\ge0\): the **entire limiting distribution** is a dyadic-orbit invariant.

See proofs/ARPL_ENTIRE_PHASE_MOMENT_LIMITING_LAW_V0_1.md.


### Mellin law and cumulant geometry

Let \(\nu_h\) be the limiting law of

\[
Y=\log\mathfrak S(H_{2^rh})
\]

and let

\[
\mu_h=(\exp)_*\nu_h
\]

be the corresponding limiting law of the positive singular-series amplitude.

The entire phase transform is simultaneously

\[
\boxed{
\mathcal M_h(z)
=
\int_{\mathbb R}e^{zy}\,d\nu_h(y)
=
\int_{(0,\infty)}x^z\,d\mu_h(x).
}
\]

Thus it is both the bilateral Laplace transform of the log law and the Mellin transform of the positive amplitude law.

Because \(\mathcal M_h(0)=1\), the normalized logarithm

\[
K_h(z)=\log\mathcal M_h(z)
\]

is analytic near \(0\) and defines the complete cumulant tower

\[
\kappa_n(h)=K_h^{(n)}(0).
\]

In particular,

\[
\boxed{
\kappa_1(h)=\mathcal L(h),
\qquad
\kappa_2(h)=\mathcal V(h).
}
\]

Every polynomial log moment exists, and the limiting law is moment-determinate.

The entire transform also gives optimized Chernoff envelopes:

\[
\Pr(Y\ge y)
\le
\inf_{s>0}
\exp(K_h(s)-sy),
\]

and for the positive amplitude \(X=e^Y\),

\[
\Pr(X\ge x)
\le
\inf_{s>0}
\frac{\mathcal M_h(s)}{x^s}.
\]

Finally,

\[
\boxed{
\kappa_n(2^kh)=\kappa_n(h)
}
\]

for every \(n\ge1\): the complete cumulant geometry is a dyadic-orbit invariant.

See proofs/ARPL_MELLIN_CUMULANT_GEOMETRY_V0_1.md.


### Procyclic phase-refinement tower

Enumerate the active base-4 channel periods

\[
e_j=\operatorname{ord}_{p_j}(4)
\]

and define

\[
L_N=\operatorname{lcm}(e_1,\dots,e_N).
\]

The finite diagonal common-clock state is exactly

\[
\boxed{
K_{h,N}\cong\mathbb Z/L_N\mathbb Z.
}
\]

When a new channel is added, every old phase cell has exactly

\[
\boxed{
b_N
=
\frac{L_{N+1}}{L_N}
=
\frac{e_{N+1}}{\gcd(e_{N+1},L_N)}
}
\]

children. Thus \(b_N=1\) identifies an exact clock-resolution redundancy, while \(b_N>1\) gives a genuine refinement.

The global phase hull is the compact procyclic inverse limit

\[
\boxed{
K_h
\cong
\varprojlim_N
\mathbb Z/L_N\mathbb Z.
}
\]

Its Pontryagin dual is the rational frequency module

\[
\boxed{
\widehat K_h
\cong
\bigcup_N
\frac1{L_N}\mathbb Z/\mathbb Z
\subset\mathbb Q/\mathbb Z.
}
\]

The previously derived Fourier--Bohr frequencies \(m/e_p\) are elements of this same module.

Equivalently, the exact phase-refinement graph has level-\(N\) vertices
\(\mathbb Z/L_N\mathbb Z\), reduction edges between successive levels, and coherent infinite paths equal to points of \(K_h\).

This is an exact inverse-limit hierarchy. No Hausdorff/fractal dimension is claimed without an explicit metric and a separate theorem.

See proofs/ARPL_PROCYCLIC_PHASE_REFINEMENT_TOWER_V0_1.md.
