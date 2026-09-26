# Skewes–Euler–Hilbert–Collatz Bridge v0.1

Status: \`ADDITIVE_RESEARCH_NOTE / EXACT_LOCAL_THEOREMS + STANDARD_ANALYTIC_INPUT + OPEN_SPECTRAL_PROGRAMME\`

This note adds a rigorously typed bridge between the dyadic fibres already used in **On Primes**, the countable self-embedding structure of Hilbert's Hotel, the Littlewood–Skewes sign-reversal phenomenon for prime counting, and the inverse fibres of the accelerated odd Collatz map.

It does **not** claim a proof of RH, Collatz, or a new prime-distribution theorem.

## 1. A common affine-dilation normal form

For \(q>0\) and a constant \(c\), define

\[
F_{q,c}(x)=qx+(q-1)c.
\]

Let \(h_c(x)=x+c\). Then

\[
h_c(F_{q,c}(x))=q\,h_c(x),
\]

so \(F_{q,c}\) is exactly conjugate to pure multiplication by \(q\). Its fixed point is \(-c\).

For the existing On-Primes map

\[
T(x)=2x+1,
\]

we have

\[
T=F_{2,1},
\qquad
T(x)+1=2(x+1).
\]

Hence for the dyadic fibre

\[
x_{a,k}=a2^k-1
\]

the logarithmic coordinate

\[
\tau_P(x)=\log(x+1)
\]

obeys the exact translation law

\[
\tau_P(Tx)-\tau_P(x)=\log 2.
\]

This is the existing dyadic fibre written as a translation lattice in log-coordinate.

## 2. Euler's infinitude of primes as an exact Hilbert-Hotel embedding

Let

\[
\mathcal H=\ell^2(\mathbb N)
\]

with basis \(|n\rangle\), and let \(p_n\) be the \(n\)-th prime. Since the set of primes is infinite and contained in \(\mathbb N\), it is countably infinite. Define

\[
V_{\mathbb P}|n\rangle=|p_n\rangle.
\]

If \(P\) is the projector onto prime-labelled basis states, then

\[
V_{\mathbb P}^\dagger V_{\mathbb P}=I,
\qquad
V_{\mathbb P}V_{\mathbb P}^\dagger=P.
\]

Thus the full countable basis embeds isometrically into the proper prime subspace. This is an exact Hilbert-Hotel-type self-embedding induced by prime infinitude.

Separately, the affine map \(n\mapsto2n+1\) defines another basis isometry

\[
A|n\rangle=|2n+1\rangle,
\]

whose range is a proper arithmetic-progression subspace. It is not a prime-preserving isometry; prime survival under \(2p+1\) is precisely the Cunningham/Sophie-Germain mask already tracked by this repository.

## 3. Littlewood–Skewes sign reversal and the zeta phase spectrum

Define

\[
\Delta(x)=\pi(x)-\operatorname{li}(x).
\]

A standard theorem of Littlewood states that \(\Delta(x)\) changes sign infinitely often. Skewes' work gave historically enormous upper bounds for the first region where \(\pi(x)>\operatorname{li}(x)\); later work reduced those upper bounds drastically. The exact first positive integer remains a separate computational question.

The rigorous analytic bridge is not "Skewes causes Collatz". It is:

\[
\text{Euler product / primes}
\longleftrightarrow
\zeta(s)
\longleftrightarrow
\text{nontrivial zeros}
\longleftrightarrow
\text{oscillatory prime-counting error}.
\]

In every explicit-formula term associated with a zero

\[
\rho=\beta+i\gamma,
\]

the factor

\[
x^\rho
=
e^{\beta\log x}\,e^{i\gamma\log x}
\]

contains an exact phase with log-frequency \(\gamma\).

Therefore, in the logarithmic variable

\[
t=\log x,
\]

a zeta-zero mode has phase

\[
e^{i\gamma t}.
\]

The sign changes of \(\Delta\) are properties of the aggregate real error term; no individual zero is identified here as the cause of a particular sign change.

## 4. Exact sampling of zero phases on dyadic prime fibres

For every prime \(p\), write its unique On-Primes address

\[
p+1=a_p2^{k_p},
\qquad a_p\ \text{odd},
\]

and define the already established defect

\[
\delta_p=\log\left(1+\frac1p\right).
\]

Then

\[
\log p
=
\log a_p+k_p\log2-\delta_p.
\]

Hence for every real \(\gamma\),

\[
\boxed{
e^{i\gamma\log p}
=
e^{i\gamma\log a_p}
e^{ik_p\gamma\log2}
e^{-i\gamma\delta_p}.
}
\]

More generally, for every complex \(\rho\),

\[
p^\rho
=
a_p^\rho\,2^{k_p\rho}\,e^{-\rho\delta_p}.
\]

This is an exact coordinate factorisation. If \(\rho=\beta+i\gamma\) is a zeta zero, the per-fibre-index phase increment is

\[
\boxed{
\omega_\gamma=\gamma\log2\pmod{2\pi}.
}
\]

Thus the dyadic fibre samples each zero mode as a rigid phase rotation in \(k\), with the prime-vs-\(p+1\) correction isolated in the exact defect factor \(e^{-i\gamma\delta_p}\).

This statement is a re-expression of the mode in dyadic coordinates; by itself it is not a new zero theorem.

## 5. Hilbert shift and the exact Weyl phase relation

On the fibre-index space \(\ell^2(\mathbb N_0)\), define

\[
S|k\rangle=|k+1\rangle,
\qquad
D_\omega|k\rangle=e^{ik\omega}|k\rangle.
\]

Then

\[
\boxed{
D_\omega S=e^{i\omega}S D_\omega.
}
\]

For a zeta-zero ordinate \(\gamma\), choose

\[
\omega=\omega_\gamma=\gamma\log2\pmod{2\pi}.
\]

The Hilbert-Hotel shift and the zero-phase progression are therefore joined by an exact Weyl-type commutation relation on the dyadic fibre index.

This is the clean operator statement behind the phrase "phase spectrum on a countable shift".

## 6. Accelerated odd Collatz inverse fibres

For odd \(n\), define the accelerated odd Collatz map

\[
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
\]

Fix an odd target \(m\).

If \(3\mid m\), there is no odd \(n\) with \(U(n)=m\).

If \(3\nmid m\), every odd one-step predecessor is exactly

\[
B_a(m)=\frac{2^a m-1}{3},
\]

where \(a\ge1\) satisfies

\[
2^a m\equiv1\pmod3.
\]

Since \(2\equiv-1\pmod3\), the admissible exponent parity is fixed:

\[
m\equiv1\pmod3
\Rightarrow
a=2,4,6,\ldots,
\]

\[
m\equiv2\pmod3
\Rightarrow
a=1,3,5,\ldots.
\]

For every admissible \(a\),

\[
3B_a(m)+1=2^a m,
\]

and because \(m\) is odd,

\[
\nu_2(3B_a(m)+1)=a,
\qquad
U(B_a(m))=m.
\]

Thus for every odd \(m\) not divisible by \(3\), the accelerated odd Collatz map has a countably infinite one-step reverse fibre.

Successive admissible exponents differ by two, and therefore

\[
\boxed{
B_{a+2}(m)=4B_a(m)+1.
}
\]

Define

\[
R(x)=4x+1=F_{4,1/3}(x).
\]

Then

\[
R(x)+\frac13
=
4\left(x+\frac13\right).
\]

The shifted Collatz reverse coordinate

\[
\tau_C(x)=\log\left(x+\frac13\right)
\]

therefore obeys

\[
\boxed{
\tau_C(Rx)-\tau_C(x)=\log4=2\log2.
}
\]

The reverse Collatz fibre is thus another exact affine-dilation lattice, centred at \(-1/3\), advancing by two units of the same base dyadic clock \(\log2\).

## 7. The common dyadic phase clock

The two exact affine sectors are:

\[
\text{On-Primes:}\quad
x+1\mapsto2(x+1),
\qquad
\Delta\tau_P=\log2,
\]

\[
\text{Collatz reverse:}\quad
x+\frac13\mapsto4\left(x+\frac13\right),
\qquad
\Delta\tau_C=2\log2.
\]

A spectral phase \(e^{i\gamma\tau}\) therefore advances by

\[
e^{i\omega_\gamma},
\qquad
\omega_\gamma=\gamma\log2
\]

on one On-Primes fibre step, and by

\[
e^{2i\omega_\gamma}
\]

on one same-target Collatz reverse-fibre step.

This is an exact shared clock. It is not evidence that Collatz dynamics controls zeta zeros or vice versa.

## 8. Euler sign phase as a representation, not a mechanism

Away from zeros of \(\Delta(x)\), define

\[
\theta_\Delta(x)=
\begin{cases}
0,&\Delta(x)>0,\\
\pi,&\Delta(x)<0.
\end{cases}
\]

Then

\[
\operatorname{sgn}\Delta(x)=e^{i\theta_\Delta(x)}.
\]

A sign reversal is therefore represented by a phase change of \(\pi\) modulo \(2\pi\). This is an exact two-state phase encoding of sign. It must not be confused with a derivation of Littlewood's theorem from Euler's identity.

## 9. Local claim ledger

| ID | Statement | Status |
|---|---|---|
| OP-X001 | \(F_{q,c}\) is conjugate to multiplication by \(q\) through \(h_c(x)=x+c\). | PROVED |
| OP-X002 | \(T(x)=2x+1=F_{2,1}\) gives \(\Delta\tau_P=\log2\). | PROVED |
| OP-X003 | Prime infinitude gives an isometry from \(\ell^2(\mathbb N)\) onto the prime-labelled subspace. | STANDARD + EXACT CONSTRUCTION |
| OP-X004 | \(\pi(x)-\operatorname{li}(x)\) changes sign infinitely often. | STANDARD |
| OP-X005 | A zero-mode phase is \(e^{i\gamma\log x}\) in log-coordinate. | EXACT ALGEBRA + STANDARD EXPLICIT-FORMULA CONTEXT |
| OP-X006 | Dyadic prime addressing gives the exact phase factorisation with increment \(\omega_\gamma=\gamma\log2\). | PROVED |
| OP-X007 | \(D_\omega S=e^{i\omega}SD_\omega\). | PROVED |
| OP-X008 | Accelerated odd Collatz reverse fibres are empty for \(3\mid m\) and countably infinite for odd \(3\nmid m\), with \(B_{a+2}=4B_a+1\). | PROVED |
| OP-X009 | The Collatz reverse log-coordinate advances by \(2\log2\). | PROVED |
| OP-X010 | Skewes/Littlewood sign phase can be encoded as \(0/\pi\). | DEFINITION |
| OP-O004 | Zero-mode phase increments on dyadic fibres may expose a nontrivial spectral statistic beyond reparametrisation. | OPEN |
| OP-O005 | Comparing \(\omega_\gamma\) and \(2\omega_\gamma\) against prime-mask and Collatz-fibre observables may reveal or falsify shared phase coherence. | OPEN |

## 10. Falsifiable next tests

1. For a finite list of verified zeta-zero ordinates \(\gamma_j\), compute
   \[
   \omega_j=\gamma_j\log2\bmod2\pi
   \]
   and test uniformity, clustering, rational near-resonance, and pair correlations.

2. Sample the phase factors on the existing prime masks
   \[
   M_a(k)=1_{\mathbb P}(a2^k-1)
   \]
   and preregister statistics before looking for correlations.

3. On accelerated Collatz reverse fibres, compare the doubled phase
   \[
   2\omega_j
   \]
   against branch-index observables. A null result is a valid outcome.

4. Keep the Skewes/Littlewood sector analytic: any claimed relation to sign reversal must be tested against a smoothed explicit formula or another continuation-safe formulation. No illegal Euler-product substitution in the critical strip is permitted.

## 11. Firewall

The exact shared object established here is the **dyadic affine/log-phase clock**.

The following are **not** established:

- RH;
- the Collatz conjecture;
- a formula for the first Skewes crossing;
- a causal equivalence between prime error oscillations and Collatz dynamics;
- a new theorem on the distribution of zeta zeros;
- a proof that \(\omega_\gamma\) has a non-random or resonant distribution.

Those remain separate open questions.
