# state estimation and sensor fusion

engineering curriculum, mathematical representations, stochastic filtering, and curated resources for inertial navigation, kalman filtering, and multi-sensor fusion.

---

## architecture overview

state estimation combines noisy, incomplete sensor measurements into a statistically optimal state trajectory:

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

## study checklist

### 01. sensor fundamentals and noise characterization
- [ ] inertial measurement units (imu): micro-electro-mechanical systems (mems) accelerometers and gyroscopes
- [ ] gnss / gps architectures: pseudorange, carrier phase, differential gps (rtk), and multipath effects
- [ ] barometers, magnetometers (hard and soft iron distortion), and wheel encoders
- [ ] stochastic error modeling: white noise, random walk, bias instability, and allan variance analysis
- [ ] strapdown inertial navigation: attitude, velocity, and position numerical integration in local navigation frames

### 02. linear and extended kalman filtering
- [ ] probability foundations: multivariate gaussian distributions, covariance matrices, and error propagation
- [ ] linear kalman filter (kf): prediction step, measurement innovation, kalman gain, and covariance update
- [ ] extended kalman filter (ekf): jacobian linearization of nonlinear kinematics and measurement models
- [ ] error-state kalman filter (eskf / mekf): on-manifold orientation tracking on $so(3)$ avoiding covariance singularities
- [ ] numerical stability: joseph form covariance update and cholesky factorization

### 03. advanced nonlinear and non-gaussian filtering
- [ ] unscented kalman filter (ukf): sigma point generation, unscented transform, and higher-order nonlinear propagation
- [ ] iterated extended kalman filter (iekf): iterative measurement updates for highly nonlinear visual and lidar residuals
- [ ] particle filters (sequential monte carlo): importance sampling, weight degeneration, and systematic resampling
- [ ] complementary filters: frequency-domain sensor fusion (high-pass gyro + low-pass accelerometer/magnetometer)

### 04. multi-sensor spatial and temporal calibration
- [ ] spatial extrinsic calibration: hand-eye calibration, lidar-to-camera, and imu-to-camera rigid transformations
- [ ] temporal synchronization: hardware trigger signals, pps (pulse per second), and inter-sensor latency compensation
- [ ] out-of-sequence measurements (oosm) and delayed sensor update handling

---

## curated resources

### video lectures & course series
- [cyrill stachniss – sensors and state estimation](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_): comprehensive university lectures on sensor physics, noise models, and probabilistic state estimation.
- [brian douglas – understanding the kalman filter & sensor fusion](https://www.youtube.com/playlist?list=PLn8PRpmsu08ryYoBpEKzoMOveSTyS-h4a): intuitive visual engineering breakdown of kalman filters, ekf, and sensor fusion dynamics.
- [vectornav – inertial navigation fundamentals tech talks](https://www.vectornav.com/resources/inertial-navigation-primer): industrial deep-dive into inertial sensors, dead reckoning, and attitude estimation.

### foundational books & academic materials
- [probabilistic robotics (sebastian thrun, wolfram burgard, dieter fox)](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/): the seminal textbook establishing recursive bayesian estimation, kalman filters, and particle filters in robotics.
- [optimal state estimation: kalman, h-infinity, and nonlinear approaches (dan simon)](https://www.wiley.com/en-us/Optimal+State+Estimation%3A+Kalman%2C+H+Infinity%2C+and+Nonlinear+Approaches-p-9780471708582): rigorous mathematical coverage of kalman filters, unscented filtering, and robust estimation.
- [quaternion kinematics for the error-state kalman filter (joan solà)](https://arxiv.org/abs/1711.02508): standard reference for 3d rotation kinematics and error-state kalman filtering on lie groups.

### open-source codebases & tools
- [ethz-asl/ethzasl_msf](https://github.com/ethz-asl/ethzasl_msf): eth zürich modular multi-sensor fusion extended kalman filter framework.
- [cra-ros-pkg/robot_localization](https://github.com/cra-ros-pkg/robot_localization): industry-standard ros 2 package for multi-sensor state estimation (ekf/ukf).
- [rlabbe/kalman-and-bayesian-filters-in-python](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python): interactive textbook and python implementation of kalman and bayesian filters.
