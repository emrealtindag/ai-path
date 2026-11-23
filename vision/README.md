# computer vision

engineering curriculum, algorithmic foundations, geometric representations, and curated resources for 2d image processing, classical feature extraction, and deep visual perception.

---

## architecture overview

computer vision transforms raw photon arrays into structured semantic and spatial understanding:

```
[camera stream: bgr / nv12 frames]
                 │
                 ▼
[image preprocessing: filtering / color spaces]
                 │
                 ▼
[geometric features: orb / sift / optical flow]
                 │
                 ▼
[visual inference: object detection / segmentation]
                 │
                 ▼
[downstream tasks: tracking / visual odometry / spatial ai]
```

---

## study checklist

### 01. classical image processing
- [ ] image representations: pixel matrices, color spaces (rgb, hsv, lab), and color channels
- [ ] linear spatial filtering: convolution kernels, gaussian blur, box filters, and separable filtering
- [ ] gradient operators and edge detection: sobel, prewitt, laplacian, and canny edge detector
- [ ] thresholding techniques: global thresholding, otsu's method, and adaptive thresholding
- [ ] morphological operations: dilation, erosion, opening, closing, and hit-or-miss transforms
- [ ] frequency domain analysis: 2d discrete fourier transform (dft), high-pass and low-pass filtering

### 02. camera models and multi-view geometry
- [ ] pinhole camera model: intrinsic calibration matrix $k$, focal lengths, and principal point
- [ ] lens distortion modeling: radial distortion ($k_1, k_2, k_3$) and tangential distortion ($p_1, p_2$)
- [ ] camera calibration: zhang's checkerboard method, homography estimation, and reprojection error minimization
- [ ] two-view geometry: epipolar lines, epipoles, essential matrix $e$, and fundamental matrix $f$
- [ ] 8-point and 5-point algorithms, ransac outlier rejection, and 3d triangulation

### 03. feature detection, description, and optical flow
- [ ] corner and keypoint detectors: harris corner detector, fast (features from accelerated segment test)
- [ ] scale and rotation invariant descriptors: sift (scale-invariant feature transform), orb (oriented fast and rotated brief)
- [ ] feature matching: nearest neighbor ratio test (lowe's ratio), flann indexing, and brute-force matching
- [ ] sparse optical flow: lucas-kanade differential method and pyramidal klt tracking
- [ ] dense optical flow: horn-schunck formulation and deep flow networks (raft)

### 04. deep visual perception and tracking
- [ ] object detection: anchor-based (yolo, faster r-cnn) and anchor-free / transformer-based (detr) architectures
- [ ] oriented bounding boxes (obb) and aerial imagery detection (visdrone, dota datasets)
- [ ] semantic and instance segmentation: mask r-cnn, unet, and segment anything (sam)
- [ ] multi-object tracking: kalman filter state prediction, hungarian matching algorithm, and deep re-identification (bytetrack, botsort)

---

## curated resources

### video lectures & course series
- [shree nayar – first principles of computer vision (columbia university)](https://www.youtube.com/@FirstPrinciplesofComputerVision): comprehensive video lectures from a world authority on camera optics, radiometric calibration, edge detection, and stereo vision.
- [cyrill stachniss – photogrammetry and image analysis (university of bonn)](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQh_J16imsvzi58vCwUTnP_): rigorous academic course covering epipolar geometry, feature matching, and structure-from-motion.
- [nicolai nielsen – computer vision and object tracking](https://www.youtube.com/@NicolaiNielsen): practical engineering tutorials on modern object detection, bytetrack, and deepsort tracking in c++ and python.

### foundational books & academic materials
- [computer vision: algorithms and applications (richard szeliski)](https://szeliski.org/Book/): freely available standard reference textbook covering classical processing to modern computational photography.
- [multiple view geometry in computer vision (richard hartley & andrew zisserman)](https://www.cambridge.org/core/books/multiple-view-geometry-in-computer-vision/4481D0E0FFC45644C43CE7B08B6E3C06): the definitive foundational bible for epipolar geometry, projective transformations, and camera calibration.
- [opencv official documentation and c++ tutorials](https://docs.opencv.org/4.x/): production c++ api references and mathematical tutorials for real-time vision pipelines.

### open-source codebases & tools
- [opencv/opencv](https://github.com/opencv/opencv): open source computer vision and machine learning software library.
- [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics): modern object detection, segmentation, and pose estimation framework.
- [ifzhang/bytetrack](https://github.com/ifzhang/ByteTrack): fast and robust multi-object association and tracking algorithm.
