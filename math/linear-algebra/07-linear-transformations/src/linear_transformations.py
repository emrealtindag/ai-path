import numpy as np
from scipy.linalg import null_space


def check_linearity(T, u, v, c=3.5):
    additivity = np.allclose(T(u + v), T(u) + T(v))
    homogeneity = np.allclose(T(c * u), c * T(u))
    return additivity and homogeneity, additivity, homogeneity


def main():
    print("=== 1. linearity tests ===")
    u2 = np.array([2.0, -1.0])
    v2 = np.array([-3.0, 4.0])
    u3 = np.array([1.0, -2.0, 3.0])
    v3 = np.array([2.0, 5.0, -1.0])

    # T1(x, y) = (x + y, 2x - y, y)
    T1 = lambda p: np.array([p[0] + p[1], 2 * p[0] - p[1], p[1]])
    # T2(x, y) = (x*y, x - y)
    T2 = lambda p: np.array([p[0] * p[1], p[0] - p[1]])
    # T3(x, y, z) = (x + y + 2z, x^2 + y^2)
    T3 = lambda p: np.array([p[0] + p[1] + 2 * p[2], p[0] ** 2 + p[1] ** 2])
    # T4(x, y, z) = (3x, 2y, x + y + z)
    T4 = lambda p: np.array([3 * p[0], 2 * p[1], p[0] + p[1] + p[2]])

    print("T1(x,y) = (x+y, 2x-y, y) linear:", check_linearity(T1, u2, v2)[0])
    print("T2(x,y) = (x*y, x-y) linear:", check_linearity(T2, u2, v2)[0])
    print("T3(x,y,z) = (x+y+2z, x^2+y^2) linear:", check_linearity(T3, u3, v3)[0])
    print("T4(x,y,z) = (3x, 2y, x+y+z) linear:", check_linearity(T4, u3, v3)[0])

    print("\n=== 2. linear transformation matrix T(u) = A @ u ===")
    A_3x2 = np.array([[2.0, 1.0],
                      [0.0, 1.0],
                      [1.0, -3.0]])
    T_direct = lambda p: np.array([2 * p[0] + p[1], p[1], p[0] - 3 * p[1]])
    print("T(u) == A @ u holds:", np.allclose(T_direct(u2), A_3x2 @ u2))
    print("A @ [2, -1]:", A_3x2 @ u2)

    A_4x2 = np.array([[2.0, 1.0],
                      [3.0, 0.0],
                      [4.0, 2.0],
                      [5.0, 3.0]])
    print("A_4x2 @ [2, -1]:", A_4x2 @ u2)

    print("\n=== 3. kernel (null space) ===")
    L = np.array([[2.0, -1.0],
                  [3.0, 1.0]])
    ker_L = null_space(L)
    print("L(x,y) = (2x-y, 3x+y) nullity:", ker_L.shape[1])

    P_xy = np.array([[1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0],
                     [0.0, 0.0, 0.0]])
    ker_P = null_space(P_xy)
    print("T(x,y,z) = (x, y, 0) nullity:", ker_P.shape[1])
    print("kernel basis vector (z-axis):", np.round(ker_P.ravel(), 3))

    print("\n=== 4. range (column space), rank, nullity & rank-nullity theorem ===")
    A_r2_r3 = np.array([[1.0, 2.0],
                        [1.0, -3.0],
                        [2.0, 1.0]])
    r1 = np.linalg.matrix_rank(A_r2_r3)
    n1 = A_r2_r3.shape[1] - r1
    print(f"T: R2 -> R3 | rank: {r1}, nullity: {n1}, rank + nullity = {r1 + n1} (domain dim: {A_r2_r3.shape[1]})")

    A_r3_r4 = np.array([[1.0, 2.0, 0.0],
                        [0.0, 1.0, -1.0],
                        [0.0, 0.0, 1.0],
                        [3.0, 1.0, 0.0]])
    r2 = np.linalg.matrix_rank(A_r3_r4)
    n2 = A_r3_r4.shape[1] - r2
    print(f"T: R3 -> R4 | rank: {r2}, nullity: {n2}, rank + nullity = {r2 + n2} (domain dim: {A_r3_r4.shape[1]})")

    # T(x, y, z) = (x + y, y + z)
    A_r3_r2 = np.array([[1.0, 1.0, 0.0],
                        [0.0, 1.0, 1.0]])
    r3 = np.linalg.matrix_rank(A_r3_r2)
    ker_r3_r2 = null_space(A_r3_r2)
    n3 = ker_r3_r2.shape[1]
    # normalize kernel basis so first entry is 1 -> [1, -1, 1]
    ker_scaled = ker_r3_r2.ravel() / ker_r3_r2.ravel()[0]
    print(f"T(x,y,z) = (x+y, y+z) | rank: {r3}, nullity: {n3}, rank + nullity = {r3 + n3} (domain dim: {A_r3_r2.shape[1]})")
    print("kernel basis (scaled):", np.round(ker_scaled, 3))
    print("A @ ker == 0 holds:", np.allclose(A_r3_r2 @ ker_scaled, 0.0))


if __name__ == "__main__":
    main()
