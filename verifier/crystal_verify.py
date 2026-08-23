"""Run the crystalline seven-point checks and interval certificate."""

import argparse, sys, time
from flint import arb, ctx
from zeta_ext import crystal_design
from zeta_ext.h0_cert import (
    window_functional, window_min_enclosure, window_monotone_factor_upper,
)
from zeta_ext.parallel import verify_parallel
from zeta_ext.verify_general import verify_general

def fast():
    ctx.prec = 256
    ok = True
    low = window_min_enclosure(crystal_design.KERNEL, 8192)
    good = bool(low >= arb(crystal_design.WINDOW_MIN)); ok &= good
    print("min_v", low, good)
    mono = window_monotone_factor_upper(crystal_design.KERNEL, 8192)
    good = bool(mono <= 0); ok &= good
    print("max_vprime_over_s", mono, good)
    c1, h = window_functional(crystal_design.KERNEL)
    good = bool(h >= arb(crystal_design.H_CERT)); ok &= good
    print("c1", c1); print("H", h, good)
    bound, A, phi = crystal_design.refined_final_bound()
    good = bool(bound >= arb(crystal_design.FINAL_BOUND_RATIONAL)); ok &= good
    print("A", A); print("Phi", phi); print("bound", bound, good)
    print("fast_parts_verified", ok)
    return 0 if ok else 1

def main(grid, workers, no_tangent):
    spec = crystal_design.certificate_spec(grid, not no_tangent)
    started = time.time()
    report = (
        verify_parallel(spec, workers=workers) if workers > 1
        else verify_general(spec, progress_every=200_000)
    )
    print("\n".join(report.lines()))
    print("wall_seconds", time.time() - started)
    return 0 if report.verified else 1

def entry():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["fast","main","all"])
    p.add_argument("--grid", type=int, default=4000)
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--no-tangent", action="store_true")
    a = p.parse_args()
    if a.command == "fast": return fast()
    if a.command == "main": return main(a.grid,a.workers,a.no_tangent)
    return fast() or main(a.grid,a.workers,a.no_tangent)

if __name__ == "__main__":
    sys.exit(entry())
