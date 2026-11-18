import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# 1. drone position uncertainty (kalman filter error ellipse)
def compute_error_ellipse(covariance_matrix):
    # eigenvalues determine the squared lengths of the ellipse axes
    # eigenvectors determine the orientation of the ellipse in space
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # sort eigenvalues in descending order
    order = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]

    # ensure canonical eigenvector orientation (first component >= 0)
    for i in range(2):
        if eigenvectors[0, i] < 0:
            eigenvectors[:, i] = -eigenvectors[:, i]

    # 2-sigma confidence bounds (roughly 95% probability region)
    semi_major_axis = 2.0 * np.sqrt(max(eigenvalues[0], 0.0))
    semi_minor_axis = 2.0 * np.sqrt(max(eigenvalues[1], 0.0))
    tilt_angle_rad = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])

    return semi_major_axis, semi_minor_axis, np.degrees(tilt_angle_rad), eigenvalues, eigenvectors

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
    if normal_vector[2] < 0:
        normal_vector = -normal_vector
    return normal_vector, centroid, eigenvalues, eigenvectors

def generate_visual_plot(drone_cov, major, minor, eigvals_2d, eigvecs_2d, points, centroid, normal, output_path):
    fig = plt.figure(figsize=(13, 6), dpi=150)
    fig.patch.set_facecolor('#0d1117')

    # left subplot: 2d error ellipse
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor('#161b22')

    theta = np.linspace(0, 2 * np.pi, 200)
    ellipse_std = np.array([major * np.cos(theta), minor * np.sin(theta)])
    ellipse_rot = eigvecs_2d @ ellipse_std

    ax1.plot(ellipse_rot[0, :], ellipse_rot[1, :], color='#58a6ff', linewidth=2.5, label='2-sigma error ellipse (95%)')
    ax1.fill(ellipse_rot[0, :], ellipse_rot[1, :], color='#58a6ff', alpha=0.15)
    ax1.scatter([0], [0], color='#f0883e', s=80, zorder=5, label='drone position (estimated mean)')

    # eigenvector arrows
    v1 = eigvecs_2d[:, 0] * major
    v2 = eigvecs_2d[:, 1] * minor
    ax1.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='#7ee787', width=0.012, label='v1: major uncertainty axis')
    ax1.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='#d2a8ff', width=0.012, label='v2: minor uncertainty axis')

    ax1.set_title('Drone Kalman Filter: Position Uncertainty Ellipse', color='#c9d1d9', fontsize=12, pad=12, fontweight='bold')
    ax1.set_xlabel('X Position Error (m)', color='#8b949e', fontsize=10)
    ax1.set_ylabel('Y Position Error (m)', color='#8b949e', fontsize=10)
    ax1.tick_params(colors='#8b949e')
    for spine in ax1.spines.values():
        spine.set_color('#30363d')
    ax1.grid(True, linestyle='--', alpha=0.3, color='#8b949e')
    ax1.set_aspect('equal', 'box')
    ax1.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9', fontsize=8.5, loc='upper left')

    # right subplot: 3d lidar surface normal
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.set_facecolor('#0d1117')
    ax2.xaxis.set_pane_color((0.08, 0.1, 0.13, 1.0))
    ax2.yaxis.set_pane_color((0.08, 0.1, 0.13, 1.0))
    ax2.zaxis.set_pane_color((0.08, 0.1, 0.13, 1.0))

    ax2.scatter(points[:, 0], points[:, 1], points[:, 2], color='#388bfd', alpha=0.5, s=25, label='LiDAR ground patch points')
    ax2.scatter([centroid[0]], [centroid[1]], [centroid[2]], color='#f0883e', s=60, label='patch centroid')
    ax2.quiver(centroid[0], centroid[1], centroid[2], normal[0], normal[1], normal[2]*0.8, color='#7ee787', linewidth=3, arrow_length_ratio=0.2, label='v3: estimated surface normal')

    ax2.set_title('LiDAR Point Cloud: PCA Surface Normal Vector', color='#c9d1d9', fontsize=12, pad=12, fontweight='bold')
    ax2.set_xlabel('X (m)', color='#8b949e', labelpad=6)
    ax2.set_ylabel('Y (m)', color='#8b949e', labelpad=6)
    ax2.set_zlabel('Z (m)', color='#8b949e', labelpad=6)
    ax2.tick_params(colors='#8b949e')
    ax2.set_zlim(-0.5, 1.0)
    ax2.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9', fontsize=8.5, loc='upper left')

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

if __name__ == "__main__":
    # sample kalman filter position covariance (x, y) with cross-correlation
    drone_cov = np.array([
        [0.25, 0.08],
        [0.08, 0.10]
    ])

    major, minor, angle, eigvals_2d, eigvecs_2d = compute_error_ellipse(drone_cov)
    print("--- drone kalman filter error ellipse ---")
    print(f"semi-major axis (uncertainty): {major:.3f} m")
    print(f"semi-minor axis (uncertainty): {minor:.3f} m")
    print(f"ellipse orientation angle:    {angle:.2f} deg")

    # sample lidar point cluster lying roughly on a ground plane (z ≈ 0)
    np.random.seed(42)
    xy = np.random.uniform(-1.0, 1.0, (120, 2))
    z = 0.03 * np.random.randn(120, 1)  # noisy flat surface
    points = np.hstack([xy, z])

    normal, centroid, eigvals_3d, eigvecs_3d = estimate_surface_normal(points)
    print("\n--- lidar point cloud surface normal ---")
    print(f"estimated normal vector: [{normal[0]:.3f}, {normal[1]:.3f}, {normal[2]:.3f}]")
    print("expected normal vector:  [0.000, 0.000, 1.000] (flat ground)")

    # generate visual plot image in assets folder
    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    plot_file = assets_dir / "robotics_eigen_visual.png"
    generate_visual_plot(drone_cov, major, minor, eigvals_2d, eigvecs_2d, points, centroid, normal, plot_file)
    print(f"\nvisual plot generated at: {plot_file.name}")
