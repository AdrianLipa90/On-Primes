# ARPL Global B2 Phase Spectrum v0.1

Status: exact mean-square convergence, finite global variance, and Besicovitch pure-point phase spectrum for the logarithmic dyadic singular-series orbit.

## 1. Dynamic logarithmic field

Fix an admissible separation

\[
h\ge6,\qquad 6\mid h.
\]

From the instantaneous factorization,

\[
\log\mathfrak S(H_{2^rh})
=
\log\left(\frac{27}{2}C_*Z(h)\right)
+
\sum_{p\ge5} w_p E_p(r;h),
\]

where

\[
w_p
=
\log\frac{p-3}{p-4}
\]

and

\[
E_p(r;h)
=
\mathbf1_{\{2^rh\equiv\pm2\pmod p\}}.
\]

For fixed \(r\), only finitely many terms are nonzero because every active \(p\) divides \(4^rh^2-4\).

Let

\[
\delta_p(h)=M(E_p)
\]

be the exact local hit density already established, and define the centered field

\[
\boxed{
Y_h(r)
=
\log\mathfrak S(H_{2^rh})-\mathcal L(h)
=
\sum_{p\ge5}
w_p\big(E_p(r;h)-\delta_p(h)\big).
}
\]

## 2. Discrete Besicovitch seminorm

For a sequence \(f:\mathbb Z_{\ge0}\to\mathbb C\), define

\[
\|f\|_{B^2}^2
=
\limsup_{T\to\infty}
\frac1T\sum_{r=0}^{T-1}|f(r)|^2.
\]

Every finite prime truncation

\[
Y_{h,P}(r)
=
\sum_{5\le p\le P}
w_p(E_p(r;h)-\delta_p(h))
\]

is periodic and hence a finite trigonometric polynomial on the discrete time variable.

## 3. Single and joint hit-count bounds

For \(p\nmid h\), the channel has period

\[
d_p=\operatorname{ord}_p(2)
\]

and at most two hit residues per period. Therefore

\[
N_p(T)
=
\#\{0\le r<T:E_p(r;h)=1\}
\le
2\left(\frac{T}{d_p}+1\right).
\]

For distinct \(p,q\), simultaneous hits lie in at most four residue classes modulo

\[
L_{pq}=\operatorname{lcm}(d_p,d_q),
\]

so

\[
N_{pq}(T)
\le
4\left(\frac{T}{L_{pq}}+1\right).
\]

Channels with \(p\mid h\) contribute zero dynamic hits.

## 4. Square-mean tail theorem — OP-D075

Define the nonnegative dynamic tail

\[
A_P(r)
=
\sum_{p>P}w_pE_p(r;h).
\]

At any finite time horizon only primes dividing

\[
M_T(h)
=
\prod_{r=0}^{T-1}(4^rh^2-4)
\]

can occur, so all finite-\(T\) expansions below contain only finitely many terms.

Expanding the square and using the hit-count bounds gives

\[
\begin{aligned}
\frac1T\sum_{r<T}A_P(r)^2
\le{}&
2\sum_{p>P}\frac{w_p^2}{d_p}
+
8\sum_{P<p<q}
\frac{w_pw_q}{L_{pq}}\\
&+
O\left(
\frac1T
\left[
\sum_{p\mid M_T(h)}w_p
\right]^2
\right).
\end{aligned}
\]

Now

\[
w_p\ll\frac1p,
\qquad
d_p\ge\log_2(p+1).
\]

The single-channel series converges.

For \(p<q\),

\[
L_{pq}\ge d_q\gg\log q,
\]

so

\[
\sum_{p<q}\frac{w_pw_q}{L_{pq}}
\ll
\sum_q
\frac1{q\log q}
\sum_{p<q}\frac1p.
\]

Using the reciprocal-prime Mertens bound,

\[
\sum_{p<q}\frac1p=O(\log\log q),
\]

and the standard upper bound \(\pi(x)\ll x/\log x\), the last prime sum converges.

For the endpoint term,

\[
\sum_{p\mid M_T(h)}w_p
\ll
\log\log |M_T(h)|.
\]

Since

\[
\log |M_T(h)|=O_h(T^2),
\]

the endpoint contribution is

\[
O_h\left(\frac{(\log T)^2}{T}\right)\to0.
\]

Consequently

\[
\boxed{
\lim_{P\to\infty}
\limsup_{T\to\infty}
\frac1T\sum_{r<T}A_P(r)^2
=
0.
}
\]

The centered tail is no larger in variance, so

\[
\boxed{
\|Y_h-Y_{h,P}\|_{B^2}\to0.
}
\]

Thus the actual logarithmic phase field is a \(B^2\)-mean-square limit of periodic sequences.

## 5. Exact pair densities

For \(p,q\ge5\), define

\[
\delta_{pq}(h)
=
M(E_pE_q).
\]

If either local hit set is empty, \(\delta_{pq}=0\).

Otherwise let \(H_p\subset\mathbb Z/d_p\mathbb Z\) and
\(H_q\subset\mathbb Z/d_q\mathbb Z\) be the one- or two-point hit sets. By CRT compatibility,

\[
\boxed{
\delta_{pq}(h)
=
\frac{
\#\{(a,b)\in H_p\times H_q:
a\equiv b\pmod{\gcd(d_p,d_q)}
\}
}{
\operatorname{lcm}(d_p,d_q)
}.
}
\]

In particular,

\[
0\le\delta_{pq}(h)\le\frac4{L_{pq}}.
\]

## 6. Global variance theorem — OP-D076

The finite-truncation variance is

\[
\begin{aligned}
V_P(h)
={}&
\sum_{5\le p\le P}
w_p^2\delta_p(1-\delta_p)\\
&+
2\sum_{5\le p<q\le P}
w_pw_q
\left(
\delta_{pq}-\delta_p\delta_q
\right).
\end{aligned}
\]

The diagonal series converges absolutely because

\[
\delta_p\le\frac2{d_p}.
\]

For the pair covariance,

\[
|\delta_{pq}-\delta_p\delta_q|
\le
\frac4{L_{pq}}
+
\frac4{d_pd_q}
\le
\frac8{L_{pq}},
\]

and the pair series converges by the estimate in OP-D075.

Therefore

\[
\boxed{
\mathcal V(h)
=
\lim_{P\to\infty}V_P(h)
}
\]

exists, is finite and nonnegative, with the absolutely convergent representation

\[
\boxed{
\mathcal V(h)
=
\sum_{p\ge5}
w_p^2\delta_p(1-\delta_p)
+
2\sum_{p<q}
w_pw_q
(\delta_{pq}-\delta_p\delta_q).
}
\]

Mean-square convergence also gives

\[
\boxed{
\mathcal V(h)
=
\lim_{T\to\infty}
\frac1T\sum_{r<T}|Y_h(r)|^2.
}
\]

## 7. Rational Fourier--Bohr frequencies

For a single channel define normalized local Fourier coefficients

\[
\widehat E_{p,h}(m)
=
\frac1{d_p}
\sum_{r=0}^{d_p-1}
E_p(r;h)e^{-2\pi i mr/d_p}.
\]

For \(m\ne0\),

\[
|\widehat E_{p,h}(m)|
\le
\frac2{d_p}.
\]

Every local frequency is rational:

\[
\lambda=\frac{m}{d_p}\pmod1.
\]

For fixed \(\lambda\in\mathbb Q/\mathbb Z\), define

\[
\boxed{
a_h(\lambda)
=
\sum_{\substack{p\ge5,\ m\\m/d_p=\lambda}}
w_p\widehat E_{p,h}(m).
}
\]

This sum is absolutely convergent because

\[
\sum_p\frac{2w_p}{d_p}
\ll
\sum_p\frac1{p\log p}
<\infty.
\]

## 8. Global phase-spectrum theorem — OP-D077

Since \(Y_h\) is a \(B^2\) limit of periodic trigonometric polynomials, it is a discrete Besicovitch-\(B^2\) almost-periodic sequence.

Its Fourier--Bohr spectrum is countable and lies in

\[
\boxed{
\Lambda_h
\subset
\bigcup_{p\ge5}
\left\{
\frac{m}{d_p}\pmod1:
1\le m<d_p
\right\}
\subset
\mathbb Q/\mathbb Z.
}
\]

The spectrum is therefore pure point and entirely rational in dyadic time.

By the Besicovitch Parseval theorem,

\[
\boxed{
\mathcal V(h)
=
\sum_{\lambda\in\Lambda_h}
|a_h(\lambda)|^2
<\infty.
}
\]

This is the exact global logarithmic phase-power spectrum of the dyadic two-twin-pair singular-series orbit.

## 9. Autocorrelation / spectrum duality — OP-D078

Define the lag-\(k\) autocorrelation of the centered logarithmic field:

\[
C_h(k)
=
\lim_{T\to\infty}
\frac1T
\sum_{r<T}
Y_h(r+k)\overline{Y_h(r)}.
\]

The limit exists for every integer \(k\), and the pure-point spectral representation is

\[
\boxed{
C_h(k)
=
\sum_{\lambda\in\Lambda_h}
|a_h(\lambda)|^2e^{2\pi i\lambda k}.
}
\]

Because

\[
\sum_\lambda|a_h(\lambda)|^2=\mathcal V(h)<\infty,
\]

this power-spectrum series is absolutely convergent.

At \(k=0\),

\[
C_h(0)=\mathcal V(h).
\]

Thus ARPL supplies an exact global autocorrelation--phase-spectrum pair for the logarithmic singular-series dynamics.

## 10. Density control of fluctuations — OP-D079

For any \(A>0\), Chebyshev's inequality applied to the Cesaro variance gives

\[
\boxed{
\limsup_{T\to\infty}
\frac1T
\#\{0\le r<T:|Y_h(r)|\ge A\}
\le
\frac{\mathcal V(h)}{A^2}.
}
\]

Hence atypically large logarithmic phase excursions have quantitatively controlled upper density.

This is a density statement, not a pointwise bound.

## 11. Dyadic orbit invariance

Replacing \(h\) by \(2^kh\) rotates every local periodic channel. Rotation changes local Fourier phases but not:

- hit densities;
- joint densities;
- variance;
- power at each global frequency after the corresponding time-origin shift.

Therefore

\[
\boxed{
\mathcal V(2^kh)=\mathcal V(h).
}
\]

The spectral amplitudes transform only by the deterministic time-translation phase associated with the orbit shift; the power spectrum is invariant.

## 12. Numerical illustration for h=6

Finite prime-channel variance truncations are:

\[
\begin{array}{c|c}
P & V_P(6)\\
\hline
50 & 0.1285264018669692\\
100 & 0.1285674436914741\\
200 & 0.1287226802226668\\
500 & 0.1287625553593365\\
1000 & 0.1287689080144238
\end{array}
\]

For small finite supports, direct common-period variance equals the aggregated rational-frequency Parseval power to numerical precision.

These values illustrate the theorem and are not used to prove convergence.

## 13. Prior-art boundary

Besicovitch almost-periodic \(B^2\) spaces, Fourier--Bohr coefficients, harmonic synthesis, and Parseval identities are standard.

The new project-specific object is the proof that this particular ARPL logarithmic singular-series orbit lies in the discrete \(B^2\) closure, with explicit number-theoretic frequencies \(m/\operatorname{ord}_p(2)\), exact hit-density coefficients, and an absolutely controlled prime-channel tail.

Literature novelty for this specialization remains NOT ESTABLISHED.

## 14. No-go

This theorem does not prove:

- convergence of the arithmetic mean of \(\mathfrak S(H_{2^rh})\);
- the Hardy--Littlewood prime-quadruplet asymptotic;
- infinitely many twin primes;
- a zeta-zero spectral equivalence;
- RH.
