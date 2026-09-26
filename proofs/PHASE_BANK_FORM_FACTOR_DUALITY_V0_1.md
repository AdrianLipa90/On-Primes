# Prime-Power Phase Bank ↔ Spectral Form Factor Duality v0.1

Status: **EXACT_FINITE_IDENTITY / EXACT_FROZEN_UNFOLDING_MAP / MONTGOMERY_SCALING_BINDING_OPEN**

Date: 2026-09-26

Parents:
- \`SPECTRAL_VON_MANGOLDT_PHASE_BANK_V0_1.md\`
- \`proofs/MONTGOMERY_DYSON_FORCED_PHASE_SPECTROSCOPY_V0_1.md\`
- Infinities \`TIR_HARDY_CAR_SPECTRAL_FORM_FACTOR_V0_1\`

## 1. Finite phase bank

Let

\[
\Gamma=\{\gamma_1,\ldots,\gamma_N\}
\]

be any finite real spectral sample. No zeta assumption is needed for the following identity.

For any \(q>0\), define

\[
R_q
=
\frac1N
\sum_{j=1}^N
q^{i\gamma_j}
=
\frac1N
\sum_{j=1}^N
e^{i\gamma_j\log q}.
\]

Then

\[
\boxed{
N|R_q|^2
=
\frac1N
\sum_{j,k=1}^N
e^{i(\gamma_j-\gamma_k)\log q}.
}
\]

This is the finite Wiener–Khintchine identity for the phase bank.

Thus a one-frequency phase-bank amplitude and the pair-difference Fourier power are the same finite observable viewed before and after taking modulus square.

## 2. Frozen-height unfolding

Fix a reference height \(T>2\pi\). The derivative of the leading smooth Riemann–von Mangoldt counting term is

\[
\nu_T
=
\frac1{2\pi}
\log\frac{T}{2\pi}.
\]

Define the frozen local unfolded coordinate

\[
u_{T,j}
=
\nu_T(\gamma_j-T).
\]

For every \(q>0\), define

\[
\boxed{
\tau_q(T)
=
\frac{\log q}{\log(T/2\pi)}.
}
\]

Since

\[
2\pi\tau_q(T)\nu_T=\log q,
\]

we have

\[
q^{i\gamma_j}
=
q^{iT}
e^{2\pi i\tau_q(T)u_{T,j}}.
\]

The factor \(q^{iT}\) is global and disappears from the modulus square. Hence

\[
\boxed{
N|R_q|^2
=
\frac1N
\left|
\sum_{j=1}^N
e^{2\pi i\tau_q(T)u_{T,j}}
\right|^2.
}
\]

Define the finite frozen-unfolding form factor

\[
K_{\Gamma,T}(\tau)
=
\frac1N
\left|
\sum_{j=1}^N
e^{2\pi i\tau u_{T,j}}
\right|^2.
\]

Then the exact frequency map is

\[
\boxed{
K_{\Gamma,T}\!\left(\tau_q(T)\right)
=
N|R_q|^2.
}
\]

This is an exact finite identity, not an analogy.

## 3. Prime-power sampling frequencies

For a prime power

\[
q=p^m,
\]

the sampled unfolded frequency is

\[
\boxed{
\tau_{p^m}(T)
=
\frac{m\log p}{\log(T/2\pi)}.
}
\]

The dyadic harmonic ladder is therefore

\[
\boxed{
\tau_{2^m}(T)
=
\frac{m\log2}{\log(T/2\pi)}.
}
\]

Thus the existing von Mangoldt phase bank samples the finite form-factor power on a logarithmic prime-power frequency lattice.

## 4. Relation to the forced ramp

The shared Hardy–CAR projector theorem independently forces

\[
S(\tau)=\min(|\tau|,1)
\]

for its normalized microscopic form factor.

Therefore, if a spectral sample is independently shown to instantiate the corresponding local projector/CAR sector, the prime-power phase-bank frequencies have the forced target

\[
\boxed{
S\!\left(\tau_{p^m}(T)\right)
=
\min\!\left(
\frac{m\log p}{\log(T/2\pi)},
1
\right).
}
\]

This is a **conditional domain application** of the forced projector theorem. The frequency map itself is unconditional finite algebra.

## 5. Critical firewall: fixed-q Landau is not the universal ramp

Landau's classical fixed-\(q\) formula and the universal Montgomery/GUE scaling probe different asymptotic regimes.

For fixed \(q\),

\[
\tau_q(T)
=
\frac{\log q}{\log(T/2\pi)}
\longrightarrow0
\qquad(T\to\infty).
\]

Thus a fixed prime power moves toward the origin of the unfolded form-factor axis.

To probe a nonzero fixed frequency \(\tau\), one needs

\[
\log q(T)
\sim
\tau\log(T/2\pi),
\]

i.e.

\[
\boxed{
q(T)\asymp (T/2\pi)^\tau.
}
\]

Montgomery's classical form-factor variable uses the equivalent leading scaling \(x=T^\alpha\), with the distinction between \(\log T\) and \(\log(T/2\pi)\) asymptotically negligible at relative order \(1/\log T\).

Therefore:

- fixed-\(q\) Landau response = arithmetic spectral line near \(\tau=0\);
- \(q(T)\)-scaled phase response = the regime relevant to a fixed nonzero form-factor frequency;
- smoothing/windowing is required before identifying the global zeta observable with the universal local ramp.

No claim may infer the full ramp from fixed-\(q\) Landau asymptotics alone.

## 6. Pair-correlation duality

For any finite unfolded sample,

\[
K_{\Gamma,T}(\tau)
=
\frac1N
\sum_{j,k}
e^{2\pi i\tau(u_{T,j}-u_{T,k})}.
\]

Thus the form factor is literally the Fourier transform of the empirical pair-difference measure.

Consequently the two forced projector statements

\[
g_2(s)
=
1-\left(\frac{\sin\pi s}{\pi s}\right)^2
\]

and

\[
S(\tau)=\min(|\tau|,1)
\]

are Fourier-dual, while the prime-power phase bank gives a distinguished arithmetic sampling lattice \(\tau_q(T)\) on the form-factor side.

## 7. Zeta-specific status

When \(\gamma_j\) are actual zeta-zero ordinates:

- the finite identity
  \[
  K_{\Gamma,T}(\tau_q)=N|R_q|^2
  \]
  remains exact;
- Landau supplies standard arithmetic information about phase sums in its own asymptotic regime;
- classical Montgomery theory supplies restricted-support correlation information under its stated hypotheses;
- the full local quasi-free/CAR projector occupancy required to inherit the complete forced ramp remains open.

This is precisely the remaining SOH-MD001B-type gate.

## 8. Compact theorem

### Theorem — prime-power phase/form-factor frequency map

For any finite real sample \(\Gamma=\{\gamma_j\}_{j=1}^N\), reference height \(T>2\pi\), and \(q>0\), let

\[
\nu_T=\frac1{2\pi}\log\frac{T}{2\pi},
\quad
u_{T,j}=\nu_T(\gamma_j-T),
\quad
\tau_q=\frac{\log q}{\log(T/2\pi)}.
\]

Then

\[
\boxed{
\frac1N
\left|
\sum_j e^{2\pi i\tau_q u_{T,j}}
\right|^2
=
N
\left|
\frac1N
\sum_j q^{i\gamma_j}
\right|^2.
}
\]

For \(q=p^m\), this samples the finite form factor at

\[
\boxed{
\tau_{p^m}
=
\frac{m\log p}{\log(T/2\pi)}.
}
\]

The identity is exact. Any inference from this sampled power to the universal forced ramp requires an independent local spectral-process binding and the appropriate scaling/window regime. Q.E.D.
