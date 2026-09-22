import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.complete_mask import (
    obstruction_mask_factors,
    obstruction_witness,
    prime_by_complete_obstruction_mask,
)
from on_primes.dyadic import fibre_value, is_prime


class CompleteMaskTests(unittest.TestCase):
    def test_complete_mask_matches_reference_primality(self):
        for a in range(1, 80, 2):
            for k in range(0, 14):
                n = fibre_value(a, k)
                self.assertEqual(
                    prime_by_complete_obstruction_mask(a, k),
                    is_prime(n),
                    (a, k, n),
                )

    def test_witness_is_actual_divisor(self):
        for a in range(1, 40, 2):
            for k in range(1, 12):
                n = fibre_value(a, k)
                r = obstruction_witness(a, k)
                if r is not None:
                    self.assertEqual(n % r, 0)
                    self.assertLessEqual(r * r, n)

    def test_a3_95_witness(self):
        self.assertEqual(fibre_value(3, 5), 95)
        self.assertEqual(obstruction_witness(3, 5), 5)

    def test_prime_has_no_hit_factor(self):
        factors = obstruction_mask_factors(3, 4)  # 47
        self.assertTrue(all(not hit for _, _, _, hit in factors))


if __name__ == "__main__":
    unittest.main()
