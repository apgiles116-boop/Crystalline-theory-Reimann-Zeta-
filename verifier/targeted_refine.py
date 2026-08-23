"""Rigorous local refinement of the unresolved grid-250 crystalline cell.

This script does not replace the global certificate.  It asks the canonical
interval verifier to check only the exact children of the one grid-250 cell
that remained unresolved in the first global run.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import time

from zeta_ext import crystal_design
from zeta_ext.verify_general import verify_general

PARENT_GRID = 250
PARENT_INDICES = (494, 263, 499, 499, 263, 494)


def focused_boxes(grid: int):
    """Return every grid-cell child of the recorded grid-250 parent cell."""
    if grid < PARENT_GRID or grid % PARENT_GRID:
        raise ValueError("grid must be a positive multiple of 250")
    ratio = grid // PARENT_GRID
    coordinate_children = [
        range(index * ratio, (index + 1) * ratio)
        for index in PARENT_INDICES
    ]
    return [
        tuple((index, index) for index in child)
        for child in itertools.product(*coordinate_children)
    ]


def main(grid: int, no_tangent: bool) -> int:
    boxes = focused_boxes(grid)
    spec = crystal_design.certificate_spec(grid, not no_tangent)

    print("targeted_parent_grid", PARENT_GRID)
    print("targeted_parent_indices", PARENT_INDICES)
    print("targeted_grid", grid)
    print("targeted_ratio", grid // PARENT_GRID)
    print("targeted_boxes", len(boxes))
    print("target", crystal_design.TARGET)
    print("use_tangent", not no_tangent)

    started = time.time()
    try:
        report = verify_general(
            spec,
            progress_every=0,
            initial_boxes=boxes,
        )
    except RuntimeError as exc:
        print("targeted_verified=False")
        print("failure", exc)
        print("wall_seconds", time.time() - started)
        return 1

    print("\n".join(report.lines()))
    print("targeted_verified", report.verified)
    print("wall_seconds", time.time() - started)
    return 0 if report.verified else 1


def entry() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=500)
    parser.add_argument("--no-tangent", action="store_true")
    args = parser.parse_args()
    return main(args.grid, args.no_tangent)


if __name__ == "__main__":
    sys.exit(entry())
