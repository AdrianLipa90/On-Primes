# Dyadic Log-Moment Decomposition v0.1

For every prime \(p\), write its unique dyadic address as
\[
p+1=a_p2^{k_p},
\qquad a_p\ \text{odd},
\qquad k_p=v_2(p+1).
\]

Define the positive defect
\[
\delta_p=\log\left(1+\frac1p\right).
\]

## Theorem 1 — exact three-term prime-log identity

\[
\boxed{
\log p
=
\log a_p
+k_p\log2
-\delta_p
}
\]

**Proof.** Since \(p+1=a_p2^{k_p}\),
\[
\log p
=\log(p+1)-\log\frac{p+1}{p}
=\log a_p+k_p\log2-\log(1+1/p).
\]
\(\square\)

## Theorem 2 — finite dyadic moment decomposition

For every finite prime cutoff \(P\), define
\[
K_P(s)=\sum_{p\le P}\frac{k_p}{p^s-1},
\]
\[
A_P(s)=\sum_{p\le P}\frac{\log a_p}{p^s-1},
\]
and
\[
D_P(s)=\sum_{p\le P}\frac{\delta_p}{p^s-1}.
\]
Then exactly
\[
\boxed{
\sum_{p\le P}\frac{\log p}{p^s-1}
=
(\log2)K_P(s)+A_P(s)-D_P(s).
}
\]

**Proof.** Substitute Theorem 1 term by term. \(\square\)

## Theorem 3 — infinite decomposition for Re(s) > 1

For \(\Re(s)>1\), all three series converge absolutely and
\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
(\log2)K(s)+A(s)-D(s),
}
\]
where \(K,A,D\) are the corresponding infinite prime sums.

For the defect term, \(0<\delta_p=\log(1+1/p)<1/p\), so its summand is smaller by an additional factor of roughly \(1/p\) relative to the usual prime-side term. For the other two terms, \(k_p\log2\le\log(p+1)\) and \(\log a_p\le\log(p+1)\), which gives convergence from the standard \((\log p)p^{-\sigma}\) comparison.

## Interpretation firewall

This decomposition shows that \(\log2\) multiplies an exact arithmetic observable
\[
K(s)=\sum_p\frac{v_2(p+1)}{p^s-1}.
\]
It does **not** show that this moment controls zeta zeros, nor does it establish a critical-line theorem. That is a separate open question.
