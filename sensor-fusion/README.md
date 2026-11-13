# sensor fusion

planned topics and study notes for state estimation, filtering and multi-sensor integration.

## topics to be covered

- **inertial sensors** — accelerometer and gyroscope operating physics, measurement models and error sources
- **sensor noise characterization** — allan variance, bias instability, random walk and thermal noise
- **dead reckoning** — strapdown inertial navigation integration, velocity and position propagation
- **bayesian estimation** — recursive bayesian state estimation, prediction step and measurement update
- **linear kalman filter** — state transition matrices, process noise, measurement covariance and kalman gain
- **extended kalman filter** — system linearization, jacobian matrices and nonlinear state estimation
- **unscented kalman filter** — sigma points, unscented transform and higher order nonlinear propagation
- **iterated extended kalman filter** — iterative measurement updates for tight visual and lidar fusion
- **particle filtering** — sequential monte carlo, importance sampling, resampling and non gaussian models
- **multi sensor calibration** — spatial extrinsic calibration between camera, lidar and imu sensors
- **temporal synchronization** — hardware triggering, timestamp matching and inter sensor latency handling
