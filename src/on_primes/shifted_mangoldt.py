"""Shifted von Mangoldt decomposition on p+1."""

from __future__ import annotations

from math import isqrt, log

from .analytic import classical_log_derivative_partial, primes_up_to


def factorize(n: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("factorize expects a positive integer")
    out: dict[int, int] = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            out[f] = out.get(f, 0) + 1
            n //= f
        f += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def shifted_von_mangoldt_channels(p: int) -> tuple[tuple[int, int, float], ...]:
    """Return (r,j,log r) for all prime powers r**j dividing p+1."""
    if p < 2:
        raise ValueError("p must be >= 2")
    fac = factorize(p + 1)
    channels: list[tuple[int, int, float]] = []
    for r in sorted(fac):
        for j in range(1, fac[r] + 1):
            channels.append((r, j, log(r)))
    return tuple(channels)


def shifted_log_sum(p: int) -> float:
    """Return sum_{r^j | p+1} log r = log(p+1)."""
    return sum(weight for _, _, weight in shifted_von_mangoldt_channels(p))


def shifted_tower_partial(s: complex, prime_limit: int) -> complex:
    """Return sum_p log(p+1)/(p**s-1) using prime-power divisor channels."""
    total = 0j
    for p in primes_up_to(prime_limit):
        denom = p ** s - 1
        for _, _, weight in shifted_von_mangoldt_channels(p):
            total += weight / denom
    return total


def defect_partial_local(s: complex, prime_limit: int) -> complex:
    """Return sum_p log(1+1/p)/(p**s-1)."""
    total = 0j
    for p in primes_up_to(prime_limit):
        total += log(1.0 + 1.0 / p) / (p ** s - 1)
    return total


def reconstructed_log_derivative_from_shifted_tower(s: complex, prime_limit: int) -> complex:
    """Finite identity: shifted tower minus defect equals classical prime sum."""
    return shifted_tower_partial(s, prime_limit) - defect_partial_local(s, prime_limit)


def base_channel_partial(r: int, s: complex, prime_limit: int) -> complex:
    """Contribution of one base prime r across all powers r**j | p+1."""
    if r < 2:
        raise ValueError("r must be >= 2")
    total = 0j
    for p in primes_up_to(prime_limit):
        e = factorize(p + 1).get(r, 0)
        if e:
            total += e * log(r) / (p ** s - 1)
    return total
