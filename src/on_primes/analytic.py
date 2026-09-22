"""Exact fibre decompositions of finite prime-side Dirichlet sums."""

from __future__ import annotations

from cmath import log as clog
from math import log

from .dyadic import dyadic_address, is_prime


def primes_up_to(limit: int) -> tuple[int, ...]:
    """Return all primes <= limit using the reference primality test."""
    if limit < 2:
        return ()
    return tuple(n for n in range(2, limit + 1) if is_prime(n))


def classical_log_derivative_partial(s: complex, prime_limit: int) -> complex:
    """Finite prime truncation sum_p log(p)/(p**s - 1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        total += log(p) / (p ** s - 1)
    return total


def fibre_log_derivative_partial(s: complex, prime_limit: int) -> complex:
    """The same finite prime sum regrouped by exact dyadic address."""
    fibres: dict[int, list[tuple[int, int]]] = {}
    for p in primes_up_to(prime_limit):
        a, k = dyadic_address(p)
        fibres.setdefault(a, []).append((k, p))

    total = 0j
    for a in sorted(fibres):
        for k, p in sorted(fibres[a]):
            total += log(p) / (p ** s - 1)
    return total


def boundary_plus_interior_partial(s: complex, prime_limit: int) -> tuple[complex, complex, complex]:
    """Return (boundary, interior, total) for the k=0 / k>=1 split."""
    boundary = 0j
    interior = 0j
    for p in primes_up_to(prime_limit):
        _, k = dyadic_address(p)
        term = log(p) / (p ** s - 1)
        if k == 0:
            boundary += term
        else:
            interior += term
    return boundary, interior, boundary + interior


def truncated_von_mangoldt_prime_power_sum(s: complex, x_max: int) -> complex:
    """Finite sum over prime powers p^m <= x_max of log(p)*p**(-m*s)."""
    total = 0j
    for p in primes_up_to(x_max):
        q = p
        while q <= x_max:
            total += log(p) * (q ** (-s))
            if q > x_max // p:
                break
            q *= p
    return total


def fibre_prime_power_sum(s: complex, x_max: int) -> complex:
    """Same finite von Mangoldt prime-power sum, regrouped by prime fibres."""
    fibres: dict[int, list[int]] = {}
    for p in primes_up_to(x_max):
        a, _ = dyadic_address(p)
        fibres.setdefault(a, []).append(p)

    total = 0j
    for a in sorted(fibres):
        for p in sorted(fibres[a]):
            q = p
            while q <= x_max:
                total += log(p) * (q ** (-s))
                if q > x_max // p:
                    break
                q *= p
    return total
