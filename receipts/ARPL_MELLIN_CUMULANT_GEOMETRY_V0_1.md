# ARPL Mellin and Cumulant Geometry — receipt v0.1

Date: 2026-09-26
Repository: AdrianLipa90/On-Primes
Branch: feat/arithmetic-relational-phase-law-v0.1

## Closed consequences of the entire transform

Given the already proved limiting law nu_h of
Y = log S(H_{2^r h}) and its entire bilateral Laplace transform M_h(z):

- the positive amplitude law mu_h=(exp)_* nu_h exists;
- M_h(z) is also the Mellin transform integral x^z d mu_h(x);
- K_h(z)=log M_h(z) is analytic in a neighborhood of z=0;
- all log-amplitude cumulants kappa_n(h) exist;
- kappa_1(h)=L(h), the global logarithmic mean;
- kappa_2(h)=V(h), the global B2 variance;
- all polynomial moments of the logarithmic field exist;
- the limiting law is moment-determinate;
- optimized upper and lower Chernoff bounds exist;
- the whole cumulant tower is invariant under h -> 2^k h.

## Important boundary

The Legendre transform
I_h(y)=sup_s {s y-K_h(s)}
is used only as a Chernoff/concentration envelope.

No large-deviation principle with an external scaling parameter is claimed.

No claim is made that the limiting law is atomless, absolutely continuous, or singular-continuous.

## Status

MELLIN_TRANSFORM = PROVED
LOCAL_CUMULANT_GEOMETRY = PROVED
ALL_LOG_MOMENTS = PROVED
CHERNOFF_ENVELOPES = PROVED
DYADIC_CUMULANT_INVARIANCE = PROVED
DISTRIBUTION_TYPE = OPEN
