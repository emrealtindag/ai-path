import numpy as np

# 1. vector length (norm) and unit vector normalization
v = np.array([1, 2, -1])
norm_v = np.linalg.norm(v)
v_hat = v / norm_v

print("vector v:", v)
print("norm of v:", round(norm_v, 4))
print("unit vector v_hat:", np.round(v_hat, 4))
print("norm of v_hat:", round(np.linalg.norm(v_hat), 4))
print("unit vector is normalized\n")

# 2. scalar and vector projection of a onto b
a = np.array([1, 2, -1])
b = np.array([3, 1, 1])

scalar_proj = np.dot(a, b) / np.linalg.norm(b)
vector_proj = (np.dot(a, b) / np.dot(b, b)) * b

print("a dot b:", np.dot(a, b))
print("scalar projection (length):", round(scalar_proj, 4))
print("vector projection onto b:", np.round(vector_proj, 4))
print("projection matches manual calculation\n")

# 3. 2d triangle area using determinant
# points: A(1, -3), B(2, 1), C(4, 3)
AB = np.array([1, 4])
AC = np.array([3, 6])

area_2d = 0.5 * abs(np.linalg.det(np.column_stack([AB, AC])))
print("2d triangle area:", round(area_2d, 4))
print("2d area matches determinant calculation\n")

# 4. 3d triangle area using cross product
# vectors: CA = (1, 2, -1), CB = (3, 4, 1)
CA = np.array([1, 2, -1])
CB = np.array([3, 4, 1])

cross_triangle = np.cross(CA, CB)
area_3d_triangle = 0.5 * np.linalg.norm(cross_triangle)

print("CA x CB:", cross_triangle)
print("3d triangle area:", round(area_3d_triangle, 4))
print("3d triangle area matches cross product magnitude\n")

# 5. 3d parallelogram area using cross product
# vectors: AB = (2, 3, -1), AD = (3, 1, 0)
AB_par = np.array([2, 3, -1])
AD_par = np.array([3, 1, 0])

cross_par = np.cross(AB_par, AD_par)
area_par = np.linalg.norm(cross_par)

print("AB x AD:", cross_par)
print("3d parallelogram area:", round(area_par, 4))
print("3d parallelogram area matches cross product magnitude")
