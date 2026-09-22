# Exact Dyadic Shells v0.1

For an odd prime \(p\), let
\[
k=v_2(p+1)\ge1.
\]

## Theorem — exact shell congruence

\[
\boxed{
v_2(p+1)=k
\iff
p\equiv2^k-1\pmod{2^{k+1}}.
}
\]

**Proof.** The condition \(v_2(p+1)=k\) means
\[
p+1=2^k u
\]
with \(u\) odd. Hence \(u=2r+1\) for some integer \(r\), so
\[
p=2^k(2r+1)-1
=(2^k-1)+r2^{k+1},
\]
which is the stated congruence. Conversely that congruence implies
\[
p+1=2^k(1+2r)
\]
with odd second factor, so the 2-adic valuation is exactly \(k\). \(\square\)

## Boundary

The prime \(2\) is the unique prime with \(k=0\). Every odd prime belongs to exactly one shell \(k\ge1\).

Thus the prime set has the disjoint partition
\[
\mathbb P
=
\{2\}
\sqcup
\bigsqcup_{k\ge1}
\{p\in\mathbb P:p\equiv2^k-1\pmod{2^{k+1}}\}.
\]

## Relation to the residue tower

The nested condition
\[
p\equiv-1\pmod{2^j}
\]
means \(v_2(p+1)\ge j\), while the shell condition selects the exact valuation. Therefore
\[
\{k_p\ge j\}
=
\bigsqcup_{k\ge j}\{k_p=k\}.
\]

## Standard distribution heuristic/theorem interface

For each fixed \(k\), the shell is a reduced residue class modulo \(2^{k+1}\). Dirichlet's theorem and the prime number theorem in arithmetic progressions govern its asymptotic prime count. This repository does not claim those classical results as new, nor does this theorem alone provide uniform control when \(k\) grows with the cutoff.
