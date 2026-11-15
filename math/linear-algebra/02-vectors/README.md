# Vectors and Eigenvalues

handwritten notes and derivations for eigenvalues eigenvectors spectral properties and matrix diagonalization

[download full notes pdf](./vectors.pdf)

---

## Eigenvalues and Eigenvectors Definition

fundamental definition of eigenvalues and eigenvectors from the characteristic equation with step by step two by two matrix solution

$$A v = \lambda v \iff (A - \lambda I) v = 0 \iff \det(A - \lambda I) = 0$$

![eigenvalues and eigenvectors definition](./assets/page-01.png)

---

## Core Properties and Applications

relationship between eigenvalues determinant and trace along with applications in diagonalization and differential systems

$$\det(A) = \prod_{i=1}^n \lambda_i \quad \text{and} \quad \text{tr}(A) = \sum_{i=1}^n \lambda_i$$

![properties and applications](./assets/page-02.png)

---

## Two by Two Systems and Complex Roots

analysis of distinct real roots repeated roots and complex conjugate eigenvalue pairs in two by two systems

$$\lambda_{1, 2} = a \pm bi \implies v_{1, 2} = u \pm iw$$

![two by two cases and complex roots](./assets/page-03.png)

---

## Three by Three Systems and Distinct Roots

characteristic polynomial derivation and eigenvector computation for three by three matrices using row reduction

$$p(\lambda) = \det(A - \lambda I) = 0 \implies (A - \lambda_k I) v_k = 0$$

![three by three distinct roots](./assets/page-04.png)

---

## Repeated Roots and Multiplicity

handling repeated eigenvalues and determining eigenvectors in degenerate cases

$$\text{algebraic multiplicity} \ge \text{geometric multiplicity}$$

![repeated roots in three by three](./assets/page-05.png)

---

## Matrix Diagonalization

constructing modal matrix and diagonal matrix with step by step verification of similarity transformations

$$D = P^{-1} A P \iff A = P D P^{-1}$$

![matrix diagonalization](./assets/page-06.png)

---

## Multiplicity and Diagonalizability Conditions

algebraic versus geometric multiplicity and necessary conditions for matrix diagonalizability

$$A \text{ is diagonalizable} \iff \text{alg mult}(\lambda) = \text{geom mult}(\lambda) \quad \forall \lambda$$

![multiplicity and diagonalizability](./assets/page-07.png)
