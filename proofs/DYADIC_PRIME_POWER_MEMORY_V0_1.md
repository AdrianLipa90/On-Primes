# Dyadic Decomposition of the Prime-Power Memory v0.1

Define the finite prime-power measure on logarithmic time by
\[
d\mu(u)
=
\sum_{p}\sum_{m\ge1}
(\log p)p^{-m/2}\,\delta_{m\log p}(u).
\]

For every finite \(t\), only prime powers \(p^m\le e^t\) contribute to
\[
\mathcal M(t)
=
\int_0^t(t-u)\,d\mu(u)
=
\sum_{m\log p\le t}
(\log p)p^{-m/2}(t-m\log p).
\]
Hence this expression is finite and requires no Euler-product continuation.

For each base prime write
\[
p+1=a_p2^{k_p},
\qquad
\delta_p=\log(1+1/p),
\]
so that
\[
\log p=\log a_p+k_p\log2-\delta_p.
\]

## Theorem — exact memory decomposition

Define
\[
\mathcal M_K(t)=
\sum_{m\log p\le t}
k_p\,p^{-m/2}(t-m\log p),
\]
\[
\mathcal M_A(t)=
\sum_{m\log p\le t}
(\log a_p)p^{-m/2}(t-m\log p),
\]
and
\[
\mathcal M_D(t)=
\sum_{m\log p\le t}
\delta_p\,p^{-m/2}(t-m\log p).
\]
Then for every finite \(t\ge0\),
\[
\boxed{
\mathcal M(t)
=
(\log2)\mathcal M_K(t)
+\mathcal M_A(t)
-\mathcal M_D(t).
}
\]

**Proof.** The sum is finite. Substitute the exact identity for \(\log p\) into every event weight and collect the three linear contributions. \(\square\)

## Why this matters for the RH programme

This identity transports the dyadic decomposition to the real prime-power measure used by explicit-formula / Suzuki-style memory terms without evaluating the Euler product in the critical strip.

It does **not** prove positivity of a Suzuki function. To affect RH, one must combine this arithmetic memory with the exact archimedean term of a valid RH-equivalent criterion and establish a new global sign/cancellation inequality.

## Immediate target

Study whether the three components have individually controllable signs or whether useful cancellation occurs specifically between
\[
(\log2)\mathcal M_K
\quad\text{and}\quad
\mathcal M_A-\mathcal M_D.
\]
The identity itself is exact; any claimed inequality is currently `OPEN`.
