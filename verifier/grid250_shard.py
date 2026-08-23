"""Run one disjoint shard of the rigorous grid-250 terminal-cell collector."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from zeta_ext import crystal_design
from zeta_ext.verify_general import verify_general


def cell_record(item):
    box, lower = item
    return {
        "box": [[int(left), int(right)] for left, right in box],
        "lower": float(lower),
    }


def main(shard: int, shard_count: int) -> int:
    if shard_count <= 0:
        raise ValueError("shard_count must be positive")
    if shard < 0 or shard >= shard_count:
        raise ValueError("shard must satisfy 0 <= shard < shard_count")

    spec = crystal_design.certificate_spec(250, True)
    unresolved = []
    report = verify_general(
        spec,
        progress_every=200_000,
        shard=shard,
        shard_count=shard_count,
        collect_unresolved=True,
        unresolved_out=unresolved,
    )

    payload = {
        "grid": 250,
        "target": str(crystal_design.TARGET),
        "shard": shard,
        "shard_count": shard_count,
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
    out = Path(f"grid250-shard-{shard}.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print("grid250_shard", shard)
    print("grid250_shard_count", shard_count)
    print("target", crystal_design.TARGET)
    print("verified_within_shard", report.verified)
    print("nodes", report.nodes)
    print("pruned", report.pruned)
    print("splits", report.splits)
    print("initial_boxes", report.initial_boxes)
    for key in sorted(report.details):
        print(key, report.details[key])
    print("unresolved_terminal_cells", len(unresolved))
    for index, (box, lower) in enumerate(unresolved):
        print(f"unresolved[{index}] box={box} lower={lower:.17g}")

    # An unresolved terminal cell is data for the merge/refinement stage, not a
    # shard failure. Any actual verifier/runtime failure still raises and fails CI.
    return 0


def entry() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard", type=int, required=True)
    parser.add_argument("--shard-count", type=int, required=True)
    args = parser.parse_args()
    return main(args.shard, args.shard_count)


if __name__ == "__main__":
    sys.exit(entry())
