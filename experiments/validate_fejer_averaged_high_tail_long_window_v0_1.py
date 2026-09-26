#!/usr/bin/env python3
"""Finite algebra checks for the Fejer long-window crosswalk.

This validator checks only the combinatorial Fejer/correlation alignment and
its boundary bound. It does not numerically prove the external
Saffari--Vaughan asymptotic.
"""
from __future__ import annotations

import math
import random


def fixed_start_correlation(a, X: int, h: int) -> float:
    return sum(a[n] * a[n + h] for n in range(X + 1, 2 * X + 1))


def fejer_correlation_average(a, X: int, L: int) -> float:
    H = L - 1
    total = fixed_start_correlation(a, X, 0)
    total += 2.0 * sum(
        (1.0 - h / L) * fixed_start_correlation(a, X, h)
        for h in range(1, H + 1)
    )
    return total / L


def sliding_energy(a, X: int, L: int) -> float:
    return sum(
        sum(a[m + j] for j in range(1, L + 1)) ** 2
        for m in range(X, 2 * X)
    )


def main() -> None:
    rng = random.Random(20260926)
    max_ratio = 0.0

    for X in [30, 50, 80]:
        for L in [2, 3, 5, 8, 12]:
            if L > X:
                continue
            a = [0.0] * (2 * X + L + 5)
            for n in range(1, len(a)):
                a[n] = 0.1 + 3.0 * rng.random()

            avg = fejer_correlation_average(a, X, L)
            energy = sliding_energy(a, X, L)
            difference = abs(energy - L * L * avg)

            max_a = max(a)
            bound = 4.0 * (L ** 3) * (max_a ** 2)
            assert difference <= bound + 1e-12
            max_ratio = max(max_ratio, difference / bound)

    print("FEJER_AVERAGED_HIGH_TAIL_LONG_WINDOW_CROSSWALK_V0_1: PASS")
    print("MAX_BOUNDARY_TO_BOUND_RATIO=", max_ratio)
    print("SAFFARI_VAUGHAN_ASYMPTOTIC=STANDARD_EXTERNAL_NOT_REPROVED")
    print("FIXED_SHIFT_TWIN_PRIME_ASYMPTOTIC_USED=false")
    print("STATUS=FINITE_CROSSWALK_PASS")


if __name__ == "__main__":
    main()
