# ARPL Singular-Series Phase Bridge v0.1

Status: exact finite identities + standard singular-series machinery + project-specific operator packaging.

## 1. Prime-pair local phase factor

For a prime \(p\) and integer gap \(h\), the Ramanujan sum satisfies

\[
c_p(h)=
\begin{cases}
p-1,&p\mid h,\\
-1,&p\nmid h.
\end{cases}
\]

Define the local pair factor

\[
A_p(h)
=
1+\frac{c_p(h)}{(p-1)^2}.
\]

Because \(c_p(h)\) depends only on \(h\bmod p\), \(A_p\) is a local observable of the ARPL phase coordinate at modulus \(p\).

For \(p=2\),

\[
A_2(h)=
\begin{cases}
2,&2\mid h,\\
0,&2\nmid h.
\end{cases}
\]

Thus parity is the first exact carrier gate for prime-pair separation.

## 2. Finite Euler--Ramanujan factorization — OP-D037

Let \(P\) be a finite set of distinct primes. Define

\[
\mathfrak S_P(h)
=
\prod_{p\in P}
\left(
1+\frac{c_p(h)}{(p-1)^2}
\right).
\]

Ramanujan sums are multiplicative in the modulus for coprime moduli. Expanding the finite product therefore gives exactly

\[
\boxed{
\mathfrak S_P(h)
=
\sum_{\substack{q\ {\rm squarefree}\\p\mid q\Rightarrow p\in P}}
\frac{c_q(h)}{\varphi(q)^2}.
}
\]

Since every such \(q\) is squarefree, \(\mu(q)^2=1\), so this is the finite-support form of the standard prime-pair Ramanujan expansion

\[
\mathfrak S(h)
=
\sum_{q\ge1}
\frac{\mu(q)^2}{\varphi(q)^2}c_q(h)
=
\prod_p
\left(
1+\frac{c_p(h)}{(p-1)^2}
\right),
\]

where the infinite identity is standard singular-series theory.

Therefore the finite singular-series value is a deterministic functional of the finite modular phase signature

\[
(h\bmod p)_{p\in P}.
\]

## 3. Dyadic invariance in the even prime-pair sector — OP-D038

For even nonzero \(h\),

\[
\boxed{
\mathfrak S(2h)=\mathfrak S(h).
}
\]

At the finite-product level this is immediate. For every odd prime \(p\),

\[
p\mid 2h\iff p\mid h,
\]

and both \(h\) and \(2h\) are divisible by \(2\). Hence every local factor \(A_p\) is unchanged.

Equivalently, after the parity channel has entered the admissible even sector, the prime-pair singular series is invariant under the ARPL dyadic transport

\[
h\mapsto2h.
\]

This does not prove occurrence of prime pairs; it is an exact invariance of the Hardy--Littlewood local-density factor.

## 4. Twin-start gap as a four-point pattern

Two twin-prime pairs whose starts differ by \(h\) correspond to the pattern

\[
H_h=\{0,2,h,h+2\}.
\]

For a prime \(p\), let

\[
\nu_p(h)
=
\#\{0,2,h,h+2\}\pmod p.
\]

The standard \(k\)-tuple local factor for this four-point pattern is

\[
B_p(h)
=
\frac{1-\nu_p(h)/p}{(1-1/p)^4}.
\]

Again \(\nu_p(h)\), hence \(B_p(h)\), depends only on \(h\bmod p\). It is therefore a local observable on the ARPL phase channel at \(p\).

## 5. Exact six-lock for two twin pairs — OP-D039

For \(p=2\),

\[
\nu_2(h)<2
\iff
h\equiv0\pmod2.
\]

For \(p=3\),

\[
\nu_3(h)<3
\iff
h\equiv0\pmod3.
\]

Consequently

\[
B_2(h)B_3(h)>0
\iff
h\equiv0\pmod6.
\]

Thus the six-lock is not merely a property of already observed twin-prime starts. It is exactly the local admissibility condition for the four-point pattern

\[
\{0,2,h,h+2\}
\]

against the first two prime channels.

Higher prime channels \(p\ge5\) do not create an analogous universal zero for this four-point pattern, because four residues cannot cover all classes modulo \(p>4\). Instead they modulate the local singular-series amplitude through \(h\bmod p\).

## 6. Dyadic local-factor dynamics — OP-D040

Under the existing On-Primes dyadic map, a separation evolves as

\[
h_r=2^rh.
\]

For each prime \(p\), define the residue orbit

\[
u_r=h_r\bmod p.
\]

Then

\[
u_{r+1}=2u_r\bmod p.
\]

The twin-quadruplet local factor evolves as the observable

\[
\boxed{
B_p(h_r)=B_p(u_r),
\qquad
u_{r+1}=2u_r\bmod p.
}
\]

Thus the same finite phase-doubling orbit already used by the fibre obstruction layer also drives the local Hardy--Littlewood amplitude for the two-twin-pair pattern.

For \(p=2,3\), once \(h\equiv0\pmod6\), those carrier channels remain locked under all dyadic iterations. For \(p\ge5\), the higher-channel amplitudes run around finite residue orbits and provide modulation.

## 7. What the reverse-test establishes

The reverse-test closes the following diagram exactly at the finite/local level:

\[
\text{gap }h
\longrightarrow
(h\bmod p)_p
\longrightarrow
\{c_p(h),\nu_p(h)\}_p
\longrightarrow
\text{local singular factors}
\longrightarrow
\text{finite singular product}.
\]

For the existing dyadic dynamics,

\[
h\mapsto2h
\]

becomes

\[
u_p\mapsto2u_p\pmod p
\]

on every local channel.

This means the singular-series layer is not external to ARPL: it is an observable of the same modular phase state.

## 8. Prior-art boundary

The following are standard and not claimed as new:

- Ramanujan sums and their multiplicativity;
- the prime-pair singular series and its Ramanujan/Euler-product representations;
- the Hardy--Littlewood prime \(k\)-tuple singular series
  \[
  \mathfrak S(H)=
  \prod_p
  \left(1-\frac{\nu_p(H)}p\right)
  \left(1-\frac1p\right)^{-|H|};
  \]
- admissibility defined by \(\nu_p(H)<p\) for every prime \(p\).

The project-specific ARPL step is the operator packaging: interpreting these local factors as observables on the same modular phase coordinates whose dynamics under \(T(x)=2x+1\) is exact phase doubling/squaring.

No claim of literature novelty for that packaging is made until a systematic search is completed.

## 9. No-go

This theorem pack does not prove:

- infinitely many prime pairs at any fixed gap;
- infinitely many twin primes;
- Hardy--Littlewood prime-pair or \(k\)-tuple conjectures;
- a zeta-zero equivalence;
- RH.

It proves exact identities about the local-density/singular-series objects conditional only on their definitions.
