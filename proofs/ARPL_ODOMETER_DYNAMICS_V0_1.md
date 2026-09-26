# ARPL Odometer Dynamics v0.1

Status: exact dynamical-system identification. Odometer theory itself is standard; the ARPL specialization is project-specific.

## 1. Phase tower

Fix admissible

\[
h\ge6,\qquad 6\mid h.
\]

Enumerate the active base-4 channels as \(p_1,p_2,\dots\), and set

\[
e_j=\operatorname{ord}_{p_j}(4),
\]

\[
L_N=\operatorname{lcm}(e_1,\dots,e_N).
\]

Then

\[
L_N\mid L_{N+1}
\]

and, by OP-D121--OP-D123,

\[
L_N\to\infty.
\]

The phase hull is

\[
K_h
\cong
\varprojlim_N\mathbb Z/L_N\mathbb Z.
\]

Let

\[
g=(1\bmod L_N)_N\in K_h.
\]

Define

\[
\boxed{
T_h(x)=x+g.
}
\]

## 2. Odometer identification — OP-D128

The system

\[
(K_h,T_h)
\]

is the inverse limit of the finite cyclic rotations

\[
x\mapsto x+1
\quad\text{on}\quad
\mathbb Z/L_N\mathbb Z.
\]

Therefore

\[
\boxed{
(K_h,T_h)
\text{ is a procyclic odometer / adding machine.}
}
\]

The original integer dyadic time \(r\) is exactly the orbit

\[
T_h^r(0)=rg.
\]

The finite phase clock at resolution \(N\) is the factor

\[
\mathbb Z/L_N\mathbb Z.
\]

## 3. Minimality — OP-D129

The element \(g\) topologically generates \(K_h\) by construction:

\[
K_h=\overline{\{rg:r\in\mathbb Z\}}.
\]

For any \(x\in K_h\),

\[
\{T_h^r(x):r\in\mathbb Z\}
=
x+\{rg:r\in\mathbb Z\}.
\]

Translation is a homeomorphism, so the closure of every orbit is

\[
x+K_h=K_h.
\]

Hence

\[
\boxed{
T_h\text{ is minimal.}
}
\]

Every phase state is recurrent at every finite resolution.

## 4. Unique ergodicity — OP-D130

Haar probability measure \(m_{K_h}\) is invariant under translation.

Let \(\eta\) be any \(T_h\)-invariant probability measure. Since invariance under \(T_h\) gives invariance under all translations by \(rg\), and the subgroup \(\{rg\}\) is dense, continuity implies that \(\eta\) is invariant under all translations in \(K_h\).

The unique translation-invariant probability measure on a compact group is Haar measure.

Therefore

\[
\boxed{
m_{K_h}
\text{ is the unique }T_h\text{-invariant probability measure.}
}
\]

Thus the ARPL phase clock is uniquely ergodic.

## 5. Uniform finite-clock sampling — OP-D131

For every continuous function

\[
f:K_h\to\mathbb C,
\]

unique ergodicity gives the uniform Birkhoff limit

\[
\boxed{
\lim_{T\to\infty}
\frac1T\sum_{r=0}^{T-1}f(T_h^r x)
=
\int_{K_h}f\,dm_{K_h},
}
\]

uniformly in \(x\).

For every cylinder observable depending only on the first \(N\) phase coordinates, this reduces exactly to averaging over one finite period:

\[
\frac1{L_N}
\sum_{r=0}^{L_N-1}
f(rg).
\]

Thus the generalized-CRT densities previously derived are the finite-factor Haar/Birkhoff averages of the odometer.

## 6. Equicontinuity and zero topological entropy — OP-D132

Equip \(K_h\) with any compatible translation-invariant inverse-limit metric, for example one built from the first level at which two points differ.

Every iterate

\[
T_h^r
\]

is a translation and therefore an isometry.

Hence the family

\[
\{T_h^r:r\in\mathbb Z\}
\]

is equicontinuous.

A compact equicontinuous dynamical system has zero topological entropy. Therefore

\[
\boxed{
h_{\rm top}(T_h)=0.
}
\]

The divergent finite-quotient information

\[
H_N=\log L_N\to\infty
\]

is therefore **phase-resolution information**, not positive dynamical entropy production.

## 7. Koopman pure-point spectrum — OP-D133

Let

\[
U_hf=f\circ T_h
\]

be the Koopman operator on

\[
L^2(K_h,m_{K_h}).
\]

Every character

\[
\chi\in\widehat K_h
\]

is an eigenfunction:

\[
U_h\chi(x)
=
\chi(x+g)
=
\chi(g)\chi(x).
\]

The characters form an orthonormal basis of \(L^2(K_h)\). Hence the Koopman spectrum is pure point.

From OP-D114,

\[
\widehat K_h
=
\bigcup_N
\frac1{L_N}\mathbb Z/\mathbb Z.
\]

Writing

\[
\chi_\lambda(g)=e^{2\pi i\lambda},
\]

the eigenvalue set is

\[
\boxed{
\sigma_{\rm pp}(U_h)
=
\left\{
e^{2\pi i\lambda}:
\lambda\in
\bigcup_N
\frac1{L_N}\mathbb Z/\mathbb Z
\right\}.
}
\]

Thus the exact rational phase-frequency module is the dynamical spectrum of the odometer itself.

## 8. Zero measure entropy — OP-D134

A compact group rotation with pure point spectrum has zero Kolmogorov--Sinai entropy.

Equivalently, \(T_h\) is an inverse limit of finite periodic systems, each of which has zero measure entropy, and entropy does not increase under this inverse-limit construction.

Therefore

\[
\boxed{
h_{m_{K_h}}(T_h)=0.
}
\]

This is compatible with unbounded phase resolution:

\[
L_N\to\infty
\]

but no stochastic entropy generation per time step.

## 9. ARPL observable as an odometer field

The logarithmic singular-series field is

\[
\mathcal Y_h(x)
=
\log A(h)
+
\sum_{p\in\mathcal A_h}
w_p\mathbf1_{C_p}(x).
\]

The integer-time sequence studied by ARPL is precisely

\[
\boxed{
Y_r(h)=\mathcal Y_h(T_h^r0).
}
\]

Finite prime truncations are locally constant functions on finite odometer factors.

The full field is their controlled mean-limit / measurable limit already established in the logarithmic, \(B^2\), and entire-transform theorem packs.

Thus the ARPL phase spectrum has two distinct but compatible levels:

1. **system spectrum**:
   \[
   \widehat K_h;
   \]
2. **observable spectrum**:
   the subset of system frequencies with nonzero Fourier coefficient for \(\mathcal Y_h\).

This separates available phase frequencies from actually excited phase modes.

## 10. Relation to the previously proved Fourier--Bohr spectrum

The earlier global \(B^2\) theorem placed the log-field spectrum inside rational frequencies generated by local clocks.

The odometer identification sharpens the ambient object:

\[
\boxed{
\Lambda_h^{\rm observable}
\subseteq
\widehat K_h
=
\bigcup_N(1/L_N)\mathbb Z/\mathbb Z.
}
\]

The local frequencies

\[
m/e_p
\]

are characters of finite factors and therefore characters of \(K_h\).

The observable may have cancellations, so equality of the actual support with the whole dual module is not claimed.

## 11. Dyadic base-point invariance

Replacing

\[
h\mapsto2^kh
\]

does not change the periods \(e_p\), hence does not change \(L_N\), \(K_h\), or \(T_h\).

It only translates the target phase configuration by \(-kg\).

Therefore all dynamical-system invariants are unchanged:

\[
\boxed{
(K_{2^kh},T_{2^kh})
\cong
(K_h,T_h)
}
\]

canonically at the clock level.

This includes:

- phase refinement tower;
- Haar measure;
- topological entropy;
- measure entropy;
- Koopman eigenvalue group.

## 12. Prior-art boundary

Odometers / adding machines, compact group rotations, Haar unique ergodicity, equicontinuity, zero entropy, and pure-point character spectrum are standard dynamical systems theory.

ARPL does not claim those general facts as new.

The project-specific result is that the singular-series phase law generated by the observable clocks

\[
e_p=\operatorname{ord}_p(4)
\]

has exactly this odometer as its canonical global time-phase system, with target phases \(\rho_p(h)\) and singular-series weights \(w_p\).

## 13. Structural consequence

The global architecture can now be written as

\[
\boxed{
\text{prime channels}
\to
\text{finite cyclic clocks}
\to
\text{odometer inverse limit}
\to
\text{Haar phase law}
\to
\text{weighted observable}
\to
\text{limiting amplitude distribution}.
}
\]

The system itself is deterministic, minimal, uniquely ergodic, zero-entropy, and pure-point.

Any apparent statistical law in the singular-series amplitude is therefore a pushforward law of a deterministic zero-entropy phase rotation, not a postulated stochastic source.
