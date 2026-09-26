# ARPL Phase-Covering Geometry — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact finite covering bounds for h=6

First 5 active channels:
P_5 = {5,7,11,13,19}

equal-weight second-moment coverage lower bound:
3481 / 4680
= 0.743803418803...

optimal exact L2 projection coverage lower bound:
57 / 73
= 0.780821917808...

First 10 active channels:
P_10 = {5,7,11,13,19,23,29,37,47,53}

optimal exact L2 bound:
62891 / 78951
= 0.796582690530...

First 15 active channels through p=79:

equal-weight bound:
8909939269035 / 11572360119749
= 0.769932768842...

optimal exact L2 bound:
1268391857255 / 1516708968451
= 0.836278998568...

therefore:
lower-edge atom mass
<=
248317111196 / 1516708968451
= 0.163721001432...

The exact finite-prefix inclusion-exclusion mass is stronger:
a_15(6) = 252/3335 = 0.075562218891...

The L2 result is useful because it uses only pairwise CRT phase geometry.

## Larger floating diagnostic for the optimal Gram bound

N=20  : B_N ~= 0.842100508236
N=30  : B_N ~= 0.856102161415
N=50  : B_N ~= 0.863251146983
N=75  : B_N ~= 0.867882004326
N=100 : B_N ~= 0.873867089717
N=150 : B_N ~= 0.877879017586
N=200 : B_N ~= 0.880669351539
N=250 : B_N ~= 0.882740513540
N=300 : B_N ~= 0.883513770918

These larger values are numerical diagnostics only and are not promoted as exact receipts.

## Exact phase-survival hazards for first 15 active channels at h=6

channels:
5,7,11,13,19,23,29,37,47,53,59,61,67,71,79

branching b_N:
2,3,5,1,3,11,7,1,23,13,29,1,1,1,1

hazards eta_N:
1/2, 1/3, 1/5, 1/2, 0, 1/11, 0, 0, 1/23, 0, 1/29, 1/4, 1/10, 0, 0

compatibility fractions c_N=b_N eta_N:
1,1,1,1/2,0,1,0,0,1,0,1,1/4,1/10,0,0

survival product:
product_N (1-eta_N)
=
252/3335.

## Exact branch-prune diagnostics

At selected prefix sizes:

N=5:
L_N = 90
S_N = 12
a_N = 2/15
D_N^surv ~= 0.5522248343

N=10:
L_N = 2,072,070
S_N = 240,240
a_N = 8/69
D_N^surv ~= 0.8518525666

N=15:
L_N = 60,090,030
S_N = 4,540,536
a_N = 252/3335
D_N^surv ~= 0.8558010299

N=20:
L_N = 44,395,715,964,600
S_N = 3,022,180,761,600
a_N = 1,677,312/24,639,647
D_N^surv ~= 0.9144873260

N=25:
L_N = 1,227,053,193,545,579,400
S_N = 80,407,676,392,243,200
a_N = 3,268,608/49,880,261
D_N^surv ~= 0.9345693617

These are finite-prefix diagnostics, not a limiting-dimension theorem.

## Status

FINITE_GRAM_KERNEL = PROVED
OPTIMAL_L2_COVERING_BOUND = PROVED
SURVIVAL_HAZARD_PRODUCT = PROVED
BRANCH_PRUNE_RECURSION = PROVED
CANONICAL_PHASE_ULTRAMETRIC_DIMENSION = PROVED
LOWER_EDGE_ATOM_ZERO_OR_POSITIVE = OPEN
LIMITING_AVOIDANCE_SET_DIMENSION = OPEN
