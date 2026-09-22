import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.modular import (
    is_obstructed_by,
    multiplicative_order_2,
    obstruction_class,
    obstruction_profile,
)


class ModularObstructionTests(unittest.TestCase):
    def test_orders(self):
        self.assertEqual(multiplicative_order_2(3), 2)
        self.assertEqual(multiplicative_order_2(5), 4)
        self.assertEqual(multiplicative_order_2(7), 3)

    def test_a3_mod5_class(self):
        self.assertEqual(obstruction_class(3, 5), (1, 4))
        self.assertFalse(is_obstructed_by(3, 1, 5))  # value is r itself
        self.assertTrue(is_obstructed_by(3, 5, 5))   # 95
        self.assertTrue(is_obstructed_by(3, 9, 5))

    def test_obstruction_equivalence_finite(self):
        for a in range(1, 40, 2):
            for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
                cls = obstruction_class(a, r)
                for k in range(30):
                    divisible = (a * (1 << k) - 1) % r == 0
                    predicted = False if cls is None else (k % cls[1] == cls[0])
                    self.assertEqual(divisible, predicted, (a, r, k, cls))

    def test_profile(self):
        profile = obstruction_profile(3, 10, (5, 7, 11))
        self.assertIn(5, profile)
        self.assertIn(5, profile[5])
        self.assertIn(9, profile[5])


if __name__ == "__main__":
    unittest.main()
