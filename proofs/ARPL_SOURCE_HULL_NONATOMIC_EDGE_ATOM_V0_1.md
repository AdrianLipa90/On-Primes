# ARPL Source-Hull Non-Atomicity and Lower-Edge Atom Criterion v0.1

Status: exact theorem pack. The infinitude-of-prime-divisors input is classical; the phase-hull consequences and lower-edge formulas are derived for the ARPL dyadic singular-series law.

## 1. Setup

Fix an admissible base separation

\[
h\ge6,\qquad 6\mid h.
\]

Write

\[
q=\frac h2.
\]

Then

\[
q\in3\mathbb Z.
\]

The dynamic divisor sequence can be written as

\[
4^rh^2-4
=
4\left(q^2 4^r-1\right).
\]

Define

\[
U_r=q^2 4^r-1.
\]

A prime \(p\ge5\) is an active ARPL channel exactly when

\[
p\mid U_r
\]

for some \(r\), equivalently when

\[
4^rh^2\equiv4\pmod p.
\]

For every active channel let

\[
e_p=\operatorname{ord}_p(4),
\]

and let

\[
\rho_p(h)\pmod{e_p}
\]

be its unique base-4 hit phase.

## 2. Infinitely many active prime channels — OP-D121

The sequence

\[
U_r=q^2 4^r-1
\]

is an integer linear recurrence with characteristic roots

\[
4,\ 1.
\]

Indeed it satisfies

\[
U_{r+2}=5U_{r+1}-4U_r.
\]

The quotient of the two distinct characteristic roots is \(4\), which is not a root of unity. Hence the recurrence is non-degenerate.

A classical theorem of Pólya states that a non-degenerate integer linear recurrence of order at least \(2\) has infinitely many distinct prime divisors.

Therefore the set

\[
\{p:\exists r,\ p\mid U_r\}
\]

is infinite.

Moreover,

\[
U_r\equiv1\pmod2
\]

and, because \(3\mid q\),

\[
U_r\equiv-1\pmod3.
\]

Thus no prime divisor of \(U_r\) is \(2\) or \(3\).

Hence every prime divisor supplied by Pólya is at least \(5\) and is an active ARPL phase channel.

Therefore

\[
\boxed{
\#\mathcal A_h=\infty,
}
\]

where \(\mathcal A_h\) is the active odd-prime channel set.

## 3. Observable periods are unbounded — OP-D122

Assume, for contradiction, that all active observable periods satisfy

\[
e_p\le E.
\]

By definition,

\[
p\mid4^{e_p}-1.
\]

Hence every active prime would divide the fixed integer

\[
\prod_{e=1}^E(4^e-1),
\]

which has only finitely many prime divisors.

This contradicts OP-D121.

Therefore

\[
\boxed{
\sup_{p\in\mathcal A_h}e_p=\infty.
}
\]

Enumerate all active channels as

\[
p_1,p_2,\dots
\]

and define

\[
L_N=\operatorname{lcm}(e_{p_1},\dots,e_{p_N}).
\]

Then

\[
\boxed{
L_N\to\infty.
}
\]

## 4. Haar measure on the phase hull is non-atomic — OP-D123

The global phase hull is

\[
K_h
\cong
\varprojlim_N
\mathbb Z/L_N\mathbb Z.
\]

Its Haar probability measure projects to uniform measure on every finite quotient.

Fix any point

\[
x\in K_h.
\]

The level-\(N\) cylinder containing \(x\) has Haar mass

\[
\frac1{L_N}.
\]

As \(L_N\to\infty\),

\[
\frac1{L_N}\to0.
\]

The singleton \(\{x\}\) is the decreasing intersection of these cylinders, so continuity from above gives

\[
m_{K_h}(\{x\})
=
\lim_{N\to\infty}\frac1{L_N}
=
0.
\]

Hence

\[
\boxed{
m_{K_h}\text{ is non-atomic}.
}
\]

The finite-quotient phase information

\[
H_N=\log L_N
\]

therefore diverges:

\[
\boxed{
H_N\to\infty.
}
\]

This is a statement about the source phase hull. It does not imply that the pushforward amplitude law is non-atomic.

## 5. Lower-edge event

The limiting logarithmic field is

\[
\mathcal Y_h(x)
=
\log A(h)
+
\sum_{p\in\mathcal A_h}
w_p\,\mathbf1_{C_p}(x),
\]

where

\[
w_p=\log\frac{p-3}{p-4}>0
\]

and

\[
C_p
=
\{x\in K_h:x_p=\rho_p(h)\}
\]

is the active hit cylinder.

The limiting positive amplitude is

\[
\mathcal X_h(x)=e^{\mathcal Y_h(x)}.
\]

Because every \(w_p>0\),

\[
\mathcal Y_h(x)=\log A(h)
\]

iff no active hit cylinder occurs:

\[
x\notin C_p
\qquad
\forall p\in\mathcal A_h.
\]

Define the avoidance set

\[
\boxed{
C_\infty(h)
=
K_h\setminus\bigcup_{p\in\mathcal A_h}C_p
=
\bigcap_{p\in\mathcal A_h}C_p^c.
}
\]

## 6. Exact lower-edge atom criterion — OP-D124

Let

\[
\nu_h
\]

be the limiting law of the logarithmic field and

\[
\mu_h=(\exp)_*\nu_h
\]

the limiting positive amplitude law.

Then

\[
\boxed{
\nu_h(\{\log A(h)\})
=
\mu_h(\{A(h)\})
=
m_{K_h}(C_\infty(h)).
}
\]

Thus the possible atom at the hard lower edge is exactly the Haar measure of the phase-avoidance set.

Define

\[
a_*(h)
=
m_{K_h}(C_\infty(h)).
\]

Then

\[
\boxed{
\text{lower-edge atom exists}
\iff
a_*(h)>0.
}
\]

Non-atomicity of the source Haar measure does not decide the sign of \(a_*(h)\).

## 7. Finite exact approximants — OP-D125

For the first \(N\) active channels define

\[
C_N(h)
=
\bigcap_{j=1}^N C_{p_j}^c.
\]

Then

\[
C_{N+1}(h)\subseteq C_N(h),
\]

and

\[
C_\infty(h)
=
\bigcap_{N\ge1}C_N(h).
\]

Therefore

\[
\boxed{
a_N(h):=m_{K_h}(C_N(h))
\downarrow
a_*(h).
}
\]

On the finite clock

\[
\mathbb Z/L_N\mathbb Z,
\]

this mass is exactly

\[
\boxed{
a_N(h)
=
\frac1{L_N}
\#\left\{
0\le r<L_N:
r\not\equiv\rho_{p_j}(h)\pmod{e_{p_j}}
\ \forall j\le N
\right\}.
}
\]

Using inclusion--exclusion and the exact generalized-CRT joint densities,

\[
\boxed{
a_N(h)
=
\sum_{J\subseteq\{1,\dots,N\}}
(-1)^{|J|}
\delta_J(h),
}
\]

with

\[
\delta_\varnothing=1.
\]

This provides an exact finite rational approximation from above to the lower-edge atom mass.

## 8. Extraction from negative moments — OP-D126

Because the limiting amplitude satisfies

\[
X\ge A(h)>0,
\]

for \(t>0\),

\[
A(h)^t\mathcal M_h(-t)
=
\int
\left(\frac{A(h)}x\right)^t
\,d\mu_h(x).
\]

The integrand lies in \([0,1]\) and converges pointwise as \(t\to\infty\) to

\[
\mathbf1_{\{x=A(h)\}}.
\]

Dominated convergence therefore gives

\[
\boxed{
a_*(h)
=
\lim_{t\to\infty}
A(h)^t\mathcal M_h(-t).
}
\]

Thus the possible lower-edge atom is encoded directly in the far negative-real asymptotic of the entire phase transform.

## 9. Independent-subclock sufficient criterion — OP-D127

Suppose there exists an infinite active subfamily

\[
\mathcal Q\subset\mathcal A_h
\]

such that the observable periods \(e_p\), \(p\in\mathcal Q\), are pairwise coprime.

For every finite \(F\subset\mathcal Q\), the CRT makes the corresponding hit cylinders independent under Haar measure:

\[
m_{K_h}
\left(
\bigcap_{p\in F}C_p^c
\right)
=
\prod_{p\in F}
\left(1-\frac1{e_p}\right).
\]

Therefore, if in addition

\[
\sum_{p\in\mathcal Q}\frac1{e_p}
=
\infty,
\]

then

\[
\prod_{p\in\mathcal Q}
\left(1-\frac1{e_p}\right)
=
0.
\]

Since avoiding all active channels implies avoiding all channels in \(\mathcal Q\),

\[
\boxed{
a_*(h)=0.
}
\]

This is a sufficient atom-removal criterion.

The existence of such a subfamily with divergent reciprocal period mass is not proved here.

## 10. Example: finite lower-edge masses for \(h=6\)

Ordering the first active channels by prime,

\[
5,7,11,13,19,23,29,37,47,53,\dots,
\]

the exact finite avoidance masses begin

\[
\begin{array}{c|c|c}
N & p_N & a_N(6)\\
\hline
1&5&1/2\\
2&7&1/3\\
3&11&4/15\\
4&13&2/15\\
5&19&2/15\\
6&23&4/33\\
7&29&4/33\\
8&37&4/33\\
9&47&8/69\\
10&53&8/69
\end{array}
\]

For the first \(15\) active channels through \(p=79\),

\[
L_{15}=60090030
\]

and direct finite-clock enumeration gives

\[
\boxed{
a_{15}(6)=\frac{252}{3335}
\approx0.07556221889.
}
\]

These values are finite-channel upper bounds on \(a_*(6)\).

They do not establish whether the limiting lower-edge atom is positive or zero.

## 11. Prior-art boundary

The theorem that non-degenerate integer linear recurrences have infinitely many distinct prime divisors is classical and goes back to Pólya.

The inverse-limit/Haar and inclusion--exclusion steps are standard compact-group and probability arguments.

The ARPL-specific content is the identification of:

- the recurrence prime divisors with active base-4 phase channels;
- the unbounded ARPL clock tower;
- the exact lower-edge atom as a phase-avoidance Haar mass;
- its extraction from the negative-real phase transform.

## 12. Current status

Closed:

\[
\boxed{
\mathcal A_h\text{ is infinite;}
}
\]

\[
\boxed{
e_p\text{ is unbounded;}
}
\]

\[
\boxed{
L_N\to\infty;
}
\]

\[
\boxed{
K_h\text{ has non-atomic Haar measure;}
}
\]

\[
\boxed{
a_*(h)
=
\lim_Na_N(h)
=
\lim_{t\to\infty}A(h)^t\mathcal M_h(-t).
}
\]

Open:

\[
\boxed{
a_*(h)=0\text{ or }>0?
}
\]

and, more generally, whether the full pushforward law \(\nu_h\) is atomic, mixed, singular-continuous, or absolutely continuous.
