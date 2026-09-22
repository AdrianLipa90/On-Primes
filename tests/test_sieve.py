import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.dyadic import fibre_value, is_prime
from on_primes.sieve import (
    certified_composite_by_sieve,
    finite_sieve_allows,
    obstructed_residues,
    sieve_period,
    survivor_density,
    survivor_residues,
)


class FiniteSieveTests(unittest.TestCase):
    def test_period(self):
        self.assertEqual(sieve_period((3, 5, 7)), 12)

    def test_exact_periodicity(self):
        divisors = (3, 5, 7, 11, 13)
        period, removed = obstructed_residues(3, divisors)
        removed = set(removed)
        for k in range(period * 5):
            self.assertEqual((k % period) in removed, ((k + period) % period) in removed)

    def test_survivors_partition_period(self):
        period, removed = obstructed_residues(3, (3, 5, 7, 11))
        p2, survivors = survivor_residues(3, (3, 5, 7, 11))
        self.assertEqual(period, p2)
        self.assertEqual(set(removed).isdisjoint(survivors), True)
        self.assertEqual(len(set(removed) | set(survivors)), period)

    def test_density_matches_count(self):
        period, survivors = survivor_residues(3, (3, 5, 7, 11, 13))
        self.assertEqual(survivor_density(3, (3, 5, 7, 11, 13)), len(survivors) / period)

    def test_no_prime_is_falsely_certified_composite(self):
        divisors = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        for a in range(1, 50, 2):
            for k in range(20):
                n = fibre_value(a, k)
                if is_prime(n):
                    self.assertFalse(certified_composite_by_sieve(a, k, divisors), (a, k, n))

    def test_rejected_large_values_have_a_witness(self):
        divisors = (3, 5, 7, 11, 13)
        for k in range(50):
            if not finite_sieve_allows(3, k, divisors):
                n = fibre_value(3, k)
                witness = any(n > r and n % r == 0 for r in divisors)
                if witness:
                    self.assertTrue(certified_composite_by_sieve(3, k, divisors))


if __name__ == "__main__":
    unittest.main()
