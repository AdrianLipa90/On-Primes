"""Exact prime-mask characterization by modular obstruction classes."""

from __future__ import annotations

from math import isqrt

from .dyadic import fibre_value, is_prime
from .modular import obstruction_class


def odd_primes_up_to(limit: int) -> tuple[int, ...]:
    """Return odd primes <= limit."""
    if limit < 3:
        return ()
    return tuple(n for n in range(3, limit + 1, 2) if is_prime(n))


def obstruction_witness(a: int, k: int) -> int | None:
    """Return a prime divisor witness <= sqrt(a*2**k-1), if one exists."""
    n = fibre_value(a, k)
    if n < 2:
        return None
    if n == 2:
        return None
    if n % 2 == 0:
        return 2
    for r in odd_primes_up_to(isqrt(n)):
        if a % r == 0:
            continue
        cls = obstruction_class(a, r)
        if cls is None:
            continue
        k0, d = cls
        if k % d == k0 and n % r == 0:
            return r
    return None


def prime_by_complete_obstruction_mask(a: int, k: int) -> bool:
    """Exact primality decision via the full obstruction mask up to sqrt(n)."""
    n = fibre_value(a, k)
    if n < 2:
        return False
    if n == 2:
        return True
    return obstruction_witness(a, k) is None


def obstruction_mask_factors(a: int, k: int) -> tuple[tuple[int, int, int, bool], ...]:
    """Return (r,k0,d,hit) for all active odd-prime obstruction classes <= sqrt(n)."""
    n = fibre_value(a, k)
    out: list[tuple[int, int, int, bool]] = []
    if n < 3:
        return ()
    for r in odd_primes_up_to(isqrt(n)):
        if a % r == 0:
            continue
        cls = obstruction_class(a, r)
        if cls is None:
            continue
        k0, d = cls
        out.append((r, k0, d, k % d == k0))
    return tuple(out)
