"""Exhaust the grid-250 search, collect every terminal miss, and refine only misses.

A successful exit is a mixed-resolution global certificate: every region pruned
at grid 250 is already rigorous, and every grid-250 terminal miss is covered by
rigorously certified children at grid 500 or (if necessary) grid 1000.
"""

from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

from zeta_ext import crystal_design
from zeta_ext.verify_general import verify_general

Q = 6


def terminal_boxes(cells):
    return [box for box, _lower in cells]


def refine_boxes(cells, parent_grid: int, child_grid: int):
    if child_grid <= parent_grid or child_grid % parent_grid:
        raise ValueError("child grid must be a larger integer multiple of parent grid")
    ratio = child_grid // parent_grid
    result = set()
    for box, _lower in cells:
        if len(box) != Q:
            raise ValueError("unexpected box dimension")
        choices = []
        for left, right in box:
            if left != right:
                raise ValueError("collector refinement expects terminal parent cells")
            choices.append(range(left * ratio, (left + 1) * ratio))
        for child in itertools.product(*choices):
            result.add(tuple((index, index) for index in child))
    expected = len(cells) * (ratio ** Q)
    if len(result) != expected:
        raise RuntimeError(
            f"refined-box tiling mismatch: got {len(result)}, expected {expected}"
        )
    return sorted(result)


def cell_record(item):
    box, lower = item
    return {
        "box": [[int(left), int(right)] for left, right in box],
        "lower": float(lower),
    }


def save_stage(path: str, grid: int, report, unresolved) -> None:
    payload = {
        "grid": grid,
        "target": str(crystal_design.TARGET),
        "verified": bool(report.verified),
        "nodes": int(report.nodes),
        "pruned": int(report.pruned),
        "splits": int(report.splits),
        "maximum_depth": int(report.maximum_depth),
        "initial_boxes": int(report.initial_boxes),
        "elapsed_seconds": float(report.elapsed_seconds),
        "details": report.details,
        "unresolved": [cell_record(item) for item in unresolved],
    }
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def print_report(label: str, report, unresolved) -> None:
    print(label)
    print("verified", report.verified)
    print("target", report.target)
    print("grid", report.grid)
    print("nodes", report.nodes)
    print("pruned", report.pruned)
    print("splits", report.splits)
    print("maximum_depth", report.maximum_depth)
    print("initial_boxes", report.initial_boxes)
    print("elapsed_seconds", f"{report.elapsed_seconds:.6f}")
    for key in sorted(report.details):
        print(key, report.details[key])
    print("unresolved_terminal_cells", len(unresolved))
    for index, (box, lower) in enumerate(unresolved):
        print(f"unresolved[{index}] box={box} lower={lower:.17g}")


def run_stage(grid: int, initial_boxes=None):
    spec = crystal_design.certificate_spec(grid, True)
    unresolved = []
    report = verify_general(
        spec,
        progress_every=200_000 if initial_boxes is None else 0,
        initial_boxes=initial_boxes,
        collect_unresolved=True,
        unresolved_out=unresolved,
    )
    return report, unresolved


def main() -> int:
    started = time.time()
    print("collector_target", crystal_design.TARGET)
    print("collector_strategy grid250 -> misses@500 -> remaining_misses@1000")

    report250, unresolved250 = run_stage(250)
    print_report("=== GRID 250 EXHAUSTIVE COLLECTOR ===", report250, unresolved250)
    save_stage("grid250-unresolved.json", 250, report250, unresolved250)

    if not unresolved250:
        print("mixed_global_verified True")
        print("global_resolution grid250")
        print("total_wall_seconds", time.time() - started)
        return 0

    boxes500 = refine_boxes(unresolved250, 250, 500)
    print("grid500_refinement_parents", len(unresolved250))
    print("grid500_refinement_children", len(boxes500))
    report500, unresolved500 = run_stage(500, boxes500)
    print_report("=== TARGETED GRID 500 REFINEMENT ===", report500, unresolved500)
    save_stage("grid500-unresolved.json", 500, report500, unresolved500)

    if not unresolved500:
        print("mixed_global_verified True")
        print("global_resolution grid250_plus_targeted_grid500")
        print("total_wall_seconds", time.time() - started)
        return 0

    boxes1000 = refine_boxes(unresolved500, 500, 1000)
    print("grid1000_refinement_parents", len(unresolved500))
    print("grid1000_refinement_children", len(boxes1000))
    report1000, unresolved1000 = run_stage(1000, boxes1000)
    print_report("=== TARGETED GRID 1000 REFINEMENT ===", report1000, unresolved1000)
    save_stage("grid1000-unresolved.json", 1000, report1000, unresolved1000)

    complete = not unresolved1000
    print("mixed_global_verified", complete)
    print(
        "global_resolution",
        "grid250_plus_targeted_grid500_grid1000" if complete else "still_unresolved",
    )
    print("total_wall_seconds", time.time() - started)
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
