# ARPL Connected Resonance Expansion v0.1

Status: exact finite combinatorial/operator theorem pack.

## 1. Common-clock moments

For a finite set \(J\) of prime channels \(p\ge5\), define

\[
M(J;h)
=
\left\langle
\prod_{p\in J}B_p(2^rh)
\right\rangle_r,
\]

where the average is over one common dyadic period and

\[
M(\varnothing;h)=1.
\]

For a singleton,

\[
M(\{p\};h)=\mu_p(h).
\]

## 2. Connected resonance cumulant — OP-D057

Define

\[
\boxed{
K(J;h)
=
\sum_{\pi\in\Pi(J)}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{A\in\pi}M(A;h),
}
\]

where \(\Pi(J)\) is the set of set partitions of \(J\).

Equivalently, moments reconstruct from connected terms by

\[
\boxed{
M(J;h)
=
\sum_{\pi\in\Pi(J)}
\prod_{A\in\pi}K(A;h).
}
\]

This is the standard moment--cumulant Möbius inversion on the partition lattice, applied here to deterministic periodic ARPL observables.

For two channels,

\[
K(\{p,q\};h)
=
M(\{p,q\};h)-M(\{p\};h)M(\{q\};h),
\]

so

\[
\boxed{
K(\{p,q\};h)=\mathcal C_{\{p,q\}}(h).
}
\]

Thus the previously defined pair resonance correction is exactly the connected two-channel term.

## 3. Genuine three-channel term

For three channels,

\[
\begin{aligned}
K(p,q,s;h)
={}&M(p,q,s;h)
-M(p,q;h)M(s;h)\\
&-M(p,s;h)M(q;h)
-M(q,s;h)M(p;h)\\
&+2M(p;h)M(q;h)M(s;h).
\end{aligned}
\]

This removes every reducible contribution built from singleton and pair moments.

For \(h=6\),

\[
\boxed{
K(\{7,13,19\};6)
=
-\frac{5168743489}{457019805007872}
\ne0.
}
\]

Therefore the common dyadic clock contains an exact connected three-channel term not reducible to products of its one- and two-channel moments.

By contrast,

\[
K(\{5,7,11\};6)=0.
\]

These are identities of the finite periodic observables, not prime-occurrence statistics.

## 4. Period-overlap graph

For fixed \(h\), assign to each channel its effective period

\[
d_p(h)=
\begin{cases}
1,&p\mid h,\\
\operatorname{ord}_p(2),&p\nmid h.
\end{cases}
\]

Define the period-overlap graph \(G_h(P)\) on a finite prime set \(P\) by

\[
p\sim q
\iff
\gcd(d_p(h),d_q(h))>1.
\]

Let its connected components be

\[
C_1,\dots,C_s.
\]

If \(i\ne j\), then every period from \(C_i\) is coprime to every period from \(C_j\). Therefore

\[
D_i=\operatorname{lcm}_{p\in C_i}d_p(h)
\]

and

\[
D_j=\operatorname{lcm}_{p\in C_j}d_p(h)
\]

are coprime.

## 5. Component factorization theorem — OP-D058

By the Chinese remainder theorem, the common clock modulo

\[
L=\prod_i D_i
\]

samples the component clocks independently. Hence

\[
\boxed{
M(P;h)
=
\prod_{i=1}^s M(C_i;h).
}
\]

Example at \(h=6\):

\[
P=\{7,13,31\}
\]

has effective periods

\[
3,\ 12,\ 5,
\]

so the components are

\[
\{7,13\},
\qquad
\{31\},
\]

and exactly

\[
\boxed{
M(\{7,13,31\};6)
=
M(\{7,13\};6)M(\{31\};6).
}
\]

## 6. Connected-support theorem — OP-D059

Suppose a finite channel set \(J\) intersects more than one connected component of \(G_h(P)\).

Then the joint moment factorizes across a nontrivial partition of \(J\). Standard cumulant Möbius inversion therefore gives

\[
\boxed{
K(J;h)=0.
}
\]

Consequently every nonzero connected resonance term is contained inside a single component of the period-overlap graph.

This gives an exact compression rule:

\[
\boxed{
\text{no connected cumulant needs to be evaluated across different period components.}
}
\]

The overlap graph is only an upper envelope: a connected component may still contain vanishing cumulants because local Fourier mode-selection rules can remove all compatible resonances.

## 7. Weighted resonance hypergraph

Define the connected ARPL resonance hypergraph by assigning each finite prime subset \(J\) the exact rational weight

\[
\boxed{
w_h(J)=K(J;h).
}
\]

A hyperedge exists exactly when

\[
w_h(J)\ne0.
\]

Then:

- singleton weights are local orbit means;
- 2-hyperedges are pair resonance corrections;
- higher hyperedges are irreducible common-clock couplings;
- all hyperedges lie inside period-overlap components.

This converts the dyadic resonance structure from a binary graph into a lossless finite connected expansion.

## 8. Reconstruction

For any finite support \(P\), the full common-clock mean can be reconstructed from connected hyperedge weights:

\[
\boxed{
M(P;h)
=
\sum_{\pi\in\Pi(P)}
\prod_{J\in\pi}w_h(J).
}
\]

No pairwise approximation is assumed.

## 9. Global direction

The independently averaged infinite baseline

\[
\mathcal I(h)=\prod_{p\ge5}\mu_p(h)
\]

is already convergent.

A sufficient route to the fully coupled infinite observable would be a convergent connected/cluster expansion controlling the higher-order weights \(K(J;h)\) as prime support grows.

No such infinite connected-weight bound is proved here.

## 10. Prior-art boundary

Moment--cumulant inversion, partition lattices, CRT factorization, and finite Fourier orthogonality are standard mathematics.

The ARPL-specific construction is the application of this exact connected expansion to the dyadic singular-factor common clock, together with the multiplicative-order period graph and its resonance hypergraph weights.

Novelty remains unestablished pending systematic literature review.
