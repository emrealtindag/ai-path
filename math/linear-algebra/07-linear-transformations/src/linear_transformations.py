import numpy as np
from scipy.linalg import null_space

# ---------------------------------------------------------
# 1. linearity conditions (page 1 & 2)
#    T(u + v) = T(u) + T(v)  and  T(c * u) = c * T(u)
# ---------------------------------------------------------
u = np.array([2.0, -1.0])
v = np.array([-3.0, 4.0])
c = 3.0


def T1(vec):
    x, y = vec
    return np.array([x + y, 2 * x - y, y])


def T2(vec):
    x, y = vec
    return np.array([x * y, x - y])


# check T1 (linear)
t1_cond1 = np.allclose(T1(u + v), T1(u) + T1(v))
t1_cond2 = np.allclose(T1(c * u), c * T1(u))
print("T1 is linear:", t1_cond1 and t1_cond2)

# check T2 (not linear)
t2_cond1 = np.allclose(T2(u + v), T2(u) + T2(v))
t2_cond2 = np.allclose(T2(c * u), c * T2(u))
print("T2 is linear:", t2_cond1 and t2_cond2)


# ---------------------------------------------------------
# 2. linear transformation matrix: T(u) = A @ u (page 2)
#    T(x, y) = (2x + y, y, x - 3y)
# ---------------------------------------------------------
def T_example(vec):
    x, y = vec
    return np.array([2 * x + y, y, x - 3 * y])


A = np.array([
    [2.0, 1.0],
    [0.0, 1.0],
    [1.0, -3.0]
])

func_out = T_example(u)
mat_out = A @ u

print("function output:", func_out)
print("matrix output:  ", mat_out)
print("T(u) == A @ u:  ", np.allclose(func_out, mat_out))


# ---------------------------------------------------------
# 3. kernel / null space: T(u) = 0 (page 3)
# ---------------------------------------------------------
# example a: L(x, y) = (2x - y, 3x + y) -> kernel = {(0, 0)}
L = np.array([
    [2.0, -1.0],
    [3.0, 1.0]
])
ker_L = null_space(L)
print("L nullity:", ker_L.shape[1])

# example b: T(x, y, z) = (x, y, 0) -> kernel = {(0, 0, z)}
P = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0]
])
ker_P = null_space(P)
print("P nullity:", ker_P.shape[1])
print("P kernel basis:", np.round(ker_P.ravel(), 2))


# ---------------------------------------------------------
# 4. range, rank, nullity & rank-nullity theorem (page 4)
#    T(x, y, z) = (x + y, y + z),  T: R^3 -> R^2
# ---------------------------------------------------------
M = np.array([
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 1.0]
])

rank_M = np.linalg.matrix_rank(M)
ker_M = null_space(M)
nullity_M = ker_M.shape[1]
domain_dim = M.shape[1]

# scale kernel vector so first entry is 1 -> [1, -1, 1]
ker_basis = ker_M.ravel() / ker_M.ravel()[0]

print("rank:", rank_M)
print("nullity:", nullity_M)
print("rank + nullity == domain dim:", rank_M + nullity_M == domain_dim)
print("kernel basis:", np.round(ker_basis, 2))
print("M @ kernel == 0:", np.allclose(M @ ker_basis, 0.0))
