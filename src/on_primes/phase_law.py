"""Exact arithmetic phase utilities for On-Primes.

The module keeps exact residue data separate from floating complex renderings.
No claim is made that pair-correlation spectra uniquely reconstruct an ordered
point process; exact reconstruction here uses the ordered gap stream.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
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


def _is_prime_small(n: int) -> bool:
    n = int(n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def _mobius(n: int) -> int:
    n = int(n)
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def _euler_phi(n: int) -> int:
    n = int(n)
    if n <= 0:
        raise ValueError("n must be positive")
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p = 3 if p == 2 else p + 2
    if x > 1:
        result -= result // x
    return result


def _divisors(n: int) -> tuple[int, ...]:
    n = int(n)
    if n <= 0:
        raise ValueError("n must be positive")
    low: list[int] = []
    high: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
        d += 1
    return tuple(low + high[::-1])


def ramanujan_sum(q: int, n: int) -> int:
    """Exact Ramanujan sum c_q(n)."""
    q = int(q)
    if q <= 0:
        raise ValueError("q must be positive")
    g = math.gcd(q, int(n))
    return sum(d * _mobius(q // d) for d in _divisors(g))


def prime_pair_local_factor(p: int, h: int) -> Fraction:
    """Local Hardy--Littlewood prime-pair factor at a prime p."""
    p = int(p)
    if not _is_prime_small(p):
        raise ValueError("p must be prime")
    return Fraction(1, 1) + Fraction(ramanujan_sum(p, int(h)), (p - 1) ** 2)


def finite_prime_pair_singular_product(h: int, primes: Iterable[int]) -> Fraction:
    """Finite Euler product of prime-pair local factors."""
    result = Fraction(1, 1)
    seen: set[int] = set()
    for p in primes:
        p = int(p)
        if p in seen:
            raise ValueError("primes must be distinct")
        seen.add(p)
        result *= prime_pair_local_factor(p, int(h))
    return result


def finite_prime_pair_ramanujan_expansion(h: int, primes: Sequence[int]) -> Fraction:
    """Exact squarefree Ramanujan expansion over a supplied finite prime support.

    This equals finite_prime_pair_singular_product(h, primes) exactly.
    """
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support) or any(not _is_prime_small(p) for p in support):
        raise ValueError("primes must be distinct primes")
    total = Fraction(0, 1)
    for mask in range(1 << len(support)):
        q = 1
        for i, p in enumerate(support):
            if (mask >> i) & 1:
                q *= p
        total += Fraction(ramanujan_sum(q, int(h)), _euler_phi(q) ** 2)
    return total


def twin_quadruplet_residue_count(p: int, h: int) -> int:
    """nu_p for H_h={0,2,h,h+2}, the two-twin-pair offset pattern."""
    p = int(p)
    if not _is_prime_small(p):
        raise ValueError("p must be prime")
    h = int(h)
    return len({0 % p, 2 % p, h % p, (h + 2) % p})


def twin_quadruplet_local_factor(p: int, h: int) -> Fraction:
    """Local k-tuple singular-series factor for H_h={0,2,h,h+2}."""
    p = int(p)
    nu = twin_quadruplet_residue_count(p, int(h))
    return Fraction(p - nu, p) / (Fraction(p - 1, p) ** 4)


def finite_twin_quadruplet_singular_product(h: int, primes: Iterable[int]) -> Fraction:
    """Finite local product for the two-twin-pair pattern H_h."""
    result = Fraction(1, 1)
    seen: set[int] = set()
    for p in primes:
        p = int(p)
        if p in seen:
            raise ValueError("primes must be distinct")
        seen.add(p)
        result *= twin_quadruplet_local_factor(p, int(h))
    return result


def twin_gap_mod6_admissible(h: int) -> bool:
    """Admissibility against the p=2 and p=3 local channels."""
    h = int(h)
    return twin_quadruplet_residue_count(2, h) < 2 and twin_quadruplet_residue_count(3, h) < 3


def twin_quadruplet_dyadic_local_orbit(p: int, h: int, steps: int) -> tuple[tuple[int, Fraction], ...]:
    """Local singular-factor observable along h -> 2h mod p."""
    p = int(p)
    steps = int(steps)
    if not _is_prime_small(p):
        raise ValueError("p must be prime")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    residue = int(h) % p
    out: list[tuple[int, Fraction]] = []
    for _ in range(steps):
        out.append((residue, twin_quadruplet_local_factor(p, residue)))
        residue = (2 * residue) % p
    return tuple(out)


def even_sector_pair_singular_dyadic_invariant(h: int, primes: Iterable[int]) -> bool:
    """Finite-product invariance S_P(2h)=S_P(h) for even h."""
    h = int(h)
    if h % 2:
        raise ValueError("h must be even")
    support = tuple(int(p) for p in primes)
    return finite_prime_pair_singular_product(h, support) == finite_prime_pair_singular_product(2 * h, support)


def doubling_order_mod_prime(p: int) -> int:
    """Multiplicative order of 2 modulo an odd prime p."""
    p = int(p)
    if not _is_prime_small(p) or p == 2:
        raise ValueError("p must be an odd prime")
    x = 2 % p
    order = 1
    while x != 1:
        x = (2 * x) % p
        order += 1
    return order


def doubling_orbits_mod_prime(p: int) -> tuple[tuple[int, ...], ...]:
    """Orbit decomposition of u -> 2u mod p on Z/pZ."""
    p = int(p)
    if not _is_prime_small(p) or p == 2:
        raise ValueError("p must be an odd prime")
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for seed in range(p):
        if seed in seen:
            continue
        orbit: list[int] = []
        u = seed
        while u not in seen:
            seen.add(u)
            orbit.append(u)
            u = (2 * u) % p
        out.append(tuple(orbit))
    return tuple(out)


def dyadic_transfer_spectrum_multiplicities(p: int) -> tuple[int, dict[int, int]]:
    """Exact multiplicities of d-th-root eigenmodes of the doubling permutation.

    Returns (d, multiplicities), where key m denotes exp(2*pi*i*m/d).
    The zero residue contributes one additional eigenvalue 1.
    """
    p = int(p)
    d = doubling_order_mod_prime(p)
    cycles = (p - 1) // d
    multiplicities = {m: cycles for m in range(d)}
    multiplicities[0] += 1
    return d, multiplicities


def twin_quadruplet_factor_decomposition(p: int) -> tuple[Fraction, Fraction]:
    """Return (baseline, spike) for p>=5.

    B_p(u)=baseline + spike*(2*1_{u=0}+1_{u=2}+1_{u=-2}).
    """
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    spike = Fraction(p**3, (p - 1) ** 4)
    baseline = Fraction(p**3 * (p - 4), (p - 1) ** 4)
    return baseline, spike


def twin_special_residue_cycles(p: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return doubling cycles containing +2 and -2 modulo p."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    orbits = doubling_orbits_mod_prime(p)
    plus = next(orbit for orbit in orbits if 2 in orbit)
    minus_residue = (-2) % p
    minus = next(orbit for orbit in orbits if minus_residue in orbit)
    return plus, minus


def twin_special_mode_support(p: int) -> tuple[int, ...]:
    """Nonzero Fourier-mode support of the baseline-subtracted +2 cycle.

    If ord_p(2) is even, +2 and -2 are half an orbit apart and odd modes cancel.
    If ord_p(2) is odd, -2 lies in a different cycle and every mode is present
    on either special cycle.
    """
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    d = doubling_order_mod_prime(p)
    if d % 2 == 0:
        return tuple(m for m in range(d) if m % 2 == 0)
    return tuple(range(d))


def twin_special_cycles_coincide(p: int) -> bool:
    """Whether +2 and -2 lie on the same doubling cycle modulo p."""
    plus, minus = twin_special_residue_cycles(p)
    return plus == minus
