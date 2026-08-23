"""Reproduce two public numerical checkpoints tied to the crystal hypothesis.

1. The published nine-point floating minimizer.
2. The 673-on-1000 balanced periodic word used upstream as a pair-energy
   obstruction.

This script is exploratory binary64 numerics, not an interval certificate.
"""

from __future__ import annotations

from collections import Counter

from crystalline_zeta.finite_gap import (
    NINE_POINT_FLOAT_MINIMIZER,
    NINE_POINT_REPORTED_FLOAT_MINIMUM,
    NINE_POINT_TARGET,
    nine_point_objective,
    span_contributions,
    squared_normalized_kernel,
)
from crystalline_zeta.geometry import mechanical_word


POINTS_PER_PERIOD = 673
PERIOD_LENGTH = 1000
EXCESS_UNITS = PERIOD_LENGTH - POINTS_PER_PERIOD  # 327
UPSTREAM_PAIR_ENERGY_CEILING = 0.003523506664


def balanced_period() -> tuple[list[int], list[int]]:
    """Return the 327/673 Christoffel bits and the corresponding 1/2 gaps."""
    bits = mechanical_word(EXCESS_UNITS, POINTS_PER_PERIOD, POINTS_PER_PERIOD)
    gaps = [1 + bit for bit in bits]
    assert len(gaps) == POINTS_PER_PERIOD
    assert sum(bits) == EXCESS_UNITS
    assert sum(gaps) == PERIOD_LENGTH
    return bits, gaps


def period_positions(gaps: list[int]) -> list[int]:
    points = [0]
    for gap in gaps[:-1]:
        points.append(points[-1] + gap)
    return points


def residue_counts(points: list[int], period: int) -> Counter[int]:
    counts: Counter[int] = Counter()
    for x in points:
        for y in points:
            counts[(y - x) % period] += 1
    return counts


def periodic_pair_energy(image_radius: int = 10) -> float:
    """Mean two-sided pair energy per point for the periodic balanced crystal.

    We sum periodic images k=-image_radius..image_radius.  Because the kernel
    square has an O(x^-2) tail, radius 10 is already stable well beyond the
    digits needed for the public 0.003523506664 comparison.
    """
    _, gaps = balanced_period()
    points = period_positions(gaps)
    counts = residue_counts(points, PERIOD_LENGTH)

    total = 0.0
    for residue, multiplicity in counts.items():
        for image in range(-image_radius, image_radius + 1):
            displacement = residue + image * PERIOD_LENGTH
            if displacement == 0:
                continue
            total += multiplicity * squared_normalized_kernel(abs(displacement))
    return total / POINTS_PER_PERIOD


def main() -> None:
    value = nine_point_objective(NINE_POINT_FLOAT_MINIMIZER)
    print("nine-point reported float minimum :", NINE_POINT_REPORTED_FLOAT_MINIMUM)
    print("nine-point reproduced minimum     :", f"{value:.16f}")
    print("absolute reproduction error       :", f"{abs(value-NINE_POINT_REPORTED_FLOAT_MINIMUM):.3e}")
    print("certified finite-gap target        :", float(NINE_POINT_TARGET))
    print("floating target margin             :", f"{value-float(NINE_POINT_TARGET):.16g}")
    print()

    print("span contributions at minimizer:")
    for span, contribution in sorted(span_contributions(NINE_POINT_FLOAT_MINIMIZER).items()):
        print(f"  span {span}: {contribution:.16g}")
    print()

    bits, gaps = balanced_period()
    print("balanced crystal period:")
    print("  points / length                 :", POINTS_PER_PERIOD, "/", PERIOD_LENGTH)
    print("  1-gaps / 2-gaps                 :", gaps.count(1), "/", gaps.count(2))
    print("  excess units                    :", sum(bits))

    energy = periodic_pair_energy(image_radius=10)
    print("  reproduced periodic pair energy :", f"{energy:.15f}")
    print("  upstream stated ceiling          :", f"{UPSTREAM_PAIR_ENERGY_CEILING:.12f}")
    print("  below stated ceiling?            :", energy < UPSTREAM_PAIR_ENERGY_CEILING)


if __name__ == "__main__":
    main()
