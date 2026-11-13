# slam

planned topics and study notes for simultaneous localization and mapping.

## topics to be covered

- **visual odometry** — feature based and direct frame to frame motion tracking across consecutive frames
- **monocular and stereo slam** — visual tracking, local map management, triangulation and keyframe selection
- **lidar odometry** — point cloud deskewing, scan to scan matching, scan to map registration and lio
- **tightly coupled vio** — sliding window joint optimization of camera visual features and imu measurements
- **tightly coupled lio** — direct point cloud registration tightly coupled with high frequency imu states
- **imu pre-integration** — manifold based pre-integration of imu measurements between keyframes on lie groups
- **factor graphs** — nonlinear least squares factor graphs, incremental smoothing and gtsam implementations
- **loop closure** — place recognition, bag of visual words, visual embeddings and loop candidate verification
- **relocalization** — recovering 6 dof camera and robot pose after tracking loss inside an existing map
- **pose graph optimization** — global graph relaxation, loop closure constraints and drift correction
- **map based localization** — metric positioning and pose tracking within pre-built geometric and visual maps
