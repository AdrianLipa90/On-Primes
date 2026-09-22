import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import primes_up_to
from on_primes.dyadic import dyadic_address
from on_primes.residue_tower import (
    direct_valuation_moment_partial,
    residue_tower_partial,
    valuation_as_residue_count,
)


class ResidueTowerTests(unittest.TestCase):
    def test_valuation_equals_nested_residue_count(self):
        for p in primes_up_to(5000):
            _, k = dyadic_address(p)
            self.assertEqual(valuation_as_residue_count(p), k)

    def test_finite_tower_real(self):
        lhs = direct_valuation_moment_partial(2.0, 2000)
        rhs = residue_tower_partial(2.0, 2000)
        self.assertAlmostEqual(lhs.real, rhs.real, places=13)
        self.assertAlmostEqual(lhs.imag, rhs.imag, places=13)

    def test_finite_tower_complex(self):
        s = 1.6 + 2.5j
        lhs = direct_valuation_moment_partial(s, 1500)
        rhs = residue_tower_partial(s, 1500)
        self.assertAlmostEqual(lhs.real, rhs.real, places=12)
        self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)


if __name__ == "__main__":
    unittest.main()
