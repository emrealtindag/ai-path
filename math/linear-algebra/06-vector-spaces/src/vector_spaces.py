import numpy as np


def verify_linear_independence():
    # test linearly independent vector set: v1 = (1, 1), v2 = (2, -3)
    A_indep = np.array([[1.0, 2.0], 
                        [1.0, -3.0]])
    rank_indep = np.linalg.matrix_rank(A_indep)
    det_indep = np.linalg.det(A_indep)
    assert rank_indep == 2
    assert not np.isclose(det_indep, 0.0)

    # test linearly dependent vector set: v1 = (1, 3), v2 = (2, 6)
    A_dep = np.array([[1.0, 2.0], 
                      [3.0, 6.0]])
    rank_dep = np.linalg.matrix_rank(A_dep)
    det_dep = np.linalg.det(A_dep)
    assert rank_dep == 1
    assert np.isclose(det_dep, 0.0)

    print("linear independence tests:")
    print(f"  independent set rank = {rank_indep}, det = {det_indep:.4f} -> linearly independent")
    print(f"  dependent set rank = {rank_dep}, det = {det_dep:.4f} -> linearly dependent\n")


def verify_coordinate_vector_r2():
    # basis vectors: s = {[1, 3], [2, 1]}
    P2 = np.array([[1.0, 2.0], 
                   [3.0, 1.0]])
    v2 = np.array([2.0, 3.0])

    # solve P2 @ [v]_s == v2
    coords_v2 = np.linalg.solve(P2, v2)
    expected_coords = np.array([4.0 / 5.0, 3.0 / 5.0])
    assert np.allclose(coords_v2, expected_coords)

    # reconstruct original vector
    v2_reconstructed = P2 @ coords_v2
    assert np.allclose(v2, v2_reconstructed)

    print("coordinate vector in r2:")
    print(f"  basis coordinates [v]_S: {coords_v2}")
    print(f"  reconstructed vector: {v2_reconstructed}")
    print("  coordinate mapping holds\n")


def verify_coordinate_vector_r3():
    # basis vectors: s = {[1, 2, 1], [2, 9, 0], [3, 3, 4]}
    P3 = np.array([[1.0, 2.0, 3.0], 
                   [2.0, 9.0, 3.0], 
                   [1.0, 0.0, 4.0]])
    v3 = np.array([5.0, -1.0, 9.0])

    # part a: solve P3 @ [v]_s == v3
    coords_v3 = np.linalg.solve(P3, v3)
    expected_coords_a = np.array([1.0, -1.0, 2.0])
    assert np.allclose(coords_v3, expected_coords_a)

    v3_reconstructed = P3 @ coords_v3
    assert np.allclose(v3, v3_reconstructed)

    # part b: forward synthesis from coordinates [-1, 3, 2]
    coords_b = np.array([-1.0, 3.0, 2.0])
    v3_synthesized = P3 @ coords_b
    expected_synthesized = np.array([11.0, 31.0, 7.0])
    assert np.allclose(v3_synthesized, expected_synthesized)

    print("coordinate vector in r3:")
    print(f"  basis coordinates [v]_S: {coords_v3}")
    print(f"  reconstructed vector: {v3_reconstructed}")
    print(f"  forward synthesis from [-1, 3, 2]: {v3_synthesized}")
    print("  all coordinate transformations hold")


if __name__ == "__main__":
    verify_linear_independence()
    verify_coordinate_vector_r2()
    verify_coordinate_vector_r3()
