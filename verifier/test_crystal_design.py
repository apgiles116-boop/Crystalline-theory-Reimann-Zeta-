"""Tests for the crystalline seven-point candidate."""

import unittest
from flint import arb, ctx, fmpq
from zeta_ext import crystal_design
from zeta_ext.h0_cert import (
    window_functional, window_min_enclosure, window_monotone_factor_upper,
)
from zeta_ext.kernel import kernel_omegas
from zeta_ext.parallel import _spec_from_primitives, _spec_to_primitives

class CrystalTests(unittest.TestCase):
    def test_exact_frequencies(self):
        ctx.prec = 192
        a = arb(crystal_design.ALPHA)
        expected = [
            arb(2).sqrt(), a, a*arb(3).sqrt(), 2*a,
            a*arb(7).sqrt(), 3*a, 2*a*arb(3).sqrt(),
        ]
        got = kernel_omegas(crystal_design.KERNEL)
        self.assertEqual(len(got), len(expected))
        for x, y in zip(got, expected):
            self.assertTrue(x.overlaps(y))

    def test_parallel_round_trip_preserves_algebraic_frequencies(self):
        spec = crystal_design.certificate_spec(grid=250)
        rebuilt = _spec_from_primitives(_spec_to_primitives(spec))
        self.assertEqual(rebuilt.kernel.algebraic_omegas, spec.kernel.algebraic_omegas)
        self.assertEqual(rebuilt.kernel.coeffs, spec.kernel.coeffs)
        self.assertEqual(rebuilt.weights, spec.weights)
        self.assertEqual(rebuilt.pressure, spec.pressure)
        self.assertEqual(rebuilt.target, spec.target)

    def test_span_capacities(self):
        for r in range(1, 7):
            total = sum(
                (fmpq(v, crystal_design.WEIGHT_DENOMINATOR)
                 for (i,j),v in crystal_design.WEIGHT_NUMERATORS.items()
                 if j-i == r),
                fmpq(0),
            )
            self.assertEqual(total, fmpq(2))

    def test_reflection_symmetry(self):
        w = crystal_design.WEIGHT_NUMERATORS
        for (i,j), value in w.items():
            self.assertEqual(value, w[(6-j, 6-i)])

    def test_capacity_gate(self):
        self.assertTrue(crystal_design.certificate_spec().capacity_ok())

    def test_window_hypotheses(self):
        ctx.prec = 256
        low = window_min_enclosure(crystal_design.KERNEL, 4096)
        self.assertTrue(low >= arb(crystal_design.WINDOW_MIN))
        monotone = window_monotone_factor_upper(crystal_design.KERNEL, 4096)
        self.assertTrue(monotone <= 0)
        _, h = window_functional(crystal_design.KERNEL)
        self.assertTrue(h >= arb(crystal_design.H_CERT))

    def test_refined_bound(self):
        ctx.prec = 256
        bound, _, _ = crystal_design.refined_final_bound()
        self.assertTrue(bound >= arb(crystal_design.FINAL_BOUND_RATIONAL))

if __name__ == "__main__":
    unittest.main(verbosity=2)
