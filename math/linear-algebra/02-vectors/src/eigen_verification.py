import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path


def compute_eigens(matrix): # compute of eigenvalues and eigenvectors of a matrix

    eigenvalues , eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


A = np.array([[1 , 2],
             [2 , 3]])

eigenvalues, eigenvectors = compute_eigens(A)


lambda1 = eigenvalues[0]
lambda2 = eigenvalues[1]

v1 = eigenvectors[:, 0]
v2 = eigenvectors[:, 1]

print("eigenvalues1:", lambda1)
print("eigenvectors1:\n", v1)
print("eigenvalues2:", lambda2)
print("eigenvectors2:\n", v2)


for i in range(len(eigenvalues)):
    print(eigenvalues[i], eigenvectors[:, i])
    print(f"eigenpair : {i+1}")
    print("eigenvalue:", eigenvalues[i])
    print("eigenvector:\n", eigenvectors[:, i])

    # A @ v (matris carpimi)
    left_side = A @ eigenvectors[:, i]
    
    # lambda * v (skaler carpim)
    right_side = eigenvalues[i] * eigenvectors[:, i]

    if np.allclose(left_side, right_side):
        print("(A @ v == lambda * v)")
    else:
        print("WRONG THEOREM")

# simple 2d eigenvector visualization
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'v1 (lambda={lambda1:.2f})')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'v2 (lambda={lambda2:.2f})')

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.gca().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Eigenvectors of Symmetric Matrix A')
plt.legend()

# save figure to assets
assets_dir = Path(__file__).resolve().parent.parent / "assets"
plt.savefig(assets_dir / "eigenvectors_plot.png", dpi=150, bbox_inches='tight')
plt.close()
print("\nplot saved to assets/eigenvectors_plot.png")
