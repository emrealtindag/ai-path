# spatial ai and slam

engineering curriculum, mathematical representations, optimization engines, and curated resources for simultaneous localization and mapping, visual-inertial odometry, and factor graphs.

---

## architecture overview

slam fuses camera and sensor measurements to simultaneously map an unknown environment and localize the agent:

```
[sensor front-end: visual features / optical flow / imu pre-integration]
                                   │
                                   ▼
          [outlier rejection: ransac / robust cost functions]
                                   │
                                   ▼
       [optimization back-end: factor graph / bundle adjustment]
                                   │
                                   ▼
             [loop closure: visual bag-of-words / dbow2]
                                   │
                                   ▼
        [spatial representation: 3d pose graph & global map]
```

---

## study checklist

### 01. visual odometry and front-ends
- [ ] feature-based visual odometry: 2d-to-2d motion estimation (5-point algorithm), 3d-to-2d perspective-n-point (pnp, epnp), and 3d-to-3d icp
- [ ] direct and semi-direct methods: photometric error formulation, lsd-slam, dso (direct sparse odometry), and svo
- [ ] keyframe selection strategies: parallax thresholds, track quality, and co-visibility graph maintenance
- [ ] robust loss functions: huber, cauchy, and tukey biweight loss to mitigate measurement outliers

### 02. visual-inertial odometry (vio)
- [ ] imu error modeling: white noise, random walk bias, scale factor, and cross-axis sensitivity
- [ ] continuous-time kinematics and integration on manifold: quaternion attitude integration
- [ ] on-manifold imu pre-integration: forster's formulation, analytical jacobians, and bias update covariance
- [ ] spatial and temporal extrinsic calibration: online camera-to-imu time offset estimation

### 03. back-end optimization and factor graphs
- [ ] nonlinear least squares: gauss-newton and levenberg-marquardt algorithms for pose estimation
- [ ] sparse linear system solving: schur complement marginalization and cholesky factorization
- [ ] factor graphs: probabilistic graphical models, variable nodes, measurement factors, and belief propagation
- [ ] sliding-window bundle adjustment: local optimization and marginalization of old states (prior factor)
- [ ] pose graph optimization (pgo): 6-dof and 7-dof (similarity transform $\text{sim}(3)$) graph relaxation

### 04. loop closure and global mapping
- [ ] place recognition: visual bag-of-words (dbow2, dbow3) and deep learned embeddings (netvlad)
- [ ] geometric verification: relative transformation estimation and inlier consistency checks
- [ ] global map merging: loop closure constraint injection and full pose graph optimization
- [ ] benchmark evaluation: absolute trajectory error (ate) and relative pose error (rpe) computation via evo

---

## curated resources

### video lectures & course series
- [cyrill stachniss – slam course (university of bonn)](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_): the gold-standard academic university course covering ekf-slam, graph-slam, pose graph optimization, and loop closure.
- [prof. daniel cremers – visual slam: lsd-slam, dso and multiple view geometry (tum)](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4): graduate-level lectures exploring direct photometric methods and variational approaches to visual slam.
- [frank dellaert – factor graphs and spatial ai lectures (georgia tech)](https://dellaert.github.io/): foundational insights on factor graphs, incremental smoothing (isam2), and spatial intelligence.

### foundational books & academic materials
- [factor graphs for robot perception (frank dellaert & michael kaess)](https://www.nowpublishers.com/article/Details/ROB-043): premier monograph establishing factor graph optimization as the modern mathematical framework for slam.
- [imu preintegration on manifold for visual-inertial odometry (christian forster et al. – ieee t-ro)](https://arxiv.org/abs/1512.02363): seminal publication defining singularity-free, on-manifold imu pre-integration for realtime vio.
- [orb-slam3: an accurate open-source library for visual, visual-inertial, and multimap slam (campos et al. – ieee t-ro)](https://arxiv.org/abs/2007.11898): authoritative reference on state-of-the-art multi-map visual and inertial localization.

### open-source codebases & tools
- [borglab/gtsam](https://github.com/borglab/gtsam): georgia tech smoothing and mapping c++ library implementing factor graphs and isam2.
- [uzh-rpg/rpg_trajectory_evaluation (evo)](https://github.com/MichaelGrupp/evo): python package for evaluating odometry and slam trajectories against ground truth.
- [uzh-rpg/vins-mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono): hkust aerial robotics robust monocular visual-inertial state estimator.
- [raulmur/orbslam3](https://github.com/UZH-RPG/rpg_svo_pro_open): premier multi-camera, visual-inertial feature-based slam system.
