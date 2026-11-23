# autonomy and flight

engineering curriculum, mathematical modeling, simulation environments, and curated resources for autonomous uav flight dynamics, autopilots, and gps-denied navigation.

---

## architecture overview

autonomous flight requires tightly coupling physics, low-level microcontroller firmware, state estimation, and high-level trajectory planning:

```
[sensors: imu / optical flow / stereo camera / lidar]
                        │
                        ▼
           [state estimation: ekf2 / vio]
                        │
                        ▼
      [trajectory generation: minimum snap / b-spline]
                        │
                        ▼
     [geometric tracking control: se(3) position & attitude]
                        │
                        ▼
      [control allocation & motor mixing: px4 / ardupilot]
                        │
                        ▼
           [actuators: brushless motors & escs]
```

---

## study checklist

### 01. flight dynamics and physics
- [ ] multirotor and fixed-wing aerodynamics: lift, drag, blade flapping, ground effect, thrust coefficients
- [ ] 6-dof nonlinear equations of motion in body and inertial reference frames ($se(3)$ kinematics)
- [ ] coriolis and centripetal accelerations, moment of inertia tensor, gyroscopic torque
- [ ] motor and esc dynamics: thrust-to-weight ratio, voltage sag, rpm feedback via dshot protocol

### 02. flight control architectures
- [ ] cascaded pid loops: angular rate (inner loop), attitude, velocity, and position (outer loop)
- [ ] feedforward acceleration compensation and integral anti-windup strategies
- [ ] geometric tracking control on $so(3)$ and $se(3)$ manifolds to prevent gimbal lock
- [ ] model predictive control (mpc) and control barrier functions (cbf) for dynamic obstacle avoidance

### 03. autopilot firmware and middleware
- [ ] px4 autopilot architecture: uorb publish-subscribe messaging bus, flight modes, and task scheduling
- [ ] px4 ekf2 24-state navigation filter and control allocation geometry
- [ ] ardupilot architecture: ap_hal hardware abstraction layer, ekf3 estimation, and chibios rtos
- [ ] mavlink communication protocol: message serialization, telemetry streams, and mission microservices
- [ ] ros 2 integration via micro-xrce-dds agent and uxrce-dds client

### 04. gps-denied navigation and spatial awareness
- [ ] visual-inertial odometry (vio) integration for local state estimation (vins-fusion, orb-slam3)
- [ ] downward-facing optical flow and lidar rangefinder sensor fusion
- [ ] occupancy voxel mapping in 3d space (octomap, esdf) for safe flight corridor generation
- [ ] companion computer architecture: high-rate offboard setpoint streaming (mavsdk, ros 2 px4_msgs)

### 05. software-in-the-loop (sitl) simulation
- [ ] px4 sitl with gazebo harmonic and jmavsim environments
- [ ] custom airframe definitions, aerodynamic coefficients, and sensor noise simulation
- [ ] hardware-in-the-loop (hitl) validation on stm32 flight controllers
- [ ] flight log analytics: parsing ulog files with pyulog, vibration spectral fft analysis, and ekf tuning

---

## curated resources

### video lectures & course series
- [phil's lab – hardware design, sensor interfacing & flight controller firmware in c/c++](https://www.youtube.com/@PhilsLab): end-to-end custom stm32 flight controller hardware design, imu/barometer sensor interfacing, and kalman filter firmware.
- [eth zürich robotics and perception group (rpg)](https://www.youtube.com/@ailabRPG/playlists): cutting-edge lectures on agile uav flight, vision-based navigation, event cameras, and high-speed autonomy.
- [brian douglas – autonomous navigation & path tracking](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg): comprehensive engineering tutorials on path tracking, pure pursuit, and control loop structures.
- [feigao fast lab (hkust) – autonomous uav planning and exploration](https://www.youtube.com/results?search_query=fei+gao+fast+lab+motion+planning): trajectory optimization, kinodynamic planning, and autonomous exploration algorithms for micro aerial vehicles.

### seminal books & academic papers
- [small unmanned aircraft: theory and practice (randy beard & tim mclain – byu magicc lab)](http://uavbook.byu.edu/): the primary engineering textbook for 6-dof quadrotor and fixed-wing flight dynamics, state-space linearization, and cascaded control loops.
- [geometric tracking control of a quadrotor uav on se(3) (taeyoung lee, melvin leok, n. harris mcclamroch – ieee cdc)](https://arxiv.org/abs/1003.2005): foundational paper establishing singularity-free geometric tracking control on lie groups for aggressive quadrotor maneuvers.
- [minimum snap trajectory generation and control for quadrotors (daniel mellinger & vijay kumar – ieee icra)](https://ieeexplore.ieee.org/document/5980409): mathematical proof of quadrotor differential flatness and minimum snap polynomial trajectory planning.
- [px4 architectural concept & companion computer integration guide](https://docs.px4.io/main/en/concept/architecture.html): official architectural reference for px4 flight tasks, uorb messaging, and companion computer bridges.
- [ardupilot architecture and ap_hal documentation](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html): in-depth breakdown of ardupilot hardware abstraction and ekf3 estimation architecture.

### open-source codebases & tools
- [px4/px4-autopilot](https://github.com/PX4/PX4-Autopilot): industry-standard flight control stack with modular uorb drivers, state estimation, and mixer logic.
- [ardupilot/ardupilot](https://github.com/ArduPilot/ardupilot): mature autopilot codebase featuring ap_hal abstraction, advanced failsafes, and multi-vehicle support.
- [mavlink/qgroundcontrol](https://github.com/mavlink/qgroundcontrol): cross-platform ground control station for parameter calibration, mission planning, and real-time telemetry visualization.
- [kumarrobotics/kr_mav_control](https://github.com/KumarRobotics/kr_mav_control): university of pennsylvania grasp lab's se(3) geometric tracking controller implementation.
- [flightmare (uzh rpg)](https://github.com/uzh-rpg/flightmare): flexible quadrotor simulation platform with unity rendering for vision-based learning and control.
- [mavlink/mavsdk](https://github.com/mavlink/MAVSDK): modern c++ api library for offboard autonomous mission control over mavlink.

---

## extended uav & autonomy resource archive

### 8.5 robot simulation

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

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **articulated robotics – simulating a robot with gazebo & ros 2:** [youtube videosu](https://www.youtube.com/watch?v=laWn7_cj434) — **[ilk izlenecek]** urdf/xacro modeline fizik, kamera ve lidar ekleyip gazebo'da sürme
  2. **nvidia developer – nvidia isaac sim & isaac ros tutorials:** [youtube oynatma listesi](https://www.youtube.com/results?search_query=nvidia+isaac+sim+tutorial+ros2) — **[fotogerçekçi gpu simülasyonu]** ray-tracing tabanlı sensör simülasyonu, sentetik veri üretimi ve donanım hızlandırmalı robotik
- **oku & simülatör dokümanları (önem sırasıyla):**
  1. **gazebo sim (modern ignition gazebo) official docs:** [gazebosim.org/docs](https://gazebosim.org/docs) — ros 2 ile entegre açık kaynak fizik ve sensör simülatörü
  2. **nvidia isaac sim & isaaclab (nvidia & eth zürich):** [isaac-sim.github.io/isaaclab](https://isaac-sim.github.io/IsaacLab/) & [github (isaac-sim/isaaclab)](https://github.com/isaac-sim/IsaacLab) — **[gpu-paralel robot öğrenmesi standartı]** tek bir gpu üzerinde binlerce robotu eşzamanlı simüle ederek insansı ve bacaklı robotlara dakikalar içinde yürüme ve manipülasyon politikaları eğiten 8.6k+ yıldızlı resmi simülasyon ve rl çerçevesi
  3. **mujoco (multi-joint dynamics with contact – deepmind):** [mujoco.readthedocs.io](https://mujoco.readthedocs.io/en/stable/overview.html) & [github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — robot öğrenmesi (rl) ve temas dinamiği için dünyanın en hızlı c/c++ fizik motoru
  4. **px4 & ardupilot sitl (software-in-the-loop) simulation guides:** [docs.px4.io/main/en/simulation](https://docs.px4.io/main/en/simulation/) · [ardupilot sitl (ardupilot.org)](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) — iha ve otonom araç algoritmalarını (copter, plane, vtol, rover) gerçek uçuş öncesi gazebo, jsbsim ve ros üzerinde donanımsız simüle edip test etme
  5. **luckyengine & luckyrobots (mujoco robotik simülatörü):** [luckyrobots (github)](https://github.com/luckyrobots/luckyrobots) & [luckyrobots.readthedocs.io](https://luckyrobots.readthedocs.io) — mujoco fizik motorunu grpc ile python'a bağlayan; robot manipülatörleri, dört bacaklı (unitree go2) ve insansı (g1) robotlar için gymnasium (`luckyenv`) rl arayüzü sunan yeni nesil simülasyon ortamı
  6. **flightmare: flexible quadrotor simulator (uzh rpg – corl):** [flightmare.bitbucket.io](https://github.com/uzh-rpg/flightmare) & [github repo (uzh-rpg/flightmare)](https://github.com/uzh-rpg/flightmare) — **[otonom iha & dron yarışı simülatörü]** davide scaramuzza ekibinin geliştirdiği; saniyede yüzbinlerce adım simüle eden ultra hızlı c++ çok rotorlu aerodinamik motoru ile unity fotogerçekçi render motorunu ayıran, otonom iha'lara takviyeli öğrenme (rl) ile çevik uçuş ve engelden kaçma öğreten açık kaynak simülatör
  7. **rotors: modular gazebo mav simulator (eth zürich asl – springer):** [github repo (ethz-asl/rotors_simulator)](https://github.com/ethz-asl/rotors_simulator) & [wiki](https://github.com/ethz-asl/rotors_simulator/wiki) — **[ros & gazebo çok rotorlu iha simülasyonu standartı]** prof. roland siegwart ekibinin geliştirdiği; asctec firefly ve hummingbird gibi çok rotorlu iha modelleri, gerçekçi imu gürültü modelleri, stereo/kamera/lidar sensör simülasyonları ve se(3) geometrik uçuş kontrolcüleri (lee controller) sunan 1.5k+ yıldızlı gazebo/ros simülatör çerçevesi
  8. **aerial gym simulator (ntnu arl & nvidia isaac gym):** [github repo (ntnu-arl/aerial_gym_simulator)](https://github.com/ntnu-arl/aerial_gym_simulator) & [aerialgym.com](https://aerialgym.com/) — **[gpu-paralel uçan robotik & rl simülasyonu]** prof. kostas alexis ekibinin geliştirdiği; nvidia isaac gym üzerinde tek bir gpu'da on binlerce iha'yı eşzamanlı simüle eden, derin pekiştirmeli öğrenme (rl) ile aerodinamik etkiler altında çevik uçuş, engelden kaçma ve görsel navigasyon politikaları eğiten 780+ yıldızlı yüksek başarımlı simülasyon çerçevesi
  9. **drake: model-based design and verification for robotics (mit csail – robotlocomotion):** [drake.mit.edu](https://drake.mit.edu/) & [github repo (robotlocomotion/drake)](https://github.com/RobotLocomotion/drake) — **[matematiksel robotik simülasyonu & yörünge optimizasyonu]** prof. russ tedrake ekibinin geliştirdiği; c++ ile yazılmış, kinematik, temas dinamiği, doğrusal olmayan optimizasyon (snopt, ipopt), lqr ve lyapunov kararlılık analizi sunan, humanoid ve manipülatör sistemleri için 4.3k+ yıldızlı mit csail simülasyon ve kontrol motoru

### 9.3 advanced control

- [ ] model predictive control (mpc)
- [ ] nonlinear control
- [ ] adaptive control
- [ ] robust control
- [ ] sliding mode control
- [ ] gain scheduling
- [ ] trajectory tracking & geometric control (se(3))
- [ ] optimal trajectory generation
- [ ] stochastic control
- [ ] distributed control
- [ ] model predictive path integral (mppi) & gpu-optimal kontrol
- [ ] dynamical systems (ds) & kararlı reaktif kontrol (epfl lasa)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **steve brunton & matlab tech talks – model predictive control (mpc) explained:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLn8PRpmsu08ozoeoXgxPSBKLyd4YEHww8) — **[ilk izlenecek]** kısıtlar altında gelecekteki yörüngeyi tahmin edip optimize eden mpc kontrolcüsünün çalışma prensibi
  2. **mit 6.832 – underactuated robotics (prof. russ tedrake):** [youtube tam dönem ders serisi](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — **[ileri akademik kontrol dersi]** doğrusal olmayan dinamik kontrol, lqr, mpc, lyapunov kararlılığı ve yörünge optimizasyonu (trajectory optimization)
  3. **eth zürich – flying machine arena lectures (prof. raffaello d'andrea):** [youtube sunumları](https://www.youtube.com/results?search_query=raffaello+d%27andrea+quadrocopter+control) — agresif manevra yapan otonom iha'ların doğrusal olmayan kontrolü
- **oku & repo (ücretsiz kitap ve endüstriyel kodlar — önem sırasıyla):**
  1. **underactuated robotics: algorithms for walking, running, swimming, flying, and manipulation (russ tedrake – mit):** [underactuated.csail.mit.edu (ücretsiz interaktif kitap & jupyter kodları)](https://underactuated.csail.mit.edu/) — **[başucu kitabı]** iha ve robot kontrolü için dünyadaki en modern ücretsiz kitap
  2. **predictive control for linear and hybrid systems (borrelli, bemporad, morari):** [mpc.berkeley.edu (ücretsiz kitap pdf)](https://www.mpc.berkeley.edu/mpc-course-material) — mpc matematiğinin standart ders kitabı
  3. **repo – commaai/openpilot:** [github.com/commaai/openpilot](https://github.com/commaai/openpilot) — **[gerçek araç kodu]** 250+ gerçek otomobil modelinde otonom şerit takibi ve hız kontrolü yapan açık kaynak sistemin `selfdrive/controls` altındaki mpc ve kalman filtresi c++/python kodlarını incele
  4. **kütüphane – casadi/casadi & acados/acados:** [web.casadi.org](https://web.casadi.org/) · [docs.acados.org](https://docs.acados.org/) — c++ ve python ile gömülü sistemlerde gerçek zamanlı doğrusal olmayan mpc (nmpc) çözmek için kullanılan endüstri standardı kütüphaneler
  5. **kr_mav_control: se(3) geometric quadrotor tracking control (upenn grasp lab – icra / cdc):** [github repo (kumarrobotics/kr_mav_control)](https://github.com/KumarRobotics/kr_mav_control) — **[iha geometrik kontrol c++ yığını]** vijay kumar ve daniel mellinger ekibinin geliştirdiği; euler açılarındaki kilitlenme (gimbal lock) problemini ortadan kaldırmak için doğrudan $so(3)$ ve $se(3)$ lie grupları üzerinde çalışan, agresif akrobatik manevralarda ve yüksek hızlı otonom uçuşlarda milimetrik yörünge takibi yapan açık kaynak c++ kontrol paketi
  6. **rosplane & vtolsim: fixed-wing & vtol autopilot (byu magicc lab – beard & mclain):** [rosplane (github)](https://github.com/byu-magicc/rosplane) · [vtolsim (github)](https://github.com/byu-magicc/vtolsim) — **[sabit kanat ve vtol iha otopilot yığını]** beard & mclain teorisini ros/c++ ile hayata geçiren; ardışık döngü kapatmalı (successive loop closure) irtifa/hız/yatış pid otopilot kontrolü, vektör alanı (vector field) tabanlı yol takibi ve dikey kalkış-sabit kanat geçiş (vtol) dinamiği sunan açık kaynak c++/python otopilot mimarisi
  7. **mppi control (model predictive path integral – mit acl):** [github repo (mit-acl/mppi_numba)](https://github.com/mit-acl/mppi_numba) — **[gpu hızlandırmalı olasılıksal optimal kontrol]** numba ve cuda kullanarak yüzlerce hz frekansta binlerce olasılıksal yörünge örneği türeten, karmaşık ve doğrusal olmayan robot dinamiklerinde risk duyarlı engelden kaçma ve kontrol sağlayan gpu-mppi kontrol mimarisi
  8. **dynamical systems (ds) for robot control & learning (epfl lasa – prof. aude billard / mit press):** [epfl-lasa.github.io](https://epfl-lasa.github.io/) · [github (epfl-lasa/fast_dynamical_systems)](https://github.com/epfl-lasa) & [seds (github)](https://github.com/epfl-lasa/icra-lfd-tutorial) — **[dinamik sistemlerle kararlı reaktif kontrol & manipülasyon]** prof. aude billard'ın mit press tarafından yayımlanan başucu teorisi; diferansiyel denklemler ve lyapunov kararlılığı (seds) kullanarak robot manipülatörlerinin beklenmedik insan müdahalelerinde veya hareketli engellerde bile hedefe güvenle ve sarsıntısız ulaşmasını garanti eden reaktif kontrol ve taklit öğrenmesi (lfd) kütüphanesi

### 9.4 autonomous motion

- [ ] trajectory generation
- [ ] trajectory optimization
- [ ] path tracking (pure pursuit, stanley controller)
- [ ] velocity control
- [ ] motion constraints
- [ ] dynamic constraints
- [ ] collision avoidance
- [ ] model-based planning

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **brian douglas – autonomous navigation & path tracking tech talks:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg) — **[ilk izlenecek]** pure pursuit, stanley controller ve yörünge takibi temelleri
  2. **eth zürich – autonomous mobile robots (motion control module – prof. roland siegwart):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) — mobil robotlarda kinematik kısıtlar ve yörünge takibi
- **oku, repo & kurs (kod, kitap ve uzmanlık serisi — önem sırasıyla):**
  1. **repo – atsushisakai/pythonrobotics (path tracking bölümü):** [github.com/atsushisakai/pythonrobotics#path-tracking](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — **[hemen çalıştırılacak kodlar]** pure pursuit, stanley, rear-wheel feedback, lqr ve mpc yörünge takip algoritmalarının animasyonlu ve temiz python implementasyonları
  2. **university of toronto – self-driving cars specialization (coursera – prof. steven waslander):** [coursera.org/specializations/self-driving-cars](https://www.coursera.org/specializations/self-driving-cars) — otonom araçlarda yanal (lateral - stanley/pure pursuit) ve boylamsal (longitudinal) kontrol denklemleri (not: youtube serisi değil, coursera uzmanlık programıdır)
  3. **trajectory planning for automatic machines and robots (luigi biagiotti & claudio melchiorri):** [springer kitap sayfası](https://link.springer.com/book/10.1007/978-3-540-85629-0) — hız, ivme ve sarsıntı (jerk / minimum snap) kısıtlı yörünge üretimi

### 11.2 motion planning

- [ ] configuration space planning
- [ ] collision checking
- [ ] trajectory planning
- [ ] sampling-based planning
- [ ] optimization-based planning (chomp, trajopt)
- [ ] kinodynamic planning & online replanning
- [ ] time-optimal planning
- [ ] safe motion planning
- [ ] graph-based exploration (gbplanner) & darpa subt otonomi
- [ ] fast & safe trajectory planning beyond sensor horizon (faster)
- [ ] ego-planner & gcopter (zju fast lab) yörünge optimizasyonu
- [ ] otonom hacimsel keşif ve sürü uçuş planlaması (fuel & racer)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **prof. dmitry berenson – motion planning lectures (university of michigan):** [youtube kanalı & ders videoları](https://www.youtube.com/results?search_query=dmitry+berenson+motion+planning) — **[ilk izlenecek – temel planlama]** çok serbestlik dereceli robotlarda çarpışma kontrolü, örnekleme ve optimizasyon tabanlı (chomp, trajopt) hareket planlama
  2. **prof. fei gao (zju fast lab) & hkust aerial robotics (boyu zhou) – autonomous uav planning, exploration & swarm lectures:** [youtube seminer & ders serisi](https://www.youtube.com/results?search_query=fei+gao+fast+lab+motion+planning) — **[iha yörünge optimizasyonu & otonom keşif dersi]** ego-planner, fuel ve gcopter mimarilerinin arkasındaki b-spline yörünge optimizasyonu, esdf'siz gradyan arama ve hiyerarşik sınır tabanlı otonom keşif teorisinin amfi dersleri
  3. **prof. russ tedrake (mit 6.832 / 6.821 – underactuated robotics: trajectory optimization):** [youtube ders oynatma listesi (mit)](https://www.youtube.com/playlist?list=PLkx8KyIQkMfU5szP43GlE_S1QGSPQfL9s) — **[zirve matematiksel planlama dersi]** doğrudan kolokasyon (direct collocation), non-lineer dinamik kısıtlar altında kinodinamik yörünge optimizasyonu ve engellerden kaçma teorisi
- **oku & kütüphane (kitap ve c++ planlama motoru — önem sırasıyla):**
  1. **the open motion planning library (ompl – c++ kütüphanesi):** [ompl.kavrakilab.org](https://ompl.kavrakilab.org/) & [github repo (ompl/ompl)](https://github.com/ompl/ompl) — **[endüstri standardı c++ kütüphanesi]** ros 2 moveit 2'nin altında çalışan rrt*, prm ve kinodinamik planlayıcıların saf c++ kodu
  2. **principles of robot motion: theory, algorithms, and implementations (howie choset, kevin lynch, seth hutchinson et al.):** [mit press kitap sayfası](https://mitpress.mit.edu/9780262033275/principles-of-robot-motion/) — robot hareket teorisinin kapsamlı referans kitabı
  3. **kr_autonomous_flight: autonomous flight system for gps-denied quadrotors (upenn grasp lab):** [github repo (kumarrobotics/kr_autonomous_flight)](https://github.com/KumarRobotics/kr_autonomous_flight) — **[tam yığın otonom uçuş & kinodinamik hareket planlama]** vijay kumar laboratuvarının açık kaynak tam otonom mimarisi; gps'siz ve bilinmeyen karmaşık ortamlarda 3b haritalama, gerçek zamanlı kinodinamik yörünge üretimi (online replanning), engellerden kaçma ve se(3) kontrolünü birleştiren entegre c++ otonomi yığını
  4. **gbplanner_ros & mbplanner_ros: graph-based & motion-primitives exploration planner (ntnu arl / team cerberus – darpa subt champion):** [github repo (ntnu-arl/gbplanner_ros)](https://github.com/ntnu-arl/gbplanner_ros) & [mbplanner_ros](https://github.com/ntnu-arl/mbplanner_ros) — **[darpa subterranean challenge şampiyonu otonom keşif ve yol planlama]** prof. kostas alexis liderliğindeki darpa subt şampiyonu ekibin geliştirdiği; gps'ten yoksun yer altı tünelleri ve karmaşık 3b ortamlarda iki katmanlı (yerel ve küresel) graf tabanlı hacimsel keşif planlaması (bifurcated graph search) ve iha/dört bacaklı robotlar için dinamik hareket primitifleri sunan dünya standardı c++/ros keşif yığını
  5. **faster: fast and safe trajectory planner in unknown environments (mit acl – ieee/rsj iros):** [github repo (mit-acl/faster)](https://github.com/mit-acl/faster) — **[sensör menzilinin ötesinde yüksek hızlı uçuş]** prof. jonathan p. how ekibinin geliştirdiği; iha'ların sensör görüş ufkunun ötesinde güvenle uçmasını sağlayan; taahhüt edilen güvenli yörünge ile yedek yörüngeyi (backup trajectory) eşzamanlı planlayarak bilinmeyen ortamlarda takılmadan ve duraksamadan yüksek hızlı agresif uçuş sağlayan mixed-integer quadratic programming (miqp) tabanlı c++ yörünge planlayıcısı
  6. **ego-planner & gcopter: gradient-based trajectory optimization (zju fast lab & hkust – ieee t-ro):** [ego-planner (github)](https://github.com/ZJU-FAST-Lab/ego-planner) · [gcopter (github)](https://github.com/ZJU-FAST-Lab/GCOPTER) — **[esdf'siz ultra hızlı iha yörünge optimizasyonu standardı]** prof. fei gao ve prof. shaojie shen laboratuvarının geliştirdiği; hesaplama yükü yüksek olan mesafe alanlarına (esdf) ihtiyaç duymadan doğrudan nokta bulutları üzerinden çarpışmasız b-spline yörünge üreten (ego-planner) ve minco (minimum kontrol eforu) polinom formülasyonuyla sık ormanlarda ve bilinmeyen engeller arasında agresif otonom sürü uçuşu sağlayan 3.6k+ yıldızlı c++ otonomi yığını
  7. **fuel & racer: fast autonomous exploration & multi-uav planning (cuhk unmanned systems lab / hkust – boyu zhou / ieee ra-l & ieee t-ro):** [fuel github (hkust-aerial-robotics/fuel)](https://github.com/HKUST-Aerial-Robotics/FUEL) & [racer github (robotics-star-lab/racer)](https://github.com/Robotics-STAR-Lab/RACER) — **[hızlı otonom iha keşfi & merkeziyetsiz sürü koordinasyonu]** prof. boyu zhou ve shaojie shen ekibinin geliştirdiği; bilinmeyen karmaşık ortamlarda sınır alanlarını (frontier) artımsal hiyerarşik yapıyla tarayarak keşif süresini dramatik biçimde kısaltan (fuel) ve dengesiz iletişim koşullarında birden fazla iha'nın harita keşfini eşgüdümlü yürüten (racer) 1.8k+ yıldızlı açık kaynak otonomi ve hareket planlama çerçevesi

### 12.4 hardware-software integration

- [ ] sensor interfaces
- [ ] actuator interfaces
- [ ] communication protocols
- [ ] firmware integration
- [ ] hardware abstraction layers (hal)
- [ ] system diagnostics
- [ ] fault detection
- [ ] reliability engineering
- [ ] px4 autopilot mimarisi (uorb & ros 2 micro-xrce-dds)
- [ ] ardupilot ap_hal & mavlink telemetri protokolü
- [ ] qgroundcontrol (qgc) & gcs görev planlama
- [ ] iha 6-dof uçuş dinamiği ve kaskad otopilot kontrolü (beard & mclain)
- [ ] se(3) üzerinde geometrik iha takip kontrolü (taeyoung lee)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **phil's lab – hardware design, sensor interfacing & flight controller firmware in c/c++:** [youtube kanalı](https://www.youtube.com/@PhilsLab) — **[ilk izlenecek – muazzam kanal]** sıfırdan iha uçuş kontrol kartı (stm32 + imu + barometre) tasarlayıp üzerinde c ile sensör sürücüsü ve kalman filtresi koşturan uçtan uca mühendislik kanalı
- **oku & repo (endüstriyel otopilot mimarisi — önem sırasıyla):**
  1. **px4 autopilot architectural overview & companion computer integration:** [docs.px4.io/main/en/concept/architecture.html](https://docs.px4.io/main/en/concept/architecture.html) & [github repo (px4/px4-autopilot)](https://github.com/PX4/PX4-Autopilot) — **[gerçek iha mimarisini incele]** sensör sürücülerinin `uorb` mesajlaşma hattıyla durum kestirimine (ekf2) ve kontrolcüye nasıl bağlandığını, ayrıca ros 2 (`uxrce_dds`) ile jetson görev bilgisayarına nasıl konuştuğunu incele
  2. **ardupilot architecture & ap_hal (andrew tridgell / ardupilot team):** [ardupilot.org](https://ardupilot.org/) · [github repo (ardupilot/ardupilot)](https://github.com/ArduPilot/ardupilot) & [mavproxy (github)](https://github.com/ArduPilot/MAVProxy) — **[dünyanın en çok kullanılan otopilot yığını & ap_hal]** andrew tridgell (rsync ve samba mucidi) öncülüğünde geliştirilen; chibios rtos üzerinde çalışan donanım soyutlama katmanı (ap_hal), 24-state ekf3 durum kestirimi, mavlink telemetri protokolü ve döner kanat/sabit kanat/vtol otonom uçuş kontrol mimarisini sunan 11.5k+ yıldızlı küresel otopilot standartı
  3. **qgroundcontrol (qgc – mavlink ground control station):** [qgroundcontrol.com](http://qgroundcontrol.com/) & [github repo (mavlink/qgroundcontrol)](https://github.com/mavlink/qgroundcontrol) — **[açık kaynak iha yer kontrol istasyonu (gcs) standardı]** px4 ve ardupilot otopilotları için dünya standardı çapraz platform (c++ / qt / qml) yer kontrol istasyonu; mavlink üzerinden otonom rota ve görev planlama (waypoint navigation), sensör ve pusula kalibrasyonu, parametre ayarlama, canlı telemetri ve video akışı (rtsp) sunan 3.7k+ yıldızlı temel havacılık arayüzü
  4. **small unmanned aircraft: theory and practice (randy beard & tim mclain – byu magicc lab):** [uavbook.byu.edu](http://uavbook.byu.edu/) & [byu magicc lab](https://magicc.byu.edu/) — **[iha otopilot dinamiği ve uçuş kontrolünün kutsal kitabı]** ardupilot ve px4 otopilotlarının arkasındaki 6-dof rijit cisim hareket denklemleri, aerodinamik kuvvet/moment türetimleri, durum uzayı doğrusallaştırması ve kaskad pid döngülerini (roll/pitch/yaw/irtifa) sıfırdan anlatan dünya çapındaki 1 numaralı referans iha kitabı
  5. **geometric tracking control of a quadrotor uav on se(3) (taeyoung lee, melvin leok, n. harris mcclamroch – ieee cdc):** [arxiv:1003.2005](https://arxiv.org/abs/1003.2005) — **[döner kanatlı iha geometrik kontrol referansı]** dört motorlu iha'larda euler açılarının getirdiği tekillikleri (gimbal lock) ortadan kaldıran; $so(3)$ ve $se(3)$ lie grupları üzerinde lyapunov kararlı agresif yörünge takibi ve akrobasi sağlayan literatürün en çok atıf alan temel iha makalesi

### 12.5 embedded ai

- [ ] tinyml
- [ ] edge inference
- [ ] model quantization (int8, fp8)
- [ ] model pruning
- [ ] knowledge distillation
- [ ] hardware acceleration
- [ ] neural processing units (npu)
- [ ] embedded gpu computing (nvidia jetson mimarisi)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **jetsonhacks – nvidia jetson (orin / nano) edge ai, camera & tensorrt guides:** [youtube kanalı](https://www.youtube.com/@JetsonHacks) & [github (jetsonhacksnano)](https://github.com/JetsonHacksNano) — **[ilk izlenecek]** gerçek bir iha/robot görev bilgisayarı olan nvidia jetson üzerinde kamera sürücüleri, cuda ve c++ tensorrt kurulumu
  2. **mit 6.5940 – tinyml and efficient deep learning computing (prof. song han):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) & [ders sitesi (hanlab.mit.edu/courses/2024-fall-65940)](https://hanlab.mit.edu/courses/2024-fall-65940) — **[dünya zirvesi ders]** model quantization (int8/fp8/int4), pruning, knowledge distillation ve donanım hızlandırmanın tüm matematiği
  3. **shawn hymel – introduction to embedded machine learning (tinyml):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL7VEa1KauMQqZFj_nWRfsCZNXaBbkuurG) — mikrodenetleyiciler üzerinde çıkarım (inference)
- **oku & repo (altın değerinde c++ & tensorrt kod tabanları — önem sırasıyla):**
  1. **repo – dusty-nv/jetson-inference (hello ai world):** [github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference) & [nvidia jetson ai lab](https://www.jetson-ai-lab.com/) — **[temel başlangıç reposu]** nvidia'nın resmi c++ ve python tensorrt tabanlı gerçek zamanlı nesne tespiti, segmentasyon ve poz kestirimi eğitim deposu
  2. **repo – wang-xinyu/tensorrtx:** [github.com/wang-xinyu/tensorrtx](https://github.com/wang-xinyu/tensorrtx) — **[portföy için kritik repo]** yolov8/v11, resnet, detr gibi modellerin pytorch'tan alınıp saf c++ tensorrt api'si ile sıfırdan nasıl yazıldığını gösteren en önemli açık kaynak proje
  3. **tinyml: machine learning with tensorflow lite on arduino and ultra-low-power microcontrollers (pete warden & daniel situnayake):** [o'reilly kitap sayfası](https://www.oreilly.com/library/view/tinyml/9781492052036/) — düşük güçlü gömülü ai referansı

### 38.5 remote sensing & aerial imagery – uzaktan algılama ve hava/uydu görüntüsü analizi

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
