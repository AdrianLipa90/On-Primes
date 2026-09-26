#!/usr/bin/env python3
"""Validator for the Mellin/additive window autocorrelation bridge."""
from __future__ import annotations

import math


def gaussian(u: float) -> float:
    return math.exp(-0.5 * u * u)


def gaussian_kernel(s: float) -> float:
    return math.sqrt(math.pi) * math.exp(-0.25 * s * s)


def pullback_G(t: float, Q: float, L: float) -> float:
    return math.exp(0.5 * t) * gaussian((math.exp(t) - Q) / L)


def simpson(f, a: float, b: float, n: int = 20000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4.0 * sum(f(a + (2 * k - 1) * h) for k in range(1, n // 2 + 1))
    total += 2.0 * sum(f(a + 2 * k * h) for k in range(1, n // 2))
    return total * h / 3.0


def main() -> None:
    max_pullback_error = 0.0
    for Q, L in [(20.0, 3.0), (100.0, 7.0), (1000.0, 30.0)]:
        for n in [2, 3, 5, 11, 29, 101, 503]:
            lhs = pullback_G(math.log(n), Q, L) / math.sqrt(n)
            rhs = gaussian((n - Q) / L)
            err = abs(lhs - rhs)
            max_pullback_error = max(max_pullback_error, err)
            assert err < 3e-15

    max_kernel_error = 0.0
    for s in [-3.0, -1.5, -0.5, 0.0, 0.75, 2.0, 4.0]:
        numerical = simpson(
            lambda u: gaussian(u) * gaussian(u + s),
            -10.0,
            10.0,
        )
        exact = gaussian_kernel(s)
        err = abs(numerical - exact)
        max_kernel_error = max(max_kernel_error, err)
        assert err < 2e-10

    # Translation identity for one pair n,m:
    max_translation_error = 0.0
    for n, m, L in [(10.0, 13.0, 4.0), (50.0, 47.0, 7.0), (100.0, 130.0, 20.0)]:
        numerical = simpson(
            lambda Q: gaussian((n - Q) / L) * gaussian((m - Q) / L),
            min(n, m) - 12.0 * L,
            max(n, m) + 12.0 * L,
        )
        exact = L * gaussian_kernel((m - n) / L)
        err = abs(numerical - exact)
        max_translation_error = max(max_translation_error, err)
        assert err < 3e-9

    print("MELLIN_ADDITIVE_WINDOW_AUTOCORRELATION_BRIDGE_V0_1: PASS")
    print("MAX_PULLBACK_ERROR=", max_pullback_error)
    print("MAX_GAUSSIAN_KERNEL_ERROR=", max_kernel_error)
    print("MAX_TRANSLATION_IDENTITY_ERROR=", max_translation_error)
    print("ZETA_ZERO_LIST_USED=false")
    print("STATUS=EXACT_WINDOW_COORDINATE_BRIDGE")


if __name__ == "__main__":
    main()
