#!/usr/bin/env python3
"""Reproduce finite-sieve survivor profiles for selected dyadic fibres."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.dyadic import is_prime
from on_primes.sieve import obstructed_residues, survivor_residues


def odd_primes_up_to(limit: int) -> tuple[int, ...]:
    return tuple(n for n in range(3, limit + 1, 2) if is_prime(n))


def profile(a: int, divisors: tuple[int, ...]) -> dict:
    period, removed = obstructed_residues(a, divisors)
    _, survivors = survivor_residues(a, divisors)
    return {
        "a": a,
        "divisors": list(divisors),
        "period": period,
        "removed_residue_count": len(removed),
        "survivor_residue_count": len(survivors),
        "survivor_density": len(survivors) / period,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, default=3)
    parser.add_argument("--prime-limit", type=int, default=53)
    args = parser.parse_args()
    divisors = odd_primes_up_to(args.prime_limit)
    print(json.dumps(profile(args.a, divisors), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
