"""Finite modular sieves on dyadic prime fibres."""

from __future__ import annotations

from math import lcm

from .dyadic import fibre_value, is_prime
from .modular import multiplicative_order_2, obstruction_class


def sieve_period(divisors: tuple[int, ...]) -> int:
    """Return the exact period induced by a finite set of odd prime divisors."""
    if not divisors:
        return 1
    period = 1
    for r in divisors:
        if not is_prime(r) or r == 2:
            raise ValueError("all divisors must be odd primes")
        period = lcm(period, multiplicative_order_2(r))
    return period


def obstructed_residues(a: int, divisors: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Return (period, residues) removed by the finite modular sieve."""
    period = sieve_period(divisors)
    removed: set[int] = set()
    for r in divisors:
        cls = obstruction_class(a, r)
        if cls is None:
            continue
        k0, d = cls
        removed.update(range(k0, period, d))
    return period, tuple(sorted(removed))


def survivor_residues(a: int, divisors: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Return residue classes modulo the exact finite-sieve period not removed."""
    period, removed = obstructed_residues(a, divisors)
    removed_set = set(removed)
    survivors = tuple(k for k in range(period) if k not in removed_set)
    return period, survivors


def survivor_density(a: int, divisors: tuple[int, ...]) -> float:
    """Exact rational density represented as a float for the periodic survivor set."""
    period, survivors = survivor_residues(a, divisors)
    return len(survivors) / period


def finite_sieve_allows(a: int, k: int, divisors: tuple[int, ...]) -> bool:
    """Return True iff k survives all modular residue obstructions in divisors."""
    if k < 0:
        raise ValueError("k must be non-negative")
    period, survivors = survivor_residues(a, divisors)
    return (k % period) in set(survivors)


def certified_composite_by_sieve(a: int, k: int, divisors: tuple[int, ...]) -> bool:
    """Return True when the finite sieve exhibits a proper prime divisor."""
    n = fibre_value(a, k)
    for r in divisors:
        cls = obstruction_class(a, r)
        if cls is None:
            continue
        k0, d = cls
        if k % d == k0 and n > r and n % r == 0:
            return True
    return False
