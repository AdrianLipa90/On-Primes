"""Dyadic residue-tower identities for v2(p+1)."""

from __future__ import annotations

from .analytic import primes_up_to
from .dyadic import dyadic_address


def valuation_as_residue_count(p: int) -> int:
    """Count powers 2**j dividing p+1, j>=1; equals v2(p+1)."""
    _, k = dyadic_address(p)
    count = 0
    j = 1
    while j <= k:
        if p % (1 << j) == ((1 << j) - 1):
            count += 1
        j += 1
    return count


def residue_tower_partial(s: complex, prime_limit: int) -> complex:
    """Return sum_j sum_{p<=P, p=-1 mod 2**j} 1/(p**s-1)."""
    primes = primes_up_to(prime_limit)
    max_k = 0
    for p in primes:
        _, k = dyadic_address(p)
        max_k = max(max_k, k)

    total = 0j
    for j in range(1, max_k + 1):
        modulus = 1 << j
        residue = modulus - 1
        for p in primes:
            if p % modulus == residue:
                total += 1 / (p ** s - 1)
    return total


def direct_valuation_moment_partial(s: complex, prime_limit: int) -> complex:
    """Return sum_{p<=P} v2(p+1)/(p**s-1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        _, k = dyadic_address(p)
        total += k / (p ** s - 1)
    return total
