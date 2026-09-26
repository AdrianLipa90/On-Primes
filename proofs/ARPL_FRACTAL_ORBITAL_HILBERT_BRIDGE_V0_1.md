# ARPL -> Fractal-Orbital Hilbert Bridge v0.1

Status: EXACT_REPRESENTATION_BRIDGE + OPEN_PHYSICAL_BINDING
Date: 2026-09-26

This note extends the Arithmetic Relational Phase Law (ARPL) without changing any of its proved statements.

## Finite Hilbert representation

For modulus q>=2, let H_q = l^2(Z/qZ) with residue basis |n>. Define

    P_(q,a)|n> = chi_(q,a)(n)|n>,

where

    chi_(q,a)(n)=exp(2 pi i a n/q).

For integers x,y,

    chi_(q,a)(y) conjugate(chi_(q,a)(x)) = chi_(q,a)(y-x),

so the ARPL separation law is exactly a relative-unitary phase law.

The mismatch scalar is

    d_(q,a)(x,y)
    = |1-chi_(q,a)(y-x)|^2
    = 4 sin^2(pi a (y-x)/q).

For primitive a, d=0 exactly when x == y mod q.

## Product signature

For pairwise-coprime moduli m_1,...,m_r use

    H_M = tensor_j H_(m_j).

The product-character representation carries the finite CRT phase signature. In the complete prime-power limit this is the representation counterpart of the injective profinite signature already recorded in ARPL v0.1.

## Dyadic scale channel

For T(x)=2x+1,

    Delta(T^r x,T^r y)=2^r Delta(x,y),

hence

    chi_(q,a)(Delta(T^r x,T^r y))
    = chi_(q,a)(Delta(x,y))^(2^r).

Thus the exact ARPL dyadic law becomes an exact discrete phase-dilation channel.

## Fractal-Orbital Moire-Hilbert connection

The external orbital construction uses

    H_MF = integral_F^oplus H_x d mu_F(x),

    A_FO = C(F) rtimes_(alpha,omega) G_orb,

and

    R_ab = U_a^* U_b.

ARPL supplies an exact arithmetic character family that can enter A_FO only through a typed adapter.

The lawful direction is

    integer separation
      -> ARPL character/signature
      -> unitary phase representation
      -> admitted orbital representation
      -> relative Moire observable.

The reverse implication is not automatic: an arbitrary Moire or PhaseNav state is not thereby a prime sequence.

## Boundary

Exact here:
- finite cyclic character representation;
- unitary phase operators;
- relative mismatch formula;
- CRT/product representation;
- dyadic phase-squaring transport.

Open:
- any physical interpretation of prime phases;
- any unique embedding into PhaseNav 36D;
- any new prime-gap or zeta-zero theorem beyond the existing ARPL/Landau notes.
