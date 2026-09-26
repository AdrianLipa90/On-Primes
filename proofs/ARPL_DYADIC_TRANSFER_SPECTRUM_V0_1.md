# ARPL Dyadic Transfer Spectrum v0.1

Status: exact finite operator theorem pack.

## 1. Doubling operator on a prime phase channel

Fix an odd prime \(p\). The ARPL dyadic transport acts on the residue state space

\[
\mathbb Z/p\mathbb Z
\]

by

\[
D_p(u)=2u\pmod p.
\]

Because \(2\) is invertible modulo \(p\), \(D_p\) is a permutation.

Let

\[
d_p=\operatorname{ord}_p(2).
\]

Then \(0\) is a fixed point and every nonzero orbit has length exactly \(d_p\). Hence the number of nonzero cycles is

\[
c_p=\frac{p-1}{d_p}.
\]

## 2. Transfer-spectrum theorem — OP-D041

Let \(U_p\) be the permutation/Koopman operator induced by \(D_p\) on functions on \(\mathbb Z/p\mathbb Z\).

Each nonzero \(d_p\)-cycle contributes every \(d_p\)-th root of unity once to the spectrum. The fixed state \(0\) contributes one additional eigenvalue \(1\).

Thus, writing

\[
\lambda_m=e^{2\pi i m/d_p},
\qquad
m=0,\dots,d_p-1,
\]

the multiplicities are

\[
\operatorname{mult}(\lambda_0)=c_p+1,
\]

and

\[
\operatorname{mult}(\lambda_m)=c_p
\quad
(1\le m<d_p).
\]

The total dimension is

\[
(c_p+1)+(d_p-1)c_p
=
1+d_pc_p
=
p.
\]

## 3. Three-level twin observable — OP-D042

For the two-twin-pair pattern

\[
H_u=\{0,2,u,u+2\},
\]

and prime \(p\ge5\), the residue count is

\[
\nu_p(H_u)=
\begin{cases}
2,&u=0,\\
3,&u=\pm2,\\
4,&\text{otherwise}.
\end{cases}
\]

Define the standard local singular factor

\[
B_p(u)=
\frac{1-\nu_p(H_u)/p}{(1-1/p)^4}.
\]

Set

\[
\alpha_p=\frac{p^3}{(p-1)^4},
\qquad
\beta_p=\frac{p^3(p-4)}{(p-1)^4}.
\]

Then exactly

\[
\boxed{
B_p(u)
=
\beta_p
+
\alpha_p
\left(
2\,\mathbf 1_{u=0}
+
\mathbf 1_{u=2}
+
\mathbf 1_{u=-2}
\right).
}
\]

Thus, after the \(p=2,3\) carrier gate, every higher prime channel is a constant background plus three distinguished phase defects: a double defect at \(0\) and equal single defects at \(\pm2\).

## 4. Special-cycle theorem

The nonzero doubling orbits are multiplicative cosets of the subgroup

\[
\langle2\rangle\subset\mathbb F_p^\times.
\]

The residues \(+2\) and \(-2\) lie in the same doubling orbit iff

\[
-1\in\langle2\rangle.
\]

Because \(\langle2\rangle\) has order \(d_p\), this is equivalent to

\[
\boxed{
+2\text{ and }-2\text{ share an orbit}
\iff
d_p\text{ is even}.
}
\]

If \(d_p\) is even, they are separated by exactly half an orbit:

\[
D_p^{d_p/2}(2)=-2.
\]

If \(d_p\) is odd, they lie on two distinct nonzero cycles.

## 5. Mode-selection rule — OP-D043

Subtract the constant background \(\beta_p\) from \(B_p\) and restrict to the doubling cycle containing \(+2\).

### Even \(d_p\)

Rotate the cycle so \(+2\) is at index \(j=0\). Then \(-2\) is at

\[
j=d_p/2.
\]

The baseline-subtracted observable on that cycle is

\[
\alpha_p
\left(
\delta_{j,0}
+
\delta_{j,d_p/2}
\right).
\]

Its normalized discrete Fourier coefficient at mode \(m\) is proportional to

\[
1+e^{-\pi i m}
=
1+(-1)^m.
\]

Therefore

\[
\boxed{
\widehat B_p(m)=0
\quad\text{for every odd }m.
}
\]

Only even transfer modes survive.

### Odd \(d_p\)

The residues \(+2\) and \(-2\) are on different cycles. Each special cycle contains one single defect above the constant background. A single delta has nonzero projection onto every Fourier mode, so every mode \(m=0,\dots,d_p-1\) is present on each special cycle.

Hence

\[
\boxed{
d_p\ {\rm even}
\Rightarrow
\text{odd-mode cancellation},
}
\]

while

\[
\boxed{
d_p\ {\rm odd}
\Rightarrow
\text{full mode support on each special cycle}.
}
\]

## 6. Interpretation inside ARPL

The chain is now exact:

\[
T(x)=2x+1
\]

induces

\[
\Delta\mapsto2\Delta
\]

and therefore, in every odd-prime phase channel,

\[
u\mapsto2u\pmod p.
\]

The same permutation controls:

1. dyadic separation transport;
2. fibre modular-obstruction phase orbits;
3. the local Hardy--Littlewood observable for two twin pairs;
4. the finite transfer spectrum;
5. the parity selection rule of the observable's eigenmode decomposition.

No probabilistic assumption enters these identities.

## 7. Boundary of the result

The transfer-spectrum theorem is finite and exact. It does not assert that the product over all prime channels defines a new global spectral theorem, nor that its mode structure predicts prime occurrence.

The next open problem is whether the tensor/product assembly of these local transfer operators admits a convergent, renormalized, or projectively consistent global operator that carries information beyond standard congruence and singular-series data.
