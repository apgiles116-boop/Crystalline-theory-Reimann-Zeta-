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
    1.045121091678781,
    1.9757697282288766,
    1.0391550128798599,
    1.9689283612878066,
    1.03792109773301,
    1.9673536713895721,
    1.0374603464038472,
    1.9667124098325488,
    1.0372739256209857,
    1.9664978134126267,
    1.0372428561303841,
    1.9665761795367578,
    1.0373508916449228,
    1.9669960284881778,
    1.0376616383090707,
    1.9680613510363698,
    1.0384158263745193,
    1.9715578157241842,
    1.0412195891685312,
    1.9940253981635425,
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
