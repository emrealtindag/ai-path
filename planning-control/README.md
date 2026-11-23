# planning and control

engineering curriculum, mathematical modeling, algorithmic optimization, and curated resources for trajectory planning, optimal control, and autonomous navigation.

---

## architecture overview

planning and control transforms high-level goals into safe, executable motor commands:

```
[global map & target goal]
             │
             ▼
[global path search: a* / rrt*]
             │
             ▼
[trajectory optimization: minimum snap / b-spline]
             │
             ▼
[local reactive controller: mpc / cbf / stanley]
             │
             ▼
[actuator commands: velocity / torque / thrust]
```

---

## study checklist

### 01. classical feedback control
- [ ] linear time-invariant (lti) systems: laplace transforms, transfer functions, and block diagrams
- [ ] time-domain specifications: rise time, settling time, overshoot, and steady-state error
- [ ] frequency response: bode plots, nyquist stability criterion, gain and phase margins
- [ ] pid controllers: proportional-integral-derivative tuning, anti-windup, derivative filtering, and feedforward control

### 02. modern state-space and optimal control
- [ ] state-space representations: $\dot{x} = ax + bu$, $y = cx + du$
- [ ] system properties: controllability and observability gramians, pole placement via ackermann's formula
- [ ] lyapunov stability: direct and indirect methods, control lyapunov functions (clf)
- [ ] linear quadratic regulator (lqr): continuous and discrete algebraic riccati equation (care / dare)
- [ ] linear quadratic gaussian (lqg): separation principle and kalman filter state feedback

### 03. model predictive control (mpc)
- [ ] receding horizon principle: finite-horizon optimization with state and input inequality constraints
- [ ] quadratic programming (qp) formulation and interior-point / active-set solvers (osqp, qpoases)
- [ ] nonlinear mpc (nmpc): direct multiple shooting, generalized gauss-newton, and acados integration
- [ ] control barrier functions (cbf): forward invariance and safe control filtering under dynamic constraints

### 04. path planning and trajectory generation
- [ ] configuration space (c-space): obstacles, Minkowski sums, and degrees of freedom
- [ ] graph search algorithms: breadth-first search (bfs), dijkstra, a*, weighted a*, dynamic d* lite
- [ ] sampling-based planners: rapidly-exploring random trees (rrt, rrt*), probabilistic roadmaps (prm)
- [ ] kinodynamic planning: state lattices, hybrid a*, and motion primitives satisfying nonholonomic constraints
- [ ] continuous trajectory optimization: minimum jerk and minimum snap polynomial splines, b-splines, and mppi (model predictive path integral)

---

## curated resources

### video lectures & course series
- [brian douglas – control system lectures & autonomous navigation](https://www.youtube.com/@ControlLectures): world-renowned video lectures demystifying classical control, root locus, bode plots, and state-space control.
- [steve brunton – control bootcamp](https://www.youtube.com/playlist?list=PLmB_c4VuNR85xX3nI2tG_iLpWpS8Lp1cE): applied modern control theory, state-space models, lqr, and robust control with python and matlab examples.
- [cmu 16-782 – planning and decision making in robotics (prof. maxim likhachev)](https://www.cs.cmu.edu/~maxim/classes/robotplanning/): academic masterclass on search-based planning, heuristic design, and dynamic replanning by the creator of d* lite.

### foundational books & academic materials
- [feedback systems: an introduction for scientists and engineers (karl johan åström & richard m. murray)](https://fbsbook.org/): freely available standard reference for feedback control, state-space methods, and frequency analysis.
- [principles of robot motion: theory, algorithms, and implementations (howie choset et al.)](https://mitpress.mit.edu/9780262033275/principles-of-robot-motion/): rigorous textbook covering configuration spaces, potential fields, sampling-based planning, and trajectory tracking.
- [trajectory generation for quadrotor uavs (charles richter, adam bry, nicholas roy – isrr)](https://dspace.mit.edu/handle/1721.1/107774): seminal research paper detailing polynomial trajectory generation and continuous-time collision avoidance.

### open-source codebases & tools
- [acados/acados](https://github.com/acados/acados): fast and embedded modern c solvers for nonlinear model predictive control and moving horizon estimation.
- [ompl/ompl](https://github.com/ompl/ompl): open motion planning library containing state-of-the-art implementations of sampling-based planners (rrt*, prm, est).
- [osqp/osqp](https://github.com/osqp/osqp): operator splitting quadratic program solver benchmarked for real-time optimal control and mpc.
- [atsushisakai/pythonrobotics](https://github.com/AtsushiSakai/PythonRobotics): reference implementations of autonomous navigation algorithms (a*, rrt*, mpc, stanley).
