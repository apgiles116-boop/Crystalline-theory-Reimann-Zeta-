from __future__ import annotations

import unittest

from crystalline_zeta.finite_gap import reproduce_nine_point_minimum
from crystalline_zeta.geometry import mechanical_word


class ReproductionTests(unittest.TestCase):
    def test_nine_point_float_minimum_reproduces(self) -> None:
        check = reproduce_nine_point_minimum()
        self.assertLess(check.absolute_error, 5e-16)

    def test_balanced_327_673_period(self) -> None:
        bits = mechanical_word(327, 673, 673)
        self.assertEqual(len(bits), 673)
        self.assertEqual(sum(bits), 327)
        gaps = [1 + bit for bit in bits]
        self.assertEqual(gaps.count(1), 346)
        self.assertEqual(gaps.count(2), 327)
        self.assertEqual(sum(gaps), 1000)


if __name__ == "__main__":
    unittest.main()
