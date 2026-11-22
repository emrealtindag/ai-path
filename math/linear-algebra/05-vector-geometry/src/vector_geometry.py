import numpy as np


# 1. uav velocity vector and speed (norm / normalization)
v_velocity = np.array([3.0, 4.0, 0.0])
speed = np.linalg.norm(v_velocity)
v_unit = v_velocity / speed

print("speed (m/s):", speed)
print("unit direction:", v_unit)
print("unit norm check:", np.linalg.norm(v_unit), "\n")


# 2. flight heading and wind force projection (scalar and vector projection)
v_heading = np.array([1.0, 0.0, 0.0])
w_wind = np.array([4.0, 3.0, 0.0])

scalar_proj = np.dot(w_wind, v_heading) / np.linalg.norm(v_heading)
v_hat = v_heading / np.linalg.norm(v_heading)
proj_vec = scalar_proj * v_hat

print("wind pushing forward (N):", scalar_proj)
print("projected wind vector:", proj_vec, "\n")


# 3. arm vector and motor thrust force (torque generation via cross product: tau = r x F)
r_arm = np.array([0.2, 0.0, 0.0])
F_thrust = np.array([0.0, 0.0, 10.0])

torque = np.cross(r_arm, F_thrust)
print("torque vector (N*m):", torque, "\n")


# 4. 3d surface mesh polygon (lidar patch: surface normal and area via cross product)
edge1 = np.array([1.0, 2.0, -1.0])
edge2 = np.array([-1.0, 1.0, 2.0])

normal_vec = np.cross(edge1, edge2)
triangle_area = 0.5 * np.linalg.norm(normal_vec)
parallelogram_area = np.linalg.norm(normal_vec)

print("surface normal vector:", normal_vec)
print("triangle area (m^2):", triangle_area)
print("parallelogram area (m^2):", parallelogram_area)
