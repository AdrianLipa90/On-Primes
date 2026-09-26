# ARPL Source-Hull Non-Atomicity and Edge-Atom Receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Exact structural checks

For admissible h=6, the first active channels are:

5, 7, 11, 13, 19, 23, 29, 37, 47, 53, 59, 61, 67, 71, 79, ...

with base-4 periods:

2, 3, 5, 6, 9, 11, 14, 18, 23, 26, 29, 30, 33, 35, 39, ...

The cumulative finite phase clock after the first 15 channels is

L_15 = 60,090,030.

## Exact finite lower-edge avoidance masses

Ordering active channels by prime, the exact finite masses are:

N=1,  through p=5:   1/2
N=2,  through p=7:   1/3
N=3,  through p=11:  4/15
N=4,  through p=13:  2/15
N=5,  through p=19:  2/15
N=6,  through p=23:  4/33
N=7,  through p=29:  4/33
N=8,  through p=37:  4/33
N=9,  through p=47:  8/69
N=10, through p=53:  8/69

Direct finite-clock enumeration at N=15 gives

a_15(6)
=
4,540,536 / 60,090,030
=
252 / 3335
=
0.07556221889055473...

The sequence a_N is monotone non-increasing by construction.

## Interpretation

Each a_N is an exact upper bound on the possible lower-edge atom mass

a_*(6)=mu_6({A(6)}).

The finite values do NOT prove that a_*(6) is positive.

They also do NOT prove that a_*(6)=0.

## Theorem status

ACTIVE_CHANNEL_SET_INFINITE = PROVED via classical Polya recurrence theorem
OBSERVABLE_PERIODS_UNBOUNDED = PROVED
PHASE_HULL_HAAR_NONATOMIC = PROVED
LOWER_EDGE_ATOM_CRITERION = PROVED
NEGATIVE_MOMENT_EXTRACTION = PROVED
FULL_PUSHFORWARD_ATOMLESSNESS = OPEN

## Validation boundary

The new finite identities were independently recomputed in-session.
The exact inclusion-exclusion helpers and regression tests were added to the branch.
No new full repository CI PASS is claimed in this receipt.
