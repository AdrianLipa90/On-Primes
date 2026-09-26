# Montgomery–Dyson Forced Phase Spectroscopy v0.1

Status: **FORCED_PREDICTION_CORE / ARPL_CROSSWALK_EXACT / ZETA_OCCUPANCY_BINDING_OPEN**

Date: 2026-09-26

Dependencies:
- current ARPL branch: \`feat/arithmetic-relational-phase-law-v0.1\`
- Infinities forced-prediction theorem:
  \`formalize/hardy-car-sine-kernel-forced-prediction-v0.1-20260926\`,
  dependency head \`7008a9121d878674a7190d0966faa727f9eacb55\`
- Secret-of-a-Half Yoshida/Fourier compatibility theorem:
  \`formalize/montgomery-dyson-hard-car-binding-v0.1-20260926\`

## 1. Existing On-Primes phase layer

ARPL already represents integer separations by additive characters

\[
\chi_{q,a}(\Delta)=e^{2\pi ia\Delta/q}
\]

and proves

\[
\chi_{q,a}(y)\overline{\chi_{q,a}(x)}
=
\chi_{q,a}(y-x).
\]

The complete prime-power residue signature is injective on integers, and the canonical global phase space is

\[
\widehat{\mathbb Z}\cong\prod_p\mathbb Z_p,
\qquad
\widehat{\widehat{\mathbb Z}}\cong\mathbb Q/\mathbb Z.
\]

Thus prime gaps already have an exact phase representation before any spectral-statistics assumption is introduced.

## 2. Spectroscopy coordinate

For any ordered locally unfolded spectral sequence \(u_j\), define

\[
\Phi_j=2\pi u_j.
\]

The two-point separation coordinate is

\[
\Delta\Phi
=
2\pi(u_i-u_j).
\]

This is a coordinate map. It does not assume a GUE law.

## 3. Forced projector law

The upstream Hardy–CAR theorem begins with the canonical consecutive-mode projector and filled CAR state, not with Montgomery/GUE. For \(N\) consecutive modes it gives

\[
\boxed{
g_{2,N}(s)
=
1-
\left[
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right]^2.
}
\]

Taking the microscopic unit-density limit,

\[
\boxed{
g_2(s)
=
1-
\left(
\frac{\sin\pi s}{\pi s}
\right)^2.
}
\]

With \(\Delta\Phi=2\pi s\),

\[
\boxed{
g_2(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2.
}
\]

The short-range law is

\[
g_2(\Delta\Phi)
=
\frac{(\Delta\Phi)^2}{12}
+
O((\Delta\Phi)^4).
\]

GUE, random matrices, zeta zeros and Montgomery's target function are not inputs to this derivation.

## 4. Compatibility with the SOH/Yoshida Fourier carrier

Secret-of-a-Half already uses the normalized modes

\[
e_n^{(a)}(x)
=
(2a)^{-1/2}e^{\pi i n x/a},
\qquad |n|\le N.
\]

Their projector is

\[
K_{N,a}(x,y)
=
\frac{1}{2a}
\frac{
\sin((2N+1)\pi(x-y)/(2a))
}{
\sin(\pi(x-y)/(2a))
}.
\]

After unfolding by its diagonal density \((2N+1)/(2a)\), the support scale \(a\) cancels and the same sinc kernel is forced.

Therefore the local phase-spectroscopy kernel is independent of whether it is written in the one-sided Hardy consecutive-mode basis or the symmetric SOH/Yoshida Fourier basis.

## 5. Prime-side phase channels remain distinct

The ARPL gap state and the zero-side unfolded spectral phase are different typed objects.

Prime side:

\[
h
\mapsto
(h\bmod p^j)_{p,j}
\mapsto
\chi_{p^j,a}(h),
\]

with Hardy–Littlewood singular-series factors already represented as modular phase observables.

Explicit-formula side:

\[
p^m
\mapsto
\omega_{p,m}=m\log p.
\]

Zero-spectrum side:

\[
\gamma_j
\mapsto
u_j
\mapsto
\Phi_j.
\]

The phase-spectroscopy programme therefore has three typed coordinates:

\[
\boxed{
\mathcal S=
\left(
\text{ARPL modular gap phase},
\text{prime-power log frequency},
\text{unfolded zero phase}
\right).
}
\]

They are related by established explicit-formula and correlation machinery only where the corresponding theorem has actually been supplied.

## 6. Status of Montgomery–Dyson

The function

\[
1-\left(\frac{\sin\pi s}{\pi s}\right)^2
\]

is not a fitted curve in this branch. Its internal status is

\[
\boxed{
\texttt{DERIVED\_IN\_FRAMEWORK / FORCED\_PREDICTION}
}
\]

for the declared consecutive-mode projector + CAR sector.

The external statement that actual Riemann-zero ordinates instantiate that sector remains the separate binding gate SOH-MD001.

Thus:

\[
\boxed{
\text{projector/CAR cage}
\Longrightarrow
\text{Montgomery–Dyson functional form}
}
\]

is closed internally, while

\[
\boxed{
\text{actual zeta zeros}
\Longrightarrow
\text{that projector/CAR occupancy}
}
\]

is still open.

## 7. Twin-prime channel

ARPL already proves that prime-pair and two-twin-pair singular factors are exact observables of modular gap phases. The \(h=2\) prime-pair channel is therefore a distinguished ARPL phase channel.

This does not make the twin-prime conjecture a corollary of the forced sine kernel. The bridge between zero correlations and prime-pair correlations must retain the standard explicit-formula/Hardy–Littlewood hypotheses and their analytic limits.

The correct relation is structural:

\[
\text{prime modular phase}
\leftrightarrow
\text{prime-pair correlation}
\leftrightarrow
\text{zero correlation}
\leftrightarrow
\text{forced projector kernel},
\]

with each arrow separately typed and audited.

## 8. No-target-leakage rule

A future zeta-specific proof must not:
- use the Montgomery pair-correlation conjecture as an assumption;
- choose a projector because it returns sinc;
- fit the local kernel to Odlyzko zero data and promote the fitted object;
- assume GUE universality.

It must derive the zeta spectral occupancy/operator map independently.

## 9. Compact result

The current On-Primes framework now contains an exact phase representation of prime gaps and imports a no-target-leakage derivation of the sine-kernel two-point law from the shared operator cage. This promotes the **phase-correlation core** from candidate to forced prediction while leaving the zeta-process and domain bindings explicit and open.


## 10. External restricted-support checkpoint

Classical analytic number theory already supplies a restricted test-function checkpoint for the same functional form: Montgomery's pair-correlation theorem matches the GUE/sine-kernel two-point statistic on its admissible Fourier-support class under the theorem's stated hypotheses, and Rudnick--Sarnak establish restricted-support higher correlation results for principal L-functions.

This is tagged **EXTERNAL_STANDARD / PARTIAL_BINDING**. It is not an input to the forced-prediction derivation and must not be used circularly in any RH argument. The full zeta local occupancy/DPP identification remains SOH-MD001B.
