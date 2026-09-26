# ARPL Phase-Survival Product and Hazard Law v0.1

Status: exact finite refinement theorem + exact infinite-product criterion for the lower-edge atom.

## 1. Avoidance sets

Fix admissible

\[
h\ge6,\qquad 6\mid h.
\]

Enumerate the active channels as

\[
p_1,p_2,\dots
\]

in any fixed order.

Let

\[
C_j=C_{p_j}
\]

be the active hit cylinder, and define

\[
A_N
=
\bigcap_{j=1}^N C_j^c.
\]

Its Haar mass is the exact finite lower-edge avoidance probability

\[
a_N(h)=m(A_N).
\]

Set

\[
A_0=K_h,
\qquad
a_0=1.
\]

Then

\[
A_{N+1}\subseteq A_N
\]

and

\[
a_N\downarrow a_*(h),
\]

where \(a_*(h)\) is the exact lower-edge atom mass.

## 2. Conditional phase-hit hazard — OP-D141

Whenever

\[
a_N>0,
\]

define

\[
\boxed{
\eta_N(h)
=
\frac{
m(A_N\cap C_{N+1})
}{
m(A_N)
}.
}
\]

Thus \(\eta_N\) is the conditional probability that the next active phase cylinder fires, given that all previous channels have been avoided.

Since

\[
A_{N+1}
=
A_N\setminus C_{N+1},
\]

we obtain

\[
a_{N+1}
=
a_N-
m(A_N\cap C_{N+1})
\]

and hence

\[
\boxed{
a_{N+1}
=
a_N(1-\eta_N).
}
\]

Equivalently,

\[
\boxed{
\eta_N
=
1-\frac{a_{N+1}}{a_N}.
}
\]

If \(a_N=0\) for some finite \(N\), then the lower-edge atom is already zero and the infinite problem is closed.

## 3. Exact survival product — OP-D142

Iterating OP-D141 gives

\[
\boxed{
a_N
=
\prod_{j=0}^{N-1}(1-\eta_j).
}
\]

Taking \(N\to\infty\),

\[
\boxed{
a_*(h)
=
\prod_{j=0}^{\infty}(1-\eta_j(h)).
}
\]

Therefore the lower-edge atom problem is exactly an infinite survival-product problem on the phase-refinement tower.

No independence hypothesis is involved.

## 4. Refinement geometry of one new channel

At stage \(N\), let

\[
L_N=\operatorname{lcm}(e_{p_1},\dots,e_{p_N}).
\]

For the next channel write

\[
e=e_{p_{N+1}},
\]

\[
g_N=\gcd(e,L_N),
\]

and

\[
\boxed{
b_N
=
\frac{e}{g_N}
=
\frac{L_{N+1}}{L_N}.
}
\]

Every level-\(N\) phase cell has exactly \(b_N\) lifts to level \(N+1\).

Let the new target phase be

\[
\rho=\rho_{p_{N+1}}(h)\pmod e.
\]

Fix a parent cell

\[
r\pmod{L_N}.
\]

The congruence system

\[
x\equiv r\pmod{L_N},
\qquad
x\equiv\rho\pmod e
\]

is solvable iff

\[
\boxed{
r\equiv\rho\pmod{g_N}.
}
\]

If solvable, exactly one of the \(b_N\) lifts of that parent cell lies in the new hit cylinder.

## 5. Compatibility fraction — OP-D143

Condition Haar measure on the surviving set \(A_N\).

Among surviving level-\(N\) parent cells, let

\[
c_N(h)
\]

be the conditional fraction satisfying

\[
r\equiv\rho_{p_{N+1}}(h)
\pmod{g_N}.
\]

Then

\[
0\le c_N\le1.
\]

For every compatible parent, exactly one of its \(b_N\) equiprobable children is removed.

Therefore

\[
\boxed{
\eta_N
=
\frac{c_N}{b_N}.
}
\]

Hence

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

This separates the next-channel effect into two independent pieces:

1. clock novelty / branching
   \[
   b_N;
   \]
2. surviving-phase compatibility
   \[
   c_N.
   \]

A channel can therefore be inactive at the survival level for two distinct reasons:

- \(c_N=0\): its phase is incompatible with every currently surviving parent;
- or its removal fraction \(c_N/b_N\) is small because the refinement factor is large.

## 6. Exact infinite-product criterion — OP-D144

Assume no finite prefix has \(a_N=0\).

Since

\[
0\le\eta_N<1,
\]

the standard infinite-product criterion gives

\[
\boxed{
a_*(h)>0
\iff
\sum_{N=0}^{\infty}
-\log(1-\eta_N)
<\infty.
}
\]

Equivalently,

\[
\boxed{
a_*(h)=0
\iff
\sum_{N=0}^{\infty}
-\log(1-\eta_N)
=\infty.
}
\]

Using \(\eta_N=c_N/b_N\),

\[
\boxed{
a_*(h)=0
\iff
\sum_N
-\log\left(
1-\frac{c_N}{b_N}
\right)
=\infty.
}
\]

Thus the atom problem has been reduced exactly to a scalar hazard series.

## 7. Small-hazard criterion — OP-D145

If

\[
\eta_N\le\frac12
\]

for all sufficiently large \(N\), then

\[
\eta_N
\le
-\log(1-\eta_N)
\le
2\eta_N.
\]

Therefore

\[
\boxed{
a_*(h)=0
\iff
\sum_N\eta_N=\infty
}
\]

under the eventual small-hazard condition.

In terms of refinement geometry,

\[
\boxed{
a_*(h)=0
\iff
\sum_N\frac{c_N}{b_N}=\infty
}
\]

whenever \(c_N/b_N\le1/2\) eventually.

## 8. Positive-atom sufficient criterion — OP-D146

Suppose:

1. no finite prefix covers the whole phase hull;
2. \(\eta_N<1\) for every \(N\);
3. the hazard series converges:
   \[
   \sum_N\eta_N<\infty.
   \]

Then

\[
\sum_N-\log(1-\eta_N)<\infty
\]

and therefore

\[
\boxed{
a_*(h)>0.
}
\]

A crude sufficient condition is

\[
\sum_N\frac1{b_N}<\infty,
\]

because

\[
0\le\eta_N=\frac{c_N}{b_N}\le\frac1{b_N}.
\]

This crude criterion is often useless when \(b_N=1\) infinitely often, but it shows explicitly that rapid clock refinement can preserve a positive avoidance mass.

## 9. Zero-atom sufficient criterion from fully compatible refinements — OP-D147

Let

\[
\mathcal F
=
\{N:c_N=1\}
\]

be the set of stages at which **every** surviving parent is compatible with the new phase modulo \(g_N\).

At such a stage,

\[
\eta_N=\frac1{b_N}.
\]

Therefore, if

\[
\boxed{
\sum_{N\in\mathcal F}\frac1{b_N}
=\infty,
}
\]

then

\[
\sum_N\eta_N=\infty
\]

and hence

\[
\boxed{
a_*(h)=0.
}
\]

This gives a deterministic phase-refinement route to removing the lower-edge atom.

## 10. Clock-redundant channels can still remove mass

If

\[
b_N=1,
\]

the new channel adds no new clock resolution.

Nevertheless,

\[
\eta_N=c_N
\]

can be strictly positive.

Therefore

\[
\boxed{
\text{clock redundancy does not imply observable redundancy}.
}
\]

A channel with no new denominator/frequency resolution can still remove a positive fraction of the surviving phase states by imposing a new target class on the already existing clock.

This distinction is essential in the ARPL refinement graph.

## 11. Exact \(h=6\) hazard example

For the first fifteen active channels

\[
5,7,11,13,19,23,29,37,47,53,59,61,67,71,79,
\]

the refinement factors are

\[
2,3,5,1,3,11,7,1,23,13,29,1,1,1,1.
\]

The exact hazards are

\[
\boxed{
\frac12,\,
\frac13,\,
\frac15,\,
\frac12,\,
0,\,
\frac1{11},\,
0,\,
0,\,
\frac1{23},\,
0,\,
\frac1{29},\,
\frac14,\,
\frac1{10},\,
0,\,
0.
}
\]

The corresponding compatibility fractions

\[
c_N=b_N\eta_N
\]

are

\[
\boxed{
1,\,
1,\,
1,\,
\frac12,\,
0,\,
1,\,
0,\,
0,\,
1,\,
0,\,
1,\,
\frac14,\,
\frac1{10},\,
0,\,
0.
}
\]

Their survival product is

\[
\prod_{N=0}^{14}(1-\eta_N)
=
\boxed{
\frac{252}{3335}
},
\]

recovering the exact finite lower-edge mass.

This illustrates all three mechanisms:

- full-compatible refinements \(c_N=1\);
- partial-compatible clock-redundant channels \(b_N=1\), \(0<c_N<1\);
- completely redundant-at-survival channels \(c_N=0\).

## 12. Relation to the negative-moment criterion

The same atom mass also satisfies

\[
a_*(h)
=
\lim_{t\to\infty}
A(h)^t\mathcal M_h(-t).
\]

Therefore the phase-survival product and far-negative Mellin/Laplace asymptotic are two exact representations of the same object:

\[
\boxed{
\prod_N
\left(
1-\frac{c_N}{b_N}
\right)
=
\lim_{t\to\infty}
A(h)^t\mathcal M_h(-t).
}
\]

This provides a bridge between the refinement graph and the analytic transform.

## 13. Current hard gate

The lower-edge problem is now reduced to estimating

\[
\boxed{
\eta_N=\frac{c_N}{b_N}.
}
\]

To prove atomlessness it is sufficient to prove divergence of the hazard series.

To prove a positive lower-edge atom it is sufficient to prove convergence.

The difficulty is no longer existence of the limiting law, nor source-hull geometry, nor finite CRT compatibility.

It is the asymptotic arithmetic of the **conditional compatibility sequence**

\[
c_N(h)
\]

relative to clock novelty

\[
b_N(h).
\]

## 14. Prior-art boundary

Conditional survival products, hazard decompositions, and infinite-product criteria are standard probability/analysis.

The ARPL-specific content is the exact arithmetic identity

\[
\eta_N=\frac{c_N}{b_N}
\]

on the multiplicative-order phase-refinement tower.

No novelty claim is made for general hazard theory.
