import numpy as np

# 1. drone position uncertainty (kalman filter error ellipse)
def compute_error_ellipse(covariance_matrix):
    # eigenvalues determine the squared lengths of the ellipse axes
    # eigenvectors determine the orientation of the ellipse in space
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # sort eigenvalues in descending order
    order = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]

    # 2-sigma confidence bounds (roughly 95% probability region)
    semi_major_axis = 2.0 * np.sqrt(max(eigenvalues[0], 0.0))
    semi_minor_axis = 2.0 * np.sqrt(max(eigenvalues[1], 0.0))
    tilt_angle_rad = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])

    return semi_major_axis, semi_minor_axis, np.degrees(tilt_angle_rad)

# 2. lidar surface normal estimation (point cloud pca)
def estimate_surface_normal(point_cluster):
    # compute centroid of points
    centroid = np.mean(point_cluster, axis=0)
    centered = point_cluster - centroid

    # covariance matrix of the 3d points
    cov = (centered.T @ centered) / len(point_cluster)

    # compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov)

    # the eigenvector corresponding to the smallest eigenvalue is the surface normal
    normal_vector = eigenvectors[:, 0]
    return normal_vector

if __name__ == "__main__":
    # sample kalman filter position covariance (x, y) with cross-correlation
    drone_cov = np.array([
        [0.25, 0.08],
        [0.08, 0.10]
    ])

    major, minor, angle = compute_error_ellipse(drone_cov)
    print("--- drone kalman filter error ellipse ---")
    print(f"semi-major axis (uncertainty): {major:.3f} m")
    print(f"semi-minor axis (uncertainty): {minor:.3f} m")
    print(f"ellipse orientation angle:    {angle:.2f} deg")

    # sample lidar point cluster lying roughly on a ground plane (z ≈ 0)
    np.random.seed(42)
    xy = np.random.uniform(-1.0, 1.0, (100, 2))
    z = 0.02 * np.random.randn(100, 1)  # noisy flat surface
    points = np.hstack([xy, z])

    normal = estimate_surface_normal(points)
    print("\n--- lidar point cloud surface normal ---")
    print(f"estimated normal vector: [{normal[0]:.3f}, {normal[1]:.3f}, {normal[2]:.3f}]")
    print("expected normal vector:  [0.000, 0.000, 1.000] (flat ground)")
