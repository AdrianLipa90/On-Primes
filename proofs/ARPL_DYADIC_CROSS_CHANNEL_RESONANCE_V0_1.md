# ARPL Dyadic Cross-Channel Resonance Law v0.1

Status: exact finite theorem pack; novelty not established.

## 1. Local clocks

Fix a finite set \(P\) of odd primes \(p\ge5\). For the two-twin-pair local observable

\[
B_p(h)=
\frac{1-\nu_p(\{0,2,h,h+2\})/p}{(1-1/p)^4},
\]

consider the common dyadic clock

\[
h_r=2^r h.
\]

If \(p\nmid h\), the local residue orbit has period

\[
d_p=\operatorname{ord}_p(2).
\]

If \(p\mid h\), the local residue is the fixed state \(0\), so the effective period is \(1\).

Write this effective period as \(d_p(h)\).

The local time series is

\[
b_p(r)=B_p(2^r h),
\qquad
b_p(r+d_p(h))=b_p(r).
\]

## 2. Global common-clock period — OP-D048

For finite support \(P\), the finite-product observable

\[
B_P(r;h)=\prod_{p\in P}B_p(2^r h)
\]

is periodic with period dividing

\[
\boxed{
L_P(h)=\operatorname{lcm}_{p\in P} d_p(h).
}
\]

Therefore its exact common-clock mean is

\[
\langle B_P\rangle_h
=
\frac1{L_P(h)}
\sum_{r=0}^{L_P(h)-1}
\prod_{p\in P}B_p(2^r h).
\]

This is a finite rational number because every local factor is rational.

## 3. Local Fourier decomposition

For each channel define normalized coefficients

\[
\widehat b_p(m)
=
\frac1{d_p}
\sum_{r=0}^{d_p-1}
b_p(r)
e^{-2\pi i mr/d_p},
\qquad
m=0,\dots,d_p-1,
\]

where \(d_p=d_p(h)\).

Then

\[
b_p(r)
=
\sum_{m=0}^{d_p-1}
\widehat b_p(m)e^{2\pi i mr/d_p}.
\]

## 4. Cross-channel resonance theorem — OP-D049

Substituting every local Fourier expansion into the common-clock product and averaging over one global period gives

\[
\boxed{
\langle B_P\rangle_h
=
\sum_{\mathbf m\in\mathcal R_P(h)}
\prod_{p\in P}\widehat b_p(m_p),
}
\]

where the resonance set is

\[
\boxed{
\mathcal R_P(h)
=
\left\{
(m_p)_{p\in P}:
0\le m_p<d_p(h),\quad
\sum_{p\in P}\frac{m_p}{d_p(h)}\in\mathbb Z
\right\}.
}
\]

Proof: after multiplying the Fourier series, the average of

\[
\exp\left(
2\pi i r
\sum_{p\in P}\frac{m_p}{d_p}
\right)
\]

over \(r=0,\dots,L_P-1\) is \(1\) exactly when the total frequency is an integer and \(0\) otherwise.

Thus only frequency tuples satisfying the exact resonance equation survive the global average.

## 5. Resonance correction — OP-D050

The independent product of local means is

\[
\prod_{p\in P}\langle B_p\rangle_h
=
\prod_{p\in P}\widehat b_p(0).
\]

Define the dyadic cross-channel resonance correction

\[
\boxed{
\mathcal C_P(h)
=
\langle B_P\rangle_h
-
\prod_{p\in P}\langle B_p\rangle_h.
}
\]

Then

\[
\boxed{
\mathcal C_P(h)
=
\sum_{\substack{\mathbf m\in\mathcal R_P(h)\\
\mathbf m\ne\mathbf 0}}
\prod_{p\in P}\widehat b_p(m_p).
}
\]

Therefore \(\mathcal C_P(h)\) measures exactly the contribution of nonzero common-clock phase resonances. It is not a fitted covariance or a probabilistic ansatz.

## 6. Coprime-period factorization theorem — OP-D051

If the effective periods

\[
\{d_p(h):p\in P\}
\]

are pairwise coprime, then the only resonance tuple is

\[
m_p=0
\quad\forall p.
\]

Hence

\[
\boxed{
\langle B_P\rangle_h
=
\prod_{p\in P}\langle B_p\rangle_h
}
\]

and therefore

\[
\boxed{
\mathcal C_P(h)=0.
}
\]

Proof: let \(L=\prod_pd_p\), valid under pairwise coprimality. The resonance condition is

\[
\sum_p m_p\frac{L}{d_p}\equiv0\pmod L.
\]

Reducing modulo \(d_j\), every term except \(j\) vanishes and

\[
m_j\frac{L}{d_j}\equiv0\pmod{d_j}.
\]

Because \(\gcd(L/d_j,d_j)=1\), this forces \(m_j=0\pmod{d_j}\). Since \(0\le m_j<d_j\), \(m_j=0\).

## 7. Local mode filters from the twin observable

For \(p\ge5\), the local observable has the exact defect form

\[
B_p(u)
=
\beta_p
+
\alpha_p
\left(
2\mathbf1_{u=0}
+
\mathbf1_{u=2}
+
\mathbf1_{u=-2}
\right).
\]

For a nonzero ordinary doubling orbit that contains neither \(+2\) nor \(-2\), the observable is constant, so only mode \(m=0\) survives.

For a special orbit:

- if \(d_p\) is even, \(+2\) and \(-2\) are half an orbit apart and only even modes survive;
- if \(d_p\) is odd, the two defects lie on different cycles and each special cycle has full mode support.

Thus a nonzero global resonance correction requires not merely shared divisors of local periods, but compatible nonzero mode support.

## 8. Dyadic resonance hypergraph

For fixed \(h\), define vertices by the active prime channels \(p\ge5\).

A finite subset \(J\) of vertices is called resonant when

\[
\mathcal C_J(h)\ne0.
\]

Equivalently, the common-clock observable on \(J\) fails to factor into the product of its local orbit means.

This defines a finite **dyadic resonance hypergraph**

\[
\mathcal H_h(P)
=
\{J\subseteq P:|J|\ge2,\ \mathcal C_J(h)\ne0\}.
\]

The hypergraph is an exact deterministic object derived from modular phase dynamics. It is not a statistical correlation graph.

## 9. Exact examples at h=6

Using the local twin-quadruplet factors:

\[
P=\{5,7\}:
\qquad
d_5=4,\quad d_7=3,
\]

so the periods are coprime and

\[
\mathcal C_{\{5,7\}}(6)=0.
\]

For

\[
P=\{7,13\},
\qquad
d_7=3,\quad d_{13}=12,
\]

the common clock contains nonzero compatible resonances and exact rational evaluation gives

\[
\frac{\langle B_{\{7,13\}}\rangle_6}
{\langle B_7\rangle_6\langle B_{13}\rangle_6}
=
\boxed{\frac{549}{550}},
\]

so

\[
\mathcal C_{\{7,13\}}(6)\ne0.
\]

For

\[
P=\{7,13,19\},
\]

the exact ratio is

\[
\boxed{
\frac{\langle B_{\{7,13,19\}}\rangle_6}
{\langle B_7\rangle_6
 \langle B_{13}\rangle_6
 \langle B_{19}\rangle_6}
=
\frac{18657}{18700}.
}
\]

These are finite exact-rational identities for the defined observables; they are not prime-occurrence frequencies.

## 10. Relation to standard mathematics

The derivation uses only standard finite Fourier orthogonality, multiplicative orders, and Hardy--Littlewood local factors.

The project-specific object is the integration of these ingredients into the ARPL common-clock operator and the explicit resonance correction/hypergraph built from the dyadic evolution \(h\mapsto2h\).

A targeted prior-art search did not surface this exact combined formulation, but that is insufficient to establish novelty.

## 11. No-go

This theorem pack does not prove:

- statistical dependence of actual prime occurrences across prime channels;
- the twin-prime conjecture;
- the Hardy--Littlewood prime \(k\)-tuple conjecture;
- a zeta-zero equivalence;
- RH.

It proves an exact deterministic coupling law for the finite singular-series observables under the shared dyadic clock.
