# Arithmetic Relational Phase Law v0.1

Status: theorem pack with exact elementary/finite identities plus explicitly separated prior art and open bridges.

## 1. Definitions

For integers \(x,y\), define the separation

\[
\Delta(x,y)=y-x.
\]

For modulus \(q\ge2\) and harmonic \(a\in\mathbb Z\), define

\[
\chi_{q,a}(n)=\exp\!\left(\frac{2\pi ian}{q}\right).
\]

The exact phase coordinate is the residue \(n\bmod q\); the complex value is its unit-circle rendering.

For pairwise-coprime moduli \(m_1,\dots,m_r\),

\[
\Phi_{\mathbf m}(\Delta)=
(\Delta\bmod m_1,\dots,\Delta\bmod m_r).
\]

For the complete prime-power signature,

\[
\Phi_\infty(\Delta)=
(\Delta\bmod p^j)_{p\ {\rm prime},\,j\ge1}.
\]

## 2. Phase-difference law — OP-D029

For all \(x,y,q,a\),

\[
\chi_{q,a}(y)\overline{\chi_{q,a}(x)}
=
\chi_{q,a}(y-x).
\]

Proof: multiply the two exponentials and subtract the exponents. Thus relative phase depends only on separation, not the absolute origin.

## 3. Finite CRT reconstruction — OP-D030

If \(m_1,\dots,m_r\) are pairwise coprime and \(M=\prod_jm_j\), then
\(\Phi_{\mathbf m}(\Delta)\) determines \(\Delta\bmod M\) uniquely.

Proof: Chinese remainder theorem.

For distinct prime bases with moduli \(p_j^{e_j}\), the phase coordinates reconstruct the separation modulo

\[
M=\prod_jp_j^{e_j}.
\]

## 4. Complete signature injectivity — OP-D031

The map

\[
\Phi_\infty:\mathbb Z\to\prod_{p,j}\mathbb Z/p^j\mathbb Z
\]

is injective.

Proof: if \(\Phi_\infty(\Delta)=\Phi_\infty(\Delta')\), then
\(d=\Delta-\Delta'\) is divisible by every prime power. If \(d\neq0\), choose a prime power \(p^j>|d|\). A nonzero integer of smaller magnitude cannot be divisible by \(p^j\), contradiction.

This is a representation theorem compatible with standard profinite/character mathematics; novelty is not claimed for the underlying CRT/profinite fact.

## 5. Ordered-gap phase representation — OP-D032

For a strictly increasing integer sequence \(x_1<x_2<\cdots\), define

\[
g_n=x_{n+1}-x_n.
\]

Then

\[
x_n=x_1+\sum_{j=1}^{n-1}g_j.
\]

Hence the anchor \(x_1\) plus the ordered gap stream reconstructs the sequence exactly. Combining with OP-D031 gives

\[
\{x_n\}
\longleftrightarrow
\left(x_1,\{g_n\}\right)
\longleftrightarrow
\left(x_1,\{\Phi_\infty(g_n)\}\right).
\]

For primes this becomes

\[
\{p_n\}
\longleftrightarrow
\left(p_1,\{p_{n+1}-p_n\}\right)
\longleftrightarrow
\left(p_1,\{\Phi_\infty(p_{n+1}-p_n)\}\right).
\]

This is an exact coordinate equivalence. It does not by itself prove a new distribution law for the gaps.

## 6. Pair-correlation / power-spectrum duality — OP-D033

For a finite periodic signal \(f_0,\dots,f_{N-1}\), define

\[
C(h)=\sum_{n=0}^{N-1}f_{n+h}\overline{f_n},
\]

with indices modulo \(N\), and

\[
F(k)=\sum_{n=0}^{N-1}f_ne^{-2\pi ikn/N}.
\]

Then

\[
|F(k)|^2=\sum_{h=0}^{N-1}C(h)e^{-2\pi ikh/N}
\]

and

\[
C(h)=\frac1N\sum_{k=0}^{N-1}|F(k)|^2e^{2\pi ikh/N}.
\]

Proof: expand \(|F(k)|^2\) and group by \(h=m-n\pmod N\).

### Firewall

Power spectrum / pair correlation does not in general uniquely reconstruct the ordered point set; homometric and phase-retrieval ambiguities exist. Exact reconstruction above uses the ordered gap stream, not \(|F|^2\) alone.

## 7. Twin-prime six-lock — OP-D034

Let \(t_n>3\) be starts of twin-prime pairs \((t_n,t_n+2)\). Every such start satisfies

\[
t_n\equiv-1\pmod6.
\]

Therefore every consecutive twin-start gap

\[
h_n=t_{n+1}-t_n
\]

obeys

\[
6\mid h_n.
\]

Equivalently,

\[
\chi_{2,1}(h_n)=1,\qquad
\chi_{3,1}(h_n)=1.
\]

Proof: every prime \(>3\) is \(\pm1\bmod6\). If \(p\equiv1\bmod6\), then \(p+2\equiv3\bmod6\) is divisible by 3, so a nonexceptional twin start must be \(-1\bmod6\).

Thus modulus 6 is an exact carrier lock. Higher modular coordinates encode additional residue information; calling them sidebands is project terminology.

## 8. Dyadic phase transport — OP-D035

The existing On-Primes map is

\[
T(x)=2x+1.
\]

For all \(x,y\),

\[
T(y)-T(x)=2(y-x).
\]

After \(r\ge0\) iterations,

\[
\Delta(T^rx,T^ry)=2^r\Delta(x,y).
\]

Therefore every modular phase character satisfies

\[
\chi_{q,a}(\Delta(T^rx,T^ry))
=
\chi_{q,a}(\Delta(x,y))^{2^r}.
\]

So the dyadic shift is exactly phase squaring on every modular unit-circle channel.

## 9. Fibre obstruction as phase-orbit hitting — OP-D036

For the existing fibre

\[
x_{a,k}=a2^k-1,
\]

fix a candidate divisor \(r\) and define

\[
u_k=a2^k\bmod r,
\qquad
z_k=e^{2\pi iu_k/r}.
\]

Then

\[
u_{k+1}\equiv2u_k\pmod r,
\qquad
z_{k+1}=z_k^2,
\]

and

\[
r\mid x_{a,k}
\iff
u_k\equiv1\pmod r
\iff
z_k=e^{2\pi i/r}.
\]

Hence each existing modular obstruction class is equivalently a hitting set of a finite phase orbit. This is mathematically equivalent to the congruence formulation already recorded in OP-D007; the value here is the unified phase coordinate layer.

## 10. Prior-art boundary

These ingredients are established mathematics and are not claimed as novel:

- characters \(e^{2\pi ian/q}\), Fourier analysis on cyclic groups, CRT, and profinite residue coordinates;
- finite Wiener--Khintchine / autocorrelation--power-spectrum duality;
- Ramanujan sums and Ramanujan--Fourier expansions;
- prior work relating Ramanujan--Fourier series and Wiener--Khintchine ideas to prime-pair correlations.

Gadiyar and Padma, Physica A 269 (1999), 503--510, DOI 10.1016/S0378-4371(99)00171-5, explicitly relate prime-pair distribution to Ramanujan--Fourier series and a Wiener--Khintchine formula.

Their later paper, Czechoslovak Mathematical Journal 64(1) (2014), 251--267, DOI 10.1007/s10587-014-0098-5, describes the corresponding Hardy--Littlewood argument as heuristic because a required interchange of limits is not justified.

The project-specific object introduced here is the **Arithmetic Relational Phase Law (ARPL)** as a unified exact coordinate layer joining:

1. ordered separations;
2. complete modular prime-power phase signatures;
3. exact reconstruction from anchor plus ordered gaps;
4. the existing dyadic map as phase squaring;
5. the existing modular fibre obstruction sieve as finite phase-orbit hitting.

Novelty of this packaging or of any stronger consequence remains OPEN pending systematic literature audit.

## 11. No-go statements

This v0.1 theorem pack does not establish:

- the twin-prime conjecture;
- the Hardy--Littlewood prime-pair or prime-k-tuple conjecture;
- an equivalence between prime gaps and nontrivial zeros of \(\zeta\);
- uniqueness of a point set from its power spectrum alone;
- the Riemann Hypothesis;
- a new physical law.
