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


def twin_local_dyadic_period(p: int, h: int) -> int:
    """Period of the residue orbit h -> 2h mod p relevant to the local observable."""
    p = int(p)
    h = int(h)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    return 1 if h % p == 0 else doubling_order_mod_prime(p)


def twin_local_orbit_values(p: int, h: int) -> tuple[Fraction, ...]:
    """Exact local-factor values over one dyadic residue period."""
    period = twin_local_dyadic_period(p, h)
    u = int(h) % int(p)
    out: list[Fraction] = []
    for _ in range(period):
        out.append(twin_quadruplet_local_factor(int(p), u))
        u = (2 * u) % int(p)
    return tuple(out)


def twin_local_orbit_mean(p: int, h: int) -> Fraction:
    """Exact mean of B_p(2^r h) over one local dyadic period."""
    values = twin_local_orbit_values(p, h)
    return sum(values, Fraction(0, 1)) / len(values)


def twin_local_orbit_variance(p: int, h: int) -> Fraction:
    """Exact variance of B_p(2^r h) over one local dyadic period."""
    values = twin_local_orbit_values(p, h)
    mean = sum(values, Fraction(0, 1)) / len(values)
    return sum((value - mean) ** 2 for value in values, Fraction(0, 1)) / len(values)


def twin_global_dyadic_period(primes: Sequence[int], h: int) -> int:
    """LCM period of the supplied local twin-factor channels under h -> 2h."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    period = 1
    for p in support:
        period = math.lcm(period, twin_local_dyadic_period(p, int(h)))
    return period


def twin_global_orbit_mean(primes: Sequence[int], h: int) -> Fraction:
    """Exact common-clock mean of the finite product of local twin factors."""
    support = tuple(int(p) for p in primes)
    period = twin_global_dyadic_period(support, int(h))
    total = Fraction(0, 1)
    residue_by_p = {p: int(h) % p for p in support}
    for _ in range(period):
        value = Fraction(1, 1)
        for p in support:
            value *= twin_quadruplet_local_factor(p, residue_by_p[p])
        total += value
        for p in support:
            residue_by_p[p] = (2 * residue_by_p[p]) % p
    return total / period


def twin_product_of_local_means(primes: Sequence[int], h: int) -> Fraction:
    """Product of independently averaged local twin-factor channels."""
    result = Fraction(1, 1)
    for p in tuple(int(p) for p in primes):
        result *= twin_local_orbit_mean(p, int(h))
    return result


def twin_dyadic_resonance_correction(primes: Sequence[int], h: int) -> Fraction:
    """Common-clock mean minus the product of independent local means."""
    support = tuple(int(p) for p in primes)
    return twin_global_orbit_mean(support, int(h)) - twin_product_of_local_means(support, int(h))


def local_periods_pairwise_coprime(primes: Sequence[int], h: int) -> bool:
    """Whether all nontrivial local dyadic periods are pairwise coprime."""
    periods = [twin_local_dyadic_period(int(p), int(h)) for p in primes]
    for i, a in enumerate(periods):
        for b in periods[i + 1:]:
            if math.gcd(a, b) != 1:
                return False
    return True


def twin_finite_dyadic_orbit_invariant(primes: Sequence[int], h: int) -> Fraction:
    """Finite-support product of local dyadic orbit means.

    This is exactly invariant under h -> 2**k * h for k>=0 on odd-prime support.
    """
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    result = Fraction(1, 1)
    for p in support:
        if not _is_prime_small(p) or p < 5:
            raise ValueError("support must contain distinct primes >= 5")
        result *= twin_local_orbit_mean(p, int(h))
    return result


def twin_local_mean_class(p: int, h: int) -> str:
    """Classify the local orbit mean for the twin-factor observable."""
    p = int(p)
    h = int(h)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    u = h % p
    if u == 0:
        return "zero-fixed"
    plus, minus = twin_special_residue_cycles(p)
    orbit = next(o for o in doubling_orbits_mod_prime(p) if u in o)
    if orbit == plus == minus:
        return "special-even"
    if orbit == plus or orbit == minus:
        return "special-odd"
    return "ordinary"


def twin_local_mean_closed_form(p: int, h: int) -> Fraction:
    """Closed-form local dyadic orbit mean of the twin-factor observable."""
    p = int(p)
    base, spike = twin_quadruplet_factor_decomposition(p)
    kind = twin_local_mean_class(p, int(h))
    if kind == "zero-fixed":
        return base + 2 * spike
    d = doubling_order_mod_prime(p)
    if kind == "special-even":
        return base + Fraction(2, d) * spike
    if kind == "special-odd":
        return base + Fraction(1, d) * spike
    return base


def twin_period_overlap_components(primes: Sequence[int], h: int) -> tuple[tuple[int, ...], ...]:
    """Connected components of the graph gcd(d_p(h), d_q(h)) > 1."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    periods = {p: twin_local_dyadic_period(p, int(h)) for p in support}
    unseen = set(support)
    components: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        unseen.remove(seed)
        component: list[int] = []
        while stack:
            p = stack.pop()
            component.append(p)
            linked = [q for q in tuple(unseen) if math.gcd(periods[p], periods[q]) > 1]
            for q in linked:
                unseen.remove(q)
                stack.append(q)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components))


def twin_component_factorized_mean(primes: Sequence[int], h: int) -> Fraction:
    """Product of exact common-clock means over period-overlap components."""
    result = Fraction(1, 1)
    for component in twin_period_overlap_components(primes, int(h)):
        result *= twin_global_orbit_mean(component, int(h))
    return result


def twin_connected_resonance_cumulant(primes: Sequence[int], h: int) -> Fraction:
    """Exact connected common-clock cumulant of the local twin-factor channels.

    Uses the moment-cumulant recursion with one distinguished anchor.
    Computational cost is exponential in the number of channels; this helper is
    intended for finite theorem/diagnostic supports rather than large scans.
    """
    support = tuple(sorted(int(p) for p in primes))
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    if not support:
        return Fraction(0, 1)

    moment_cache: dict[tuple[int, ...], Fraction] = {(): Fraction(1, 1)}
    cumulant_cache: dict[tuple[int, ...], Fraction] = {}

    def moment(subset: tuple[int, ...]) -> Fraction:
        subset = tuple(sorted(subset))
        if subset not in moment_cache:
            moment_cache[subset] = twin_global_orbit_mean(subset, int(h))
        return moment_cache[subset]

    def cumulant(subset: tuple[int, ...]) -> Fraction:
        subset = tuple(sorted(subset))
        if subset in cumulant_cache:
            return cumulant_cache[subset]
        if len(subset) == 1:
            value = moment(subset)
            cumulant_cache[subset] = value
            return value
        anchor = subset[0]
        rest = subset[1:]
        total = moment(subset)
        # Sum over all proper blocks B containing the anchor.
        for mask in range(1 << len(rest)):
            block = (anchor,) + tuple(rest[i] for i in range(len(rest)) if (mask >> i) & 1)
            if len(block) == len(subset):
                continue
            block_set = set(block)
            complement = tuple(x for x in subset if x not in block_set)
            total -= cumulant(tuple(sorted(block))) * moment(complement)
        cumulant_cache[subset] = total
        return total

    return cumulant(support)


def _bell_number(n: int) -> int:
    """Bell number B_n."""
    n = int(n)
    if n < 0:
        raise ValueError("n must be nonnegative")
    row = [1]
    for _ in range(n):
        new = [row[-1]]
        for j in range(len(row)):
            new.append(new[-1] + row[j])
        row = new
    return row[0]


def twin_centered_joint_moment(primes: Sequence[int], h: int) -> Fraction:
    """Exact common-clock moment of centered local twin-factor observables."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    if not support:
        return Fraction(1, 1)
    periods = [twin_local_dyadic_period(p, int(h)) for p in support]
    period = math.lcm(*periods)
    residues = {p: int(h) % p for p in support}
    means = {p: twin_local_orbit_mean(p, int(h)) for p in support}
    total = Fraction(0, 1)
    for _ in range(period):
        value = Fraction(1, 1)
        for p in support:
            value *= twin_quadruplet_local_factor(p, residues[p]) - means[p]
        total += value
        for p in support:
            residues[p] = (2 * residues[p]) % p
    return total / period


def twin_centered_moment_resonance_bound(primes: Sequence[int], h: int) -> Fraction:
    """Finite Fourier-resonance upper bound for a centered joint moment.

    |E prod X_p| <= 2^n * prod(alpha_p) / lcm(d_p(h)).
    """
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    if not support:
        return Fraction(1, 1)
    periods = [twin_local_dyadic_period(p, int(h)) for p in support]
    L = math.lcm(*periods)
    alpha_product = Fraction(1, 1)
    for p in support:
        _, alpha = twin_quadruplet_factor_decomposition(p)
        alpha_product *= alpha
    return Fraction(2 ** len(support), L) * alpha_product


def twin_connected_cumulant_fixed_order_bound(primes: Sequence[int], h: int) -> Fraction:
    """Crude rigorous fixed-order bound for the connected cumulant.

    For n>=2:
      |K(J;h)| <= Bell(n)*(n-1)!*2^n*prod(alpha_p)/max_p d_p(h).
    """
    support = tuple(int(p) for p in primes)
    n = len(support)
    if n < 2:
        raise ValueError("at least two channels are required")
    if len(set(support)) != n:
        raise ValueError("primes must be distinct")
    periods = [twin_local_dyadic_period(p, int(h)) for p in support]
    D = max(periods)
    alpha_product = Fraction(1, 1)
    for p in support:
        _, alpha = twin_quadruplet_factor_decomposition(p)
        alpha_product *= alpha
    coefficient = _bell_number(n) * math.factorial(n - 1) * (2 ** n)
    return Fraction(coefficient, D) * alpha_product


def twin_channel_is_dynamically_active(p: int, h: int) -> bool:
    """Whether the centered local observable is nonconstant along the dyadic orbit."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    if int(h) % p == 0:
        return False
    kind = twin_local_mean_class(p, int(h))
    return kind in {"special-even", "special-odd"}


def twin_background_factor(p: int) -> Fraction:
    """Generic p>=5 local factor beta_p for residues u not in {0,+2,-2}."""
    p = int(p)
    base, _ = twin_quadruplet_factor_decomposition(p)
    return base


def twin_zero_correction_ratio(p: int) -> Fraction:
    """Ratio B_p(0)/beta_p = (p-2)/(p-4)."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    return Fraction(p - 2, p - 4)


def twin_special_correction_ratio(p: int) -> Fraction:
    """Ratio B_p(+/-2)/beta_p = (p-3)/(p-4)."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    return Fraction(p - 3, p - 4)


def twin_finite_instantaneous_product(primes: Sequence[int], h: int, r: int) -> Fraction:
    """Finite product prod_p B_p(2**r h)."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    r = int(r)
    if r < 0:
        raise ValueError("r must be nonnegative")
    x = (2**r) * int(h)
    result = Fraction(1, 1)
    for p in support:
        result *= twin_quadruplet_local_factor(p, x)
    return result


def twin_finite_instantaneous_factorization(primes: Sequence[int], h: int, r: int) -> Fraction:
    """Finite baseline-times-finite-corrections factorization.

    For support P:
      prod_{p in P} B_p(x)
      = prod beta_p
        * prod_{p|h, p in P} (p-2)/(p-4)
        * prod_{p|(x^2-4), p in P} (p-3)/(p-4),
    with x=2**r h and p>=5.
    """
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    r = int(r)
    if r < 0:
        raise ValueError("r must be nonnegative")
    x = (2**r) * int(h)
    result = Fraction(1, 1)
    for p in support:
        if not _is_prime_small(p) or p < 5:
            raise ValueError("support must contain distinct primes >= 5")
        result *= twin_background_factor(p)
        if int(h) % p == 0:
            result *= twin_zero_correction_ratio(p)
        elif (x * x - 4) % p == 0:
            result *= twin_special_correction_ratio(p)
    return result


def twin_special_hit_density(p: int, h: int) -> Fraction:
    """Density of dyadic times with 2**r h == +/-2 mod p over one local orbit."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    if int(h) % p == 0:
        return Fraction(0, 1)
    kind = twin_local_mean_class(p, int(h))
    d = doubling_order_mod_prime(p)
    if kind == "special-even":
        return Fraction(2, d)
    if kind == "special-odd":
        return Fraction(1, d)
    return Fraction(0, 1)


def twin_local_log_orbit_mean(p: int, h: int) -> float:
    """Exact-period arithmetic mean of log B_p(2**r h), returned as float."""
    p = int(p)
    values = twin_local_orbit_values(p, int(h))
    return sum(math.log(float(v)) for v in values) / len(values)


def twin_local_log_orbit_formula(p: int, h: int) -> float:
    """Closed form for the local log-orbit mean."""
    p = int(p)
    beta = twin_background_factor(p)
    if int(h) % p == 0:
        return math.log(float(beta * twin_zero_correction_ratio(p)))
    density = twin_special_hit_density(p, int(h))
    return math.log(float(beta)) + float(density) * math.log(float(twin_special_correction_ratio(p)))


def twin_finite_log_geometric_mean(primes: Sequence[int], h: int, include_carriers: bool = False) -> float:
    """Finite-support dyadic-time mean of log local factors."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    total = 0.0
    if include_carriers:
        if int(h) % 6 != 0:
            raise ValueError("carrier factors p=2,3 are fixed only for h divisible by 6")
        total += math.log(27.0 / 2.0)
    for p in support:
        total += twin_local_log_orbit_formula(p, int(h))
    return total


def twin_special_hit_positions(p: int, h: int) -> tuple[int, ...]:
    """Dyadic-time residues in one local period where 2**r h == +/-2 mod p."""
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    if int(h) % p == 0:
        return ()
    d = doubling_order_mod_prime(p)
    u = int(h) % p
    hits: list[int] = []
    for r in range(d):
        if u in (2 % p, (-2) % p):
            hits.append(r)
        u = (2 * u) % p
    return tuple(hits)


def twin_joint_special_hit_density(p: int, q: int, h: int) -> Fraction:
    """Exact common-clock density of simultaneous +/-2 hits in channels p and q."""
    p = int(p)
    q = int(q)
    if p == q:
        return twin_special_hit_density(p, int(h))
    if not _is_prime_small(p) or p < 5 or not _is_prime_small(q) or q < 5:
        raise ValueError("p and q must be distinct primes >= 5")
    hp = twin_special_hit_positions(p, int(h))
    hq = twin_special_hit_positions(q, int(h))
    if not hp or not hq:
        return Fraction(0, 1)
    dp = doubling_order_mod_prime(p)
    dq = doubling_order_mod_prime(q)
    g = math.gcd(dp, dq)
    compatible = sum(1 for a in hp for b in hq if (a - b) % g == 0)
    return Fraction(compatible, math.lcm(dp, dq))


def twin_log_pair_covariance(p: int, q: int, h: int) -> float:
    """Covariance contribution of two log-correction channels."""
    p = int(p)
    q = int(q)
    wp = math.log(float(twin_special_correction_ratio(p)))
    wq = math.log(float(twin_special_correction_ratio(q)))
    dp = float(twin_special_hit_density(p, int(h)))
    dq = float(twin_special_hit_density(q, int(h)))
    joint = float(twin_joint_special_hit_density(p, q, int(h)))
    return wp * wq * (joint - dp * dq)


def twin_finite_log_variance(primes: Sequence[int], h: int) -> float:
    """Exact-period variance of the finite dynamic log correction, via densities."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    variance = 0.0
    for p in support:
        w = math.log(float(twin_special_correction_ratio(p)))
        delta = float(twin_special_hit_density(p, int(h)))
        variance += w * w * delta * (1.0 - delta)
    for i, p in enumerate(support):
        for q in support[i + 1 :]:
            variance += 2.0 * twin_log_pair_covariance(p, q, int(h))
    return variance


def twin_finite_log_fourier_coefficients(primes: Sequence[int], h: int) -> dict[Fraction, complex]:
    """Aggregate nonzero B2 Fourier coefficients of the finite centered log signal.

    Frequencies are represented in Q/Z by Fraction values in [0,1).
    """
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    coeffs: dict[Fraction, complex] = {}
    for p in support:
        if not _is_prime_small(p) or p < 5:
            raise ValueError("support must contain distinct primes >= 5")
        hits = twin_special_hit_positions(p, int(h))
        if not hits:
            continue
        d = doubling_order_mod_prime(p)
        w = math.log(float(twin_special_correction_ratio(p)))
        for m in range(1, d):
            c = sum(cmath.exp(-2j * math.pi * m * r / d) for r in hits) / d
            if abs(c) < 1e-15:
                continue
            freq = Fraction(m, d)
            coeffs[freq] = coeffs.get(freq, 0j) + w * c
    return coeffs


def twin_finite_log_parseval_power(primes: Sequence[int], h: int) -> float:
    """Sum of squared aggregated nonzero Fourier coefficients."""
    return sum(abs(c) ** 2 for c in twin_finite_log_fourier_coefficients(primes, int(h)).values())


def quadruplet_observable_period(p: int, h: int) -> int:
    """Minimal carrier period for the +/-2 twin observable under dyadic time.

    For p not dividing h this is ord_p(4) = ord_p(2)/gcd(ord_p(2),2).
    A zero-locked channel p|h is dynamically constant and is assigned period 1.
    """
    p = int(p)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    if int(h) % p == 0:
        return 1
    d = doubling_order_mod_prime(p)
    return d // math.gcd(d, 2)


def twin_quadratic_hit_phase(p: int, h: int) -> int | None:
    """Unique r mod ord_p(4) with 4**r h**2 == 4 mod p, if it exists."""
    p = int(p)
    h = int(h)
    if not _is_prime_small(p) or p < 5:
        raise ValueError("p must be a prime >= 5")
    if h % p == 0:
        return None
    e = quadruplet_observable_period(p, h)
    target = 4 % p
    h2 = (h * h) % p
    u = h2
    for r in range(e):
        if u == target:
            return r
        u = (4 * u) % p
    return None


def twin_quadratic_hit_density(p: int, h: int) -> Fraction:
    """Exact special-hit density in the compressed base-4 clock."""
    phase = twin_quadratic_hit_phase(int(p), int(h))
    if phase is None:
        return Fraction(0, 1)
    return Fraction(1, quadruplet_observable_period(int(p), int(h)))


def twin_quadratic_joint_hit_density(p: int, q: int, h: int) -> Fraction:
    """Exact joint density using one residue class per active base-4 channel."""
    p = int(p)
    q = int(q)
    if p == q:
        return twin_quadratic_hit_density(p, int(h))
    rp = twin_quadratic_hit_phase(p, int(h))
    rq = twin_quadratic_hit_phase(q, int(h))
    if rp is None or rq is None:
        return Fraction(0, 1)
    ep = quadruplet_observable_period(p, int(h))
    eq = quadruplet_observable_period(q, int(h))
    if (rp - rq) % math.gcd(ep, eq) != 0:
        return Fraction(0, 1)
    return Fraction(1, math.lcm(ep, eq))


def twin_fractional_special_multiplier(p: int, s: float) -> float:
    """b_{p,s} = ((p-3)/(p-4))**s - 1 for 0<s<1."""
    p = int(p)
    s = float(s)
    if not 0.0 < s < 1.0:
        raise ValueError("s must satisfy 0 < s < 1")
    return float(twin_special_correction_ratio(p)) ** s - 1.0


def twin_finite_fractional_common_clock_mean(primes: Sequence[int], h: int, s: float) -> float:
    """Direct finite-support common-clock mean of the dynamic factor^s."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    s = float(s)
    if not 0.0 < s < 1.0:
        raise ValueError("s must satisfy 0 < s < 1")
    periods = [quadruplet_observable_period(p, int(h)) for p in support]
    L = math.lcm(*periods) if periods else 1
    phases = {p: twin_quadratic_hit_phase(p, int(h)) for p in support}
    multipliers = {p: twin_fractional_special_multiplier(p, s) for p in support}
    total = 0.0
    for r in range(L):
        value = 1.0
        for p, e in zip(support, periods):
            phase = phases[p]
            if phase is not None and r % e == phase:
                value *= 1.0 + multipliers[p]
        total += value
    return total / L


def twin_finite_fractional_subset_mean(primes: Sequence[int], h: int, s: float) -> float:
    """Finite subset/CRT expansion of the same fractional common-clock mean."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    s = float(s)
    if not 0.0 < s < 1.0:
        raise ValueError("s must satisfy 0 < s < 1")
    phases = {p: twin_quadratic_hit_phase(p, int(h)) for p in support}
    periods = {p: quadruplet_observable_period(p, int(h)) for p in support}
    b = {p: twin_fractional_special_multiplier(p, s) for p in support}
    total = 1.0
    n = len(support)
    for mask in range(1, 1 << n):
        chosen = [support[i] for i in range(n) if (mask >> i) & 1]
        if any(phases[p] is None for p in chosen):
            continue
        compatible = True
        for i, p in enumerate(chosen):
            for q in chosen[i + 1 :]:
                if (phases[p] - phases[q]) % math.gcd(periods[p], periods[q]) != 0:
                    compatible = False
                    break
            if not compatible:
                break
        if not compatible:
            continue
        L = math.lcm(*(periods[p] for p in chosen))
        weight = 1.0
        for p in chosen:
            weight *= b[p]
        total += weight / L
    return total


def twin_real_moment_multiplier(p: int, s: float) -> float:
    """b_{p,s}=((p-3)/(p-4))**s-1 for any finite real s."""
    p = int(p)
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    return float(twin_special_correction_ratio(p)) ** s - 1.0


def twin_finite_real_moment_common_clock(primes: Sequence[int], h: int, s: float) -> float:
    """Direct finite-support common-clock mean of dynamic factor**s."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    periods = [quadruplet_observable_period(p, int(h)) for p in support]
    L = math.lcm(*periods) if periods else 1
    phases = {p: twin_quadratic_hit_phase(p, int(h)) for p in support}
    multipliers = {p: twin_real_moment_multiplier(p, s) for p in support}
    total = 0.0
    for r in range(L):
        value = 1.0
        for p, e in zip(support, periods):
            phase = phases[p]
            if phase is not None and r % e == phase:
                value *= 1.0 + multipliers[p]
        total += value
    return total / L


def twin_finite_real_moment_subset_mean(primes: Sequence[int], h: int, s: float) -> float:
    """Finite CRT subset expansion for a real moment exponent s."""
    support = tuple(int(p) for p in primes)
    if len(set(support)) != len(support):
        raise ValueError("primes must be distinct")
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    phases = {p: twin_quadratic_hit_phase(p, int(h)) for p in support}
    periods = {p: quadruplet_observable_period(p, int(h)) for p in support}
    b = {p: twin_real_moment_multiplier(p, s) for p in support}
    total = 1.0
    n = len(support)
    for mask in range(1, 1 << n):
        chosen = [support[i] for i in range(n) if (mask >> i) & 1]
        if any(phases[p] is None for p in chosen):
            continue
        compatible = True
        for i, p in enumerate(chosen):
            for q in chosen[i + 1 :]:
                if (phases[p] - phases[q]) % math.gcd(periods[p], periods[q]) != 0:
                    compatible = False
                    break
            if not compatible:
                break
        if not compatible:
            continue
        L = math.lcm(*(periods[p] for p in chosen))
        weight = 1.0
        for p in chosen:
            weight *= b[p]
        total += weight / L
    return total
