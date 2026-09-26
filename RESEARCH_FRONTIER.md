# Research Frontier

## Established chain

The current branch establishes, with explicit proofs/tests where applicable:

\[
p+1=a2^k
\]

\[
T(x)=2x+1:\ (a,k)\mapsto(a,k+1)
\]

\[
\log p=\log a+v_2(p+1)\log2-\log(1+1/p)
\]

and, for \(\Re(s)>1\),

\[
-\frac{\zeta'(s)}{\zeta(s)}
=(\log2)K(s)+A(s)-D(s).
\]

The dyadic moment

\[
K(s)=\sum_p\frac{v_2(p+1)}{p^s-1}
\]

has the exact residue-tower decomposition

\[
K(s)=\sum_{j\ge1}
\sum_{p\equiv-1\ (\mathrm{mod}\ 2^j)}
\frac1{p^s-1},
\]

and each tower level admits a Dirichlet-character decomposition modulo \(2^j\).

## Hard no-go

Do **not** substitute \(s=1/2+it\) directly into the prime sums above and treat the resulting expressions as convergent Euler-product identities.

The derivations rely on absolute convergence in \(\Re(s)>1\). The analytic continuation of the full object

\[
-\zeta'(s)/\zeta(s)
\]

does not imply that the separated pieces \(K(s)\), \(A(s)\), and \(D(s)\) individually possess the same continuation or that termwise continuation preserves their interpretation.

The classical prime-zeta function already demonstrates the obstruction: its Möbius-log representation inherits singularities from zeta zeros/poles after analytic continuation. Therefore cancellation between separated pieces must be proved rather than assumed.

Any critical-strip use must proceed by one of the following rigorously controlled routes:

1. derive analytic continuation for the combined fibre/character expression;
2. introduce a smoothing kernel and prove convergence/uniformity before moving the contour;
3. connect to an explicit formula or Weil/Suzuki form where analytic continuation is already built in;
4. prove a cancellation theorem showing which divergent/singular pieces combine to a regular object.

## Immediate open gates

### OP-F01 — Character/L-function closure

Determine whether the combined tower expression can be rewritten in terms of standard \(L(s,\chi)\) objects in a form whose analytic continuation is explicit and whose cancellation structure is preserved.

### OP-F02 — Functional-equation transport

Determine how, if at all, the decomposition

\[
(\log2)K+A-D
\]

transforms under the zeta functional-equation involution \(s\mapsto1-s\). No componentwise functional equation is currently claimed.

### OP-F03 — Smoothed explicit-formula bridge

Construct a smoothed version of the dyadic-fibre prime measure and derive its exact appearance in a classical explicit formula. This is the preferred path toward the critical strip because it avoids illegal use of the Euler product there.

### OP-F04 — Suzuki/Weil insertion

Express the prime-power measure

\[
\sum_{p,m}(\log p)p^{-m/2}\,\delta_{m\log p}
\]

using the dyadic address of each base prime and test whether the fibre/tower decomposition yields a new inequality or cancellation for the signed memory term. Reindexing alone is insufficient.

## Success criterion

A result becomes relevant to RH only if it proves a new sign, positivity, zero-free, or cancellation statement after the analytic-continuation barrier is handled rigorously.

Until then, the project status is:

- dyadic coordinate system: `PROVED`;
- modular/Riesel sieve layer: `PROVED/STANDARD`;
- prime-side fibre decomposition for `Re(s)>1`: `PROVED`;
- residue/character bridge for `Re(s)>1`: `PROVED/STANDARD`;
- new critical-strip theorem: `OPEN`;
- Riemann Hypothesis: `OPEN`.

### OP-F05 — Growing-modulus uniformity

The fixed-channel theory is now closed for every fixed base prime `r`: exact shells, PNT-AP shell asymptotics, and mean valuation

\[
\frac1{\pi(x)}\sum_{p\le x}v_r(p+1)
\to
\frac{r}{(r-1)^2}.
\]

Also

\[
\sum_{r\le R}\frac{r\log r}{(r-1)^2}
=
\log R+O(1).
\]

Therefore the next genuinely nonlocal gate is to control many channels simultaneously when the channel/modulus cutoff grows with `x`. A useful theorem must quantify the error uniformly across prime-power moduli rather than taking `r,j` fixed first.

Relevant classical tools include Siegel-Walfisz, Brun-Titchmarsh, Bombieri-Vinogradov, large-sieve and dispersion estimates. Any claimed improvement beyond their standard ranges must be proved independently.

### OP-F06 — Dynamic obstruction intersection

The prime mask at `(a,k)` is now exactly the intersection of all active modular obstruction masks for primes up to `sqrt(a*2^k-1)`. The unresolved distribution problem is to estimate the survivor set when this obstruction family grows dynamically with `k`, including correlations between periods `ord_r(2)`.

### OP-F07 — Hexagonal/dyadic cross-sieve

The centered-hexagonal sequence

\[
H_n=3n^2+3n+1
\]

has an exact single-channel prime-divisor restriction: every prime divisor satisfies \(q\equiv1\pmod6\). For each prime \(q>3\), its modular obstruction mask in shell index \(n\) has exactly two residue classes when \(q\equiv1\pmod6\) and none when \(q\equiv5\pmod6\).

The sequence is simultaneously an Eisenstein norm:

\[
H_n=N((n+1)-n\omega).
\]

The next open gate is to determine whether intersections between these two-root shell masks and the existing dyadic fibre masks produce any nontrivial correlation, cancellation, or sieve bound beyond a change of coordinates. No independence assumption is permitted.



### OP-F08 — Arithmetic Relational Phase Law closure

ARPL v0.1 now supplies exact phase coordinates for ordered separations:

\[
\Phi_\infty(\Delta)
=
(\Delta\bmod p^j)_{p,\ j\ge1},
\]

with injectivity on \(\mathbb Z\), and therefore the exact ordered-gap representation

\[
\{p_n\}
\longleftrightarrow
\left(p_1,\{g_n\}\right)
\longleftrightarrow
\left(p_1,\{\Phi_\infty(g_n)\}\right).
\]

The same theorem pack identifies the existing dyadic map with phase squaring,

\[
\chi_{q,a}(\Delta(T^rx,T^ry))
=
\chi_{q,a}(\Delta(x,y))^{2^r},
\]

and re-expresses existing modular divisor obstructions as finite phase-orbit hitting.

The next nontrivial gate is **not** to reprove CRT/Fourier theory. It is to determine whether the ordered modular phase dynamics yields a new invariant, compression theorem, correlation law, or analytic operator that is stronger than the underlying standard harmonic/profinite representation.

### OP-F09 — Ramanujan channel / ordered-gap bridge

Prior literature already connects Ramanujan--Fourier expansions and Wiener--Khintchine ideas to prime-pair autocorrelation. The open task is to build a rigorous bridge between:

\[
\text{ordered prime-gap phase stream}
\]

and

\[
\text{Ramanujan / character correlation channels},
\]

while preserving exactly which information is lost when passing from the ordered stream to pair correlation or power spectrum.

A valid result must explicitly distinguish:

- exact ordered-gap reconstruction;
- pair-correlation data;
- power-spectrum data;
- Hardy--Littlewood singular-series heuristics;
- any analytic continuation used in zeta-related expressions.

### OP-F10 — Zeta-spectrum operator

Investigate whether there exists a rigorously defined operator mapping the arithmetic phase representation of primes to the oscillatory terms of an explicit formula involving zeta zeros.

No equivalence is currently established between the prime-gap phase stream and the zero ordinates \(\gamma\). Any such bridge must pass through a valid explicit-formula or transform theorem and must not infer invertibility from pair-correlation data alone.


### OP-F11 — Ordered information beyond singular-series observables

The local Hardy--Littlewood bridge is now exact at the finite/operator level:

\[
h \mapsto (h\bmod p)_p
\mapsto \{c_p(h),\nu_p(h)\}_p
\mapsto \text{local singular factors}.
\]

This closes the question of whether the singular-series layer is representable inside ARPL: it is.

What remains open is whether the **ordered sequence** of these phase states contains a new invariant or dynamical law not already captured by standard singular-series, Ramanujan--Fourier, sieve, or character machinery.

The next test must therefore compare two objects with the same local singular-series statistics but different ordering. Any proposed ARPL invariant must distinguish them if it genuinely uses ordered phase dynamics.

### OP-F12 — Dyadic local-factor transfer operator

For a fixed prime channel \(p\), the two-twin-pair local factor is an observable \(B_p(u)\) on the finite state space \(u\in\mathbb Z/p\mathbb Z\), and the On-Primes dyadic dynamics acts by

\[
u\mapsto2u\pmod p.
\]

Construct the corresponding finite transfer/permutation operator and determine:

1. orbit decomposition as a function of \(\operatorname{ord}_p(2)\);
2. spectrum of the transfer operator;
3. projection of \(B_p\) onto its eigenmodes;
4. whether the product over prime channels yields a useful convergent or renormalized global observable.

This is the next genuinely operator-theoretic ARPL gate.


### OP-F13 — Global profinite transfer assembly

The finite channel operator is now closed, and the canonical global state space is

\[
\widehat{\mathbb Z}\cong\prod_p\mathbb Z_p,
\]

with dual \(\mathbb Q/\mathbb Z\).

The next global gate is to construct a projectively consistent observable/transfer formalism on this compact state space that combines:

1. the one-way \(2\)-adic filtration;
2. the invertible odd-\(p\) channel dynamics;
3. Ramanujan exact-order frequency shells;
4. singular-series local observables;
5. ordered-gap dynamics.

A nontrivial result must do more than restate Pontryagin duality or the Chinese remainder theorem. It must produce a new invariant, operator identity, convergence theorem, or recoverability statement not already implied by standard profinite harmonic analysis.

### OP-F14 — Half-kernel versus half-boundary

The dual dyadic operator has the exact kernel

\[
\ker(r\mapsto2r\text{ on }\mathbb Q/\mathbb Z)=\{0,1/2\}.
\]

On-Primes independently has a half-integer boundary lemma in the original affine variable. These are mathematically distinct occurrences of \(1/2\).

Open task: determine whether there is a rigorous conjugacy, functorial relation, or no-go theorem between these two appearances. Numerical coincidence alone is not evidence of identity.


### OP-F15 — Resonance hypergraph compression

The finite common-clock law now distinguishes two layers:

\[
\text{local singular-series marginals}
\]

versus

\[
\text{cross-channel dyadic resonances}.
\]

For finite prime support \(P\), the exact correction

\[
\mathcal C_P(h)
=
\left\langle\prod_{p\in P}B_p(2^rh)\right\rangle_r
-
\prod_{p\in P}\left\langle B_p(2^rh)\right\rangle_r
\]

vanishes whenever the effective local periods are pairwise coprime, while shared period factors can create nonzero corrections when local Fourier supports satisfy the resonance equation

\[
\sum_p \frac{m_p}{d_p(h)}\in\mathbb Z.
\]

The next hard gate is to determine whether the resulting resonance hypergraph admits a compression or invariant that survives increasing prime support and separates actual ordered prime/twin-gap data from suitable null models.

A valid global claim must specify:

1. the support-growth rule \(P\to\infty\);
2. normalization/renormalization of local factors;
3. convergence or projective consistency;
4. a null model preserving trivial modular carriers;
5. an invariant not already forced by the multiplicative-order table alone.

### OP-F16 — Zeta bridge only after resonance closure

Do not map the resonance hypergraph directly to zeta zeros.

A zeta bridge becomes admissible only after a global ARPL observable is shown to have a controlled limit or transform. The preferred route remains an explicit formula or a rigorously smoothed prime-power measure. Any proposed correspondence with zero ordinates must preserve the distinction between:

- exact finite modular resonance;
- conjectural prime-tuple occurrence asymptotics;
- analytic continuation;
- zero-spectrum statistics.


### OP-F17 — Coupled global resonance limit

The independent global orbit baseline is now closed:

\[
\mathcal I(h)
=
\prod_{p\ge5}\mu_p(h)
\]

exists, is finite and positive for every fixed \(h\ne0\), and satisfies

\[
\mathcal I(2^kh)=\mathcal I(h).
\]

The remaining global problem is no longer existence of a phase-space observable. It is whether the **shared-clock** finite-support means

\[
M_P(h)
=
\left\langle
\prod_{p\in P}B_p(2^rh)
\right\rangle_r
\]

converge under an explicit support-growth rule and, if so, how their limit differs from \(\mathcal I(h)\).

Equivalently, determine whether the exact finite corrections

\[
\mathcal C_P(h)
=
M_P(h)-\prod_{p\in P}\mu_p(h)
\]

admit a controlled infinite-support limit.

Required outputs:

1. a support-growth convention;
2. a summable bound or cancellation theorem for connected resonance contributions;
3. proof of convergence, or a no-go/divergence theorem;
4. comparison against null phase clocks preserving all local orbit means.

### OP-F18 — Connected resonance expansion

Develop a connected/cumulant expansion for the deterministic common-clock observables. The goal is to separate reducible products of lower-order resonances from genuinely multi-channel terms.

A successful formulation should produce weights \(K(J;h)\) on finite prime subsets \(J\) such that:

- \(K(J;h)=0\) whenever the common-clock dynamics factorizes across a nontrivial partition of \(J\);
- the moment \(M_P(h)\) can be reconstructed from connected weights by the usual partition expansion;
- convergence of a suitable sum of connected weights would imply convergence of the fully coupled global observable.

This is the current hard gate.


### OP-F18 status update — finite connected expansion CLOSED

The finite connected/cumulant expansion is now exact. The connected weights

\[
K(J;h)
\]

reconstruct all finite common-clock moments by partition expansion, and vanish across distinct period-overlap components.

The finite compression problem is therefore closed at the algebraic level.

### OP-F19 — Infinite connected-cluster convergence

The remaining problem is analytic:

Determine whether the connected weights obey a summable bound under a specified increasing prime support, sufficient to make the connected expansion converge.

A successful theorem could take the form

\[
\sum_{\substack{J\ni p_0\\|J|\ge2}}
|K(J;h)|\,W(J)<\infty
\]

for an explicit weight \(W\), or an equivalent cluster criterion.

This would promote the finite decomposition

\[
\text{baseline}+\text{connected resonances}
\]

to a fully coupled infinite-channel ARPL observable.

Failure to obtain such a bound should be recorded as a no-go rather than hidden by finite numerics.


### OP-F19 status update — fixed-order infinite-channel layers CLOSED

For every fixed connected order \(n\ge2\), the global prime-channel sum

\[
\mathcal K_n(h)
=
\sum_{\substack{J\subset\mathbb P_{\ge5}\\|J|=n}}
K(J;h)
\]

is now absolutely convergent for every fixed \(h\ne0\).

The proof uses the exact resonance-kernel estimate

\[
|M_X(J;h)|
\le
2^{|J|}
\frac{\prod_{p\in J}\alpha_p}
{\operatorname{lcm}_{p\in J}d_p}
\]

and the resulting cumulant bound with one surviving factor
\(1/\max d_p\). Since

\[
d_p=\operatorname{ord}_p(2)\ge\log_2(p+1),
\]

the remaining prime sum is controlled by Mertens plus
\(\pi(x)\ll x/\log x\).

Therefore the analytic frontier has moved again.

### OP-F20 — all-orders cluster convergence

The unresolved series is now only the connected-order sum

\[
\sum_{n\ge2}\mathcal K_n(h).
\]

The current Bell/factorial cumulant majorant is not summable in \(n\), so fixed-order convergence cannot be promoted mechanically.

The next valid routes are:

1. derive a much sharper connected-graph/tree bound replacing Bell growth;
2. exploit the exact local mode-selection zeros to reduce combinatorics;
3. prove sufficient decay from increasing least common multiples inside connected clusters;
4. or establish a no-go showing that the unrenormalized all-orders expansion diverges and identify the correct renormalized object.

No all-orders convergence claim is made yet.


### OP-F21 — time average of the exact instantaneous factorization

The instantaneous infinite-channel singular-series state is now closed:

\[
\mathfrak S(H_{2^rh})
=
\frac{27}{2}C_*Z(h)R(4^rh^2-4).
\]

Therefore the fully coupled common-clock problem can be restated without an infinite Euler product at each time:

\[
\frac1T\sum_{r<T}\mathfrak S(H_{2^rh})
=
\frac{27}{2}C_*Z(h)
\frac1T\sum_{r<T}R(4^rh^2-4).
\]

The unresolved global question is now the mean behavior of the finite divisor-weight observable

\[
R(4^rh^2-4)
=
\prod_{\substack{p\mid 4^rh^2-4\\p\ge5}}
\frac{p-3}{p-4}.
\]

This is a sharper target than an abstract infinite-channel cluster sum.

Required next steps:

1. determine whether the Cesaro mean of \(R(4^rh^2-4)\) exists for fixed admissible \(h\);
2. compare it with the independently averaged baseline \(\mathcal I(h)\);
3. express any discrepancy through the connected resonance layers \(\mathcal K_n(h)\);
4. identify relevant prior art for divisor statistics of exponential sequences \(a\,4^r-4\).

No mean-value theorem is claimed yet.


### OP-F22 — Scaled prime-power form-factor closure

The finite frequency bridge is closed:

\[
K_{\Gamma,T}(\tau_q)
=
N|R_q|^2,
\qquad
\tau_q=\frac{\log q}{\log(T/2\pi)}.
\]

The remaining asymptotic gate is to construct a continuation-safe and properly windowed arithmetic family \(q(T)\) with

\[
\log q(T)\sim\tau\log(T/2\pi)
\]

for fixed \(0<\tau<1\), and derive the connected pair-power limit from the prime/explicit-formula side without inserting the sine kernel or Montgomery target.

A valid theorem must explicitly separate fixed-\(q\) Landau asymptotics, \(q(T)\)-scaled frequencies, local versus global zero windows, diagonal terms, smoothing, and every RH-dependent step.

### OP-F23 — Noncircular zeta occupancy/operator binding

Projector geometry, the sine kernel, the ramp/plateau, and the prime-power frequency coordinate are now closed in their declared sectors. What remains for a zeta-specific derivation is an operator/state theorem that maps the prime/Weil spectral object to the local zero process strongly enough to transfer those forced projector statistics.

If RH is itself the target, Montgomery's RH-conditional subcritical ramp may be used only as external validation, not as a premise. The conjectured plateau for \(|\alpha|>1\) likewise cannot be imported as a proof step.

A successful closure must be zero-list-free at the derivation layer and must identify the normalization/window/projector or an equivalent pair-process object from arithmetic data.
