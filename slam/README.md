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

---

## extended checklist and resources

### 7.6 visual slam

- [ ] feature-based slam (orb-slam, orb-slam2, orb-slam3)
- [ ] direct slam (lsd-slam, dso)
- [ ] semi-direct slam (svo)
- [ ] visual odometry (vo)
- [ ] monocular slam
- [ ] stereo slam
- [ ] rgb-d slam
- [ ] loop closure
- [ ] relocalization
- [ ] map optimization
- [ ] pose graph optimization
- [ ] bundle adjustment
- [ ] dense foundation slam (mast3r-slam, dust3r)
- [ ] tartanair & tartanvo slam benchmark
- [ ] droid-slam (deep recurrent visual slam) & basalt vio

**resources:**

- **video lectures:**
  1. **cyrill stachniss – slam course (university of bonn):** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — core university course covering odometry, ekf-slam, particle filters, pose graph optimization, and loop closure
  2. **prof. daniel cremers – direct slam: lsd-slam & dso (tum):** [youtube lecture series](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — lectures on direct photometric visual odometry and slam
  3. **joan solà – slam & factor graphs:** [youtube search](https://www.youtube.com/results?search_query=joan+sola+slam) — factor graphs and optimization on manifolds
  4. **prof. davide scaramuzza (uzh rpg) – vision algorithms for mobile robotics:** [course page](https://rpg.ifi.uzh.ch/teaching.html) & [uzh rpg youtube](https://www.youtube.com/@ailabRPG/playlists) — classic university course on visual odometry, optical flow, calibration, epipolar geometry, and slam
- **books, papers & repositories:**
  1. **visual odometry tutorials (part i & ii – scaramuzza & fraundorfer):** [part i pdf](https://rpg.ifi.uzh.ch/docs/VO_Part_I_Scaramuzza.pdf) & [part ii pdf](https://rpg.ifi.uzh.ch/docs/VO_Part_II_Scaramuzza.pdf) — concise 20-page overview summarizing visual odometry math
  2. **orb-slam3 (campos et al.):** [arxiv:2007.11898](https://arxiv.org/abs/2007.11898) — key paper for feature-based visual, visual-inertial, and multi-map slam
  3. **orb_slam3 & orb_slam2 (c++):** [orb_slam3](https://github.com/UZ-SLAMLab/ORB_SLAM3) · [orb_slam2](https://github.com/raulmur/ORB_SLAM2) — reference c++ codebases showing multi-threaded tracking, local mapping, and loop closing
  4. **gtsam (georgia tech):** [gtsam.org](https://gtsam.org/) & [github repo](https://github.com/borglab/gtsam) — standard c++ library for factor graph and pose graph optimization
  5. **mast3r-slam (imperial college / dyson lab):** [project page](https://edexheim.github.io/mast3r-slam/) & [github repo](https://github.com/rmurai0610/MASt3R-SLAM) — real-time monocular dense slam built on 3d foundation model priors
  6. **svo: semi-direct visual odometry (uzh rpg):** [github](https://github.com/uzh-rpg/rpg_svo_pro_open) & [legacy](https://github.com/uzh-rpg/rpg_svo) — fast 55+ fps semi-direct visual odometry designed for embedded uavs
  7. **tartanair & tartanvo benchmark (cmu airlab):** [dataset site](https://theairlab.org/tartanair-dataset/) · [tartanair_tools](https://github.com/castacks/tartanair_tools) & [tartanairpy](https://github.com/castacks/tartanairpy) — challenging unreal engine slam and optical flow benchmark with ground-truth trajectories
  8. **droid-slam & basalt (princeton / tu munich):** [droid-slam](https://github.com/princeton-vl/DROID-SLAM) & [basalt](https://gitlab.com/VladyslavUsenko/basalt) — deep optical-flow bundle adjustment slam and fast cpu c++ visual-inertial odometry

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
  2. **eth zürich – autonomous mobile robots (localization):** [course page](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots.html) — odometry error models and map-based localization
- **books, papers & repositories:**
  1. **probabilistic robotics – ch. 7 & 8:** [book page](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — foundational theory of markov, grid, and particle filter localization
  2. **ros 2 nav2 amcl configuration guide:** [docs.nav2.org](https://docs.nav2.org/) — tuning particle filter localization on physical mobile robots
  3. **maplab (eth zürich asl):** [github repo](https://github.com/ethz-asl/maplab) — c++ visual-inertial mapping, multi-session localization, and map merging framework
  4. **dpgo & clipper (mit acl):** [dpgo](https://github.com/mit-acl/dpgo) · [clipper](https://github.com/mit-acl/clipper) — c++ libraries for distributed multi-robot pose graph optimization and graph-based outlier rejection
