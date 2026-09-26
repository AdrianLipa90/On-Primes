# LCM–von Mangoldt Commensurate Phase Clock v0.1

Status: **EXACT_FINITE_ARITHMETIC_CLOCK / EXACT_LOW-BLOCK_PHASE_CLOSURE**

Date: 2026-09-26

Parents:
- \`proofs/FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1.md\`
- \`proofs/SHIFTED_VON_MANGOLDT_CRT_PHASE_V0_1.md\`
- \`SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1.md\`

## 1. Canonical common clock

For an integer cutoff \(R\ge1\), define

\[
\boxed{
L_R=\operatorname{lcm}(1,2,\ldots,R).
}
\]

Every CRT compatibility modulus appearing in the low-divisor block has the form

\[
g=\gcd(d,e),
\qquad
d,e\le R,
\]

and therefore

\[
g\le R
\quad\Longrightarrow\quad
g\mid L_R.
\]

Thus \(L_R\) is a canonical common period for every low-divisor phase-lock channel.

## 2. Exact von Mangoldt identity

The prime factorization of \(L_R\) contains, for each prime \(p\le R\), the highest power

\[
p^{\lfloor\log_pR\rfloor}.
\]

Hence

\[
\log L_R
=
\sum_{p\le R}
\lfloor\log_pR\rfloor\log p.
\]

But

\[
\lfloor\log_pR\rfloor
=
\#\{m\ge1:p^m\le R\}.
\]

Therefore

\[
\log L_R
=
\sum_{p^m\le R}\log p
=
\sum_{n\le R}\Lambda(n).
\]

Thus

\[
\boxed{
\log\operatorname{lcm}(1,\ldots,R)
=
\psi(R).
}
\]

Equivalently,

\[
\boxed{
L_R=e^{\psi(R)}.
}
\]

This is an exact identity, not an asymptotic.

## 3. Exact Fejér closure on the common clock

Let

\[
L=H+1
\]

and suppose

\[
\boxed{
L_R\mid L.
}
\]

For every \(g\le R\), we then have

\[
L\bmod g=0.
\]

The exact Fejér gate average from the parent theorem is

\[
Q_H(g)
=
\frac1g+
\frac{r_g(g-r_g)}{gL^2},
\qquad
r_g=L\bmod g.
\]

Hence all edge corrections vanish simultaneously:

\[
\boxed{
Q_H(g)=\frac1g
\qquad
(1\le g\le R).
}
\]

Thus the entire low-divisor phase block completes an exact common clock.

## 4. Exact low-block factorization

The Fejér-averaged low-divisor density coefficient is

\[
\overline M_{H,R}
=
\sum_{d,e\le R}
\frac{
\mu(d)\mu(e)\log d\log e
}{
\operatorname{lcm}(d,e)
}
Q_H(\gcd(d,e)).
\]

On a commensurate clock \(L_R\mid H+1\),

\[
Q_H(\gcd(d,e))
=
\frac1{\gcd(d,e)}.
\]

Using

\[
\gcd(d,e)\operatorname{lcm}(d,e)=de,
\]

we get

\[
\overline M_{H,R}
=
\sum_{d,e\le R}
\frac{
\mu(d)\mu(e)\log d\log e
}{
de
}.
\]

Therefore

\[
\boxed{
\overline M_{H,R}
=
\left(
\sum_{d\le R}
\frac{\mu(d)\log d}{d}
\right)^2
}
\]

**exactly at finite \(R\)**.

There is no Fejér edge correction.

## 5. PNT limit

The classical PNT-related Möbius identity gives

\[
\sum_{d\le R}
\frac{\mu(d)\log d}{d}
\to -1.
\]

Hence on the canonical clock sequence

\[
H_R+1=L_R,
\]

or on any integer multiple thereof,

\[
\boxed{
\overline M_{H_R,R}\to1.
}
\]

The finite factorization is exact; only the limiting value uses the standard PNT input.

## 6. Prime-power interpretation of the clock length

Since

\[
\psi(R)=\sum_{p^m\le R}\log p,
\]

the logarithm of the exact common period is the cumulative sum of the same prime-power von Mangoldt weights that appear in the spectral phase bank.

Thus the low-divisor modular clock and the prime-power spectral bank are linked by the exact identity

\[
\boxed{
\text{common period}
=
\exp\!\left(
\sum_{p^m\le R}\log p
\right).
}
\]

This is a structural arithmetic identity. It does not by itself prove any prime-pair or zeta-zero statistical law.

## 7. Scale cost

The prime number theorem also gives

\[
\psi(R)\sim R,
\]

so

\[
\log L_R\sim R.
\]

Therefore an exact common clock for all moduli up to \(R\) has exponential length in \(R\):

\[
L_R=e^{(1+o(1))R}.
\]

Conversely, an observation window of polynomial size \(H=X^\alpha\) can close all low-divisor phase channels exactly only up to a scale

\[
R\asymp\log H\asymp\log X
\]

if one insists on the exact LCM clock.

This is not a defect: the previous Fejér theorem allows approximate closure for much larger \(R\), while the present theorem identifies the exact finite commensurate subsequence.

## 8. Compact theorem

### Theorem — LCM–von Mangoldt common clock

For

\[
L_R=\operatorname{lcm}(1,\ldots,R),
\]

one has exactly

\[
\boxed{\log L_R=\psi(R).}
\]

If \(H+1\) is a multiple of \(L_R\), then every low-divisor CRT phase gate with \(d,e\le R\) completes an exact Fejér period and

\[
\boxed{
\overline M_{H,R}
=
\left(
\sum_{d\le R}
\frac{\mu(d)\log d}{d}
\right)^2.
}
\]

Q.E.D.
