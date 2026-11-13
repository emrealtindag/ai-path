# autonomy and flight

planned topics and study notes for uav flight dynamics, autopilots and gps-denied autonomy.

## topics to be covered

- **flight physics** — aerodynamics of multirotors and fixed wing aircraft, lift, drag, thrust and moments
- **six degrees of freedom dynamics** — nonlinear equations of motion, body frames, inertia and external forces
- **geometric flight control** — geometric tracking control on the special euclidean group se3
- **px4 autopilot architecture** — uorb messaging bus, flight modes, ekf2 navigation filter and mixer logic
- **ardupilot architecture** — ap_hal hardware abstraction, ekf3 state estimation and vehicle flight modes
- **mavlink protocol** — message serialization, telemetry streams, command protocols and ground control stations
- **companion computer integration** — offboard flight control, high rate pose setpoints and companion bridges
- **gps-denied navigation** — optical flow odometry, vision position estimates and sensor degraded flight
- **edge ai deployment** — model optimization, tensorrt fp16 and int8 engines, nvidia jetson inference pipelines
- **flight telemetry analytics** — flight log parsing, system identification, vibration spectral analysis and tuning
