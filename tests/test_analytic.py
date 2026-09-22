import cmath
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import (
    boundary_plus_interior_partial,
    classical_log_derivative_partial,
    fibre_log_derivative_partial,
    fibre_prime_power_sum,
    truncated_von_mangoldt_prime_power_sum,
)


class AnalyticReindexingTests(unittest.TestCase):
    def test_prime_sum_exact_reindexing_real_s(self):
        for P in (10, 100, 1000):
            lhs = classical_log_derivative_partial(2.0, P)
            rhs = fibre_log_derivative_partial(2.0, P)
            self.assertAlmostEqual(lhs.real, rhs.real, places=14)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=14)

    def test_prime_sum_exact_reindexing_complex_s(self):
        s = 1.7 + 4.25j
        lhs = classical_log_derivative_partial(s, 500)
        rhs = fibre_log_derivative_partial(s, 500)
        self.assertAlmostEqual(lhs.real, rhs.real, places=12)
        self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)

    def test_unique_boundary_term_is_p2(self):
        s = 2.0
        boundary, interior, total = boundary_plus_interior_partial(s, 1000)
        expected = __import__('math').log(2) / (2 ** s - 1)
        self.assertAlmostEqual(boundary.real, expected, places=14)
        self.assertAlmostEqual(boundary.imag, 0.0, places=14)
        self.assertAlmostEqual(total.real, classical_log_derivative_partial(s, 1000).real, places=14)

    def test_prime_power_reindexing(self):
        for X in (10, 100, 500):
            s = 1.3 + 0.7j
            lhs = truncated_von_mangoldt_prime_power_sum(s, X)
            rhs = fibre_prime_power_sum(s, X)
            self.assertAlmostEqual(lhs.real, rhs.real, places=12)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)


if __name__ == "__main__":
    unittest.main()
