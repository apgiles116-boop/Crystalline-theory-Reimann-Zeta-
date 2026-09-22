using JuMP
using Ipopt
using LinearAlgebra
using Printf
import MathOptInterface as MOI

# Type E: deterministic two-sided safe-triangle scan.
# Numerical reconnaissance only; not a proof certificate.

const AMAX = 1.0 / 4.0
const EPS_TARGET = 0.04795128168835
const FEAS_TOL = 5.0e-8
const RHOS = (0.50, 0.25, 0.00, -0.25, -0.45)

const GOOD_STATUS = (
    MOI.LOCALLY_SOLVED,
    MOI.ALMOST_LOCALLY_SOLVED,
    MOI.OPTIMAL,
    MOI.ALMOST_OPTIMAL,
)

function geometric_start(a::NTuple{3,Float64}, rho::Float64)
    G = [1.0 rho rho; rho 1.0 rho; rho rho 1.0]
    L = Matrix(cholesky(Symmetric(G)).L)
    Zd = zeros(5,3)
    Zd[1:3,:] .= transpose(L)
    Md = zeros(5,3)
    th = (0.0, 2pi/3, 4pi/3)
    for i in 1:3
        Md[4,i] = cos(th[i])
        Md[5,i] = sin(th[i])
    end
    P = zeros(5,3); N = zeros(5,3)
    for i in 1:3
        m = sqrt(a[i]) .* Md[:,i]
        z = sqrt(1-a[i]) .* Zd[:,i]
        P[:,i] .= m + z
        N[:,i] .= m - z
    end
    return P,N
end

function orthogonal_unit(z)
    zh = z / norm(z)
    best = zeros(5); bn = -1.0
    for k in 1:5
        e = zeros(5); e[k] = 1.0
        v = e - dot(e,zh)*zh
        if norm(v) > bn
            bn = norm(v); best .= v
        end
    end
    return best / norm(best)
end

function retarget(Pold,Nold,a::NTuple{3,Float64})
    P = zeros(5,3); N = zeros(5,3)
    for i in 1:3
        m0 = (Pold[:,i] + Nold[:,i]) / 2
        z0 = (Pold[:,i] - Nold[:,i]) / 2
        zh = z0 / norm(z0)
        if norm(m0) > 1e-10
            mh = m0 / norm(m0)
            mh -= dot(mh,zh)*zh
            mh = norm(mh) > 1e-10 ? mh/norm(mh) : orthogonal_unit(zh)
        else
            mh = orthogonal_unit(zh)
        end
        m = sqrt(a[i]) .* mh
        z = sqrt(1-a[i]) .* zh
        P[:,i] .= m + z
        N[:,i] .= m - z
    end
    return P,N
end

function audit(P,N,a)
    unit_res=0.0; deep_res=0.0; orth_res=0.0; amid_res=0.0
    for i in 1:3
        unit_res=max(unit_res,abs(dot(P[:,i],P[:,i])-1),abs(dot(N[:,i],N[:,i])-1))
        deep_res=max(deep_res,abs(dot(P[:,i],N[:,i])-(2a[i]-1)))
        m=(P[:,i]+N[:,i])/2; z=(P[:,i]-N[:,i])/2
        orth_res=max(orth_res,abs(dot(m,z)))
        amid_res=max(amid_res,abs(dot(m,m)-a[i]))
    end
    cross_viol=0.0
    for i in 1:2, j in i+1:3
        vals=(dot(P[:,i],P[:,j]),dot(P[:,i],N[:,j]),dot(N[:,i],P[:,j]),dot(N[:,i],N[:,j]))
        for v in vals
            cross_viol=max(cross_viol,max(abs(v)-0.5,0.0))
        end
    end
    Z=(P-N)/2
    x=dot(Z[:,1],Z[:,2]); y=dot(Z[:,2],Z[:,3]); z=dot(Z[:,3],Z[:,1])
    safe_viol=maximum((max(abs(x)-0.5,0.0),max(abs(y)-0.5,0.0),max(abs(z)-0.5,0.0)))
    F=x^2+y^2+z^2
    maxres=maximum((unit_res,deep_res,orth_res,amid_res,cross_viol,safe_viol))
    return (F=F,loss=0.75-F,x=x,y=y,z=z,unit_res=unit_res,deep_res=deep_res,
            orth_res=orth_res,amid_res=amid_res,cross_viol=cross_viol,
            safe_viol=safe_viol,maxres=maxres)
end

function solve_once(a,P0,N0)
    model=Model(Ipopt.Optimizer)
    set_silent(model)
    set_optimizer_attribute(model,"tol",1e-10)
    set_optimizer_attribute(model,"acceptable_tol",1e-8)
    set_optimizer_attribute(model,"constr_viol_tol",1e-10)
    set_optimizer_attribute(model,"max_iter",2500)
    set_optimizer_attribute(model,"print_level",0)
    @variable(model,-1 <= P[1:5,1:3] <= 1)
    @variable(model,-1 <= N[1:5,1:3] <= 1)
    for i in 1:3
        @NLconstraint(model,sum(P[k,i]^2 for k in 1:5)==1)
        @NLconstraint(model,sum(N[k,i]^2 for k in 1:5)==1)
        @NLconstraint(model,sum(P[k,i]*N[k,i] for k in 1:5)==2a[i]-1)
    end
    for i in 1:2, j in i+1:3
        @NLconstraint(model,-0.5 <= sum(P[k,i]*P[k,j] for k in 1:5) <= 0.5)
        @NLconstraint(model,-0.5 <= sum(P[k,i]*N[k,j] for k in 1:5) <= 0.5)
        @NLconstraint(model,-0.5 <= sum(N[k,i]*P[k,j] for k in 1:5) <= 0.5)
        @NLconstraint(model,-0.5 <= sum(N[k,i]*N[k,j] for k in 1:5) <= 0.5)
    end
    x=@NLexpression(model,0.25*sum((P[k,1]-N[k,1])*(P[k,2]-N[k,2]) for k in 1:5))
    y=@NLexpression(model,0.25*sum((P[k,2]-N[k,2])*(P[k,3]-N[k,3]) for k in 1:5))
    z=@NLexpression(model,0.25*sum((P[k,3]-N[k,3])*(P[k,1]-N[k,1]) for k in 1:5))
    @NLconstraint(model,-0.5 <= x <= 0.5)
    @NLconstraint(model,-0.5 <= y <= 0.5)
    @NLconstraint(model,-0.5 <= z <= 0.5)
    @NLobjective(model,Max,x^2+y^2+z^2)
    for i in 1:3, k in 1:5
        set_start_value(P[k,i],P0[k,i]); set_start_value(N[k,i],N0[k,i])
    end
    optimize!(model)
    status=termination_status(model)
    status in GOOD_STATUS || return nothing
    Pv=value.(P); Nv=value.(N); au=audit(Pv,Nv,a)
    return (P=Pv,N=Nv,audit=au,status=status)
end

function solve_point(a; previous=nothing)
    starts=Tuple{Matrix{Float64},Matrix{Float64},String}[]
    if previous !== nothing
        P0,N0=retarget(previous.P,previous.N,a); push!(starts,(P0,N0,"warm"))
    end
    for rho in RHOS
        P0,N0=geometric_start(a,rho)
        push!(starts,(P0,N0,@sprintf("r%+.2f",rho)))
    end
    best=nothing
    for (P0,N0,name) in starts
        r=solve_once(a,P0,N0); r===nothing && continue
        r.audit.maxres > FEAS_TOL && continue
        if best===nothing || r.audit.F > best.audit.F + 1e-12
            best=(P=r.P,N=r.N,audit=r.audit,status=r.status,start=name)
        end
    end
    return best
end

function diagnostics(label,result)
    println("\n================================================================")
    println(" DIAGNOSTIC: ",label)
    println("================================================================")
    P=result.P; N=result.N; M=(P+N)/2; Z=(P-N)/2
    for (i,j) in ((1,2),(2,3),(3,1))
        u=dot(M[:,i],M[:,j]); p=dot(M[:,i],Z[:,j])
        q=dot(Z[:,i],M[:,j]); r=dot(Z[:,i],Z[:,j])
        epp=dot(P[:,i],P[:,j]); epn=dot(P[:,i],N[:,j])
        enp=dot(N[:,i],P[:,j]); enn=dot(N[:,i],N[:,j])
        @printf("pair %d%d: u=%+.12f p=%+.12f q=%+.12f r=%+.12f\n",i,j,u,p,q,r)
        @printf("         endpoint = [%+.12f %+.12f %+.12f %+.12f]\n",epp,epn,enp,enn)
    end
    V=hcat(M[:,1],Z[:,1],M[:,2],Z[:,2],M[:,3],Z[:,3])
    lam=sort(eigvals(Symmetric(transpose(V)*V)))
    println("Gram6 eigenvalues:")
    @printf("  %.12e %.12e %.12e %.12e %.12e %.12e\n",lam...)
    println("max feasibility residual = ",result.audit.maxres)
end

tests=[
    ("S000",(0.0,0.0,0.0)),
    ("S050",(0.05,0.05,0.05)),
    ("HHL504",(0.25,0.25,5.0/504.0)),
    ("HLL050",(0.25,0.05,0.05)),
    ("S250",(0.25,0.25,0.25)),
]

previous=nothing
println("case      a1      a2      a3        Fmax        loss    loss-eps     maxres     start")
for (label,a) in tests
    r=solve_point(a;previous=previous)
    if r===nothing
        @printf("%-7s NO ACCEPTED SOLUTION\n",label)
        continue
    end
    previous=r
    au=r.audit
    @printf("%-7s %7.4f %7.4f %7.4f %11.8f %11.8f %+11.8f %10.2e %9s\n",
            label,a...,au.F,au.loss,au.loss-EPS_TARGET,au.maxres,r.start)
    if label=="HHL504" || label=="HLL050"
        diagnostics(label,r)
    end
end
