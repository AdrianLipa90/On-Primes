import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.memory import (
    dyadic_memory_components,
    prime_power_events_up_to_log_time,
    prime_power_memory,
    reconstructed_prime_power_memory,
)


class PrimePowerMemoryTests(unittest.TestCase):
    def test_events_respect_log_time_cutoff(self):
        for t in (math.log(2), math.log(10), math.log(100), math.log(500)):
            for event in prime_power_events_up_to_log_time(t):
                self.assertLessEqual(event.time, t + 1e-11)
                self.assertLessEqual(event.q, math.floor(math.exp(t) + 1e-9))

    def test_memory_decomposition(self):
        for x in (2, 3, 5, 10, 50, 100, 500, 1000):
            t = math.log(x)
            direct = prime_power_memory(t)
            rebuilt = reconstructed_prime_power_memory(t)
            self.assertAlmostEqual(direct, rebuilt, places=11)

    def test_components_are_finite(self):
        for x in (10, 100, 1000):
            vals = dyadic_memory_components(math.log(x))
            for value in vals:
                self.assertTrue(math.isfinite(value))


if __name__ == "__main__":
    unittest.main()
