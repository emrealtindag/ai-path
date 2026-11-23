# state estimation and sensor fusion

engineering curriculum, mathematical representations, stochastic filtering, and curated resources for inertial navigation, kalman filtering, and multi-sensor fusion.

---

## architecture overview

```
[sensors: imu / gnss / wheel encoders / barometer / camera]
                              │
                              ▼
        [stochastic noise modeling: allan variance / bias]
                              │
                              ▼
            [state prediction: strapdown kinematics]
                              │
                              ▼
       [measurement update: kalman gain / innovation]
                              │
                              ▼
         [fused state output: pose / velocity / biases]
```

---

## complete checklist and resources

### 10.1 sensor fundamentals

- [ ] imu (inertial measurement unit)
- [ ] accelerometers
- [ ] gyroscopes
- [ ] magnetometers
- [ ] gps/gnss
- [ ] cameras
- [ ] lidar
- [ ] radar
- [ ] wheel encoders
- [ ] barometers
- [ ] ultrasonic sensors
- [ ] sensor noise models (white noise, random walk)
- [ ] sensor calibration

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – sensors and sensing (imu, lidar, camera, gnss & noise models):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[ilk izlenecek]** otonom sistemlerde kullanılan tüm sensörlerin fiziği, hata modelleri ve kalibrasyonu
  2. **brian douglas – sensor fusion & imu fundamentals:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLn8PRpmsu08ryYoBpEKzoMOveSTyS-h4a) — ivmeölçer, jiroskop, manyetometre ve gps'in neden tek başına yetmediği (drift vs noise)
- **oku (teknik kılavuz ve kitaplar — önem sırasıyla):**
  1. **vectornav inertial navigation primer (ücretsiz teknik el kitabı):** [vectornav.com/resources/inertial-navigation-primer](https://www.vectornav.com/resources/inertial-navigation-primer) — **[en iyi sensör rehberi]** imu çalışma prensipleri, white noise, bias instability, allan variance ve referans çerçeveleri için endüstriyel kılavuz
  2. **introduction to random signals and applied kalman filtering (brown & hwang):** [wiley kitap sayfası](https://www.wiley.com/en-us/Introduction+to+Random+Signals+and+Applied+Kalman+Filtering+with+Matlab+Exercises%2C+4th+Edition-p-9780470609699) — stokastik süreçler ve sensör gürültü modellemesi

### 10.2 state estimation

- [ ] state-space models
- [ ] system observability
- [ ] measurement models
- [ ] process models
- [ ] noise models
- [ ] covariance
- [ ] bayesian estimation

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – probabilistic state estimation & bayes filter:** [youtube ders videosu](https://www.youtube.com/watch?v=0lKHFJpaZvE) — **[ilk izlenecek]** bayes filtresinin (prediction + correction adımları) ve kovaryans yayılımının matematiksel temeli
- **oku (temel referans kitaplar — önem sırasıyla):**
  1. **probabilistic robotics (sebastian thrun, wolfram burgard, dieter fox – mit press):** [probabilistic-robotics.org](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — **[temel başvuru kitabı]** bölüm 2, 3 ve 4: durum kestirimi ve olasılıksal robotiğin kurucu eseri
  2. **state estimation for robotics (timothy d. barfoot – university of toronto):** [asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf (ücretsiz resmi tam kitap pdf)](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf) — **[ileri seviye başucu kitabı]** doğrusal/doğrusal olmayan durum kestirimi ve 3b lie grupları ($se(3)$) üzerinde sensör füzyonu (ücretsiz pdf)

### 10.3 filtering

- [ ] moving average filter
- [ ] low-pass filter
- [ ] high-pass filter
- [ ] complementary filter
- [ ] kalman filter (kf)
- [ ] extended kalman filter (ekf)
- [ ] unscented kalman filter (ukf)
- [ ] particle filter (sequential monte carlo)
- [ ] information filter
- [ ] error-state kalman filter (eskf)
- [ ] 24-state havacılık ekf mimarisi (inertialnav / px4 ekf2)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **michel van biezen – the kalman filter series (1d & multi-dimensional):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT) — **[ilk izlenecek]** kalman kazancı (kalman gain) ve kovaryans matrislerinin kağıt-kalemle en sade sayısal türetimi
  2. **cyrill stachniss – kalman filter (kf), extended kalman filter (ekf), ukf & particle filter:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[ana mühendislik dersi]** doğrusal olmayan sistemlerde jacobian ile ekf, sigma noktaları ile ukf ve parçacık filtreleri
- **oku & repo (interaktif kitap, makale ve gerçek kodlar — önem sırasıyla):**
  1. **kalman and bayesian filters in python (roger r. labbe jr.):** [github.com/rlabbe/kalman-and-bayesian-filters-in-python (ücretsiz interaktif kitap)](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) — **[uygulamalı interaktif kaynak]** sıfırdan kf, ekf, ukf ve particle filter'ı jupyter notebook üzerinde adım adım kodlayarak öğreten açık kaynak kitap
  2. **quaternion kinematics for the error-state kalman filter – eskf (joan solà):** [arxiv:1711.02508 (ücretsiz pdf)](https://arxiv.org/pdf/1711.02508.pdf) — **[iha & 3b navigasyon için zorunlu]** modern uçuş kontrolcülerinde (px4, ardupilot) kullanılan error-state kalman filter (eskf) ve kuaterniyon entegrasyonunun başucu makalesi
  3. **repo – commaai/openpilot (`rednose`kalman filter):** [github.com/commaai/openpilot](https://github.com/commaai/openpilot) — gerçek otonom araçta çalışan sembolik/c++ kalman filtresi implementasyonu
  4. **inertialnav: 24-state extended kalman filter for aerospace navigation (paul riseborough):** [github repo (priseborough/inertialnav)](https://github.com/priseborough/InertialNav) — **[px4 ve ardupilot ekf motorunun matematiksel ve c++ kaynağı]** px4 (ecl/ekf2) ve ardupilot (ekf2/ekf3) navigasyon filtresinin baş mimarı paul riseborough'nun açık kaynak reposu; kuaterniyon tabanlı 3b yönelim, hız, konum, gyro/ivmeölçer biasları, dünya manyetik alanı ve rüzgar kestiriminin sympy sembolik türetimlerini ve saf c++ filtre kodunu içeren havacılık standartı

### 10.4 advanced sensor fusion

- [ ] imu-camera fusion
- [ ] visual-inertial odometry (vio & msckf)
- [ ] gnss-imu fusion
- [ ] lidar-inertial odometry (lio)
- [ ] radar-camera fusion
- [ ] multi-sensor calibration
- [ ] multi-modal perception
- [ ] probabilistic sensor fusion
- [ ] thermal-inertial odometry (rovtio) & radar-inertial fusion
- [ ] okvis / okvis 2 (imperial srl) anahtar çerçeveli vio
- [ ] r3live & r3live++ (hku mars) lidar-görsel-ataletsel füzyon

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler & sunumlar — önem sırasıyla):**
  1. **hkust aerial robotics group (prof. shaojie shen) – vins-mono & vins-fusion presentations:** [youtube kanalı](https://www.youtube.com/@hkustaerialroboticsgroup6329) — **[ilk izlenecek sunum]** gps olmayan ortamlarda uçan iha'ların kamera + imu füzyonu (vio) ile nasıl konum bulduğu
  2. **hku mars lab (prof. fu zhang) – fast-lio, fast-lio2 & r3live presentations:** [youtube kanalı](https://www.youtube.com/@marslabhku1418) — lidar + imu ve kamera sıkı bağlı (tightly-coupled) odometri mimarisi
  3. **joan solà (iri csic-upc) – course on slam & micro lie theory:** [youtube video serisi (joan solà)](https://www.youtube.com/results?search_query=joan+sola+slam) — **[temel matematik dersi]** fast-lio, r3live ve vins'in kalbinde yatan 3b dönüşümler ($so(3)/se(3)$), lie cebiri, imu ön-entegrasyonu (pre-integration) ve manifold üzerinde durum kestirimi matematiğini tahtada adım adım türeten başvuru ders serisi
  4. **prof. frank dellaert (georgia tech csx803-amr) – factor graphs, invariant ekf & sensor fusion:** [youtube sunum & dersleri](https://www.youtube.com/results?search_query=frank+dellaert+factor+graphs) — **[ileri optimizasyon dersi]** gtsam kütüphanesinin yaratıcısından; isam2 faktör grafikleri, kayan pencere (sliding window) optimizasyonu ve çok sensörlü (kamera, lidar, imu) füzyonun teorik mimarisi
- **oku & repo (altın değerinde c++ kod tabanları — önem sırasıyla):**
  1. **vins-mono: a robust and versatile monocular visual-inertial state estimator (qin, li, shen – ieee t-ro):** [arxiv:1708.03852](https://arxiv.org/abs/1708.03852) & [c++ repo (hkust-aerial-robotics/vins-mono)](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) — **[iha görsel-ataletsel odometri c++ reposu]** imu ön-entegrasyonu (pre-integration) ve kayan pencere (sliding window) optimizasyonunun c++ kodu
  2. **fast-lio2: fast direct lidar-inertial odometry (xu, zhang et al. – ieee t-ro):** [arxiv:2107.06829](https://arxiv.org/abs/2107.06829) & [c++ repo (hku-mars/fast_lio)](https://github.com/hku-mars/FAST_LIO) — **[en hızlı lidar-imu füzyonu]** ikd-tree veri yapısı ve iterated kalman filter kullanan endüstri standardı c++ paketi
  3. **repo – tixiaoshan/lio-sam:** [github.com/tixiaoshan/lio-sam](https://github.com/TixiaoShan/LIO-SAM) — gtsam faktör grafikleri üzerinde lidar + imu + gps füzyonu yapan çok temiz c++ reposu
  4. **açık üniversite müfredatı – georgia tech csx803-amr (prof. frank dellaert):** [dellaert.github.io/26s-amr](https://dellaert.github.io/26S-AMR/) & [github repo (dellaert/26s-amr)](https://github.com/dellaert/26S-AMR) — **[2026 bahar ileri mobil robotik dersi]** sualtı (swim), dört bacaklı/insansı (walk), kara aracı (drive) ve drone/iha (fly) üzerinde lie grupları ($se(3)$), invariant ekf, faktör grafları (gtsam), imu preintegration, lio ve sürekli zamanlı slam (ct-slam) projeleri içeren dünya standartlarında açık kaynak üniversite müfredatı
  5. **msckf vio: multi-state constraint kalman filter (upenn grasp lab – ieee ra-l / iros):** [github repo (kumarrobotics/msckf_vio)](https://github.com/KumarRobotics/msckf_vio) — **[filtre tabanlı vio referans c++ reposu]** efsanevi vijay kumar laboratuvarının geliştirdiği; harita noktalarını durum vektöründe tutmayıp kayan poz penceresi üzerinde geometrik kısıt uygulayarak $\mathcal{o}(n)$ lineer karmaşıklıkla gömülü işlemcilerde ve otonom mikro-iha'larda yüksek frekanslı stereo kamera+imu konumlandırması yapan endüstri standardı ekf mimarisi
  6. **kimera-vio & kimera-vio-ros (mit spark lab – ieee t-ro):** [kimera-vio (github)](https://github.com/MIT-SPARK/Kimera-VIO) · [kimera-vio-ros (github)](https://github.com/MIT-SPARK/Kimera-VIO-ROS) — **[gtsam tabanlı stereo vio standartı]** prof. luca carlone ekibinin geliştirdiği; stereo kamera ve imu verilerini gtsam isam2 faktör grafiği üzerinde kayan pencereyle optimize eden, imu bias kestirimi ve gerçek zamanlı 3b örgü (mesh) üreten endüstri ve akademi standardı ros/c++ vio motoru
  7. **rovtio & radvio: visual-thermal & radar-inertial odometry (ntnu arl / team cerberus):** [rovtio github (ntnu-arl/rovtio)](https://github.com/ntnu-arl/rovtio) & [radvio github (ntnu-arl/radvio)](https://github.com/ntnu-arl/radvio) — **[görsel-termal & radar-ataletsel odometri (zorlu koşullar)]** darpa subterranean challenge şampiyonu ekibin geliştirdiği; toz, duman, zifiri karanlık ve sis gibi optik kameraların ve lidar'ın çöktüğü yer altı ve afet senaryolarında termal kamera + imu (rovtio) ve 4d mmwave radar + kamera + imu (radvio) sıkı bağlı füzyonu yapan öncü c++ durum kestirimi algoritmaları
  8. **okvis & okvis 2: open keyframe-based visual-inertial slam (imperial college london srl & tu munich – stefan leutenegger / ieee t-ro):** [github repo (smartroboticslab/okvis2)](https://github.com/SmartRoboticsLab/okvis2) & [github legacy (ethz-asl/okvis)](https://github.com/ethz-asl/okvis) — **[optimizasyon tabanlı anahtar çerçeve vio mimarisi]** prof. stefan leutenegger ekibinin geliştirdiği; ceres solver üzerinde kayan pencere (sliding window) faktör grafiği optimizasyonu yapan, imu ön-entegrasyonu ve anahtar çerçeve marjinalizasyonu (marginalization) teorisini literatüre kazandıran 1.5k+ yıldızlı c++ görsel-eylemsiz durum kestirimi motoru
  9. **r3live & r3live++: real-time rgb-colored lidar-inertial-visual state estimation & radiance mesh (hku mars lab – fu zhang / icra & ieee t-ro):** [github repo (hku-mars/r3live)](https://github.com/hku-mars/r3live) — **[lidar-görsel-ataletsel füzyon & fotogerçekçi 3b haritalama]** prof. fu zhang laboratuvarının geliştirdiği; lidar, imu ve optik kamerayı sıkı bağlı (tightly-coupled) iki alt mimaride (lio ve vio) birleştiren, gerçek zamanlı milimetrik durum kestirimiyle birlikte ortamın renkli ve fotogerçekçi 3b radyan (radiance) yüzey örgüsünü (mesh) oluşturan 2.7k+ yıldızlı çoklu-modalite sensör füzyonu başyapıtı

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

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – markov localization, grid localization & monte carlo localization (mcl):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[ilk izlenecek]** bir robotun bilinen harita içinde kendi konumunu olasılıksal olarak nasıl bulduğunun en net anlatımı
  2. **eth zürich – autonomous mobile robots (localization module – prof. roland siegwart):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — tekerlek odometrisi hata modelleri ve harita tabanlı lokalizasyon
- **oku & doküman (önem sırasıyla):**
  1. **probabilistic robotics – bölüm 7 & 8 (mobile robot localization: markov & grid/monte carlo):** [probabilistic-robotics.org](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) — lokalizasyon algoritmalarının teorik temeli
  2. **ros 2 nav2 amcl (adaptive monte carlo localization) configuration guide:** [docs.nav2.org/configuration/packages/configuring-amcl.html](https://docs.nav2.org/) — gerçek robotta parçacık filtresi lokalizasyonunu ayarlama rehberi
  3. **maplab: an open framework for visual-inertial mapping and localization (eth zürich asl – roland siegwart):** [github repo (ethz-asl/maplab)](https://github.com/ethz-asl/maplab) & [dokümantasyon](https://github.com/ethz-asl/maplab) — **[görsel-ataletsel haritalama ve lokalizasyon çerçevesi]** prof. roland siegwart ekibinin geliştirdiği; robotun daha önce çıkarılmış bir harita içinde kamera+imu ile 6-dof santimetrik konumunu bulmasını sağlayan (visual-inertial localization), çoklu oturum (multi-session) ve çoklu robot harita birleştirmesi (map merging) yapan 2.8k+ yıldızlı c++ otonomi motoru
  4. **dpgo & clipper: distributed pose graph optimization & robust data association (mit acl – ieee t-ro):** [dpgo (github)](https://github.com/mit-acl/dpgo) · [clipper (github)](https://github.com/mit-acl/clipper) — **[çoklu robot slam & graf tabanlı veri eşleme]** merkezi bir sunucuya ihtiyaç duymadan çoklu robotların pose graph'larını dağıtık riemann optimizasyonu ile çözen (dpgo) ve aşırı gürültülü/aykırı değer içeren ortamlarda graf-teorisi (clique) ile geometrik veri eşlemesi yapan c++ kütüphaneleri
