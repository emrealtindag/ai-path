# state estimation and sensor fusion

engineering curriculum, mathematical representations, stochastic filtering, and curated resources for inertial navigation, kalman filtering, and multi-sensor fusion.

---

## architecture overview

```
[sensors: imu / gnss / wheel encoders / barometer / camera]
                              │
                              ▼
        [stochastic noise modeling: allan variance / bias]
                              │
                              ▼
            [state prediction: strapdown kinematics]
                              │
                              ▼
       [measurement update: kalman gain / innovation]
                              │
                              ▼
         [fused state output: pose / velocity / biases]
```

---

## complete checklist and resources

### 10.1 sensor fundamentals

- [ ] imu (inertial measurement unit)
- [ ] accelerometers
- [ ] gyroscopes
- [ ] magnetometers
- [ ] gps/gnss
- [ ] cameras
- [ ] lidar
- [ ] radar
- [ ] wheel encoders
- [ ] barometers
- [ ] ultrasonic sensors
- [ ] sensor noise models (white noise, random walk)
- [ ] sensor calibration

**resources:**

- **video lectures:**
  1. **cyrill stachniss – sensors and sensing:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — physics, noise models, and calibration for imu, lidar, camera, and gnss
  2. **brian douglas – sensor fusion & imu fundamentals:** [youtube playlist](https://www.youtube.com/playlist?list=PLn8PRpmsu08ryYoBpEKzoMOveSTyS-h4a) — why accelerometers, gyroscopes, magnetometers, and gps need fusion (drift vs noise)
- **books, papers & repositories:**
  1. **vectornav inertial navigation primer:** [free technical handbook](https://www.vectornav.com/resources/inertial-navigation-primer) — clear industrial guide to imu physics, white noise, allan variance, and reference frames
  2. **introduction to random signals & applied kalman filtering (brown & hwang):** [book page](https://www.wiley.com/en-us/Introduction+to+Random+Signals+and+Applied+Kalman+Filtering+with+Matlab+Exercises%2C+4th+Edition-p-9780470609699) — stochastic processes and sensor noise modeling

### 10.2 state estimation

- [ ] state-space models
- [ ] system observability
- [ ] measurement models
- [ ] process models
- [ ] noise models
- [ ] covariance
- [ ] bayesian estimation

**resources:**

- **video lectures:**
  1. **cyrill stachniss – probabilistic state estimation & bayes filter:** [youtube lecture video](https://www.youtube.com/watch?v=0lKHFJpaZvE) — math foundations of bayes filter prediction, correction, and covariance propagation
- **books, papers & repositories:**
  1. **probabilistic robotics (thrun, burgard, fox):** [book page](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — chapters 2–4: foundational textbook on recursive state estimation
  2. **state estimation for robotics (timothy d. barfoot):** [free pdf](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf) — graduate textbook on nonlinear state estimation and sensor fusion on $se(3)$ lie groups

### 10.3 filtering

- [ ] moving average filter
- [ ] low-pass filter
- [ ] high-pass filter
- [ ] complementary filter
- [ ] kalman filter (kf)
- [ ] extended kalman filter (ekf)
- [ ] unscented kalman filter (ukf)
- [ ] particle filter (sequential monte carlo)
- [ ] information filter
- [ ] error-state kalman filter (eskf)
- [ ] 24-state aviation ekf architecture (inertialnav / px4 ekf2)

**resources:**

- **video lectures:**
  1. **michel van biezen – the kalman filter series:** [youtube playlist](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT) — worked step-by-step numerical examples of kalman gain and covariance updates
  2. **cyrill stachniss – kf, ekf, ukf & particle filter:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — jacobian ekf linearization, sigma-point ukf, and particle filters
- **books, papers & repositories:**
  1. **kalman and bayesian filters in python (roger r. labbe jr.):** [free interactive book](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) — open-source jupyter notebook book building kf, ekf, ukf, and particle filters from scratch
  2. **quaternion kinematics for the error-state kalman filter (joan solà):** [arxiv:1711.02508 (free pdf)](https://arxiv.org/pdf/1711.02508.pdf) — core paper behind eskf and quaternion attitude integration in px4 and ardupilot
  3. **commaai/openpilot (`rednose` kalman filter):** [github.com/commaai/openpilot](https://github.com/commaai/openpilot) — symbolic/c++ kalman filter code running on real self-driving vehicles
  4. **inertialnav: 24-state aviation ekf (paul riseborough):** [github repo](https://github.com/priseborough/InertialNav) — sympy math derivations and pure c++ code for the 24-state navigation ekf powering px4 and ardupilot

### 10.4 advanced sensor fusion

- [ ] imu-camera fusion
- [ ] visual-inertial odometry (vio & msckf)
- [ ] gnss-imu fusion
- [ ] lidar-inertial odometry (lio)
- [ ] radar-camera fusion
- [ ] multi-sensor calibration
- [ ] multi-modal perception
- [ ] probabilistic sensor fusion
- [ ] thermal-inertial odometry (rovtio) & radar-inertial fusion
- [ ] okvis / okvis 2 keyframe-based vio
- [ ] r3live & r3live++ lidar-visual-inertial fusion

**resources:**

- **video lectures:**
  1. **hkust aerial robotics group – vins-mono & vins-fusion:** [youtube channel](https://www.youtube.com/@hkustaerialroboticsgroup6329) — presentations showing how uavs localize in gps-denied spaces via camera + imu fusion
  2. **hku mars lab – fast-lio & r3live presentations:** [youtube channel](https://www.youtube.com/@marslabhku1418) — tightly-coupled lidar-imu and visual odometry architectures
  3. **joan solà – slam & micro lie theory:** [youtube search](https://www.youtube.com/results?search_query=joan+sola+slam) — whiteboard derivations for $so(3)/se(3)$ lie algebra and imu pre-integration
  4. **prof. frank dellaert – factor graphs, invariant ekf & sensor fusion:** [youtube search](https://www.youtube.com/results?search_query=frank+dellaert+factor+graphs) — lectures on isam2 factor graphs, sliding-window optimization, and multi-sensor fusion
- **books, papers & repositories:**
  1. **vins-mono (qin, li, shen):** [arxiv:1708.03852](https://arxiv.org/abs/1708.03852) & [c++ repo](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) — c++ visual-inertial state estimator with imu pre-integration and sliding-window optimization
  2. **fast-lio2 (hku mars lab):** [arxiv:2107.06829](https://arxiv.org/abs/2107.06829) & [c++ repo](https://github.com/hku-mars/FAST_LIO) — fast tightly-coupled lidar-inertial odometry using ikd-tree and iterated kalman filter
  3. **tixiaoshan/lio-sam:** [github.com/tixiaoshan/lio-sam](https://github.com/TixiaoShan/LIO-SAM) — clean c++ implementation fusing lidar, imu, and gps using gtsam factor graphs
  4. **georgia tech csx803-amr (prof. frank dellaert):** [course page](https://dellaert.github.io/26S-AMR/) & [github repo](https://github.com/dellaert/26S-AMR) — open university course projects on invariant ekf, factor graphs, lio, and continuous-time slam
  5. **msckf vio (upenn grasp lab):** [github repo](https://github.com/KumarRobotics/msckf_vio) — filter-based $\mathcal{o}(n)$ complexity stereo visual-inertial odometry running at high frequency on embedded uav hardware
  6. **kimera-vio & kimera-vio-ros (mit spark lab):** [kimera-vio](https://github.com/MIT-SPARK/Kimera-VIO) · [kimera-vio-ros](https://github.com/MIT-SPARK/Kimera-VIO-ROS) — gtsam isam2 stereo visual-inertial odometry with real-time 3d mesh generation
  7. **rovtio & radvio (ntnu arl):** [rovtio](https://github.com/ntnu-arl/rovtio) & [radvio](https://github.com/ntnu-arl/radvio) — thermal-inertial and 4d radar-inertial c++ state estimation for smoke, dust, and low-visibility conditions
  8. **okvis & okvis 2 (imperial / tu munich):** [okvis2](https://github.com/SmartRoboticsLab/okvis2) & [okvis](https://github.com/ethz-asl/okvis) — keyframe-based sliding-window visual-inertial slam in c++ using ceres
  9. **r3live & r3live++ (hku mars lab):** [github repo](https://github.com/hku-mars/r3live) — tightly-coupled lidar, imu, and rgb camera state estimation with colored 3d radiance mesh mapping

### 10.5 localization

- [ ] dead reckoning
- [ ] odometry
- [ ] visual odometry
- [ ] inertial navigation
- [ ] gnss-based localization (rtk-gps)
- [ ] map-based localization
- [ ] monte carlo localization (mcl)
- [ ] particle filter localization
- [ ] visual-inertial localization
- [ ] lidar localization (ndt, icp-based)
- [ ] distributed pose graph optimization (dpgo) & multi-robot slam

**resources:**

- **video lectures:**
  1. **cyrill stachniss – markov, grid & monte carlo localization:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — clear lectures on probabilistic localization inside known maps
  2. **eth zürich – autonomous mobile robots (localization):** [youtube lecture series](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — odometry error models and map-based localization
- **books, papers & repositories:**
  1. **probabilistic robotics – ch. 7 & 8:** [book page](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — foundational theory of markov, grid, and particle filter localization
  2. **ros 2 nav2 amcl configuration guide:** [docs.nav2.org](https://docs.nav2.org/) — tuning particle filter localization on physical mobile robots
  3. **maplab (eth zürich asl):** [github repo](https://github.com/ethz-asl/maplab) — c++ visual-inertial mapping, multi-session localization, and map merging framework
  4. **dpgo & clipper (mit acl):** [dpgo](https://github.com/mit-acl/dpgo) · [clipper](https://github.com/mit-acl/clipper) — c++ libraries for distributed multi-robot pose graph optimization and graph-based outlier rejection
