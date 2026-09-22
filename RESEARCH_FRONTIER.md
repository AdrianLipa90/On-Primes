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
