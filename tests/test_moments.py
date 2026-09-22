import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import classical_log_derivative_partial, primes_up_to
from on_primes.moments import (
    defect_partial,
    dyadic_moment_partial,
    fibre_label_partial,
    prime_log_components,
    reconstructed_log_derivative_partial,
)


class DyadicMomentTests(unittest.TestCase):
    def test_prime_log_identity(self):
        for p in primes_up_to(5000):
            label, dyadic, defect = prime_log_components(p)
            self.assertAlmostEqual(math.log(p), label + dyadic - defect, places=13)

    def test_finite_moment_reconstruction_real(self):
        for P in (10, 100, 1000):
            lhs = classical_log_derivative_partial(2.0, P)
            rhs = reconstructed_log_derivative_partial(2.0, P)
            self.assertAlmostEqual(lhs.real, rhs.real, places=13)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=13)

    def test_finite_moment_reconstruction_complex(self):
        s = 1.4 + 3.0j
        lhs = classical_log_derivative_partial(s, 1000)
        rhs = reconstructed_log_derivative_partial(s, 1000)
        self.assertAlmostEqual(lhs.real, rhs.real, places=12)
        self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)

    def test_defect_bound(self):
        for p in primes_up_to(5000):
            _, _, defect = prime_log_components(p)
            self.assertGreater(defect, 0.0)
            self.assertLess(defect, 1.0 / p)


if __name__ == "__main__":
    unittest.main()
