# robotics and embodied ai

engineering curriculum, mathematical modeling, middleware, physical ai, robotics foundation models, and curated resources for robot kinematics, rigid-body dynamics, ros 2, and physical simulation.

---

## architecture overview

```
[task / mission specification]
             │
             ▼
  [motion planning: c-space / rrt*]
             │
             ▼
  [kinematics & dynamics: jacobians / lagrangian]
             │
             ▼
  [middleware & coordination: ros 2 / tf2 / dds]
             │
             ▼
  [simulation & real-world: gazebo / isaac sim / hardware]
```

---

## complete checklist and resources

### 01. robotics

#### 8.1 robotics fundamentals

- [ ] robot types
- [ ] robot components
- [ ] degrees of freedom (dof)
- [ ] actuators
- [ ] motors (bldc, step, servo)
- [ ] encoders
- [ ] sensors
- [ ] coordinate frames
- [ ] robot configuration
- [ ] forward kinematics
- [ ] inverse kinematics
- [ ] workspace
- [ ] manipulators

**resources:**

- **video lectures:**
  1. **kevin lynch – modern robotics (northwestern university):** [youtube playlist](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — screw theory, configuration spaces, and modern robotics math
  2. **eth zürich – autonomous mobile robots (roland siegwart):** [youtube lecture series](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — mobile robotics lectures covering perception, kinematics, localization, and planning
- **books, papers & repositories:**
  1. **modern robotics: mechanics, planning, and control (lynch & park):** [free pdf](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf) — textbook paired with python/matlab/c++ robotics libraries
  2. **introduction to robotics (john j. craig):** [book page](https://www.pearson.com/en-us/subject-catalog/p/introduction-to-robotics-mechanics-and-control/P200000003304) — classic textbook on robot mechanics and control

#### 8.2 robot kinematics

- [ ] homogeneous transformation
- [ ] denavit-hartenberg (d-h) parameters
- [ ] forward kinematics
- [ ] inverse kinematics
- [ ] jacobian
- [ ] differential kinematics
- [ ] singularities
- [ ] redundant manipulators

**resources:**

- **video lectures:**
  1. **angela sodemann (robogrok) – robot kinematics & dh frames:** [youtube channel](https://www.youtube.com/@asodemann3) & [youtube search](https://www.youtube.com/results?search_query=angela+sodemann+robotics+kinematics) — step-by-step tutorials on homogeneous transforms, dh tables, and forward/inverse kinematics
  2. **kevin lynch – modern robotics ch. 4–6:** [youtube playlist](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — twists, velocity jacobians, and singularity analysis
- **books, papers & repositories:**
  1. **modern robotics – chapters 4, 5 & 6:** [free pdf](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf) — forward kinematics, velocity jacobians, and inverse kinematics
  2. **robot modeling and control (spong, hutchinson, vidyasagar):** [book page](https://www.wiley.com/en-us/Robot+Modeling+and+Control%2C+2nd+Edition-p-9781119523994) — classic textbook for dh parameterization and jacobian derivations

#### 8.3 robot dynamics

- [ ] newton-euler formulation
- [ ] lagrangian mechanics
- [ ] rigid body dynamics
- [ ] inertia tensor
- [ ] forces and torques
- [ ] dynamic modeling
- [ ] contact dynamics
- [ ] actuator dynamics
- [ ] fixed-wing & aerodynamic dynamics

**resources:**

- **video lectures:**
  1. **kevin lynch – modern robotics ch. 8 (dynamics of open chains):** [youtube playlist](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — lagrangian and newton-euler equations, inertia matrices $m(\theta)$, and coriolis forces
  2. **mit 6.832 – underactuated robotics (russ tedrake):** [youtube lecture series](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — modeling nonlinear dynamics for uavs, legged robots, and manipulators
  3. **steve brunton – lagrangian mechanics & robot dynamics:** [youtube search](https://www.youtube.com/results?search_query=steve+brunton+lagrangian+dynamics) — concise overview of analytical mechanics
- **books, papers & repositories:**
  1. **modern robotics – chapter 8 (dynamics of open chains):** [free pdf](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf)
  2. **rigid body dynamics algorithms (roy featherstone):** [book page](https://link.springer.com/book/10.1007/978-1-4899-7560-7) — algorithms powering physics engines like mujoco, pinocchio, and drake
  3. **stack-of-tasks/pinocchio:** [github repo](https://github.com/stack-of-tasks/pinocchio) — fast c++ library computing rigid-body kinematics and dynamics in microseconds
  4. **small unmanned aircraft (beard & mclain):** [book info](https://press.princeton.edu/books/hardcover/9780691149219/small-unmanned-aircraft) & [python simulator](https://github.com/byu-magicc/mavsim_public) — core uav textbook covering coordinate frames, aerodynamics, 12-state 6-dof dynamics, and autopilot loops

#### 8.4 robot operating system (ros / ros 2)

- [ ] ros fundamentals
- [ ] ros 2 architecture
- [ ] nodes
- [ ] topics
- [ ] services
- [ ] actions
- [ ] parameters
- [ ] launch files
- [ ] tf2 (transform library)
- [ ] urdf (unified robot description format)
- [ ] xacro
- [ ] rviz
- [ ] `rosbag`
- [ ] dds (data distribution service)
- [ ] lifecycle nodes
- [ ] ros 2 control
- [ ] navigation stack (nav2)
- [ ] moveit 2
- [ ] plotjuggler & real-time telemetry analysis

**resources:**

- **turkish resources:**
- **video lectures:**
  1. **articulated robotics (josh newans) – ros 2 guide:** [youtube playlist](https://www.youtube.com/playlist?list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT) — practical step-by-step series building a robot with urdf, tf2, `ros2_control`, gazebo, and nav2
  2. **the construct – ros 2 tutorials (c++ & python):** [youtube channel](https://www.youtube.com/@TheConstruct) — tutorials on lifecycle nodes, dds, qos profiles, and ros 2 patterns
- **books, papers & repositories:**
  1. **ros 2 official documentation (lyrical luth lts):** [docs.ros.org](https://docs.ros.org/en/lyrical/) & [release schedule](https://docs.ros.org/en/lyrical/The-ROS2-Project/Release-Schedule.html) — official installation and c++ (`rclcpp`) / python (`rclpy`) api reference
  2. **nav2 (ros 2 navigation stack):** [docs.nav2.org](https://docs.nav2.org/) & [github repo](https://github.com/ros-planning/navigation2) — mapping, localization (amcl), costmaps, and behavior tree navigation in c++
  3. **moveit 2:** [moveit.picknik.ai](https://moveit.picknik.ai/main/index.html) & [github repo](https://github.com/moveit/moveit2) — standard motion planning stack for robot arms and manipulators
  4. **plotjuggler (davide faconti):** [plotjuggler.io](https://www.plotjuggler.io/) & [github repo](https://github.com/PlotJuggler/PlotJuggler) — fast opengl visualizer for ros topics, udp telemetry streams, and rosbag debugging

#### 8.5 robot simulation

- [ ] gazebo / gazebo sim (ignition)
- [ ] nvidia isaac sim & isaaclab (gpu-parallel robot simulation)
- [ ] mujoco
- [ ] webots
- [ ] pybullet
- [ ] coppeliasim
- [ ] digital twins
- [ ] physics simulation
- [ ] sensor simulation
- [ ] hardware-in-the-loop (hil)
- [ ] software-in-the-loop (sitl)
- [ ] flightmare & uav simulation
- [ ] rotors & gazebo mav simulation
- [ ] aerial gym simulator & gpu-parallel aerial robotics
- [ ] drake (mit csail) & mathematical simulation

**resources:**

- **video lectures:**
  1. **articulated robotics – simulating a robot with gazebo & ros 2:** [youtube video](https://www.youtube.com/watch?v=laWn7_cj434) — adding physics, cameras, and lidar to urdf/xacro models in gazebo
  2. **nvidia developer – isaac sim & isaac ros:** [youtube search](https://www.youtube.com/results?search_query=nvidia+isaac+sim+tutorial+ros2) — ray-traced sensor simulation, synthetic data, and gpu-accelerated robotics
- **books, papers & repositories:**
  1. **gazebo sim official docs:** [gazebosim.org/docs](https://gazebosim.org/docs) — open-source physics and sensor simulator integrated with ros 2
  2. **nvidia isaac sim & isaaclab:** [docs](https://isaac-sim.github.io/IsaacLab/) & [github repo](https://github.com/isaac-sim/IsaacLab) — gpu-parallel simulation framework training thousands of robots simultaneously with rl
  3. **mujoco (deepmind):** [docs](https://mujoco.readthedocs.io/en/stable/overview.html) & [github repo](https://github.com/google-deepmind/mujoco) — fast c/c++ physics engine for contact dynamics and robot learning
  4. **px4 & ardupilot sitl simulation guides:** [px4 simulation](https://docs.px4.io/main/en/simulation/) · [ardupilot sitl](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) — testing flight stacks in gazebo/jsbsim without physical hardware
  5. **luckyengine & luckyrobots:** [github repo](https://github.com/luckyrobots/luckyrobots) & [docs](https://luckyrobots.readthedocs.io) — mujoco simulator with grpc python sdk and gymnasium interface for legged/humanoid robots
  6. **flightmare (uzh rpg):** [github repo](https://github.com/uzh-rpg/flightmare) — high-speed c++ quadrotor aerodynamics combined with photorealistic unity rendering for agile rl drone flight
  7. **rotors gazebo mav simulator (eth zürich):** [github repo](https://github.com/ethz-asl/rotors_simulator) & [wiki](https://github.com/ethz-asl/rotors_simulator/wiki) — modular gazebo multirotor models with realistic imu noise, sensors, and lee se(3) controller
  8. **aerial gym simulator (ntnu arl):** [github repo](https://github.com/ntnu-arl/aerial_gym_simulator) & [aerialgym.com](https://aerialgym.com/) — simulates thousands of multirotors in parallel on one gpu for aerial rl navigation
  9. **drake (mit csail):** [drake.mit.edu](https://drake.mit.edu/) & [github repo](https://github.com/RobotLocomotion/drake) — c++ modeling, contact dynamics, trajectory optimization, lqr, and lyapunov control toolbox

#### 8.6 robot perception

- [ ] camera perception
- [ ] lidar perception
- [ ] radar perception
- [ ] sensor calibration (extrinsic camera-lidar, camera-imu)
- [ ] object detection
- [ ] object tracking
- [ ] 3d object detection
- [ ] semantic segmentation
- [ ] scene understanding
- [ ] occupancy mapping
- [ ] 2.5d elevation mapping & traversability (gpu-accelerated)
- [ ] direct targetless camera-lidar extrinsic calibration

**resources:**

- **video lectures:**
  1. **cyrill stachniss – mobile sensing and robotics:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — lidar processing, octomap occupancy grid mapping, and sensor calibration
  2. **eth zürich – autonomous mobile robots (perception & mapping):** [youtube lecture series](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — visual and laser perception pipelines for mobile robots
- **books, papers & repositories:**
  1. **autoware universe perception stack:** [docs](https://autowarefoundation.github.io/autoware-documentation/main/) & [github repo](https://github.com/autowarefoundation/autoware.universe) — ros 2 c++ camera-lidar-radar fusion, 3d object detection, and occupancy mapping
  2. **nvidia isaac ros perception (nitros):** [nvidia-isaac-ros.github.io](https://nvidia-isaac-ros.github.io/) — gpu/tensorrt accelerated ros 2 packages for stereo depth and visual slam
  3. **ethz-asl/kalibr:** [github repo](https://github.com/ethz-asl/kalibr) — standard toolbox for multi-camera and camera-imu spatiotemporal calibration
  4. **elevation_mapping_cupy (eth zürich):** [github repo](https://github.com/leggedrobotics/elevation_mapping_cupy) & [docs](https://leggedrobotics.github.io/elevation_mapping_cupy/) — 50+ hz gpu-accelerated terrain elevation and traversability mapping for rough terrain
  5. **wavemap (eth zürich asl):** [github repo](https://github.com/ethz-asl/wavemap) & [arxiv:2304.14813](https://arxiv.org/abs/2304.14813) — fast multi-resolution 3d occupancy mapping using wavelet compression in c++
  6. **direct_visual_lidar_calibration:** [github repo](https://github.com/koide3/direct_visual_lidar_calibration) — targetless c++/ros 2 extrinsic calibration between lidar and cameras

#### 8.7 robot learning

- [ ] learning from demonstration (lfd) & human-in-the-loop rl
- [ ] imitation learning
- [ ] behavior cloning
- [ ] inverse reinforcement learning
- [ ] reinforcement learning (rl)
- [ ] deep reinforcement learning (dqn, ppo, sac)
- [ ] sim-to-real transfer
- [ ] domain randomization
- [ ] robot foundation models
- [ ] airstack & field robotics sim-to-real stack
- [ ] diffusion policy & umi (stanford real lab)

**resources:**

- **video lectures:**
  1. **uc berkeley cs285 – deep reinforcement learning:** [youtube lecture series](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) & [course site](https://rail.eecs.berkeley.edu/deeprlcourse/) — imitation learning, behavior cloning, ppo, sac, and model-based rl
  2. **prof. shuran song – visuomotor policy learning & diffusion:** [youtube search](https://www.youtube.com/results?search_query=shuran+song+diffusion+policy+robotics) — learning multimodal robot action policies via diffusion models
- **books, papers & repositories:**
  1. **openai spinning up in deep rl:** [spinningup.openai.com](https://spinningup.openai.com/en/latest/) — clean math and pytorch starter guide for ppo, sac, and td3
  2. **robot learning from demonstration (survey):** [arxiv:1911.09052](https://arxiv.org/abs/1911.09052) — comprehensive survey on imitation learning algorithms
  3. **huggingface/lerobot:** [github repo](https://github.com/huggingface/lerobot) — pytorch toolkit for real-world robot imitation learning (act, diffusion policy) and rl
  4. **luckyrobots & lerobot sim2real bridge:** [github repo](https://github.com/luckyrobots/luckyrobots) & [tutorial](https://luckyrobots.github.io/lerobot-luckyengine-tutorial/) — collecting mujoco demos to train sim2real policies with lerobot
  5. **learning high-speed flight in the wild (uzh rpg):** [github repo](https://github.com/uzh-rpg/agile_autonomy) & [paper](https://www.science.org/doi/10.1126/scirobotics.abg5810) — zero-shot sim-to-real neural navigation flying autonomous drones through forests at 40 km/h
  6. **rlkit & softlearning (uc berkeley):** [rlkit](https://github.com/rail-berkeley/rlkit) · [softlearning](https://github.com/rail-berkeley/softlearning) — official codebases for sac, td3, and continuous-control robotics rl
  7. **hil-serl & serl (uc berkeley):** [hil-serl](https://github.com/rail-berkeley/hil-serl) · [serl](https://github.com/rail-berkeley/serl) · [project page](https://serl-robot.github.io/) — real-world human-in-the-loop reinforcement learning training robot assembly in 1-2 hours
  8. **rsl_rl (eth zürich):** [github repo](https://github.com/leggedrobotics/rsl_rl) — fast gpu-accelerated ppo library used for quadruped and humanoid locomotion in isaaclab
  9. **airstack (cmu airlab):** [github repo](https://github.com/castacks/AirStack) — ros 2 and isaac sim autonomy stack for field robots and uav sim-to-real transfer
  10. **diffusion policy (stanford / columbia):** [project page](https://diffusion-policy.cs.columbia.edu/) · [github repo](https://github.com/real-stanford/diffusion_policy) & [umi gripper](https://github.com/real-stanford/universal_manipulation_interface) — generating multimodal robot action trajectories with diffusion models

#### 8.8 robot applications

- [ ] industrial robotics
- [ ] collaborative robotics (cobots)
- [ ] mobile robotics (agv, amr)
- [ ] manipulation
- [ ] warehouse robotics
- [ ] service robotics
- [ ] medical robotics
- [ ] agricultural robotics
- [ ] assistive robotics
- [ ] humanoid robotics
- [ ] autonomous vehicles

**resources:**

- **video lectures:**
  1. **ieee spectrum robotics:** [youtube channel](https://www.youtube.com/@IEEESpectrum) — engineering coverage of industrial, medical, field, and humanoid robots
  2. **boston dynamics technical talks:** [youtube channel](https://www.youtube.com/@BostonDynamics) — talks on perception, mpc control, and planning for atlas and spot
- **books, papers & repositories:**
  1. **springer handbook of robotics:** [book page](https://link.springer.com/book/10.1007/978-3-319-32552-1) — comprehensive handbook across all robotics fields

---

### 02. advanced & emerging technologies

#### 19.1 advanced ai

- [ ] foundation models
- [ ] multimodal foundation models
- [ ] world models
- [ ] agentic ai
- [ ] test-time compute
- [ ] reasoning models (o1, deepseek-r1, etc.)
- [ ] neuro-symbolic ai
- [ ] continual learning
- [ ] self-supervised learning
- [ ] federated learning
- [ ] efficient ai
- [ ] small language models (slm)

**resources:**

- **video lectures:**
  1. **ai explained:** [youtube channel](https://www.youtube.com/@aiexplained-official) — grounded benchmark analysis of reasoning and foundation models
  2. **yannic kilcher:** [youtube channel](https://www.youtube.com/@YannicKilcher) — technical machine learning paper reviews
- **books, papers & repositories:**
  1. **world models (ha & schmidhuber):** [interactive article](https://worldmodels.github.io/) — classic article on learning compressed latent world models for planning
  2. **arxiv artificial intelligence (`cs.ai`) recent submissions:** [arxiv.org/list/cs.ai/recent](https://arxiv.org/list/cs.AI/recent)

#### 19.2 physical ai & embodied intelligence

- [ ] embodied ai
- [ ] robot foundation models
- [ ] vision-language-action models
- [ ] robot learning
- [ ] imitation learning
- [ ] reinforcement learning
- [ ] sim-to-real
- [ ] world models
- [ ] human-robot interaction
- [ ] autonomous manipulation

**resources:**

- **video lectures:**
  1. **bair robot learning seminars:** [youtube search](https://www.youtube.com/results?search_query=berkeley+robot+learning+embodied+ai)
  2. **stanford robotics center seminars:** [youtube channel](https://www.youtube.com/@stanfordonline) — talks on physical ai, vlas, and manipulation
- **books, papers & repositories:**
  1. **embodied ai workshop (cvpr):** [embodied-ai.org](https://embodied-ai.org/) — annual workshop talks and benchmarks on embodied ai simulators

#### 19.3 advanced robotics

- [ ] humanoid robotics
- [ ] whole-body control (wbc - locomotion & manipulation)
- [ ] humanoid foundation models (nvidia gr00t, gear-sonic)
- [ ] legged robotics (quadrupeds & sim2real actuator modeling)
- [ ] soft robotics
- [ ] swarm robotics
- [ ] medical robotics
- [ ] surgical robotics
- [ ] agricultural robotics
- [ ] assistive robotics
- [ ] autonomous mobile manipulation
- [ ] behavior-1k & omnigibson mobile manipulation
- [ ] mit mini cheetah software & convex mpc locomotion
- [ ] 6-dof robotic grasping detection (graspnet-1billion)
- [ ] articulated object manipulation & part perception (gapartnet)

**resources:**

- **video lectures:**
  1. **prof. russ tedrake (mit 6.4210 – robotic manipulation):** [youtube playlist](https://www.youtube.com/playlist?list=PLkx8KyIQkMfWr191lqbN8WfV08j-ui8WX) & [lecture notes](https://manipulation.csail.mit.edu/) — 6-dof point cloud grasping, contact mechanics, and manipulation control
  2. **prof. marco hutter (eth zürich) – legged robotics lectures:** [youtube search](https://www.youtube.com/results?search_query=marco+hutter+legged+robotics+lecture) — reduced-order models, convex mpc, whole-body control, and sim2real for quadrupeds
  3. **boston dynamics & unitree official channels:** [boston dynamics](https://www.youtube.com/@BostonDynamics) · [unitree](https://www.youtube.com/@UnitreeRobotics) — field demos of whole-body mpc and rl for quadrupeds and humanoids
  4. **ieee spectrum robotics:** [youtube channel](https://www.youtube.com/@IEEESpectrum)
- **books, papers & repositories:**
  1. **humanoid robotics: a reference:** [book page](https://link.springer.com/referencework/10.1007/978-94-007-6046-2) — bipedal balance (zmp), gait generation, and humanoid mechanics
- **books, papers & repositories:**
  1. **nvidia gr00t whole-body control:** [github repo](https://github.com/NVlabs/GR00T-WholeBodyControl) & [docs](https://nvlabs.github.io/GR00T-WholeBodyControl/) — combining lower-body rl locomotion with upper-body ik manipulation on humanoids
  2. **pace (eth zürich rsl):** [github repo](https://github.com/leggedrobotics/pace-sim2real) & [arxiv:2403.07663](https://arxiv.org/abs/2403.07663) — sim-to-real actuator system identification using standard joint encoders
  3. **behavior-1k, omnigibson & robosuite (stanford):** [project page](https://behavior.stanford.edu/) · [behavior-1k](https://github.com/StanfordVL/BEHAVIOR-1K) & [robosuite](https://github.com/ARISE-Initiative/robosuite) — photorealistic indoor mobile manipulation environments for embodied ai
  4. **mit mini cheetah software & convex mpc:** [github repo](https://github.com/mit-biomimetics/Cheetah-Software) — complete open-source c++ quadruped stack with convex mpc, whole-body impulse control, and state estimation
  5. **graspnet-1billion (sjtu mvig lab):** [github repo](https://github.com/graspnet/graspnet-baseline) & [graspnet.net](https://graspnet.net/) — 6-dof robotic grasping predictions directly from 3d point clouds
  6. **gapartnet (pku epic lab):** [github repo](https://github.com/PKU-EPIC/GAPartNet) & [project page](https://pku-epic.github.io/GAPartNet/) — 3d pose estimation and manipulation of articulated objects (cabinets, drawers, doors)

#### 19.4 advanced perception

- [ ] event-based cameras
- [ ] neuromorphic vision
- [ ] radar perception (4d imaging radar)
- [ ] thermal vision
- [ ] hyperspectral imaging
- [ ] multi-sensor perception
- [ ] 4d scene understanding
- [ ] dynamic 3d reconstruction

**resources:**

- **video lectures:**
  1. **rpg lab uzh (davide scaramuzza):** [youtube playlists](https://www.youtube.com/@ailabRPG/playlists) — high-speed uav perception fusing event-based cameras with rgb frames
- **books, papers & repositories:**
  1. **awesome event-based vision (uzh rpg):** [github repo](https://github.com/uzh-rpg/event-based_vision_resources) — curated papers, c++/python codebases, and simulators for neuromorphic cameras
  2. **4d imaging radar surveys (ieee):** [arxiv search](https://arxiv.org/search/?query=4D+imaging+radar+autonomous+driving&searchtype=all) — 4d mmwave radar perception complementing lidar in bad weather

#### 19.5 advanced computing

- [ ] neuromorphic computing
- [ ] quantum computing fundamentals
- [ ] photonic computing
- [ ] edge computing
- [ ] heterogeneous computing
- [ ] high performance computing (hpc)
- [ ] accelerated computing

**resources:**

- **video lectures:**
  1. **ibm technology & qiskit:** [qiskit youtube](https://www.youtube.com/@qiskit) · [ibm technology](https://www.youtube.com/@IBMTechnology) — heterogeneous computing, hpc, and quantum computing fundamentals
- **books, papers & repositories:**
  1. **ibm quantum learning:** [learning.quantum.ibm.com](https://learning.quantum.ibm.com/) — free intro to quantum information and algorithms

#### 19.6 advanced learning methods

- [ ] meta-learning & maml (learning to learn)
- [ ] few-shot learning
- [ ] lifelong learning
- [ ] active learning
- [ ] self-training
- [ ] domain adaptation
- [ ] causal machine learning
- [ ] reinforcement learning
- [ ] multi-agent reinforcement learning

**resources:**

- **video lectures:**
  1. **judea pearl – causal inference lectures:** [youtube search](https://www.youtube.com/results?search_query=judea+pearl+causal+inference+lecture) — correlation vs causality and intervention math
- **books, papers & repositories:**
  1. **meta-learning in neural networks: a survey:** [arxiv:2004.05439](https://arxiv.org/abs/2004.05439) — thorough survey on few-shot and meta-learning algorithms
  2. **maml & maml-rl (finn, abbeel, levine):** [arxiv:1703.03400](https://arxiv.org/abs/1703.03400) · [maml](https://github.com/cbfinn/maml) · [maml-rl](https://github.com/cbfinn/maml_rl) · [learn2learn](https://github.com/learnables/learn2learn) — foundational paper and pytorch repos for fast task adaptation in few-shot rl
  3. **causal inference in statistics: a primer (pearl et al.):** [book page](https://www.wiley.com/en-us/Causal+Inference+in+Statistics%3A+A+Primer-p-9781119186847) — concise math intro to causal graphs and inference

---

### 03. robotics foundation models literature

#### robotics

##### neural scaling laws
* neural scaling laws for embodied ai: neural scaling laws for embodied ai [[paper]](https://arxiv.org/abs/2405.14005)

##### robot policy learning for decision-making and controls
###### language-conditioned imitation learning
* cliport: what and where pathways for robotic manipulation [[paper]](https://arxiv.org/abs/2109.12098)[[project]](https://cliport.github.io/)[[code]](https://github.com/cliport/cliport)
* perceiver-actor: a multi-task transformer for robotic manipulation [[paper]](https://arxiv.org/abs/2209.05451)[[project]](https://peract.github.io/)[[code]](https://github.com/peract/peract)
* play-lmp: learning latent plans from play [[project]](https://learning-from-play.github.io/)
* multi-context imitation: language-conditioned imitation learning over unstructured data [[project]](https://language-play.github.io)

###### language-assisted reinforcement learning
* towards a unified agent with foundation models [[paper]](https://arxiv.org/abs/2307.09668)
* reward design with language models [[paper]](https://arxiv.org/abs/2303.00001)
* learning to generate better than your llm [[paper]](https://arxiv.org/pdf/2306.11816.pdf)[[code]](https://github.com/Cornell-RL/tril)
* guiding pretraining in reinforcement learning with large language models [[paper]](https://arxiv.org/abs/2302.06692)[[code]](https://github.com/yuqingd/ellm)
* motif: intrinsic motivation from artificial intelligence feedback [[paper]](https://arxiv.org/abs/2310.00166)[[code]](https://github.com/facebookresearch/motif)

##### language-image goal-conditioned value learning
* saycan: do as i can, not as i say: grounding language in robotic affordances [[paper]](https://arxiv.org/abs/2204.01691)[[project]](https://say-can.github.io/)[[code]](https://github.com/google-research/google-research/tree/master/saycan)
* zero-shot reward specification via grounded natural language [[paper]](https://proceedings.mlr.press/v162/mahmoudieh22a/mahmoudieh22a.pdf)
* voxposer: composable 3d value maps for robotic manipulation with language models [[project]](https://voxposer.github.io)
* vip: towards universal visual reward and representation via value-implicit pre-training [[paper]](https://arxiv.org/abs/2210.00030)[[project]](https://sites.google.com/view/vip-rl)
* liv: language-image representations and rewards for robotic control [[paper]](https://arxiv.org/abs/2306.00958)[[project]](https://penn-pal-lab.github.io/LIV/)
* lorel: learning language-conditioned robot behavior from offline data and crowd-sourced annotation [[paper]](https://arxiv.org/abs/2109.01115)[[project]](https://sites.google.com/view/robotlorel)
* text2motion: from natural language instructions to feasible plans [[paper]](https://arxiv.org/abs/2303.12153)[[project]](https://sites.google.com/stanford.edu/text2motion)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

##### robot task planning using large language models
* language models as zero-shot planners: extracting actionable knowledge for embodied agents [[paper]](https://arxiv.org/abs/2201.07207)[[project]](https://wenlong.page/language-planner/)
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* nl2tl: transforming natural languages to temporal logics using large language models [[paper]](https://arxiv.org/pdf/2305.07766.pdf)[[project]](https://yongchao98.github.io/MIT-realm-NL2TL/)[[code]](https://github.com/yongchao98/NL2TL)
* autotamp: autoregressive task and motion planning with llms as translators and checkers[[paper]](https://arxiv.org/abs/2306.06531)[[project]](https://yongchao98.github.io/MIT-REALM-AutoTAMP/)
* latte: language trajectory transformer [[paper]](https://arxiv.org/abs/2208.02918)[[code]](https://github.com/arthurfenderbucker/LaTTe-Language-Trajectory-TransformEr)
* planning with large language models via corrective re-prompting [[paper]](https://arxiv.org/abs/2211.09935)
* describe, explain, plan and select: interactive planning with llms enables open-world multi-task agents [[paper]](https://arxiv.org/pdf/2302.01560.pdf)[[code]](https://github.com/CraftJarvis/MC-Planner)
* jarvis-1: open-world multi-task agents with memory-augmented multimodal language models [[paper]](https://arxiv.org/pdf/2311.05997.pdf)[[project]](https://craftjarvis.github.io/JARVIS-1/)[[code]](https://github.com/CraftJarvis/JARVIS-1)
* an embodied generalist agent in 3d world [[paper]](https://arxiv.org/pdf/2311.12871.pdf)[[project]](https://embodied-generalist.github.io/)[[code]](https://github.com/embodied-generalist/embodied-generalist)
* llm+p: empowering large language models with optimal planning proficiency [[paper]](https://arxiv.org/pdf/2304.11477.pdf)[[code]](https://github.com/Cranial-XIX/llm-pddl)
* mp5: a multi-modal open-ended embodied system in minecraft via active perception [[paper]](https://arxiv.org/pdf/2312.07472.pdf)[[project]](https://iranqin.github.io/MP5.github.io/)[[code]](https://github.com/IranQin/MP5)

##### llm-based code generation
* progprompt: generating situated robot task plans using large language models [[paper]](https://arxiv.org/abs/2209.11302)[[project]](https://progprompt.github.io/)
* code as policies: language model programs for embodied control [[paper]](https://arxiv.org/abs/2209.07753)[[project]](https://code-as-policies.github.io/)
* chatgpt for robotics: design principles and model abilities [[paper]](https://arxiv.org/abs/2306.17582)[[project]](https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/chatgpt-for-robotics/)[[code]](https://github.com/microsoft/PromptCraft-Robotics)
* voyager: an open-ended embodied agent with large language models [[paper]](https://arxiv.org/abs/2305.16291)[[project]](https://voyager.minedojo.org/)
* visual programming: compositional visual reasoning without training [[paper]](https://arxiv.org/abs/2211.11559)[[project]](https://prior.allenai.org/projects/visprog)[[code]](https://github.com/allenai/visprog)
* deploying and evaluating llms to program service mobile robots [[paper]](https://arxiv.org/abs/2311.11183)[[project]](https://amrl.cs.utexas.edu/codebotler/)[[code]](https://github.com/ut-amrl/codebotler)

##### robot transformers
* motiongpt: finetuned llms are general-purpose motion generators [[paper]](https://arxiv.org/abs/2306.10900)[[project]](https://qiqiapink.github.io/MotionGPT/)
* rt-1: robotics transformer for real-world control at scale [[paper]](https://robotics-transformer.github.io/assets/rt1.pdf)[[project]](https://robotics-transformer.github.io/)[[code]](https://github.com/google-research/robotics_transformer)
* masked visual pre-training for motor control [[paper]](https://arxiv.org/abs/2203.06173)[[project]](https://tetexiao.com/projects/mvp)[[code]](https://github.com/ir413/mvp)
* real-world robot learning with masked visual pre-training [[paper]](https://arxiv.org/abs/2210.03109)[[project]](https://tetexiao.com/projects/real-mvp)
* r3m: a universal visual representation for robot manipulation [[paper]](https://arxiv.org/abs/2203.12601)[[project]](https://sites.google.com/view/robot-r3m/)[[code]](https://github.com/facebookresearch/r3m)
* robot learning with sensorimotor pre-training [[paper]](https://arxiv.org/abs/2306.10007)[[project]](https://robotic-pretrained-transformer.github.io/)
* rt-2: vision-language-action models transfer web knowledge to robotic control [[paper]](https://arxiv.org/abs/2307.15818)[[project]](https://robotics-transformer2.github.io/)
* pact: perception-action causal transformer for autoregressive robotics pre-training [[paper]](https://arxiv.org/abs/2209.11133)
* groot: learning to follow instructions by watching gameplay videos [[paper]](https://arxiv.org/pdf/2310.08235.pdf)[[project]](https://craftjarvis.github.io/GROOT/)[[code]](https://github.com/CraftJarvis/GROOT)
* behavior transformers (bet): cloning k modes with one stone [[paper]](https://arxiv.org/abs/2206.11251)[[project]](https://mahis.life/bet/)[[code]](https://github.com/notmahi/bet)
* conditional behavior transformers (c-bet), from play to policy: conditional behavior generation from uncurated robot data [[paper]](https://arxiv.org/abs/2210.10047)[[project]](https://play-to-policy.github.io/)[[code]](https://github.com/jeffacce/play-to-policy)
* magic vfm: meta-learning adaptation for ground interaction control with visual foundation models [[paper]](https://arxiv.org/abs/2407.12304)

##### in-context learning for decision-making
* a survey on in-context learning [[paper]](https://arxiv.org/abs/2301.00234)
* large language models as general pattern machines [[paper]](https://arxiv.org/abs/2307.04721)
* chain-of-thought predictive control [[paper]](https://arxiv.org/abs/2304.00776)
* react: synergizing reasoning and acting in language models [[paper]](https://arxiv.org/abs/2210.03629)
* icrt: in-context imitation learning via next-token prediction [[paper]](https://arxiv.org/abs/2408.15980) [[project]](https://icrt.dev/) [[code]](https://github.com/Max-Fu/icrt)

##### open-vocabulary robot navigation and manipulation
* cows on pasture: baselines and benchmarks for language-driven zero-shot object navigation [[paper]](https://arxiv.org/pdf/2203.10421.pdf)[[project]](https://cow.cs.columbia.edu/)
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* lsc: language-guided skill coordination for open-vocabulary mobile pick-and-place [[project]](https://languageguidedskillcoordination.github.io/)
* l3mvn: leveraging large language models for visual target navigation [[project]](https://arxiv.org/abs/2304.05501)
* open-world object manipulation using pre-trained vision-language models [[paper]](https://robot-moo.github.io/assets/moo.pdf)[[project]](https://robot-moo.github.io/)
* vima: general robot manipulation with multimodal prompts [[paper]](https://arxiv.org/abs/2210.03094)[[project]](https://vimalabs.github.io/)[[code]](https://github.com/vimalabs/VIMA)
* diffusion-based generation, optimization, and planning in 3d scenes [[paper]](https://arxiv.org/pdf/2301.06015.pdf)[[project]](https://scenediffuser.github.io/)[[code]](https://github.com/scenediffuser/Scene-Diffuser)
* lotus: continual imitation learning for robot manipulation through unsupervised skill discovery [[paper]](http://arxiv.org/abs/2311.02058) [[project]](https://ut-austin-rpl.github.io/Lotus/)
* imitating shortest paths in simulation enables effective navigation and manipulation in the real world [[paper]](https://arxiv.org/abs/2312.02976) [[project]](https://spoc-robot.github.io/)
* thinkbot: embodied instruction following with thought chain reasoning [[paper]](https://arxiv.org/abs/2312.07062) [[project]](https://guanxinglu.github.io/thinkbot/)
* clip-fields: weakly supervised semantic fields for robotic memory [[paper]](https://arxiv.org/abs/2210.05663) [[project]](https://mahis.life/clip-fields) [[code]](https://github.com/notmahi/clip-fields)
* usa-net: unified semantic and affordance representations for robot memory [[paper]](https://arxiv.org/abs/2304.12164) [[project]](https://usa.bolte.cc/) [[code]](https://github.com/codekansas/usa)

#### relevant to robotics (perception)

##### open-vocabulary object detection and 3d classification
* simple open-vocabulary object detection with vision transformers [[paper]](https://arxiv.org/pdf/2205.06230.pdf)[[code]](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit)
*  grounded language-image pre-training [[paper]](https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Grounded_Language-Image_Pre-Training_CVPR_2022_paper.pdf)[[code]](https://github.com/microsoft/GLIP)
*  grounding dino: marrying dino with grounded pre-training for open-set object detection [[paper]](https://arxiv.org/abs/2303.05499)[[code]](https://github.com/IDEA-Research/GroundingDINO)
*  pointclip: point cloud understanding by clip [[paper]](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_PointCLIP_Point_Cloud_Understanding_by_CLIP_CVPR_2022_paper.pdf)[[code]](https://github.com/ZrrSkywalker/PointCLIP)
*  point-bert: pre-training 3d point cloud transformers with masked point modeling [[paper]](https://arxiv.org/abs/2111.14819)[[code]](https://github.com/lulutang0608/Point-BERT)
*  ulip: learning a unified representation of language, images, and point clouds for 3d understanding [[paper]](https://arxiv.org/abs/2212.05171)[[project]](https://tycho-xue.github.io/ULIP/)[[code]](https://github.com/salesforce/ULIP)
*  ulip-2: towards scalable multimodal pre-training for 3d understanding [[paper]](https://arxiv.org/pdf/2305.08275.pdf)[[code]](https://github.com/salesforce/ULIP)
*  3d-vista: pre-trained transformer for 3d vision and text alignment [[paper]](https://arxiv.org/pdf/2308.04352.pdf)[[project]](https://3d-vista.github.io/)[[code]](https://github.com/3d-vista/3D-VisTA)

##### open-vocabulary semantic segmentation
* language-driven semantic segmentation [[paper]](https://arxiv.org/abs/2201.03546)[[code]](https://github.com/isl-org/lang-seg)
* emerging properties in self-supervised vision transformers [[paper]](https://arxiv.org/abs/2104.14294)[[code]](https://github.com/facebookresearch/dino)
* segment anything [[paper]](https://arxiv.org/abs/2304.02643)[[project]](https://segment-anything.com/)
* fast segment anything [[paper]](https://arxiv.org/abs/2306.12156)[[code]](https://github.com/CASIA-IVA-Lab/FastSAM)
* faster segment anything: towards lightweight sam for mobile applications [[paper]](https://arxiv.org/abs/2306.14289)[[code]](https://github.com/ChaoningZhang/MobileSAM)
* track anything: segment anything meets videos [[paper]](https://arxiv.org/abs/2304.11968)[[code]](https://github.com/gaomingqi/Track-Anything)

##### open-vocabulary 3d scene representations
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* clip-nerf: text-and-image driven manipulation of neural radiance fields [[paper]](https://arxiv.org/abs/2112.05139)[[project]](https://cassiepython.github.io/clipnerf/)
* clip-fields: weakly supervised semantic fields for robotic memory [[paper]](https://arxiv.org/abs/2210.05663) [[project]](https://mahis.life/clip-fields) [[code]](https://github.com/notmahi/clip-fields)
* lerf: language embedded radiance fields [[paper]](https://arxiv.org/abs/2303.09553)[[project]](https://www.lerf.io/)[[code]](https://github.com/kerrj/lerf)
* decomposing nerf for editing via feature field distillation [[paper]](https://arxiv.org/abs/2205.15585)[[project]](https://pfnet-research.github.io/distilled-feature-fields)

##### object representations
* foundationpose: unified 6d pose estimation and tracking of novel objects [[paper]](https://arxiv.org/abs/2312.08344)[[project]](https://nvlabs.github.io/FoundationPose/)
* bundlesdf: neural 6-dof tracking and 3d reconstruction of unknown objects [[paper]](https://arxiv.org/abs/2303.14158)[[project]](https://bundlesdf.github.io//)
* neural descriptor fields: se(3)-equivariant object representations for manipulation [[paper]](https://arxiv.org/abs/2112.05124)[[project]](https://yilundu.github.io/ndf/)
* distilled feature fields enable few-shot language-guided manipulation [[paper]](https://arxiv.org/abs/2308.07931)[[project]](https://f3rm.github.io/)
* you only look at one: category-level object representations for pose estimation from a single example [[paper]](https://arxiv.org/abs/2305.12626)
* zero-shot category-level object pose estimation [[paper]](https://arxiv.org/abs/2204.03635)[[code]](https://github.com/applied-ai-lab/zero-shot-pose)
* viola: imitation learning for vision-based manipulation with object proposal priors [[paper]](https://arxiv.org/abs/2210.11339)[[project]](https://ut-austin-rpl.github.io/VIOLA/)[[code]](https://github.com/UT-Austin-RPL/VIOLA)
* learning generalizable manipulation policies with object-centric 3d representations [[paper]](http://arxiv.org/abs/2310.14386)[[project]](https://ut-austin-rpl.github.io/GROOT/)[[code]](https://github.com/UT-Austin-RPL/GROOT)

##### affordance information
* affordance diffusion: synthesizing hand-object interactions [[paper]](https://arxiv.org/abs/2303.12538)[[project]](https://judyye.github.io/affordiffusion-www/)
* affordances from human videos as a versatile representation for robotics [[paper]](https://arxiv.org/abs/2304.08488)[[project]](https://robo-affordances.github.io/)

##### predictive models
* adversarial inverse reinforcement learning with self-attention dynamics model [[paper]](https://ieeexplore.ieee.org/document/9361118)
* connected autonomous vehicle motion planning with video predictions from smart, self-supervised infrastructure [[paper]](https://arxiv.org/pdf/2309.07504.pdf)
* self-supervised traffic advisors: distributed, multi-view traffic prediction for smart cities [[paper]](https://arxiv.org/abs/2204.06171)
* planning with diffusion for flexible behavior synthesis [[paper]](https://arxiv.org/abs/2205.09991)
* phenaki: variable-length video generation from open domain textual description [[paper]](https://arxiv.org/abs/2210.02399)
* robonet: large-scale multi-robot learning [[paper]](https://arxiv.org/abs/1910.11215)
* gaia-1: a generative world model for autonomous driving [[paper]](https://arxiv.org/abs/2309.17080)
* learning universal policies via text-guided video generation [[paper]](https://arxiv.org/abs/2302.00111)
* video language planning [[paper]](https://arxiv.org/abs/2310.10625)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

#### relevant to robotics (embodied ai)
* inner monologue: embodied reasoning through planning with language models [[paper]](https://arxiv.org/abs/2207.05608)[[project]](https://innermonologue.github.io/)
* statler: state-maintaining language models for embodied reasoning [[paper]](https://arxiv.org/abs/2306.17840)[[project]](https://statler-lm.github.io/)
* embodiedgpt: vision-language pre-training via embodied chain of thought [[paper]](https://arxiv.org/pdf/2305.15021.pdf)[[project]](https://embodiedgpt.github.io/)
* minedojo: building open-ended embodied agents with internet-scale knowledge [[paper]](https://openreview.net/forum?id=rc8o_j8I8PX)[[code]](https://github.com/MineDojo/MineDojo)
* video pretraining (vpt): learning to act by watching unlabeled online videos [[paper]](https://arxiv.org/abs/2206.11795)
* open-world multi-task control through goal-aware representation learning and adaptive horizon prediction [[paper]](https://arxiv.org/pdf/2301.10034.pdf)[[code]](https://github.com/CraftJarvis/MC-Controller)
* describe, explain, plan and select: interactive planning with llms enables open-world multi-task agents [[paper]](https://arxiv.org/pdf/2302.01560.pdf)[[code]](https://github.com/CraftJarvis/MC-Planner)
* voyager: an open-ended embodied agent with large language models [[paper]](https://arxiv.org/abs/2305.16291)[[project]](https://voyager.minedojo.org/)[[code]](https://github.com/MineDojo/Voyager)
* ghost in the minecraft: generally capable agents for open-world environments via large language models with text-based knowledge and memory [[paper]](https://arxiv.org/abs/2305.17144)[[project]](https://github.com/OpenGVLab/GITM)
* language models as zero-shot planners: extracting actionable knowledge for embodied agents [[paper]](https://arxiv.org/pdf/2201.07207.pdf)[[project]](https://wenlong.page/language-planner/)[[code]](https://github.com/huangwl18/language-planner)
* groot: learning to follow instructions by watching gameplay videos [[paper]](https://arxiv.org/pdf/2310.08235.pdf)[[project]](https://craftjarvis.github.io/GROOT/)[[code]](https://github.com/CraftJarvis/GROOT)
* jarvis-1: open-world multi-task agents with memory-augmented multimodal language models [[paper]](https://arxiv.org/pdf/2311.05997.pdf)[[project]](https://craftjarvis.github.io/JARVIS-1/)[[code]](https://github.com/CraftJarvis/JARVIS-1)
* sqa3d: situated question answering in 3d scenes [[paper]](https://arxiv.org/pdf/2210.07474.pdf)[[project]](https://sqa3d.github.io/)[[code]](https://github.com/SilongYong/SQA3D)
* mp5: a multi-modal open-ended embodied system in minecraft via active perception [[paper]](https://arxiv.org/pdf/2312.07472.pdf)[[project]](https://iranqin.github.io/MP5.github.io/)[[code]](https://github.com/IranQin/MP5)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

##### generalist ai
* generative agents: interactive simulacra of human behavior [[paper]](https://arxiv.org/abs/2304.03442)
* towards generalist robots: a promising paradigm via generative simulation [[paper]](https://arxiv.org/abs/2305.10455)
* a generalist agent [[paper]](https://arxiv.org/abs/2205.06175)
* an embodied generalist agent in 3d world [[paper]](https://arxiv.org/pdf/2311.12871.pdf)[[project]](https://embodied-generalist.github.io/)[[code]](https://github.com/embodied-generalist/embodied-generalist)

##### simulators
* gibson env: real-world perception for embodied agents [[paper]](https://arxiv.org/abs/1808.10654)
* igibson 2.0: object-centric simulation for robot learning of everyday household tasks [[paper]](https://arxiv.org/abs/2108.03272)[[project]](https://svl.stanford.edu/igibson/)
* behavior-1k: a benchmark for embodied ai with 1,000 everyday activities and realistic simulation [[paper]](https://openreview.net/forum?id=_8DoIe8G3t)[[project]](https://behavior.stanford.edu/behavior-1k)
* habitat: a platform for embodied ai research [[paper]](https://arxiv.org/abs/1904.01201)[[project]](https://aihabitat.org/)
* habitat 2.0: training home assistants to rearrange their habitat [[paper]](https://arxiv.org/abs/2106.14405)
* robothor: an open simulation-to-real embodied ai platform [[paper]](https://arxiv.org/abs/2004.06799)[[project]](https://ai2thor.allenai.org/robothor/)
* virtualhome: simulating household activities via programs [[paper]](https://arxiv.org/abs/1806.07011)
* arnold: a benchmark for language-grounded task learning with continuous states in realistic 3d scenes [[paper]](https://arxiv.org/pdf/2304.04321.pdf)[[project]](https://arnold-benchmark.github.io/)[[code]](https://github.com/arnold-benchmark/arnold)
* alfred: a benchmark for interpreting grounded instructions for everyday tasks [[paper]](https://arxiv.org/abs/1912.01734)[[project]](https://askforalfred.com/)[[code]](https://github.com/askforalfred/alfred)
* libero: benchmarking knowledge transfer in lifelong robot learning [[paper]](https://arxiv.org/pdf/2306.03310.pdf)[[project]](https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/overview.html)[[code]](https://github.com/Lifelong-Robot-Learning/LIBERO)
* procthor: large-scale embodied ai using procedural generation [[paper]](https://arxiv.org/abs/2206.06994)[[project]](https://procthor.allenai.org/)[[code]](https://github.com/allenai/procthor)
