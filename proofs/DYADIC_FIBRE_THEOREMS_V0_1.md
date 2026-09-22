# Dyadic Fibre Theorem Pack v0.1

## Definition 1 — dyadic address

For an integer \(n\ge1\), write
\[
n+1=a2^k
\]
with \(a\) odd and \(k\ge0\). Define the dyadic address of \(n\) as \((a,k)\).

### Theorem 1 — uniqueness

The dyadic address exists and is unique.

**Proof.** Let \(k=v_2(n+1)\). Then \(a=(n+1)/2^k\) is an odd positive integer. If \(n+1=b2^j\) with odd \(b\), then by uniqueness of the 2-adic valuation \(j=k\), hence \(b=a\). \(\square\)

## Definition 2 — fibre

For odd \(a\ge1\), define
\[
\mathcal F_a=\{x_{a,k}=a2^k-1:k\ge0\}.
\]

### Theorem 2 — exact affine shift

For \(T(x)=2x+1\),
\[
T(x_{a,k})=x_{a,k+1}.
\]

**Proof.**
\[
T(a2^k-1)=2a2^k-2+1=a2^{k+1}-1.
\]
\(\square\)

### Corollary 2.1 — conjugacy to doubling

For fixed odd \(a\), define
\[
C_a(x)=\frac{x+1}{a}.
\]
Then on \(\mathcal F_a\),
\[
C_a(Tx)=2C_a(x).
\]
Thus the affine dynamics inside each fibre is exactly conjugate to dyadic doubling.

## Theorem 3 — integer boundary prime

On the layer \(k=0\), the only prime is \(2\).

**Proof.** \(x_{a,0}=a-1\). Since \(a\) is odd, \(a-1\) is even. The only even prime is \(2\), forcing \(a=3\). \(\square\)

## Theorem 4 — half-boundary lemma

For
\[
x\in\frac12+\mathbb Z_{\ge0},
\]
one has
\[
T(x)\in\mathbb P\iff x=\frac12.
\]

**Proof.** Write \(x=n+\tfrac12\) with \(n\ge0\). Then
\[
T(x)=2n+2=2(n+1),
\]
which is even. It is prime exactly when it equals \(2\), i.e. when \(n=0\). \(\square\)

### Corollary 4.1

The unique half-integer predecessor of the unique prime on the \(k=0\) layer is
\[
T^{-1}(2)=\frac12.
\]
This is a boundary property of the affine map; it does not make \(1/2\) a prime number.

## Theorem 5 — exact logarithmic lattice

For every fibre element,
\[
\log(x_{a,k}+1)=\log a+k\log2.
\]

**Proof.** Since \(x_{a,k}+1=a2^k\), take logarithms. \(\square\)

## Theorem 6 — prime-log defect

For a prime \(p=x_{a,k}\), define
\[
\delta_p=\log\left(1+\frac1p\right)>0.
\]
Then
\[
\log p=\log a+k\log2-\delta_p.
\]

**Proof.** Since \(p+1=a2^k\),
\[
\log p=\log(p+1)-\log\frac{p+1}{p}
=\log a+k\log2-\log\left(1+\frac1p\right).
\]
\(\square\)

## Research boundary

These theorems establish a coordinate system and exact dynamics. They do not determine for which addresses \((a,k)\) the value \(a2^k-1\) is prime.
