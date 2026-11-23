# autonomy and flight

engineering curriculum, mathematical modeling, simulation environments, and curated resources for autonomous uav flight dynamics, autopilots, and gps-denied navigation.

---

## architecture overview

autonomous flight requires tightly coupling physics, low-level microcontroller firmware, state estimation, and high-level trajectory planning:

```
[sensors: imu / optical flow / stereo camera / lidar]
                        │
                        ▼
           [state estimation: ekf2 / vio]
                        │
                        ▼
      [trajectory generation: minimum snap / b-spline]
                        │
                        ▼
     [geometric tracking control: se(3) position & attitude]
                        │
                        ▼
      [control allocation & motor mixing: px4 / ardupilot]
                        │
                        ▼
           [actuators: brushless motors & escs]
```

---

## study checklist

### 01. flight dynamics and physics
- [ ] multirotor and fixed-wing aerodynamics: lift, drag, blade flapping, ground effect, thrust coefficients
- [ ] 6-dof nonlinear equations of motion in body and inertial reference frames ($se(3)$ kinematics)
- [ ] coriolis and centripetal accelerations, moment of inertia tensor, gyroscopic torque
- [ ] motor and esc dynamics: thrust-to-weight ratio, voltage sag, rpm feedback via dshot protocol

### 02. flight control architectures
- [ ] cascaded pid loops: angular rate (inner loop), attitude, velocity, and position (outer loop)
- [ ] feedforward acceleration compensation and integral anti-windup strategies
- [ ] geometric tracking control on $so(3)$ and $se(3)$ manifolds to prevent gimbal lock
- [ ] model predictive control (mpc) and control barrier functions (cbf) for dynamic obstacle avoidance

### 03. autopilot firmware and middleware
- [ ] px4 autopilot architecture: uorb publish-subscribe messaging bus, flight modes, and task scheduling
- [ ] px4 ekf2 24-state navigation filter and control allocation geometry
- [ ] ardupilot architecture: ap_hal hardware abstraction layer, ekf3 estimation, and chibios rtos
- [ ] mavlink communication protocol: message serialization, telemetry streams, and mission microservices
- [ ] ros 2 integration via micro-xrce-dds agent and uxrce-dds client

### 04. gps-denied navigation and spatial awareness
- [ ] visual-inertial odometry (vio) integration for local state estimation (vins-fusion, orb-slam3)
- [ ] downward-facing optical flow and lidar rangefinder sensor fusion
- [ ] occupancy voxel mapping in 3d space (octomap, esdf) for safe flight corridor generation
- [ ] companion computer architecture: high-rate offboard setpoint streaming (mavsdk, ros 2 px4_msgs)

### 05. software-in-the-loop (sitl) simulation
- [ ] px4 sitl with gazebo harmonic and jmavsim environments
- [ ] custom airframe definitions, aerodynamic coefficients, and sensor noise simulation
- [ ] hardware-in-the-loop (hitl) validation on stm32 flight controllers
- [ ] flight log analytics: parsing ulog files with pyulog, vibration spectral fft analysis, and ekf tuning

---

## curated resources

### video lectures & course series
- [phil's lab – hardware design, sensor interfacing & flight controller firmware in c/c++](https://www.youtube.com/@PhilsLab): end-to-end custom stm32 flight controller hardware design, imu/barometer sensor interfacing, and kalman filter firmware.
- [university of zürich robotics and perception group (uzh rpg)](https://www.youtube.com/@ailabRPG/playlists): cutting-edge lectures on agile uav flight, vision-based navigation, event cameras, and high-speed autonomy.
- [brian douglas – autonomous navigation & path tracking](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg): comprehensive engineering tutorials on path tracking, pure pursuit, and control loop structures.
- [fei gao fast lab (zhejiang university) – autonomous uav planning and exploration](https://www.youtube.com/results?search_query=fei+gao+fast+lab+motion+planning): trajectory optimization, kinodynamic planning, and autonomous exploration algorithms for micro aerial vehicles.

### seminal books & academic papers
- [small unmanned aircraft: theory and practice (randy beard & tim mclain – byu magicc lab)](http://uavbook.byu.edu/): the primary engineering textbook for 6-dof quadrotor and fixed-wing flight dynamics, state-space linearization, and cascaded control loops.
- [geometric tracking control of a quadrotor uav on se(3) (taeyoung lee, melvin leok, n. harris mcclamroch – ieee cdc)](https://arxiv.org/abs/1003.2005): foundational paper establishing singularity-free geometric tracking control on lie groups for aggressive quadrotor maneuvers.
- [minimum snap trajectory generation and control for quadrotors (daniel mellinger & vijay kumar – ieee icra)](https://ieeexplore.ieee.org/document/5980409): mathematical proof of quadrotor differential flatness and minimum snap polynomial trajectory planning.
- [px4 architectural concept & companion computer integration guide](https://docs.px4.io/main/en/concept/architecture.html): official architectural reference for px4 flight tasks, uorb messaging, and companion computer bridges.
- [ardupilot architecture and ap_hal documentation](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html): in-depth breakdown of ardupilot hardware abstraction and ekf3 estimation architecture.

### open-source codebases & tools
- [px4/px4-autopilot](https://github.com/PX4/PX4-Autopilot): industry-standard flight control stack with modular uorb drivers, state estimation, and mixer logic.
- [ardupilot/ardupilot](https://github.com/ArduPilot/ardupilot): mature autopilot codebase featuring ap_hal abstraction, advanced failsafes, and multi-vehicle support.
- [mavlink/qgroundcontrol](https://github.com/mavlink/qgroundcontrol): cross-platform ground control station for parameter calibration, mission planning, and real-time telemetry visualization.
- [kumarrobotics/kr_mav_control](https://github.com/KumarRobotics/kr_mav_control): university of pennsylvania grasp lab's se(3) geometric tracking controller implementation.
- [flightmare (uzh rpg)](https://github.com/uzh-rpg/flightmare): flexible quadrotor simulation platform with unity rendering for vision-based learning and control.
- [mavlink/mavsdk](https://github.com/mavlink/MAVSDK): modern c++ api library for offboard autonomous mission control over mavlink.

---

## extended uav & autonomy resource archive

### 8.5 robot simulation

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

### 9.3 advanced control

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

### 9.4 autonomous motion

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

### 11.2 motion planning

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

### 12.4 hardware-software integration

- [ ] sensor interfaces
- [ ] actuator interfaces
- [ ] communication protocols
- [ ] firmware integration
- [ ] hardware abstraction layers (hal)
- [ ] system diagnostics
- [ ] fault detection
- [ ] reliability engineering
- [ ] px4 autopilot architecture (uorb & ros 2 micro-xrce-dds)
- [ ] ardupilot ap_hal & mavlink telemetry protocol
- [ ] qgroundcontrol (qgc) & gcs mission planning
- [ ] uav 6-dof flight dynamics & cascaded autopilot control (beard & mclain)
- [ ] geometric uav tracking control on se(3) (taeyoung lee)

**resources:**

- **video lectures:**
  1. **phil's lab – hardware design & flight controller firmware in c/c++:** [youtube channel](https://www.youtube.com/@PhilsLab) — designing custom stm32 + imu flight controller pcbs and writing sensor drivers and kalman filters in c
- **books, papers & repositories:**
  1. **px4 autopilot architecture & companion integration:** [docs.px4.io](https://docs.px4.io/main/en/concept/architecture.html) & [github repo](https://github.com/PX4/PX4-Autopilot) — how sensor drivers connect via `uorb` to ekf2, flight controllers, and ros 2 (`uxrce_dds`) on a companion computer
  2. **ardupilot architecture & ap_hal:** [ardupilot.org](https://ardupilot.org/) · [github repo](https://github.com/ArduPilot/ardupilot) & [mavproxy](https://github.com/ArduPilot/MAVProxy) — hardware abstraction layer (ap_hal) on chibios rtos with 24-state ekf3 and mavlink support for copter, plane, and vtol
  3. **qgroundcontrol (mavlink ground control station):** [qgroundcontrol.com](http://qgroundcontrol.com/) & [github repo](https://github.com/mavlink/qgroundcontrol) — c++/qt ground control software for waypoint mission planning, calibration, parameter tuning, and live telemetry
  4. **small unmanned aircraft: theory and practice (beard & mclain):** [uavbook.byu.edu](http://uavbook.byu.edu/) & [magicc lab](https://magicc.byu.edu/) — core textbook explaining the 6-dof flight dynamics, aerodynamics, and cascaded pid loops behind ardupilot and px4
  5. **geometric tracking control of a quadrotor uav on se(3) (taeyoung lee et al.):** [arxiv:1003.2005](https://arxiv.org/abs/1003.2005) — seminal paper eliminating euler gimbal lock by tracking quadrotor trajectories directly on $so(3)$ and $se(3)$

### 12.5 embedded ai

- [ ] tinyml
- [ ] edge inference
- [ ] model quantization (int8, fp8)
- [ ] model pruning
- [ ] knowledge distillation
- [ ] hardware acceleration
- [ ] neural processing units (npu)
- [ ] embedded gpu computing (nvidia jetson architecture)

**resources:**

- **video lectures:**
  1. **jetsonhacks – nvidia jetson edge ai & tensorrt:** [youtube channel](https://www.youtube.com/@JetsonHacks) & [github](https://github.com/JetsonHacksNano) — guides for camera drivers, cuda, and c++ tensorrt setups on nvidia jetson
  2. **mit 6.5940 – tinyml & efficient deep learning computing (song han):** [youtube lecture series](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) & [course site](https://hanlab.mit.edu/courses/2024-fall-65940) — quantization (int8/fp8/int4), pruning, distillation, and hardware-aware efficiency
  3. **shawn hymel – introduction to embedded machine learning:** [youtube playlist](https://www.youtube.com/playlist?list=PL7VEa1KauMQqZFj_nWRfsCZNXaBbkuurG) — running neural network inference on microcontrollers
- **books, papers & repositories:**
  1. **dusty-nv/jetson-inference:** [github repo](https://github.com/dusty-nv/jetson-inference) & [nvidia jetson ai lab](https://www.jetson-ai-lab.com/) — official c++/python tensorrt tutorials for real-time detection, segmentation, and pose estimation
  2. **wang-xinyu/tensorrtx:** [github repo](https://github.com/wang-xinyu/tensorrtx) — shows how to convert models like yolov8/v11, resnet, and detr from pytorch and write them from scratch using the pure c++ tensorrt api
  3. **tinyml (pete warden & daniel situnayake):** [o'reilly book page](https://www.oreilly.com/library/view/tinyml/9781492052036/) — practical reference for machine learning on arduino and ultra-low-power microcontrollers

### 38.5 remote sensing & aerial imagery

- [ ] satellite and aerial image basics
- [ ] multispectral and hyperspectral imaging
- [ ] sar (synthetic aperture radar)
- [ ] thermal and infrared imaging
- [ ] aerial object detection (small and oriented objects)
- [ ] land cover segmentation
- [ ] change detection
- [ ] georeferencing and coordinate reference systems
- [ ] gis tools (qgis, gdal)
- [ ] aerial datasets (dota, visdrone, xview)
- [ ] geospatial foundation models
- [ ] uav imagery analytics
