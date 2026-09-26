"""Exact arithmetic phase utilities for On-Primes.

The module keeps exact residue data separate from floating complex renderings.
No claim is made that pair-correlation spectra uniquely reconstruct an ordered
point process; exact reconstruction here uses the ordered gap stream.
"""

from __future__ import annotations

import cmath
import math
from collections.abc import Iterable, Mapping, Sequence


def phase_residue(delta: int, modulus: int) -> int:
    """Return the exact modular phase coordinate delta mod modulus."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return int(delta) % int(modulus)


def phase_value(delta: int, modulus: int, harmonic: int = 1) -> complex:
    """Render an exact residue coordinate as a unit complex phase."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    residue = (int(harmonic) * int(delta)) % int(modulus)
    return cmath.exp(2j * math.pi * residue / modulus)


def phase_difference(x: int, y: int, modulus: int, harmonic: int = 1) -> complex:
    """Character ratio chi(y) * conjugate(chi(x)) = chi(y-x)."""
    return phase_value(y - x, modulus, harmonic)


def ordered_gaps(points: Sequence[int]) -> tuple[int, ...]:
    """Return positive consecutive gaps of a strictly increasing integer sequence."""
    pts = tuple(int(x) for x in points)
    if any(b <= a for a, b in zip(pts, pts[1:])):
        raise ValueError("points must be strictly increasing")
    return tuple(b - a for a, b in zip(pts, pts[1:]))


def reconstruct_from_gaps(anchor: int, gaps: Iterable[int]) -> tuple[int, ...]:
    """Reconstruct the ordered point sequence from one anchor and ordered gaps."""
    out = [int(anchor)]
    current = int(anchor)
    for gap in gaps:
        gap = int(gap)
        if gap <= 0:
            raise ValueError("gaps must be positive")
        current += gap
        out.append(current)
    return tuple(out)


def prime_power_signature(delta: int, prime_powers: Mapping[int, int]) -> dict[int, int]:
    """Return exact residues modulo p**j for pairwise-distinct prime bases."""
    sig: dict[int, int] = {}
    for p, exponent in prime_powers.items():
        p = int(p)
        exponent = int(exponent)
        if p <= 1 or exponent <= 0:
            raise ValueError("bases must exceed 1 and exponents must be positive")
        modulus = p**exponent
        sig[modulus] = int(delta) % modulus
    return sig


def crt_reconstruct(signature: Mapping[int, int]) -> tuple[int, int]:
    """Reconstruct x modulo M from pairwise-coprime residue coordinates."""
    items = [(int(m), int(r) % int(m)) for m, r in signature.items()]
    if not items:
        return (0, 1)
    for i, (m, _) in enumerate(items):
        if m <= 0:
            raise ValueError("moduli must be positive")
        for n, _ in items[i + 1 :]:
            if math.gcd(m, n) != 1:
                raise ValueError("moduli must be pairwise coprime")
    M = math.prod(m for m, _ in items)
    x = 0
    for m, r in items:
        Mi = M // m
        inv = pow(Mi, -1, m)
        x = (x + r * Mi * inv) % M
    return (x, M)


def cyclic_autocorrelation(signal: Sequence[complex]) -> tuple[complex, ...]:
    """Cyclic autocorrelation C[h] = sum_n f[n+h] conjugate(f[n])."""
    data = tuple(complex(v) for v in signal)
    N = len(data)
    if N == 0:
        return ()
    return tuple(
        sum(data[(n + h) % N] * data[n].conjugate() for n in range(N))
        for h in range(N)
    )


def dft_power(signal: Sequence[complex]) -> tuple[float, ...]:
    """Unnormalised DFT power |F[k]|^2 on the N-th roots of unity."""
    data = tuple(complex(v) for v in signal)
    N = len(data)
    if N == 0:
        return ()
    powers: list[float] = []
    for k in range(N):
        F = sum(
            data[n] * cmath.exp(-2j * math.pi * k * n / N)
            for n in range(N)
        )
        powers.append(float((F * F.conjugate()).real))
    return tuple(powers)


def inverse_power_to_autocorrelation(power: Sequence[float]) -> tuple[complex, ...]:
    """Inverse DFT of power; equals cyclic autocorrelation for matching convention."""
    p = tuple(float(v) for v in power)
    N = len(p)
    if N == 0:
        return ()
    return tuple(
        sum(p[k] * cmath.exp(2j * math.pi * k * h / N) for k in range(N)) / N
        for h in range(N)
    )


def dyadic_gap_transport(delta: int, iterations: int = 1) -> int:
    """Gap transport under T(x)=2x+1: Delta -> 2**iterations * Delta."""
    iterations = int(iterations)
    if iterations < 0:
        raise ValueError("iterations must be nonnegative")
    return (2**iterations) * int(delta)


def fibre_phase_orbit(a: int, modulus: int, length: int, start_k: int = 0) -> tuple[int, ...]:
    """Exact residue orbit u_k = a*2**k mod modulus.

    The update law is u_{k+1} = 2*u_k mod modulus; as unit phases this is
    z_{k+1}=z_k**2.
    """
    a = int(a)
    modulus = int(modulus)
    length = int(length)
    start_k = int(start_k)
    if modulus <= 1:
        raise ValueError("modulus must exceed 1")
    if length < 0 or start_k < 0:
        raise ValueError("length and start_k must be nonnegative")
    u = (a * pow(2, start_k, modulus)) % modulus
    out: list[int] = []
    for _ in range(length):
        out.append(u)
        u = (2 * u) % modulus
    return tuple(out)


def fibre_obstruction_hits(a: int, divisor: int, length: int, start_k: int = 0) -> tuple[int, ...]:
    """Indices k for which divisor | (a*2**k - 1), detected as phase hits u_k=1."""
    orbit = fibre_phase_orbit(a, divisor, length, start_k)
    return tuple(start_k + i for i, residue in enumerate(orbit) if residue == 1 % divisor)
