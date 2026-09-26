#!/usr/bin/env python3
"""Validate the finite shifted von Mangoldt CRT-phase decomposition."""
from __future__ import annotations
import math


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x=n
    count=0
    p=2
    while p*p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def von_mangoldt_mobius(n: int) -> float:
    return -sum(
        mobius(d)*math.log(d)
        for d in range(1,n+1)
        if n % d == 0
    )


def crt_count(X: int, h: int, d: int, e: int) -> int:
    g=math.gcd(d,e)
    if h % g:
        return 0
    ell=math.lcm(d,e)
    # Finite validator: locate the unique compatible residue.
    r=next(
        r for r in range(1,ell+1)
        if r % d == 0 and (r+h) % e == 0
    )
    if r > X:
        return 0
    return (X-r)//ell + 1


def direct_corr(X: int, h: int) -> float:
    return sum(
        von_mangoldt_mobius(n)
        * von_mangoldt_mobius(n+h)
        for n in range(1,X+1)
    )


def crt_corr(X: int, h: int) -> float:
    total=0.0
    for d in range(1,X+1):
        md=mobius(d)
        if md == 0:
            continue
        for e in range(1,X+h+1):
            me=mobius(e)
            if me == 0:
                continue
            count=crt_count(X,h,d,e)
            if count:
                total += (
                    md*me
                    * math.log(d)*math.log(e)
                    * count
                )
    return total


def main():
    max_err=0.0
    for X in [10,20,40,80]:
        for h in [1,2,3,4,6,10]:
            direct=direct_corr(X,h)
            via_crt=crt_corr(X,h)
            err=abs(direct-via_crt)
            max_err=max(max_err,err)
            assert err < 3e-12

    # Explicit phase/CRT compatibility.
    for d in range(1,15):
        for e in range(1,15):
            g=math.gcd(d,e)
            for h in range(0,30):
                phase=complex(
                    math.cos(2*math.pi*h/g),
                    math.sin(2*math.pi*h/g),
                )
                locked=abs(phase-1) < 2e-12
                assert locked == (h % g == 0)

    print("ON_PRIMES_SHIFTED_VON_MANGOLDT_CRT_PHASE_V0_1: PASS")
    print("MAX_ABS_CORRELATION_ERROR=",max_err)
    print("CRT_COMPATIBILITY_EQ_PHASE_LOCK=true")
    print("HARDY_LITTLEWOOD_ASYMPTOTIC_USED=false")
    print("STATUS=EXACT_FINITE_IDENTITY")


if __name__ == "__main__":
    main()
