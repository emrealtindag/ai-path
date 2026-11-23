# robotics

engineering curriculum, mathematical modeling, middleware, and curated resources for robot kinematics, rigid-body dynamics, ros 2, and physical simulation.

---

## architecture overview

robotics connects physical mechanics with software computation:

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

## study checklist

### 01. kinematics and spatial representations
- [ ] homogeneous transformation matrices in $se(3)$ and rotation representations in $so(3)$
- [ ] forward kinematics (fk): product of exponentials (poe) and denavit-hartenberg (dh) conventions
- [ ] inverse kinematics (ik): analytical solutions, numerical jacobian pseudoinverse, and damped least squares
- [ ] geometric and analytical jacobians: manipulability ellipsoids and singularity identification
- [ ] mobile robot kinematics: unicycle, differential drive, ackermann steering, and omnidirectional chassis

### 02. rigid-body dynamics and actuation
- [ ] spatial inertia tensors, angular momentum, and coriolis acceleration
- [ ] lagrangian mechanics: kinetic energy, potential energy, and euler-lagrange equations of motion
- [ ] newton-euler recursive inverse dynamics algorithm (rnea)
- [ ] electric actuator dynamics: bldc motors, torque-speed curves, back-emf, and gear transmission efficiency

### 03. robot operating system (ros 2)
- [ ] computational graph: nodes, topics, publishers, subscribers, services, and actions
- [ ] ros 2 dds (data distribution service) middleware, quality of service (qos) policies, and zero-copy shared memory
- [ ] tf2 coordinate transformation tree: static broadcasters, dynamic listeners, and temporal lookups
- [ ] robot modeling: urdf (unified robot description format), xacro macros, collision geometries, and joint limits
- [ ] lifecycle managed nodes, launch files, parameter management, and ros2_control framework

### 04. robot physics simulation
- [ ] gazebo simulation: physics engines (ode, bullet, dart), world definition (.sdf), contact dynamics, and sensors
- [ ] nvidia isaac sim: omniverse usd scene composition, physx 5 gpu accelerated physics, and parallel synthetic data generation
- [ ] sim-to-real transfer: domain randomization of friction, mass distribution, latency, and sensor noise

---

## curated resources

### video lectures & course series
- [kevin lynch – modern robotics: mechanics, planning, and control (northwestern university)](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx): definitive academic lecture series covering screw theory, lie algebra in robotics, and manipulation dynamics.
- [eth zürich – autonomous mobile robots (prof. roland siegwart)](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm): master-level university lectures on kinematics, perception, localization, and planning for ground and aerial robots.
- [articulated robotics – building mobile robots with ros 2](https://www.youtube.com/@ArticulatedRobotics): pragmatic step-by-step video tutorials on building a physical differential drive robot using ros 2, urdf, and gazebo.

### foundational books & academic materials
- [modern robotics: mechanics, planning, and control (kevin m. lynch & frank c. park)](http://hades.mech.northwestern.edu/index.php/Modern_Robotics): the world-standard textbook modernizing robot kinematics through screw theory and matrix exponentials.
- [introduction to autonomous mobile robots (roland siegwart, i. r. nourbakhsh, d. scaramuzza)](https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/): comprehensive text on mobile robot locomotion, kinematics, sensors, and localization.
- [ros 2 official design documents and documentation](https://design.ros2.org/): architectural papers explaining dds integration, rclcpp c++ client library, and realtime design principles.

### open-source codebases & tools
- [ros2/rclcpp](https://github.com/ros2/rclcpp): official modern c++ client library for ros 2 computation graphs.
- [stack-of-tasks/pinocchio](https://github.com/stack-of-tasks/pinocchio): high-performance modern c++ library for rigid body dynamics algorithms and analytical derivatives.
- [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim): modular modern gazebo simulation engine with multi-physics support.
- [ros-controls/ros2_control](https://github.com/ros-controls/ros2_control): production-grade hardware abstraction and realtime controller management for ros 2.
