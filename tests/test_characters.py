import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.characters import (
    character_ids_pow2,
    character_value_pow2,
    residue_class_prime_sum_partial,
    residue_class_via_characters_partial,
    residue_indicator_via_characters,
)


class CharacterBridgeTests(unittest.TestCase):
    def test_character_count_is_phi(self):
        for j in range(1, 8):
            self.assertEqual(len(character_ids_pow2(j)), 1 << (j - 1))

    def test_character_orthogonality_indicator(self):
        for j in range(1, 7):
            q = 1 << j
            for n in range(1, q * 3, 2):
                value = residue_indicator_via_characters(j, n)
                expected = 1.0 if n % q == q - 1 else 0.0
                self.assertAlmostEqual(value.real, expected, places=12)
                self.assertAlmostEqual(value.imag, 0.0, places=12)

    def test_multiplicativity_on_units(self):
        for j in range(1, 7):
            q = 1 << j
            for cid in character_ids_pow2(j):
                for a in range(1, q, 2):
                    for b in range(1, q, 2):
                        lhs = character_value_pow2(j, cid, a * b)
                        rhs = character_value_pow2(j, cid, a) * character_value_pow2(j, cid, b)
                        self.assertAlmostEqual(lhs.real, rhs.real, places=12)
                        self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)

    def test_residue_prime_sum_character_reconstruction(self):
        s = 1.8 + 1.7j
        for j in range(1, 6):
            lhs = residue_class_prime_sum_partial(j, s, 1000)
            rhs = residue_class_via_characters_partial(j, s, 1000)
            self.assertAlmostEqual(lhs.real, rhs.real, places=11)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=11)


if __name__ == "__main__":
    unittest.main()
