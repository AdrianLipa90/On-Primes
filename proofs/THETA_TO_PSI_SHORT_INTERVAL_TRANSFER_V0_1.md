# Theta-to-Psi Short-Interval Transfer v0.1

Status: **ELEMENTARY_TRANSFER / STANDARD_THETA_INPUT_COMPATIBILITY**

Date: 2026-09-26

Purpose: the unconditional Saffari--Vaughan/Huxley short-interval mean-square estimate is naturally stated for the Chebyshev prime sum
\[
\vartheta(x)=\sum_{p\le x}\log p,
\]
while the phase-bank and shifted-correlation stack uses
\[
\psi(x)=\sum_{n\le x}\Lambda(n).
\]
This note supplies the missing prime-power transfer explicitly.

## 1. Prime-power remainder

Define
\[
D(x)=\psi(x)-\vartheta(x)
=\sum_{\substack{p^k\le x\\k\ge2}}\log p.
\]

Fix \(X\ge2\), \(x\in[X,2X]\), and \(1\le h\le X\). Then
\[
D(x+h)-D(x)
=
\sum_{k\ge2}
\sum_{x<p^k\le x+h}\log p.
\]

For squares,
\[
\#\{m:x<m^2\le x+h\}
\le
\sqrt{x+h}-\sqrt{x}+1
\ll
hX^{-1/2}+1.
\]
Hence the square contribution is
\[
O\!\left((hX^{-1/2}+1)\log X\right).
\]

For \(k\ge3\), the number of possible integer bases at a fixed exponent is
\[
O\!\left(hX^{1/k-1}+1\right)
\subset
O\!\left(hX^{-2/3}+1\right).
\]
There are \(O(\log X)\) admissible exponents and each weight is \(O(\log X)\). Therefore
\[
\sum_{k\ge3}\sum_{x<p^k\le x+h}\log p
=
O\!\left(
hX^{-2/3}\log^2X+\log^2X
\right).
\]

Combining both parts,
\[
\boxed{
D(x+h)-D(x)
=
O\!\left(
hX^{-1/2}\log^2X+\log^2X
\right).
}
\]

## 2. Uniform negligibility in the \(X^{1/6+\varepsilon}\) range

If
\[
h\ge X^{1/6+\varepsilon},
\]
then
\[
\frac{|D(x+h)-D(x)|}{h}
\ll
X^{-1/2}\log^2X
+
X^{-1/6-\varepsilon}\log^2X
\to0
\]
uniformly for \(x\in[X,2X]\).

Thus
\[
\boxed{
D(x+h)-D(x)=o(h)
}
\]
uniformly in the declared range.

## 3. Mean-square transfer

Write
\[
E_\vartheta(x,h)
=
\vartheta(x+h)-\vartheta(x)-h,
\]
\[
E_\psi(x,h)
=
\psi(x+h)-\psi(x)-h.
\]

Then
\[
E_\psi(x,h)
=
E_\vartheta(x,h)
+
D(x+h)-D(x).
\]

Suppose the standard unconditional prime short-interval input gives
\[
\int_X^{2X}|E_\vartheta(x,h)|^2\,dx
=
o(Xh^2)
\]
uniformly in a range containing
\[
h\ge X^{1/6+\varepsilon}.
\]

By Section 2,
\[
\int_X^{2X}|D(x+h)-D(x)|^2\,dx
=
o(Xh^2).
\]

Cauchy--Schwarz controls the cross term, so
\[
\boxed{
\int_X^{2X}
|\psi(x+h)-\psi(x)-h|^2\,dx
=
o(Xh^2).
}
\]

Therefore the \(\vartheta\)-based Saffari--Vaughan/Huxley mean-square estimate transfers to the \(\psi\)-based von Mangoldt observable used in the phase-spectroscopy stack.

## 4. Prior-art boundary

The short-interval mean-square theorem for primes is standard external input. The relevant classical source is Saffari--Vaughan, with the \(1/6\) threshold tied to the classical zero-density input; later literature states the \(h\ge X^{1/6}(\log X)^B\) form explicitly.

This note claims no new prime-distribution theorem. Its role is bookkeeping: it prevents the repository from silently identifying a \(\vartheta\)-statement with a \(\psi\)-statement.

## 5. Compact lemma

### Lemma -- theta-to-psi short-interval transfer

For \(x\in[X,2X]\) and \(1\le h\le X\),
\[
\boxed{
[(\psi-\vartheta)(x+h)-(\psi-\vartheta)(x)]
=
O\!\left(
hX^{-1/2}\log^2X+\log^2X
\right).
}
\]

Consequently, for every fixed \(\varepsilon>0\), any uniform estimate
\[
\int_X^{2X}
|\vartheta(x+h)-\vartheta(x)-h|^2dx
=
o(Xh^2)
\]
valid for \(h\ge X^{1/6+\varepsilon}\) transfers to
\[
\boxed{
\int_X^{2X}
|\psi(x+h)-\psi(x)-h|^2dx
=
o(Xh^2)
}
\]
in the same range. Q.E.D.
