"""Falsified q=20 uniform-weight crystalline candidate.

This file records an instructive negative result. A dimer seed initially gave
F ~= 0.0115173430872 for q=20 uniform span-capacity weights and pressure
1/3000, suggesting a projected bound above the current public record.

An exhaustive search over all 2^20 binary words g_i in {1,2} found the unique
binary ground pattern 112112... . Continuous relaxation from that seed drops
the objective to F ~= 0.0111220298291, which kills the proposed target 0.0115.

Keeping this failed candidate in the repository prevents accidental reuse and
shows why crystalline adversarial seeds must be tested before certification.
"""

from __future__ import annotations

from fractions import Fraction

from crystalline_zeta.deduction import optimize_block_length
from crystalline_zeta.finite_gap import finite_gap_objective


Q = 20
PRESSURE = Fraction(1, 3000)
KILLED_TARGET = Fraction(23, 2000)  # 0.0115

DIMER_LOCAL_MINIMIZER = (
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

# Continuous L-BFGS-B relaxation of the binary 112112... adversarial seed.
ADVERSARIAL_112_MINIMIZER = (
    1.035563,
    1.031998,
    1.959052,
    1.028088,
    1.027701,
    1.954169,
    1.026974,
    1.026873,
    1.953137,
    1.026710,
    1.026710,
    1.953137,
    1.026873,
    1.026974,
    1.954169,
    1.027701,
    1.028088,
    1.959052,
    1.031998,
    1.035563,
)


def uniform_weights(q: int = Q) -> dict[tuple[int, int], float]:
    return {
        (i, j): 2.0 / (q + 1 - (j - i))
        for i in range(q + 1)
        for j in range(i + 1, q + 1)
    }


def main() -> None:
    weights = uniform_weights()
    dimer = finite_gap_objective(DIMER_LOCAL_MINIMIZER, float(PRESSURE), weights)
    adversarial = finite_gap_objective(ADVERSARIAL_112_MINIMIZER, float(PRESSURE), weights)
    killed_bound, killed_m = optimize_block_length(
        Q, float(PRESSURE), float(KILLED_TARGET), maximum_m=500
    )
    surviving_local_projection, surviving_m = optimize_block_length(
        Q, float(PRESSURE), adversarial, maximum_m=500
    )

    print("q                         :", Q)
    print("pressure                  :", float(PRESSURE))
    print("dimer local F             :", f"{dimer:.15f}")
    print("112 adversarial local F   :", f"{adversarial:.15f}")
    print("killed target             :", float(KILLED_TARGET))
    print("target violated?          :", adversarial < float(KILLED_TARGET))
    print("old projected bound       :", f"{killed_bound:.12f}", "at m=", killed_m)
    print("projection using 112 F    :", f"{surviving_local_projection:.12f}", "at m=", surviving_m)
    print()
    print("STATUS: FALSIFIED. Do not attempt interval certification of 0.0115.")


if __name__ == "__main__":
    main()
