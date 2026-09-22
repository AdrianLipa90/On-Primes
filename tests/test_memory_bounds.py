import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import primes_up_to
from on_primes.dyadic import dyadic_address
from on_primes.memory import dyadic_memory_components


class MemoryBoundTests(unittest.TestCase):
    def test_prime_defect_bound(self):
        for p in primes_up_to(10000):
            delta = math.log1p(1.0 / p)
            self.assertGreater(delta, 0.0)
            self.assertLess(delta, 1.0 / p)

    def test_odd_prime_dyadic_reserve(self):
        target = math.log(1.5)
        for p in primes_up_to(10000):
            if p == 2:
                continue
            _, k = dyadic_address(p)
            delta = math.log1p(1.0 / p)
            self.assertGreaterEqual(k * math.log(2.0) - delta + 1e-15, target)

    def test_memory_components_nonnegative(self):
        for x in (2, 3, 10, 100, 1000):
            k_mem, a_mem, d_mem = dyadic_memory_components(math.log(x))
            self.assertGreaterEqual(k_mem, -1e-14)
            self.assertGreaterEqual(a_mem, -1e-14)
            self.assertGreaterEqual(d_mem, -1e-14)

    def test_boundary_identity(self):
        self.assertAlmostEqual(math.log(3.0) - math.log(1.5), math.log(2.0), places=15)


if __name__ == "__main__":
    unittest.main()
