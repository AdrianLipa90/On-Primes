# ARPL Singular-Series Reverse Test v0.1 — receipt

- Date: 2026-09-26
- Repository: AdrianLipa90/On-Primes
- Branch: feat/arithmetic-relational-phase-law-v0.1
- Scope: reverse-test ARPL modular phase coordinates against standard prime-pair and prime-k-tuple singular-series formulas.

## Exact computational checks

Independent exact-rational checks performed in-session:

- finite Euler product == finite squarefree Ramanujan expansion:
  - 256/256 gap values PASS
  - prime support {2,3,5,7,11,13}
- even-sector dyadic invariance S_P(2h)=S_P(h):
  - 128/128 even gap values PASS
- two-twin-pair local admissibility at p=2,3 iff h == 0 mod 6:
  - 999/999 gap values PASS
- higher-prime local-factor phase-orbit update u -> 2u mod p:
  - checked for p in {5,7,11,13,17,19}, h=1..99, 20 orbit steps each: PASS

These checks validate the implementation identities over finite test domains; the corresponding finite identities are also proved algebraically in the theorem pack.

## Result

PASS: the standard singular-series local factors are exact observables of ARPL modular phase coordinates.

For prime pairs:
S_P(h) = product_p [1 + c_p(h)/(p-1)^2].

For two twin pairs separated by h:
H_h = {0,2,h,h+2},
B_p(h) = (1 - nu_p(H_h)/p) / (1 - 1/p)^4.

The p=2 and p=3 channels jointly admit H_h iff h is divisible by 6.

Under dyadic transport h -> 2h, every local channel evolves by the exact residue map u -> 2u mod p.

## Epistemic boundary

- finite factorization identities: PROVED
- standard infinite singular-series formulas: STANDARD
- Hardy--Littlewood occurrence asymptotics: CONJECTURAL where classically conjectural
- twin-prime infinitude: OPEN
- zeta-zero operator equivalence: OPEN
