#!/usr/bin/env python3
"""Validator for the LCM-von-Mangoldt commensurate clock."""
from __future__ import annotations

import math


def primes_up_to(n: int):
    sieve=[True]*(n+1)
    if n>=0: sieve[0]=False
    if n>=1: sieve[1]=False
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            for k in range(p*p,n+1,p):
                sieve[k]=False
    return [p for p in range(2,n+1) if sieve[p]]


def lcm_upto(R: int) -> int:
    out=1
    for n in range(1,R+1):
        out=math.lcm(out,n)
    return out


def psi_prime_power(R: int) -> float:
    total=0.0
    for p in primes_up_to(R):
        q=p
        while q<=R:
            total+=math.log(p)
            if q>R//p:
                break
            q*=p
    return total


def mobius_sieve(n: int):
    mu=[0]*(n+1)
    mu[1]=1
    primes=[]
    comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]:
            primes.append(i)
            mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0:
                mu[i*p]=0
                break
            mu[i*p]=-mu[i]
    return mu


def q_gate(H: int,g: int)->float:
    L=H+1
    r=L%g
    return 1/g+r*(g-r)/(g*L*L)


def avg_density(H: int,R: int,mu)->float:
    total=0.0
    for d in range(1,R+1):
        for e in range(1,R+1):
            if not mu[d] or not mu[e]:
                continue
            g=math.gcd(d,e)
            ell=d*e//g
            total += mu[d]*mu[e]*math.log(d)*math.log(e)/ell*q_gate(H,g)
    return total


def factorized(R: int,mu)->float:
    s=sum(mu[d]*math.log(d)/d for d in range(1,R+1) if mu[d])
    return s*s


def main():
    max_log_error=0.0
    max_factor_error=0.0
    mu=mobius_sieve(40)
    for R in range(2,31):
        L=lcm_upto(R)
        max_log_error=max(max_log_error,abs(math.log(L)-psi_prime_power(R)))
        assert max_log_error < 2e-12

        H=L-1
        for g in range(1,R+1):
            assert L%g==0
            assert abs(q_gate(H,g)-1/g) < 2e-15

        err=abs(avg_density(H,R,mu)-factorized(R,mu))
        max_factor_error=max(max_factor_error,err)
        assert err < 3e-12

    print("LCM_VON_MANGOLDT_COMMENSURATE_CLOCK_V0_1: PASS")
    print("MAX_LOG_IDENTITY_ERROR=",max_log_error)
    print("MAX_FACTOR_ERROR=",max_factor_error)
    print("STATUS=EXACT_FINITE_COMMON_CLOCK")


if __name__=="__main__":
    main()
