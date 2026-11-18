import numpy as np

# define two sample invertible 2x2 matrices
A = np.array([[2, 1],
              [1, 3]])

B = np.array([[3, 2],
              [1, 4]])

print("=== 1. transpose of product: (AB)^T == B^T @ A^T ===")
left_t = (A @ B).T
right_t = B.T @ A.T
print("(A @ B).T:\n", left_t)
print("B.T @ A.T:\n", right_t)
if np.allclose(left_t, right_t):
    print("verification: SUCCESS ((AB)^T == B^T @ A^T)\n")

print("=== 2. symmetric and skew-symmetric decomposition ===")
# any square matrix A = 0.5 * (A + A^T) + 0.5 * (A - A^T)
sym = 0.5 * (A + A.T)
skew = 0.5 * (A - A.T)
print("symmetric part is symmetric:", np.allclose(sym, sym.T))
print("skew-symmetric part satisfies A^T == -A:", np.allclose(skew.T, -skew))
if np.allclose(A, sym + skew):
    print("verification: SUCCESS (A == A_sym + A_skew)\n")

print("=== 3. inverse of product: (AB)^-1 == B^-1 @ A^-1 ===")
inv_AB = np.linalg.inv(A @ B)
inv_B_inv_A = np.linalg.inv(B) @ np.linalg.inv(A)
print("(A @ B)^-1:\n", inv_AB)
print("B^-1 @ A^-1:\n", inv_B_inv_A)
if np.allclose(inv_AB, inv_B_inv_A):
    print("verification: SUCCESS ((AB)^-1 == B^-1 @ A^-1)\n")

print("=== 4. determinant properties ===")
det_AB = np.linalg.det(A @ B)
det_A_det_B = np.linalg.det(A) * np.linalg.det(B)
print(f"det(AB) = {det_AB:.4f}, det(A)*det(B) = {det_A_det_B:.4f}")
if np.isclose(det_AB, det_A_det_B):
    print("verification: SUCCESS (det(AB) == det(A) * det(B))")

det_inv_A = np.linalg.det(np.linalg.inv(A))
inv_det_A = 1.0 / np.linalg.det(A)
print(f"det(A^-1) = {det_inv_A:.4f}, 1/det(A) = {inv_det_A:.4f}")
if np.isclose(det_inv_A, inv_det_A):
    print("verification: SUCCESS (det(A^-1) == 1 / det(A))\n")

print("=== 5. cramer's rule vs numpy solve ===")
# solve A @ x = b
b = np.array([5, 8])
det_A = np.linalg.det(A)

# replace 1st column with b
A0 = A.copy()
A0[:, 0] = b
x0 = np.linalg.det(A0) / det_A

# replace 2nd column with b
A1 = A.copy()
A1[:, 1] = b
x1 = np.linalg.det(A1) / det_A

x_cramer = np.array([x0, x1])
x_solve = np.linalg.solve(A, b)

print("cramer's rule solution:", x_cramer)
print("numpy linalg solve:    ", x_solve)
if np.allclose(x_cramer, x_solve):
    print("verification: SUCCESS (cramer matches np.linalg.solve)")
