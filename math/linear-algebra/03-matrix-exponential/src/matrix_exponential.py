import numpy as np 
import matplotlib.pyplot as plt

def compute_eigenvalues_and_eigenvectors(matrix):

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(A)

t = 1.0
P = eigenvectors
e_Dt = np.diag(np.exp(eigenvalues * t))
e_At_diag = P @ e_Dt @ np.linalg.inv(P)

# the other way to compute e^(At) is using the Cayley-Hamilton theorem

a1 = np.exp(3 * t) - np.exp(2 * t)
a0 = 3 * np.exp(2 * t) - 2 * np.exp(3 * t)

I = np.eye(2)
e_At_cayley = (a0 * I) + (a1 * A)

print(" using eigen decomposition:\n", e_At_diag)
print(" using Cayley-Hamilton theorem:\n", e_At_cayley)

if np.allclose(e_At_diag, e_At_cayley):
    print("\nboth of method give the same result")
