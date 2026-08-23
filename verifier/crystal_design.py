"""Exact crystalline-spectrum seven-point candidate."""

from __future__ import annotations

from flint import arb, fmpq
from .kernel import KernelSpec
from .verify_general import CertificateSpec

ALPHA = fmpq(8_796_791, 1_000_000)
WINDOW_DENOMINATOR = 10**9
WINDOW_NUMERATORS = (
    1_000_000_000,
    321_105,
    2_731_970,
    -18_049_287,
    27_754_300,
    -24_732_331,
    10_205_774,
)
CRYSTAL_RADICANDS = (1, 3, 4, 7, 9, 12)

KERNEL = KernelSpec(
    coeffs=tuple(fmpq(n, WINDOW_DENOMINATOR) for n in WINDOW_NUMERATORS),
    omega_pi_multiples=(),
    has_sqrt2_term=True,
    algebraic_omegas=tuple((ALPHA, r) for r in CRYSTAL_RADICANDS),
)

WEIGHT_DENOMINATOR = 10**6
WEIGHT_NUMERATORS = {
    (0,1):225_284,(1,2):418_596,(2,3):356_120,
    (3,4):356_120,(4,5):418_596,(5,6):225_284,
    (0,2):825_671,(1,3):106_631,(2,4):135_396,
    (3,5):106_631,(4,6):825_671,
    (0,3):1_000_000,(1,4):0,(2,5):0,(3,6):1_000_000,
    (0,4):1_000_000,(1,5):0,(2,6):1_000_000,
    (0,5):1_000_000,(1,6):1_000_000,
    (0,6):2_000_000,
}

PRESSURE = fmpq(1, 1980)
TARGET = fmpq(299, 50_000)
H_CERT = fmpq(6_723_743, 10_000_000)
WINDOW_MIN = fmpq(3, 4)
REFINED_BLOCK_LENGTH = 177
FINAL_BOUND_RATIONAL = fmpq(6_733_364, 10_000_000)

def certificate_spec(grid: int = 4000, use_tangent: bool = True) -> CertificateSpec:
    weights = {
        key: fmpq(value, WEIGHT_DENOMINATOR)
        for key, value in WEIGHT_NUMERATORS.items()
        if value
    }
    return CertificateSpec(
        kernel=KERNEL, q=6, pressure=PRESSURE, target=TARGET,
        weights=weights, grid=grid, use_tangent=use_tangent,
    )

def refined_final_bound() -> tuple[arb, arb, arb]:
    m = REFINED_BLOCK_LENGTH
    q = 6
    a_value = arb(TARGET) * (m - q)
    phi = 2 * (arb(fmpq(m - 1, m)) * a_value).sqrt() - 1 + a_value / m
    bound = (
        m * arb(H_CERT) - (m - q) * q * arb(PRESSURE)
    ) / (m - phi)
    return bound, a_value, phi
