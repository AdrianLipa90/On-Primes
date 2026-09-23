import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.centered_hexagonal import (
    centered_hexagonal,
    is_obstructed_by,
    obstruction_roots_mod_prime,
    shell_increment,
)


class CenteredHexagonalPrimeChannelTests(unittest.TestCase):
    def test_initial_values(self):
        self.assertEqual(
            [centered_hexagonal(n) for n in range(10)],
            [1, 7, 19, 37, 61, 91, 127, 169, 217, 271],
        )

    def test_shell_increments(self):
        for n in range(1, 100):
            self.assertEqual(
                centered_hexagonal(n) - centered_hexagonal(n - 1),
                shell_increment(n),
            )

    def test_all_values_are_one_mod_six(self):
        for n in range(1000):
            self.assertEqual(centered_hexagonal(n) % 6, 1)

    def test_split_prime_channels_have_exact_root_count(self):
        for q in (7, 13, 19, 31, 37, 43, 61, 67, 73):
            roots = obstruction_roots_mod_prime(q)
            self.assertEqual(q % 6, 1)
            self.assertEqual(len(roots), 2)
            for n in roots:
                self.assertEqual(centered_hexagonal(n) % q, 0)

    def test_inert_prime_channels_have_no_roots(self):
        for q in (5, 11, 17, 23, 29, 41, 47, 53, 59):
            self.assertEqual(q % 6, 5)
            self.assertEqual(obstruction_roots_mod_prime(q), ())

    def test_known_obstructions_and_equality_exception(self):
        self.assertFalse(is_obstructed_by(1, 7))  # H_1 = 7 itself
        self.assertTrue(is_obstructed_by(5, 7))   # H_5 = 91
        self.assertTrue(is_obstructed_by(5, 13))  # H_5 = 91
        self.assertTrue(is_obstructed_by(7, 13))  # H_7 = 169

    def test_every_small_prime_divisor_is_one_mod_six(self):
        for n in range(1, 300):
            value = centered_hexagonal(n)
            q = 2
            remaining = value
            while q * q <= remaining:
                if remaining % q == 0:
                    self.assertEqual(q % 6, 1, (n, value, q))
                    while remaining % q == 0:
                        remaining //= q
                q += 1
            if remaining > 1:
                self.assertEqual(remaining % 6, 1, (n, value, remaining))


if __name__ == "__main__":
    unittest.main()
