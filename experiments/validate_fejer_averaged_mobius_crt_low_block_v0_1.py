#!/usr/bin/env python3
"""Validator for the Fejer-averaged Mobius-CRT low block."""
from __future__ import annotations

import math


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def fejer_weight(H: int, h: int) -> float:
    if abs(h) > H:
        return 0.0
    return 1.0 - abs(h) / (H + 1)


def gate_average_direct(H: int, g: int) -> float:
    L = H + 1
    return sum(
        fejer_weight(H, h)
        for h in range(-H, H + 1)
        if h % g == 0
    ) / L


def gate_average_closed(H: int, g: int) -> float:
    L = H + 1
    r = L % g
    return 1.0 / g + r * (g - r) / (g * L * L)


def density_coefficient(h: int, R: int, mu: list[int]) -> float:
    total = 0.0
    for d in range(1, R + 1):
        if mu[d] == 0:
            continue
        for e in range(1, R + 1):
            if mu[e] == 0:
                continue
            g = math.gcd(d, e)
            if h % g == 0:
                total += (
                    mu[d] * mu[e] * math.log(d) * math.log(e)
                    / (d * e // g)
                )
    return total


def averaged_density_direct(H: int, R: int, mu: list[int]) -> float:
    L = H + 1
    return (
        density_coefficient(0, R, mu)
        + 2.0
        * sum(
            (1.0 - h / L) * density_coefficient(h, R, mu)
            for h in range(1, H + 1)
        )
    ) / L


def averaged_density_factorized(H: int, R: int, mu: list[int]):
    L = H + 1
    S = sum(
        mu[d] * math.log(d) / d
        for d in range(1, R + 1)
        if mu[d]
    )
    correction = 0.0
    for d in range(1, R + 1):
        if mu[d] == 0:
            continue
        for e in range(1, R + 1):
            if mu[e] == 0:
                continue
            g = math.gcd(d, e)
            r = L % g
            correction += (
                mu[d]
                * mu[e]
                * math.log(d)
                * math.log(e)
                * r
                * (g - r)
                / (d * e * L * L)
            )
    return S * S + correction, S, correction


def correction_bound(H: int, R: int) -> float:
    L = H + 1
    return (
        math.log(R) ** 2
        * (5.0 * R + (1.0 + math.log(R)) ** 2)
        / (4.0 * L * L)
    )


def crt_count_bruteforce(X: int, h: int, d: int, e: int) -> int:
    return sum(
        1
        for n in range(1, X + 1)
        if n % d == 0 and (n + h) % e == 0
    )


def low_block(X: int, h: int, R: int, mu: list[int]) -> float:
    total = 0.0
    for d in range(1, R + 1):
        if mu[d] == 0:
            continue
        for e in range(1, R + 1):
            if mu[e] == 0:
                continue
            total += (
                mu[d]
                * mu[e]
                * math.log(d)
                * math.log(e)
                * crt_count_bruteforce(X, h, d, e)
            )
    return total


def averaged_low_block(X: int, H: int, R: int, mu: list[int]) -> float:
    L = H + 1
    return (
        low_block(X, 0, R, mu)
        + 2.0
        * sum(
            (1.0 - h / L) * low_block(X, h, R, mu)
            for h in range(1, H + 1)
        )
    ) / L


def main() -> None:
    mu = mobius_sieve(128)

    max_gate_error = 0.0
    for H in [2, 5, 10, 31, 64]:
        for g in range(1, 50):
            err = abs(
                gate_average_direct(H, g)
                - gate_average_closed(H, g)
            )
            max_gate_error = max(max_gate_error, err)
            assert err < 2e-15

    max_factorization_error = 0.0
    max_correction_to_bound = 0.0
    for H in [5, 10, 31, 64]:
        for R in [3, 5, 8, 12, 20]:
            direct = averaged_density_direct(H, R, mu)
            factored, _, correction = averaged_density_factorized(H, R, mu)
            err = abs(direct - factored)
            max_factorization_error = max(max_factorization_error, err)
            assert err < 3e-12

            bound = correction_bound(H, R)
            assert abs(correction) <= bound + 1e-14
            if bound > 0.0:
                max_correction_to_bound = max(
                    max_correction_to_bound,
                    abs(correction) / bound,
                )

    max_low_block_error_to_bound = 0.0
    for X in [50, 100, 200]:
        for H in [3, 7, 12]:
            for R in [3, 5, 8]:
                observed = averaged_low_block(X, H, R, mu)
                density = averaged_density_direct(H, R, mu)
                error = abs(observed - X * density)
                bound = (R * math.log(R)) ** 2
                assert error <= bound + 1e-10
                max_low_block_error_to_bound = max(
                    max_low_block_error_to_bound,
                    error / bound,
                )

    print("FEJER_AVERAGED_MOBIUS_CRT_LOW_BLOCK_V0_1: PASS")
    print("MAX_GATE_ERROR=", max_gate_error)
    print("MAX_FACTORIZATION_ERROR=", max_factorization_error)
    print("MAX_CORRECTION_TO_BOUND_RATIO=", max_correction_to_bound)
    print("MAX_LOW_BLOCK_ERROR_TO_BOUND_RATIO=", max_low_block_error_to_bound)
    print("FIXED_SHIFT_HARDY_LITTLEWOOD_USED=false")
    print("ZETA_ZERO_LIST_USED=false")
    print("STATUS=EXACT_AVERAGED_LOW_BLOCK")


if __name__ == "__main__":
    main()
