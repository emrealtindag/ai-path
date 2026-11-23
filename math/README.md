# mathematics for autonomous systems

engineering curriculum, mathematical proofs, derivations, and curated resources for linear algebra, multivariate calculus, lie groups, probability, and numerical optimization.

---

## architecture overview

mathematics forms the first-principles bedrock upon which every autonomous perception, control, and ai algorithm is built:

```
[linear algebra: vector spaces / svd / projections]
                        │
                        ▼
[multivariate calculus: gradients / jacobians / lie theory]
                        │
                        ▼
[probability & statistics: bayes / gaussians / covariance]
                        │
                        ▼
[numerical optimization: gauss-newton / levenberg-marquardt]
                        │
                        ▼
[applied engineering: state estimation / slam / uav dynamics]
```

---

## study checklist

### 01. linear algebra
- [x] scalars, vectors, and matrix algebraic operations
- [x] matrix inverses, determinants, and linear systems
- [x] eigenvalues, eigenvectors, and characteristic polynomials
- [ ] vector spaces, subspaces, linear independence, basis, and dimension
- [ ] inner product spaces, orthogonal projections, and gram-schmidt orthogonalization
- [ ] matrix rank, null space (kernel), column space, and fundamental theorem of linear algebra
- [ ] matrix factorizations: lu decomposition, qr factorization (householder / givens), cholesky decomposition
- [ ] singular value decomposition (svd): geometric interpretation, pseudo-inverse, and low-rank approximation
- [ ] positive definite matrices, quadratic forms, and matrix calculus (gradients of vector/matrix functions)

### 02. multivariate calculus and differential geometry
- [ ] scalar and vector fields, partial derivatives, directional derivatives, and gradient vectors
- [ ] jacobian matrices (vector-valued functions) and hessian matrices (second-order curvature)
- [ ] multivariable chain rule in compact matrix notation
- [ ] multivariate taylor series expansions and local quadratic approximations
- [ ] lie groups and lie algebras: 3d rotations on $so(3)$, rigid-body transformations on $se(3)$
- [ ] exponential and logarithmic maps, hat and vee operators, and left/right jacobians on manifolds

### 03. probability, statistics, and stochastic processes
- [ ] random variables, probability density functions (pdf), and cumulative distribution functions (cdf)
- [ ] conditional probability, independence, law of total probability, and bayes' theorem
- [ ] expectation, variance, covariance matrices, and cross-covariance
- [ ] multivariate gaussian (normal) distribution: properties, marginalization, conditioning, and affine transformations
- [ ] propagation of uncertainty via first-order taylor series approximation
- [ ] maximum likelihood estimation (mle) and maximum a posteriori (map) estimators

### 04. differential equations and numerical optimization
- [ ] ordinary differential equations (odes): first-order and second-order linear time-invariant (lti) systems
- [ ] state-space representations and matrix exponential solutions ($e^{at}$)
- [ ] numerical integration schemes: explicit euler, semi-implicit euler, and runge-kutta 4th order (rk4)
- [ ] unconstrained optimization: gradient descent, momentum, and newton-raphson method
- [ ] nonlinear least squares: gauss-newton algorithm, levenberg-marquardt dampening, and ceres solver principles

---

## curated resources

### video lectures & course series
- [gilbert strang – mit 18.06 linear algebra](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D): the undisputed classic university course on linear algebra, subspaces, projections, and eigenvalues.
- [3blue1brown – essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab): visual and geometric intuition behind vector spaces, determinants, matrix transformations, and dot/cross products.
- [3blue1brown – essence of calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr): fundamental geometric perspective on limits, derivatives, chain rule, and gradients.
- [joan solà – lie theory for state estimation in robotics lectures](https://www.youtube.com/watch?v=sLHph_9eYdc): applied mathematics of lie groups, quaternions, and manifold derivatives.

### foundational books & academic materials
- [introduction to applied linear algebra – vectors, matrices, and least squares (stephen boyd & lieven vandenberghe)](https://web.stanford.edu/~boyd/vmls/): outstanding freely available textbook emphasizing real-world engineering, least squares, and matrix models.
- [linear algebra done right (sheldon axler)](https://linear.axler.net/): rigorous mathematical exploration focusing on linear maps, vector spaces, and spectral theory without determinants.
- [numerical optimization (jorge nocedal & stephen j. wright)](https://link.springer.com/book/10.1007/978-0-387-40065-5): the authoritative reference on gradient descent, line searches, newton methods, and nonlinear least squares.

### open-source codebases & tools
- [libeigen/eigen](https://gitlab.com/libeigen/eigen): high-performance modern c++ template library for linear algebra, matrices, vectors, and numerical solvers.
- [ceres-solver/ceres-solver](https://github.com/ceres-solver/ceres-solver): google's open-source c++ library for modeling and solving large, complicated nonlinear least squares problems.
- [scipy/scipy](https://github.com/scipy/scipy): fundamental algorithms for scientific computing in python (optimization, linear algebra, integration).
