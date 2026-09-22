import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.memory import dyadic_memory_components, prime_power_memory
from on_primes.shifted_memory import (
    shifted_memory_channels,
    shifted_memory_defect,
    shifted_memory_total,
)


class ShiftedMemoryTests(unittest.TestCase):
    def test_shifted_channels_reconstruct_memory(self):
        for x in (2, 3, 10, 100, 1000):
            t = math.log(x)
            self.assertAlmostEqual(
                shifted_memory_total(t),
                prime_power_memory(t),
                places=10,
            )

    def test_r2_channel_matches_old_dyadic_component(self):
        for x in (10, 100, 1000):
            t = math.log(x)
            channels = shifted_memory_channels(t)
            k_mem, _, d_mem = dyadic_memory_components(t)
            self.assertAlmostEqual(channels.get(2, 0.0), math.log(2.0) * k_mem, places=10)
            self.assertAlmostEqual(shifted_memory_defect(t), d_mem, places=10)

    def test_odd_channels_match_old_label_component(self):
        for x in (10, 100, 1000):
            t = math.log(x)
            channels = shifted_memory_channels(t)
            _, a_mem, _ = dyadic_memory_components(t)
            odd_total = sum(v for r, v in channels.items() if r != 2)
            self.assertAlmostEqual(odd_total, a_mem, places=10)

    def test_channels_nonnegative(self):
        channels = shifted_memory_channels(math.log(1000))
        self.assertTrue(channels)
        for value in channels.values():
            self.assertGreaterEqual(value, 0.0)


if __name__ == "__main__":
    unittest.main()
