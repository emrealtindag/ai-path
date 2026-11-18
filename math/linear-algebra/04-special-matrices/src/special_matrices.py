import numpy as np

print("=== 1. CONJUGATE TRANSPOSE (HERMITIAN TRANSPOSE) ===")
# complex matrices from handwritten notes page 1
A = np.array([[3 + 7j, 0], 
              [2j, 4 - 1j]])

B = np.array([[1, 3 - 2j], 
              [5j, 2j + 1]])

# conjugate transpose property: (AB)* == B* @ A*
left_star = (A @ B).conj().T
right_star = B.conj().T @ A.conj().T

print("(A @ B)*:\n", left_star)
print("B* @ A*:\n", right_star)
if np.allclose(left_star, right_star):
    print("verification: SUCCESS ((AB)* == B* @ A*)\n")

print("=== 2. UNITARY MATRIX (U* @ U == I) ===")
# unitary matrix from handwritten notes page 2
U = 0.5 * np.array([[1 + 1j, 1 - 1j], 
                    [1 - 1j, 1 + 1j]])

U_star = U.conj().T
identity = U_star @ U

print("U* @ U:\n", np.round(identity, 4))
if np.allclose(identity, np.eye(2)):
    print("verification: SUCCESS (U is unitary: U* == U^-1)\n")

print("=== 3. HERMITIAN MATRIX AND REAL EIGENVALUES ===")
# hermitian matrix from handwritten notes page 3 & 4
H = np.array([[1, 2j], 
              [-2j, 3]])

H_star = H.conj().T
print("H == H*:", np.allclose(H, H_star))

eigenvalues_H, eigenvectors_H = np.linalg.eig(H)
print("eigenvalues of H:", eigenvalues_H)
# hermitian eigenvalues are guaranteed to be purely real numbers
is_real = np.all(np.isreal(eigenvalues_H))
print("are all eigenvalues real?:", is_real)
if np.allclose(H, H_star) and is_real:
    print("verification: SUCCESS (Hermitian matrix has strictly real eigenvalues: 2 ± sqrt(5))\n")

print("=== 4. IDEMPOTENT MATRIX (M^2 == M) ===")
# idempotent projection matrix from handwritten notes page 4
M = 0.5 * np.array([[1.0, 1.0], 
                    [1.0, 1.0]])

M_squared = M @ M
print("M^2:\n", M_squared)

eigenvalues_M, _ = np.linalg.eig(M)
print("eigenvalues of M:", np.round(eigenvalues_M, 4))

rank_M = np.linalg.matrix_rank(M)
trace_M = int(np.round(np.trace(M)))
print(f"rank(M) = {rank_M}, trace(M) = {trace_M}")

if np.allclose(M, M_squared) and rank_M == trace_M:
    print("verification: SUCCESS (M^2 == M, rank == trace, eigenvalues are strictly 0 and 1)")
