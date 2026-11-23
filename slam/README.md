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
- [ ] tartanair & tartanvo slam kıyaslaması
- [ ] droid-slam (deep recurrent visual slam) & basalt vio

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – slam course (bonn üniversitesi):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[temel akademik slam dersi – ilk izlenecek]** odometri, ekf-slam, particle filter slam, pose graph optimization ve loop closure'ı baştan sona öğreten ders serisi
  2. **prof. daniel cremers – multiple view geometry & direct slam: lsd-slam, dso (tum):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — **[zirve akademik ders]** doğrudan piksel parlaklığı (photometric error) üzerinden çalışan direct slam ve görsel odometri
  3. **joan solà – course on slam & factor graphs:** [youtube oynatma listesi](https://www.youtube.com/results?search_query=joan+sola+slam) — faktör grafikleri (factor graphs) ve manifold üzerinde optimizasyon
  4. **prof. davide scaramuzza (uzh rpg) – vision algorithms for mobile robotics (vamr):** [youtube oynatma listesi / uzh vamr](https://www.youtube.com/playlist?list=PLdMorpQLjeXmbFaVku4JdjmQByHHqTd1F) & [ders sayfası (rpg.ifi.uzh.ch)](https://rpg.ifi.uzh.ch/teaching.html) — **[zirve görsel robotik dersi]** dünyanın en prestijli robotik algılama laboratuvarından (uzh rpg); görsel odometri, optik akış, kamera kalibrasyonu, epipolar geometri ve visual slam mimarilerini baştan sona anlatan altın standart amfi dersi
- **📖 oku & 💻 repo (makale ve endüstriyel c++ kod tabanları — önem sırasıyla):**
  1. **visual odometry: part i (the first 30 years and fundamentals) & part ii (photogrammetry and filter-based methods) – davide scaramuzza & friedrich fraundorfer:** [part i pdf (uzh rpg)](https://rpg.ifi.uzh.ch/docs/VO_Part_I_Scaramuzza.pdf) & [part ii pdf (uzh rpg)](https://rpg.ifi.uzh.ch/docs/VO_Part_II_Scaramuzza.pdf) — **[ilk okunacak tutorial makalesi]** görsel odometrinin tüm matematiğini 20 sayfada özetleyen başucu rehberi
  2. **orb-slam3: an accurate open-source library for visual, visual-inertial, and multimap slam (campos et al., ieee t-ro 2021):** [arxiv:2007.11898](https://arxiv.org/abs/2007.11898) — modern özellik tabanlı ve görsel-ataletsel (kamera+imu) slam'in referans makalesi
  3. **repo – uz-slamlab/orb_slam3 & raulmur/orb_slam2:** [github.com/uz-slamlab/orb_slam3](https://github.com/UZ-SLAMLab/ORB_SLAM3) · [github.com/raulmur/orb_slam2](https://github.com/raulmur/ORB_SLAM2) — **[satır satır okunacak c++ kodu]** gerçek zamanlı tracking, local mapping ve loop closing thread'lerinin c++ ile nasıl yazıldığını görmek için temel açık kaynak proje
  4. **kütüphane – gtsam (georgia tech smoothing and mapping library):** [gtsam.org](https://gtsam.org/) & [github repo (borglab/gtsam)](https://github.com/borglab/gtsam) — pose graph ve factor graph optimizasyonu için c++ kütüphanesi
  5. **mast3r-slam: real-time dense slam with 3d reconstruction priors (imperial college london / dyson robotics lab – cvpr 2025):** [edexheim.github.io/mast3r-slam](https://edexheim.github.io/mast3r-slam/) & [github repo (rmurai0610/mast3r-slam)](https://github.com/rmurai0610/MASt3R-SLAM) — **[yapay zekâ vakıf modeli tabanlı yoğun slam]** slam öncüsü andrew davison ve dyson robotik laboratuvarı'ndan çıkan; mast3r 3b temsilini kullanarak tek kameradan seyrek noktalar yerine fotogerçekçi yoğunlukta 3b harita ve gerçek zamanlı yörünge kestirimi yapan modern dense slam mimarisi
  6. **svo: semi-direct visual odometry (uzh rpg – icra / ieee t-ro):** [github (uzh-rpg/rpg_svo_pro_open)](https://github.com/uzh-rpg/rpg_svo_pro_open) & [github legacy (uzh-rpg/rpg_svo)](https://github.com/uzh-rpg/rpg_svo) — **[yarı-doğrudan görsel odometri]** davide scaramuzza ekibinin geliştirdiği; özellik çıkarımı maliyetini ortadan kaldırmak için doğrudan piksel parlaklık farkı (fotometrik hata) ile köşe takibini birleştiren, gömülü sistemlerde ve otonom iha'larda 55+ fps çalışan öncü semi-direct vo mimarisi
  7. **tartanair & tartanvo: visual slam & deep vo benchmark (cmu airlab – ieee/rsj iros & cvpr):** [theairlab.org/tartanair-dataset](https://theairlab.org/tartanair-dataset/) · [github repo (castacks/tartanair_tools)](https://github.com/castacks/tartanair_tools) & [github repo (castacks/tartanairpy)](https://github.com/castacks/tartanairpy) — **[görsel slam & optik akış kıyaslama standardı]** prof. sebastian scherer ekibinin geliştirdiği; fotogerçekçi unreal engine simülasyonunda zorlu hava koşulları, dinamik aydınlatma, optik akış ve ground-truth pozlarla visual slam ve derin görsel odometri (deep vo) modellerini eğitmek ve test etmek için kullanılan 1.000+ atıflı küresel kıyaslama standardı
  8. **droid-slam & basalt: deep visual slam & fast optimization-based vio (princeton vl & tu munich):** [droid-slam (github)](https://github.com/princeton-vl/DROID-SLAM) & [basalt (gitlab)](https://gitlab.com/VladyslavUsenko/basalt) — **[modern derin slam & yüksek hızlı vio standardı]** derin öğrenmeli optik akış ile klasik bundle adjustment'ı birleştiren droid-slam ve ceres optimizasyonunu lineer olmayan faktör geri kazanımıyla (factor recovery) harmanlayıp cpu üzerinde yüzlerce fps hızında çalışan basalt c++ vio mimarisi

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

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – markov localization, grid localization & monte carlo localization (mcl):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[ilk izlenecek]** bir robotun bilinen harita içinde kendi konumunu olasılıksal olarak nasıl bulduğunun en net anlatımı
  2. **eth zürich – autonomous mobile robots (localization module – prof. roland siegwart):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — tekerlek odometrisi hata modelleri ve harita tabanlı lokalizasyon
- **📖 oku & 💻 doküman (önem sırasıyla):**
  1. **probabilistic robotics – bölüm 7 & 8 (mobile robot localization: markov & grid/monte carlo):** [probabilistic-robotics.org](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — lokalizasyon algoritmalarının teorik temeli
  2. **ros 2 nav2 amcl (adaptive monte carlo localization) configuration guide:** [docs.nav2.org/configuration/packages/configuring-amcl.html](https://docs.nav2.org/) — gerçek robotta parçacık filtresi lokalizasyonunu ayarlama rehberi
  3. **maplab: an open framework for visual-inertial mapping and localization (eth zürich asl – roland siegwart):** [github repo (ethz-asl/maplab)](https://github.com/ethz-asl/maplab) & [dokümantasyon](https://github.com/ethz-asl/maplab) — **[görsel-ataletsel haritalama ve lokalizasyon çerçevesi]** prof. roland siegwart ekibinin geliştirdiği; robotun daha önce çıkarılmış bir harita içinde kamera+imu ile 6-dof santimetrik konumunu bulmasını sağlayan (visual-inertial localization), çoklu oturum (multi-session) ve çoklu robot harita birleştirmesi (map merging) yapan 2.8k+ yıldızlı c++ otonomi motoru
  4. **dpgo & clipper: distributed pose graph optimization & robust data association (mit acl – ieee t-ro):** [dpgo (github)](https://github.com/mit-acl/dpgo) · [clipper (github)](https://github.com/mit-acl/clipper) — **[çoklu robot slam & graf tabanlı veri eşleme]** merkezi bir sunucuya ihtiyaç duymadan çoklu robotların pose graph'larını dağıtık riemann optimizasyonu ile çözen (dpgo) ve aşırı gürültülü/aykırı değer içeren ortamlarda graf-teorisi (clique) ile geometrik veri eşlemesi yapan c++ kütüphaneleri
