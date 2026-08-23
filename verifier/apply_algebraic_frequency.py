"""Apply the crystalline algebraic-frequency extension to the pinned upstream verifier.

This intentionally uses exact source-shape checks rather than a fuzzy patch. If
upstream changes the relevant code, the script fails closed and CI must be
updated deliberately.
"""

from __future__ import annotations

from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source match, found {count}")
    return text.replace(old, new, 1)


def patch_kernel(path: Path) -> None:
    text = path.read_text()

    old_fields = '''    has_sqrt2_term: bool = True  # first term omega = sqrt(2) when True\n\n    def __post_init__(self) -> None:\n        expected = len(self.omega_pi_multiples) + (1 if self.has_sqrt2_term else 0)\n        if len(self.coeffs) != expected:\n            raise ValueError("coefficient count mismatch")\n'''
    new_fields = '''    has_sqrt2_term: bool = True  # first term omega = sqrt(2) when True\n    algebraic_omegas: Tuple[Tuple[fmpq, int], ...] = ()\n\n    def __post_init__(self) -> None:\n        expected = (\n            len(self.omega_pi_multiples)\n            + len(self.algebraic_omegas)\n            + (1 if self.has_sqrt2_term else 0)\n        )\n        if len(self.coeffs) != expected:\n            raise ValueError("coefficient count mismatch")\n        for _, radicand in self.algebraic_omegas:\n            if radicand <= 0:\n                raise ValueError("algebraic frequency radicands must be positive")\n'''
    text = replace_once(text, old_fields, new_fields, "KernelSpec extension")

    old_omegas = '''def _omegas(spec: KernelSpec) -> List[arb]:\n    result: List[arb] = []\n    if spec.has_sqrt2_term:\n        result.append(arb(2).sqrt())\n    pi = arb.pi()\n    for mult in spec.omega_pi_multiples:\n        result.append(mult * pi)\n    return result\n'''
    new_omegas = '''def kernel_omegas(spec: KernelSpec) -> List[arb]:\n    """Construct all frequencies as rigorous Arb balls."""\n    result: List[arb] = []\n    if spec.has_sqrt2_term:\n        result.append(arb(2).sqrt())\n    pi = arb.pi()\n    for mult in spec.omega_pi_multiples:\n        result.append(mult * pi)\n    for scale, radicand in spec.algebraic_omegas:\n        result.append(arb(scale) * arb(radicand).sqrt())\n    return result\n\n\n_omegas = kernel_omegas\n'''
    text = replace_once(text, old_omegas, new_omegas, "kernel frequency constructor")
    path.write_text(text)


def patch_h0(path: Path) -> None:
    text = path.read_text()
    text = replace_once(
        text,
        'from .kernel import KernelSpec, sinc_derivatives\n',
        'from .kernel import KernelSpec, kernel_omegas, sinc_derivatives\n',
        "h0 import",
    )
    old = '''def _omegas(spec: KernelSpec) -> List[arb]:\n    result: List[arb] = []\n    if spec.has_sqrt2_term:\n        result.append(arb(2).sqrt())\n    pi = arb.pi()\n    for mult in spec.omega_pi_multiples:\n        result.append(mult * pi)\n    return result\n'''
    text = replace_once(text, old, '_omegas = kernel_omegas\n', "h0 frequency constructor")
    path.write_text(text)


def main() -> None:
    root = Path(__file__).resolve().parent.parent / "upstream"
    if not root.exists():
        root = Path.cwd()
    patch_kernel(root / "src/zeta_ext/kernel.py")
    patch_h0(root / "src/zeta_ext/h0_cert.py")
    print("algebraic-frequency extension applied")


if __name__ == "__main__":
    main()
