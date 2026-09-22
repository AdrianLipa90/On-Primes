"""Exact dyadic moment decomposition of prime logarithms."""

from __future__ import annotations

from math import log

from .dyadic import dyadic_address
from .analytic import primes_up_to


def prime_log_components(p: int) -> tuple[float, float, float]:
    """Return (label, dyadic, defect) with log(p)=label+dyadic-defect."""
    a, k = dyadic_address(p)
    label = log(a)
    dyadic = k * log(2.0)
    defect = log(1.0 + 1.0 / p)
    return label, dyadic, defect


def dyadic_moment_partial(s: complex, prime_limit: int) -> complex:
    """K_P(s)=sum_{p<=P} v2(p+1)/(p**s-1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        _, k = dyadic_address(p)
        total += k / (p ** s - 1)
    return total


def fibre_label_partial(s: complex, prime_limit: int) -> complex:
    """A_P(s)=sum log(a_p)/(p**s-1), a_p=oddpart(p+1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        a, _ = dyadic_address(p)
        total += log(a) / (p ** s - 1)
    return total


def defect_partial(s: complex, prime_limit: int) -> complex:
    """D_P(s)=sum log(1+1/p)/(p**s-1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        total += log(1.0 + 1.0 / p) / (p ** s - 1)
    return total


def reconstructed_log_derivative_partial(s: complex, prime_limit: int) -> complex:
    """Return log(2) K_P(s) + A_P(s) - D_P(s)."""
    return (
        log(2.0) * dyadic_moment_partial(s, prime_limit)
        + fibre_label_partial(s, prime_limit)
        - defect_partial(s, prime_limit)
    )
