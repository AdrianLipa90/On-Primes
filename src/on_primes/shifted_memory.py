"""Shifted von Mangoldt channel decomposition of prime-power memory."""

from __future__ import annotations

from collections import defaultdict
from math import exp, floor, log

from .analytic import primes_up_to
from .shifted_mangoldt import factorize


def shifted_memory_channels(t: float) -> dict[int, float]:
    """Return base-prime channel contributions before subtracting the defect."""
    if t < 0:
        raise ValueError("t must be non-negative")
    x_max = floor(exp(t) + 1e-12)
    out: dict[int, float] = defaultdict(float)
    for p in primes_up_to(x_max):
        fac = factorize(p + 1)
        q = p
        m = 1
        while q <= x_max:
            event_time = m * log(p)
            if event_time <= t + 1e-12:
                kernel = (q ** -0.5) * (t - event_time)
                for r, exponent in fac.items():
                    out[r] += exponent * log(r) * kernel
            if q > x_max // p:
                break
            q *= p
            m += 1
    return dict(sorted(out.items()))


def shifted_memory_defect(t: float) -> float:
    """Return the positive defect memory from log(1+1/p)."""
    if t < 0:
        raise ValueError("t must be non-negative")
    x_max = floor(exp(t) + 1e-12)
    total = 0.0
    for p in primes_up_to(x_max):
        delta = log(1.0 + 1.0 / p)
        q = p
        m = 1
        while q <= x_max:
            event_time = m * log(p)
            if event_time <= t + 1e-12:
                total += delta * (q ** -0.5) * (t - event_time)
            if q > x_max // p:
                break
            q *= p
            m += 1
    return total


def shifted_memory_total(t: float) -> float:
    """Return sum of all shifted channels minus defect."""
    channels = shifted_memory_channels(t)
    return sum(channels.values()) - shifted_memory_defect(t)
