import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.covering import covering_certificate, is_residue_covering_set


class CoveringSetTests(unittest.TestCase):
    def test_known_riesel_covering_set(self):
        divisors = (3, 5, 7, 13, 17, 241)
        self.assertTrue(is_residue_covering_set(509203, divisors))
        cert = covering_certificate(509203, divisors, k_start=1)
        self.assertTrue(cert["certifies_all_composite"])
        self.assertEqual(cert["small_equality_exceptions"], [])

    def test_a3_small_primes_not_covering(self):
        self.assertFalse(is_residue_covering_set(3, (3, 5, 7, 11, 13)))


if __name__ == "__main__":
    unittest.main()
