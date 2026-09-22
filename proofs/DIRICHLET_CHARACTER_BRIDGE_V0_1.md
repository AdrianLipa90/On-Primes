# Dirichlet Character Bridge for the Dyadic Residue Tower v0.1

Fix
\[
q=2^j,\qquad j\ge1.
\]
For odd integers \(n\), Dirichlet-character orthogonality on \((\mathbb Z/q\mathbb Z)^\times\) gives
\[
\boxed{
\mathbf 1_{\{n\equiv-1\pmod q\}}
=
\frac1{\varphi(q)}
\sum_{\chi\ (\mathrm{mod}\ q)}
\overline{\chi(-1)}\chi(n).
}
\]

## Theorem 1 — character decomposition of one dyadic tower level

For \(\Re(s)>1\), define
\[
K_j(s)=
\sum_{p\equiv-1\ (\mathrm{mod}\ 2^j)}
\frac1{p^s-1}
\]
and
\[
\Pi_\chi(s)=\sum_p\frac{\chi(p)}{p^s-1}.
\]
Then
\[
\boxed{
K_j(s)
=
\frac1{\varphi(2^j)}
\sum_{\chi\ (\mathrm{mod}\ 2^j)}
\overline{\chi(-1)}\Pi_\chi(s).
}
\]

**Proof.** Insert the character-orthogonality identity into the prime sum. Absolute convergence for \(\Re(s)>1\) permits the finite character sum and prime sum to be interchanged. The prime \(2\) contributes zero to all characters modulo \(2^j\), and it is not in the residue class \(-1\pmod{2^j}\). \(\square\)

## Corollary 1.1 — character decomposition of the full dyadic moment

Since
\[
K(s)=\sum_{j\ge1}K_j(s),
\]
we obtain
\[
\boxed{
K(s)=
\sum_{j\ge1}
\frac1{\varphi(2^j)}
\sum_{\chi\ (\mathrm{mod}\ 2^j)}
\overline{\chi(-1)}\Pi_\chi(s).
}
\]

Thus the exact coefficient of \(\log2\) in the prime-log decomposition is a hierarchy of character-weighted prime sums over moduli \(2,4,8,\dots\).

## Theorem 2 — connection to generalized prime-zeta sums

Define
\[
P_\chi(s)=\sum_p\frac{\chi(p)}{p^s}.
\]
For \(\Re(s)>1\),
\[
\boxed{
\Pi_\chi(s)=\sum_{m\ge1}P_\chi(ms),
}
\]
because
\[
\frac1{p^s-1}=\sum_{m\ge1}p^{-ms}.
\]

Moreover the standard Euler product for a Dirichlet \(L\)-function gives
\[
\log L(s,\chi)
=
\sum_{r\ge1}\frac1r P_{\chi^r}(rs).
\]
By Möbius inversion,
\[
\boxed{
P_\chi(s)
=
\sum_{r\ge1}\frac{\mu(r)}{r}
\log L(rs,\chi^r),
}
\]
in the half-plane of absolute convergence, with a consistent logarithm branch inherited from the Euler product.

## Research boundary

This provides an exact bridge from the dyadic fibre coordinate to classical Dirichlet-character and Dirichlet-\(L\) objects for \(\Re(s)>1\). Analytic continuation toward the critical strip is not supplied by these algebraic identities and remains a separate problem.
