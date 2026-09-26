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
    ramanujan_sum,
    finite_prime_pair_singular_product,
    finite_prime_pair_ramanujan_expansion,
    twin_quadruplet_residue_count,
    twin_quadruplet_local_factor,
    finite_twin_quadruplet_singular_product,
    twin_gap_mod6_admissible,
    twin_quadruplet_dyadic_local_orbit,
    even_sector_pair_singular_dyadic_invariant,
    doubling_order_mod_prime,
    doubling_orbits_mod_prime,
    dyadic_transfer_spectrum_multiplicities,
    twin_quadruplet_factor_decomposition,
    twin_special_residue_cycles,
    twin_special_mode_support,
    twin_special_cycles_coincide,
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


    def test_finite_euler_ramanujan_factorization(self):
        support = (2, 3, 5, 7, 11)
        for h in range(1, 65):
            self.assertEqual(
                finite_prime_pair_singular_product(h, support),
                finite_prime_pair_ramanujan_expansion(h, support),
            )

    def test_prime_pair_local_channels(self):
        self.assertEqual(ramanujan_sum(5, 10), 4)
        self.assertEqual(ramanujan_sum(5, 11), -1)
        self.assertEqual(finite_prime_pair_singular_product(3, (2, 3, 5)), 0)
        self.assertGreater(finite_prime_pair_singular_product(6, (2, 3, 5)), 0)

    def test_even_sector_pair_singular_series_is_dyadic_invariant(self):
        support = (2, 3, 5, 7, 11, 13)
        for h in range(2, 100, 2):
            self.assertTrue(even_sector_pair_singular_dyadic_invariant(h, support))

    def test_twin_quadruplet_mod6_gate(self):
        for h in range(1, 120):
            self.assertEqual(twin_gap_mod6_admissible(h), h % 6 == 0)
            local23 = finite_twin_quadruplet_singular_product(h, (2, 3))
            if h % 6 == 0:
                self.assertGreater(local23, 0)
                self.assertEqual(twin_quadruplet_residue_count(2, h), 1)
                self.assertEqual(twin_quadruplet_residue_count(3, h), 2)
            else:
                self.assertEqual(local23, 0)

    def test_twin_quadruplet_factor_tracks_dyadic_phase_orbit(self):
        p, h, steps = 7, 6, 12
        orbit = twin_quadruplet_dyadic_local_orbit(p, h, steps)
        residue = h % p
        for observed_residue, factor in orbit:
            self.assertEqual(observed_residue, residue)
            self.assertEqual(factor, twin_quadruplet_local_factor(p, residue))
            residue = (2 * residue) % p


    def test_doubling_orbit_decomposition(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
            d = doubling_order_mod_prime(p)
            orbits = doubling_orbits_mod_prime(p)
            nonzero = tuple(o for o in orbits if o != (0,))
            self.assertEqual(orbits[0], (0,))
            self.assertTrue(all(len(o) == d for o in nonzero))
            self.assertEqual(len(nonzero), (p - 1) // d)
            self.assertEqual({u for o in orbits for u in o}, set(range(p)))

    def test_transfer_spectrum_multiplicities(self):
        for p in (5, 7, 11, 13, 17, 23, 31):
            d, mult = dyadic_transfer_spectrum_multiplicities(p)
            cycles = (p - 1) // d
            self.assertEqual(mult[0], cycles + 1)
            for m in range(1, d):
                self.assertEqual(mult[m], cycles)
            self.assertEqual(sum(mult.values()), p)

    def test_twin_local_factor_three_level_decomposition(self):
        for p in (5, 7, 11, 13, 17, 19):
            base, spike = twin_quadruplet_factor_decomposition(p)
            for u in range(p):
                predicted = base
                if u == 0:
                    predicted += 2 * spike
                if u in (2, (-2) % p):
                    predicted += spike
                self.assertEqual(predicted, twin_quadruplet_local_factor(p, u))

    def test_special_cycle_parity_selection_rule(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            d = doubling_order_mod_prime(p)
            plus, minus = twin_special_residue_cycles(p)
            self.assertEqual(twin_special_cycles_coincide(p), d % 2 == 0)
            if d % 2 == 0:
                self.assertEqual(set(twin_special_mode_support(p)), set(range(0, d, 2)))
                self.assertEqual(plus, minus)
            else:
                self.assertEqual(set(twin_special_mode_support(p)), set(range(d)))
                self.assertNotEqual(plus, minus)


if __name__ == "__main__":
    unittest.main()
