#!/usr/bin/env python3
"""Exact finite validator for the shifted von Mangoldt pair-power decomposition."""
from __future__ import annotations
import cmath
import math


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    # Lambda(n)=log p iff n is a prime power p^k.
    for p in range(2, int(math.isqrt(n)) + 2):
        # primality of p
        if any(p % d == 0 for d in range(2, int(math.isqrt(p)) + 1)):
            continue
        q=p
        while q < n:
            q*=p
        if q == n:
            return math.log(p)
    # n may itself be prime.
    if all(n % d for d in range(2, int(math.isqrt(n)) + 1)):
        return math.log(n)
    return 0.0


def weights(Q: int, omega: float, sigma: float) -> list[complex]:
    out=[0j]*(Q+1)
    for n in range(2,Q+1):
        lam=von_mangoldt(n)
        if lam == 0.0:
            continue
        x=math.log(n)
        window=math.exp(-0.5*((x-omega)/sigma)**2)
        phase=cmath.exp(0.37j*x)
        out[n]=lam/math.sqrt(n)*window*phase
    return out


def direct_power(b: list[complex]) -> float:
    return abs(sum(b))**2


def shifted_power(b: list[complex]) -> complex:
    Q=len(b)-1
    diag=sum(abs(b[n])**2 for n in range(1,Q+1))
    off=0j
    for h in range(1,Q):
        for n in range(1,Q-h+1):
            off += b[n]*b[n+h].conjugate()
    return diag+2.0*off.real


def main():
    max_err=0.0
    for Q in [20,50,100,180]:
        for omega in [1.0,2.3,3.7,4.8]:
            for sigma in [0.25,0.7,1.2]:
                b=weights(Q,omega,sigma)
                a=direct_power(b)
                c=shifted_power(b)
                err=abs(a-c)
                max_err=max(max_err,err)
                assert err < 2e-12

    print("ON_PRIMES_VON_MANGOLDT_PAIR_POWER_DECOMPOSITION_V0_1: PASS")
    print("MAX_ABS_ERROR=",max_err)
    print("HARDY_LITTLEWOOD_USED_AS_INPUT=false")
    print("ZETA_ZERO_LIST_USED=false")
    print("STATUS=EXACT_FINITE_ARITHMETIC_DECOMPOSITION")


if __name__ == "__main__":
    main()
