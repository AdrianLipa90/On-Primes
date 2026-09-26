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
    twin_local_dyadic_period,
    twin_local_orbit_values,
    twin_local_orbit_mean,
    twin_local_orbit_variance,
    twin_global_dyadic_period,
    twin_global_orbit_mean,
    twin_product_of_local_means,
    twin_dyadic_resonance_correction,
    local_periods_pairwise_coprime,
    twin_finite_dyadic_orbit_invariant,
    twin_local_mean_class,
    twin_local_mean_closed_form,
    twin_period_overlap_components,
    twin_component_factorized_mean,
    twin_connected_resonance_cumulant,
    twin_centered_joint_moment,
    twin_centered_moment_resonance_bound,
    twin_connected_cumulant_fixed_order_bound,
    twin_channel_is_dynamically_active,
    twin_background_factor,
    twin_zero_correction_ratio,
    twin_special_correction_ratio,
    twin_finite_instantaneous_product,
    twin_finite_instantaneous_factorization,
    twin_special_hit_density,
    twin_local_log_orbit_mean,
    twin_local_log_orbit_formula,
    twin_finite_log_geometric_mean,
    twin_special_hit_positions,
    twin_joint_special_hit_density,
    twin_log_pair_covariance,
    twin_finite_log_variance,
    twin_finite_log_fourier_coefficients,
    twin_finite_log_parseval_power,
    quadruplet_observable_period,
    twin_quadratic_hit_phase,
    twin_quadratic_hit_density,
    twin_quadratic_joint_hit_density,
    twin_fractional_special_multiplier,
    twin_finite_fractional_common_clock_mean,
    twin_finite_fractional_subset_mean,
    twin_real_moment_multiplier,
    twin_finite_real_moment_common_clock,
    twin_finite_real_moment_subset_mean,
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


    def test_local_orbit_statistics_are_exact(self):
        for p in (5, 7, 11, 13, 17, 19):
            values = twin_local_orbit_values(p, 6)
            self.assertEqual(len(values), twin_local_dyadic_period(p, 6))
            mean = sum(values) / len(values)
            variance = sum((v - mean) ** 2 for v in values) / len(values)
            self.assertEqual(mean, twin_local_orbit_mean(p, 6))
            self.assertEqual(variance, twin_local_orbit_variance(p, 6))

    def test_pairwise_coprime_periods_factorize_global_mean(self):
        examples = (
            ((5, 7), 6),       # periods 4 and 3
            ((5, 7, 11), 6),   # effective common-clock resonance still vanishes
        )
        self.assertTrue(local_periods_pairwise_coprime((5, 7), 6))
        self.assertEqual(
            twin_global_orbit_mean((5, 7), 6),
            twin_product_of_local_means((5, 7), 6),
        )
        self.assertEqual(twin_dyadic_resonance_correction((5, 7), 6), 0)

        for support, h in examples:
            self.assertEqual(
                twin_global_dyadic_period(support, h),
                __import__("math").lcm(*(twin_local_dyadic_period(p, h) for p in support)),
            )

    def test_shared_periods_can_generate_nonzero_resonance(self):
        self.assertFalse(local_periods_pairwise_coprime((7, 13), 6))
        self.assertNotEqual(twin_dyadic_resonance_correction((7, 13), 6), 0)
        self.assertEqual(
            twin_global_orbit_mean((7, 13), 6) / twin_product_of_local_means((7, 13), 6),
            __import__("fractions").Fraction(549, 550),
        )

        self.assertNotEqual(twin_dyadic_resonance_correction((7, 13, 19), 6), 0)
        self.assertEqual(
            twin_global_orbit_mean((7, 13, 19), 6) / twin_product_of_local_means((7, 13, 19), 6),
            __import__("fractions").Fraction(18657, 18700),
        )


    def test_local_mean_closed_form_matches_orbit_average(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            for h in (6, 12, 18, 30, 42):
                self.assertEqual(
                    twin_local_mean_closed_form(p, h),
                    twin_local_orbit_mean(p, h),
                )
                self.assertIn(
                    twin_local_mean_class(p, h),
                    {"zero-fixed", "special-even", "special-odd", "ordinary"},
                )

    def test_finite_global_orbit_invariant_is_dyadic(self):
        support = (5, 7, 11, 13, 17, 19, 23, 29, 31)
        for h in (6, 18, 30, 42, 66):
            reference = twin_finite_dyadic_orbit_invariant(support, h)
            for k in range(8):
                self.assertEqual(
                    twin_finite_dyadic_orbit_invariant(support, (2**k) * h),
                    reference,
                )


    def test_period_overlap_components_factorize_exactly(self):
        support = (7, 13, 31)
        self.assertEqual(
            twin_period_overlap_components(support, 6),
            ((7, 13), (31,)),
        )
        self.assertEqual(
            twin_global_orbit_mean(support, 6),
            twin_component_factorized_mean(support, 6),
        )

    def test_connected_pair_cumulant_is_resonance_correction(self):
        for support in ((5, 7), (7, 13), (13, 19)):
            self.assertEqual(
                twin_connected_resonance_cumulant(support, 6),
                twin_dyadic_resonance_correction(support, 6),
            )

    def test_genuine_three_channel_connected_term(self):
        self.assertEqual(
            twin_connected_resonance_cumulant((7, 13, 19), 6),
            __import__("fractions").Fraction(-5168743489, 457019805007872),
        )
        self.assertEqual(
            twin_connected_resonance_cumulant((5, 7, 11), 6),
            0,
        )


    def test_centered_joint_moment_resonance_bound(self):
        supports = (
            (5, 7),
            (7, 13),
            (7, 13, 19),
            (5, 7, 11),
            (7, 13, 19, 37),
        )
        for support in supports:
            moment = twin_centered_joint_moment(support, 6)
            bound = twin_centered_moment_resonance_bound(support, 6)
            self.assertLessEqual(abs(moment), bound)

    def test_connected_cumulant_fixed_order_bound(self):
        supports = (
            (5, 7),
            (7, 13),
            (13, 19),
            (7, 13, 19),
            (5, 7, 11),
            (7, 13, 19, 37),
        )
        for support in supports:
            actual = twin_connected_resonance_cumulant(support, 6)
            bound = twin_connected_cumulant_fixed_order_bound(support, 6)
            self.assertLessEqual(abs(actual), bound)

    def test_inactive_channel_kills_centered_moment(self):
        inactive = tuple(
            p for p in (5, 7, 11, 13, 17, 19, 23, 29, 31)
            if not twin_channel_is_dynamically_active(p, 6)
        )
        self.assertTrue(inactive)
        p = inactive[0]
        self.assertEqual(twin_centered_joint_moment((p, 7), 6), 0)


    def test_instantaneous_factorization_identity(self):
        support = (5, 7, 11, 13, 17, 19, 23, 29, 31)
        for h in (6, 18, 30, 42, 66):
            for r in range(8):
                self.assertEqual(
                    twin_finite_instantaneous_product(support, h, r),
                    twin_finite_instantaneous_factorization(support, h, r),
                )

    def test_local_correction_ratios(self):
        for p in (5, 7, 11, 13, 17, 19):
            beta = twin_background_factor(p)
            self.assertEqual(
                twin_quadruplet_local_factor(p, 0) / beta,
                twin_zero_correction_ratio(p),
            )
            self.assertEqual(
                twin_quadruplet_local_factor(p, 2) / beta,
                twin_special_correction_ratio(p),
            )
            self.assertEqual(
                twin_quadruplet_local_factor(p, -2) / beta,
                twin_special_correction_ratio(p),
            )


    def test_local_log_orbit_formula(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
            for h in (6, 18, 30, 42, 66):
                self.assertAlmostEqual(
                    twin_local_log_orbit_mean(p, h),
                    twin_local_log_orbit_formula(p, h),
                    places=12,
                )

    def test_special_hit_density_matches_direct_orbit(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
            h = 6
            d = twin_local_dyadic_period(p, h)
            if h % p == 0:
                expected = 0
            else:
                u = h % p
                hits = 0
                for _ in range(d):
                    if u in (2 % p, (-2) % p):
                        hits += 1
                    u = (2 * u) % p
                expected = __import__("fractions").Fraction(hits, d)
            self.assertEqual(twin_special_hit_density(p, h), expected)

    def test_finite_log_geometric_mean_is_dyadic_invariant(self):
        support = (5, 7, 11, 13, 17, 19, 23, 29, 31)
        for h in (6, 18, 30, 42):
            reference = twin_finite_log_geometric_mean(support, h, include_carriers=True)
            for k in range(6):
                self.assertAlmostEqual(
                    twin_finite_log_geometric_mean(support, (2**k)*h, include_carriers=True),
                    reference,
                    places=12,
                )


    def test_joint_special_hit_density_by_direct_clock(self):
        for p, q in ((5, 7), (7, 13), (13, 19), (11, 31)):
            dp = twin_local_dyadic_period(p, 6)
            dq = twin_local_dyadic_period(q, 6)
            L = __import__("math").lcm(dp, dq)
            hp = set(twin_special_hit_positions(p, 6))
            hq = set(twin_special_hit_positions(q, 6))
            count = sum((r % dp in hp) and (r % dq in hq) for r in range(L))
            self.assertEqual(
                twin_joint_special_hit_density(p, q, 6),
                __import__("fractions").Fraction(count, L),
            )

    def test_log_variance_matches_direct_common_clock(self):
        support = (5, 7, 11, 13, 17, 19)
        periods = [twin_local_dyadic_period(p, 6) for p in support]
        L = __import__("math").lcm(*periods)
        weights = {
            p: __import__("math").log(float(twin_special_correction_ratio(p)))
            for p in support
        }
        hit_sets = {p: set(twin_special_hit_positions(p, 6)) for p in support}
        values = [
            sum(weights[p] for p, d in zip(support, periods) if r % d in hit_sets[p])
            for r in range(L)
        ]
        mean = sum(values) / L
        direct = sum((v - mean) ** 2 for v in values) / L
        self.assertAlmostEqual(twin_finite_log_variance(support, 6), direct, places=12)

    def test_log_phase_parseval(self):
        for support in ((5, 7, 11), (5, 7, 11, 13, 17, 19)):
            self.assertAlmostEqual(
                twin_finite_log_variance(support, 6),
                twin_finite_log_parseval_power(support, 6),
                places=11,
            )

    def test_log_variance_is_dyadic_invariant(self):
        support = (5, 7, 11, 13, 17, 19, 23, 29, 31)
        reference = twin_finite_log_variance(support, 6)
        for k in range(6):
            self.assertAlmostEqual(
                twin_finite_log_variance(support, (2**k) * 6),
                reference,
                places=12,
            )


    def test_base4_observable_period_reduction(self):
        import math
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            if 6 % p == 0:
                continue
            d = doubling_order_mod_prime(p)
            e = quadruplet_observable_period(p, 6)
            self.assertEqual(e, d // math.gcd(d, 2))
            self.assertEqual(pow(4, e, p), 1)

    def test_base4_single_hit_phase_matches_plusminus2_clock(self):
        for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            phase = twin_quadratic_hit_phase(p, 6)
            e = quadruplet_observable_period(p, 6)
            old_hits = twin_special_hit_positions(p, 6)
            reduced = {r % e for r in old_hits}
            if phase is None:
                self.assertEqual(reduced, set())
                self.assertEqual(twin_quadratic_hit_density(p, 6), 0)
            else:
                self.assertEqual(reduced, {phase})
                self.assertEqual(
                    twin_quadratic_hit_density(p, 6),
                    __import__("fractions").Fraction(1, e),
                )

    def test_base4_joint_density_matches_old_density(self):
        for p, q in ((5, 7), (7, 13), (13, 19), (11, 29), (17, 31)):
            self.assertEqual(
                twin_quadratic_joint_hit_density(p, q, 6),
                twin_joint_special_hit_density(p, q, 6),
            )


    def test_fractional_subset_expansion_matches_direct_clock(self):
        supports = (
            (5, 7, 11),
            (5, 7, 11, 13),
            (7, 13, 19),
        )
        for support in supports:
            for s in (0.25, 0.5, 0.9):
                self.assertAlmostEqual(
                    twin_finite_fractional_common_clock_mean(support, 6, s),
                    twin_finite_fractional_subset_mean(support, 6, s),
                    places=12,
                )

    def test_fractional_mean_is_dyadic_invariant(self):
        support = (5, 7, 11, 13)
        for s in (0.25, 0.5, 0.9):
            reference = twin_finite_fractional_subset_mean(support, 6, s)
            for k in range(5):
                self.assertAlmostEqual(
                    twin_finite_fractional_subset_mean(support, (2**k) * 6, s),
                    reference,
                    places=12,
                )


    def test_real_moment_subset_expansion_matches_direct_clock(self):
        supports = ((5, 7, 11), (5, 7, 11, 13), (7, 13, 19))
        for support in supports:
            for s in (-2.0, -0.5, 0.0, 1.0, 2.0, 4.0):
                self.assertAlmostEqual(
                    twin_finite_real_moment_common_clock(support, 6, s),
                    twin_finite_real_moment_subset_mean(support, 6, s),
                    places=11,
                )

    def test_raw_arithmetic_mean_finite_support_is_dyadic_invariant(self):
        support = (5, 7, 11, 13, 19)
        reference = twin_finite_real_moment_subset_mean(support, 6, 1.0)
        for k in range(6):
            self.assertAlmostEqual(
                twin_finite_real_moment_subset_mean(support, (2**k)*6, 1.0),
                reference,
                places=12,
            )


if __name__ == "__main__":
    unittest.main()
