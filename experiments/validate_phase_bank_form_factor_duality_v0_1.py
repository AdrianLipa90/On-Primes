#!/usr/bin/env python3
"""Exact finite validator for prime-power phase bank / form-factor duality."""
import cmath
import math


def phase_mean(gammas, q):
    return sum(cmath.exp(1j*g*math.log(q)) for g in gammas)/len(gammas)


def frozen_density(T):
    return math.log(T/(2*math.pi))/(2*math.pi)


def tau_q(T, q):
    return math.log(q)/math.log(T/(2*math.pi))


def frozen_form_factor(gammas, T, tau):
    nu=frozen_density(T)
    phases=[
        cmath.exp(2j*math.pi*tau*nu*(g-T))
        for g in gammas
    ]
    return abs(sum(phases))**2/len(gammas)


def main():
    # Deliberately synthetic/non-zeta samples: theorem is finite algebra.
    samples=[
        [1.0,2.5,4.25,7.0],
        [0.125,1.75,3.0,3.125,9.5],
        [14.0,21.0,25.0,30.5,33.0,38.0],
    ]
    for gammas in samples:
        for T in [100.0,1_000.0,1_000_000.0]:
            assert T > 2*math.pi
            for q in [2.0,4.0,8.0,9.0,25.0,37.0,123.5]:
                lhs=frozen_form_factor(gammas,T,tau_q(T,q))
                rhs=len(gammas)*abs(phase_mean(gammas,q))**2
                assert abs(lhs-rhs) < 2e-11

    # Prime-power frequency map.
    T=1_000_000.0
    for p,m in [(2,1),(2,5),(3,2),(5,3),(7,1)]:
        q=p**m
        expected=m*math.log(p)/math.log(T/(2*math.pi))
        assert abs(tau_q(T,q)-expected) < 1e-15

    # Fixed q collapses toward tau=0.
    for q in [2.0,8.0,27.0]:
        vals=[tau_q(T,q) for T in [1e4,1e8,1e16,1e32]]
        assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))

    # To hold tau approximately fixed, q must scale as (T/2pi)^tau.
    for T in [1e4,1e8,1e16]:
        for tau in [0.2,0.5,0.8]:
            q=(T/(2*math.pi))**tau
            assert abs(tau_q(T,q)-tau) < 2e-15

    print("ON_PRIMES_PHASE_BANK_FORM_FACTOR_DUALITY_V0_1: PASS")
    print("ZETA_ZERO_LIST_REQUIRED=false")
    print("FINITE_IDENTITY=K_T(tau_q)=N*|R_q|^2")
    print("TAU_Q=log(q)/log(T/(2pi))")
    print("FIXED_Q_TO_RAMP_INFERENCE=false")
    print("STATUS=EXACT_FINITE_IDENTITY")


if __name__ == "__main__":
    main()
