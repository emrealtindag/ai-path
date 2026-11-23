# 3d computer vision and spatial ai

engineering curriculum, mathematical representations, geometric algorithms, simulation rendering, and curated resources for 3d perception, point clouds, and neural scene representations.

---

## architecture overview

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

## complete checklist and resources

### 01. 3d computer vision & spatial ai

#### 7.1 3d mathematics

- [ ] 3d coordinate systems
- [ ] cartesian coordinates
- [ ] homogeneous coordinates
- [ ] rotation matrices
- [ ] euler angles
- [ ] quaternions
- [ ] axis-angle representation
- [ ] rigid body transformations
- [ ] se(3)
- [ ] so(3)
- [ ] coordinate frame transformations

**resources:**

- **video lectures:**
  1. **3blue1brown – visualizing quaternions & 3d rotation:** [youtube video](https://www.youtube.com/watch?v=d4EgbgTm0Bg) & [interactive site](https://eater.net/quaternions) — clear visual explanation of 3d rotations and avoiding gimbal lock with quaternions
  2. **cyrill stachniss – 3d coordinate transformations & homogeneous coordinates:** [youtube lecture video](https://www.youtube.com/watch?v=PvEl63t-opM) — coordinate frame transformation matrices ($se(3), so(3)$) in robotics and 3d vision
- **books, papers & repositories:**
  1. **a micro lie theory for state estimation in robotics (joan solà et al.):** [arxiv:1812.01537 (free pdf)](https://arxiv.org/pdf/1812.01537.pdf) — practical guide to 3d manifold jacobians for writing slam and kalman filters
  2. **lie groups for 2d and 3d transformations (ethan eade):** [ethaneade.com/lie.pdf](https://ethaneade.com/lie.pdf) — handy formula cheat sheet when implementing 3d geometry in c++

#### 7.2 depth estimation

- [ ] stereo depth estimation
- [ ] foundation stereo matching (foundationstereo)
- [ ] monocular depth estimation
- [ ] multi-view stereo (mvs)
- [ ] depth maps
- [ ] depth completion
- [ ] depth prediction networks (midas, depth anything)
- [ ] metric depth estimation
- [ ] relative depth estimation

**resources:**

- **video lectures:**
  1. **shree nayar – stereo vision & depth estimation:** [youtube playlist](https://www.youtube.com/playlist?list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo) — core physics and math of disparity, triangulation, and stereo depth
  2. **cyrill stachniss – stereo vision & multi-view stereo:** [youtube search](https://www.youtube.com/results?search_query=cyrill+stachniss+stereo+vision) — dense depth map generation from stereo pairs
- **books, papers & repositories:**
  1. **opencv stereo depth map tutorial:** [docs.opencv.org](https://docs.opencv.org/4.x/dd/d53/tutorial_py_depthmap.html) — classical disparity map extraction using stereobm and stereosgbm
  2. **depth anything & depth anything v2:** [arxiv:2401.10891](https://arxiv.org/abs/2401.10891) & [github repo](https://github.com/DepthAnything/Depth-Anything-V2) — high-accuracy monocular relative and metric depth estimation
  3. **foundationstereo (nvidia research):** [project page](https://nvlabs.github.io/FoundationStereo/) & [github repo](https://github.com/NVlabs/FoundationStereo) — zero-shot stereo depth and 3d point cloud model optimized for jetson/tensorrt
  4. **defm: depth foundation model for robot navigation (eth zürich):** [github repo](https://github.com/leggedrobotics/defm) — predicts metric depth directly in meters from a single camera for elevation mapping and obstacle avoidance

#### 7.3 3d reconstruction

- [ ] structure from motion (sfm)
- [ ] multi-view geometry
- [ ] bundle adjustment
- [ ] camera pose estimation (pnp algorithms)
- [ ] sparse reconstruction
- [ ] dense reconstruction
- [ ] point cloud generation
- [ ] mesh reconstruction
- [ ] surface reconstruction
- [ ] modern global structure-from-motion (glomap)

**resources:**

- **turkish resources:**
  1. **metu ceng 483 – 3d vision & multi-view geometry:** [course page](https://user.ceng.metu.edu.tr/~skalkan/)
- **video lectures:**
  1. **cyrill stachniss – photogrammetry ii (sfm, pnp & bundle adjustment):** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y) — step-by-step estimation of 3d camera poses (pnp) and point clouds (bundle adjustment)
  2. **prof. daniel cremers – multiple view geometry (tum):** [youtube lecture series](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — university course on multi-view 3d reconstruction math
- **books, papers & repositories:**
  1. **colmap (sfm & mvs):** [colmap.github.io](https://colmap.github.io/) & [github repo](https://github.com/colmap/colmap) — standard c++ pipeline for structure-from-motion, camera pose extraction, and bundle adjustment
  2. **multiple view geometry (hartley & zisserman – ch. 17 & 18):** [robots.ox.ac.uk/~vgg/hzbook](https://www.robots.ox.ac.uk/~vgg/hzbook/) — theoretical reference for sfm and bundle adjustment
  3. **glomap: global structure-from-motion (colmap team):** [github repo](https://github.com/colmap/glomap) — global pose graph sfm reconstruction up to 10x faster than incremental colmap

#### 7.4 point cloud processing

- [ ] point cloud fundamentals
- [ ] point cloud registration & graph slam (open3d_slam)
- [ ] kiss-icp & fast lidar odometry
- [ ] scan context & lidar loop closure
- [ ] icp (iterative closest point)
- [ ] generalized icp
- [ ] pointnet
- [ ] pointnet++
- [ ] point transformer
- [ ] voxelization
- [ ] octrees
- [ ] point cloud segmentation
- [ ] 3d object detection

**resources:**

- **video lectures:**
  1. **cyrill stachniss – point cloud registration & icp:** [youtube search](https://www.youtube.com/results?search_query=cyrill+stachniss+icp+point+cloud) — math derivation of icp and svd point cloud alignment
  2. **open3d official tutorials:** [youtube search](https://www.youtube.com/results?search_query=open3d+tutorial) — practical 3d point cloud and mesh workflows
- **books, papers & repositories:**
  1. **open3d documentation (c++ & python):** [open3d.org/docs](https://www.open3d.org/docs/release/) & [github repo](https://github.com/isl-org/Open3D) — modern c++/python library for voxelization, octrees, icp, and surface reconstruction
  2. **point cloud library (pcl):** [pointclouds.org](https://pointclouds.org/) & [tutorials](https://pcl.readthedocs.io/projects/tutorials/en/master/) — standard c++ library for lidar point cloud processing in ros 2
  3. **pointnet (qi et al., stanford):** [arxiv:1612.00593](https://arxiv.org/abs/1612.00593) — core paper introducing deep learning directly on unordered 3d point sets
  4. **open3d slam (eth zürich):** [github repo](https://github.com/leggedrobotics/open3d_slam) — open-source c++ 3d lidar/rgb-d slam using point-to-plane icp, gicp, submaps, and pose graph optimization
  5. **kiss-icp (university of bonn):** [github repo](https://github.com/PRBonn/kiss-icp) & [paper pdf](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/vizzo2023ral.pdf) — simple, fast point-to-point icp lidar odometry running 100+ hz on a single cpu thread without imu
  6. **scan context (kaist url):** [github repo](https://github.com/gisbi-kim/ScanContext) & [sc-lego-loam](https://github.com/gisbi-kim/SC-LeGO-LOAM) — rotation-invariant 3d lidar descriptor for place recognition and loop closure

#### 7.5 advanced spatial ai

- [ ] neural radiance fields (nerf)
- [ ] gaussian splatting
- [ ] 3d gaussian splatting (3dgs)
- [ ] neural scene representations
- [ ] neural implicit surfaces
- [ ] occupancy networks
- [ ] scene understanding
- [ ] semantic mapping & 3d scene graphs (kimera)
- [ ] 3d scene graphs
- [ ] dynamic scene reconstruction
- [ ] 4d scene understanding

**resources:**

- **video lectures:**
  1. **nerf & 3d gaussian splatting explanations:** [youtube video (3dgs)](https://www.youtube.com/watch?v=HVv_IQKlafQ) — visual and mathematical overview of nerf and 3d gaussian splatting
  2. **prof. frank dellaert – 3d gaussian splatting & spatial ai:** [youtube search](https://www.youtube.com/results?search_query=frank+dellaert+spatial+ai) — robotics mapping and spatial ai perspective
- **books, papers & repositories:**
  1. **3d gaussian splatting (kerbl et al., siggraph 2023):** [arxiv:2308.04079](https://arxiv.org/abs/2308.04079) & [official repo](https://github.com/graphdeco-inria/gaussian-splatting) — real-time 100+ fps neural rendering with custom cuda rasterizer
  2. **nerf (mildenhall et al.):** [arxiv:2003.08934](https://arxiv.org/abs/2003.08934) & [project page](https://www.matthewtancik.com/nerf) — foundational paper on volumetric rendering and neural scene representations
  3. **nerfstudio:** [docs.nerf.studio](https://docs.nerf.studio/) & [github repo](https://github.com/nerfstudio-project/nerfstudio) — modular framework for training nerf and gaussian splats on custom video
  4. **kimera & kimera-semantics (mit spark lab):** [kimera](https://github.com/MIT-SPARK/Kimera) · [kimera-semantics](https://github.com/MIT-SPARK/Kimera-Semantics) — real-time metric-semantic 3d mesh reconstruction and 3d scene graphs using tsdf

---

### 02. computer graphics, rendering & simulation

#### 40.1 graphics fundamentals

- [ ] rasterization pipeline
- [ ] model-view-projection transforms
- [ ] z-buffer and clipping
- [ ] texture mapping and mipmaps
- [ ] shading models (phong, pbr)
- [ ] brdf
- [ ] rendering equation
- [ ] ray tracing
- [ ] path tracing
- [ ] global illumination
- [ ] monte carlo rendering
- [ ] color science and color management
- [ ] anti-aliasing

#### 40.2 geometry processing

- [ ] triangle meshes and half-edge structure
- [ ] mesh simplification
- [ ] subdivision surfaces
- [ ] uv parameterization
- [ ] signed distance functions (sdf)
- [ ] marching cubes
- [ ] poisson surface reconstruction
- [ ] splines and nurbs
- [ ] bounding volume hierarchies (bvh)
- [ ] collision detection
- [ ] skinning and rigging

#### 40.3 graphics apis & tools

- [ ] opengl
- [ ] vulkan
- [ ] webgpu
- [ ] shader programming (glsl, hlsl)
- [ ] blender
- [ ] unreal engine and unity
- [ ] openusd
- [ ] pytorch3d and kaolin
- [ ] mitsuba
- [ ] nvidia warp and taichi

#### 40.4 differentiable & neural rendering

- [ ] differentiable rasterization
- [ ] differentiable ray tracing
- [ ] inverse rendering
- [ ] relighting
- [ ] text-to-3d (dreamfusion)
- [ ] image-to-3d and large reconstruction models
- [ ] 3d generative models
- [ ] 4d generation
- [ ] avatar generation (3dmm, neural avatars)

#### 40.5 physics simulation & synthetic data

- [ ] rigid body simulation
- [ ] soft body and cloth simulation
- [ ] fluid simulation (sph, eulerian)
- [ ] finite element method (fem)
- [ ] position-based dynamics
- [ ] differentiable simulators
- [ ] synthetic data pipelines (blender, unreal, isaac sim)
- [ ] procedural world generation

**resources:**

- **video lectures:**
  1. [cmu 15-462 — computer graphics (keenan crane)](https://www.youtube.com/playlist?list=PL9_jI1bdZmz2emSh0UQ5iOdT2xRHFHL7E) — mvp matrices, rasterization, mesh processing, signed distance fields, and ray tracing
  2. [games101 — introduction to computer graphics (lingqi yan)](https://www.youtube.com/playlist?list=PLX_rk23kyFXVEodpOJYP30K4LZhioDU5t) — transformation matrices, shading, and physically based rendering (pbr)
  3. **ten minute physics (matthias müller / nvidia physx):** [site](https://matthias-research.github.io/pages/tenMinutePhysics/) & [youtube channel](https://www.youtube.com/@TenMinutePhysics) — coding particle, rigid-body, and collision physics engines from scratch
- **books, papers & repositories:**
  1. [learnopengl (joey de vries)](https://learnopengl.com/) — practical c++ guide to coordinate spaces, camera matrices, z-buffering, and shaders
  2. [physically based rendering (pbr-book.org)](https://pbr-book.org/) & [mitsuba 3 (github)](https://github.com/mitsuba-renderer/mitsuba3) — classic rendering book and differentiable ray-tracing engine
  3. [blenderproc (github)](https://github.com/DLR-RM/BlenderProc) & [nvidia warp (github)](https://github.com/NVIDIA/warp) — generating synthetic vision datasets and high-speed gpu physics simulation
