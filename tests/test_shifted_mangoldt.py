import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import classical_log_derivative_partial, primes_up_to
from on_primes.shifted_mangoldt import (
    base_channel_partial,
    factorize,
    reconstructed_log_derivative_from_shifted_tower,
    shifted_log_sum,
    shifted_tower_partial,
    shifted_von_mangoldt_channels,
)


class ShiftedMangoldtTests(unittest.TestCase):
    def test_factorization(self):
        self.assertEqual(factorize(1), {})
        self.assertEqual(factorize(60), {2: 2, 3: 1, 5: 1})

    def test_shifted_log_identity(self):
        for p in primes_up_to(5000):
            self.assertAlmostEqual(shifted_log_sum(p), math.log(p + 1), places=13)

    def test_channel_congruences(self):
        for p in primes_up_to(2000):
            for r, j, _ in shifted_von_mangoldt_channels(p):
                self.assertEqual((p + 1) % (r ** j), 0)
                self.assertEqual(p % (r ** j), (r ** j) - 1)

    def test_shifted_tower_reconstructs_prime_sum(self):
        for s in (2.0, 1.7 + 2.2j):
            lhs = classical_log_derivative_partial(s, 1000)
            rhs = reconstructed_log_derivative_from_shifted_tower(s, 1000)
            self.assertAlmostEqual(lhs.real, rhs.real, places=11)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=11)

    def test_two_channel_matches_v2_weight(self):
        s = 2.0
        direct = base_channel_partial(2, s, 2000)
        expected = 0j
        for p in primes_up_to(2000):
            e = factorize(p + 1).get(2, 0)
            expected += e * math.log(2.0) / (p ** s - 1)
        self.assertAlmostEqual(direct.real, expected.real, places=13)


if __name__ == "__main__":
    unittest.main()
