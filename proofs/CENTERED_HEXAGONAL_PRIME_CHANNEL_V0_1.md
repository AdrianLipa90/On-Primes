# Centered-Hexagonal Prime Channel v0.1

Status: candidate theorem pack.

Define

\[
H_n = 1 + 3n(n+1)=3n^2+3n+1,\qquad n\ge 0.
\]

These are the centered hexagonal numbers with shell increments

\[
H_n-H_{n-1}=6n.
\]

## Theorem 1 — fixed residue class

For every integer \(n\ge0\),

\[
H_n\equiv 1\pmod 6.
\]

### Proof

The product \(n(n+1)\) is even, hence \(3n(n+1)\) is divisible by 6. Therefore

\[
H_n=1+3n(n+1)\equiv1\pmod6.
\]

## Theorem 2 — prime-divisor channel

If a prime \(q\) divides \(H_n\), then

\[
q\equiv1\pmod6.
\]

### Proof

First, \(H_n\) is odd, so \(q\ne2\). Also \(H_n\equiv1\pmod3\), so \(q\ne3\).

Assume therefore \(q>3\) and \(q\mid H_n\). The identity

\[
(6n+3)^2=12H_n-3
\]

gives

\[
(6n+3)^2\equiv-3\pmod q.
\]

Hence \(-3\) is a quadratic residue modulo \(q\). By the standard quadratic-reciprocity criterion

\[
\left(\frac{-3}{q}\right)=1
\quad\Longleftrightarrow\quad
q\equiv1\pmod3
\]

for primes \(q>3\). Since \(q\) is odd, this is equivalent to

\[
q\equiv1\pmod6.
\]

Thus every prime divisor of every \(H_n\) lies in the single reduced residue class \(1\pmod6\).

## Theorem 3 — exact modular obstruction multiplicity

Let \(q>3\) be prime. The congruence

\[
H_n\equiv0\pmod q
\]

has:

- exactly two residue classes \(n\pmod q\) when \(q\equiv1\pmod6\);
- no residue classes when \(q\equiv5\pmod6\).

### Proof

The polynomial

\[
3n^2+3n+1
\]

has discriminant

\[
\Delta=3^2-4\cdot3\cdot1=-3.
\]

For \(q>3\), the discriminant is nonzero modulo \(q\). Therefore the quadratic has exactly two roots when \(-3\) is a quadratic residue and zero roots when it is a nonresidue. By the criterion above, these cases are exactly \(q\equiv1\pmod6\) and \(q\equiv5\pmod6\), respectively.

Thus the centered-hexagonal sequence has an exact modular obstruction mask made only from two-class channels associated with primes \(q\equiv1\pmod6\).

## Eisenstein-lattice form

Let \(\omega=e^{2\pi i/3}\). In the Eisenstein integers,

\[
N(a+b\omega)=a^2-ab+b^2.
\]

Taking

\[
a=n+1,\qquad b=-n
\]

gives

\[
N((n+1)-n\omega)
=(n+1)^2+n(n+1)+n^2
=3n^2+3n+1
=H_n.
\]

So the same sequence is an exact norm sequence on the hexagonal/Eisenstein lattice.

This does not characterize primality: composite values such as

\[
H_5=91=7\cdot13,
\qquad
H_7=169=13^2
\]

still occur. What is exact is the restriction that every prime divisor is itself in the \(1\pmod6\) channel.

## Relation to the existing On-Primes programme

The existing dyadic fibre uses periodic modular obstruction masks in the exponent coordinate \(k\). The centered-hexagonal lane supplies a second exact mask system in the shell coordinate \(n\):

\[
q\equiv1\pmod6
\quad\Longrightarrow\quad
n\equiv r_1(q),r_2(q)\pmod q.
\]

A future cross-sieve may study intersections between the dyadic obstruction masks and these hexagonal two-root masks. No independence, density improvement, or prime-distribution theorem is claimed at this stage.

## Claim boundary

- centered-hexagonal formula and shell increments: exact;
- \(H_n\equiv1\pmod6\): proved;
- all prime divisors \(q\equiv1\pmod6\): proved;
- exactly two/no modular roots according to \(q\bmod6\): proved;
- Eisenstein norm representation: exact;
- useful new prime-distribution consequence from coupling this channel to dyadic fibres: open.
