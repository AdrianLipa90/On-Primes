"""Centered-hexagonal channel for prime/composite obstruction studies."""

from __future__ import annotations

from .dyadic import is_prime


def centered_hexagonal(n: int) -> int:
    """Return H_n = 1 + 3*n*(n+1), with H_0 = 1."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return 1 + 3 * n * (n + 1)


def shell_increment(n: int) -> int:
    """Return H_n - H_(n-1) = 6*n for shell n >= 1."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    return 6 * n


def obstruction_roots_mod_prime(q: int) -> tuple[int, ...]:
    """Return n mod q for which q divides H_n.

    For primes q > 3 the theorem in
    proofs/CENTERED_HEXAGONAL_PRIME_CHANNEL_V0_1.md gives:
      * q == 1 (mod 6): exactly two roots;
      * q == 5 (mod 6): no roots.
    This is a transparent reference enumerator, not a fast root solver.
    """
    if not is_prime(q):
        raise ValueError("q must be prime")
    return tuple(n for n in range(q) if centered_hexagonal(n) % q == 0)


def is_obstructed_by(n: int, q: int) -> bool:
    """True when prime q is a proper divisor of H_n."""
    value = centered_hexagonal(n)
    return value > q and value % q == 0
