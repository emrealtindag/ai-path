# planning, control, and symbolic reasoning

engineering curriculum, mathematical modeling, algorithmic optimization, classical ai planning, and curated resources for trajectory planning, optimal control, and autonomous navigation.

---

## architecture overview

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

## complete checklist and resources

### 01. control theory

#### 9.1 classical control

- [ ] system modeling
- [ ] transfer functions
- [ ] laplace transform
- [ ] block diagrams
- [ ] feedback systems
- [ ] open-loop control
- [ ] closed-loop control
- [ ] pid controllers
- [ ] stability
- [ ] root locus
- [ ] bode plots
- [ ] nyquist stability criterion
- [ ] frequency response

**resources:**

- **turkish resources:**
  1. **metu ee302 – feedback systems (prof. m. mert ankaralı):** [course page](https://blog.metu.edu.tr/mertan/) — classical feedback control course notes
- **video lectures:**
  1. **brian douglas – control systems lectures:** [youtube channel](https://www.youtube.com/@BrianBDouglas) & [official archive](https://engineeringmedia.com/) — visual explanations of pid, bode plots, nyquist criterion, and root locus
- **books, papers & repositories:**
  1. **feedback control of dynamic systems (franklin, powell, emami-naeini):** [book page](https://www.pearson.com/en-us/subject-catalog/p/feedback-control-of-dynamic-systems/P200000003242) — standard textbook on control system design
  2. **modern control engineering (katsuhiko ogata):** classic textbook for control engineering

#### 9.2 modern control

- [ ] state-space representation
- [ ] state transition matrix
- [ ] controllability
- [ ] observability
- [ ] pole placement
- [ ] linear quadratic regulator (lqr)
- [ ] linear quadratic gaussian (lqg)
- [ ] state feedback
- [ ] optimal control

**resources:**

- **turkish resources:**
  1. **metu ee402 – discrete-time control systems (prof. m. mert ankaralı):** [course page](https://blog.metu.edu.tr/mertan/) & [youtube channel](https://www.youtube.com/@technicaltutorials8909) — discrete-time state-space control, state feedback, and observer design
- **video lectures:**
  1. **steve brunton – control bootcamp:** [youtube playlist](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m) — 20 short lectures on state-space control, controllability, lqr, lqg, and kalman filtering
  2. **brian douglas – state-space & modern control:** [youtube playlist](https://www.youtube.com/playlist?list=PLUMWjy5jgHK3j74Z5Tq6Tso1fSfVWZC8L) — intuitive guide to state-space equations
- **books, papers & repositories:**
  1. **data-driven science and engineering – ch. 8 (brunton & kutz):** [free pdf](https://databookuw.com/databook.pdf) — modern state-space control, lqr, and lqg
  2. **feedback systems (åström & murray):** [free pdf](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers) — free standard textbook on state-space feedback control

#### 9.3 advanced control

- [ ] model predictive control (mpc)
- [ ] nonlinear control
- [ ] adaptive control
- [ ] robust control
- [ ] sliding mode control
- [ ] gain scheduling
- [ ] trajectory tracking & geometric control (se(3))
- [ ] optimal trajectory generation
- [ ] stochastic control
- [ ] distributed control
- [ ] model predictive path integral (mppi) & gpu optimal control
- [ ] dynamical systems (ds) & stable reactive control (epfl lasa)

**resources:**

- **video lectures:**
  1. **steve brunton & matlab tech talks – mpc explained:** [youtube playlist](https://www.youtube.com/playlist?list=PLn8PRpmsu08ozoeoXgxPSBKLyd4YEHww8) — how model predictive control optimizes trajectories under constraints
  2. **mit 6.832 – underactuated robotics (russ tedrake):** [youtube lecture series](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — nonlinear control, lqr, mpc, lyapunov stability, and trajectory optimization
  3. **eth zürich – flying machine arena (raffaello d'andrea):** [youtube talks](https://www.youtube.com/results?search_query=raffaello+d%27andrea+quadrocopter+control) — nonlinear control for high-agility autonomous quadrotors
- **books, papers & repositories:**
  1. **underactuated robotics (russ tedrake – mit):** [free interactive book & notebooks](https://underactuated.csail.mit.edu/) — open interactive textbook for uav and robot control
  2. **predictive control for linear & hybrid systems (borrelli, bemporad, morari):** [free pdf](https://www.mpc.berkeley.edu/mpc-course-material) — standard mathematical textbook for mpc
  3. **commaai/openpilot:** [github repo](https://github.com/commaai/openpilot) — production c++/python mpc and kalman filter controllers under `selfdrive/controls`
  4. **casadi & acados:** [web.casadi.org](https://web.casadi.org/) · [docs.acados.org](https://docs.acados.org/) — standard c++/python solvers for real-time embedded nonlinear mpc (nmpc)
  5. **kr_mav_control (upenn grasp lab):** [github repo](https://github.com/KumarRobotics/kr_mav_control) — c++ $so(3)/se(3)$ geometric quadrotor tracking control avoiding gimbal lock during aggressive flight
  6. **rosplane & vtolsim (byu magicc lab):** [rosplane](https://github.com/byu-magicc/rosplane) · [vtolsim](https://github.com/byu-magicc/vtolsim) — c++/ros autopilot implementing beard & mclain fixed-wing and vtol flight control
  7. **mppi control (mit acl):** [github repo](https://github.com/mit-acl/mppi_numba) — gpu-accelerated stochastic mppi trajectory optimization with cuda/numba
  8. **dynamical systems for robot control (epfl lasa):** [epfl-lasa.github.io](https://epfl-lasa.github.io/) · [github](https://github.com/epfl-lasa) · [seds](https://github.com/epfl-lasa/icra-lfd-tutorial) — reactive lyapunov-stable control and learning from demonstration libraries

#### 9.4 autonomous motion

- [ ] trajectory generation
- [ ] trajectory optimization
- [ ] path tracking (pure pursuit, stanley controller)
- [ ] velocity control
- [ ] motion constraints
- [ ] dynamic constraints
- [ ] collision avoidance
- [ ] model-based planning

**resources:**

- **video lectures:**
  1. **brian douglas – autonomous navigation & path tracking:** [youtube playlist](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg) — fundamentals of pure pursuit, stanley controller, and path tracking
  2. **eth zürich – motion control for mobile robots:** [course page](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots.html) — kinematic constraints and trajectory tracking
- **books, papers & repositories:**
  1. **pythonrobotics (path tracking):** [github repo](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — clean animated python code for pure pursuit, stanley, lqr, and mpc path tracking
  2. **self-driving cars specialization (university of toronto):** [coursera](https://www.coursera.org/specializations/self-driving-cars) — lateral (stanley/pure pursuit) and longitudinal vehicle control equations
  3. **trajectory planning for automatic machines & robots:** [book page](https://link.springer.com/book/10.1007/978-3-540-85629-0) — smooth polynomial trajectories bounded by velocity, acceleration, and jerk/snap

---

### 02. path planning & decision making

#### 11.1 classical path planning

- [ ] configuration space (c-space)
- [ ] grid-based planning
- [ ] breadth-first search (bfs)
- [ ] dijkstra
- [ ] a*
- [ ] d* lite
- [ ] rrt (rapidly-exploring random trees)
- [ ] rrt*
- [ ] prm (probabilistic roadmaps)
- [ ] potential fields
- [ ] visibility graphs

**resources:**

- **video lectures:**
  1. **brian douglas – autonomous navigation path planning:** [youtube video](https://www.youtube.com/watch?v=Fw8JQ5Q-ZwU) — fast clear overview of a*, rrt, and potential fields
  2. **cmu 16-782 – planning and decision making in robotics (maxim likhachev):** [course page](https://www.cs.cmu.edu/~maxim/classes/robotplanning/) & [youtube search](https://www.youtube.com/results?search_query=maxim+likhachev+search+based+planning) — lectures on a*, weighted a*, ara*, and d* lite by the algorithm's creator
  3. **mit 16.410 – principles of autonomy & decision making:** [mit ocw course page](https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/) — autonomy planning for aerospace systems
- **books, papers & repositories:**
  1. **pythonrobotics (path planning):** [github repo](https://github.com/AtsushiSakai/PythonRobotics#path-planning) — runnable python simulations of dijkstra, a*, d* lite, prm, rrt, and rrt*
  2. **planning algorithms (steven m. lavalle):** [free pdf](https://lavalle.pl/planning/) — classic free textbook on c-space and motion planning by the inventor of rrt

#### 11.2 motion planning

- [ ] configuration space planning
- [ ] collision checking
- [ ] trajectory planning
- [ ] sampling-based planning
- [ ] optimization-based planning (chomp, trajopt)
- [ ] kinodynamic planning & online replanning
- [ ] time-optimal planning
- [ ] safe motion planning
- [ ] graph-based exploration (gbplanner) & darpa subt autonomy
- [ ] fast & safe trajectory planning beyond sensor horizon (faster)
- [ ] ego-planner & gcopter (zju fast lab) trajectory optimization
- [ ] autonomous volumetric exploration & swarm planning (fuel & racer)

**resources:**

- **video lectures:**
  1. **prof. dmitry berenson – motion planning lectures:** [youtube search](https://www.youtube.com/results?search_query=dmitry+berenson+motion+planning) — collision checking, sampling-based planning, chomp, and trajopt
  2. **prof. fei gao (zju fast lab) & boyu zhou – autonomous uav planning:** [youtube search](https://www.youtube.com/results?search_query=fei+gao+fast+lab+motion+planning) — b-spline trajectory optimization, esdf-free planning, and frontier exploration
  3. **prof. russ tedrake (mit 6.832) – trajectory optimization:** [youtube playlist](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — direct collocation and kinodynamic trajectory optimization under nonlinear constraints
- **books, papers & repositories:**
  1. **ompl (open motion planning library):** [ompl.kavrakilab.org](https://ompl.kavrakilab.org/) & [github repo](https://github.com/ompl/ompl) — pure c++ sampling-based and kinodynamic motion planners powering ros 2 moveit 2
  2. **principles of robot motion (choset, lynch, hutchinson):** [book page](https://mitpress.mit.edu/9780262033275/principles-of-robot-motion/) — comprehensive textbook on robot motion theory
  3. **kr_autonomous_flight (upenn grasp lab):** [github repo](https://github.com/KumarRobotics/kr_autonomous_flight) — complete c++ gps-denied quadrotor autonomy stack combining mapping, online replanning, and $se(3)$ control
  4. **gbplanner_ros & mbplanner_ros (ntnu arl):** [gbplanner_ros](https://github.com/ntnu-arl/gbplanner_ros) & [mbplanner_ros](https://github.com/ntnu-arl/mbplanner_ros) — darpa subterranean challenge winning volumetric exploration planners for uavs and quadrupeds
  5. **faster (mit acl):** [github repo](https://github.com/mit-acl/faster) — miqp-based c++ trajectory planner guaranteeing safe high-speed drone flight in unknown cluttered spaces
  6. **ego-planner & gcopter (zju fast lab):** [ego-planner](https://github.com/ZJU-FAST-Lab/ego-planner) · [gcopter](https://github.com/ZJU-FAST-Lab/GCOPTER) — fast c++ drone trajectory planners avoiding esdf computation for dense forest flight and swarms
  7. **fuel & racer (hkust / cuhk):** [fuel](https://github.com/HKUST-Aerial-Robotics/FUEL) & [racer](https://github.com/Robotics-STAR-Lab/RACER) — hierarchical frontier-based fast drone exploration and decentralized multi-uav planning

#### 11.3 decision making

- [ ] finite state machines (fsm)
- [ ] behavior trees (bt)
- [ ] rule-based systems
- [ ] decision theory
- [ ] markov decision processes (mdp)
- [ ] partially observable markov decision processes (pomdp)
- [ ] hierarchical planning
- [ ] task and motion planning (tamp)

**resources:**

- **video lectures:**
  1. **petter ögren – behavior trees in robotics & ai:** [youtube channel](https://www.youtube.com/@PetterOgren/videos) — why finite state machines fail at scale and how behavior trees modularize robot decisions
  2. **behaviortree.cpp & groot2 tutorials:** [behaviortree.dev/docs/intro](https://www.behaviortree.dev/docs/intro) — coding behavior trees in c++ and ros 2
- **books, papers & repositories:**
  1. **behavior trees in robotics and ai (colledanchise & ögren):** [arxiv:1709.00084 (free pdf)](https://arxiv.org/pdf/1709.00084.pdf) — clear reference book on autonomous task management with behavior trees
  2. **algorithms for decision making (kochenderfer et al.):** [free pdf](https://algorithmsbook.com/files/dm.pdf) — free mit press book on mdps, pomdps, and decision making under uncertainty
  3. **behaviortree.cpp & nav2:** [behaviortree.cpp](https://github.com/BehaviorTree/BehaviorTree.CPP) · [navigation2](https://github.com/ros-planning/navigation2) — c++17 behavior tree library used inside ros 2 nav2

#### 11.4 multi-agent systems

- [ ] multi-robot coordination
- [ ] distributed decision making
- [ ] multi-agent planning
- [ ] cooperative robotics
- [ ] swarm intelligence
- [ ] multi-agent reinforcement learning (marl)
- [ ] decentralized swarm trajectory planning (mader / rmader)

**resources:**

- **video lectures:**
  1. **prof. vijay kumar (grasp lab) – aerial swarm robotics:** [youtube talks](https://www.youtube.com/results?search_query=vijay+kumar+swarm+robotics+grasp+lab) — decentralized drone swarm coordination, formation control, and cooperative mapping
  2. **prof. jonathan p. how (mit acl) – decentralized multi-agent planning:** [youtube search](https://www.youtube.com/results?search_query=jonathan+how+mit+multi+agent+trajectory+planning) — asynchronous coordination, communication delays, and decentralized collision avoidance
- **books, papers & repositories:**
  1. **multiagent systems (shoham & leyton-brown):** [free pdf](http://www.masfoundations.org/mas.pdf) — algorithmic and game-theoretic foundations of multi-agent systems
- **books, papers & repositories:**
  1. **scrimmage multi-agent simulator (gtri):** [github repo](https://github.com/gtri/scrimmage) & [docs](https://gtri.github.io/scrimmage/sphinx/html/index.html) — c++/python simulator for large drone swarms and multi-agent reinforcement learning
  2. **mader & robust-mader (mit acl):** [mader](https://github.com/mit-acl/mader) & [rmader](https://github.com/mit-acl/rmader) — decentralized asynchronous multi-uav trajectory planner handling communication delays

---

### 03. classical ai

#### 27.1 search & problem solving

- [ ] uninformed search (bfs, dfs, iterative deepening)
- [ ] informed search (greedy, a*, ida*)
- [ ] admissible and consistent heuristics
- [ ] heuristic design
- [ ] local search (hill climbing, simulated annealing)
- [ ] beam search
- [ ] adversarial search (minimax, alpha-beta pruning)
- [ ] monte carlo tree search
- [ ] constraint satisfaction problems (csp)
- [ ] arc consistency (ac-3)
- [ ] backtracking with forward checking

#### 27.2 logic & automated reasoning

- [ ] propositional logic
- [ ] first-order logic
- [ ] resolution and unification
- [ ] forward and backward chaining
- [ ] prolog
- [ ] datalog
- [ ] answer set programming
- [ ] non-monotonic reasoning
- [ ] sat solvers (cdcl)
- [ ] smt solvers (z3)
- [ ] automated theorem proving
- [ ] formal verification basics

#### 27.3 knowledge representation

- [ ] semantic networks and frames
- [ ] ontologies (owl)
- [ ] rdf and sparql
- [ ] description logics
- [ ] knowledge graphs
- [ ] knowledge graph embeddings (transe, rotate)
- [ ] rule-based expert systems
- [ ] commonsense knowledge bases (conceptnet)
- [ ] neuro-symbolic integration

#### 27.4 automated planning

- [ ] strips
- [ ] pddl
- [ ] planning graphs (graphplan)
- [ ] heuristic planners (ff, fast downward)
- [ ] hierarchical task networks (htn)
- [ ] temporal planning
- [ ] contingent and probabilistic planning
- [ ] plan execution and monitoring
- [ ] llm + pddl planning

#### 27.5 game ai

- [ ] expectiminimax
- [ ] counterfactual regret minimization
- [ ] chess engines (stockfish, nnue)
- [ ] alphago and alphazero
- [ ] utility ai
- [ ] goal-oriented action planning (goap)
- [ ] procedural content generation

#### 27.6 intelligent agents & multi-agent theory

- [ ] agent types (reflex, goal-based, utility-based)
- [ ] bdi architecture
- [ ] cognitive architectures (soar, act-r)
- [ ] auctions and negotiation
- [ ] mechanism design
- [ ] coalition formation
- [ ] agent communication protocols

**resources:**

- **turkish resource:** [bilgisayar kavramları (şadi evren şeker) — ai search & symbolic logic (youtube)](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — turkish intro to search algorithms, a*, minimax, and expert systems
- **video lectures:**
  1. [uc berkeley cs188 — introduction to artificial intelligence](https://www.youtube.com/playlist?list=PLp8QV47qJEg67UTShQ4er4RYQ3rOeDKxv) — classic course on a*, heuristics, csp, minimax, mcts, and mdps
  2. [harvard cs50’s introduction to ai with python (youtube)](https://www.youtube.com/watch?v=5NgNicANyqM) — practical python walkthrough of search, logic, probability, and optimization
- **books, papers & repositories:**
  1. [russell & norvig — aima & aima-python (github)](https://github.com/aimacode/aima-python) — standard textbook and python code repository for search, logic, and planning
  2. [plansys2 (ros 2 planning system, github)](https://github.com/PlanSys2/ros2_planning_system) — connects pddl symbolic task planning directly to ros 2 robots
  3. [z3 theorem prover (microsoft research, github)](https://github.com/Z3Prover/z3) — standard smt solver for constraint solving and formal verification
