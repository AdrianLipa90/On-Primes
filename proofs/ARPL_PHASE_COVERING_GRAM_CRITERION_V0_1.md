# ARPL Phase-Covering Gram Criterion v0.1

Status: exact finite Hilbert-space covering theorem + infinite atom-removal criterion.

## 1. Active hit cylinders

Fix admissible

\[
h\ge6,\qquad 6\mid h.
\]

For each active odd-prime channel \(p\), let

\[
e_p=\operatorname{ord}_p(4),
\qquad
\rho_p=\rho_p(h)\pmod{e_p},
\]

and define the hit cylinder in the ARPL odometer

\[
C_p
=
\{x\in K_h:x_p=\rho_p\}.
\]

Its Haar measure is

\[
\boxed{
d_p:=m(C_p)=\frac1{e_p}.
}
\]

For two active channels \(p,q\), generalized CRT gives

\[
m(C_p\cap C_q)
=
\begin{cases}
\displaystyle
\frac1{\operatorname{lcm}(e_p,e_q)},
&
\rho_p\equiv\rho_q
\pmod{\gcd(e_p,e_q)},
\\[3mm]
0,
&
\text{otherwise}.
\end{cases}
\]

## 2. Phase-covering Gram matrix — OP-D135

For a finite active set

\[
P=\{p_1,\dots,p_N\},
\]

define

\[
f_i=\mathbf1_{C_{p_i}}\in L^2(K_h,m).
\]

The Gram matrix is

\[
\boxed{
G_{ij}
=
\langle f_i,f_j\rangle
=
m(C_{p_i}\cap C_{p_j}).
}
\]

Define the density vector

\[
\boxed{
d_i
=
\langle f_i,1\rangle
=
\frac1{e_{p_i}}.
}
\]

Then \(G\) is symmetric positive semidefinite.

Every entry is an exact rational number determined by the periods and phase-compatibility relation.

## 3. Weighted covering bound — OP-D136

Let

\[
U_P=\bigcup_{p\in P}C_p
\]

and choose arbitrary real weights

\[
w=(w_p)_{p\in P}.
\]

Define

\[
F_w
=
\sum_{p\in P}w_p\mathbf1_{C_p}.
\]

Since \(F_w=0\) outside \(U_P\),

\[
\langle F_w,1\rangle
=
\langle F_w,\mathbf1_{U_P}\rangle.
\]

Cauchy--Schwarz gives

\[
|\langle F_w,1\rangle|^2
\le
\|F_w\|_2^2\,m(U_P).
\]

Now

\[
\langle F_w,1\rangle=w^\top d
\]

and

\[
\|F_w\|_2^2=w^\top G w.
\]

Therefore, whenever \(w^\top G w>0\),

\[
\boxed{
m(U_P)
\ge
\frac{(w^\top d)^2}{w^\top G w}.
}
\]

This holds for arbitrary real weights; positivity of the weights is not required.

## 4. Equal-weight second-moment bound

Choosing

\[
w_p=1
\]

gives

\[
\boxed{
m(U_P)
\ge
\frac{
\left(\sum_{p\in P}1/e_p\right)^2
}{
\sum_{p,q\in P}m(C_p\cap C_q)
}.
}
\]

Equivalently, if

\[
X_P=\sum_{p\in P}\mathbf1_{C_p},
\]

then

\[
m(U_P)
=
\Pr(X_P>0)
\ge
\frac{(\mathbb E X_P)^2}{\mathbb E X_P^2}.
\]

This is the finite second-moment / Cauchy--Schwarz covering bound.

## 5. Optimal finite \(L^2\) bound — OP-D137

Let

\[
V_P=\operatorname{span}\{f_p:p\in P\}
\subset L^2(K_h,m)
\]

and let

\[
\Pi_P1
\]

be the orthogonal projection of the constant function \(1\) onto \(V_P\).

The normal equations are

\[
Gw=d.
\]

They are always consistent: if \(v\in\ker G\), then

\[
\left\|\sum_pv_pf_p\right\|_2^2
=
v^\top Gv
=
0,
\]

so

\[
\sum_pv_pf_p=0
\quad\text{in }L^2,
\]

and therefore

\[
v^\top d
=
\left\langle
\sum_pv_pf_p,1
\right\rangle
=
0.
\]

Thus \(d\) is orthogonal to \(\ker G\), hence lies in the range of the symmetric matrix \(G\).

For any solution \(w\) of

\[
Gw=d,
\]

the projection is

\[
\Pi_P1=\sum_pw_pf_p,
\]

and

\[
\|\Pi_P1\|_2^2
=
w^\top Gw
=
w^\top d.
\]

Therefore the optimal weighted bound is

\[
\boxed{
B_P
:=
\sup_w
\frac{(w^\top d)^2}{w^\top Gw}
=
\|\Pi_P1\|_2^2
=
d^\top G^+d,
}
\]

where \(G^+\) denotes the Moore--Penrose pseudoinverse.

Since every vector in \(V_P\) is supported inside \(U_P\),

\[
\boxed{
B_P\le m(U_P).
}
\]

Hence the exact finite avoidance mass satisfies

\[
\boxed{
a_P
:=
1-m(U_P)
\le
1-B_P.
}
\]

## 6. Monotonicity — OP-D138

If

\[
P\subseteq Q,
\]

then

\[
V_P\subseteq V_Q.
\]

Orthogonal projection onto a larger closed finite-dimensional subspace cannot decrease the projection norm. Therefore

\[
\boxed{
B_P\le B_Q.
}
\]

Thus, for any increasing exhaustion of active channels,

\[
P_1\subset P_2\subset\cdots,
\]

the sequence

\[
B_N:=B_{P_N}
\]

is monotone non-decreasing and bounded by \(1\). Hence

\[
B_N\to B_\infty
\]

for some

\[
0\le B_\infty\le1.
\]

## 7. Infinite lower-edge atom criterion — OP-D139

Let

\[
U_\infty
=
\bigcup_{p\in\mathcal A_h}C_p
\]

and

\[
a_*(h)=1-m(U_\infty)
\]

be the exact lower-edge atom mass from OP-D124.

For every finite prefix,

\[
B_N\le m(U_{P_N})\le m(U_\infty)=1-a_*(h).
\]

Therefore

\[
\boxed{
a_*(h)
\le
1-B_\infty.
}
\]

In particular,

\[
\boxed{
B_N\to1
\quad\Longrightarrow\quad
a_*(h)=0.
}
\]

Thus lower-edge atomlessness can be proved by showing that the constant function \(1\) lies in the \(L^2\)-closure of the span of the active phase-hit cylinders.

Equivalently,

\[
\boxed{
a_*(h)=0
\quad\text{is implied by}\quad
1\in
\overline{
\operatorname{span}\{
\mathbf1_{C_p}:p\in\mathcal A_h
\}
}^{\,L^2}.
}
\]

The converse is not claimed.

## 8. Pair-correlation formulation

Write

\[
G_{pq}
=
\delta_{\{p,q\}}(h)
\]

for \(p\ne q\), and

\[
G_{pp}=\frac1{e_p}.
\]

Thus the whole finite \(L^2\) covering problem is encoded by:

1. local clock densities \(1/e_p\);
2. pairwise generalized-CRT compatibility;
3. gcd/lcm overlap geometry.

No higher-order intersections are required to compute the optimal linear-span bound \(B_P\).

This makes \(B_P\) substantially more scalable than full inclusion--exclusion.

## 9. Example: \(h=6\)

For the first five active channels

\[
P_5=\{5,7,11,13,19\},
\]

the equal-weight bound is

\[
\frac{3481}{4680}
\approx0.743803,
\]

while the optimal \(L^2\) bound is

\[
\boxed{
B_{P_5}
=
\frac{57}{73}
\approx0.780822.
}
\]

For the first ten active channels

\[
P_{10}=
\{5,7,11,13,19,23,29,37,47,53\},
\]

\[
B_{P_{10}}
=
\boxed{
\frac{62891}{78951}
}
\approx0.796583.
\]

For the first fifteen active channels through \(p=79\),

\[
\boxed{
B_{P_{15}}
=
\frac{1268391857255}{1516708968451}
\approx0.836278999.
}
\]

Hence

\[
\boxed{
a_*(6)
\le
1-B_{P_{15}}
=
\frac{248317111196}{1516708968451}
\approx0.1637210015.
}
\]

This \(L^2\) bound is weaker than the exact finite-prefix inclusion--exclusion value

\[
a_{15}(6)=\frac{252}{3335}\approx0.0755622,
\]

but it uses only pairwise phase geometry and scales polynomially in the number of channels once the Gram matrix is known.

## 10. Stronger pairwise sufficient criterion — OP-D140

Define

\[
S_N=\sum_{p\in P_N}\frac1{e_p}
\]

and

\[
Q_N
=
\sum_{p,q\in P_N}G_{pq}
=
\mathbb E X_N^2.
\]

The equal-weight theorem gives

\[
m(U_{P_N})
\ge
\frac{S_N^2}{Q_N}.
\]

Therefore

\[
\boxed{
\frac{S_N^2}{Q_N}\to1
\quad\Longrightarrow\quad
a_*(h)=0.
}
\]

This is a purely pair-correlation phase-covering criterion.

A stronger criterion is

\[
\boxed{
B_{P_N}=d_N^\top G_N^+d_N\to1.
}
\]

Neither limit is proved here.

## 11. Prior-art boundary

The Hilbert-space projection identity, Gram matrices, Cauchy--Schwarz/second-moment bounds, and Moore--Penrose optimization are standard functional analysis and probability.

The ARPL-specific content is the exact arithmetic Gram kernel

\[
G_{pq}
=
m(C_p\cap C_q)
\]

generated by multiplicative-order clocks and generalized-CRT phase compatibility, and its use as a computable criterion for the lower-edge atom.

## 12. Current status

Closed:

- exact finite Gram kernel;
- arbitrary-weight covering inequality;
- optimal finite \(L^2\) projection bound;
- monotonicity under channel refinement;
- pairwise sufficient criteria for lower-edge atom removal.

Open:

\[
\boxed{
B_N\stackrel{?}{\longrightarrow}1
}
\]

and

\[
\boxed{
a_*(h)\stackrel{?}{=}0.
}
\]
