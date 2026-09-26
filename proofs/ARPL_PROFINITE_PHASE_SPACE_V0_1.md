# ARPL Profinite Phase Space v0.1

Status: standard profinite/Pontryagin structure specialized to the On-Primes ARPL operator.

## 1. Canonical completion of the phase signature

The complete compatible residue state of an integer is naturally an element of the profinite completion

\[
\widehat{\mathbb Z}
=
\varprojlim_n \mathbb Z/n\mathbb Z
\cong
\prod_p \mathbb Z_p.
\]

The canonical embedding

\[
\iota:\mathbb Z\hookrightarrow\widehat{\mathbb Z}
\]

sends an integer to its compatible family of residues modulo every \(n\), equivalently to all of its \(p\)-adic coordinates.

Therefore the complete ARPL modular phase signature is not an ad hoc product of channels: its canonical compact arithmetic state space is \(\widehat{\mathbb Z}\).

This identification is standard profinite mathematics.

## 2. Canonical phase dual

The Pontryagin dual of \(\widehat{\mathbb Z}\) is

\[
\widehat{\widehat{\mathbb Z}}
\cong
\mathbb Q/\mathbb Z
\]

with the discrete topology.

A rational frequency

\[
r=\frac aq\pmod1
\]

acts on an embedded integer \(n\) by the character

\[
\chi_r(n)
=
e^{2\pi i rn}
=
e^{2\pi i an/q}.
\]

Thus the modular phase characters already used in ARPL are precisely the finite-order characters of the canonical profinite arithmetic state space.

## 3. Ramanujan shells in the dual group — OP-D044

The elements of exact order \(q\) in \(\mathbb Q/\mathbb Z\) are

\[
\left\{
\frac aq\pmod1:(a,q)=1
\right\}.
\]

Therefore the Ramanujan sum is exactly the character sum over the order-\(q\) frequency shell:

\[
\boxed{
c_q(n)
=
\sum_{\substack{r\in\mathbb Q/\mathbb Z\\\operatorname{ord}(r)=q}}
\chi_r(n).
}
\]

Hence the standard prime-pair singular series can be written as the weighted arithmetic spectral observable

\[
\boxed{
\mathfrak S(h)
=
\sum_{q\ge1}
\frac{\mu(q)^2}{\varphi(q)^2}
\sum_{\operatorname{ord}(r)=q}
\chi_r(h).
}
\]

This is a repackaging of the standard Ramanujan expansion in the canonical Pontryagin dual language; the formula itself is not claimed as new.

## 4. Global dyadic operator — OP-D045

The ARPL gap transport is multiplication by two:

\[
D:\widehat{\mathbb Z}\to\widehat{\mathbb Z},
\qquad
D(x)=2x.
\]

Under

\[
\widehat{\mathbb Z}\cong\prod_p\mathbb Z_p,
\]

the operator decomposes componentwise.

For every odd prime \(p\), \(2\) is a unit in \(\mathbb Z_p\), so

\[
x_p\mapsto2x_p
\]

is an automorphism.

For \(p=2\),

\[
x_2\mapsto2x_2
\]

is injective but not surjective and satisfies

\[
v_2(2x_2)=v_2(x_2)+1
\]

for nonzero \(x_2\). Its image is \(2\mathbb Z_2\), of index 2.

Consequently

\[
D(\widehat{\mathbb Z})
=
2\widehat{\mathbb Z}
\]

is an index-2 subgroup. The global dyadic operator is therefore invertible on every odd \(p\)-adic channel and one-way on the \(2\)-adic channel.

## 5. Dual dyadic operator and the half-kernel — OP-D046

The pullback of a character by \(D\) is

\[
(D^*\chi_r)(x)
=
\chi_r(2x)
=
\chi_{2r}(x).
\]

Therefore on the dual frequency group

\[
D^*:\mathbb Q/\mathbb Z\to\mathbb Q/\mathbb Z,
\qquad
r\mapsto2r.
\]

This map is surjective and has kernel

\[
\boxed{
\ker D^*
=
\left\{
0,\frac12
\right\}.
}
\]

Proof: \(2r=0\pmod1\) iff \(r=0\) or \(r=1/2\pmod1\).

Thus \(1/2\) is the unique nonzero character frequency annihilated by one dual dyadic step.

This statement concerns the dual group \(\mathbb Q/\mathbb Z\). It must not be conflated with the separate half-integer boundary lemma already present in On-Primes, although both arise from the same multiplication-by-two arithmetic.

## 6. Odd-shell permutation and even-shell collapse — OP-D047

If \(q\) is odd and \(r=a/q\) has exact order \(q\), then

\[
2r=\frac{2a}{q}
\]

also has exact order \(q\), because \(2\) is invertible modulo \(q\). Hence \(D^*\) permutes every odd-denominator order shell.

If \(q\) is even and \(r=a/q\) has exact order \(q\), then \(a\) is odd and

\[
2r=\frac{a}{q/2}\pmod1,
\]

so the order loses one factor of 2.

Therefore the dual dyadic action has an exact asymmetry:

\[
\boxed{
\text{odd denominator shells are permuted;}
\qquad
\text{even denominator shells flow toward their odd part.}
}
\]

For squarefree denominators this removes the factor \(2\) in one step.

## 7. Relation to the singular-series invariance

The standard prime-pair singular series is supported only on squarefree denominator shells through \(\mu(q)^2\).

Under \(D^*\):

- odd squarefree shells are internally permuted;
- even squarefree shells \(2m\) collapse onto the corresponding odd shell \(m\).

This is the dual-group form of the special role of the parity channel in prime-pair admissibility and of the previously proved even-sector identity

\[
\mathfrak S(2h)=\mathfrak S(h)
\qquad
(h\ \text{even}).
\]

## 8. Structural consequence for ARPL

The current ARPL phase law now has a canonical global architecture:

\[
\boxed{
\widehat{\mathbb Z}
\quad\overset{\mathrm{Pontryagin}}{\longleftrightarrow}\quad
\mathbb Q/\mathbb Z.
}
\]

On the state side:

\[
x\mapsto2x.
\]

On the frequency side:

\[
r\mapsto2r.
\]

Locally:

\[
\mathbb Z_p:
\begin{cases}
\text{automorphism},&p\ne2,\\
\text{injective index-2 contraction in the }2\text{-adic filtration},&p=2.
\end{cases}
\]

This provides the global operator space for the finite prime-channel transfer operators already derived in ARPL.

## 9. Epistemic boundary

All group-theoretic identifications used here are standard:

- \(\widehat{\mathbb Z}\cong\prod_p\mathbb Z_p\);
- Pontryagin dual \((\widehat{\mathbb Z})^\vee\cong\mathbb Q/\mathbb Z\);
- characters \(e^{2\pi ian/q}\);
- Ramanujan sums as sums over primitive order-\(q\) characters.

The project-specific contribution is their integration with the existing On-Primes dyadic fibres, ordered-gap representation, modular obstruction phase orbits, singular-series observables, and transfer operator.

No claim is made here that this integration by itself constitutes a new theorem of prime distribution.
