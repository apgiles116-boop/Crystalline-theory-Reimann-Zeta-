from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence


Kernel = Callable[[float], complex]


def pairwise_distance_matrix(points: Sequence[float]) -> list[list[float]]:
    return [[abs(x - y) for y in points] for x in points]


def gram_matrix(points: Sequence[float], kernel: Kernel) -> list[list[complex]]:
    """Construct the Hermitian-style kernel Gram matrix K(x_i-x_j).

    The caller is responsible for supplying a kernel with the required
    positive-definiteness/symmetry properties for the intended theorem.
    """
    return [[kernel(x - y) for y in points] for x in points]


def quadratic_form(matrix: Sequence[Sequence[complex]], weights: Sequence[complex]) -> complex:
    if len(matrix) != len(weights):
        raise ValueError("matrix/weight dimension mismatch")
    total = 0j
    for i, wi in enumerate(weights):
        for j, wj in enumerate(weights):
            total += wi.conjugate() * matrix[i][j] * wj
    return total


def normalized_equal_weight_energy(points: Sequence[float], kernel: Kernel) -> float:
    """Equal-weight normalized quadratic energy, useful as a geometry diagnostic."""
    n = len(points)
    if n == 0:
        raise ValueError("need at least one point")
    G = gram_matrix(points, kernel)
    w = [1 / math.sqrt(n)] * n
    return float(quadratic_form(G, w).real)


def toeplitz_symbol(samples: Sequence[complex], theta: float) -> complex:
    """Evaluate a finite symmetric Toeplitz symbol from nonnegative-lag samples.

    samples[k] represents K(kh), k >= 0. Assumes the negative-lag coefficient
    is conjugate(samples[k]).
    """
    if not samples:
        return 0j
    val = complex(samples[0])
    for k, ck in enumerate(samples[1:], start=1):
        val += ck * cmath.exp(-1j * k * theta) + ck.conjugate() * cmath.exp(1j * k * theta)
    return val


def second_differences(values: Sequence[float]) -> list[float]:
    return [values[i + 1] - 2 * values[i] + values[i - 1] for i in range(1, len(values) - 1)]


@dataclass(frozen=True)
class GeometryDiagnostics:
    min_gap: float
    max_gap: float
    mean_gap: float
    gap_variance: float
    span: float


def geometry_diagnostics(points: Sequence[float]) -> GeometryDiagnostics:
    xs = sorted(points)
    if len(xs) < 2:
        return GeometryDiagnostics(0.0, 0.0, 0.0, 0.0, 0.0)
    gaps = [b - a for a, b in zip(xs, xs[1:])]
    mean = sum(gaps) / len(gaps)
    var = sum((g - mean) ** 2 for g in gaps) / len(gaps)
    return GeometryDiagnostics(min(gaps), max(gaps), mean, var, xs[-1] - xs[0])
