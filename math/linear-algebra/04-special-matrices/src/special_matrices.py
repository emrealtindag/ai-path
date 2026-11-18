import numpy as np

# 1. conjugate transpose
A = np.array([[3 + 7j, 0], 
              [2j, 4 - 1j]])

B = np.array([[1, 3 - 2j], 
              [5j, 2j + 1]])

left_star = (A @ B).conj().T
right_star = B.conj().T @ A.conj().T

print("(A @ B)*:\n", left_star)
print("B* @ A*:\n", right_star)
if np.allclose(left_star, right_star):
    print("conjugate transpose property holds: (AB)* == B* @ A*\n")

# 2. unitary matrix
U = 0.5 * np.array([[1 + 1j, 1 - 1j], 
                    [1 - 1j, 1 + 1j]])

identity = U.conj().T @ U

print("U* @ U:\n", np.round(identity, 4))
if np.allclose(identity, np.eye(2)):
    print("U is unitary: U* @ U == I\n")

# 3. hermitian matrix and real eigenvalues
H = np.array([[1, 2j], 
              [-2j, 3]])

eigenvalues_H, _ = np.linalg.eig(H)
print("eigenvalues of H:", eigenvalues_H)

if np.allclose(H, H.conj().T) and np.all(np.isreal(eigenvalues_H)):
    print("H is hermitian and all eigenvalues are real: 2 ± sqrt(5)\n")

# 4. idempotent matrix
M = 0.5 * np.array([[1.0, 1.0], 
                    [1.0, 1.0]])

eigenvalues_M, _ = np.linalg.eig(M)
rank_M = np.linalg.matrix_rank(M)
trace_M = int(np.round(np.trace(M)))

print("M^2:\n", M @ M)
print("eigenvalues of M:", np.round(eigenvalues_M, 4))
print(f"rank = {rank_M}, trace = {trace_M}")

if np.allclose(M, M @ M) and rank_M == trace_M:
    print("M is idempotent: M^2 == M and eigenvalues are 0 and 1")
