# planning, control, and symbolic reasoning

engineering curriculum, mathematical modeling, algorithmic optimization, classical ai planning, and curated resources for trajectory planning, optimal control, and autonomous navigation.

---

## architecture overview

```
[global map & target goal]
             │
             ▼
[global path search: a* / rrt*]
             │
             ▼
[trajectory optimization: minimum snap / b-spline]
             │
             ▼
[local reactive controller: mpc / cbf / stanley]
             │
             ▼
[actuator commands: velocity / torque / thrust]
```

---

## complete checklist and resources

### 01. control theory – kontrol sistemleri

#### 9.1 classical control

- [ ] system modeling
- [ ] transfer functions
- [ ] laplace transform
- [ ] block diagrams
- [ ] feedback systems
- [ ] open-loop control
- [ ] closed-loop control
- [ ] pid controllers
- [ ] stability
- [ ] root locus
- [ ] bode plots
- [ ] nyquist stability criterion
- [ ] frequency response

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe akademik ve mühendislik kaynakları):**
  1. **odtü ee302 – feedback systems (prof. dr. m. mert ankaralı ders sayfası):** [blog.metu.edu.tr/mertan](https://blog.metu.edu.tr/mertan/) — klasik kontrol sistemleri ders sayfası
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **brian douglas – control systems lectures & matlab tech talks:** [youtube kanalı (control system lectures)](https://www.youtube.com/@BrianBDouglas) & [resmi arşiv (engineeringmedia.com)](https://engineeringmedia.com/) — **[ilk izlenecek – temel seri]** pid, bode, nyquist, root locus ve geri besleme (feedback) mantığını sıfır ezberle görselleştiren referans seri
- **oku (klasik ders kitapları — önem sırasıyla):**
  1. **feedback control of dynamic systems (gene franklin, j. dapowell, abbas emami-naeini):** [pearson kitap sayfası](https://www.pearson.com/en-us/subject-catalog/p/feedback-control-of-dynamic-systems/P200000003242) — abd üniversitelerindeki en iyi kontrol tasarımı kitabı
  2. **modern control engineering (katsuhiko ogata):** klasik kontrol mühendisliği referans kitabı

#### 9.2 modern control

- [ ] state-space representation
- [ ] state transition matrix
- [ ] controllability
- [ ] observability
- [ ] pole placement
- [ ] linear quadratic regulator (lqr)
- [ ] linear quadratic gaussian (lqg)
- [ ] state feedback
- [ ] optimal control

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe akademik kaynaklar):**
  1. **prof. dr. m. mert ankaralı (odtü ee402 – discrete-time control systems):** [resmi ders sayfası (blog.metu.edu.tr/mertan)](https://blog.metu.edu.tr/mertan/) & [youtube ders kanalı (@technicaltutorials8909)](https://www.youtube.com/@technicaltutorials8909) — ayrık zamanlı sistemler, durum uzayı (state-space), durum geri beslemesi (state feedback) ve gözlemleyici (observer) tasarımı (düzeltme: odtü ee402 video dersleri m. mert ankaralı'ya aittir; prof. klaus werner schmidt'in alanı ayrık olay sistemlerinin kontrolüdür)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **steve brunton – control bootcamp (state-space, controllability, observability, lqr, lqg & kalman filter):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m) — **[ilk izlenecek – zorunlu seri]** modern kontrol teorisini (lqr ve lqg) 20 kısa videoda matrislerle ve matlab/python kodlarıyla öğreten referans seri
  2. **brian douglas – state-space equations & modern control:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLUMWjy5jgHK3j74Z5Tq6Tso1fSfVWZC8L) — durum uzayı denklemlerinin fiziksel sezgisi
- **oku (ücretsiz kitaplar — önem sırasıyla):**
  1. **data-driven science and engineering: machine learning, dynamical systems, and control (brunton & kutz – bölüm 8):** [databookuw.com (ücretsiz pdf)](https://databookuw.com/databook.pdf) — lqr, lqg ve modern durum uzayı kontrolü
  2. **feedback systems: an introduction for scientists and engineers (karl j. åström & richard m. murray – caltech):** [fbswiki.org (ücretsiz tam kitap pdf)](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers) — modern durum uzayı kontrolünün en iyi ücretsiz ders kitabı

#### 9.3 advanced control

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

#### 9.4 autonomous motion

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

---

### 02. path planning & decision making

#### 11.1 classical path planning

- [ ] configuration space (c-space)
- [ ] grid-based planning
- [ ] breadth-first search (bfs)
- [ ] dijkstra
- [ ] a*
- [ ] d* lite
- [ ] rrt (rapidly-exploring random trees)
- [ ] rrt*
- [ ] prm (probabilistic roadmaps)
- [ ] potential fields
- [ ] visibility graphs

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **brian douglas – autonomous navigation: path planning (a*, rrt, potential fields):** [youtube videosu](https://www.youtube.com/watch?v=Fw8JQ5Q-ZwU) — **[ilk izlenecek]** ızgara tabanlı (grid-based) ve örnekleme tabanlı (sampling-based) yol planlama algoritmalarının 15 dakikada genel resmini çizme
  2. **cmu 16-782 – planning and decision making in robotics (prof. maxim likhachev):** [ders sayfası & materyaller](https://www.cs.cmu.edu/~maxim/classes/robotplanning/) & [youtube ders videoları](https://www.youtube.com/results?search_query=maxim+likhachev+search+based+planning) — **[dünya zirvesi akademik ders]** a*, weighted a*, ara* ve d* lite algoritmalarını bizzat icat eden profesörün dersleri
  3. **mit 16.410 / 16.413 – principles of autonomy and decision making:** [mit ocw ders sayfası](https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/) — havacılık ve uzay otonomi planlaması
- **oku & repo (ücretsiz kitap ve kodlar — önem sırasıyla):**
  1. **repo – atsushisakai/pythonrobotics (path planning bölümü):** [github.com/atsushisakai/pythonrobotics#path-planning](https://github.com/AtsushiSakai/PythonRobotics#path-planning) — **[uygulamalı kodlar]** dijkstra, a*, d* lite, potential field, prm, rrt ve rrt* algoritmalarının çalışan python simülasyonları
  2. **planning algorithms (steven m. lavalle – uiuc):** [lavalle.pl/planning (ücretsiz tam kitap pdf)](https://lavalle.pl/planning/) — **[temel akademik kitap]** rrt'nin mucidi olan profesörün yazdığı, konfigürasyon uzayı (c-space) ve hareket planlamanın ücretsiz referans kitabı

#### 11.2 motion planning

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

#### 11.3 decision making

- [ ] finite state machines (fsm)
- [ ] behavior trees (bt)
- [ ] rule-based systems
- [ ] decision theory
- [ ] markov decision processes (mdp)
- [ ] partially observable markov decision processes (pomdp)
- [ ] hierarchical planning
- [ ] task and motion planning (tamp)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **petter ögren – behavior trees in robotics and ai lectures (kth royal institute of technology):** [youtube kanalı & ders serisi](https://www.youtube.com/@PetterOgren/videos) — **[ilk izlenecek]** klasik sonlu durum makinelerinin (fsm) neden karmaşık robotlarda çöktüğünü ve davranış ağaçlarının (behavior trees) nasıl modüler karar verdiğini anlatan en iyi seri
  2. **davide faconti – behaviortree.cpp & groot2 tutorials:** [behaviortree.dev/docs/intro](https://www.behaviortree.dev/docs/intro) — c++ ve ros 2 ile davranış ağacı kodlama
- **oku & repo (ücretsiz kitaplar ve c++ kodları — önem sırasıyla):**
  1. **behavior trees in robotics and ai: an introduction (michele colledanchise & petter ögren):** [arxiv:1709.00084 (ücretsiz tam kitap pdf)](https://arxiv.org/pdf/1709.00084.pdf) — **[zorunlu kitap]** iha görev yönetimi ve otonom robot karar mekanizması için başucu kitabı
  2. **algorithms for decision making (mykel j. kochenderfer, tim a. wheeler, kyle h. wray – stanford):** [algorithmsbook.com (ücretsiz tam kitap pdf)](https://algorithmsbook.com/files/dm.pdf) — **[belirsizlik altında karar verme]** mdp, pomdp ve olasılıksal karar teorisi için mit press tarafından basılan ücretsiz başyapıt
  3. **repo – behaviortree/behaviortree.cpp & ros-planning/navigation2:** [github.com/behaviortree/behaviortree.cpp](https://github.com/BehaviorTree/BehaviorTree.CPP) · [github.com/ros-planning/navigation2](https://github.com/ros-planning/navigation2) — ros 2 nav2'nin görev koordinasyonunda kullandığı endüstriyel c++17 behavior tree kütüphanesi

#### 11.4 multi-agent systems

- [ ] multi-robot coordination
- [ ] distributed decision making
- [ ] multi-agent planning
- [ ] cooperative robotics
- [ ] swarm intelligence
- [ ] multi-agent reinforcement learning (marl)
- [ ] decentralized swarm trajectory planning (mader / rmader)

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **prof. vijay kumar (upenn grasp lab) – aerial swarm robotics & cooperative autonomy:** [youtube sunumları](https://www.youtube.com/results?search_query=vijay+kumar+swarm+robotics+grasp+lab) — **[ilk izlenecek – sürü iha temeli]** sürü iha'ların (swarm uavs) merkeziyetsiz koordinasyonu, formasyon kontrolü ve ortak haritalaması
  2. **prof. jonathan p. how (mit acl) – decentralized multi-agent coordination & robust trajectory planning:** [youtube sunum & seminer serisi](https://www.youtube.com/results?search_query=jonathan+how+mit+multi+agent+trajectory+planning) — **[çoklu ajan planlama dersi]** mader ve robust-mader'in arkasındaki iletişim gecikmeleri, asenkron koordinasyon ve dinamik engeller altında merkeziyetsiz çarpışmasız yörünge planlaması (deconfliction) ve konsensüs teorisi
- **oku (ücretsiz referans kitap):**
  1. **multiagent systems: algorithmic, game-theoretic, and logical foundations (yoav shoham & kevin leyton-brown – stanford):** [masfoundations.org (ücretsiz tam kitap pdf)](http://www.masfoundations.org/mas.pdf) — çoklu ajan karar verme ve oyun teorisi temelleri
- **simülatör & açık kaynak repo (önem sırasıyla):**
  1. **scrimmage multi-agent simulator (georgia tech research institute - gtri):** [gtri/scrimmage (github)](https://github.com/gtri/scrimmage) & [dokümantasyon](https://gtri.github.io/scrimmage/sphinx/html/index.html) — **[kitlesel sürü & çoklu ajan simülatörü]** onlarca/yüzlerce iha, kara aracı ve robotik ajanın sürü koordinasyonu (swarm robotics), diferansiyel oyun teorisi, dağıtık görev paylaşımı ve çoklu ajan pekiştirmeli öğrenmesi (marl) için geliştirilmiş yüksek başarımlı c++/python simülasyon altyapısı
  2. **mader & robust-mader: decentralized multi-agent trajectory planner (mit acl – ieee t-ro):** [mader github (mit-acl/mader)](https://github.com/mit-acl/mader) & [rmader github (mit-acl/rmader)](https://github.com/mit-acl/rmader) — **[çoklu iha & dinamik sürü yörünge planlayıcısı]** prof. jonathan p. how ekibinin geliştirdiği; dinamik ve bilinmeyen ortamlarda uçan çoklu iha sürülerinin merkeziyetsiz (decentralized), asenkron ve iletişim gecikmelerine dayanıklı çarpışmasız yörünge üretimi (deconfliction) yapan çığır açıcı c++/ros mimarisi

---

### 03. classical ai – sembolik yapay zekâ, akıl yürütme ve planlama

#### 27.1 search & problem solving – arama ve problem çözme

- [ ] uninformed search (bfs, dfs, iterative deepening)
- [ ] informed search (greedy, a*, ida*)
- [ ] admissible and consistent heuristics
- [ ] heuristic design
- [ ] local search (hill climbing, simulated annealing)
- [ ] beam search
- [ ] adversarial search (minimax, alpha-beta pruning)
- [ ] monte carlo tree search
- [ ] constraint satisfaction problems (csp)
- [ ] arc consistency (ac-3)
- [ ] backtracking with forward checking

#### 27.2 logic & automated reasoning – mantık ve otomatik akıl yürütme

- [ ] propositional logic
- [ ] first-order logic
- [ ] resolution and unification
- [ ] forward and backward chaining
- [ ] prolog
- [ ] datalog
- [ ] answer set programming
- [ ] non-monotonic reasoning
- [ ] sat solvers (cdcl)
- [ ] smt solvers (z3)
- [ ] automated theorem proving
- [ ] formal verification basics

#### 27.3 knowledge representation – bilgi temsili

- [ ] semantic networks and frames
- [ ] ontologies (owl)
- [ ] rdf and sparql
- [ ] description logics
- [ ] knowledge graphs
- [ ] knowledge graph embeddings (transe, rotate)
- [ ] rule-based expert systems
- [ ] commonsense knowledge bases (conceptnet)
- [ ] neuro-symbolic integration

#### 27.4 automated planning – otomatik görev planlama

- [ ] strips
- [ ] pddl
- [ ] planning graphs (graphplan)
- [ ] heuristic planners (ff, fast downward)
- [ ] hierarchical task networks (htn)
- [ ] temporal planning
- [ ] contingent and probabilistic planning
- [ ] plan execution and monitoring
- [ ] llm + pddl planning

#### 27.5 game ai – oyun yapay zekâsı

- [ ] expectiminimax
- [ ] counterfactual regret minimization
- [ ] chess engines (stockfish, nnue)
- [ ] alphago and alphazero
- [ ] utility ai
- [ ] goal-oriented action planning (goap)
- [ ] procedural content generation

#### 27.6 intelligent agents & multi-agent theory – akıllı etmenler ve çok etmenli sistem teorisi

- [ ] agent types (reflex, goal-based, utility-based)
- [ ] bdi architecture
- [ ] cognitive architectures (soar, act-r)
- [ ] auctions and negotiation
- [ ] mechanism design
- [ ] coalition formation
- [ ] agent communication protocols

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr:** [şadi evren şeker — yapay zeka (arama algoritmaları, a*, minimax, uzman sistemler) (youtube)](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — klasik arama ve sembolik yapay zeka kavramlarına türkçe giriş.
- **yt:**
  1. **[ilk izlenecek — arama, csp, planlama]** [uc berkeley cs188 — introduction to artificial intelligence (dan klein & pieter abbeel)](https://www.youtube.com/playlist?list=PLp8QV47qJEg67UTShQ4er4RYQ3rOeDKxv) — a*, heuristics, csp, minimax, mcts ve klasik planlamanın standart üniversite dersi.
  2. **[görsel & uygulamalı giriş]** [harvard cs50’s introduction to artificial intelligence with python (youtube)](https://www.youtube.com/watch?v=5NgNicANyqM) — arama, mantık, belirsizlik ve optimizasyon algoritmalarının python ile uygulanışı.
- **oku & repo:**
  1. [stuart russell & peter norvig — artificial intelligence: a modern approach (aima), 4th ed. & aima-python (github)](https://github.com/aimacode/aima-python) — klasik ai, arama, mantık, pddl planlama ve çok etmenli sistemlerin ana başvuru kitabı ve kod deposu.
  2. [plansys2 — ros 2 planning system (ros2_planning_system github)](https://github.com/PlanSys2/ros2_planning_system) — pddl tabanlı sembolik görev planlamayı doğrudan ros 2 robotlarına bağlayan kütüphane.
  3. [z3 theorem prover — microsoft research (github)](https://github.com/Z3Prover/z3) — smt çözümü, kısıt doğrulama ve biçimsel doğrulama (formal verification) için standart araç.
