"""Exact dyadic shells determined by v2(p+1)."""

from __future__ import annotations

from .analytic import primes_up_to
from .dyadic import dyadic_address


def shell_residue(k: int) -> tuple[int, int]:
    """Return (residue, modulus) for the exact shell v2(p+1)=k, k>=1."""
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k must be an integer >= 1")
    modulus = 1 << (k + 1)
    residue = (1 << k) - 1
    return residue, modulus


def in_exact_shell(n: int, k: int) -> bool:
    """Return True iff n == 2**k-1 mod 2**(k+1)."""
    residue, modulus = shell_residue(k)
    return n % modulus == residue


def prime_shell_counts(limit: int) -> dict[int, int]:
    """Count primes <= limit by exact k=v2(p+1), including k=0 for p=2."""
    counts: dict[int, int] = {}
    for p in primes_up_to(limit):
        _, k = dyadic_address(p)
        counts[k] = counts.get(k, 0) + 1
    return counts
