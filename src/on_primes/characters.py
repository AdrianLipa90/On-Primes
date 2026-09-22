"""Dirichlet characters modulo powers of two and residue-class decompositions."""

from __future__ import annotations

import cmath
from functools import lru_cache

from .analytic import primes_up_to


def character_ids_pow2(j: int) -> tuple[tuple[int, int], ...]:
    """Return identifiers for all Dirichlet characters modulo 2**j."""
    if not isinstance(j, int) or isinstance(j, bool) or j < 1:
        raise ValueError("j must be an integer >= 1")
    if j == 1:
        return ((0, 0),)
    if j == 2:
        return ((0, 0), (1, 0))
    order = 1 << (j - 2)
    return tuple((b, c) for b in (0, 1) for c in range(order))


@lru_cache(maxsize=None)
def _unit_coordinates_pow2(j: int) -> dict[int, tuple[int, int]]:
    q = 1 << j
    if j == 1:
        return {1: (0, 0)}
    if j == 2:
        return {1: (0, 0), 3: (1, 0)}
    order = 1 << (j - 2)
    coords: dict[int, tuple[int, int]] = {}
    x = 1
    for t in range(order):
        coords[x] = (0, t)
        coords[(-x) % q] = (1, t)
        x = (x * 5) % q
    return coords


def character_value_pow2(j: int, char_id: tuple[int, int], n: int) -> complex:
    """Evaluate a Dirichlet character modulo 2**j.

    For j>=3 the unit group is represented as C2 x C_(2**(j-2)),
    with generators -1 and 5.
    """
    ids = character_ids_pow2(j)
    if char_id not in ids:
        raise ValueError("invalid character id for modulus")
    q = 1 << j
    r = n % q
    if r % 2 == 0:
        return 0j
    eps, t = _unit_coordinates_pow2(j)[r]
    b, c = char_id
    sign = -1.0 if (b * eps) % 2 else 1.0
    if j <= 2:
        return complex(sign, 0.0)
    order = 1 << (j - 2)
    phase = cmath.exp(2j * cmath.pi * c * t / order)
    return sign * phase


def residue_indicator_via_characters(j: int, n: int) -> complex:
    """Character-orthogonality indicator for n == -1 mod 2**j (odd n)."""
    q = 1 << j
    if n % 2 == 0:
        return 0j
    chars = character_ids_pow2(j)
    total = 0j
    for cid in chars:
        chi_minus_one = character_value_pow2(j, cid, -1)
        chi_n = character_value_pow2(j, cid, n)
        total += chi_minus_one.conjugate() * chi_n
    return total / len(chars)


def residue_class_prime_sum_partial(j: int, s: complex, prime_limit: int) -> complex:
    """Sum 1/(p**s-1) for primes p<=P with p == -1 mod 2**j."""
    q = 1 << j
    target = q - 1
    total = 0j
    for p in primes_up_to(prime_limit):
        if p % q == target:
            total += 1 / (p ** s - 1)
    return total


def character_prime_sum_partial(j: int, char_id: tuple[int, int], s: complex, prime_limit: int) -> complex:
    """Sum chi(p)/(p**s-1) over primes p<=P."""
    total = 0j
    for p in primes_up_to(prime_limit):
        total += character_value_pow2(j, char_id, p) / (p ** s - 1)
    return total


def residue_class_via_characters_partial(j: int, s: complex, prime_limit: int) -> complex:
    """Orthogonality reconstruction of the -1 residue-class prime sum."""
    chars = character_ids_pow2(j)
    total = 0j
    for cid in chars:
        coeff = character_value_pow2(j, cid, -1).conjugate()
        total += coeff * character_prime_sum_partial(j, cid, s, prime_limit)
    return total / len(chars)
