import numpy as np
from scipy.linalg import null_space


# 1. camera to body coordinate transformation (change of basis)
# camera detects target at [v]_C (2m right, 0m down, 5m forward)
v_cam = np.array([2.0, 0.0, 5.0])

# transition matrix P (camera -> body)
transition_matrix = np.array([[0.0, 0.0, 1.0],
                              [1.0, 0.0, 0.0],
                              [0.0, 1.0, 0.0]])

# forward transform: [v]_B = P @ [v]_C
v_body = transition_matrix @ v_cam

# inverse transform check: [v]_C = inv(P) @ [v]_B
p_inverse = np.linalg.inv(transition_matrix)
v_cam_recovered = p_inverse @ v_body

print("--- 1. change of basis (camera -> body) ---")
print("camera frame:", v_cam)
print("body frame (x: forward, y: right, z: down):", v_body)
print("reconstructed camera frame:", v_cam_recovered)
print("change of basis holds:", np.allclose(v_cam, v_cam_recovered), "\n")


# 2. hexacopter null space and fault-tolerant motor control
# control allocation matrix B (4 outputs: thrust, roll, pitch, yaw from 6 motors)
B = np.array([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
              [1.0, 0.5, -0.5, -1.0, -0.5, 0.5],
              [0.0, 1.0, 1.0, 0.0, -1.0, -1.0],
              [1.0, -1.0, 1.0, -1.0, 1.0, -1.0]])

rank_B = np.linalg.matrix_rank(B)
columns_B = B.shape[1]
nullity_B = columns_B - rank_B

# orthonormal basis for the null space (Ax = 0)
Z = null_space(B)

print("--- 2. null space and motor allocation ---")
print("matrix B rank:", rank_B)
print("number of motors (columns):", columns_B)
print("nullity (free variables / degrees of redundancy):", nullity_B)
print("null space basis Z shape:", Z.shape)
print("B @ Z == 0 condition holds:", np.allclose(B @ Z, 0.0))

# normal hover thrusts (5 N each)
u0 = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
y_initial = B @ u0

# motor 1 overheats: redistribute thrust using null space vector Z[:, 0]
u_null = Z[:, 0] * 2.0
u_new = u0 + u_null
y_new = B @ u_new

print("baseline motor thrusts:", u0)
print("adjusted motor thrusts (motor 1 relieved):", np.round(u_new, 2))
print("net forces and torques preserved:", np.allclose(y_initial, y_new), "\n")


# 3. transition matrix between two non-standard bases (A -> B)
# sensor A (lidar basis) and sensor B (camera basis)
M_a = np.array([[2.0, 1.0], [1.0, 4.0]])
M_b = np.array([[3.0, -2.0], [1.0, 1.0]])

inv_M_b = np.linalg.inv(M_b)
transition_A_to_B = inv_M_b @ M_a

# coordinate vector in basis A transformed to basis B
x_a = np.array([2.0, 1.0])
x_b = transition_A_to_B @ x_a

print("--- 3. transition matrix between two bases (A -> B) ---")
print("transition matrix (A -> B):\n", np.round(transition_A_to_B, 2))
print("coordinates in basis B:", np.round(x_b, 2))
print("both bases represent same physical vector:", np.allclose(M_a @ x_a, M_b @ x_b), "\n")


# 4. column space and dynamic pivot basis
# last row is linear combination of first two rows (row3 = row1 + row2)
A = np.array([[1.0, 2.0, 0.0, 3.0],
              [0.0, 1.0, 1.0, 2.0],
              [1.0, 3.0, 1.0, 5.0]])

rank_A = np.linalg.matrix_rank(A)
column_space_dim = rank_A

# dynamic pivot column extraction using :rank_A
column_space_basis = A[:, :rank_A]
rank_basis = np.linalg.matrix_rank(column_space_basis)

print("--- 4. column space and pivot basis ---")
print("matrix rank:", rank_A)
print("column space dimension:", column_space_dim)
print("column space basis columns:\n", column_space_basis)
print("basis rank:", rank_basis, "\n")


# 5. subspace closure conditions (W1 vs W2)
# subspace W1: x1 = 0 (plane passing through origin)
w1_a = np.array([0.0, 2.0, -1.0])
w1_b = np.array([0.0, -3.0, 4.0])
w1_sum = w1_a + w1_b

# non-subspace W2: x1 + x2 = 2 (plane not passing through origin)
w2_a = np.array([1.0, 1.0, 5.0])
w2_b = np.array([0.0, 2.0, -3.0])
w2_sum = w2_a + w2_b

print("--- 5. subspace closure conditions ---")
print("W1 (x1 = 0) closed under addition:", w1_sum[0] == 0.0)
print("W2 (x1 + x2 = 2) closed under addition:", (w2_sum[0] + w2_sum[1]) == 2.0)
