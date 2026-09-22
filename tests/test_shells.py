import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from on_primes.analytic import primes_up_to
from on_primes.dyadic import dyadic_address
from on_primes.shells import in_exact_shell, shell_residue


class DyadicShellTests(unittest.TestCase):
    def test_exact_shell_equivalence(self):
        for p in primes_up_to(10000):
            _, k = dyadic_address(p)
            if p == 2:
                self.assertEqual(k, 0)
                continue
            self.assertTrue(in_exact_shell(p, k))
            for j in range(1, min(k + 3, 12)):
                self.assertEqual(in_exact_shell(p, j), j == k)

    def test_shell_residues(self):
        self.assertEqual(shell_residue(1), (1, 4))
        self.assertEqual(shell_residue(2), (3, 8))
        self.assertEqual(shell_residue(3), (7, 16))
        self.assertEqual(shell_residue(4), (15, 32))


if __name__ == "__main__":
    unittest.main()
