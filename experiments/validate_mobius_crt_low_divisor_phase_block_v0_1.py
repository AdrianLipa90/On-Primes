#!/usr/bin/env python3
"""Validate the controlled low-divisor Möbius-CRT phase block."""
from __future__ import annotations
import cmath
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


def crt_count(X: int, h: int, d: int, e: int) -> int:
    g=math.gcd(d,e)
    if h % g:
        return 0
    ell=math.lcm(d,e)
    r=next(
        r for r in range(1,ell+1)
        if r % d == 0 and (r+h) % e == 0
    )
    if r > X:
        return 0
    return (X-r)//ell + 1


def low_exact(X: int, h: int, R: int) -> float:
    total=0.0
    for d in range(1,R+1):
        md=mobius(d)
        if md == 0:
            continue
        for e in range(1,R+1):
            me=mobius(e)
            if me == 0:
                continue
            total += (
                md*me*math.log(d)*math.log(e)
                * crt_count(X,h,d,e)
            )
    return total


def low_density(X: int, h: int, R: int) -> float:
    coeff=0.0
    for d in range(1,R+1):
        md=mobius(d)
        if md == 0:
            continue
        for e in range(1,R+1):
            me=mobius(e)
            if me == 0:
                continue
            g=math.gcd(d,e)
            if h % g:
                continue
            coeff += (
                md*me*math.log(d)*math.log(e)
                / math.lcm(d,e)
            )
    return X*coeff


def phase_indicator(g: int, h: int) -> complex:
    return sum(
        cmath.exp(2j*math.pi*a*h/g)
        for a in range(g)
    )/g


def main():
    max_ratio=0.0
    for X in [100,300,1000]:
        for h in [1,2,3,6,10]:
            for R in [5,10,20]:
                exact=low_exact(X,h,R)
                density=low_density(X,h,R)
                err=abs(exact-density)
                bound=(R*math.log(R))**2
                max_ratio=max(max_ratio,err/bound)
                assert err <= bound + 1e-10

                for d in range(1,R+1):
                    for e in range(1,R+1):
                        g=math.gcd(d,e)
                        ind=phase_indicator(g,h)
                        expected=1.0 if h % g == 0 else 0.0
                        assert abs(ind.real-expected) < 2e-12
                        assert abs(ind.imag) < 2e-12

    print("ON_PRIMES_MOBIUS_CRT_LOW_DIVISOR_PHASE_BLOCK_V0_1: PASS")
    print("MAX_ERROR_TO_BOUND_RATIO=",max_ratio)
    print("LOW_BLOCK_BOUND=(R log R)^2")
    print("CHARACTER_INDICATOR=EXACT")
    print("STATUS=EXACT_TRUNCATED_DECOMPOSITION")


if __name__ == "__main__":
    main()
