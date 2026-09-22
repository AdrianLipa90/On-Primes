import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import primes_up_to
from on_primes.valuation_shells import (
    exact_shifted_shell_residues,
    in_exact_shifted_shell,
    vp,
)


class ValuationShellTests(unittest.TestCase):
    def test_residue_count(self):
        for r in (2, 3, 5, 7, 11):
            for j in range(1, 4):
                modulus, residues = exact_shifted_shell_residues(r, j)
                self.assertEqual(modulus, r ** (j + 1))
                self.assertEqual(len(residues), r - 1)
                self.assertEqual(len(set(residues)), r - 1)

    def test_exact_equivalence_on_primes(self):
        for p in primes_up_to(5000):
            for r in (2, 3, 5, 7, 11):
                j0 = vp(p + 1, r)
                for j in range(1, 5):
                    self.assertEqual(in_exact_shifted_shell(p, r, j), j0 == j)

    def test_dyadic_special_case(self):
        for j in range(1, 6):
            modulus, residues = exact_shifted_shell_residues(2, j)
            self.assertEqual(modulus, 2 ** (j + 1))
            self.assertEqual(residues, (2 ** j - 1,))


if __name__ == "__main__":
    unittest.main()
