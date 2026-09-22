"""Exact dyadic-fibre primitives for the On-Primes programme.

All arithmetic identities in this module are elementary. Numerical scans built
on top of them must not be promoted to primality theorems.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt, log, log1p


def v2(n: int) -> int:
    """Return the exponent of 2 in a positive integer n."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("v2 expects a positive integer")
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def odd_part(n: int) -> int:
    """Return the odd part of a positive integer n."""
    return n >> v2(n)


def dyadic_address(n: int) -> tuple[int, int]:
    """Return the unique (a, k) with n + 1 = a*2**k and a odd."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("dyadic_address expects an integer n >= 1")
    m = n + 1
    k = v2(m)
    a = m >> k
    return a, k


def fibre_value(a: int, k: int) -> int:
    """Return x_{a,k} = a*2**k - 1 for odd positive a and k >= 0."""
    if not isinstance(a, int) or isinstance(a, bool) or a <= 0 or a % 2 == 0:
        raise ValueError("a must be a positive odd integer")
    if not isinstance(k, int) or isinstance(k, bool) or k < 0:
        raise ValueError("k must be a non-negative integer")
    return a * (1 << k) - 1


def sophie_step(x):
    """Affine Sophie-Germain/Cunningham step T(x) = 2*x + 1."""
    return 2 * x + 1


def is_prime(n: int) -> bool:
    """Deterministic primality test suitable for reference-scale experiments."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    f = 5
    while f <= limit:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def prime_mask(a: int, k_max: int) -> tuple[bool, ...]:
    """Return M_a(k) for k = 0..k_max inclusive."""
    if not isinstance(k_max, int) or isinstance(k_max, bool) or k_max < 0:
        raise ValueError("k_max must be a non-negative integer")
    return tuple(is_prime(fibre_value(a, k)) for k in range(k_max + 1))


def cunningham_run(a: int, start_k: int = 0, max_length: int = 10_000) -> tuple[int, ...]:
    """Return the consecutive prime run in one fibre starting at start_k."""
    if start_k < 0 or max_length < 0:
        raise ValueError("start_k and max_length must be non-negative")
    run: list[int] = []
    for j in range(max_length):
        value = fibre_value(a, start_k + j)
        if not is_prime(value):
            break
        run.append(value)
    return tuple(run)


def half_boundary_prime_preimages(n_max: int) -> tuple[Fraction, ...]:
    """Scan x=n+1/2, 0<=n<=n_max, returning those with T(x) prime."""
    if not isinstance(n_max, int) or isinstance(n_max, bool) or n_max < 0:
        raise ValueError("n_max must be a non-negative integer")
    out: list[Fraction] = []
    for n in range(n_max + 1):
        x = Fraction(2 * n + 1, 2)
        y = sophie_step(x)
        if y.denominator == 1 and is_prime(y.numerator):
            out.append(x)
    return tuple(out)


def log_fibre_coordinate(a: int, k: int) -> float:
    """Return log(a) + k*log(2) = log(x_{a,k}+1)."""
    fibre_value(a, k)  # validation
    return log(a) + k * log(2.0)


def log_prime_defect(p: int) -> float:
    """Return delta_p = log(1 + 1/p) for a prime p."""
    if not is_prime(p):
        raise ValueError("p must be prime")
    return log1p(1.0 / p)
