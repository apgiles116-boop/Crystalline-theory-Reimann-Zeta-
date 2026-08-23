"""Reproduction utilities for the public nine-point finite-gap certificate.

The constants and objective in this module are transcribed from the MIT-licensed
public repository ``trmdy/zeta-simple-zeros-673137``.  This module is a
floating-point research harness only; it is not an interval verifier.

The certified objective has the form

    F(g_1,...,g_q) = p * sum(g_i)
                   + sum_{0<=i<j<=q} a_ij * w(y_j-y_i),

where y_j = g_1+...+g_j and w(x)=(K(x)/K(0))^2.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Sequence


WINDOW_DENOMINATOR = 10**9
WINDOW_NUMERATORS = (
    1_000_000_000,
    3_322_500,
    -7_609_135,
    1_190_194,
    -731_476,
    -1_680_572,
    1_141_360,
)
WINDOW_COEFFICIENTS = tuple(n / WINDOW_DENOMINATOR for n in WINDOW_NUMERATORS)

NINE_POINT_PRESSURE = Fraction(1, 2500)
NINE_POINT_TARGET = Fraction(15_211, 2_500_000)
NINE_POINT_WEIGHT_DENOMINATOR = 10_000_000
NINE_POINT_WEIGHT_NUMERATORS = (
    1_802_576, 4_832_031, 5_411_933, 10_000_000, 10_000_000, 10_000_000,
    10_000_000, 20_000_000,
    2_694_869, 2_295_599, 1_780_844, 0, 0, 0, 10_000_000,
    2_714_860, 0, 2_807_223, 0, 0, 10_000_000,
    2_787_695, 5_744_740, 2_807_223, 0, 10_000_000,
    2_787_695, 0, 1_780_844, 10_000_000,
    2_714_860, 2_295_599, 5_411_933,
    2_694_869, 4_832_031,
    1_802_576,
)

NINE_POINT_FLOAT_MINIMIZER = (
    1.0380368456650184,
    1.976267441774638,
    1.0388837672365134,
    1.9726539577231619,
    1.0384947052911064,
    1.964068181294902,
    1.0348237069572437,
    1.02447768443671,
)
NINE_POINT_REPORTED_FLOAT_MINIMUM = 0.006102730481857188


def _sinc(z: float) -> float:
    if z == 0.0:
        return 1.0
    return math.sin(z) / z


def window_kernel(x: float) -> float:
    """Evaluate the public cosine-window overlap kernel K(x) in binary64."""
    c = 2.0 * math.pi * x
    omegas = (math.sqrt(2.0),) + tuple(2.0 * math.pi * j for j in range(1, 7))
    total = 0.0
    for coefficient, omega in zip(WINDOW_COEFFICIENTS, omegas):
        total += coefficient * (
            _sinc((omega - c) / 2.0) + _sinc((omega + c) / 2.0)
        ) / 2.0
    return total


KERNEL_AT_ZERO = window_kernel(0.0)


def squared_normalized_kernel(x: float) -> float:
    value = window_kernel(x) / KERNEL_AT_ZERO
    return value * value


def pair_order(point_count: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (i, j)
        for i in range(point_count)
        for j in range(i + 1, point_count)
    )


NINE_POINT_PAIR_ORDER = pair_order(9)
NINE_POINT_WEIGHTS = {
    pair: numerator / NINE_POINT_WEIGHT_DENOMINATOR
    for pair, numerator in zip(NINE_POINT_PAIR_ORDER, NINE_POINT_WEIGHT_NUMERATORS)
    if numerator
}


def finite_gap_objective(
    gaps: Sequence[float],
    pressure: float,
    weights: Mapping[tuple[int, int], float],
) -> float:
    """Evaluate F for an arbitrary nonnegative gap vector and pair weights."""
    q = len(gaps)
    points = [0.0]
    for gap in gaps:
        if gap < 0.0:
            raise ValueError("gaps must be nonnegative")
        points.append(points[-1] + float(gap))

    result = float(pressure) * sum(float(g) for g in gaps)
    for (i, j), weight in weights.items():
        if not (0 <= i < j <= q):
            raise ValueError(f"weight index {(i, j)} outside gap window")
        result += weight * squared_normalized_kernel(points[j] - points[i])
    return result


def nine_point_objective(gaps: Sequence[float]) -> float:
    if len(gaps) != 8:
        raise ValueError("nine-point objective requires eight gaps")
    return finite_gap_objective(
        gaps,
        float(NINE_POINT_PRESSURE),
        NINE_POINT_WEIGHTS,
    )


def span_contributions(gaps: Sequence[float]) -> dict[int, float]:
    """Break the nine-point pair term into contributions by span j-i."""
    if len(gaps) != 8:
        raise ValueError("nine-point objective requires eight gaps")
    points = [0.0]
    for gap in gaps:
        points.append(points[-1] + float(gap))
    result = {r: 0.0 for r in range(1, 9)}
    for (i, j), weight in NINE_POINT_WEIGHTS.items():
        result[j - i] += weight * squared_normalized_kernel(points[j] - points[i])
    return result


@dataclass(frozen=True)
class ReproductionCheck:
    observed: float
    reference: float

    @property
    def absolute_error(self) -> float:
        return abs(self.observed - self.reference)


def reproduce_nine_point_minimum() -> ReproductionCheck:
    observed = nine_point_objective(NINE_POINT_FLOAT_MINIMIZER)
    return ReproductionCheck(observed, NINE_POINT_REPORTED_FLOAT_MINIMUM)
