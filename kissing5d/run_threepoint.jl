using Pkg
using Downloads

Pkg.add("ClusteredLowRankSolver")
Pkg.add("Nemo")

using ClusteredLowRankSolver
using Nemo

src = Downloads.download("https://raw.githubusercontent.com/nanleij/ClusteredLowRankSolver.jl/main/examples/ThreePointBound.jl")
include(src)
using .ThreePointBound

n = 5
costheta = 1//2
d = length(ARGS) >= 1 ? parse(Int, ARGS[1]) : 4

println("BEGIN n=$n costheta=$costheta d=$d")
problem, dualsol, primalsol = three_point_spherical_codes(
    n, costheta, d, d;
    prec=256,
    duality_gap_threshold=1e-18,
    omega_d=10^3,
    omega_p=10^3,
)
println("PRIMAL d=$d value=", objvalue(problem, primalsol))
println("DUAL d=$d value=", dualobjvalue(problem, dualsol))
println("END d=$d")
