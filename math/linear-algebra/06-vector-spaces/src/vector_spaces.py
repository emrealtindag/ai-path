import numpy as np


def verify_subspaces():
    # test subspace w1: x1 == 0 (closed under addition and scaling)
    w1_a = np.array([0.0, 2.0, -1.0])
    w1_b = np.array([0.0, -3.0, 4.0])
    c = 2.5

    # check closure under addition and scalar multiplication
    assert (w1_a + w1_b)[0] == 0.0
    assert (c * w1_a)[0] == 0.0

    # counterexample w2: x1 + x2 == 2 (affine plane, not passing through origin)
    w2_a = np.array([1.0, 1.0, 5.0])   # 1 + 1 == 2
    w2_b = np.array([0.0, 2.0, -3.0])  # 0 + 2 == 2
    w2_sum = w2_a + w2_b              # sum has x1 + x2 == 4 != 2
    assert (w2_sum[0] + w2_sum[1]) != 2.0

    print("subspace closure tests:")
    print("  w1 (x1 == 0) is closed under addition and scaling -> valid subspace")
    print("  w2 (x1 + x2 == 2) fails addition closure (sum = 4 != 2) -> not a subspace\n")


def verify_linear_independence():
    # independent set in r2: v1 = (1, 1), v2 = (2, -3)
    A_indep = np.array([[1.0, 2.0], 
                        [1.0, -3.0]])
    rank_indep = np.linalg.matrix_rank(A_indep)
    det_indep = np.linalg.det(A_indep)
    assert rank_indep == 2
    assert not np.isclose(det_indep, 0.0)

    # dependent set in r2: v1 = (1, 3), v2 = (2, 6)
    A_dep = np.array([[1.0, 2.0], 
                      [3.0, 6.0]])
    rank_dep = np.linalg.matrix_rank(A_dep)
    det_dep = np.linalg.det(A_dep)
    assert rank_dep == 1
    assert np.isclose(det_dep, 0.0)

    # 3d independent set from notes: (1, 1, 0), (0, 1, 0), (1, 0, 1)
    A_3d = np.array([[1.0, 0.0, 1.0], 
                     [1.0, 1.0, 0.0], 
                     [0.0, 0.0, 1.0]])
    assert np.isclose(np.linalg.det(A_3d), 1.0)
    assert np.linalg.matrix_rank(A_3d) == 3

    print("linear independence tests:")
    print(f"  independent set rank = {rank_indep}, det = {det_indep:.4f} -> linearly independent")
    print(f"  dependent set rank = {rank_dep}, det = {det_dep:.4f} -> linearly dependent")
    print(f"  3d set det = {np.linalg.det(A_3d):.4f}, rank = 3 -> linearly independent\n")


def verify_span():
    # spanning set in r2: s1 = {(1, 2), (-1, 1)} -> rank 2 spans r2
    S1 = np.array([[1.0, -1.0], 
                   [2.0, 1.0]])
    rank_S1 = np.linalg.matrix_rank(S1)
    assert rank_S1 == 2

    # non-spanning set in r2: s2 = {(2, 4), (-1, -2)} -> rank 1 cannot span r2
    S2 = np.array([[2.0, -1.0], 
                   [4.0, -2.0]])
    rank_S2 = np.linalg.matrix_rank(S2)
    assert rank_S2 == 1

    print("spanning tests:")
    print(f"  set s1 rank = {rank_S1} == 2 -> spans r2")
    print(f"  set s2 rank = {rank_S2} < 2 -> fails to span r2\n")


def verify_basis_and_dimension():
    # basis in r2: s = {[1, 2], [3, 4]}
    B = np.array([[1.0, 3.0], 
                  [2.0, 4.0]])
    det_B = np.linalg.det(B)
    dim_B = np.linalg.matrix_rank(B)
    assert not np.isclose(det_B, 0.0)
    assert dim_B == 2

    print("basis and dimension tests:")
    print(f"  basis matrix det = {det_B:.4f} != 0, rank = {dim_B}")
    print(f"  vectors form a valid basis with dimension = {dim_B}\n")


def verify_coordinate_vectors():
    # 1. r2 coordinate vector: basis s = {[1, 3], [2, 1]}, target v = [2, 3]
    P2 = np.array([[1.0, 2.0], 
                   [3.0, 1.0]])
    v2 = np.array([2.0, 3.0])
    coords_v2 = np.linalg.solve(P2, v2)
    assert np.allclose(coords_v2, [4.0 / 5.0, 3.0 / 5.0])
    assert np.allclose(P2 @ coords_v2, v2)

    # 2. r3 coordinate vector: basis s = {[1, 2, 1], [2, 9, 0], [3, 3, 4]}, target v = [5, -1, 9]
    P3 = np.array([[1.0, 2.0, 3.0], 
                   [2.0, 9.0, 3.0], 
                   [1.0, 0.0, 4.0]])
    v3 = np.array([5.0, -1.0, 9.0])
    coords_v3 = np.linalg.solve(P3, v3)
    assert np.allclose(coords_v3, [1.0, -1.0, 2.0])
    assert np.allclose(P3 @ coords_v3, v3)

    # forward reconstruction from coordinates [-1, 3, 2]
    coords_forward = np.array([-1.0, 3.0, 2.0])
    v3_synthesized = P3 @ coords_forward
    assert np.allclose(v3_synthesized, [11.0, 31.0, 7.0])

    print("coordinate vector tests:")
    print(f"  r2 coordinates [v]_S: {coords_v2} -> reconstructed: {P2 @ coords_v2}")
    print(f"  r3 coordinates [v]_S: {coords_v3} -> reconstructed: {P3 @ coords_v3}")
    print(f"  forward synthesis from [-1, 3, 2]: {v3_synthesized}")
    print("  all coordinate mappings hold")


if __name__ == "__main__":
    verify_subspaces()
    verify_linear_independence()
    verify_span()
    verify_basis_and_dimension()
    verify_coordinate_vectors()
