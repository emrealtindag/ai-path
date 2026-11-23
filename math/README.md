# mathematics for autonomous systems

engineering curriculum, mathematical proofs, derivations, and curated resources for linear algebra, multivariate calculus, lie groups, probability, and numerical optimization.

---

## handwritten modules & implementations

- **[linear algebra](./linear-algebra/)** — matrix proofs, eigenvalues/eigenvectors, matrix exponential, special hermitian/unitary matrices, 3d vector geometry, and vector spaces.
- **[calculus](./calculus/)** — 3d euclidean vector geometry, dot/cross products, projections, and multivariable foundations.

---

## architecture overview

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

## complete checklist and resources

### 01. mathematics

#### 2.1 linear algebra

**core topics:**

- [x] scalars, vectors, matrices
- [ ] vector spaces
- [ ] linear independence
- [ ] basis and dimension
- [x] matrix operations
- [x] matrix inverse
- [x] determinants
- [ ] rank and null space
- [x] eigenvalues and eigenvectors
- [ ] orthogonality
- [ ] orthogonal projection
- [ ] matrix decomposition
- [ ] lu decomposition
- [ ] qr decomposition
- [ ] singular value decomposition (svd)
- [ ] positive definite matrices
- [ ] least squares
- [ ] matrix calculus

**advanced connections:**

- [ ] principal component analysis (pca)
- [ ] optimization
- [ ] computer vision geometry
- [ ] neural networks
- [ ] state estimation
- [ ] 3d transformations ($se(3)$, $so(3)$)

**resources:**

- **turkish resources:**
  1. **buders – linear algebra:** [youtube playlists (@buders)](https://www.youtube.com/@Buders) — practical turkish lectures on matrix operations, determinants, rank, eigenvalues, and eigenvectors
  2. **nesin math village – ali nesin linear algebra:** [youtube playlist](https://www.youtube.com/playlist?list=PL-VAZnoQqQ4UF8Y7Q4rf8ruNSVhnfEmWn) — theoretical foundations of vector spaces and linear transformations (turkish)
  3. **books (turkish):** h. hilmi hacısalihoğlu – linear algebra · bernard kolman – applied linear algebra
- **video lectures:**
  1. **3blue1brown – essence of linear algebra:** [youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — visual 3d meaning of matrices, determinants, and eigenvalues
  2. **mit 18.06 linear algebra (prof. gilbert strang):** [youtube lecture series](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) — core university course covering svd, least squares, qr/lu decomposition, and orthogonal projections
  3. **mit 18.065 matrix methods in data analysis, signal processing, and ml (gilbert strang):** [youtube lecture series](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k) — matrix methods focused directly on machine learning and optimization
- **books, papers & repositories:**
  1. **immersive linear algebra:** [immersivemath.com/ila](http://immersivemath.com/ila/index.html) — interactive graphics to build intuition for linear algebra and 3d transforms
  2. **mathematics for machine learning (deisenroth, faisal, ong):** [mml-book.github.io (free pdf)](https://mml-book.github.io/book/mml-book.pdf) — chapters 2–4 and chapter 10 (pca & svd)
  3. **the matrix calculus you need for deep learning (parr & howard):** [explained.ai/matrix-calculus](https://explained.ai/matrix-calculus/) — gradients and matrix derivatives used in neural networks
  4. **library – eigen c++:** [eigen.tuxfamily.org](https://eigen.tuxfamily.org/dox/GettingStarted.html) — standard c++ linear algebra library for robotics, slam, and state estimation

#### 2.2 calculus

**core topics:**

- [x] limits and continuity
- [x] differentiation
- [ ] integration
- [ ] partial derivatives
- [ ] multivariable calculus
- [x] chain rule
- [ ] gradient
- [ ] jacobian matrix
- [ ] hessian matrix
- [ ] directional derivatives
- [ ] vector calculus
- [ ] multiple integrals
- [ ] taylor series
- [ ] differential calculus
- [ ] integral calculus

**advanced connections:**

- [ ] backpropagation
- [ ] gradient descent
- [ ] neural network optimization
- [ ] robotics kinematics
- [ ] motion planning
- [ ] continuous optimization

**resources:**

- **turkish resources:**
  1. **buders – calculus 1 & calculus 2:** [youtube channel](https://www.youtube.com/@Buders) — turkish lectures on limits, derivatives, integrals, partial derivatives, gradients, and jacobians
- **video lectures:**
  1. **3blue1brown – essence of calculus:** [youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — visual intuition behind derivatives, chain rule, and taylor series
  2. **mit 18.02 multivariable calculus (prof. denis auroux):** [youtube lecture series](https://www.youtube.com/playlist?list=PL4C4C8A7D06566F38) — 3d vector calculus, gradients, directional derivatives, and lagrange multipliers
  3. **mit 18.01 single variable calculus (prof. david jerison):** [youtube lecture series](https://www.youtube.com/playlist?list=PL590CCC2BC5AF3BC1) — core single-variable calculus lectures
  4. **professor leonard – calculus 1, 2 & 3:** [youtube playlists](https://www.youtube.com/@ProfessorLeonard/playlists) — step-by-step walkthroughs with lots of solved practice problems
- **books, papers & repositories:**
  1. **mathematics for machine learning – chapter 5 (vector calculus):** [mml-book.github.io (free pdf)](https://mml-book.github.io/book/mml-book.pdf) — jacobians, hessians, and backpropagation math
  2. **paul’s online math notes (calculus i, ii, iii):** [tutorial.math.lamar.edu](https://tutorial.math.lamar.edu/) — written reference notes with worked step-by-step examples

#### 2.3 probability & statistics

**core topics:**

- [ ] probability theory
- [ ] conditional probability
- [ ] bayes’ theorem
- [ ] random variables
- [ ] probability distributions
- [ ] gaussian distribution
- [ ] bernoulli distribution
- [ ] binomial distribution
- [ ] poisson distribution
- [ ] multivariate gaussian
- [ ] expectation and variance
- [ ] covariance and correlation
- [ ] conditional distributions
- [ ] maximum likelihood estimation (mle)
- [ ] maximum a posteriori estimation (map)
- [ ] hypothesis testing
- [ ] confidence intervals
- [ ] statistical inference
- [ ] bayesian statistics
- [ ] monte carlo methods

**advanced connections:**

- [ ] kalman filter
- [ ] bayesian filtering
- [ ] particle filters
- [ ] probabilistic robotics
- [ ] machine learning
- [ ] uncertainty estimation
- [ ] sensor fusion

**resources:**

- **turkish resources:**
  1. **buders – probability & statistics:** [youtube channel](https://www.youtube.com/@Buders) — turkish lectures on conditional probability, bayes theorem, and distributions
- **video lectures:**
  1. **statquest with josh starmer – statistics & probability fundamentals:** [youtube playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) — clear visual guide to mle, map, covariance, and probability distributions
  2. **mit 6.041 probabilistic systems analysis and applied probability (prof. john tsitsiklis):** [youtube lecture series](https://www.youtube.com/playlist?list=PLUl4u3cNGP60A3XMwZ5sep719_nh95qOe) — probability theory for robotics, sensor noise, and state estimation
  3. **harvard stat 110 – probability (prof. joe blitzstein):** [youtube lecture series](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — deep probability theory, conditional expectation, and monte carlo methods
- **books, papers & repositories:**
  1. **seeing theory (brown university):** [seeing-theory.brown.edu](https://seeing-theory.brown.edu/) — interactive browser visualizations for probability distributions and bayesian inference
  2. **probabilistic machine learning: an introduction (kevin murphy):** [probml.github.io/pml-book](https://probml.github.io/pml-book/book1.html) — multivariate gaussians, bayesian learning, and uncertainty estimation (free pdf)
  3. **think stats & think bayes (allen downey):** [greenteapress.com](https://greenteapress.com/wp/) — learn probability and bayesian filtering by writing python code (free)

#### 2.4 differential equations

**core topics:**

- [ ] ordinary differential equations (ode)
- [ ] partial differential equations (pde)
- [ ] linear differential equations
- [ ] nonlinear differential equations
- [ ] initial value problems
- [ ] boundary value problems
- [ ] numerical solutions
- [ ] stability analysis
- [ ] dynamical systems

**where it is used:**

- [ ] robot motion models
- [ ] physical system simulations
- [ ] control systems
- [ ] dynamic modeling
- [ ] motion estimation

**resources:**

- **turkish resources:**
  1. **buders – differential equations:** [youtube channel](https://www.youtube.com/@Buders) — turkish lectures on odes, initial value problems, and laplace transforms
- **video lectures:**
  1. **3blue1brown – differential equations:** [youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6) — visual intuition for phase space, stability, and dynamical systems
  2. **steve brunton – differential equations & dynamical systems:** [youtube playlist](https://www.youtube.com/playlist?list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA) — practical engineering lectures for robot kinematics, control systems, and nonlinear dynamics
  3. **mit 18.03 differential equations (prof. arthur mattuck):** [youtube lecture series](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D) — classic mit differential equations curriculum
- **books, papers & repositories:**
  1. **data-driven science and engineering (brunton & kutz):** [databookuw.com](https://databookuw.com/) — dynamical systems, control, and machine learning (free course materials)
  2. **paul’s online math notes – differential equations:** [tutorial.math.lamar.edu/classes/de/de.aspx](https://tutorial.math.lamar.edu/Classes/DE/DE.aspx) — practical solution methods and worked examples
  3. **nonlinear dynamics and chaos (steven strogatz):** [youtube playlist](https://www.youtube.com/playlist?list=PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V) — nonlinear systems and stability analysis

#### 2.5 optimization

**core topics:**

- [ ] convex optimization
- [ ] nonlinear optimization
- [ ] linear programming
- [ ] quadratic programming
- [ ] gradient descent
- [ ] stochastic gradient descent (sgd)
- [ ] adam and adamw
- [ ] newton’s method
- [ ] constrained optimization
- [ ] lagrange multipliers
- [ ] kkt conditions (karush-kuhn-tucker)
- [ ] least squares optimization
- [ ] nonlinear least squares
- [ ] gauss-newton
- [ ] levenberg-marquardt

**resources:**

- **turkish resources:**
  1. **itu / metu numerical optimization open courseware:** [metu ocw](https://ocw.metu.edu.tr/) — turkish/english course notes on constrained optimization, lagrange multipliers, and kkt conditions
- **video lectures:**
  1. **cyrill stachniss – least squares, gauss-newton & levenberg-marquardt:** [youtube lecture videos](https://www.youtube.com/results?search_query=cyrill+stachniss+least+squares+gauss+newton) — clear explanation of nonlinear least squares in robotics, camera calibration, and slam
  2. **stanford ee364a – convex optimization (prof. stephen boyd):** [youtube lecture series](https://www.youtube.com/playlist?list=PL3940DD956CDF0622) — standard reference course for convex optimization, qp, lagrangian duality, and kkt
  3. **steve brunton – optimization bootcamp:** [youtube videos](https://www.youtube.com/results?search_query=steve+brunton+optimization) — overview of gradient descent and engineering optimization
- **books, papers & repositories:**
  1. **ceres solver (non-linear least squares):** [github.com/ceres-solver/ceres-solver](https://github.com/ceres-solver/ceres-solver) — google's c++ optimization library built for slam and bundle adjustment
  2. **convex optimization (boyd & vandenberghe):** [web.stanford.edu/~boyd/cvxbook](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — full textbook available as free pdf
  3. **methods for non-linear least squares problems (madsen, nielsen, tingleff – dtu):** [free pdf guide](https://www2.imm.dtu.dk/pubdb/edoc/imm3215.pdf) — clean 60-page math derivation of gauss-newton and levenberg-marquardt
  4. **numerical optimization (nocedal & wright):** [springer book page](https://link.springer.com/book/10.1007/978-0-387-40065-5) — core textbook on numerical optimization theory

#### 2.6 numerical methods

**core topics:**

- [ ] numerical integration
- [ ] numerical differentiation
- [ ] root finding
- [ ] interpolation
- [ ] approximation
- [ ] numerical linear algebra
- [ ] error analysis
- [ ] numerical stability
- [ ] floating point arithmetic
- [ ] runge-kutta methods (rk4)
- [ ] euler methods
- [ ] heun’s method

**resources:**

- **turkish resources:**
  1. **buders – numerical analysis:** [youtube channel](https://www.youtube.com/@Buders) — turkish lectures on euler, runge-kutta (rk4), root finding, and numerical integration
- **video lectures:**
  1. **jeffrey chasnov – numerical methods for engineers (hkust):** [youtube playlist](https://www.youtube.com/playlist?list=PLkZjai-2Jcxn35XnijUtqqEg0Wi5Sn8ab) — rk4, ode solvers, and numerical stability for engineers
  2. **mit 18.085 computational science and engineering (prof. gilbert strang):** [youtube lecture series](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D) — numerical linear algebra and differential equation solvers
- **books, papers & repositories:**
  1. **numerical computing with matlab (cleve moler):** [mathworks.com/moler/chapters.html](https://www.mathworks.com/moler/chapters.html) — free chapters on floating-point math, ode solvers, and svd
  2. **what every computer scientist should know about floating-point arithmetic (david goldberg):** [free article (oracle docs)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) — essential read to understand fp32/fp16 precision loss and rounding errors in c++ and gpu code
  3. **numerical linear algebra (trefethen & bau):** [siam book page](https://my.siam.org/Store/Product/viewproduct/?ProductId=950) — numerical stability and matrix algorithms
  4. **conjugate gradient without the agonizing pain (jonathan richard shewchuk – cmu):** [cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf) — intuitive guide to the conjugate gradient method used for large sparse linear systems in slam (ceres/gtsam) and physics

#### 2.7 other mathematics topics

**core topics:**

- [ ] discrete mathematics
- [ ] graph theory
- [ ] combinatorics
- [ ] set theory
- [ ] mathematical logic
- [ ] information theory
- [ ] signal processing mathematics
- [ ] fourier analysis
- [ ] laplace transform
- [ ] z-transform
- [ ] complex numbers
- [ ] tensor algebra
- [ ] lie groups and lie algebras ($so(3)$, $se(3)$)

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları (şadi evren şeker) – discrete math & graph theory:** [sadievrenseker.com](https://sadievrenseker.com/) — turkish notes on sets, logic, combinatorics, and graph theory
  2. **buders – discrete mathematics:** [youtube channel](https://www.youtube.com/@Buders) — university-level discrete math lectures in turkish
- **video lectures:**
  1. **mit 6.042j mathematics for computer science (prof. tom leighton):** [youtube lecture series](https://www.youtube.com/playlist?list=PLB7540DEDD482705B) — proof techniques, graph theory, and discrete math for computer science
  2. **william fiset – graph theory playlist:** [youtube playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) — visual graph theory series before studying algorithms and path planning
  3. **brad osgood – the fourier transform and its applications (stanford ee261):** [youtube lecture series](https://www.youtube.com/playlist?list=PLB24BC7956EE040CD) — fourier transforms for image processing and signal analysis
  4. **mit 6.003 signals and systems (prof. dennis freeman):** [youtube lecture series](https://www.youtube.com/playlist?list=PL41692B571DD0AF9B) — laplace and z-transforms, filtering, and frequency domain
  5. **eigenchris – tensors for beginners & lie groups:** [youtube playlist](https://www.youtube.com/playlist?list=PLJHszsWbB6hrkmmq57lX8BV-o-YIOFsiG) — tensor algebra and differential geometry
  6. **welch labs – imaginary numbers are real:** [youtube playlist](https://www.youtube.com/playlist?list=PLiaHhY2iBX9g6KIvZ_703G3KJXapKkNaF) — visual intuition for complex numbers
- **books, papers & repositories:**
  1. **a micro lie theory for state estimation in robotics (joan solà et al.):** [arxiv:1812.01537 (free pdf)](https://arxiv.org/pdf/1812.01537.pdf) — clear practical paper explaining $so(3)$ and $se(3)$ lie groups for robotics and slam engineers
  2. **lie groups for 2d and 3d transformations (ethan eade):** [ethaneade.com/lie.pdf](https://ethaneade.com/lie.pdf) — handbook on 3d transformation matrices and exponential maps
  3. **optimization on smooth manifolds (nicolas boumal):** [nicolasboumal.net/book](https://www.nicolasboumal.net/book/) — open-source textbook on differentiation and gradient descent on lie groups ($so(3), se(3)$) and riemannian manifolds
  4. **mathematics for computer science (lehman, leighton, meyer – mit):** [free pdf](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) — mit's official discrete mathematics textbook
  5. **the scientist and engineer's guide to digital signal processing (steven w. smith):** [dspguide.com](https://www.dspguide.com/pdfbook.htm) — free practical book on sensor filtering and dsp
  6. **information theory, inference, and learning algorithms (david mackay):** [inference.org.uk/itprnn/book.pdf](https://www.inference.org.uk/itprnn/book.pdf) — information theory (entropy, kl-divergence) and probabilistic inference

---

### 02. scientific computing & research engineering

#### 17.1 scientific computing

- [ ] numerical computing
- [ ] scientific python
- [ ] scipy
- [ ] numpy internals
- [ ] jax
- [ ] parallel computing
- [ ] numerical optimization
- [ ] simulation
- [ ] monte carlo simulation
- [ ] computational modeling

**resources:**

- **video lectures:**
  1. **steve brunton – scientific computing & data-driven engineering in python:** [youtube channel](https://www.youtube.com/@Eigensteve) — scientific computing, ode solvers, fft, and simulation
- **books, papers & repositories:**
  1. **python scientific lecture notes (scipy lectures):** [scipy-lectures.org](https://scipy-lectures.org/) — free engineering guide covering numpy internals (strides, broadcasting), scipy optimization, and speedup techniques
  2. **jax official documentation (autograd and xla – google):** [jax.readthedocs.io/en/latest/quickstart.html](https://jax.readthedocs.io/en/latest/quickstart.html) — autodiff (`grad`), vectorization (`vmap`), and jit compilation (`jit`) on gpu/tpu for fast scientific computing and mujoco mjx simulation

#### 17.2 research methodology

- [ ] scientific literature review
- [ ] paper reading
- [ ] research questions
- [ ] hypothesis formulation
- [ ] experimental design
- [ ] baseline models
- [ ] benchmarking
- [ ] ablation studies
- [ ] statistical significance
- [ ] reproducibility
- [ ] research writing (latex)
- [ ] technical documentation

**resources:**

- **video lectures:**
  1. **andrew ng (stanford cs230) – reading research papers:** [youtube video](https://www.youtube.com/watch?v=733m6qBH-jI) — how to read ai papers effectively and review literature
  2. **overleaf official latex tutorials:** [youtube playlist](https://www.youtube.com/playlist?list=PLPN-43XehstNCE7EzhxX513R2qmjbwc8K) — writing technical reports and papers in latex
- **books, papers & repositories:**
  1. **how to read a paper (prof. s. keshav – university of waterloo):** [ccr.sigcomm.org/online/files/p83-keshava.pdf (free 2-page pdf)](https://ccr.sigcomm.org/online/files/p83-keshavA.pdf) — three-pass technique to extract core ideas and math from papers quickly
  2. **learn latex in 30 minutes (overleaf documentation):** [overleaf.com/learn/latex/learn_latex_in_30_minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) — writing equations, algorithm blocks, and bibliographies (bibtex)

#### 17.3 advanced research areas

- [ ] representation learning
- [ ] geometric deep learning
- [ ] neural fields
- [ ] differentiable programming
- [ ] differentiable simulation
- [ ] physics-informed neural networks (pinn)
- [ ] neural operators
- [ ] self-supervised representation learning
- [ ] test-time adaptation
- [ ] continual learning
- [ ] robust machine learning
- [ ] uncertainty-aware ai

**resources:**

- **video lectures:**
  1. **steve brunton – physics-informed machine learning (piml & pinns):** [youtube playlist](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — embedding differential equations and physical laws into neural network losses and architectures
  2. **prof. michael bronstein (oxford) – geometric deep learning course:** [youtube lecture series](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — deep learning on symmetries, equivariance, groups, graphs, and 3d manifolds
- **books, papers & repositories:**
  1. **geometric deep learning: grids, groups, graphs, geodesics, and gauges (bronstein, bruna, cohen, veličković):** [geometricdeeplearning.com (free pdf)](https://geometricdeeplearning.com/) — book unifying cnns, gnns, and transformers under one geometric framework
  2. **physics-informed neural networks – pinns (maziar raissi et al.):** [maziarraissi.github.io/pinns](https://maziarraissi.github.io/PINNs/) — papers and code for physics-informed deep learning

#### 17.4 graduate-level specializations

- [ ] computer vision
- [ ] robotics
- [ ] autonomous systems
- [ ] machine learning
- [ ] artificial intelligence
- [ ] 3d computer vision
- [ ] control systems
- [ ] computer science
- [ ] embedded ai
- [ ] computational imaging

**resources:**

- **books, papers & repositories:**
  1. **csrankings (prof. emery berger):** [csrankings.org](https://csrankings.org/#/fromyear/2016/toyear/2026/index?ai&vision&mlmining&robotics&world) — tool to find universities and research labs by cvpr, icra, iros, and neurips publication output
  2. **arxiv computer science (`cs.ro` & `cs.cv`):** [arxiv.org/list/cs.ro/recent](https://arxiv.org/list/cs.RO/recent) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — daily robotics and computer vision preprints
  3. **hugging face daily papers & connected papers:** [huggingface.co/papers](https://huggingface.co/papers) · [connectedpapers.com](https://www.connectedpapers.com/) — visual citation graphs and trending ai papers
