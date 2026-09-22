"""Modular obstruction classes for dyadic fibres."""

from __future__ import annotations

from math import gcd

from .dyadic import fibre_value, is_prime


def multiplicative_order_2(r: int) -> int:
    """Return ord_r(2) for an odd integer r > 1."""
    if not isinstance(r, int) or isinstance(r, bool) or r <= 1 or r % 2 == 0:
        raise ValueError("r must be an odd integer > 1")
    x = 2 % r
    d = 1
    while x != 1:
        x = (2 * x) % r
        d += 1
        if d > r:
            raise ArithmeticError("failed to find multiplicative order")
    return d


def obstruction_class(a: int, r: int) -> tuple[int, int] | None:
    """Return (k0, d) with r | a*2**k - 1 iff k == k0 (mod d).

    The function is restricted to odd prime r not dividing a. If no such
    exponent exists, return None.
    """
    if not isinstance(a, int) or isinstance(a, bool) or a <= 0 or a % 2 == 0:
        raise ValueError("a must be a positive odd integer")
    if not is_prime(r) or r == 2:
        raise ValueError("r must be an odd prime")
    if gcd(a, r) != 1:
        return None
    d = multiplicative_order_2(r)
    target = pow(a, -1, r)
    x = 1
    for k in range(d):
        if x == target:
            return k, d
        x = (2 * x) % r
    return None


def is_obstructed_by(a: int, k: int, r: int) -> bool:
    """True when r is a proper divisor of a*2**k - 1."""
    cls = obstruction_class(a, r)
    if cls is None:
        return False
    k0, d = cls
    if k % d != k0:
        return False
    n = fibre_value(a, k)
    return n > r and n % r == 0


def obstruction_profile(a: int, k_max: int, divisors: tuple[int, ...]) -> dict[int, tuple[int, ...]]:
    """Map each tested odd prime divisor to obstructed k values up to k_max."""
    if k_max < 0:
        raise ValueError("k_max must be non-negative")
    profile: dict[int, tuple[int, ...]] = {}
    for r in divisors:
        cls = obstruction_class(a, r)
        if cls is None:
            profile[r] = ()
            continue
        k0, d = cls
        values = tuple(
            k for k in range(k0, k_max + 1, d)
            if fibre_value(a, k) > r
        )
        profile[r] = values
    return profile
