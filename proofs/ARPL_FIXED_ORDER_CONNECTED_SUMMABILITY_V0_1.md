# ARPL Fixed-Order Connected Summability v0.1

Status: exact finite Fourier bounds + absolute convergence of every fixed connected order \(n\ge2\).

## 1. Centered local observables

For a prime \(p\ge5\), fixed nonzero integer gap \(h\), and dyadic time \(r\), define

\[
X_p(r;h)
=
B_p(2^rh)-\mu_p(h),
\]

where \(B_p\) is the local two-twin-pair singular factor and \(\mu_p(h)\) is its exact full-orbit mean.

If \(p\mid h\), the local residue is fixed at zero and therefore

\[
X_p(r;h)\equiv0.
\]

If \(p\nmid h\), write

\[
d_p=\operatorname{ord}_p(2).
\]

The centered observable is periodic with period \(d_p\).

## 2. Local Fourier coefficient bound — OP-D060

Use normalized Fourier coefficients

\[
\widehat X_p(m)
=
\frac1{d_p}
\sum_{r=0}^{d_p-1}
X_p(r;h)e^{-2\pi i mr/d_p}.
\]

Because \(X_p\) is centered,

\[
\widehat X_p(0)=0.
\]

For \(p\ge5\),

\[
B_p(u)
=
\beta_p+
\alpha_p
\left(
2\mathbf1_{u=0}
+
\mathbf1_{u=2}
+
\mathbf1_{u=-2}
\right),
\qquad
\alpha_p=\frac{p^3}{(p-1)^4}.
\]

On a nonzero orbit the state \(u=0\) is absent.

If the orbit is ordinary, it contains neither \(+2\) nor \(-2\), so \(X_p\equiv0\).

If \(d_p\) is odd and the orbit is special, it contains exactly one of \(+2,-2\). Hence every nonzero Fourier coefficient has magnitude

\[
|\widehat X_p(m)|=\frac{\alpha_p}{d_p}.
\]

If \(d_p\) is even and the orbit is special, \(+2\) and \(-2\) occur half an orbit apart. Hence

\[
\widehat X_p(m)
=
\frac{\alpha_p}{d_p}
e^{-2\pi i m r_0/d_p}
\left(1+(-1)^m\right),
\]

so odd modes vanish and even nonzero modes have magnitude

\[
\frac{2\alpha_p}{d_p}.
\]

Therefore, in every case,

\[
\boxed{
|\widehat X_p(m)|
\le
\frac{2\alpha_p}{d_p}
\qquad(m\ne0).
}
\]

## 3. Resonant centered-moment bound — OP-D061

Let \(J\) be a finite set of distinct prime channels, \(n=|J|\), none dividing \(h\). Let

\[
L_J=\operatorname{lcm}_{p\in J}d_p.
\]

The common-clock centered moment is

\[
M_X(J;h)
=
\left\langle
\prod_{p\in J}X_p(r;h)
\right\rangle_r.
\]

After Fourier expansion, only mode tuples satisfying

\[
\sum_{p\in J}\frac{m_p}{d_p}\in\mathbb Z
\]

survive.

The homomorphism

\[
\prod_{p\in J}\mathbb Z/d_p\mathbb Z
\longrightarrow
\mathbb Q/\mathbb Z,
\qquad
(m_p)_p
\mapsto
\sum_p\frac{m_p}{d_p}
\]

has image of order \(L_J\). Hence its kernel has exactly

\[
\frac{\prod_{p\in J}d_p}{L_J}
\]

elements.

Dropping the restrictions \(m_p\ne0\) and the additional local mode-selection zeros can only enlarge the count. Using OP-D060,

\[
\begin{aligned}
|M_X(J;h)|
&\le
\frac{\prod_pd_p}{L_J}
\prod_{p\in J}\frac{2\alpha_p}{d_p}\\
&=
\boxed{
\frac{2^n}{L_J}
\prod_{p\in J}\alpha_p.
}
\end{aligned}
\]

If any channel is constant, the actual centered moment is zero.

## 4. Connected cumulant bound — OP-D062

For \(n\ge2\), joint cumulants are invariant under adding constants to any argument. Therefore the connected ARPL weight \(K(J;h)\) equals the cumulant of the centered variables \(X_p\).

For centered variables, every partition containing a singleton block contributes zero. Thus

\[
K(J;h)
=
\sum_{\substack{\pi\in\Pi(J)\\
\text{no singleton blocks}}}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{A\in\pi}M_X(A;h).
\]

For each block \(A\), OP-D061 gives

\[
|M_X(A;h)|
\le
\frac{2^{|A|}}{L_A}
\prod_{p\in A}\alpha_p.
\]

Let

\[
D_J=\max_{p\in J}d_p.
\]

In every partition, the block containing a channel with period \(D_J\) has \(L_A\ge D_J\), while every other \(L_A\ge1\). Hence

\[
\prod_{A\in\pi}\frac1{L_A}
\le
\frac1{D_J}.
\]

Using \((|\pi|-1)!\le(n-1)!\) and at most \(B_n\) set partitions, where \(B_n\) is the Bell number,

\[
\boxed{
|K(J;h)|
\le
B_n(n-1)!2^n
\frac{\prod_{p\in J}\alpha_p}{D_J}.
}
\]

This is deliberately crude but fully explicit.

## 5. Prime-channel estimates

For every \(p\ge5\),

\[
\alpha_p
=
\frac1p\left(\frac{p}{p-1}\right)^4
\le
\frac1p\left(\frac54\right)^4.
\]

Also

\[
p\mid 2^{d_p}-1
\]

implies

\[
p\le2^{d_p}-1
\]

and therefore

\[
\boxed{
d_p\ge\log_2(p+1).
}
\]

No conjecture about Artin primitive roots or the typical size of \(d_p\) is used.

## 6. Fixed-order absolute summability — OP-D063

Fix \(h\ne0\) and an integer \(n\ge2\).

Define the order-\(n\) global connected layer

\[
\boxed{
\mathcal K_n(h)
=
\sum_{\substack{J\subset\mathbb P_{\ge5}\\|J|=n}}
K(J;h).
}
\]

Terms containing a prime divisor of \(h\) vanish because that local centered observable is constant, so only finitely many channels are removed.

Order the primes in \(J\) as

\[
p_1<\cdots<p_n=q.
\]

Then

\[
D_J\ge d_q\ge\log_2(q+1).
\]

Using OP-D062 and the bound \(\alpha_p\ll1/p\),

\[
|K(J;h)|
\ll_n
\frac1{\log q}
\prod_{j=1}^n\frac1{p_j}.
\]

Therefore

\[
\sum_{|J|=n}|K(J;h)|
\ll_n
\sum_q
\frac1{q\log q}
\left(
\sum_{p<q}\frac1p
\right)^{n-1}.
\]

The classical Mertens estimate gives

\[
\sum_{p<q}\frac1p
=
O(\log\log q).
\]

Hence it remains to bound

\[
\sum_q
\frac{(\log\log q)^{n-1}}{q\log q}.
\]

This prime sum converges. For example, on dyadic blocks

\[
2^k\le q<2^{k+1},
\]

the standard upper bound

\[
\pi(x)\ll\frac{x}{\log x}
\]

gives block contribution

\[
\ll_n
\frac{(\log k)^{n-1}}{k^2},
\]

whose sum over \(k\) converges.

Consequently

\[
\boxed{
\sum_{\substack{J\subset\mathbb P_{\ge5}\\|J|=n}}
|K(J;h)|
<\infty
\qquad
\text{for every fixed }n\ge2.
}
\]

Thus every fixed connected order has a rigorously defined global infinite-prime-channel value.

## 7. What is now closed

The hierarchy

\[
\mathcal K_2(h),\quad
\mathcal K_3(h),\quad
\mathcal K_4(h),\ldots
\]

is termwise well-defined: each layer separately is absolutely convergent across all prime channels.

This is stronger than finite-support convergence and requires no statistical model for primes.

## 8. What remains open

The theorem does **not** prove convergence after summing over connected order:

\[
\sum_{n\ge2}\mathcal K_n(h).
\]

The constant in OP-D062 grows rapidly with \(n\), and the present argument does not supply a summable majorant uniform in \(n\).

Therefore the current global status is:

\[
\boxed{
\text{every fixed connected order: CLOSED;}
}
\]

\[
\boxed{
\text{all-orders connected cluster sum: OPEN.}
}
\]

## 9. Prior-art boundary

The proof uses standard:

- finite Fourier orthogonality;
- multiplicative orders;
- moment--cumulant Möbius inversion;
- Mertens' theorem for reciprocal primes;
- the standard upper bound \(\pi(x)\ll x/\log x\).

The ARPL-specific content is their combination for the dyadic singular-factor phase channels.

No novelty claim is made without a broader literature audit.
