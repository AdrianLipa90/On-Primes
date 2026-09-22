"""Finite prime-power memory in dyadic fibre coordinates."""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, floor, log

from .analytic import primes_up_to
from .dyadic import dyadic_address


@dataclass(frozen=True)
class PrimePowerEvent:
    p: int
    m: int
    q: int
    time: float
    weight: float
    a: int
    k: int
    defect: float


def prime_power_events_up_to_log_time(t: float) -> tuple[PrimePowerEvent, ...]:
    """Return all p^m with m*log(p) <= t, weighted by log(p)/sqrt(p^m)."""
    if t < 0:
        raise ValueError("t must be non-negative")
    x_max = floor(exp(t) + 1e-12)
    events: list[PrimePowerEvent] = []
    for p in primes_up_to(x_max):
        a, k = dyadic_address(p)
        defect = log(1.0 + 1.0 / p)
        q = p
        m = 1
        while q <= x_max:
            event_time = m * log(p)
            if event_time <= t + 1e-12:
                events.append(
                    PrimePowerEvent(
                        p=p,
                        m=m,
                        q=q,
                        time=event_time,
                        weight=log(p) / (q ** 0.5),
                        a=a,
                        k=k,
                        defect=defect,
                    )
                )
            if q > x_max // p:
                break
            q *= p
            m += 1
    events.sort(key=lambda e: (e.time, e.p, e.m))
    return tuple(events)


def prime_power_memory(t: float) -> float:
    """Triangular signed-memory magnitude from the finite prime-power measure."""
    return sum(e.weight * (t - e.time) for e in prime_power_events_up_to_log_time(t))


def dyadic_memory_components(t: float) -> tuple[float, float, float]:
    """Return (K_mem, A_mem, D_mem) with M=log(2)K_mem+A_mem-D_mem."""
    k_mem = 0.0
    a_mem = 0.0
    d_mem = 0.0
    for e in prime_power_events_up_to_log_time(t):
        kernel = (e.q ** -0.5) * (t - e.time)
        k_mem += e.k * kernel
        a_mem += log(e.a) * kernel
        d_mem += e.defect * kernel
    return k_mem, a_mem, d_mem


def reconstructed_prime_power_memory(t: float) -> float:
    """Reconstruct prime-power memory from dyadic components."""
    k_mem, a_mem, d_mem = dyadic_memory_components(t)
    return log(2.0) * k_mem + a_mem - d_mem
