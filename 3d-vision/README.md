# 3d computer vision and spatial ai

engineering curriculum, mathematical representations, geometric algorithms, and curated resources for 3d perception, point clouds, and neural scene representations.

---

## architecture overview

3d computer vision lifts 2d visual arrays into spatial geometric coordinates:

```
[stereo camera / depth sensor / lidar]
                  │
                  ▼
[depth estimation: semi-global matching / depth completion]
                  │
                  ▼
[3d point cloud: filtering / voxelization / normals]
                  │
                  ▼
[geometric registration: icp / feature matching]
                  │
                  ▼
[3d representations: tsdf meshes / octomap / 3d gaussian splatting]
```

---

## study checklist

### 01. 3d mathematics and lie theory
- [ ] 3d coordinate frames, homogeneous coordinates, and change of reference frames
- [ ] rotation representations: euler angles, axis-angle, quaternions, and rotation matrices
- [ ] the special orthogonal group $so(3)$ and special euclidean group $se(3)$
- [ ] lie algebra $\mathfrak{so}(3)$ and $\mathfrak{se}(3)$: hat and vee operators, exponential and logarithmic maps
- [ ] on-manifold perturbation models and analytical jacobians for optimization

### 02. stereo vision and depth estimation
- [ ] stereo geometry: baseline, disparity, epipolar rectification, and depth triangulation ($z = f \cdot b / d$)
- [ ] stereo matching algorithms: block matching (bm) and semi-global block matching (sgbm)
- [ ] monocular depth estimation: self-supervised networks, scale ambiguity, and depth completion from sparse lidar

### 03. 3d point cloud processing
- [ ] point cloud representations, kd-tree spatial indexing, and radius neighbor searches
- [ ] point cloud filtering: passthrough filters, voxel grid downsampling, and statistical outlier removal (sor)
- [ ] surface normal estimation and principal curvature analysis
- [ ] rigid registration: iterative closest point (icp, point-to-point, point-to-plane), ransac, and g-icp
- [ ] segmentation: planar segmentation via ransac and euclidean cluster extraction

### 04. 3d reconstruction and neural representations
- [ ] volumetric mapping: truncated signed distance fields (tsdf) and voxel hashing (kinectfusion)
- [ ] occupancy grids: 3d octrees (octomap) and euclidean signed distance fields (esdf) for collision avoidance
- [ ] neural radiance fields (nerf): volume rendering, positional encoding, and implicit scene representations
- [ ] 3d gaussian splatting: anisotropic 3d gaussians, differentiable tile-based rasterization, and real-time radiance rendering

---

## curated resources

### video lectures & course series
- [cyrill stachniss – 3d coordinate transformations, homogeneous coordinates & lie algebra](https://www.youtube.com/watch?v=vVi8646427I): rigorous university lecture detailing the mathematics of $se(3)$ and $so(3)$ transformations in robotics and 3d vision.
- [3blue1brown – visualizing quaternions & 3d rotation](https://www.youtube.com/watch?v=d4EgbgTm0Bg): the clearest intuitive visual explanation of 4d numbers and quaternion math without gimbal lock.
- [prof. daniel cremers – multiple view geometry (technical university of munich)](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4): graduate-level course on variational methods, stereo reconstruction, and dense 3d vision.

### foundational books & academic materials
- [a micro lie theory for state estimation in robotics (joan solà, jérémie deray, dinesh atchuthan)](https://arxiv.org/abs/1812.01537): the premier practical guide to lie groups and lie algebras for engineers implementing state estimation and 3d optimization.
- [3d point cloud processing: modeling and applications (j. a. beraldin et al.)](https://link.springer.com/book/10.1007/978-3-642-15967-1): rigorous mathematical foundations of lidar data processing, surface normals, and spatial alignment.
- [3d gaussian splatting for real-time radiance field rendering (bernhard kerbl et al. – acm tog / siggraph)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/): seminal graphics paper pioneering real-time photo-realistic 3d scene representations.

### open-source codebases & tools
- [isl-org/open3d](https://github.com/isl-org/Open3D): modern c++ library for 3d data processing, point clouds, meshes, and visualization.
- [pointcloudlibrary/pcl](https://github.com/PointCloudLibrary/pcl): established large scale open-source framework for 2d/3d image and point cloud processing.
- [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting): official reference codebase for training and rendering 3d gaussian splats.
- [octomap/octomap](https://github.com/OctoMap/octomap): 3d occupancy grid mapping approach based on octrees for robotic navigation.
