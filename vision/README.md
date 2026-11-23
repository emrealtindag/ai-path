# computer vision

engineering curriculum, algorithmic foundations, geometric representations, and curated resources for 2d image processing, classical feature extraction, applied vision, and deep visual perception.

---

## architecture overview

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

## complete checklist and resources

### 01. computer vision

#### 6.1 image processing

- [ ] digital image fundamentals
- [ ] image representation
- [ ] color spaces (rgb, hsv, lab)
- [ ] image filtering
- [ ] gaussian blur
- [ ] median filtering
- [ ] edge detection
- [ ] canny
- [ ] sobel
- [ ] laplacian
- [ ] thresholding (otsu)
- [ ] morphological operations (dilation, erosion)
- [ ] histogram equalization
- [ ] image pyramids
- [ ] frequency domain processing
- [ ] fourier transform
- [ ] image restoration
- [ ] image enhancement

**resources:**

- **turkish resources:**
  1. **metu ceng 483 – introduction to computer vision (sinan kalkan & emre akbaş):** [academic page](https://kovan.ceng.metu.edu.tr/~sinan/) — university syllabus on image filtering, edge detection, and representations
  2. **itu blg 453e – computer vision:** [syllabus](https://www.sis.itu.edu.tr/TR/ogrenci/lisans/ders-planlari/plan/BLGE/201810.html) — turkish university computer vision syllabus and topics
  3. **bilgisayar kavramları – image processing:** [sadievrenseker.com](https://sadievrenseker.com/) — turkish intro to basic filters, morphology, and histogram equalization
  4. **zafer demirkol (@zaferdemirkol):** [youtube channel](https://www.youtube.com/@zaferdemirkol) — turkish talks on general ai and tensorflow
- **video lectures:**
  1. **shree nayar – first principles of computer vision (columbia university):** [youtube playlists](https://www.youtube.com/@firstprinciplesofcomputerv3258/playlists) — clear university lectures on image formation, filtering, edge detection, and frequency analysis
  2. **murtaza's workshop – opencv python & c++:** [youtube channel](https://www.youtube.com/@murtazasworkshop) — hands-on coding tutorials for opencv pipelines
- **books, papers & repositories:**
  1. **opencv 4.x image processing tutorials:** [docs.opencv.org](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html) — code walkthroughs for canny, sobel, otsu thresholding, morphology, and color spaces
  2. **digital image processing (gonzalez & woods):** [imageprocessingplace.com](http://www.imageprocessingplace.com/) — classic textbook on classical image processing

#### 6.2 classical computer vision

- [ ] feature detection
- [ ] harris corner detector
- [ ] fast
- [ ] sift
- [ ] surf
- [ ] orb
- [ ] brief
- [ ] feature description
- [ ] feature matching
- [ ] brute force matching
- [ ] flann
- [ ] ransac
- [ ] homography
- [ ] image registration
- [ ] optical flow
- [ ] lucas-kanade
- [ ] dense optical flow (farneback)
- [ ] background subtraction
- [ ] motion detection

**resources:**

- **turkish resources:**
  1. **metu ceng 483 – features, ransac & optical flow modules:** [course page](https://user.ceng.metu.edu.tr/~skalkan/)
- **video lectures:**
  1. **shree nayar – features, ransac, optical flow & tracking:** [youtube playlists](https://www.youtube.com/@firstprinciplesofcomputerv3258/playlists) — clear math lectures on harris corners, sift, homography, ransac, and lucas-kanade optical flow
  2. **cyrill stachniss – photogrammetry i & ii (university of bonn):** [youtube playlists](https://www.youtube.com/@CyrillStachniss/playlists) — feature detection and matching taught from a robotics, uav mapping, and slam perspective
- **books, papers & repositories:**
  1. **opencv feature detection & homography tutorials:** [docs.opencv.org](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html) — practical image matching tutorials with orb, sift, flann, and ransac
  2. **computer vision: algorithms and applications, 2nd ed. (richard szeliski):** [free pdf](https://szeliski.org/Book/) — chapters 7–9 covering feature matching, alignment, and optical flow
  3. **cvg/lightglue (eth zürich):** [github.com/cvg/lightglue](https://github.com/cvg/LightGlue) — fast learned local feature matcher outperforming classical sift/orb matching
  4. **zju3dv/loftr:** [github.com/zju3dv/loftr](https://github.com/zju3dv/LoFTR) — detector-free transformer matcher that handles low-texture surfaces

#### 6.3 camera geometry

- [ ] pinhole camera model
- [ ] intrinsic parameters ($k$)
- [ ] extrinsic parameters ($[r \mid t]$)
- [ ] camera calibration (zhang's method)
- [ ] lens distortion
- [ ] radial distortion
- [ ] tangential distortion
- [ ] perspective projection
- [ ] coordinate systems
- [ ] rotation matrices
- [ ] translation vectors
- [ ] homogeneous coordinates
- [ ] epipolar geometry
- [ ] fundamental matrix ($f$)
- [ ] essential matrix ($e$)
- [ ] stereo geometry

**resources:**

- **turkish resources:**
  1. **metu ceng 483 – camera model, calibration & stereo geometry notes:** [course page](https://user.ceng.metu.edu.tr/~skalkan/)
- **video lectures:**
  1. **shree nayar – camera calibration & epipolar geometry:** [youtube playlist](https://www.youtube.com/playlist?list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo) — clear intuitive breakdown of pinhole cameras, $k, [r\mid t]$ matrices, and essential/fundamental matrices
  2. **cyrill stachniss – camera calibration & epipolar geometry:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y) — step-by-step whiteboard matrix derivations for camera calibration and stereo geometry
  3. **prof. daniel cremers – multiple view geometry (tum):** [youtube lecture series](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — university course on 3d camera geometry and visual odometry math
- **books, papers & repositories:**
  1. **opencv camera calibration & 3d reconstruction tutorials:** [docs.opencv.org](https://docs.opencv.org/4.x/d9/db7/tutorial_py_table_of_contents_calib3d.html) — calibrating real cameras with a checkerboard and removing lens distortion
  2. **multiple view geometry in computer vision (hartley & zisserman):** [robots.ox.ac.uk/~vgg/hzbook](https://www.robots.ox.ac.uk/~vgg/hzbook/) — standard reference book on projective camera geometry, epipolar geometry, and 3d reconstruction
  3. **an invitation to 3-d vision (yi ma et al.):** [book page](https://link.springer.com/book/10.1007/978-0-387-21779-6) — textbook on rigid-body motion and multi-view geometry

#### 6.4 deep learning for vision

- [ ] cnn architectures
- [ ] lenet
- [ ] alexnet
- [ ] vgg
- [ ] resnet
- [ ] densenet
- [ ] efficientnet
- [ ] mobilenet
- [ ] convnext
- [ ] feature pyramid networks (fpn)
- [ ] attention mechanisms
- [ ] vision transformers (vit)
- [ ] swin transformer

**resources:**

- **turkish resources:**
  1. **metu ceng 501 – deep learning (sinan kalkan):** [course page](https://kovan.ceng.metu.edu.tr/~sinan/) & [github repo](https://github.com/sinankalkan/CENG501-Spring2021) — slides on resnet, fpn, vit, and visual deep learning
- **video lectures:**
  1. **stanford cs231n – deep learning for computer vision:** [youtube lecture series](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv) & [lecture notes](https://cs231n.github.io/) — classic stanford course on deep learning for visual tasks
  2. **michigan eecs 498-007 – deep learning for computer vision (justin johnson):** [youtube lecture series](https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r) — updated cs231n covering pytorch and vision transformers
- **books, papers & repositories:**
  1. **pytorch image models (`timm`):** [docs](https://huggingface.co/docs/timm/index) & [github repo](https://github.com/huggingface/pytorch-image-models) — standard library providing pretrained resnet, efficientnet, convnext, vit, and swin backbones
  2. **deep residual learning for image recognition – resnet (he et al.):** [arxiv:1512.03385](https://arxiv.org/abs/1512.03385) — foundational paper introducing residual skip connections
  3. **swin transformer (liu et al.):** [arxiv:2103.14030](https://arxiv.org/abs/2103.14030) — hierarchical vision transformer backbone for detection and segmentation
  4. **deeplearning-models (sebastian raschka):** [github repo](https://github.com/rasbt/deeplearning-models) — clean pure-pytorch notebooks for lenet, resnet, mobilenet, vaes, gans, and training tricks

#### 6.5 object detection

- [ ] two-stage detectors
- [ ] r-cnn
- [ ] fast r-cnn
- [ ] faster r-cnn
- [ ] one-stage detectors
- [ ] ssd
- [ ] yolo architectures (v1–v11)
- [ ] retinanet (focal loss)
- [ ] detr (detection transformer)
- [ ] real-time object detection
- [ ] object tracking
- [ ] non-maximum suppression (nms)

**resources:**

- **turkish resources:**
  1. **metu ceng 783 – object detection (r-cnn, yolo, detr) notes:** [course page](https://user.ceng.metu.edu.tr/~skalkan/DL/)
- **video lectures:**
  1. **justin johnson (eecs 498) – object detection lectures:** [youtube lecture video](https://www.youtube.com/watch?v=TB-fdISzpHQ) — clear breakdown of r-cnn, faster r-cnn, anchor boxes, nms, and yolo
  2. **murtaza's workshop – yolo custom object detection:** [youtube channel](https://www.youtube.com/@murtazasworkshop) — practical tutorials on training yolo on custom datasets and running live cameras
  3. **deeplearning.ai – object detection module:** [youtube playlist](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF) — fundamentals of iou, anchor boxes, and non-maximum suppression (nms)
- **books, papers & repositories:**
  1. **ultralytics yolo documentation:** [docs.ultralytics.com](https://docs.ultralytics.com/) & [github repo](https://github.com/ultralytics/ultralytics) — guide to training, validating, and exporting yolo models to onnx/tensorrt
  2. **detr & rt-detr (end-to-end detection with transformers):** [arxiv:2005.12872](https://arxiv.org/abs/2005.12872) & [rt-detr repo](https://github.com/lyuwenyu/RT-DETR) — nms-free transformer-based real-time object detection
  3. **open-mmlab/mmdetection:** [github.com/open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection) — modular object detection toolbox for research and benchmarking
  4. **hugging face trending papers & arxiv cs.cv:** [huggingface.co/papers/trending](https://huggingface.co/papers/trending) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — tracking latest computer vision papers and models

#### 6.6 image segmentation

- [ ] semantic segmentation
- [ ] instance segmentation
- [ ] panoptic segmentation
- [ ] fcn (fully convolutional networks)
- [ ] u-net
- [ ] deeplab (v1, v2, v3, v3+)
- [ ] mask r-cnn
- [ ] segformer
- [ ] mask2former
- [ ] segment anything models (sam, sam 2)

**resources:**

- **turkish resources:**
  1. **metu ceng 783 – semantic, instance & panoptic segmentation slides:** [course page](https://user.ceng.metu.edu.tr/~skalkan/DL/)
- **video lectures:**
  1. **stanford cs231n – detection and image segmentation:** [youtube lecture video](https://www.youtube.com/watch?v=nDPWywWRIRo) — theoretical foundations of fcn, transposed convolution, u-net, and mask r-cnn
  2. **digitalsreeni – image segmentation in python:** [youtube channel](https://www.youtube.com/@DigitalSreeni) — practical step-by-step training of u-net, mask r-cnn, and sam
- **books, papers & repositories:**
  1. **segment anything model 2 – sam 2 (meta ai):** [github repo](https://github.com/facebookresearch/sam2) & [paper (arxiv)](https://arxiv.org/abs/2408.00714) — real-time zero-shot segmentation across images and video
  2. **u-net (ronneberger et al.):** [arxiv:1505.04597](https://arxiv.org/abs/1505.04597) — classic encoder-decoder skip-connection architecture for pixel segmentation
  3. **mask r-cnn (he et al.):** [arxiv:1703.06870](https://arxiv.org/abs/1703.06870) — core instance segmentation paper introducing roialign
  4. **qubvel/segmentation_models.pytorch:** [github repo](https://github.com/qubvel-org/segmentation_models.pytorch) — easy pytorch library for u-net, deeplabv3+, and fpn segmentation models

#### 6.7 visual tracking

- [ ] single object tracking (sot)
- [ ] multiple object tracking (mot)
- [ ] kalman-based tracking
- [ ] sort (simple online and realtime tracking)
- [ ] deepsort
- [ ] bytetrack
- [ ] optical flow tracking
- [ ] appearance-based tracking
- [ ] re-identification (reid)
- [ ] tracking-by-detection

**resources:**

- **turkish resources:**
  1. **teknofest uav & air defense team technical notes:** turkish community open-source repos combining kalman filtering, yolo, and bytetrack
- **video lectures:**
  1. **nicolai nielsen – object tracking tutorials:** [youtube channel](https://www.youtube.com/@NicolaiAI) — practical tutorials on sort, deepsort, bytetrack, hungarian matching, and kalman filters in c++/python
  2. **roboflow – bytetrack & supervision tracking:** [youtube channel](https://www.youtube.com/@Roboflow) — assigning track ids, plotting paths, and speed/zone analytics
- **books, papers & repositories:**
  1. **bytetrack (zhang et al.):** [arxiv:2110.06864](https://arxiv.org/abs/2110.06864) & [github repo](https://github.com/ifzhang/ByteTrack) — robust multi-object tracking associating low-confidence boxes under occlusion (includes c++/tensorrt code)
  2. **deepsort (wojke et al.):** [arxiv:1703.07402](https://arxiv.org/abs/1703.07402) — multi-object tracking combining kalman motion estimation with visual appearance features
  3. **mikel-brostrom/boxmot:** [github.com/mikel-brostrom/boxmot](https://github.com/mikel-brostrom/boxmot) — modular tracking library wrapping bytetrack, bot-sort, deepocsort, and strongsort

#### 6.8 modern visual ai

- [ ] vision foundation models
- [ ] self-supervised vision
- [ ] dino
- [ ] dinov2
- [ ] dinov3
- [ ] clip (contrastive language-image pretraining)
- [ ] siglip
- [ ] sam / sam 2
- [ ] image embeddings
- [ ] visual representations
- [ ] image retrieval
- [ ] semantic similarity
- [ ] visual search
- [ ] cross-view matching
- [ ] few-shot recognition
- [ ] zero-shot recognition
- [ ] open-vocabulary detection
- [ ] open-vocabulary segmentation

**resources:**

- **video lectures:**
  1. **umar jamil – coding clip & vlms from scratch:** [youtube channel](https://www.youtube.com/@umarjamilai) — writing contrastive image-text alignment (clip) and embeddings from scratch in pytorch
  2. **yannic kilcher – dinov2 & clip paper breakdowns:** [dinov2 video](https://www.youtube.com/watch?v=h3ij3F3cPIk) & [clip video](https://www.youtube.com/watch?v=T9XSU0pKX2E) — detailed architecture breakdowns of self-supervised vision foundation models
  3. **ai coffee break with letitia:** [youtube channel](https://www.youtube.com/@AICoffeeBreak) — concise clear summaries of vision transformers, clip, dino, and siglip
- **books, papers & repositories:**
  1. **dinov2 (meta ai):** [arxiv:2304.07193](https://arxiv.org/abs/2304.07193) · [demo](https://dinov2.metademolab.com/) · [github repo](https://github.com/facebookresearch/dinov2) — strong self-supervised visual backbone for depth, retrieval, and cross-view matching without fine-tuning
  2. **clip (openai / open_clip):** [arxiv:2103.00020](https://arxiv.org/abs/2103.00020) & [github repo](https://github.com/mlfoundations/open_clip) — foundational paper and open-source training for open-vocabulary perception
  3. **siglip (google research):** [arxiv:2303.15343](https://arxiv.org/abs/2303.15343) — more efficient sigmoid loss successor to clip

#### 6.9 advanced vision research

- [ ] robust visual recognition
- [ ] domain generalization
- [ ] domain adaptation
- [ ] visual anomaly detection
- [ ] low-light vision
- [ ] night vision algorithms
- [ ] adverse weather perception
- [ ] motion blur robustness
- [ ] image super resolution
- [ ] image restoration
- [ ] video understanding
- [ ] temporal modeling
- [ ] event-based vision

**resources:**

- **video lectures:**
  1. **prof. davide scaramuzza (rpg lab, uzh) – event cameras & agile drones:** [youtube playlists](https://www.youtube.com/@ailabRPG/playlists) — sub-millisecond neuromorphic event cameras and high-speed autonomous uav perception
  2. **cvpr / iccv / eccv workshop recordings:** [computer vision foundation youtube](https://www.youtube.com/@ComputerVisionFoundation) — vision algorithms for fog, rain, low light, and motion blur
- **books, papers & repositories:**
  1. **event-based vision: a survey (gallego, scaramuzza et al.):** [arxiv:1904.08405 (free pdf)](https://arxiv.org/pdf/1904.08405.pdf) — comprehensive survey on event-based cameras and algorithms
  2. **openvinotoolkit/anomalib:** [github.com/openvinotoolkit/anomalib](https://github.com/openvinotoolkit/anomalib) — industrial deep learning library for visual anomaly and defect detection
  3. **hugging face trending & arxiv cs.cv:** [huggingface.co/papers/trending](https://huggingface.co/papers/trending) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — latest papers on image restoration, low-light vision, and super-resolution

---

### 02. applied vision

#### 38.1 ocr & document ai

- [ ] text detection (east, dbnet)
- [ ] text recognition (crnn, trocr)
- [ ] scene text recognition
- [ ] document layout analysis
- [ ] layoutlm and document transformers
- [ ] donut (ocr-free document understanding)
- [ ] table structure recognition
- [ ] handwriting recognition
- [ ] document vqa
- [ ] key information extraction
- [ ] tesseract, paddleocr, easyocr

#### 38.2 face & biometrics

- [ ] face detection (mtcnn, retinaface)
- [ ] face alignment and landmarks
- [ ] face recognition (facenet, arcface)
- [ ] verification vs identification
- [ ] liveness and anti-spoofing
- [ ] fingerprint and iris recognition
- [ ] gait recognition
- [ ] biometric privacy and regulation

#### 38.3 human understanding

- [ ] 2d human pose estimation (openpose, hrnet, rtmpose)
- [ ] 3d human pose and mesh recovery (smpl)
- [ ] hand pose estimation
- [ ] gaze estimation
- [ ] action recognition
- [ ] gesture recognition
- [ ] crowd counting
- [ ] pedestrian intent and trajectory prediction
- [ ] human motion prediction
- [ ] motion capture

#### 38.4 video understanding

- [ ] video classification (i3d, slowfast)
- [ ] video transformers (timesformer, vivit, videomae)
- [ ] temporal action localization
- [ ] video object segmentation
- [ ] video captioning and video qa
- [ ] deep optical flow (flownet, raft)
- [ ] video prediction
- [ ] frame interpolation
- [ ] long video understanding
- [ ] video compression basics (h.264, h.265)

#### 38.5 remote sensing & aerial imagery

- [ ] satellite and aerial image basics
- [ ] multispectral and hyperspectral imaging
- [ ] sar (synthetic aperture radar)
- [ ] thermal and infrared imaging
- [ ] aerial object detection (small and oriented objects)
- [ ] land cover segmentation
- [ ] change detection
- [ ] georeferencing and coordinate reference systems
- [ ] gis tools (qgis, gdal)
- [ ] aerial datasets (dota, visdrone, xview)
- [ ] geospatial foundation models
- [ ] uav imagery analytics

#### 38.6 captioning, grounding & visual reasoning

- [ ] image captioning
- [ ] referring expression comprehension
- [ ] visual grounding (grounding dino)
- [ ] scene graph generation
- [ ] dense captioning
- [ ] visual reasoning benchmarks

#### 38.7 image generation & editing

- [ ] inpainting and outpainting
- [ ] image-to-image translation (pix2pix, cyclegan)
- [ ] style transfer
- [ ] controlnet
- [ ] lora and dreambooth for diffusion
- [ ] ip-adapter
- [ ] instruction-based image editing
- [ ] image matting
- [ ] deblurring and denoising
- [ ] colorization
- [ ] deepfake generation and detection

**resources:**

- **turkish resource:** [itu / metu remote sensing & gis notes](https://www.itu.edu.tr/) — coordinate reference systems (crs), multispectral/sar imaging, and aerial photogrammetry basics
- **video lectures:**
  1. **raft (princeton vision & robotics):** [github.com/princeton-vl/raft](https://github.com/princeton-vl/RAFT) — deep optical flow estimation and motion analysis
  2. [qgis & gdal spatial analysis tutorials (spatial thoughts / youtube)](https://www.youtube.com/@SpatialThoughts) — georeferencing, coordinate transforms, and raster image processing
- **books, papers & repositories:**
  1. [mmrotate (github)](https://github.com/open-mmlab/mmrotate) & [ultralytics yolo obb](https://docs.ultralytics.com/tasks/obb/) — oriented bounding box and small object detection codebases for uav and satellite imagery
  2. [sahi — slicing aided hyper inference (github)](https://github.com/obss/sahi) — sliced inference library improving small object detection in high-res aerial imagery (visdrone, dota)
  3. [torchgeo (microsoft, github)](https://github.com/microsoft/torchgeo) — pytorch library for multispectral, hyperspectral, sar, and geospatial datasets
  4. [paddleocr (github)](https://github.com/PaddlePaddle/PaddleOCR) · [mmpose (github)](https://github.com/open-mmlab/mmpose) · [groundingdino (github)](https://github.com/IDEA-Research/GroundingDINO) — tools for ocr, human pose estimation, and open-vocabulary visual grounding
