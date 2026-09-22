"""Exact r-adic valuation shells for p+1."""

from __future__ import annotations

from .dyadic import is_prime


def vp(n: int, r: int) -> int:
    """Return v_r(n) for prime r and positive integer n."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not is_prime(r):
        raise ValueError("r must be prime")
    j = 0
    while n % r == 0:
        n //= r
        j += 1
    return j


def exact_shifted_shell_residues(r: int, j: int) -> tuple[int, tuple[int, ...]]:
    """Residues mod r**(j+1) with v_r(n+1)=j, for j>=1."""
    if not is_prime(r):
        raise ValueError("r must be prime")
    if not isinstance(j, int) or isinstance(j, bool) or j < 1:
        raise ValueError("j must be an integer >= 1")
    modulus = r ** (j + 1)
    base = r ** j - 1
    residues = tuple((base + c * (r ** j)) % modulus for c in range(r - 1))
    return modulus, tuple(sorted(residues))


def in_exact_shifted_shell(n: int, r: int, j: int) -> bool:
    """True iff v_r(n+1)=j."""
    modulus, residues = exact_shifted_shell_residues(r, j)
    return n % modulus in set(residues)
