"""Merge rigorous grid-250 shard results and refine every terminal miss."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from zeta_ext import crystal_design

from grid250_collect_and_refine import refine_boxes, run_stage, save_stage, print_report


def load_shards(shards_dir: Path, shard_count: int):
    paths = sorted(shards_dir.glob("grid250-shard-*.json"))
    if len(paths) != shard_count:
        raise RuntimeError(
            f"expected {shard_count} shard files, found {len(paths)} in {shards_dir}"
        )

    payloads = [json.loads(path.read_text()) for path in paths]
    by_shard = {}
    for payload in payloads:
        if payload.get("grid") != 250:
            raise RuntimeError("unexpected shard grid")
        if payload.get("target") != str(crystal_design.TARGET):
            raise RuntimeError("shard target mismatch")
        if int(payload.get("shard_count")) != shard_count:
            raise RuntimeError("shard-count mismatch")
        shard = int(payload.get("shard"))
        if shard in by_shard:
            raise RuntimeError(f"duplicate shard {shard}")
        by_shard[shard] = payload

    if set(by_shard) != set(range(shard_count)):
        raise RuntimeError(
            f"incomplete shard set: got {sorted(by_shard)}, expected 0..{shard_count - 1}"
        )

    # All shards must have been built from exactly the same lower-bound tables.
    w_hashes = {p["details"].get("w_table_sha256") for p in by_shard.values()}
    w2_hashes = {p["details"].get("w_second_table_sha256") for p in by_shard.values()}
    if len(w_hashes) != 1 or None in w_hashes:
        raise RuntimeError(f"w-table hash mismatch across shards: {sorted(w_hashes)}")
    if len(w2_hashes) != 1 or None in w2_hashes:
        raise RuntimeError(f"w-second-table hash mismatch across shards: {sorted(w2_hashes)}")

    unresolved = []
    seen_boxes = set()
    for shard in range(shard_count):
        payload = by_shard[shard]
        for record in payload.get("unresolved", []):
            box = tuple((int(left), int(right)) for left, right in record["box"])
            if box in seen_boxes:
                raise RuntimeError(f"duplicate unresolved box across shards: {box}")
            seen_boxes.add(box)
            unresolved.append((box, float(record["lower"])))

    summary = {
        "grid": 250,
        "target": str(crystal_design.TARGET),
        "shard_count": shard_count,
        "shards": [by_shard[i] for i in range(shard_count)],
        "initial_boxes_total": sum(int(by_shard[i]["initial_boxes"]) for i in range(shard_count)),
        "nodes_total": sum(int(by_shard[i]["nodes"]) for i in range(shard_count)),
        "pruned_total": sum(int(by_shard[i]["pruned"]) for i in range(shard_count)),
        "splits_total": sum(int(by_shard[i]["splits"]) for i in range(shard_count)),
        "unresolved_terminal_cells": len(unresolved),
        "w_table_sha256": next(iter(w_hashes)),
        "w_second_table_sha256": next(iter(w2_hashes)),
    }
    Path("grid250-sharded-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    return unresolved, summary


def main(shards_dir: str, shard_count: int) -> int:
    started = time.time()
    unresolved250, summary = load_shards(Path(shards_dir), shard_count)

    print("=== GRID 250 SHARDED EXHAUSTIVE COLLECTOR ===")
    print("target", crystal_design.TARGET)
    print("shard_count", shard_count)
    print("initial_boxes_total", summary["initial_boxes_total"])
    print("nodes_total", summary["nodes_total"])
    print("pruned_total", summary["pruned_total"])
    print("splits_total", summary["splits_total"])
    print("w_table_sha256", summary["w_table_sha256"])
    print("w_second_table_sha256", summary["w_second_table_sha256"])
    print("unresolved_terminal_cells", len(unresolved250))
    for index, (box, lower) in enumerate(unresolved250):
        print(f"unresolved250[{index}] box={box} lower={lower:.17g}")

    if not unresolved250:
        print("mixed_global_verified True")
        print("global_resolution sharded_grid250")
        print("total_wall_seconds", time.time() - started)
        return 0

    boxes500 = refine_boxes(unresolved250, 250, 500)
    print("grid500_refinement_parents", len(unresolved250))
    print("grid500_refinement_children", len(boxes500))
    report500, unresolved500 = run_stage(500, boxes500)
    print_report("=== TARGETED GRID 500 REFINEMENT ===", report500, unresolved500)
    save_stage("grid500-sharded-unresolved.json", 500, report500, unresolved500)

    if not unresolved500:
        print("mixed_global_verified True")
        print("global_resolution sharded_grid250_plus_targeted_grid500")
        print("total_wall_seconds", time.time() - started)
        return 0

    boxes1000 = refine_boxes(unresolved500, 500, 1000)
    print("grid1000_refinement_parents", len(unresolved500))
    print("grid1000_refinement_children", len(boxes1000))
    report1000, unresolved1000 = run_stage(1000, boxes1000)
    print_report("=== TARGETED GRID 1000 REFINEMENT ===", report1000, unresolved1000)
    save_stage("grid1000-sharded-unresolved.json", 1000, report1000, unresolved1000)

    complete = not unresolved1000
    print("mixed_global_verified", complete)
    print(
        "global_resolution",
        "sharded_grid250_plus_targeted_grid500_grid1000"
        if complete
        else "still_unresolved",
    )
    print("total_wall_seconds", time.time() - started)
    return 0 if complete else 1


def entry() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shards-dir", default="shards")
    parser.add_argument("--shard-count", type=int, default=8)
    args = parser.parse_args()
    return main(args.shards_dir, args.shard_count)


if __name__ == "__main__":
    sys.exit(entry())
