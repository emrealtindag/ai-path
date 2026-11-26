import numpy as np
from scipy.linalg import null_space


# ---------------------------------------------------------
# 1. orthogonal vectors & sets (page 1 & 2)
#    two vectors are orthogonal if u . v = 0
# ---------------------------------------------------------
def is_orthogonal(u, v):
    return np.isclose(np.dot(u, v), 0.0)


u1 = np.array([1.0, -2.0, 1.0])
v1 = np.array([3.0, 1.0, -1.0])
print("u1 . v1 =", np.dot(u1, v1), "| orthogonal:", is_orthogonal(u1, v1))

u2 = np.array([1.0, 2.0, -1.0, 4.0])
v2 = np.array([2.0, 1.0, -5.0, -6.0])
print("u2 . v2 =", np.dot(u2, v2), "| orthogonal:", is_orthogonal(u2, v2))


# ---------------------------------------------------------
# 2. orthonormal set & orthogonal complement (page 3)
# ---------------------------------------------------------
def is_orthonormal_set(vectors):
    n = len(vectors)
    for i in range(n):
        if not np.isclose(np.linalg.norm(vectors[i]), 1.0):
            return False
        for j in range(i + 1, n):
            if not np.isclose(np.dot(vectors[i], vectors[j]), 0.0):
                return False
    return True


e1 = np.array([1.0, 0.0, 0.0])
e2 = np.array([0.0, -1.0, 0.0])
e3 = np.array([0.0, 0.0, 1.0])
print("standard signed set is orthonormal:", is_orthonormal_set([e1, e2, e3]))

# orthogonal complement S_perp for S = {[1,1,0,2], [2,0,1,1], [1,-1,1,1]}
S = np.array([
    [1.0, 1.0, 0.0, 2.0],
    [2.0, 0.0, 1.0, 1.0],
    [1.0, -1.0, 1.0, 1.0]
])
S_perp = null_space(S)
print("S_perp dimension:", S_perp.shape[1])
print("S @ S_perp == 0:", np.allclose(S @ S_perp, 0.0))


# ---------------------------------------------------------
# 3. gram-schmidt orthogonalization (page 4)
# ---------------------------------------------------------
def gram_schmidt(vectors):
    orthogonal = []
    for v in vectors:
        w = v.copy()
        for u in orthogonal:
            proj = (np.dot(v, u) / np.dot(u, u)) * u
            w = w - proj
        orthogonal.append(w)

    orthonormal = []
    for u in orthogonal:
        orthonormal.append(u / np.linalg.norm(u))
    return orthogonal, orthonormal


a1 = np.array([1.0, 2.0])
a2 = np.array([-3.0, 4.0])
orth_2d, onorm_2d = gram_schmidt([a1, a2])
print("gram-schmidt 2d orthogonal basis:", [np.round(vec, 3).tolist() for vec in orth_2d])
print("gram-schmidt 2d orthonormal check:", is_orthonormal_set(onorm_2d))


# ---------------------------------------------------------
# 4. QR factorization: A = Q @ R (page 5)
# ---------------------------------------------------------
A_qr = np.array([
    [1.0, 3.0],
    [2.0, 5.0]
])

cols = [A_qr[:, 0], A_qr[:, 1]]
_, q_cols = gram_schmidt(cols)
Q = np.column_stack(q_cols)
R = Q.T @ A_qr

print("Q:\n", np.round(Q, 4))
print("R:\n", np.round(R, 4))
print("Q @ R == A:", np.allclose(Q @ R, A_qr))
print("Q.T @ Q == I:", np.allclose(Q.T @ Q, np.eye(2)))


# ---------------------------------------------------------
# 5. orthogonal matrix verification (page 6)
#    A^-1 = A^T  and  A @ A^T = I
# ---------------------------------------------------------
A_orth = np.array([
    [np.sqrt(3.0) / 2.0, -0.5],
    [0.5, np.sqrt(3.0) / 2.0]
])

cond_inv = np.allclose(np.linalg.inv(A_orth), A_orth.T)
cond_eye = np.allclose(A_orth @ A_orth.T, np.eye(2))
print("A_orth inverse == transpose:", cond_inv)
print("A_orth @ A_orth.T == I:", cond_eye)


# ---------------------------------------------------------
# 6. least squares method: A^T A x = A^T b (page 7)
# ---------------------------------------------------------
A_ls = np.array([
    [1.0, -1.0],
    [3.0, 2.0],
    [-2.0, 4.0]
])
b_ls = np.array([4.0, 1.0, 3.0])

x_hat = np.linalg.solve(A_ls.T @ A_ls, A_ls.T @ b_ls)
error_vec = b_ls - A_ls @ x_hat
error_norm = np.linalg.norm(error_vec)

print("least squares solution x_hat:", np.round(x_hat, 4))
print("residual vector (b - A x):", np.round(error_vec, 4))
print("least squares error ||b - A x||:", round(error_norm, 4))


# ---------------------------------------------------------
# 7. curve fitting with least squares: y = a*x + b (page 8)
#    points: (0, 1), (1, 3), (2, 4), (3, 4)
# ---------------------------------------------------------
A_fit = np.array([
    [0.0, 1.0],
    [1.0, 1.0],
    [2.0, 1.0],
    [3.0, 1.0]
])
b_fit = np.array([1.0, 3.0, 4.0, 4.0])

params = np.linalg.solve(A_fit.T @ A_fit, A_fit.T @ b_fit)
a_slope, b_intercept = params
print(f"best-fit line: y = {a_slope:.2f}x + {b_intercept:.2f}")
