# ARPL Phase-Survival Tree and Canonical Codimension v0.1

Status: exact combinatorial realization of the lower-edge avoidance process inside the canonical ARPL ultrametric phase graph.

## 1. Surviving phase cells

Fix the ordered active channels

\[
p_1,p_2,\dots
\]

and let

\[
L_N=\operatorname{lcm}(e_{p_1},\dots,e_{p_N}).
\]

The finite level-\(N\) phase clock has exactly

\[
L_N
\]

cells.

Let

\[
A_N
=
\bigcap_{j=1}^N C_{p_j}^c
\]

be the phase states that avoid the first \(N\) hit cylinders, and define

\[
a_N=m(A_N).
\]

Since \(A_N\) is a union of level-\(N\) residue cylinders, the number of surviving cells is

\[
\boxed{
S_N
=
a_NL_N
\in\mathbb Z_{\ge0}.
}
\]

Thus the finite lower-edge avoidance mass has the exact combinatorial form

\[
\boxed{
a_N=\frac{S_N}{L_N}.
}
\]

## 2. Branch-and-prune recursion — OP-D155

At the next channel, let

\[
b_N=\frac{L_{N+1}}{L_N}
\]

be the refinement branching factor.

Before imposing the new phase cylinder, every one of the \(S_N\) surviving parent cells has \(b_N\) children, giving

\[
b_NS_N
\]

candidate children.

Let

\[
C_N
\]

be the number of surviving parent cells whose residue is compatible with the new target phase modulo

\[
g_N=\gcd(e_{p_{N+1}},L_N).
\]

Every compatible parent loses exactly one child; every incompatible parent loses none.

Therefore

\[
\boxed{
S_{N+1}
=
b_NS_N-C_N.
}
\]

Writing

\[
c_N=\frac{C_N}{S_N},
\]

this becomes

\[
\boxed{
S_{N+1}
=
S_N(b_N-c_N).
}
\]

Dividing by

\[
L_{N+1}=b_NL_N
\]

recovers the hazard law

\[
\boxed{
a_{N+1}
=
a_N
\left(
1-\frac{c_N}{b_N}
\right).
}
\]

Thus the exact finite graph dynamics is:

\[
\boxed{
\text{branch by }b_N
\quad\longrightarrow\quad
\text{prune }C_N\text{ children}.
}
\]

## 3. Canonical finite phase dimension — OP-D156

At canonical metric scale

\[
\varepsilon_N=\frac1{L_N},
\]

the finite survivor approximation \(A_N\) consists of \(S_N\) disjoint phase cylinders.

Define its finite resolution exponent

\[
\boxed{
D_N^{\rm surv}
=
\frac{\log S_N}{\log L_N}
}
\]

whenever

\[
L_N>1,\qquad S_N>0.
\]

Using \(S_N=a_NL_N\),

\[
\boxed{
D_N^{\rm surv}
=
1+
\frac{\log a_N}{\log L_N}.
}
\]

Equivalently, define the finite phase codimension

\[
\boxed{
\Delta_N
=
1-D_N^{\rm surv}
=
\frac{-\log a_N}{\log L_N}.
}
\]

Because

\[
1\le S_N\le L_N
\]

whenever the finite avoidance set is nonempty,

\[
\boxed{
0\le D_N^{\rm surv}\le1,
\qquad
0\le\Delta_N\le1.
}
\]

## 4. Codimension as accumulated hazard — OP-D157

From the exact survival product,

\[
-\log a_N
=
\sum_{j=0}^{N-1}
-\log(1-\eta_j).
\]

Therefore

\[
\boxed{
\Delta_N
=
\frac{
\sum_{j<N}
-\log(1-\eta_j)
}{
\log L_N
}.
}
\]

Using

\[
\eta_j=\frac{c_j}{b_j},
\]

we obtain

\[
\boxed{
\Delta_N
=
\frac{
\sum_{j<N}
-\log\left(1-\frac{c_j}{b_j}\right)
}{
\sum_{j<N}\log b_j
},
}
\]

where zero-refinement stages \(b_j=1\) contribute zero to the denominator but can contribute positive pruning to the numerator.

Hence the canonical phase codimension compares:

\[
\boxed{
\text{accumulated pruning information}
\quad\text{vs}\quad
\text{accumulated clock-resolution information}.
}
\]

## 5. Infinite avoidance set and box-dimension bound — OP-D158

Let

\[
A_\infty
=
\bigcap_{N\ge1}A_N
\]

be the full lower-edge phase-avoidance set.

Since

\[
A_\infty\subseteq A_N,
\]

it can be covered at scale \(1/L_N\) by at most \(S_N\) canonical cylinders.

Therefore

\[
N(A_\infty,1/L_N)
\le
S_N.
\]

It follows that

\[
\boxed{
\overline{\dim}_{\rm B}(A_\infty)
\le
\limsup_{N\to\infty}
\frac{\log S_N}{\log L_N}.
}
\]

Since

\[
\frac{\log S_N}{\log L_N}
=
1-
\frac{-\log a_N}{\log L_N},
\]

we get

\[
\boxed{
\overline{\dim}_{\rm B}(A_\infty)
\le
1-
\liminf_{N\to\infty}
\frac{-\log a_N}{\log L_N}.
}
\]

The right-hand side is clipped at \(0\) if necessary.

## 6. Hausdorff-dimension upper bound — OP-D159

The same finite cylinders give, for \(s>0\),

\[
\mathcal H^s_{1/L_N}(A_\infty)
\le
S_NL_N^{-s}
=
a_NL_N^{1-s}.
\]

Define

\[
\Delta_*
=
\liminf_{N\to\infty}
\frac{-\log a_N}{\log L_N}.
\]

If

\[
s>1-\Delta_*,
\]

then along a subsequence realizing the liminf,

\[
a_NL_N^{1-s}\to0.
\]

Hence

\[
\boxed{
\dim_H(A_\infty)
\le
\max\{0,1-\Delta_*\}.
}
\]

Thus polynomial-scale decay

\[
a_N\lesssim L_N^{-\delta}
\]

forces phase codimension at least \(\delta\).

## 7. Positive lower-edge atom implies full phase dimension

If

\[
a_*(h)>0,
\]

then \(A_\infty\) has positive Haar measure.

By the canonical \(1\)-Ahlfors regularity theorem,

\[
\boxed{
\dim_H(A_\infty)=1.
}
\]

Equivalently,

\[
a_*(h)>0
\quad\Longrightarrow\quad
\Delta_*=0.
\]

The converse is false in general: a zero-measure set can still have full Hausdorff dimension.

Therefore

\[
\boxed{
a_*(h)=0
}
\]

and

\[
\boxed{
\dim_H(A_\infty)<1
}
\]

are distinct questions.

## 8. A genuinely fractal zero-atom regime

If one proves both

\[
a_N\to0
\]

and

\[
\Delta_*>0,
\]

then the lower-edge avoidance phase set has:

- zero Haar measure;
- strictly smaller Hausdorff dimension than the full phase hull.

In that regime the avoidance set is a genuine lower-dimensional arithmetic fractal in the canonical ARPL ultrametric.

If instead

\[
a_N\to0
\]

but

\[
\Delta_*=0,
\]

then the avoidance set can remain full-dimensional despite having zero measure.

This distinction prevents conflating measure decay with dimension loss.

## 9. \(h=6\) finite diagnostics

For the active-channel ordering by increasing prime, exact calculations give:

\[
\begin{array}{c|c|c|c}
N & L_N & S_N & D_N^{\rm surv}\\
\hline
5
&
90
&
12
&
0.5522248\ldots
\\
10
&
2\,072\,070
&
240\,240
&
0.8518526\ldots
\\
15
&
60\,090\,030
&
4\,540\,536
&
0.8558010\ldots
\\
20
&
44\,395\,715\,964\,600
&
3\,022\,180\,761\,600
&
0.9144873\ldots
\\
25
&
1\,227\,053\,193\,545\,579\,400
&
80\,407\,676\,392\,243\,200
&
0.9345694\ldots
\end{array}
\]

These are finite-prefix diagnostics only.

They show that clock resolution is currently growing substantially faster than avoidance mass is shrinking.

They do not determine the limiting atom or Hausdorff dimension.

## 10. Structural synthesis

The phase-refinement graph now has three exact scalar layers:

### Resolution

\[
\log L_N
=
\sum_{j<N}\log b_j.
\]

### Survival

\[
-\log a_N
=
\sum_{j<N}
-\log\left(1-\frac{c_j}{b_j}\right).
\]

### Relative codimension

\[
\boxed{
\Delta_N
=
\frac{\text{survival cost}}{\text{resolution gain}}.
}
\]

This is the canonical metric form of the ARPL branch/prune geometry.

## 11. Boundary

The finite recursion and dimension upper bounds are proved.

Not proved:

- \(a_*(h)=0\);
- existence of \(\lim D_N^{\rm surv}\);
- equality between the finite-prefix exponent limit and the Hausdorff dimension of \(A_\infty\);
- a nontrivial lower bound on \(\dim_H(A_\infty)\) in the zero-mass case.

Any equality theorem requires additional regularity of the pruning process.
