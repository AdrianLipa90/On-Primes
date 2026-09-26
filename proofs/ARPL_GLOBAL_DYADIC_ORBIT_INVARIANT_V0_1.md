# ARPL Global Dyadic Orbit Invariant v0.1

Status: exact global convergence/invariance theorem built from standard local Hardy--Littlewood factors.

## 1. Local orbit mean

For a prime \(p\ge5\), define the two-twin-pair local factor

\[
B_p(h)
=
\frac{1-\nu_p(\{0,2,h,h+2\})/p}{(1-1/p)^4}.
\]

Let

\[
d_p=\operatorname{ord}_p(2).
\]

For fixed nonzero integer \(h\), define the local dyadic orbit mean

\[
\mu_p(h)
=
\begin{cases}
B_p(0),&p\mid h,\\[1mm]
\displaystyle
\frac1{d_p}\sum_{r=0}^{d_p-1}B_p(2^rh),&p\nmid h.
\end{cases}
\]

This definition is independent of which point of the same doubling orbit is chosen as the starting point.

## 2. Exact local classification — OP-D053

For \(p\ge5\), write

\[
\alpha_p=\frac{p^3}{(p-1)^4},
\qquad
\beta_p=\frac{p^3(p-4)}{(p-1)^4}.
\]

The local observable is

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

Therefore:

### Zero-fixed orbit

If \(p\mid h\),

\[
\boxed{
\mu_p(h)=\beta_p+2\alpha_p.
}
\]

### Ordinary nonzero orbit

If the doubling orbit of \(h\bmod p\) contains neither \(+2\) nor \(-2\),

\[
\boxed{
\mu_p(h)=\beta_p.
}
\]

### Special orbit, even \(d_p\)

If the orbit contains \(+2\) and \(d_p\) is even, then it also contains \(-2\), exactly half an orbit away. Hence

\[
\boxed{
\mu_p(h)=\beta_p+\frac{2\alpha_p}{d_p}.
}
\]

### Special orbit, odd \(d_p\)

If \(d_p\) is odd, the \(+2\) and \(-2\) residues lie on distinct cycles. On either special cycle,

\[
\boxed{
\mu_p(h)=\beta_p+\frac{\alpha_p}{d_p}.
}
\]

These cases exhaust all residue orbits.

## 3. Local dyadic invariance — OP-D054

For every \(p\ge5\), every nonzero integer \(h\), and every \(k\ge0\),

\[
\boxed{
\mu_p(2^kh)=\mu_p(h).
}
\]

Proof:

- if \(p\mid h\), then \(p\mid2^kh\), so both states are the same zero-fixed orbit;
- if \(p\nmid h\), multiplying the starting residue by \(2^k\) merely rotates the same finite doubling cycle, and a full-cycle average is invariant under rotation.

Thus each local mean is an orbit invariant of the dyadic action.

## 4. Absolute convergence of the global product — OP-D055

For fixed nonzero \(h\), define

\[
\boxed{
\mathcal I(h)
=
\prod_{p\ge5}\mu_p(h).
}
\]

Only finitely many primes \(p\) divide \(h\), so zero-fixed exceptional factors occur finitely often.

For all remaining \(p\),

\[
\mu_p(h)
=
\beta_p+\varepsilon_p(h),
\qquad
0\le\varepsilon_p(h)\le\frac{2\alpha_p}{d_p}.
\]

The background defect is exactly

\[
1-\beta_p
=
\frac{6p^2-4p+1}{(p-1)^4}
=
O(p^{-2}).
\]

Also

\[
\alpha_p
=
\frac{p^3}{(p-1)^4}
=
O(p^{-1}).
\]

Since \(d_p=\operatorname{ord}_p(2)\) and \(p\mid2^{d_p}-1\),

\[
p\le2^{d_p}-1,
\]

hence

\[
d_p\ge\log_2(p+1).
\]

Therefore

\[
|\mu_p(h)-1|
\le
O(p^{-2})
+
O\!\left(\frac1{p\log p}\right).
\]

The prime sums

\[
\sum_p\frac1{p^2}
\quad\text{and}\quad
\sum_p\frac1{p\log p}
\]

converge. The second follows, for example, from the standard upper bound
\(\pi(x)=O(x/\log x)\) by dyadic decomposition or partial summation.

Consequently

\[
\boxed{
\sum_{p\ge5}|\mu_p(h)-1|<\infty.
}
\]

Since every \(\mu_p(h)>0\), the Euler-type product

\[
\boxed{
0<\mathcal I(h)<\infty
}
\]

converges to a finite nonzero value.

## 5. Global dyadic orbit invariant — OP-D056

By OP-D054 every finite partial product satisfies

\[
\prod_{5\le p\le P}\mu_p(2^kh)
=
\prod_{5\le p\le P}\mu_p(h).
\]

Taking the absolutely convergent limit gives

\[
\boxed{
\mathcal I(2^kh)=\mathcal I(h)
\qquad
(k\ge0,\ h\ne0).
}
\]

Thus \(\mathcal I\) is a rigorously defined global invariant of the dyadic orbit.

For positive integers this means that \(\mathcal I(h)\) depends only on the odd part of \(h\):

\[
\boxed{
\mathcal I(h)=\mathcal I(\operatorname{oddpart}(h)).
}
\]

For twin-start gaps, which already satisfy \(6\mid h\), this invariant ignores the pure power-of-two scale while retaining the odd-channel orbit structure.

## 6. Relation to the common-clock resonance observable

The invariant

\[
\mathcal I(h)=\prod_p\mu_p(h)
\]

is the convergent product of independently averaged local channels.

It is not automatically equal to the increasing-support limit of the shared-clock means

\[
\left\langle
\prod_{p\le P}B_p(2^rh)
\right\rangle_r,
\]

because finite supports can have nonzero cross-channel resonance corrections

\[
\mathcal C_P(h).
\]

Hence the global structure separates cleanly into:

\[
\boxed{
\text{convergent dyadic orbit baseline}
+
\text{cross-channel resonance corrections}.
}
\]

The baseline is now closed. Convergence of a fully coupled infinite-channel common-clock observable remains open.

## 7. Numerical receipt, not theorem input

For \(h=6\), direct floating evaluation of finite prime truncations of \(\mathcal I(h)\) gave:

\[
\begin{array}{c|c}
P & \prod_{5\le p\le P}\mu_p(6)\\
\hline
100 & 0.5548091709609418\\
200 & 0.5520054504165318\\
500 & 0.5508141210259084\\
1000 & 0.5504696762697121\\
2000 & 0.5503050937246090\\
5000 & 0.5502185828395376\\
10000 & 0.5501934372310352
\end{array}
\]

These values illustrate convergence only; the proof is the summability argument above.

## 8. Prior-art boundary

The proof uses standard ingredients:

- multiplicative order;
- finite orbit averaging;
- Hardy--Littlewood local singular factors;
- standard convergence estimates for prime sums.

The specific invariant \(\mathcal I(h)\) is introduced here as the ARPL global dyadic orbit baseline. A literature audit is still required before any novelty claim.

## 9. No-go

This invariant does not prove:

- occurrence of twin-prime pairs;
- infinitely many twin primes;
- the Hardy--Littlewood asymptotic;
- convergence of the fully coupled infinite resonance correction;
- a zeta-zero correspondence;
- RH.
