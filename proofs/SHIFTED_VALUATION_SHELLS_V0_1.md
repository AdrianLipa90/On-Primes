# Shifted Prime-Adic Valuation Shells v0.1

Fix a prime \(r\) and an integer \(j\ge1\).

## Theorem 1 — exact residue-shell description

The condition
\[
v_r(p+1)=j
\]
is equivalent to
\[
p+1=r^j u,
\qquad r\nmid u.
\]
Writing \(u=c+rv\) with \(c\in\{1,\dots,r-1\}\), we obtain
\[
p\equiv cr^j-1\pmod{r^{j+1}}.
\]
Therefore
\[
\boxed{
v_r(p+1)=j
\iff
p\in\bigcup_{c=1}^{r-1}
\left(cr^j-1\pmod{r^{j+1}}\right).
}
\]

There are exactly \(r-1\) residue classes in the exact shell. Each is reduced modulo \(r^{j+1}\), because every representative is congruent to \(-1\pmod r\).

For \(r=2\), this collapses to the single dyadic class
\[
p\equiv2^j-1\pmod{2^{j+1}}.
\]

## Theorem 2 — fixed-shell asymptotic (standard consequence)

For fixed prime \(r\) and fixed \(j\ge1\), the prime number theorem in arithmetic progressions yields
\[
\#\{p\le x:v_r(p+1)=j\}
\sim
\frac{r-1}{\varphi(r^{j+1})}\operatorname{Li}(x).
\]
Since
\[
\varphi(r^{j+1})=r^j(r-1),
\]
we get
\[
\boxed{
\#\{p\le x:v_r(p+1)=j\}
\sim
\frac{\operatorname{Li}(x)}{r^j}.
}
\]

This is a classical consequence of PNT in arithmetic progressions, not a new prime-distribution theorem.

## Interpretation

For every fixed base-prime channel \(r\), the positive valuation shells have geometric fixed-shell weights
\[
r^{-1},r^{-2},r^{-3},\dots
\]
in the prime-counting asymptotic.

For \(r=2\), these sum to 1, reflecting that every odd prime has \(v_2(p+1)\ge1\).

For odd \(r\),
\[
\sum_{j\ge1}r^{-j}=\frac1{r-1},
\]
matching the asymptotic proportion of primes in the class \(-1\pmod r\).

## Uniformity firewall

The asymptotic above holds with \(r,j\) fixed while \(x\to\infty\). No uniform statement for growing \(r\) or \(j\) is claimed. Such uniformity belongs to deeper results on primes in arithmetic progressions (Siegel-Walfisz, Brun-Titchmarsh, Bombieri-Vinogradov and related theory).
