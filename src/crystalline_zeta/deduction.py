"""Floating versions of the refined finite-m deduction formulas.

These formulas mirror the public refined deduction used by
``trmdy/zeta-simple-zeros-673137``.  They are for candidate exploration; a
proof must use exact rationals and interval arithmetic.
"""

from __future__ import annotations

import math


H_CERT = 3_362_285_207 / 5_000_000_000


def refined_bound(q: int, pressure: float, target: float, m: int) -> float:
    """Evaluate the refined finite-m assembly for a candidate certificate."""
    if q <= 0 or m <= q:
        raise ValueError("require 0 < q < m")
    if pressure < 0.0 or target <= 0.0:
        raise ValueError("pressure must be nonnegative and target positive")

    a_value = target * (m - q)
    phi = 2.0 * math.sqrt(((m - 1) / m) * a_value) - 1.0 + a_value / m
    return (
        m * H_CERT - (m - q) * q * pressure
    ) / (m - phi)


def optimize_block_length(
    q: int,
    pressure: float,
    target: float,
    minimum_m: int | None = None,
    maximum_m: int = 1000,
) -> tuple[float, int]:
    """Return the best floating assembled bound and block length in a range."""
    if minimum_m is None:
        minimum_m = q + 1
    best_bound = float("-inf")
    best_m = -1
    for m in range(max(q + 1, minimum_m), maximum_m + 1):
        value = refined_bound(q, pressure, target, m)
        if value > best_bound:
            best_bound = value
            best_m = m
    return best_bound, best_m
