import numpy as np 
import matplotlib.pyplot as plt


def compute_eigens(matrix): # compute of eigenvalues and eigenvectors of a matrix

    eigenvalues , eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


A = np.array([[1 , 2],
             [2 , 3]])

eigenvalues, eigenvectors = compute_eigens(A)
P = eigenvectors
D = np.diag(eigenvalues)
P_inv = np.linalg.inv(P)

D_computed = P_inv @ A @ P


print("matrix A:\n", A)
print("\nModal matrix P (eigenvectors):\n", P)
print("\nExpected D (diagonal):\n", D)
print("\nComputed D (P_inv @ A @ P):\n", D_computed)


if np.allclose(D, D_computed):
    print("\nDiagonalization theorem is okey! (D == P_inv @ A @ P)")
