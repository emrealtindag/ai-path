# vector spaces

handwritten notes, mathematical derivations and numerical verifications for vector spaces, subspaces, linear independence, spanning sets, bases, dimension, and coordinate vector representations

[download full notes pdf](./vector-spaces.pdf) | [runnable script: src/vector_spaces.py](./src/vector_spaces.py)

---

## vector space axioms and closure

definition of abstract vector spaces over real field $\mathbb{R}$, closure under vector addition and scalar multiplication, and the 10 structural axioms verified in $\mathbb{R}^3$

$$
u, v \in V \implies u + v \in V \quad \text{and} \quad c \in \mathbb{R}, u \in V \implies c \cdot u \in V
$$

![vector space axioms](./assets/page-01.png)

---

## subspaces and closure conditions

conditions for a non-empty subset $W \subseteq V$ to form a subspace, zero vector inclusion, and counterexample analysis for affine planes and nonlinear constraints

$$
w_1, w_2 \in W \implies w_1 + w_2 \in W \quad \text{and} \quad c \in \mathbb{R}, w \in W \implies c \cdot w \in W
$$

![subspaces and verification](./assets/page-02.png)

### computational verification

```python
# test subspace w1: x1 == 0 (closed under addition and scaling)
w1_a = np.array([0.0, 2.0, -1.0])
w1_b = np.array([0.0, -3.0, 4.0])
assert (w1_a + w1_b)[0] == 0.0
assert (2.5 * w1_a)[0] == 0.0

# counterexample w2: x1 + x2 == 2 (fails closure under addition)
w2_a = np.array([1.0, 1.0, 5.0])
w2_b = np.array([0.0, 2.0, -3.0])
assert (w2_a + w2_b)[0] + (w2_a + w2_b)[1] != 2.0
```

```text
subspace closure tests:
  w1 (x1 == 0) is closed under addition and scaling -> valid subspace
  w2 (x1 + x2 == 2) fails addition closure (sum = 4 != 2) -> not a subspace
```

---

## linear combinations

expressing arbitrary spatial vectors as linear combinations of basis or generating vectors

$$
w = \sum_{i=1}^k c_i v_i = c_1 v_1 + c_2 v_2 + \dots + c_k v_k
$$

![linear combinations](./assets/page-03.png)

---

## linear dependence and independence

geometric meaning of linear independence, collinear and coplanar sets, and trivial solution criterion for homogeneous systems

$$
\sum_{i=1}^n c_i v_i = 0 \iff c_1 = c_2 = \dots = c_n = 0
$$

![linear dependence vs independence](./assets/page-04.png)

---

## linear independence via determinants and rank

testing linear independence of column vector sets using determinant non-singularity and full matrix rank

$$
\det(A) \ne 0 \iff \text{rank}(A) = n \iff \{v_1, \dots, v_n\} \text{ is linearly independent}
$$

![independence via determinant](./assets/page-05.png)
![polynomial independence and determinant parameters](./assets/page-06.png)

### computational verification

```python
# independent set in r2: rank == 2, det != 0
A_indep = np.array([[1.0, 2.0], [1.0, -3.0]])
assert np.linalg.matrix_rank(A_indep) == 2
assert not np.isclose(np.linalg.det(A_indep), 0.0)

# dependent set in r2: rank == 1, det == 0
A_dep = np.array([[1.0, 2.0], [3.0, 6.0]])
assert np.linalg.matrix_rank(A_dep) == 1
assert np.isclose(np.linalg.det(A_dep), 0.0)
```

```text
linear independence tests:
  independent set rank = 2, det = -5.0000 -> linearly independent
  dependent set rank = 1, det = 0.0000 -> linearly dependent
  3d set det = 1.0000, rank = 3 -> linearly independent
```

---

## span and spanning sets

definition of subspace span, minimal vector requirements to span $\mathbb{R}^n$, and linear system consistency checks

$$
\text{span}\{v_1, \dots, v_k\} = \{ c_1 v_1 + \dots + c_k v_k \mid c_i \in \mathbb{R} \}
$$

![spanning sets and dimension conditions](./assets/page-07.png)

### computational verification

```python
# spanning set in r2: full rank spans r2
S1 = np.array([[1.0, -1.0], [2.0, 1.0]])
assert np.linalg.matrix_rank(S1) == 2

# non-spanning set in r2: rank 1 cannot span r2
S2 = np.array([[2.0, -1.0], [4.0, -2.0]])
assert np.linalg.matrix_rank(S2) == 1
```

```text
spanning tests:
  set s1 rank = 2 == 2 -> spans r2
  set s2 rank = 1 < 2 -> fails to span r2
```

---

## basis and dimension

minimal generating sets that are simultaneously linearly independent and span the vector space, standard bases, and degree of freedom / dimension

$$
\mathcal{B} \text{ is a basis for } V \iff \text{span}(\mathcal{B}) = V \quad \text{and} \quad \mathcal{B} \text{ is linearly independent}
$$

$$
\dim(V) = |\mathcal{B}|
$$

![basis definition and standard bases](./assets/page-08.png)
![polynomial basis and dimension](./assets/page-09.png)

### computational verification

```python
# basis in r2: s = {[1, 2], [3, 4]} -> det != 0, rank == 2
B = np.array([[1.0, 3.0], [2.0, 4.0]])
assert not np.isclose(np.linalg.det(B), 0.0)
assert np.linalg.matrix_rank(B) == 2
```

```text
basis and dimension tests:
  basis matrix det = -2.0000 != 0, rank = 2
  vectors form a valid basis with dimension = 2
```

---

## coordinate vectors

unique representation of vectors relative to an ordered basis $\mathcal{B}$, forward synthesis and inverse coordinate extraction via linear systems

$$
v = P [v]_\mathcal{B} \iff [v]_\mathcal{B} = P^{-1} v
$$

![coordinate vectors in r2 and r3](./assets/page-10.png)

### computational verification

```python
# 1. r2 coordinate vector: basis s = {[1, 3], [2, 1]}, target v = [2, 3]
P2 = np.array([[1.0, 2.0], [3.0, 1.0]])
v2 = np.array([2.0, 3.0])
coords_v2 = np.linalg.solve(P2, v2)
assert np.allclose(coords_v2, [4.0 / 5.0, 3.0 / 5.0])
assert np.allclose(P2 @ coords_v2, v2)

# 2. r3 coordinate vector: basis s = {[1, 2, 1], [2, 9, 0], [3, 3, 4]}, target v = [5, -1, 9]
P3 = np.array([[1.0, 2.0, 3.0], [2.0, 9.0, 3.0], [1.0, 0.0, 4.0]])
v3 = np.array([5.0, -1.0, 9.0])
coords_v3 = np.linalg.solve(P3, v3)
assert np.allclose(coords_v3, [1.0, -1.0, 2.0])
assert np.allclose(P3 @ coords_v3, v3)

# forward synthesis from coordinates [-1, 3, 2]
coords_forward = np.array([-1.0, 3.0, 2.0])
v3_synthesized = P3 @ coords_forward
assert np.allclose(v3_synthesized, [11.0, 31.0, 7.0])
```

```text
coordinate vector tests:
  r2 coordinates [v]_S: [0.8 0.6] -> reconstructed: [2. 3.]
  r3 coordinates [v]_S: [ 1. -1.  2.] -> reconstructed: [ 5. -1.  9.]
  forward synthesis from [-1, 3, 2]: [11. 31.  7.]
  all coordinate mappings hold
```

---

## real-world and robotics applications

where vector spaces, bases and coordinate vectors run inside real robotics and state estimation code:

- **reference frames in uav navigation**: a drone operates across multiple coordinate spaces (inertial world frame, body frame, gimbal frame, camera sensor frame). each frame is an ordered orthonormal basis. a target position vector is invariant in physical space, but its coordinate vector $[p]_\mathcal{B}$ changes numerically based on the chosen basis.
- **state space representations in control (6-dof)**: the state of an autonomous drone is modeled as an element in a 12-dimensional vector space $\mathbb{R}^{12}$ containing position $(x, y, z)$, velocity $(\dot{x}, \dot{y}, \dot{z})$, attitude angles $(\phi, \theta, \psi)$, and angular rates $(p, q, r)$. the dimension of this vector space equals the state degrees of freedom.
- **lidar feature extraction and linear independence**: in point cloud processing, fitting a 3d plane requires at least three non-collinear laser points. checking the linear independence / rank of the point difference vectors prevents degenerate planar fits when points lie along a single scan line.
- **actuator redundancy and null space**: an aerial vehicle or robotic arm with more actuators than task degrees of freedom (e.g. an 8-rotor octocopter controlling 6-dof motion) operates in an over-determined vector space where motor mixing matrices exploit the subspace structure to maintain control authority even during motor failure.
