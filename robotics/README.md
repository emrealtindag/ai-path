# robotics and embodied ai

engineering curriculum, mathematical modeling, middleware, physical ai, robotics foundation models, and curated resources for robot kinematics, rigid-body dynamics, ros 2, and physical simulation.

---

## architecture overview

```
[task / mission specification]
             │
             ▼
  [motion planning: c-space / rrt*]
             │
             ▼
  [kinematics & dynamics: jacobians / lagrangian]
             │
             ▼
  [middleware & coordination: ros 2 / tf2 / dds]
             │
             ▼
  [simulation & real-world: gazebo / isaac sim / hardware]
```

---

## complete checklist and resources

### 01. robotics – robotik

#### 8.1 robotics fundamentals

- [ ] robot types
- [ ] robot components
- [ ] degrees of freedom (dof)
- [ ] actuators
- [ ] motors (bldc, step, servo)
- [ ] encoders
- [ ] sensors
- [ ] coordinate frames
- [ ] robot configuration
- [ ] forward kinematics
- [ ] inverse kinematics
- [ ] workspace
- [ ] manipulators

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **kevin lynch – modern robotics: mechanics, planning, and control (northwestern university):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — **[ilk izlenecek – temel akademik ders]** vida teorisi (screw theory), konfigürasyon uzayı ve modern robotik matematiği
  2. **eth zürich – autonomous mobile robots (prof. roland siegwart):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — **[mobil robotik & otonomi dersi]** tekerlekli/uçan mobil robotlarda algılama, kinematik, lokalizasyon ve planlamayı birleştiren üniversite dersi
- **📖 oku (ücretsiz başucu kitapları — önem sırasıyla):**
  1. **modern robotics: mechanics, planning, and control (kevin m. lynch & frank c. park):** [modernrobotics.org (ücretsiz tam kitap pdf & kodlar)](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf) — python/matlab/c++ kütüphanesi (`modernrobotics`) ile birlikte gelen modern ders kitabı
  2. **introduction to robotics: mechanics and control (john j. craig):** [kitap sayfası](https://www.pearson.com/en-us/subject-catalog/p/introduction-to-robotics-mechanics-and-control/P200000003304) — klasik robotik mekaniği referansı

#### 8.2 robot kinematics

- [ ] homogeneous transformation
- [ ] denavit-hartenberg (d-h) parameters
- [ ] forward kinematics
- [ ] inverse kinematics
- [ ] jacobian
- [ ] differential kinematics
- [ ] singularities
- [ ] redundant manipulators

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **angela sodemann (robogrok) – robot kinematics & denavit-hartenberg (d-h) frames:** [youtube kanalı](https://www.youtube.com/@asodemann3) & [arama bağlantısı](https://www.youtube.com/results?search_query=angela+sodemann+robotics+kinematics) — **[ilk izlenecek]** homojen dönüşüm matrisleri, d-h tablosu çıkarma ve ileri/ters kinematiği en sezgisel anlatan pratik seri
  2. **kevin lynch – modern robotics chapters 4, 5 & 6 (forward/inverse kinematics & velocity jacobian):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — **[ana akademik ders]** uzaysal hız (twist), jacobian matrisi ve tekillik (singularity) analizi
- **📖 oku (kitaplar — önem sırasıyla):**
  1. **modern robotics – bölüm 4 (forward kinematics), bölüm 5 (velocity kinematics and statics) & bölüm 6 (inverse kinematics):** [ücretsiz kitap pdf](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf)
  2. **robot modeling and control (mark w. spong, seth hutchinson, m. vidyasagar):** [kitap sayfası](https://www.wiley.com/en-us/Robot+Modeling+and+Control%2C+2nd+Edition-p-9781119523994) — klasik d-h parametrizasyonu ve jakobiyen türetimleri için standart kaynak

#### 8.3 robot dynamics

- [ ] newton-euler formulation
- [ ] lagrangian mechanics
- [ ] rigid body dynamics
- [ ] inertia tensor
- [ ] forces and torques
- [ ] dynamic modeling
- [ ] contact dynamics
- [ ] actuator dynamics
- [ ] fixed-wing & aerodynamic dynamics (sabit kanat iha uçuş dinamiği)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **kevin lynch – modern robotics chapter 8 (dynamics of open chains):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx) — **[ilk izlenecek]** lagrange ve newton-euler formülasyonları, kütle/atalet matrisi ($m(\theta)$) ve coriolis kuvvetleri
  2. **mit 6.832 – underactuated robotics (prof. russ tedrake):** [youtube tam dönem ders serisi](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — **[dünya zirvesi]** iha'lar, dört ayaklı/insansı robotlar ve doğrusal olmayan dinamik sistemlerin modellemesi
  3. **steve brunton – lagrangian mechanics & robot dynamics:** [youtube videoları](https://www.youtube.com/results?search_query=steve+brunton+lagrangian+dynamics) — analitik mekanik özeti
- **📖 oku & 💻 kütüphane (kitap ve c++ dinamik motorları — önem sırasıyla):**
  1. **modern robotics – bölüm 8 (dynamics of open chains):** [ücretsiz kitap pdf](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf)
  2. **rigid body dynamics algorithms (roy featherstone):** [springer kitap sayfası](https://link.springer.com/book/10.1007/978-1-4899-7560-7) — yüksek hızlı robotik simülatörlerin (mujoco, pinocchio, drake) arkasındaki algoritmalar
  3. **repo – stack-of-tasks/pinocchio:** [github.com/stack-of-tasks/pinocchio](https://github.com/stack-of-tasks/pinocchio) — c++ ve python ile mikro-saniye seviyesinde rijit gövde dinamiği ve kinematiği hesaplayan endüstriyel kütüphane
  4. **small unmanned aircraft: theory and practice (randy beard & tim mclain – princeton university press):** [kitap bilgisi (press.princeton.edu)](https://press.princeton.edu/books/hardcover/9780691149219/small-unmanned-aircraft) & [resmi python simülatörü (byu-magicc/mavsim_public)](https://github.com/byu-magicc/mavsim_public) — **[sabit kanatlı iha uçuş dinamiğinin kutsal kitabı]** byu magicc laboratuvarının geliştirdiği; koordinat çerçeveleri (gövde, rüzgar, ned), aerodinamik kuvvet ve momentler, 12 durum değişkenli 6-dof rijit gövde dinamiği, ardışık döngü kapatmalı otopilot ve ekf durum kestirimi içeren dünya çapındaki 1 numaralı referans ders kitabı ve 1k+ yıldızlı resmi python simülatörü

#### 8.4 robot operating system (ros / ros 2)

- [ ] ros fundamentals
- [ ] ros 2 architecture
- [ ] nodes
- [ ] topics
- [ ] services
- [ ] actions
- [ ] parameters
- [ ] launch files
- [ ] tf2 (transform library)
- [ ] urdf (unified robot description format)
- [ ] xacro
- [ ] rviz
- [ ] `rosbag`
- [ ] dds (data distribution service)
- [ ] lifecycle nodes
- [ ] ros 2 control
- [ ] navigation stack (nav2)
- [ ] moveit 2
- [ ] plotjuggler & gerçek zamanlı telemetri analizi

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **articulated robotics (josh newans) – ros 2 complete guide & building a mobile robot:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT) — **[ilk izlenecek – uygulamalı ros 2 serisi]** sıfırdan urdf, tf2, `ros2_control`, gazebo, lidar/kamera ve nav2 ile otonom robot kurmayı öğreten kapsamlı seri
  2. **the construct – ros 2 tutorials (c++ & python):** [youtube kanalı](https://www.youtube.com/@TheConstruct) — lifecycle nodes, dds, qos profilleri ve endüstriyel ros 2 pratikleri
- **📖 oku & 💻 repo (resmi doküman ve endüstriyel kodlar — önem sırasıyla):**
  1. **ros 2 official documentation (güncel lts: lyrical luth — mayıs 2026 – mayıs 2031):** [docs.ros.org/en/lyrical](https://docs.ros.org/en/lyrical/) & [release schedule](https://docs.ros.org/en/lyrical/The-ROS2-Project/Release-Schedule.html) — **[resmi kurulum ve api referansı]** güncel lts sürümü mayıs 2026 çıkışlı **lyrical luth**'tur. eski sürümlerle (humble/jazzy) çekilmiş videolardan kavramları öğrenebilirsin ama kurulum ve c++ (`rclcpp`) / python (`rclpy`) geliştirme için lyrical dokümanını kullan
  2. **nav2 (ros 2 navigation stack) official documentation & repo:** [docs.nav2.org](https://docs.nav2.org/) & [github.com/ros-planning/navigation2](https://github.com/ros-planning/navigation2) — **[otonom mobil robotların kalbi]** haritalama, lokalizasyon (amcl), maliyet haritaları (costmaps) ve behavior tree tabanlı navigasyon c++ kodu
  3. **moveit 2 (robotic manipulation framework):** [moveit.picknik.ai](https://moveit.picknik.ai/main/index.html) & [github.com/moveit/moveit2](https://github.com/moveit/moveit2) — robot kolları ve manipülatörler için hareket planlama yığını
  4. **plotjuggler: fast & intuitive time series visualizer (davide faconti):** [plotjuggler.io](https://www.plotjuggler.io/) & [github repo (plotjuggler/plotjuggler)](https://github.com/PlotJuggler/PlotJuggler) — **[robot telemetri & rosbag analiz standardı]** gerçek zamanlı ros/ros 2 topic verilerini, udp akışlarını ve kaydedilmiş rosbag (.db3 / .bag) dosyalarını anında görselleştiren; motor hızları, kontrolcü hataları ve sensör verilerini lua fonksiyonlarıyla canlı analiz etmeyi sağlayan, opengl hızlandırmalı 4.6k+ yıldızlı vazgeçilmez robotik hata ayıklama aracı

#### 8.5 robot simulation

- [ ] gazebo / gazebo sim (ignition)
- [ ] nvidia isaac sim & isaaclab (gpu-paralel robotik simülasyonu)
- [ ] mujoco
- [ ] webots
- [ ] pybullet
- [ ] coppeliasim
- [ ] digital twins
- [ ] physics simulation
- [ ] sensor simulation
- [ ] hardware-in-the-loop (hil)
- [ ] software-in-the-loop (sitl)
- [ ] flightmare & iha/dron simülasyonu
- [ ] rotors & gazebo mav simülasyonu
- [ ] aerial gym simulator & gpu-paralel hava robotiği
- [ ] drake (mit csail) & matematiksel simülasyon

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **articulated robotics – simulating a robot with gazebo & ros 2:** [youtube videosu](https://www.youtube.com/watch?v=laWn7_cj434) — **[ilk izlenecek]** urdf/xacro modeline fizik, kamera ve lidar ekleyip gazebo'da sürme
  2. **nvidia developer – nvidia isaac sim & isaac ros tutorials:** [youtube oynatma listesi](https://www.youtube.com/results?search_query=nvidia+isaac+sim+tutorial+ros2) — **[fotogerçekçi gpu simülasyonu]** ray-tracing tabanlı sensör simülasyonu, sentetik veri üretimi ve donanım hızlandırmalı robotik
- **📖 oku & 💻 simülatör dokümanları (önem sırasıyla):**
  1. **gazebo sim (modern ignition gazebo) official docs:** [gazebosim.org/docs](https://gazebosim.org/docs) — ros 2 ile entegre açık kaynak fizik ve sensör simülatörü
  2. **nvidia isaac sim & isaaclab (nvidia & eth zürich):** [isaac-sim.github.io/isaaclab](https://isaac-sim.github.io/IsaacLab/) & [github (isaac-sim/isaaclab)](https://github.com/isaac-sim/IsaacLab) — **[gpu-paralel robot öğrenmesi standartı]** tek bir gpu üzerinde binlerce robotu eşzamanlı simüle ederek insansı ve bacaklı robotlara dakikalar içinde yürüme ve manipülasyon politikaları eğiten 8.6k+ yıldızlı resmi simülasyon ve rl çerçevesi
  3. **mujoco (multi-joint dynamics with contact – deepmind):** [mujoco.readthedocs.io](https://mujoco.readthedocs.io/en/stable/overview.html) & [github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — robot öğrenmesi (rl) ve temas dinamiği için dünyanın en hızlı c/c++ fizik motoru
  4. **px4 & ardupilot sitl (software-in-the-loop) simulation guides:** [docs.px4.io/main/en/simulation](https://docs.px4.io/main/en/simulation/) · [ardupilot sitl (ardupilot.org)](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) — iha ve otonom araç algoritmalarını (copter, plane, vtol, rover) gerçek uçuş öncesi gazebo, jsbsim ve ros üzerinde donanımsız simüle edip test etme
  5. **luckyengine & luckyrobots (mujoco robotik simülatörü):** [luckyrobots (github)](https://github.com/luckyrobots/luckyrobots) & [luckyrobots.readthedocs.io](https://luckyrobots.readthedocs.io) — mujoco fizik motorunu grpc ile python'a bağlayan; robot manipülatörleri, dört bacaklı (unitree go2) ve insansı (g1) robotlar için gymnasium (`luckyenv`) rl arayüzü sunan yeni nesil simülasyon ortamı
  6. **flightmare: flexible quadrotor simulator (uzh rpg – corl):** [flightmare.bitbucket.io](https://github.com/uzh-rpg/flightmare) & [github repo (uzh-rpg/flightmare)](https://github.com/uzh-rpg/flightmare) — **[otonom iha & dron yarışı simülatörü]** davide scaramuzza ekibinin geliştirdiği; saniyede yüzbinlerce adım simüle eden ultra hızlı c++ çok rotorlu aerodinamik motoru ile unity fotogerçekçi render motorunu ayıran, otonom iha'lara takviyeli öğrenme (rl) ile çevik uçuş ve engelden kaçma öğreten açık kaynak simülatör
  7. **rotors: modular gazebo mav simulator (eth zürich asl – springer):** [github repo (ethz-asl/rotors_simulator)](https://github.com/ethz-asl/rotors_simulator) & [wiki](https://github.com/ethz-asl/rotors_simulator/wiki) — **[ros & gazebo çok rotorlu iha simülasyonu standartı]** prof. roland siegwart ekibinin geliştirdiği; asctec firefly ve hummingbird gibi çok rotorlu iha modelleri, gerçekçi imu gürültü modelleri, stereo/kamera/lidar sensör simülasyonları ve se(3) geometrik uçuş kontrolcüleri (lee controller) sunan 1.5k+ yıldızlı gazebo/ros simülatör çerçevesi
  8. **aerial gym simulator (ntnu arl & nvidia isaac gym):** [github repo (ntnu-arl/aerial_gym_simulator)](https://github.com/ntnu-arl/aerial_gym_simulator) & [aerialgym.com](https://aerialgym.com/) — **[gpu-paralel uçan robotik & rl simülasyonu]** prof. kostas alexis ekibinin geliştirdiği; nvidia isaac gym üzerinde tek bir gpu'da on binlerce iha'yı eşzamanlı simüle eden, derin pekiştirmeli öğrenme (rl) ile aerodinamik etkiler altında çevik uçuş, engelden kaçma ve görsel navigasyon politikaları eğiten 780+ yıldızlı yüksek başarımlı simülasyon çerçevesi
  9. **drake: model-based design and verification for robotics (mit csail – robotlocomotion):** [drake.mit.edu](https://drake.mit.edu/) & [github repo (robotlocomotion/drake)](https://github.com/RobotLocomotion/drake) — **[matematiksel robotik simülasyonu & yörünge optimizasyonu]** prof. russ tedrake ekibinin geliştirdiği; c++ ile yazılmış, kinematik, temas dinamiği, doğrusal olmayan optimizasyon (snopt, ipopt), lqr ve lyapunov kararlılık analizi sunan, humanoid ve manipülatör sistemleri için 4.3k+ yıldızlı mit csail simülasyon ve kontrol motoru

#### 8.6 robot perception

- [ ] camera perception
- [ ] lidar perception
- [ ] radar perception
- [ ] sensor calibration (extrinsic camera-lidar, camera-imu)
- [ ] object detection
- [ ] object tracking
- [ ] 3d object detection
- [ ] semantic segmentation
- [ ] scene understanding
- [ ] occupancy mapping
- [ ] 2.5d elevation mapping & traversability (gpu-hızlandırmalı yükseklik haritalama)
- [ ] doğrudan kamera-lidar dışsal kalibrasyonu (direct_visual_lidar_calibration)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – mobile sensing and robotics (kamera, lidar & 3b doluluk haritaları):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **[ilk izlenecek]** lidar nokta bulutu işleme, octomap / occupancy grid mapping ve sensör kalibrasyonu
  2. **eth zürich – autonomous mobile robots (perception & mapping lectures – prof. roland siegwart):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — mobil robotlarda görsel ve lazer tabanlı algılama hattı
- **📖 oku & 💻 repo (endüstriyel algılama yığınları — önem sırasıyla):**
  1. **autoware universe perception stack documentation:** [autowarefoundation.github.io/autoware-documentation/main/design/autoware-architecture/perception](https://autowarefoundation.github.io/autoware-documentation/main/) & [github repo](https://github.com/autowarefoundation/autoware.universe) — **[gerçek otonom araç mimarisini incele]** kamera-lidar-radar füzyonu, 3b nesne tespiti (centerpoint) ve doluluk haritalarının ros 2 c++ ile nasıl kurulduğunu gösteren açık kaynak sistem
  2. **nvidia isaac ros perception packages (nitros):** [nvidia-isaac-ros.github.io](https://nvidia-isaac-ros.github.io/) — gpu/tensorrt hızlandırmalı ros 2 algılama, derinlik ve visual slam düğümleri
  3. **repo –ethz-asl/kalibr:** [github.com/ethz-asl/kalibr](https://github.com/ethz-asl/kalibr) — çoklu kamera ve kamera-imu dışsal (extrinsic) kalibrasyonu için standart açık kaynak araç kutusu
  4. **elevation_mapping_cupy: gpu-accelerated 2.5d elevation mapping (eth zürich rsl – iros):** [github repo (leggedrobotics/elevation_mapping_cupy)](https://github.com/leggedrobotics/elevation_mapping_cupy) & [dokümantasyon](https://leggedrobotics.github.io/elevation_mapping_cupy/) — **[bacaklı robotlar için gpu yükseklik ve geçilebilirlik haritalaması]** anymal robotunu geliştiren eth zürih ekibinin geliştirdiği; engebeli arazilerde, merdivenlerde ve doğada bacaklı ve tekerlekli robotların güvenle basabileceği yüzeyleri (footholds) ve yüzey normallerini nvidia gpu (cupy) üzerinde 50+ hz gerçek zamanlı hesaplayan 1.1k+ yıldızlı 2.5b haritalama paketi
  5. **wavemap: real-time 3d multi-resolution occupancy mapping (eth zürich asl – rss / ieee t-ro):** [github repo (ethz-asl/wavemap)](https://github.com/ethz-asl/wavemap) & [makale (arxiv:2304.14813)](https://arxiv.org/abs/2304.14813) — **[3b hacimsel doluluk haritalama standartı]** prof. roland siegwart ekibinin geliştirdiği; klasik octomap'in ışın izleme (raycasting) gecikmesini ve ayrıklaştırma hatalarını dalgacık (wavelet) sıkıştırmasıyla aşan, lidar ve derinlik kameraları için çok çözünürlüklü ve ultra hafif 3b doluluk/çarpışma haritaları üreten açık kaynak c++ haritalama motoru
  6. **direct_visual_lidar_calibration: targetless lidar-camera extrinsic calibration (kenji koide – aist):** [github repo (koide3/direct_visual_lidar_calibration)](https://github.com/koide3/direct_visual_lidar_calibration) — **[hedefsiz kamera-lidar kalibrasyon standardı]** kamera ile lidar arasındaki dışsal (extrinsic) rotasyon ve öteleme parametrelerini, dama tahtası veya hedef plaka gerektirmeden doğrudan ortamın kenar ve düzlem özellikleri üzerinden milimetrik hassasiyetle hesaplayan endüstri standardı c++/ros 2 kalibrasyon aracı

#### 8.7 robot learning

- [ ] learning from demonstration (lfd) & human-in-the-loop rl
- [ ] imitation learning
- [ ] behavior cloning
- [ ] inverse reinforcement learning
- [ ] reinforcement learning (rl)
- [ ] deep reinforcement learning (dqn, ppo, sac)
- [ ] sim-to-real transfer
- [ ] domain randomization
- [ ] robot foundation models
- [ ] airstack & saha robotiği sim-to-real yığını
- [ ] diffusion policy & umi (stanford real lab)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **uc berkeley cs285 – deep reinforcement learning (prof. sergey levine):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) & [ders sitesi](https://rail.eecs.berkeley.edu/deeprlcourse/) — **[temel akademik robot learning dersi]** imitation learning, behavior cloning, policy gradients, ppo, sac ve model-based rl
  2. **prof. shuran song (stanford real lab & columbia) – visuomotor policy learning & diffusion in robotics:** [youtube seminer & ders videoları](https://www.youtube.com/results?search_query=shuran+song+diffusion+policy+robotics) — **[görsel-motor politika & difüzyon dersi]** diffusion policy ve umi'ın arkasındaki eylem difüzyon modelleri (ddpm), çok modlu insan gösterimlerinden eylem dağılımı öğrenme ve sim2real aktarımının ders anlatımı
- **📖 oku & 💻 repo (rehber, makale ve kütüphaneler — önem sırasıyla):**
  1. **openai spinning up in deep rl:** [spinningup.openai.com](https://spinningup.openai.com/en/latest/) — **[ilk okunacak]** pekiştirmeli öğrenme (ppo, sac, td3) algoritmalarının en temiz matematiksel ve pytorch kodlu başlangıç rehberi
  2. **robot learning from demonstration (lfd): a survey (ravichandar et al.):** [ieee / arxiv makalesi](https://arxiv.org/abs/1911.09052) — taklit yoluyla öğrenme yöntemlerinin kapsamlı incelemesi
  3. **repo – huggingface/lerobot:** [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot) — gerçek dünya robotları için pytorch tabanlı imitation learning (act, diffusion policy) ve rl kütüphanesi
  4. **repo & sim2real köprüsü – luckyrobots / luckyengine:** [luckyrobots (github)](https://github.com/luckyrobots/luckyrobots) & [lerobot sim2real tutorial](https://luckyrobots.github.io/lerobot-luckyengine-tutorial/) — **[mujoco + lerobot sim2real hattı]** mujoco tabanlı fotogerçekçi luckyengine simülatöründe gösterim (demonstration) toplayıp hugging face lerobot ile politika eğiterek so-100 kolu ve unitree go2/g1 robotlarına sıfır gerçek veriyle %72 sim2real başarı sağlayan grpc python sdk'sı
  5. **learning high-speed flight in the wild (uzh rpg – science robotics):** [agile_autonomy (github)](https://github.com/uzh-rpg/agile_autonomy) & [science robotics makalesi](https://www.science.org/doi/10.1126/scirobotics.abg5810) — **[uç nokta sim-to-real otonom uçuş]** davide scaramuzza ve vladlen koltun ekibinin geliştirdiği; yalnızca simülasyonda eğitilip sıfır gerçek dünya verisiyle (zero-shot sim-to-real) bilinmeyen ormanlarda ve haritasız harabelerde 40 km/s hızla engellerden kaçan tam otonom iha derin öğrenme seyrüsefer politikası
  6. **rlkit & softlearning: rl toolkit & resmi soft actor-critic (uc berkeley rail lab – sergey levine):** [rlkit (github)](https://github.com/rail-berkeley/rlkit) · [softlearning (github)](https://github.com/rail-berkeley/softlearning) — **[sürekli kontrol, robot öğrenmesi & resmi sac reposu]** prof. sergey levine ve tuomas haarnoja ekibinin geliştirdiği; robot manipülasyonu ve bacaklı robotlarda dünya standardı olan maksimum entropi rl / soft actor-critic (sac), td3 ve meta-rl (pearl) algoritmalarının resmi uygulama ve araştırma kod tabanları
  7. **hil-serl & serl: sample-efficient robotic reinforcement learning (uc berkeley rail lab – corl / icra):** [hil-serl (github)](https://github.com/rail-berkeley/hil-serl) · [serl (github)](https://github.com/rail-berkeley/serl) · [serl-robot.github.io](https://serl-robot.github.io/) — **[fiziksel robot üzerinde gerçek zamanlı rl devrimi]** sergey levine ekibinin geliştirdiği; simülasyona gerek kalmadan doğrudan gerçek robot kolu üzerinde (franka, ur5) insan müdahaleleri (human-in-the-loop) ve öncül verilerle (rlpd) sadece 1-2 saat içinde hassas montaj (kablo takma, pcb montajı) öğreten en son teknoloji robot öğrenmesi yığını
  8. **rsl_rl: fast gpu-accelerated rl for robotics (eth zürich rsl – corl / science robotics):** [github repo (leggedrobotics/rsl_rl)](https://github.com/leggedrobotics/rsl_rl) — **[bacaklı ve insansı robot lokomosyonu ppo standardı]** marco hutter ekibinin geliştirdiği; nvidia isaaclab ve isaac gym üzerinde binlerce robotu tamamen gpu vram üzerinde dakikalar içinde yürüten (science robotics makalesi), dünyadaki insansı ve dört bacaklı robot lokomosyonunun 1 numaralı gpu-paralel ppo pekiştirmeli öğrenme kütüphanesi
  9. **airstack: agent-native autonomy stack for field robotics (cmu airlab):** [github repo (castacks/airstack)](https://github.com/castacks/AirStack) & [theairlab.org/airstack](https://github.com/castacks/AirStack) — **[saha robotiği ve iha sim-to-real otonomi yığını]** prof. sebastian scherer ekibinin geliştirdiği; ros 2, nvidia isaac sim (pegasussimulator) ve gövde üstü otonomiyi birleştiren, iha'lar ve saha robotlarında yapay zekâ politikalarının simülasyondan fiziksel donanıma hızlı aktarımını (sim-to-real) sağlayan açık kaynak otonomi çerçevesi
  10. **diffusion policy: visuomotor policy learning via action diffusion (stanford real lab & columbia – shuran song / rss):** [diffusion-policy.cs.columbia.edu](https://diffusion-policy.cs.columbia.edu/) · [github repo (real-stanford/diffusion_policy)](https://github.com/real-stanford/diffusion_policy) & [umi handheld gripper (github)](https://github.com/real-stanford/universal_manipulation_interface) — **[modern robot öğrenmesi & görsel-motor politika devrimi]** prof. shuran song ekibinin geliştirdiği; robot manipülasyonunda eylemleri difüzyon modeli (denoising diffusion probabilistic models) ile üreterek çok modlu (multimodal) insan gösterimlerini ve karmaşık montaj görevlerini başarıyla çözen, tesla optimus, figure ai ve lerobot tarafından benimsenen 2.5k+ yıldızlı temel robot öğrenmesi mimarisi

#### 8.8 robot applications

- [ ] industrial robotics
- [ ] collaborative robotics (cobots)
- [ ] mobile robotics (agv, amr)
- [ ] manipulation
- [ ] warehouse robotics
- [ ] service robotics
- [ ] medical robotics
- [ ] agricultural robotics
- [ ] assistive robotics
- [ ] humanoid robotics
- [ ] autonomous vehicles

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video kanalları — önem sırasıyla):**
  1. **ieee spectrum robotics:** [youtube kanalı](https://www.youtube.com/@IEEESpectrum) — dünyadaki en yeni endüstriyel, medikal, tarımsal ve insansı robotik sistemlerin mühendislik incelemeleri
  2. **boston dynamics & agility robotics technical talks:** [boston dynamics youtube](https://www.youtube.com/@BostonDynamics) — atlas ve spot robotlarının algılama, mpc kontrol ve hareket planlama mimarileri
- **📖 oku (referans ansiklopedi):**
  1. **springer handbook of robotics (bruno siciliano & oussama khatib):** [springer kitap sayfası](https://link.springer.com/book/10.1007/978-3-319-32552-1) — tüm robotik alt disiplinlerini kapsayan 2000+ sayfalık başucu ansiklopedisi

---

### 02. advanced & emerging technologies

#### 19.1 advanced ai

- [ ] foundation models
- [ ] multimodal foundation models
- [ ] world models
- [ ] agentic ai
- [ ] test-time compute
- [ ] reasoning models (o1, deepseek-r1 vb.)
- [ ] neuro-symbolic ai
- [ ] continual learning
- [ ] self-supervised learning
- [ ] federated learning
- [ ] efficient ai
- [ ] small language models (slm)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video kanalları — önem sırasıyla):**
  1. **ai explained:** [youtube kanalı](https://www.youtube.com/@aiexplained-official) — yeni çıkan reasoning (o1, deepseek-r1), test-time compute ve foundation modellerinin abartıdan uzak, benchmark verilerine dayalı analizi
  2. **yannic kilcher:** [youtube kanalı](https://www.youtube.com/@YannicKilcher) — derinlemesine makale incelemeleri
- **📖 oku (etkileşimli makale ve arşiv — önem sırasıyla):**
  1. **world models (david ha & jürgen schmidhuber):** [worldmodels.github.io (etkileşimli makale)](https://worldmodels.github.io/) — bir ajanın kendi içinde çevresinin simülasyonunu (dünya modelini) öğrenip rüyasında (latent space) plan yapmasını anlatan kurucu makale
  2. **arxiv artificial intelligence (`cs.ai`) recent submissions:** [arxiv.org/list/cs.ai/recent](https://arxiv.org/list/cs.AI/recent)

#### 19.2 physical ai & embodied intelligence

- [ ] embodied ai
- [ ] robot foundation models
- [ ] vision-language-action models
- [ ] robot learning
- [ ] imitation learning
- [ ] reinforcement learning
- [ ] sim-to-real
- [ ] world models
- [ ] human-robot interaction
- [ ] autonomous manipulation

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı araştırma seminerleri — önem sırasıyla):**
  1. **berkeley artificial intelligence research (bair) & robot learning lab (pieter abbeel / sergey levine):** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=berkeley+robot+learning+embodied+ai)
  2. **stanford robotics center seminars:** [youtube kanalı](https://www.youtube.com/@stanfordonline) — physical ai, vla ve insansı robot manipülasyonu
- **📖 oku (konferans ve benchmark platformu):**
  1. **embodied ai workshop (cvpr):** [embodied-ai.org](https://embodied-ai.org/) — fiziksel dünyada algılama ve hareket eden yapay zekâ sistemlerinin yıllık zirve çalıştayı ve açık kaynak simülatör listesi

#### 19.3 advanced robotics

- [ ] humanoid robotics
- [ ] whole-body control (wbc - locomotion & manipulation)
- [ ] humanoid foundation models (nvidia gr00t, gear-sonic)
- [ ] legged robotics (quadrupeds & sim2real actuator modeling)
- [ ] soft robotics
- [ ] swarm robotics
- [ ] medical robotics
- [ ] surgical robotics
- [ ] agricultural robotics
- [ ] assistive robotics
- [ ] autonomous mobile manipulation
- [ ] behavior-1k & omnigibson mobil manipülasyon
- [ ] mit mini cheetah software & convex mpc dört bacaklı lokomosyon
- [ ] 6-dof robotik kavrama tespiti (graspnet-1billion)
- [ ] eklemli nesne manipülasyonu ve parça seviyesi algılama (gapartnet)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler & mühendislik kanalları — önem sırasıyla):**
  1. **prof. russ tedrake (mit 6.4210 / 6.800 – robotic manipulation: perception, tracking, and grasping):** [youtube oynatma listesi (mit)](https://www.youtube.com/playlist?list=PLkx8KyIQkMfWr191lqbN8WfV08j-ui8WX) & [ders notları (manipulation.csail.mit.edu)](https://manipulation.csail.mit.edu/) — **[robotik kavrama & manipülasyon başucu dersi]** graspnet ve gapartnet'in teorik temelini oluşturan; 3b nokta bulutlarından 6-dof kavrama (grasping), kuvvet/sürtünme konileri (friction cones), eklemli (articulated) nesne etkileşimi ve temas mekaniğini amfide tahtada anlatan mit başvuru dersi
  2. **prof. marco hutter (eth zürich rsl) – legged robotics & quadruped locomotion lectures:** [youtube ders & sunum serisi](https://www.youtube.com/results?search_query=marco+hutter+legged+robotics+lecture) — **[bacaklı robotik & lokomosyon dersi]** anymal ve bacaklı robotların arkasındaki basitleştirilmiş dinamik modeller (slip, zmp), convex mpc, tüm vücut kontrolü (wbc) ve sim2real aktarımının akademik dersleri
  3. **boston dynamics & unitree robotics official channels:** [boston dynamics youtube](https://www.youtube.com/@BostonDynamics) · [unitree robotics youtube](https://www.youtube.com/@UnitreeRobotics) — dört ayaklı (quadruped) ve insansı (humanoid) robotlarda tüm-vücut kontrolü (whole-body mpc & rl) saha uygulamaları
  4. **ieee spectrum robotics:** [youtube kanalı](https://www.youtube.com/@IEEESpectrum)
- **📖 oku (referans kitap):**
  1. **humanoid robotics: a reference (ambarish goswami & prahlad vadakkepat):** [springer kitap sayfası](https://link.springer.com/referencework/10.1007/978-94-007-6046-2) — iki ayaklı denge (zmp), yürüyüş üretimi ve insansı robot mekaniği
- **💻 açık kaynak insansı robotik reposu (önem sırasıyla):**
  1. **nvidia gr00t whole-body control (nvidia research gear lab):** [nvlabs/gr00t-wholebodycontrol (github)](https://github.com/NVlabs/GR00T-WholeBodyControl) & [dokümantasyon](https://nvlabs.github.io/GR00T-WholeBodyControl/) — **[insansı robot tüm-vücut kontrolü (wbc)]** insansı (humanoid) robotlarda alt gövde yürümesini (locomotion rl) ve üst gövde manipülasyonunu (upper-body ik) birleştiren, nvidia isaaclab simülasyonu ve jetson orin donanımında çalışan resmi gear-sonic ve decoupled wbc kontrol mimarisi
  2. **pace: sim-to-real actuator identification for legged robots (eth zürich rsl – marco hutter):** [github repo (leggedrobotics/pace-sim2real)](https://github.com/leggedrobotics/pace-sim2real) & [makale (arxiv:2403.07663)](https://arxiv.org/abs/2403.07663) — **[bacaklı robotlarda eyleyici sim2real standartı]** efsanevi anymal robotunu geliştiren eth zürih ekibinin açık kaynak projesi; bacaklı ve insansı robotların simülasyondan (isaaclab) gerçeğe aktarımında en büyük engel olan motor ve eklem dinamiklerini (gecikme, sürtünme, dişli boşluğu) harici tork sensörü gerektirmeden standart eklem enkoderleriyle kalibre eden sistem kimlikleme (system identification) çerçevesi
  3. **behavior-1k, omnigibson & robosuite (stanford vision and learning lab – fei-fei li & silvio savarese):** [behavior.stanford.edu](https://behavior.stanford.edu/) · [github repo (stanfordvl/behavior-1k)](https://github.com/StanfordVL/BEHAVIOR-1K) & [robosuite (github)](https://github.com/ARISE-Initiative/robosuite) — **[insansı & mobil manipülasyon embodied ai standardı]** stanford vl laboratuvarının geliştirdiği; ev ve ofis ortamlarında 1.000 günlük insan aktivitesini (yemek yapma, temizlik, nesne manipülasyonu) fotogerçekçi fizik motorunda (omnigibson) simüle eden ve robot kollarında taklit öğrenmesi (imitation learning) için dünya standardı kabul edilen 1.5k+ yıldızlı robotik ekosistemi
  4. **mit mini cheetah software & convex mpc (mit biomimetic robotics lab – sangbae kim / ieee t-ro):** [github repo (mit-biomimetic/cheetah-software)](https://github.com/mit-biomimetics/Cheetah-Software) — **[dört bacaklı robot dinamiği ve mpc kontrol standartı]** prof. sangbae kim ekibinin geliştirdiği; mit mini cheetah robotunun tüm kontrol mimarisini açık kaynak sunan; basitleştirilmiş tek sert gövde modeli üzerinde convex model predictive control (mpc), tüm vücut itki kontrolü (whole-body impulse control - wbic), lcm mesajlaşma ve durum kestirimi içeren 2.5k+ yıldızlı bacaklı robotik başyapıtı
  5. **graspnet-1billion & anygrasp: 6-dof robotik kavrama ve nokta bulutu manipülasyon standardı (sjtu mvig lab – cewu lu / cvpr):** [github repo (graspnet/graspnet-baseline)](https://github.com/graspnet/graspnet-baseline) & [graspnet.net](https://graspnet.net/) — **[robotik kavramada dünya standardı benchmark & model]** prof. cewu lu ekibinin geliştirdiği; robot kollarının (franka, ur5 vb.) dağınık ve karmaşık 3b sahnelerdeki bilinmeyen nesneleri nokta bulutu üzerinden 6 serbestlik dereceli (6-dof) yakalama pozisyonlarını yüksek doğrulukla tespit etmesini sağlayan 1.5k+ yıldızlı küresel kavrama (grasping) ve manipülasyon standardı
  6. **gapartnet: 3d articulated object perception and interaction (pku epic lab – he wang / cvpr highlight):** [github repo (pku-epic/gapartnet)](https://github.com/PKU-EPIC/GAPartNet) & [pku-epic.github.io/gapartnet](https://pku-epic.github.io/GAPartNet/) — **[eklemli nesne manipülasyonu & genellenebilir parça temsili]** pekin üniversitesi epic laboratuvarının geliştirdiği; robotların dolap kapağı, çekmece, fırın, kapı gibi eklemli (articulated) nesneleri 3b ortamda algılamasını, tutamak/kol pozlarını kestirmesini ve isaac gym simülasyonuyla genel geçer etkileşim politikaları (manipulation policies) öğrenmesini sağlayan referans açık kaynak çerçeve

#### 19.4 advanced perception

- [ ] event-based cameras
- [ ] neuromorphic vision
- [ ] radar perception (4d imaging radar)
- [ ] thermal vision
- [ ] hyperspectral imaging
- [ ] multi-sensor perception
- [ ] 4d scene understanding
- [ ] dynamic 3d reconstruction

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı araştırma grubu — önem sırasıyla):**
  1. **rpg lab uzh (prof. davide scaramuzza – university of zurich):** [youtube kanalı](https://www.youtube.com/@ailabRPG/playlists) — **[dünya lideri laboratuvar]** event-based (nöromorfik) kameralar ve geleneksel rgb kameraların füzyonu ile yüksek hızlı iha algılaması
- **📖 oku & 💻 repo (makale ve veri setleri — önem sırasıyla):**
  1. **event-based vision resources (awesome event-based vision – uzh rpg):** [github.com/uzh-rpg/event-based_vision_resources](https://github.com/uzh-rpg/event-based_vision_resources) — nöromorfik kameralar üzerine tüm makaleler, açık kaynak c++/python kodları ve simülatörler
  2. **4d imaging radar for autonomous driving surveys (ieee):** [arxiv arama bağlantısı](https://arxiv.org/search/?query=4D+imaging+radar+autonomous+driving&searchtype=all) — kötü hava koşullarında lidar'ı tamamlayan 4b radar algılaması

#### 19.5 advanced computing

- [ ] neuromorphic computing
- [ ] quantum computing fundamentals
- [ ] photonic computing
- [ ] edge computing
- [ ] heterogeneous computing
- [ ] high performance computing (hpc)
- [ ] accelerated computing

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video kanalları — önem sırasıyla):**
  1. **ibm technology & qiskit youtube channels:** [qiskit youtube](https://www.youtube.com/@qiskit) · [ibm technology youtube](https://www.youtube.com/@IBMTechnology) — heterojen hesaplama, hpc ve kuantum hesaplama temelleri
- **📖 oku (etkileşimli eğitim):**
  1. **ibm quantum learning:** [learning.quantum.ibm.com](https://learning.quantum.ibm.com/) — kuantum bilgi teorisi ve algoritmalarına ücretsiz giriş

#### 19.6 advanced learning methods

- [ ] meta-learning & maml (öğrenmeyi öğrenme)
- [ ] few-shot learning
- [ ] lifelong learning
- [ ] active learning
- [ ] self-training
- [ ] domain adaptation
- [ ] causal machine learning
- [ ] reinforcement learning
- [ ] multi-agent reinforcement learning

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **judea pearl – causal inference & the book of why lectures:** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=judea+pearl+causal+inference+lecture) — korelasyon ile nedensellik (causality) arasındaki fark ve müdahale (intervention) matematiği
- **📖 oku & 💻 repo (kitap, makale ve meta-learning kod tabanları — önem sırasıyla):**
  1. **meta-learning in neural networks: a survey (hospedales et al. – ieee tpami):** [arxiv:2004.05439](https://arxiv.org/abs/2004.05439) — "öğrenmeyi öğrenme" (meta-learning) algoritmalarının kapsamlı özeti
  2. **maml & maml-rl: model-agnostic meta-learning (finn, abbeel, levine – icml):** [arxiv:1703.03400](https://arxiv.org/abs/1703.03400) · [maml (cbfinn/maml)](https://github.com/cbfinn/maml) · [maml-rl (cbfinn/maml_rl)](https://github.com/cbfinn/maml_rl) · [pytorch (learnables/learn2learn)](https://github.com/learnables/learn2learn) — **[öğrenmeyi öğrenme, few-shot & meta-rl standartı]** chelsea finn ekibinin geliştirdiği; sınıflandırma, regresyon ve takviyeli öğrenmede (meta-rl) robotun/ajanın sadece birkaç denemede yeni ortama ve göreve adapte olmasını sağlayan 9.000+ atıflı çığır açan makale, orijinal rl kodu ve modern pytorch ekosistemi
  3. **causal inference in statistics: a primer (judea pearl, madelyn glymour, nicholas p. jewell):** [kitap sayfası](https://www.wiley.com/en-us/Causal+Inference+in+Statistics%3A+A+Primer-p-9781119186847) — nedensel çıkarıma matematiksel giriş

---

### 03. robotics foundation models literature

#### robotics

##### neural scaling laws
* neural scaling laws for embodied ai: neural scaling laws for embodied ai [[paper]](https://arxiv.org/abs/2405.14005)


##### robot policy learning for decision-making and controls
###### language-conditioned imitation learning
* cliport: what and where pathways for robotic manipulation [[paper]](https://arxiv.org/abs/2109.12098)[[project]](https://cliport.github.io/)[[code]](https://github.com/cliport/cliport)
* perceiver-actor: a multi-task transformer for robotic manipulation [[paper]](https://arxiv.org/abs/2209.05451)[[project]](https://peract.github.io/)[[code]](https://github.com/peract/peract)
* play-lmp: learning latent plans from play [[project]](https://learning-from-play.github.io/)
* multi-context imitation: language-conditioned imitation learning over unstructured data [[project]](https://language-play.github.io)

###### language-assisted reinforcement learning
* towards a unified agent with foundation models [[paper]](https://arxiv.org/abs/2307.09668)
* reward design with language models [[paper]](https://arxiv.org/abs/2303.00001)
* learning to generate better than your llm [[paper]](https://arxiv.org/pdf/2306.11816.pdf)[[code]](https://github.com/Cornell-RL/tril)
* guiding pretraining in reinforcement learning with large language models [[paper]](https://arxiv.org/abs/2302.06692)[[code]](https://github.com/yuqingd/ellm)
* motif: intrinsic motivation from artificial intelligence feedback [[paper]](https://arxiv.org/abs/2310.00166)[[code]](https://github.com/facebookresearch/motif)

##### language-image goal-conditioned value learning
* saycan: do as i can, not as i say: grounding language in robotic affordances [[paper]](https://arxiv.org/abs/2204.01691)[[project]](https://say-can.github.io/)[[code]](https://github.com/google-research/google-research/tree/master/saycan)
* zero-shot reward specification via grounded natural language [[paper]](https://proceedings.mlr.press/v162/mahmoudieh22a/mahmoudieh22a.pdf)
* voxposer: composable 3d value maps for robotic manipulation with language models [[project]](https://voxposer.github.io)
* vip: towards universal visual reward and representation via value-implicit pre-training [[paper]](https://arxiv.org/abs/2210.00030)[[project]](https://sites.google.com/view/vip-rl)
* liv: language-image representations and rewards for robotic control [[paper]](https://arxiv.org/abs/2306.00958)[[project]](https://penn-pal-lab.github.io/LIV/)
* lorel: learning language-conditioned robot behavior from offline data and crowd-sourced annotation [[paper]](https://arxiv.org/abs/2109.01115)[[project]](https://sites.google.com/view/robotlorel)
* text2motion: from natural language instructions to feasible plans [[paper]](https://arxiv.org/abs/2303.12153)[[project]](https://sites.google.com/stanford.edu/text2motion)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

##### robot task planning using large language models
* language models as zero-shot planners: extracting actionable knowledge for embodied agents [[paper]](https://arxiv.org/abs/2201.07207)[[project]](https://wenlong.page/language-planner/)
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* nl2tl: transforming natural languages to temporal logics using large language models [[paper]](https://arxiv.org/pdf/2305.07766.pdf)[[project]](https://yongchao98.github.io/MIT-realm-NL2TL/)[[code]](https://github.com/yongchao98/NL2TL)
* autotamp: autoregressive task and motion planning with llms as translators and checkers[[paper]](https://arxiv.org/abs/2306.06531)[[project]](https://yongchao98.github.io/MIT-REALM-AutoTAMP/)
* latte: language trajectory transformer [[paper]](https://arxiv.org/abs/2208.02918)[[code]](https://github.com/arthurfenderbucker/LaTTe-Language-Trajectory-TransformEr)
* planning with large language models via corrective re-prompting [[paper]](https://arxiv.org/abs/2211.09935)
* describe, explain, plan and select: interactive planning with llms enables open-world multi-task agents [[paper]](https://arxiv.org/pdf/2302.01560.pdf)[[code]](https://github.com/CraftJarvis/MC-Planner)
* jarvis-1: open-world multi-task agents with memory-augmented multimodal language models [[paper]](https://arxiv.org/pdf/2311.05997.pdf)[[project]](https://craftjarvis.github.io/JARVIS-1/)[[code]](https://github.com/CraftJarvis/JARVIS-1)
* an embodied generalist agent in 3d world [[paper]](https://arxiv.org/pdf/2311.12871.pdf)[[project]](https://embodied-generalist.github.io/)[[code]](https://github.com/embodied-generalist/embodied-generalist)
* llm+p: empowering large language models with optimal planning proficiency [[paper]](https://arxiv.org/pdf/2304.11477.pdf)[[code]](https://github.com/Cranial-XIX/llm-pddl)
* mp5: a multi-modal open-ended embodied system in minecraft via active perception [[paper]](https://arxiv.org/pdf/2312.07472.pdf)[[project]](https://iranqin.github.io/MP5.github.io/)[[code]](https://github.com/IranQin/MP5)

##### llm-based code generation
* progprompt: generating situated robot task plans using large language models [[paper]](https://arxiv.org/abs/2209.11302)[[project]](https://progprompt.github.io/)
* code as policies: language model programs for embodied control [[paper]](https://arxiv.org/abs/2209.07753)[[project]](https://code-as-policies.github.io/)
* chatgpt for robotics: design principles and model abilities [[paper]](https://arxiv.org/abs/2306.17582)[[project]](https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/chatgpt-for-robotics/)[[code]](https://github.com/microsoft/PromptCraft-Robotics)
* voyager: an open-ended embodied agent with large language models [[paper]](https://arxiv.org/abs/2305.16291)[[project]](https://voyager.minedojo.org/)
* visual programming: compositional visual reasoning without training [[paper]](https://arxiv.org/abs/2211.11559)[[project]](https://prior.allenai.org/projects/visprog)[[code]](https://github.com/allenai/visprog)
* deploying and evaluating llms to program service mobile robots [[paper]](https://arxiv.org/abs/2311.11183)[[project]](https://amrl.cs.utexas.edu/codebotler/)[[code]](https://github.com/ut-amrl/codebotler)

##### robot transformers
* motiongpt: finetuned llms are general-purpose motion generators [[paper]](https://arxiv.org/abs/2306.10900)[[project]](https://qiqiapink.github.io/MotionGPT/)
* rt-1: robotics transformer for real-world control at scale [[paper]](https://robotics-transformer.github.io/assets/rt1.pdf)[[project]](https://robotics-transformer.github.io/)[[code]](https://github.com/google-research/robotics_transformer)
* masked visual pre-training for motor control [[paper]](https://arxiv.org/abs/2203.06173)[[project]](https://tetexiao.com/projects/mvp)[[code]](https://github.com/ir413/mvp)
* real-world robot learning with masked visual pre-training [[paper]](https://arxiv.org/abs/2210.03109)[[project]](https://tetexiao.com/projects/real-mvp)
* r3m: a universal visual representation for robot manipulation [[paper]](https://arxiv.org/abs/2203.12601)[[project]](https://sites.google.com/view/robot-r3m/)[[code]](https://github.com/facebookresearch/r3m)
* robot learning with sensorimotor pre-training [[paper]](https://arxiv.org/abs/2306.10007)[[project]](https://robotic-pretrained-transformer.github.io/)
* rt-2: vision-language-action models transfer web knowledge to robotic control [[paper]](https://arxiv.org/abs/2307.15818)[[project]](https://robotics-transformer2.github.io/)
* pact: perception-action causal transformer for autoregressive robotics pre-training [[paper]](https://arxiv.org/abs/2209.11133)
* groot: learning to follow instructions by watching gameplay videos [[paper]](https://arxiv.org/pdf/2310.08235.pdf)[[project]](https://craftjarvis.github.io/GROOT/)[[code]](https://github.com/CraftJarvis/GROOT)
* behavior transformers (bet): cloning k modes with one stone [[paper]](https://arxiv.org/abs/2206.11251)[[project]](https://mahis.life/bet/)[[code]](https://github.com/notmahi/bet)
* conditional behavior transformers (c-bet), from play to policy: conditional behavior generation from uncurated robot data [[paper]](https://arxiv.org/abs/2210.10047)[[project]](https://play-to-policy.github.io/)[[code]](https://github.com/jeffacce/play-to-policy)
* magic vfm: meta-learning adaptation for ground interaction control with visual foundation models [[paper]](https://arxiv.org/abs/2407.12304)

##### in-context learning for decision-making
* a survey on in-context learning [[paper]](https://arxiv.org/abs/2301.00234)
* large language models as general pattern machines [[paper]](https://arxiv.org/abs/2307.04721)
* chain-of-thought predictive control [[paper]](https://arxiv.org/abs/2304.00776)
* react: synergizing reasoning and acting in language models [[paper]](https://arxiv.org/abs/2210.03629)
* icrt: in-context imitation learning via next-token prediction [[paper]](https://arxiv.org/abs/2408.15980) [[project]](https://icrt.dev/) [[code]](https://github.com/Max-Fu/icrt)

##### open-vocabulary robot navigation and manipulation
* cows on pasture: baselines and benchmarks for language-driven zero-shot object navigation [[paper]](https://arxiv.org/pdf/2203.10421.pdf)[[project]](https://cow.cs.columbia.edu/)
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* lsc: language-guided skill coordination for open-vocabulary mobile pick-and-place [[project]](https://languageguidedskillcoordination.github.io/)
* l3mvn: leveraging large language models for visual target navigation [[project]](https://arxiv.org/abs/2304.05501)
* open-world object manipulation using pre-trained vision-language models [[paper]](https://robot-moo.github.io/assets/moo.pdf)[[project]](https://robot-moo.github.io/)
* vima: general robot manipulation with multimodal prompts [[paper]](https://arxiv.org/abs/2210.03094)[[project]](https://vimalabs.github.io/)[[code]](https://github.com/vimalabs/VIMA)
* diffusion-based generation, optimization, and planning in 3d scenes [[paper]](https://arxiv.org/pdf/2301.06015.pdf)[[project]](https://scenediffuser.github.io/)[[code]](https://github.com/scenediffuser/Scene-Diffuser)
* lotus: continual imitation learning for robot manipulation through unsupervised skill discovery [[paper]](http://arxiv.org/abs/2311.02058) [[project]](https://ut-austin-rpl.github.io/Lotus/)
* imitating shortest paths in simulation enables effective navigation and manipulation in the real world [[paper]](https://arxiv.org/abs/2312.02976) [[project]](https://spoc-robot.github.io/)
* thinkbot: embodied instruction following with thought chain reasoning [[paper]](https://arxiv.org/abs/2312.07062) [[project]](https://guanxinglu.github.io/thinkbot/)
* clip-fields: weakly supervised semantic fields for robotic memory [[paper]](https://arxiv.org/abs/2210.05663) [[project]](https://mahis.life/clip-fields) [[code]](https://github.com/notmahi/clip-fields)
* usa-net: unified semantic and affordance representations for robot memory [[paper]](https://arxiv.org/abs/2304.12164) [[project]](https://usa.bolte.cc/) [[code]](https://github.com/codekansas/usa)

#### relevant to robotics (perception)

##### open-vocabulary object detection and 3d classification
* simple open-vocabulary object detection with vision transformers [[paper]](https://arxiv.org/pdf/2205.06230.pdf)[[code]](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit)
*  grounded language-image pre-training [[paper]](https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Grounded_Language-Image_Pre-Training_CVPR_2022_paper.pdf)[[code]](https://github.com/microsoft/GLIP)
*  grounding dino: marrying dino with grounded pre-training for open-set object detection [[paper]](https://arxiv.org/abs/2303.05499)[[code]](https://github.com/IDEA-Research/GroundingDINO)
*  pointclip: point cloud understanding by clip [[paper]](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_PointCLIP_Point_Cloud_Understanding_by_CLIP_CVPR_2022_paper.pdf)[[code]](https://github.com/ZrrSkywalker/PointCLIP)
*  point-bert: pre-training 3d point cloud transformers with masked point modeling [[paper]](https://arxiv.org/abs/2111.14819)[[code]](https://github.com/lulutang0608/Point-BERT)
*  ulip: learning a unified representation of language, images, and point clouds for 3d understanding [[paper]](https://arxiv.org/abs/2212.05171)[[project]](https://tycho-xue.github.io/ULIP/)[[code]](https://github.com/salesforce/ULIP)
*  ulip-2: towards scalable multimodal pre-training for 3d understanding [[paper]](https://arxiv.org/pdf/2305.08275.pdf)[[code]](https://github.com/salesforce/ULIP)
*  3d-vista: pre-trained transformer for 3d vision and text alignment [[paper]](https://arxiv.org/pdf/2308.04352.pdf)[[project]](https://3d-vista.github.io/)[[code]](https://github.com/3d-vista/3D-VisTA)

##### open-vocabulary semantic segmentation
* language-driven semantic segmentation [[paper]](https://arxiv.org/abs/2201.03546)[[code]](https://github.com/isl-org/lang-seg)
* emerging properties in self-supervised vision transformers [[paper]](https://arxiv.org/abs/2104.14294)[[code]](https://github.com/facebookresearch/dino)
* segment anything [[paper]](https://arxiv.org/abs/2304.02643)[[project]](https://segment-anything.com/)
* fast segment anything [[paper]](https://arxiv.org/abs/2306.12156)[[code]](https://github.com/CASIA-IVA-Lab/FastSAM)
* faster segment anything: towards lightweight sam for mobile applications [[paper]](https://arxiv.org/abs/2306.14289)[[code]](https://github.com/ChaoningZhang/MobileSAM)
* track anything: segment anything meets videos [[paper]](https://arxiv.org/abs/2304.11968)[[code]](https://github.com/gaomingqi/Track-Anything)

##### open-vocabulary 3d scene representations
* open-vocabulary queryable scene representations for real world planning (nlmap) [[paper]](https://arxiv.org/pdf/2209.09874.pdf)[[project]](https://nlmap-saycan.github.io/)
* clip-nerf: text-and-image driven manipulation of neural radiance fields [[paper]](https://arxiv.org/abs/2112.05139)[[project]](https://cassiepython.github.io/clipnerf/)
* clip-fields: weakly supervised semantic fields for robotic memory [[paper]](https://arxiv.org/abs/2210.05663) [[project]](https://mahis.life/clip-fields) [[code]](https://github.com/notmahi/clip-fields)
* lerf: language embedded radiance fields [[paper]](https://arxiv.org/abs/2303.09553)[[project]](https://www.lerf.io/)[[code]](https://github.com/kerrj/lerf)
* decomposing nerf for editing via feature field distillation [[paper]](https://arxiv.org/abs/2205.15585)[[project]](https://pfnet-research.github.io/distilled-feature-fields)

##### object representations
* foundationpose: unified 6d pose estimation and tracking of novel objects [[paper]](https://arxiv.org/abs/2312.08344)[[project]](https://nvlabs.github.io/FoundationPose/)
* bundlesdf: neural 6-dof tracking and 3d reconstruction of unknown objects [[paper]](https://arxiv.org/abs/2303.14158)[[project]](https://bundlesdf.github.io//)
* neural descriptor fields: se(3)-equivariant object representations for manipulation [[paper]](https://arxiv.org/abs/2112.05124)[[project]](https://yilundu.github.io/ndf/)
* distilled feature fields enable few-shot language-guided manipulation [[paper]](https://arxiv.org/abs/2308.07931)[[project]](https://f3rm.github.io/)
* you only look at one: category-level object representations for pose estimation from a single example [[paper]](https://arxiv.org/abs/2305.12626)
* zero-shot category-level object pose estimation [[paper]](https://arxiv.org/abs/2204.03635)[[code]](https://github.com/applied-ai-lab/zero-shot-pose)
* viola: imitation learning for vision-based manipulation with object proposal priors [[paper]](https://arxiv.org/abs/2210.11339)[[project]](https://ut-austin-rpl.github.io/VIOLA/)[[code]](https://github.com/UT-Austin-RPL/VIOLA)
* learning generalizable manipulation policies with object-centric 3d representations [[paper]](http://arxiv.org/abs/2310.14386)[[project]](https://ut-austin-rpl.github.io/GROOT/)[[code]](https://github.com/UT-Austin-RPL/GROOT)

##### affordance information
* affordance diffusion: synthesizing hand-object interactions [[paper]](https://arxiv.org/abs/2303.12538)[[project]](https://judyye.github.io/affordiffusion-www/)
* affordances from human videos as a versatile representation for robotics [[paper]](https://arxiv.org/abs/2304.08488)[[project]](https://robo-affordances.github.io/)

##### predictive models
* adversarial inverse reinforcement learning with self-attention dynamics model [[paper]](https://ieeexplore.ieee.org/document/9361118)
* connected autonomous vehicle motion planning with video predictions from smart, self-supervised infrastructure [[paper]](https://arxiv.org/pdf/2309.07504.pdf)
* self-supervised traffic advisors: distributed, multi-view traffic prediction for smart cities [[paper]](https://arxiv.org/abs/2204.06171)
* planning with diffusion for flexible behavior synthesis [[paper]](https://arxiv.org/abs/2205.09991)
* phenaki: variable-length video generation from open domain textual description [[paper]](https://arxiv.org/abs/2210.02399)
* robonet: large-scale multi-robot learning [[paper]](https://arxiv.org/abs/1910.11215)
* gaia-1: a generative world model for autonomous driving [[paper]](https://arxiv.org/abs/2309.17080)
* learning universal policies via text-guided video generation [[paper]](https://arxiv.org/abs/2302.00111)
* video language planning [[paper]](https://arxiv.org/abs/2310.10625)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

#### relevant to robotics (embodied ai)
* inner monologue: embodied reasoning through planning with language models [[paper]](https://arxiv.org/abs/2207.05608)[[project]](https://innermonologue.github.io/)
* statler: state-maintaining language models for embodied reasoning [[paper]](https://arxiv.org/abs/2306.17840)[[project]](https://statler-lm.github.io/)
* embodiedgpt: vision-language pre-training via embodied chain of thought [[paper]](https://arxiv.org/pdf/2305.15021.pdf)[[project]](https://embodiedgpt.github.io/)
* minedojo: building open-ended embodied agents with internet-scale knowledge [[paper]](https://openreview.net/forum?id=rc8o_j8I8PX)[[code]](https://github.com/MineDojo/MineDojo)
* video pretraining (vpt): learning to act by watching unlabeled online videos [[paper]](https://arxiv.org/abs/2206.11795)
* open-world multi-task control through goal-aware representation learning and adaptive horizon prediction [[paper]](https://arxiv.org/pdf/2301.10034.pdf)[[code]](https://github.com/CraftJarvis/MC-Controller)
* describe, explain, plan and select: interactive planning with llms enables open-world multi-task agents [[paper]](https://arxiv.org/pdf/2302.01560.pdf)[[code]](https://github.com/CraftJarvis/MC-Planner)
* voyager: an open-ended embodied agent with large language models [[paper]](https://arxiv.org/abs/2305.16291)[[project]](https://voyager.minedojo.org/)[[code]](https://github.com/MineDojo/Voyager)
* ghost in the minecraft: generally capable agents for open-world environments via large language models with text-based knowledge and memory [[paper]](https://arxiv.org/abs/2305.17144)[[project]](https://github.com/OpenGVLab/GITM)
* language models as zero-shot planners: extracting actionable knowledge for embodied agents [[paper]](https://arxiv.org/pdf/2201.07207.pdf)[[project]](https://wenlong.page/language-planner/)[[code]](https://github.com/huangwl18/language-planner)
* groot: learning to follow instructions by watching gameplay videos [[paper]](https://arxiv.org/pdf/2310.08235.pdf)[[project]](https://craftjarvis.github.io/GROOT/)[[code]](https://github.com/CraftJarvis/GROOT)
* jarvis-1: open-world multi-task agents with memory-augmented multimodal language models [[paper]](https://arxiv.org/pdf/2311.05997.pdf)[[project]](https://craftjarvis.github.io/JARVIS-1/)[[code]](https://github.com/CraftJarvis/JARVIS-1)
* sqa3d: situated question answering in 3d scenes [[paper]](https://arxiv.org/pdf/2210.07474.pdf)[[project]](https://sqa3d.github.io/)[[code]](https://github.com/SilongYong/SQA3D)
* mp5: a multi-modal open-ended embodied system in minecraft via active perception [[paper]](https://arxiv.org/pdf/2312.07472.pdf)[[project]](https://iranqin.github.io/MP5.github.io/)[[code]](https://github.com/IranQin/MP5)
* minedreamer: learning to follow instructions via chain-of-imagination for simulated-world control [[paper]](https://arxiv.org/pdf/2403.12037.pdf)[[project]](https://sites.google.com/view/minedreamer/main)[[code]](https://github.com/Zhoues/MineDreamer)

##### generalist ai
* generative agents: interactive simulacra of human behavior [[paper]](https://arxiv.org/abs/2304.03442)
* towards generalist robots: a promising paradigm via generative simulation [[paper]](https://arxiv.org/abs/2305.10455)
* a generalist agent [[paper]](https://arxiv.org/abs/2205.06175)
* an embodied generalist agent in 3d world [[paper]](https://arxiv.org/pdf/2311.12871.pdf)[[project]](https://embodied-generalist.github.io/)[[code]](https://github.com/embodied-generalist/embodied-generalist)

##### simulators
* gibson env: real-world perception for embodied agents [[paper]](https://arxiv.org/abs/1808.10654)
* igibson 2.0: object-centric simulation for robot learning of everyday household tasks [[paper]](https://arxiv.org/abs/2108.03272)[[project]](https://svl.stanford.edu/igibson/)
* behavior-1k: a benchmark for embodied ai with 1,000 everyday activities and realistic simulation [[paper]](https://openreview.net/forum?id=_8DoIe8G3t)[[project]](https://behavior.stanford.edu/behavior-1k)
* habitat: a platform for embodied ai research [[paper]](https://arxiv.org/abs/1904.01201)[[project]](https://aihabitat.org/)
* habitat 2.0: training home assistants to rearrange their habitat [[paper]](https://arxiv.org/abs/2106.14405)
* robothor: an open simulation-to-real embodied ai platform [[paper]](https://arxiv.org/abs/2004.06799)[[project]](https://ai2thor.allenai.org/robothor/)
* virtualhome: simulating household activities via programs [[paper]](https://arxiv.org/abs/1806.07011)
* arnold: a benchmark for language-grounded task learning with continuous states in realistic 3d scenes [[paper]](https://arxiv.org/pdf/2304.04321.pdf)[[project]](https://arnold-benchmark.github.io/)[[code]](https://github.com/arnold-benchmark/arnold)
* alfred: a benchmark for interpreting grounded instructions for everyday tasks [[paper]](https://arxiv.org/abs/1912.01734)[[project]](https://askforalfred.com/)[[code]](https://github.com/askforalfred/alfred)
* libero: benchmarking knowledge transfer in lifelong robot learning [[paper]](https://arxiv.org/pdf/2306.03310.pdf)[[project]](https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/overview.html)[[code]](https://github.com/Lifelong-Robot-Learning/LIBERO)
* procthor: large-scale embodied ai using procedural generation [[paper]](https://arxiv.org/abs/2206.06994)[[project]](https://procthor.allenai.org/)[[code]](https://github.com/allenai/procthor)
