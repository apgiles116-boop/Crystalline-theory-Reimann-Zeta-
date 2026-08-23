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


def patch_parallel(path: Path) -> None:
    """Keep algebraic frequencies intact when CertificateSpec crosses processes."""
    text = path.read_text()
    old_encode = '''        "omega_pi_multiples": list(spec.kernel.omega_pi_multiples),\n        "has_sqrt2_term": spec.kernel.has_sqrt2_term,\n        "q": spec.q,\n'''
    new_encode = '''        "omega_pi_multiples": list(spec.kernel.omega_pi_multiples),\n        "has_sqrt2_term": spec.kernel.has_sqrt2_term,\n        "algebraic_omegas": [\n            ((int(scale.p), int(scale.q)), int(radicand))\n            for scale, radicand in spec.kernel.algebraic_omegas\n        ],\n        "q": spec.q,\n'''
    text = replace_once(text, old_encode, new_encode, "parallel kernel encoding")

    old_decode = '''        omega_pi_multiples=tuple(data["omega_pi_multiples"]),\n        has_sqrt2_term=data["has_sqrt2_term"],\n    )\n'''
    new_decode = '''        omega_pi_multiples=tuple(data["omega_pi_multiples"]),\n        has_sqrt2_term=data["has_sqrt2_term"],\n        algebraic_omegas=tuple(\n            (fmpq(p, q), int(radicand))\n            for (p, q), radicand in data.get("algebraic_omegas", [])\n        ),\n    )\n'''
    text = replace_once(text, old_decode, new_decode, "parallel kernel decoding")
    path.write_text(text)


def patch_verify_general(path: Path) -> None:
    """Add focused-box starts and fail-closed terminal-cell collection."""
    text = path.read_text()

    old_signature = '''def verify_general(\n    spec: CertificateSpec,\n    progress_every: int = 0,\n    shard: int = 0,\n    shard_count: int = 1,\n    tables: Optional[Tuple[List[float], List[float]]] = None,\n) -> GeneralReport:\n'''
    new_signature = '''def verify_general(\n    spec: CertificateSpec,\n    progress_every: int = 0,\n    shard: int = 0,\n    shard_count: int = 1,\n    tables: Optional[Tuple[List[float], List[float]]] = None,\n    initial_boxes: Optional[Sequence[Tuple[CellRange, ...]]] = None,\n    collect_unresolved: bool = False,\n    unresolved_out: Optional[List[Tuple[Tuple[CellRange, ...], float]]] = None,\n) -> GeneralReport:\n'''
    text = replace_once(
        text, old_signature, new_signature, "verify_general extended signature"
    )

    old_stack = '''    stack: List[Tuple[Tuple[CellRange, ...], int]] = [\n        (tuple(parts), 0)\n        for index, parts in enumerate(itertools.product(*coordinate_components))\n        if index % shard_count == shard\n    ]\n    initial_boxes = len(stack)\n'''
    new_stack = '''    if initial_boxes is None:\n        stack: List[Tuple[Tuple[CellRange, ...], int]] = [\n            (tuple(parts), 0)\n            for index, parts in enumerate(itertools.product(*coordinate_components))\n            if index % shard_count == shard\n        ]\n    else:\n        checked_boxes: List[Tuple[CellRange, ...]] = []\n        for supplied in initial_boxes:\n            if len(supplied) != q:\n                raise ValueError("initial box dimension mismatch")\n            normalized = tuple((int(left), int(right)) for left, right in supplied)\n            for left, right in normalized:\n                if left < 0 or right < left:\n                    raise ValueError("invalid initial cell range")\n            checked_boxes.append(normalized)\n        stack = [\n            (box, 0)\n            for index, box in enumerate(checked_boxes)\n            if index % shard_count == shard\n        ]\n    initial_box_count = len(stack)\n'''
    text = replace_once(
        text, old_stack, new_stack, "verify_general initial-box stack"
    )

    text = replace_once(
        text,
        '    nodes = pruned = splits = maximum_depth = 0\n',
        '    nodes = pruned = splits = maximum_depth = 0\n    unresolved_count = 0\n',
        "verify_general unresolved counter",
    )

    old_terminal = '''        if max(widths) == 0:\n            raise RuntimeError(\n                f"certificate failed at a terminal cell: box={box}, lower={lower}"\n            )\n'''
    new_terminal = '''        if max(widths) == 0:\n            if collect_unresolved:\n                unresolved_count += 1\n                if unresolved_out is not None:\n                    unresolved_out.append((tuple(box), lower))\n                continue\n            raise RuntimeError(\n                f"certificate failed at a terminal cell: box={box}, lower={lower}"\n            )\n'''
    text = replace_once(
        text, old_terminal, new_terminal, "verify_general terminal collector"
    )

    text = replace_once(
        text,
        '        verified=True,\n',
        '        verified=(unresolved_count == 0),\n',
        "verify_general verified flag",
    )
    text = replace_once(
        text,
        '        initial_boxes=initial_boxes,\n',
        '        initial_boxes=initial_box_count,\n',
        "verify_general report initial-box count",
    )
    text = replace_once(
        text,
        '            "pressure_pruned": pressure_pruned,\n',
        '            "pressure_pruned": pressure_pruned,\n            "unresolved_count": unresolved_count,\n',
        "verify_general unresolved report",
    )
    path.write_text(text)


def main() -> None:
    root = Path(__file__).resolve().parent.parent / "upstream"
    if not root.exists():
        root = Path.cwd()
    patch_kernel(root / "src/zeta_ext/kernel.py")
    patch_h0(root / "src/zeta_ext/h0_cert.py")
    patch_parallel(root / "src/zeta_ext/parallel.py")
    patch_verify_general(root / "src/zeta_ext/verify_general.py")
    print("algebraic-frequency, targeted-box, and collector extensions applied")


if __name__ == "__main__":
    main()
