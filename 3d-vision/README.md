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

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **3blue1brown – visualizing quaternions (4d numbers) & 3d rotation:** [youtube videosu](https://www.youtube.com/watch?v=d4EgbgTm0Bg) & [etkileşimli site (eater.net/quaternions)](https://eater.net/quaternions) — **[ilk izlenecek]** gimbal lock problemini ve kuaterniyonların (quaternions) 3b uzaydaki dönüş mantığını anlamak için en iyi kaynak
  2. **cyrill stachniss – 3d coordinate transformations, homogeneous coordinates & lie algebra:** [youtube ders videosu](https://www.youtube.com/watch?v=PvEl63t-opM) — **[ana mühendislik dersi]** robotik ve 3d vision'da koordinat eksenleri arası dönüşüm matrisleri ($se(3), so(3)$)
- **📖 oku (zorunlu referans makaleler — önem sırasıyla):**
  1. **a micro lie theory for state estimation in robotics (joan solà et al.):** [arxiv:1812.01537 (ücretsiz pdf)](https://arxiv.org/pdf/1812.01537.pdf) — **[başucu makalesi]** 3b dönüşümlerin türevlerini (jacobian) almak ve slam/kalman filtresi yazmak için zorunlu rehber
  2. **lie groups for 2d and 3d transformations (ethan eade):** [ethaneade.com/lie.pdf](https://ethaneade.com/lie.pdf) — c++ ile 3b geometri kodlarken elinin altında duracak formül referansı

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

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **shree nayar – stereo vision & depth estimation (first principles of cv):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo) — **[ilk izlenecek]** disparite (disparity), üçgenleme (triangulation) ve stereo derinlik hesabının temel fiziği
  2. **cyrill stachniss – stereo vision and multi-view stereo (mvs):** [youtube ders videoları](https://www.youtube.com/results?search_query=cyrill+stachniss+stereo+vision) — yoğun derinlik haritası (dense depth map) üretimi
- **📖 oku & 💻 repo (doküman ve sota modeller — önem sırasıyla):**
  1. **opencv depth map from stereo images tutorial:** [docs.opencv.org/4.x/dd/d53/tutorial_py_depthmap.html](https://docs.opencv.org/4.x/dd/d53/tutorial_py_depthmap.html) — stereobm ve stereosgbm ile klasik derinlik haritası çıkarma kodu
  2. **depth anything & depth anything v2 (yang et al.):** [arxiv:2401.10891](https://arxiv.org/abs/2401.10891) & [github repo (depthanything/depth-anything-v2)](https://github.com/DepthAnything/Depth-Anything-V2) — **[tek kameradan derinlikte dünya zirvesi]** tek bir rgb kameradan (monocular) yüksek hassasiyetli bağıl ve metrik derinlik kestirimi
  3. **foundationstereo: zero-shot stereo matching (nvidia research – cvpr 2025 best paper nomination):** [nvlabs.github.io/foundationstereo](https://nvlabs.github.io/FoundationStereo/) & [github repo (nvlabs/foundationstereo)](https://github.com/NVlabs/FoundationStereo) — **[stereo derinlikte dünya zirvesi]** çift kamera (stereo) görüntülerinden sıfır-atış (zero-shot) genelleme ile yoğun disparite, metrik ölçekli derinlik haritası ve 3b nokta bulutu üreten, jetson/tensorrt optimize nvidia temel modeli
  4. **defm: depth foundation model for robot navigation (eth zürich rsl – marco hutter):** [github repo (leggedrobotics/defm)](https://github.com/leggedrobotics/defm) — **[robotik için metrik derinlik vakıf modeli]** anymal ekibinin geliştirdiği; bacaklı ve otonom mobil robotların tek kameradan (monocular) doğrudan metre cinsinden metrik derinlik ve 3b nokta bulutu üreterek haritalama (elevation mapping) ve engelden kaçma yapmasını sağlayan açık kaynak derinlik temel modeli

#### 7.3 3d reconstruction

- [ ] structure from motion (sfm)
- [ ] multi-view geometry
- [ ] bundle adjustment
- [ ] camera pose estimation (pnp algoritmaları)
- [ ] sparse reconstruction
- [ ] dense reconstruction
- [ ] point cloud generation
- [ ] mesh reconstruction
- [ ] surface reconstruction
- [ ] modern küresel structure-from-motion (glomap)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe akademik kaynaklar):**
  1. **odtü ceng 483 & itü blg 453e – 3b görü ve çoklu görünüm geometrisi modülleri:** [odtü ceng](https://user.ceng.metu.edu.tr/~skalkan/)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – photogrammetry ii (structure from motion, pnp & bundle adjustment):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y) — **[ilk izlenecek]** 2b görüntülerden 3b kamera pozunu (pnp) ve 3b nokta bulutunu (sfm & bundle adjustment) adım adım çıkarma
  2. **prof. daniel cremers – multiple view geometry in computer vision (tum):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — **[ileri akademik ders]** çoklu görünümde 3b yeniden yapılandırma matematiği
- **📖 oku & 💻 repo (endüstriyel c++ kodları ve kitaplar — önem sırasıyla):**
  1. **repo & doküman – colmap (structure-from-motion and multi-view stereo):** [colmap.github.io](https://colmap.github.io/) & [github.com/colmap/colmap](https://github.com/colmap/colmap) — **[endüstri standardı c++ kodu]** hem nerf/3dgs öncesi kamera pozu çıkarmak için kullanılan hem de c++ ile sfm/bundle adjustment mimarisini öğrenmek için incelenecek açık kaynak proje
  2. **multiple view geometry in computer vision (hartley & zisserman – bölüm 17 & 18):** [robots.ox.ac.uk/~vgg/hzbook](https://www.robots.ox.ac.uk/~vgg/hzbook/) — sfm ve bundle adjustment'ın teorik referansı
  3. **glomap: global structure-from-motion revisited (colmap team – cvpr / eccv):** [github repo (colmap/glomap)](https://github.com/colmap/glomap) — **[modern küresel sfm standardı]** efsanevi colmap ekibinin geliştirdiği; geleneksel artımsal (incremental) sfm yerine küresel poz grafiği optimizasyonu yaparak 10 kat daha hızlı ve geniş ölçekli 3b nokta bulutu ve kamera pozu çıkaran modern c++ sfm standardı

#### 7.4 point cloud processing

- [ ] point cloud fundamentals
- [ ] point cloud registration & graph slam (open3d_slam)
- [ ] kiss-icp (bonn prbonn) & hızlı lidar odometri
- [ ] scan context (kaist url) & lidar döngü kapatma
- [ ] icp (iterative closest point)
- [ ] generalized icp
- [ ] pointnet
- [ ] pointnet++
- [ ] point transformer
- [ ] voxelization
- [ ] octrees
- [ ] point cloud segmentation
- [ ] 3d object detection

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – point cloud registration & iterative closest point (icp):** [youtube ders videoları](https://www.youtube.com/results?search_query=cyrill+stachniss+icp+point+cloud) — **[ilk izlenecek]** lidar ve rgb-d sensörlerden gelen iki 3b nokta bulutunu hizalayan icp ve svd algoritmalarının türetimi
  2. **open3d official youtube webinar & tutorial series:** [youtube kanalı](https://www.youtube.com/results?search_query=open3d+tutorial) — modern 3b veri işleme pratikleri
- **📖 oku & 💻 repo (kütüphane ve makaleler — önem sırasıyla):**
  1. **open3d official documentation (c++ & python):** [open3d.org/docs/release](https://www.open3d.org/docs/release/) & [github repo (isl-org/open3d)](https://github.com/isl-org/Open3D) — **[ilk kullanılacak kütüphane]** voxelization, octree, icp, yüzey oluşturma ve 3b görselleştirme için en modern c++/python kütüphanesi
  2. **point cloud library (pcl – c++ endüstri standardı):** [pointclouds.org](https://pointclouds.org/) & [pcl tutorials](https://pcl.readthedocs.io/projects/tutorials/en/master/) — **[ros 2 & c++ standardı]** otonom araçlarda ve ros 2'de lidar verisi işlemek için kullanılan klasik c++ kütüphanesi
  3. **pointnet: deep learning on point sets for 3d classification and segmentation (qi et al., stanford):** [arxiv:1612.00593](https://arxiv.org/abs/1612.00593) — 3b nokta bulutları üzerinde derin öğrenmeyi başlatan temel makale
  4. **open3d slam: pointcloud-based graph slam (eth zürich rsl – marco hutter):** [github repo (leggedrobotics/open3d_slam)](https://github.com/leggedrobotics/open3d_slam) — **[open3d tabanlı 3b nokta bulutu slam standardı]** anymal robotunu geliştiren eth zürih ekibinin açık kaynak c++ projesi; open3d kütüphanesini kullanarak nokta-düzlem icp, genelleştirilmiş icp (gicp), alt-harita (submap) yönetimi, döngü kapatma (loop closure) ve poz grafı optimizasyonu (pgo) ile tam teşekküllü 3b lidar ve rgb-d slam mimarisi
  5. **kiss-icp: in defense of point-to-point icp – simple, robust & fast lidar odometry (university of bonn – cyrill stachniss / ieee ra-l 2023):** [github repo (prbonn/kiss-icp)](https://github.com/PRBonn/kiss-icp) & [dokümantasyon](https://cims.nyu.edu/~vittal/kiss-icp/) — **[modern lidar odometri ve nokta bulutu kayıt standardı]** prof. cyrill stachniss ekibinin geliştirdiği; karmaşık özellik çıkarımı veya imu gerektirmeden, adaptif eşikleme (adaptive thresholding) ve basit nokta-nokta icp ile tek bir cpu çekirdeğinde 100+ hz hızla çalışan, ouster, hesai ve velodyne sensörleri için 2.4k+ yıldızlı modern c++/python lidar odometri paketi
  6. **scan context: place recognition & loop detection for 3d lidar slam (kaist url – giseop kim & hyun myung / ieee t-ro & iros):** [github repo (gisbi-kim/scancontext)](https://github.com/gisbi-kim/ScanContext) & [sc-lego-loam (github)](https://github.com/gisbi-kim/SC-LeGO-LOAM) — **[lidar slam döngü kapatma ve konum tanıma dünya standardı]** prof. hyun myung ekibinin geliştirdiği; 3b nokta bulutlarını azimut ve radyal halkalara bölerek görüş açısı ve sensör yöneliminden bağımsız çalışan, lio-sam ve a-loam gibi sistemlere entegre edilerek drift birikimini sıfırlayan ve küresel haritada yer tanıyan 2.2k+ yıldızlı açık kaynak lidar tanımlayıcısı (descriptor)

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

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **yannic kilcher & two minute papers – nerf & 3d gaussian splatting explanations:** [youtube videosu (3dgs)](https://www.youtube.com/watch?v=HVv_IQKlafQ) — **[ilk izlenecek]** nerf ve 3d gaussian splatting'in neden devrim yarattığının görsel ve matematiksel özeti
  2. **prof. frank dellaert (georgia tech) – 3d gaussian splatting & spatial ai lectures:** [youtube kanalı & sunumlar](https://www.youtube.com/results?search_query=frank+dellaert+spatial+ai) — robotik haritalama ve mekânsal yapay zekâ (spatial ai) perspektifi
- **📖 oku & 💻 repo (makale ve resmi kodlar — önem sırasıyla):**
  1. **3d gaussian splatting for real-time radiance field rendering (kerbl et al., siggraph 2023):** [arxiv:2308.04079](https://arxiv.org/abs/2308.04079) & [resmi repo (graphdeco-inria/gaussian-splatting)](https://github.com/graphdeco-inria/gaussian-splatting) — **[gerçek zamanlı 3b sahne temsili]** 100+ fps hızında fotogerçekçi 3b sahne oluşturma ve cuda rasterizer kodu
  2. **nerf: representing scenes as neural radiance fields for view synthesis (mildenhall et al., eccv 2020):** [arxiv:2003.08934](https://arxiv.org/abs/2003.08934) & [proje sayfası](https://www.matthewtancik.com/nerf) — hacimsel ışın izleme (volumetric rendering) ve sinirsel sahne temsillerinin kurucu makalesi
  3. **repo – nerfstudio-project/nerfstudio:** [docs.nerf.studio](https://docs.nerf.studio/) & [github repo](https://github.com/nerfstudio-project/nerfstudio) — nerf ve gaussian splatting modellerini kendi videolarınla kolayca eğitmek için modüler çerçeve
  4. **kimera & kimera-semantics: metric-semantic slam & 3d scene graphs (mit spark lab – icra / ieee t-ro):** [spark-lab.mit.edu/kimera](https://github.com/MIT-SPARK/Kimera) · [kimera (github)](https://github.com/MIT-SPARK/Kimera) · [kimera-semantics (github)](https://github.com/MIT-SPARK/Kimera-Semantics) — **[metrik-semantik haritalama & 3b mesh rekonstrüksiyonu]** prof. luca carlone ekibinin geliştirdiği; 2b derin öğrenme segmentasyonlarını stereo/rgb-d nokta bulutlarıyla hacimsel tsdf (voxblox) üzerinde birleştirerek anlık 3b semantik örgü (mesh) ve nesne/oda hiyerarşisi (3d dynamic scene graphs) kuran dünya standardı açık kaynak spatial ai kütüphanesi

---

### 02. computer graphics, rendering & simulation – bilgisayar grafikleri, görüntü oluşturma ve simülasyon

#### 40.1 graphics fundamentals – bilgisayar grafikleri temelleri

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

#### 40.2 geometry processing – geometri ve mesh işleme

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

#### 40.3 graphics apis & tools – grafik api’leri ve motorları

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

#### 40.4 differentiable & neural rendering – türevlenebilir ve sinirsel görüntü oluşturma

- [ ] differentiable rasterization
- [ ] differentiable ray tracing
- [ ] inverse rendering
- [ ] relighting
- [ ] text-to-3d (dreamfusion)
- [ ] image-to-3d and large reconstruction models
- [ ] 3d generative models
- [ ] 4d generation
- [ ] avatar generation (3dmm, neural avatars)

#### 40.5 physics simulation & synthetic data – fizik simülasyonu ve sentetik veri üretimi

- [ ] rigid body simulation
- [ ] soft body and cloth simulation
- [ ] fluid simulation (sph, eulerian)
- [ ] finite element method (fem)
- [ ] position-based dynamics
- [ ] differentiable simulators
- [ ] synthetic data pipelines (blender, unreal, isaac sim)
- [ ] procedural world generation

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (doğrudan yt 1. sıradaki ders ve learnopengl üzerinden ilerle).
- ▶️ **yt:**
  1. **[ilk izlenecek — bilgisayar grafikleri & geometri]** [cmu 15-462 / 15-662 — computer graphics (keenan crane — youtube)](https://www.youtube.com/playlist?list=PL9_jI1bdZmz2emSh0UQ5iOdT2xRHFHL7E) — model-view-projection matrisleri (kamera projeksiyonunun ikizi), rasterizasyon, mesh işleme, sdf ve ışın izleme.
  2. **[hızlı giriş]** [games101 — introduction to computer graphics (lingqi yan — youtube)](https://www.youtube.com/playlist?list=PL_w_qWAQZtAZhtzPI5pkAtcUVgmzdAP8g) — dönüşüm matrisleri, gölgeleme ve fiziksel tabanlı görüntü oluşturma (pbr).
  3. **ten minute physics (dr. matthias müller / nvidia physx):** [matthias-research.github.io/pages/tenminutephysics](https://matthias-research.github.io/pages/tenMinutePhysics/) & [youtube kanalı](https://www.youtube.com/@TenMinutePhysics) — nvidia'nın baş fizik araştırmacısından; parçacık simülasyonu, kumaş fiziği, rijit cisim dinamikleri ve robotik çarpışma motorlarını sıfırdan c++/javascript ile kodlama dersleri.
- 📖 **oku & 💻 repo:**
  1. [learnopengl — joey de vries (learnopengl.com)](https://learnopengl.com/) — c++ ile koordinat sistemleri, kamera matrisleri, z-buffer ve shader programlamanın uygulamalı rehberi.
  2. [matt pharr, wenzel jakob & greg humphreys — physically based rendering: from theory to implementation (pbr-book.org — ücretsiz online)](https://pbr-book.org/) & [mitsuba 3 differentiable renderer (github)](https://github.com/mitsuba-renderer/mitsuba3) — ışın izleme ve türevlenebilir görüntü oluşturma (differentiable rendering).
  3. [blenderproc — procedural blender pipeline for photorealistic synthetic data (dlr-rm github)](https://github.com/DLR-RM/BlenderProc) & [nvidia warp (github)](https://github.com/NVIDIA/warp) — derin öğrenme modelleri için fotogerçekçi sentetik veri üretimi ve gpu fizik simülasyonu.
