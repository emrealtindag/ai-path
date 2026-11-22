import numpy as np
import scipy.linalg


def verify_subspaces():
    # test subspace w1: x1 == 0 (closed under addition and scaling)
    w1_a = np.array([0.0, 2.0, -1.0])
    w1_b = np.array([0.0, -3.0, 4.0])
    c = 2.5

    # check closure under addition and scalar multiplication
    assert (w1_a + w1_b)[0] == 0.0
    assert (c * w1_a)[0] == 0.0

    # counterexample w2: x1 + x2 == 2 (fails closure under addition)
    w2_a = np.array([1.0, 1.0, 5.0])
    w2_b = np.array([0.0, 2.0, -3.0])
    w2_sum = w2_a + w2_b
    assert (w2_sum[0] + w2_sum[1]) != 2.0

    print("subspace closure tests:")
    print("  w1 (x1 == 0) is closed under addition and scaling -> valid subspace")
    print("  w2 (x1 + x2 == 2) fails addition closure (sum = 4 != 2) -> not a subspace\n")


def verify_linear_independence():
    # independent set in r2: rank == 2, det != 0
    A_indep = np.array([[1.0, 2.0], 
                        [1.0, -3.0]])
    rank_indep = np.linalg.matrix_rank(A_indep)
    det_indep = np.linalg.det(A_indep)
    assert rank_indep == 2
    assert not np.isclose(det_indep, 0.0)

    # dependent set in r2: rank == 1, det == 0
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
    # spanning set in r2: full rank spans r2
    S1 = np.array([[1.0, -1.0], 
                   [2.0, 1.0]])
    rank_S1 = np.linalg.matrix_rank(S1)
    assert rank_S1 == 2

    # non-spanning set in r2: rank 1 cannot span r2
    S2 = np.array([[2.0, -1.0], 
                   [4.0, -2.0]])
    rank_S2 = np.linalg.matrix_rank(S2)
    assert rank_S2 == 1

    print("spanning tests:")
    print(f"  set s1 rank = {rank_S1} == 2 -> spans r2")
    print(f"  set s2 rank = {rank_S2} < 2 -> fails to span r2\n")


def verify_basis_and_dimension():
    # basis in r2: s = {[1, 2], [3, 4]} -> det != 0, rank == 2
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

    # forward synthesis from coordinates [-1, 3, 2]
    coords_forward = np.array([-1.0, 3.0, 2.0])
    v3_synthesized = P3 @ coords_forward
    assert np.allclose(v3_synthesized, [11.0, 31.0, 7.0])

    print("coordinate vector tests:")
    print(f"  r2 coordinates [v]_S: {coords_v2} -> reconstructed: {P2 @ coords_v2}")
    print(f"  r3 coordinates [v]_S: {coords_v3} -> reconstructed: {P3 @ coords_v3}")
    print(f"  forward synthesis from [-1, 3, 2]: {v3_synthesized}")
    print("  all coordinate mappings hold\n")


def verify_change_of_basis():
    # example from page 12: standard basis B and new basis B' = {[3, 1], [-2, 1]}
    P = np.array([[3.0, -2.0], 
                  [1.0, 1.0]])
    P_inv = np.linalg.inv(P)

    # check analytical inverse: 1/5 * [[1, 2], [-1, 3]]
    P_inv_expected = 0.2 * np.array([[1.0, 2.0], 
                                     [-1.0, 3.0]])
    assert np.allclose(P_inv, P_inv_expected)

    # part b: [u]_B = P @ [u]_B' for [u]_B' = [2, 1]
    u_Bprime = np.array([2.0, 1.0])
    u_B = P @ u_Bprime
    assert np.allclose(u_B, [4.0, 3.0])

    # part d: [v]_B' = P^-1 @ [v]_B for [v]_B = [1, 3]
    v_B = np.array([1.0, 3.0])
    v_Bprime = P_inv @ v_B
    assert np.allclose(v_Bprime, [7.0 / 5.0, 8.0 / 5.0])

    # example from page 13: transition matrix from basis A to basis B
    M_A = np.array([[2.0, 1.0], 
                    [1.0, 4.0]])
    M_B = np.array([[3.0, -2.0], 
                    [1.0, 1.0]])
    P_A_to_B = np.linalg.inv(M_B) @ M_A
    assert np.allclose(P_A_to_B, [[0.8, 1.8], [0.2, 2.2]])

    print("change of basis tests:")
    print(f"  transition matrix P (B' -> B):\n{P}")
    print(f"  coordinate mapping [u]_B = P @ [u]_B': {u_B}")
    print(f"  inverse mapping [v]_B' = P^-1 @ [v]_B: {v_Bprime}")
    print(f"  transition matrix between two non-standard bases (A -> B):\n{P_A_to_B}")
    print("  change of basis properties hold\n")


def verify_row_and_column_spaces():
    # 1. row space example from page 13 (4x5 matrix)
    A_row = np.array([[1.0, -2.0, 0.0, 0.0, 3.0], 
                      [2.0, -5.0, -3.0, -2.0, 6.0], 
                      [0.0, 5.0, 15.0, 10.0, 0.0], 
                      [2.0, 6.0, 18.0, 8.0, 6.0]])
    rank_row = np.linalg.matrix_rank(A_row)
    assert rank_row == 3

    # 2. column space example from page 14 (3x5 matrix)
    A_col = np.array([[2.0, 4.0, 6.0, -2.0, 0.0], 
                      [3.0, 1.0, -2.0, 4.0, 5.0], 
                      [6.0, 2.0, -4.0, 8.0, 10.0]])
    rank_col = np.linalg.matrix_rank(A_col)
    assert rank_col == 2

    # check pivot columns in column space
    col_basis = A_col[:, :2]
    assert np.linalg.matrix_rank(col_basis) == 2

    print("row and column space tests:")
    print(f"  row space matrix rank = {rank_row} -> dimension of row space = {rank_row}")
    print(f"  column space matrix rank = {rank_col} -> dimension of column space = {rank_col}")
    print("  pivot columns form a linearly independent basis for column space\n")


def verify_nullspace_and_rank_nullity():
    # null space example from page 15 (4x6 matrix, Ax == 0)
    A = np.array([[-1.0, 2.0, 0.0, 4.0, 5.0, -3.0], 
                  [3.0, -7.0, 2.0, 0.0, 1.0, 4.0], 
                  [2.0, -5.0, 2.0, 4.0, 6.0, 1.0], 
                  [4.0, -9.0, 2.0, -4.0, -4.0, 7.0]])
    
    n_cols = A.shape[1]
    rank_A = np.linalg.matrix_rank(A)
    nullity_A = n_cols - rank_A

    assert rank_A == 2
    assert nullity_A == 4
    # rank-nullity theorem verification
    assert rank_A + nullity_A == n_cols

    # compute numerical orthonormal basis for null space using svd/null_space
    null_basis = scipy.linalg.null_space(A)
    assert null_basis.shape == (6, 4)
    # verify A @ v_null == 0 for all null space basis vectors
    assert np.allclose(A @ null_basis, np.zeros((4, 4)))

    print("null space and rank-nullity theorem tests:")
    print(f"  matrix shape: {A.shape} (rows x columns)")
    print(f"  rank = {rank_A} (number of pivot columns)")
    print(f"  nullity = {nullity_A} (number of free variables)")
    print(f"  rank + nullity = {rank_A} + {nullity_A} = {n_cols} (number of columns)")
    print("  all null space basis vectors satisfy A @ v == 0")


if __name__ == "__main__":
    verify_subspaces()
    verify_linear_independence()
    verify_span()
    verify_basis_and_dimension()
    verify_coordinate_vectors()
    verify_change_of_basis()
    verify_row_and_column_spaces()
    verify_nullspace_and_rank_nullity()
