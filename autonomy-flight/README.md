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
- [eth zürich robotics and perception group (rpg)](https://www.youtube.com/@uzhrpg): cutting-edge lectures on agile uav flight, vision-based navigation, event cameras, and high-speed autonomy.
- [brian douglas – autonomous navigation & path tracking](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg): comprehensive engineering tutorials on path tracking, pure pursuit, and control loop structures.
- [feigao fast lab (hkust) – autonomous uav planning and exploration](https://www.youtube.com/results?search_query=fei+gao+fast+lab+motion+planning): trajectory optimization, kinodynamic planning, and autonomous exploration algorithms for micro aerial vehicles.

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
- [flightmare (uzh rpg)](https://flightmare.bitbucket.io/): flexible quadrotor simulation platform with unity rendering for vision-based learning and control.
- [mavlink/mavsdk](https://github.com/mavlink/MAVSDK): modern c++ api library for offboard autonomous mission control over mavlink.
