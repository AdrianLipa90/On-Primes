import unittest

from on_primes.phase_law import (
    crt_reconstruct,
    cyclic_autocorrelation,
    dft_power,
    dyadic_gap_transport,
    fibre_obstruction_hits,
    fibre_phase_orbit,
    inverse_power_to_autocorrelation,
    ordered_gaps,
    phase_difference,
    phase_residue,
    phase_value,
    prime_power_signature,
    reconstruct_from_gaps,
)


class ArithmeticRelationalPhaseLawTests(unittest.TestCase):
    def test_phase_difference_law(self):
        for q in (2, 3, 5, 7, 11, 16):
            x, y = 137, 911
            lhs = phase_value(y, q) * phase_value(x, q).conjugate()
            rhs = phase_difference(x, y, q)
            self.assertAlmostEqual(lhs.real, rhs.real, places=12)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)
            self.assertEqual(phase_residue(y - x, q), (y - x) % q)

    def test_crt_phase_reconstruction(self):
        delta = 123456789
        sig = prime_power_signature(delta, {2: 5, 3: 3, 5: 2, 7: 1})
        x, modulus = crt_reconstruct(sig)
        self.assertEqual(x, delta % modulus)
        self.assertEqual(modulus, (2**5) * (3**3) * (5**2) * 7)

    def test_ordered_gap_roundtrip(self):
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        gaps = ordered_gaps(primes)
        self.assertEqual(reconstruct_from_gaps(primes[0], gaps), primes)

    def test_wiener_khinchin_finite_identity(self):
        signal = (0, 1, 0, 1, 1, 0, 0, 1)
        direct = cyclic_autocorrelation(signal)
        spectral = inverse_power_to_autocorrelation(dft_power(signal))
        for a, b in zip(direct, spectral):
            self.assertAlmostEqual(a.real, b.real, places=10)
            self.assertAlmostEqual(a.imag, b.imag, places=10)

    def test_dyadic_transport_is_phase_squaring(self):
        delta = 37
        for q in (3, 5, 7, 11, 13):
            z = phase_value(delta, q)
            for r in range(6):
                transported = phase_value(dyadic_gap_transport(delta, r), q)
                expected = z ** (2**r)
                self.assertAlmostEqual(transported.real, expected.real, places=10)
                self.assertAlmostEqual(transported.imag, expected.imag, places=10)

    def test_fibre_obstruction_phase_hits_match_divisibility(self):
        a, r, length = 3, 7, 30
        hits = fibre_obstruction_hits(a, r, length)
        brute = tuple(k for k in range(length) if (a * (2**k) - 1) % r == 0)
        self.assertEqual(hits, brute)
        orbit = fibre_phase_orbit(a, r, length)
        for u, v in zip(orbit, orbit[1:]):
            self.assertEqual(v, (2 * u) % r)

    def test_twin_prime_start_gaps_are_six_locked_beyond_three(self):
        def is_prime(n):
            if n < 2:
                return False
            if n % 2 == 0:
                return n == 2
            d = 3
            while d * d <= n:
                if n % d == 0:
                    return False
                d += 2
            return True

        starts = tuple(p for p in range(5, 5000) if is_prime(p) and is_prime(p + 2))
        gaps = ordered_gaps(starts)
        self.assertTrue(gaps)
        self.assertTrue(all(g % 6 == 0 for g in gaps))
        self.assertTrue(all(phase_residue(g, 2) == 0 for g in gaps))
        self.assertTrue(all(phase_residue(g, 3) == 0 for g in gaps))


if __name__ == "__main__":
    unittest.main()
