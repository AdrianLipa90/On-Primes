# Fixed-Channel Mean Valuation Theorem v0.1

Fix a prime \(r\). Define
\[
V_r(x)=\sum_{p\le x}v_r(p+1),
\]
where the sum is over primes \(p\).

Using
\[
v_r(p+1)=\sum_{j\ge1}\mathbf1_{\{r^j\mid p+1\}},
\]
we have the exact finite identity
\[
V_r(x)=\sum_{j\ge1}\pi(x;r^j,-1),
\]
where only \(j\le\log_r(x+1)\) can contribute.

## Theorem

For every fixed prime \(r\),
\[
\boxed{
V_r(x)
\sim
\frac{r}{(r-1)^2}\operatorname{Li}(x).
}
\]
Equivalently, since \(\pi(x)\sim\operatorname{Li}(x)\),
\[
\boxed{
\frac1{\pi(x)}\sum_{p\le x}v_r(p+1)
\longrightarrow
\frac{r}{(r-1)^2}.
}
\]

### Proof

Fix an integer \(J\ge1\). For each fixed \(j\le J\), the prime number theorem in arithmetic progressions gives
\[
\pi(x;r^j,-1)
\sim
\frac{\operatorname{Li}(x)}{\varphi(r^j)}.
\]
Hence
\[
\sum_{j\le J}\pi(x;r^j,-1)
=
\operatorname{Li}(x)
\sum_{j\le J}\frac1{\varphi(r^j)}
+o(\operatorname{Li}(x)).
\]

It remains to control the tail uniformly enough to let \(J\to\infty\). Split the tail at \(r^j\le\sqrt x\).

For \(r^j\le\sqrt x\), Brun-Titchmarsh gives, for large \(x\),
\[
\pi(x;r^j,-1)
\le
\frac{2x}{\varphi(r^j)\log(x/r^j)}
\le
\frac{4x}{\varphi(r^j)\log x}.
\]
Therefore
\[
\sum_{\substack{j>J\\r^j\le\sqrt x}}
\pi(x;r^j,-1)
\ll
\operatorname{Li}(x)
\sum_{j>J}\frac1{\varphi(r^j)}.
\]

For \(r^j>\sqrt x\), the number of integers at most \(x\) in one residue class modulo \(r^j\) is at most \(x/r^j+1\). Thus
\[
\sum_{r^j>\sqrt x}\pi(x;r^j,-1)
\ll
\sqrt x+\log x
=
o(\operatorname{Li}(x)).
\]

Now
\[
\sum_{j\ge1}\frac1{\varphi(r^j)}
=
\sum_{j\ge1}\frac1{r^{j-1}(r-1)}
=
\frac{r}{(r-1)^2}.
\]
Let first \(x\to\infty\) and then \(J\to\infty\). This proves the theorem. \(\square\)

## Corollary — mean logarithmic channel weight

For fixed prime \(r\),
\[
\boxed{
\frac1{\pi(x)}
\sum_{p\le x}v_r(p+1)\log r
\longrightarrow
\frac{r\log r}{(r-1)^2}.
}
\]

Examples of the limiting mean valuation:

\[
r=2:\ 2,
\qquad
r=3:\ \frac34,
\qquad
r=5:\ \frac5{16},
\qquad
r=7:\ \frac7{36}.
\]

## Scope firewall

The theorem is for each fixed base prime \(r\). It does not justify summing the asymptotic over all \(r\) without additional uniform estimates. The divergence of the aggregate channel weight is precisely what is needed to reconstruct the growth of \(\log(p+1)\), so global interchange requires separate analysis.
