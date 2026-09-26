# ARPL Quadratic Phase Clock v0.1

Status: exact reduction of the two-twin-pair phase observable from the base-2 residue orbit to its minimal base-4 clock.

## 1. The observable is sign-blind

For a prime \(p\ge5\), the dynamic special event is

\[
2^rh\equiv\pm2\pmod p.
\]

Squaring gives the equivalent condition

\[
\boxed{
4^rh^2\equiv4\pmod p.
}
\]

Thus the two equal special residues \(+2\) and \(-2\) are one event in the squared phase coordinate.

## 2. Minimal observable period — OP-D080

Let

\[
d_p=\operatorname{ord}_p(2).
\]

For \(p\nmid h\), define

\[
e_p=\operatorname{ord}_p(4).
\]

The standard order identity gives

\[
\boxed{
e_p=
\frac{d_p}{\gcd(d_p,2)}.
}
\]

Hence

\[
e_p=
\begin{cases}
d_p,&d_p\text{ odd},\\
d_p/2,&d_p\text{ even}.
\end{cases}
\]

The local residue state \(2^rh\bmod p\) can require \(d_p\) steps to return, but the sign-symmetric twin observable has minimal carrier period dividing \(e_p\), and on an active channel its hit sequence has exactly period \(e_p\).

If \(p\mid h\), the dynamic special event never occurs and the centered channel is constant; assign effective period \(1\).

## 3. Single-phase theorem — OP-D081

Assume \(p\nmid h\). The powers \(4^r\) run once through the cyclic subgroup

\[
\langle4\rangle\subset\mathbb F_p^\times
\]

over \(r\bmod e_p\).

Therefore the equation

\[
4^rh^2\equiv4\pmod p
\]

has either:

- no solution modulo \(e_p\), or
- exactly one solution
  \[
  r\equiv\rho_p(h)\pmod{e_p}.
  \]

Consequently the special-hit indicator has the exact compressed form

\[
\boxed{
E_p(r;h)
=
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}}
}
\]

for active channels, and \(E_p\equiv0\) for inactive channels.

Thus

\[
\boxed{
\delta_p(h)
=
\begin{cases}
1/e_p,&\text{active},\\
0,&\text{inactive}.
\end{cases}
}
\]

This unifies the previous \(1/d_p\) versus \(2/d_p\) cases.

## 4. Exact joint density — OP-D082

For two active channels \(p,q\), let their unique phases be

\[
\rho_p\pmod{e_p},
\qquad
\rho_q\pmod{e_q}.
\]

The simultaneous-hit system

\[
r\equiv\rho_p\pmod{e_p},
\qquad
r\equiv\rho_q\pmod{e_q}
\]

has a solution iff

\[
\boxed{
\rho_p\equiv\rho_q
\pmod{\gcd(e_p,e_q)}.
}
\]

If compatible, CRT gives exactly one class modulo

\[
\operatorname{lcm}(e_p,e_q),
\]

so

\[
\boxed{
\delta_{pq}(h)
=
\frac1{\operatorname{lcm}(e_p,e_q)}.
}
\]

If incompatible,

\[
\boxed{\delta_{pq}(h)=0.}
\]

This is sharper than the earlier upper bound based on up to four signed hit combinations.

## 5. Local Fourier spectrum — OP-D083

For an active channel,

\[
E_p(r)=\mathbf1_{\{r\equiv\rho_p\pmod{e_p}\}}.
\]

Its normalized Fourier coefficient on \(\mathbb Z/e_p\mathbb Z\) is

\[
\widehat E_p(m)
=
\frac1{e_p}
e^{-2\pi i m\rho_p/e_p},
\qquad
m=0,\dots,e_p-1.
\]

Therefore every nonzero local mode has the same magnitude

\[
\boxed{
|\widehat E_p(m)|=\frac1{e_p}.
}
\]

The previous odd-mode cancellation for even \(d_p\) is exactly the statement that the observable actually factors through the quotient clock of length \(e_p=d_p/2\).

The genuine twin-observable frequency lattice is therefore

\[
\boxed{
\lambda=\frac{m}{e_p}
=
\frac{m}{\operatorname{ord}_p(4)}
\pmod1.
}
\]

## 6. Global logarithmic field in compressed form

The dynamic logarithmic field becomes

\[
\boxed{
\log\mathfrak S(H_{2^rh})
=
\log\left(\frac{27}{2}C_*Z(h)\right)
+
\sum_{p\in\mathcal A_h}
w_p
\mathbf1_{\{r\equiv\rho_p(h)\pmod{e_p}\}},
}
\]

where

\[
w_p=\log\frac{p-3}{p-4}
\]

and \(\mathcal A_h\) is the set of active odd-prime channels.

This is a weighted superposition of exact arithmetic pulse trains.

## 7. Relation to the divisor factorization

The active condition at time \(r\),

\[
r\equiv\rho_p(h)\pmod{e_p},
\]

is equivalent to

\[
p\mid4^rh^2-4.
\]

Thus the base-4 phase-clock description and the instantaneous divisor-weight description are exactly the same object in temporal and arithmetic coordinates.

## 8. Boundary

The identity

\[
\operatorname{ord}_p(4)
=
\operatorname{ord}_p(2)/\gcd(\operatorname{ord}_p(2),2)
\]

and CRT are standard mathematics.

The ARPL-specific contribution is the recognition and use of the minimal sign-quotiented clock for this singular-series observable, not a claim that multiplicative-order theory itself is new.
