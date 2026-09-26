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
