"""Covering-set certificates for Riesel-type dyadic fibres."""

from __future__ import annotations

from .dyadic import fibre_value, is_prime
from .sieve import obstructed_residues, sieve_period


def is_residue_covering_set(a: int, divisors: tuple[int, ...]) -> bool:
    """True iff the divisibility classes cover every exponent residue."""
    period = sieve_period(divisors)
    _, removed = obstructed_residues(a, divisors)
    return len(removed) == period


def covering_certificate(a: int, divisors: tuple[int, ...], k_start: int = 1) -> dict:
    """Return a finite certificate payload for a full residue covering.

    `residue_covering` proves that every exponent has a divisor from `divisors`.
    `small_equality_exceptions` lists exponents at which the sequence value
    equals a covering prime rather than having it as a proper divisor.
    A Riesel compositeness certificate additionally requires those exceptions
    to be absent from the exponent range under consideration.
    """
    if k_start < 0:
        raise ValueError("k_start must be non-negative")
    period = sieve_period(divisors)
    residue_covering = is_residue_covering_set(a, divisors)
    equality_exceptions: list[dict[str, int]] = []
    if residue_covering:
        max_r = max(divisors, default=0)
        k = k_start
        while fibre_value(a, k) <= max_r:
            n = fibre_value(a, k)
            if n in divisors:
                equality_exceptions.append({"k": k, "value": n})
            k += 1
    return {
        "a": a,
        "divisors": list(divisors),
        "period": period,
        "k_start": k_start,
        "residue_covering": residue_covering,
        "small_equality_exceptions": equality_exceptions,
        "certifies_all_composite": residue_covering and not equality_exceptions,
    }
