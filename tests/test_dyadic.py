import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.dyadic import (
    cunningham_run,
    dyadic_address,
    fibre_value,
    half_boundary_prime_preimages,
    is_prime,
    log_fibre_coordinate,
    log_prime_defect,
    prime_mask,
    sophie_step,
)


class DyadicFibreTests(unittest.TestCase):
    def test_round_trip_addresses(self):
        for n in range(1, 10_000):
            a, k = dyadic_address(n)
            self.assertEqual(a % 2, 1)
            self.assertEqual(fibre_value(a, k), n)

    def test_sophie_step_is_fibre_shift(self):
        for a in range(1, 100, 2):
            for k in range(10):
                self.assertEqual(
                    sophie_step(fibre_value(a, k)),
                    fibre_value(a, k + 1),
                )

    def test_only_prime_on_k_zero_boundary_is_two(self):
        primes = [fibre_value(a, 0) for a in range(1, 1001, 2) if is_prime(fibre_value(a, 0))]
        self.assertEqual(primes, [2])

    def test_half_boundary_lemma_finite_regression(self):
        self.assertEqual(half_boundary_prime_preimages(10_000), (Fraction(1, 2),))
        self.assertEqual(sophie_step(Fraction(1, 2)), 2)

    def test_classical_cunningham_example(self):
        self.assertEqual(cunningham_run(3), (2, 5, 11, 23, 47))
        self.assertFalse(is_prime(95))

    def test_prime_mask_for_a_three(self):
        self.assertEqual(prime_mask(3, 5), (True, True, True, True, True, False))

    def test_exact_log_lattice_numerically(self):
        for a in range(1, 50, 2):
            for k in range(8):
                x = fibre_value(a, k)
                self.assertAlmostEqual(log_fibre_coordinate(a, k), math.log(x + 1), places=14)

    def test_prime_log_defect_identity(self):
        for p in (2, 3, 5, 11, 23, 47, 101):
            a, k = dyadic_address(p)
            delta = log_prime_defect(p)
            self.assertGreater(delta, 0.0)
            self.assertAlmostEqual(
                math.log(p),
                math.log(a) + k * math.log(2.0) - delta,
                places=14,
            )


if __name__ == "__main__":
    unittest.main()
