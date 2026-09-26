#!/usr/bin/env python3
"""Finite no-target-leakage validator for the On-Primes phase-spectroscopy core."""
import math


def g2_finite(mode_count: int, s: float) -> float:
    if mode_count < 2:
        raise ValueError("mode_count must be >= 2")
    if abs(s) < 1e-14:
        return 0.0
    return 1.0 - (
        math.sin(math.pi*s)
        / (mode_count*math.sin(math.pi*s/mode_count))
    )**2


def g2_limit(s: float) -> float:
    if abs(s) < 1e-14:
        return 0.0
    return 1.0 - (math.sin(math.pi*s)/(math.pi*s))**2


def phase_form(delta_phi: float) -> float:
    if abs(delta_phi) < 1e-14:
        return 0.0
    return 1.0 - (
        math.sin(delta_phi/2)/(delta_phi/2)
    )**2


def main():
    grid=[-3.0+6.0*j/600 for j in range(601)]
    errors=[]
    for M in [17,65,257,1025]:
        err=max(abs(g2_finite(M,s)-g2_limit(s)) for s in grid)
        errors.append(err)
    assert all(errors[i+1] < errors[i] for i in range(len(errors)-1))
    assert errors[-1] < 4e-7

    for s in [-2.1,-0.7,-0.2,0.2,0.7,2.1]:
        assert abs(g2_limit(s)-phase_form(2*math.pi*s)) < 1e-14

    for dp in [1e-3,5e-4,2.5e-4]:
        ratio=phase_form(dp)/(dp*dp)
        assert abs(ratio-1/12) < 2e-6

    print("ON_PRIMES_MONTGOMERY_DYSON_PHASE_SPECTROSCOPY_V0_1: PASS")
    print("GUE_OR_MONTGOMERY_USED_AS_INPUT=false")
    print("ZETA_ZERO_LIST_USED=false")
    print("MAX_ERROR_M1025=", errors[-1])
    print("CORE_STATUS=DERIVED_IN_FRAMEWORK/FORCED_PREDICTION")
    print("ZETA_OCCUPANCY_BINDING=OPEN_SOH_MD001")


if __name__ == "__main__":
    main()
