# Prime-Power Memory Sign and Defect Bounds v0.1

For a prime \(p\), write
\[
p+1=a_p2^{k_p},
\qquad
\delta_p=\log(1+1/p).
\]

At a prime-power event \(p^m\le e^t\), define the nonnegative triangular kernel
\[
W_{p,m}(t)=p^{-m/2}(t-m\log p)\ge0.
\]

## Lemma 1 — component signs

Because \(k_p\ge0\), \(a_p\ge1\), \(\delta_p>0\), and \(W_{p,m}(t)\ge0\),
\[
\mathcal M_K(t)\ge0,
\qquad
\mathcal M_A(t)\ge0,
\qquad
\mathcal M_D(t)\ge0.
\]

## Lemma 2 — defect bound

For every prime \(p\),
\[
0<\delta_p=\log(1+1/p)<\frac1p.
\]

Therefore
\[
0<\mathcal M_D(t)
<
\sum_{m\log p\le t}
p^{-m/2-1}(t-m\log p)
\]
whenever at least one event contributes.

## Lemma 3 — interior dyadic reserve

For every odd prime \(p\),
\[
k_p=v_2(p+1)\ge1
\]
and
\[
\delta_p\le\log(4/3).
\]
Hence
\[
\boxed{
k_p\log2-\delta_p
\ge
\log2-\log(4/3)
=
\log(3/2)>0.
}
\]

Consequently, if the sum is restricted to odd base primes,
\[
\boxed{
(\log2)\mathcal M_K^{\mathrm{odd}}(t)
-\mathcal M_D^{\mathrm{odd}}(t)
\ge
\log(3/2)
\sum_{\substack{p\ge3,\ m\ge1\\m\log p\le t}}
W_{p,m}(t).
}
\]

## Boundary event

For \(p=2\), \((a,k)=(3,0)\), so
\[
\log a-\delta_2
=
\log3-\log(3/2)
=
\log2.
\]
Thus the unique even-prime boundary is handled by the label-minus-defect sector rather than the dyadic-moment sector.

## RH relevance

These are rigorous sign/bound statements for the arithmetic memory components. They do not by themselves establish the sign of an RH-equivalent Suzuki/Weil functional, because the prime-power memory enters together with an archimedean term whose global competition must still be controlled.
