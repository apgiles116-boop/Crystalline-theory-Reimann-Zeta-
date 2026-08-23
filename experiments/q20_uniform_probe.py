"""A clean 21-point (q=20) exploratory finite-gap candidate.

This is not a certificate.  It uses the public kernel, uniform span-capacity
weights a_ij = 2/(q+1-(j-i)), pressure 1/3000, and a dimer/crystal local
minimizer found by binary64 L-BFGS-B search.

The point of this file is to freeze a simple, reproducible target for the next
fail-closed global verification campaign.
"""

from __future__ import annotations

from fractions import Fraction

from crystalline_zeta.deduction import optimize_block_length
from crystalline_zeta.finite_gap import finite_gap_objective


Q = 20
PRESSURE = Fraction(1, 3000)
CONSERVATIVE_TARGET = Fraction(23, 2000)  # 0.0115, deliberately below local min

# Binary64 local minimizer from a dimer seed. Reflection gives the equivalent
# reverse solution. Values are stored only as a discovery checkpoint.
LOCAL_MINIMIZER = (
    1.04512,
    1.97577,
    1.03915,
    1.96893,
    1.03792,
    1.96735,
    1.03746,
    1.96671,
    1.03727,
    1.96650,
    1.03724,
    1.96658,
    1.03735,
    1.96700,
    1.03766,
    1.96806,
    1.03842,
    1.97156,
    1.04122,
    1.99403,
)


def uniform_weights(q: int = Q) -> dict[tuple[int, int], float]:
    """Capacity-saturating homogeneous weights for every span."""
    return {
        (i, j): 2.0 / (q + 1 - (j - i))
        for i in range(q + 1)
        for j in range(i + 1, q + 1)
    }


def main() -> None:
    weights = uniform_weights()
    observed = finite_gap_objective(LOCAL_MINIMIZER, float(PRESSURE), weights)
    candidate_bound, block_length = optimize_block_length(
        Q, float(PRESSURE), float(CONSERVATIVE_TARGET), maximum_m=500
    )
    optimistic_bound, optimistic_m = optimize_block_length(
        Q, float(PRESSURE), observed, maximum_m=500
    )

    print("q                              :", Q)
    print("pressure                       :", float(PRESSURE))
    print("local observed F               :", f"{observed:.15f}")
    print("conservative target            :", float(CONSERVATIVE_TARGET))
    print("local margin over target       :", f"{observed-float(CONSERVATIVE_TARGET):.9g}")
    print("projected bound at target      :", f"{candidate_bound:.12f}")
    print("best block length              :", block_length)
    print("optimistic local-only projection:", f"{optimistic_bound:.12f}")
    print("optimistic block length        :", optimistic_m)
    print()
    print("WARNING: neither projection is certified until the global q=20")
    print("finite-gap inequality is proved over every nonnegative gap vector.")


if __name__ == "__main__":
    main()
