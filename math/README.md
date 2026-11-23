# mathematics for autonomous systems

engineering curriculum, mathematical proofs, derivations, and curated resources for linear algebra, multivariate calculus, lie groups, probability, and numerical optimization.

---

## handwritten modules & implementations

- **[linear algebra](./linear-algebra/)** — matrix proofs, eigenvalues/eigenvectors, matrix exponential, special hermitian/unitary matrices, 3d vector geometry, and vector spaces.
- **[calculus](./calculus/)** — 3d euclidean vector geometry, dot/cross products, projections, and multivariable foundations.

---

## architecture overview

```
[linear algebra: vector spaces / svd / projections]
                        │
                        ▼
[multivariate calculus: gradients / jacobians / lie theory]
                        │
                        ▼
[probability & statistics: bayes / gaussians / covariance]
                        │
                        ▼
[numerical optimization: gauss-newton / levenberg-marquardt]
                        │
                        ▼
[applied engineering: state estimation / slam / uav dynamics]
```

---

## complete checklist and resources

### 01. mathematics – matematiksel temel

#### 2.1 linear algebra – lineer cebir

**temel konular:**

- [x] scalars, vectors, matrices
- [ ] vector spaces
- [ ] linear independence
- [ ] basis and dimension
- [x] matrix operations
- [x] matrix inverse
- [x] determinants
- [ ] rank and null space
- [x] eigenvalues and eigenvectors
- [ ] orthogonality
- [ ] orthogonal projection
- [ ] matrix decomposition
- [ ] lu decomposition
- [ ] qr decomposition
- [ ] singular value decomposition (svd)
- [ ] positive definite matrices
- [ ] least squares
- [ ] matrix calculus

**ileri bağlantılar:**

- [ ] principal component analysis (pca)
- [ ] optimization
- [ ] computer vision geometry
- [ ] neural networks
- [ ] state estimation
- [ ] 3d transformations ($se(3)$, $so(3)$)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **buders boğaziçiliden özel ders – lineer cebir:** [youtube kanalı oynatma listeleri (@buders5730)](https://www.youtube.com/@Buders) — matris işlemleri, determinant, rank, özdeğer ve özvektörlerin türkçe pratik anlatımı (doğrulanmış oynatma listesi)
  2. **nesin matematik köyü – ali nesin lineer cebir dersleri:** [nesin matematik köyü youtube kanalı](https://www.youtube.com/playlist?list=PL-VAZnoQqQ4UF8Y7Q4rf8ruNSVhnfEmWn) — vektör uzayları ve lineer dönüşümlerin teorik temeli
  3. **kitaplar:** h. hilmi hacısalihoğlu – lineer cebir · bernard kolman – uygulamalı lineer cebir (çeviri)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **3blue1brown – essence of linear algebra:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **[ilk izlenecek]** matrislerin, determinantın ve özdeğerlerin 3b uzaydaki geometrik anlamı
  2. **mit 18.06 linear algebra (prof. gilbert strang):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) — **[ana akademik ders]** svd, least squares, qr/lu ayrıştırma ve dik izdüşüm için temel üniversite dersi
  3. **mit 18.065 matrix methods in data analysis, signal processing, and ml (gilbert strang):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k) — doğrudan yapay zekâ ve optimizasyon odaklı ileri matris yöntemleri
- **📖 oku & 💻 repo (kitap, makale ve kütüphaneler — önem sırasıyla):**
  1. **immersive linear algebra:** [immersivemath.com/ila](http://immersivemath.com/ila/index.html) — etkileşimli grafiklerle lineer cebir ve 3b dönüşüm sezgisi
  2. **mathematics for machine learning (deisenroth, faisal, ong):** [mml-book.github.io (ücretsiz pdf)](https://mml-book.github.io/book/mml-book.pdf) — bölüm 2–4 ve bölüm 10 (pca & svd)
  3. **the matrix calculus you need for deep learning (parr & howard):** [explained.ai/matrix-calculus](https://explained.ai/matrix-calculus/) — sinir ağlarında gradyan ve matris türevleri
  4. **kütüphane – eigen c++:** [eigen.tuxfamily.org](https://eigen.tuxfamily.org/dox/GettingStarted.html) — c++ ile robotik, slam ve durum kestiriminde kullanacağın endüstri standardı lineer cebir kütüphanesi

#### 2.2 calculus – analiz

**temel konular:**

- [x] limits and continuity
- [x] differentiation
- [ ] integration
- [ ] partial derivatives
- [ ] multivariable calculus
- [x] chain rule
- [ ] gradient
- [ ] jacobian matrix
- [ ] hessian matrix
- [ ] directional derivatives
- [ ] vector calculus
- [ ] multiple integrals
- [ ] taylor series
- [ ] differential calculus
- [ ] integral calculus

**ileri bağlantılar:**

- [ ] backpropagation
- [ ] gradient descent
- [ ] neural network optimization
- [ ] robotics kinematics
- [ ] motion planning
- [ ] continuous optimization

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **buders boğaziçiliden özel ders – calculus 1 & calculus 2:** [youtube kanalı & listeler](https://www.youtube.com/@Buders) — limit, türev, integral, çok değişkenli fonksiyonlar, kısmi türev, gradyan ve jakobiyen matrisi
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **3blue1brown – essence of calculus:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **[ilk izlenecek]** türev, zincir kuralı (chain rule) ve taylor serilerinin görsel sezgisi
  2. **mit 18.02 multivariable calculus (prof. denis auroux):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL4C4C8A7D06566F38) — **[ana akademik ders]** 3b uzayda vektör kalkülüsü, gradyan, yönlü türev ve lagrange çarpanları
  3. **mit 18.01 single variable calculus (prof. david jerison):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL590CCC2BC5AF3BC1) — tek değişkenli analiz temelleri
  4. **professor leonard – calculus 1, 2 & 3:** [youtube oynatma listeleri](https://www.youtube.com/@ProfessorLeonard/playlists) — konuyu sıfırdan bol soru çözümüyle pekiştirmek için en detaylı anlatım
- **📖 oku (kitap ve ders notları — önem sırasıyla):**
  1. **mathematics for machine learning – bölüm 5 (vector calculus):** [mml-book.github.io (ücretsiz pdf)](https://mml-book.github.io/book/mml-book.pdf) — jacobian, hessian ve backpropagation matematiği
  2. **paul’s online math notes (calculus i, ii, iii):** [tutorial.math.lamar.edu](https://tutorial.math.lamar.edu/) — adım adım çözümlü örneklerle yazılı başvuru kaynağı

#### 2.3 probability & statistics – olasılık ve istatistik

**temel konular:**

- [ ] probability theory
- [ ] conditional probability
- [ ] bayes’ theorem
- [ ] random variables
- [ ] probability distributions
- [ ] gaussian distribution
- [ ] bernoulli distribution
- [ ] binomial distribution
- [ ] poisson distribution
- [ ] multivariate gaussian
- [ ] expectation and variance
- [ ] covariance and correlation
- [ ] conditional distributions
- [ ] maximum likelihood estimation (mle)
- [ ] maximum a posteriori estimation (map)
- [ ] hypothesis testing
- [ ] confidence intervals
- [ ] statistical inference
- [ ] bayesian statistics
- [ ] monte carlo methods

**ileri bağlantılar:**

- [ ] kalman filter
- [ ] bayesian filtering
- [ ] particle filters
- [ ] probabilistic robotics
- [ ] machine learning
- [ ] uncertainty estimation
- [ ] sensor fusion

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **buders boğaziçiliden özel ders:** [youtube kanalı oynatma listeleri (@buders5730)](https://www.youtube.com/@Buders) — koşullu olasılık, bayes teoremi ve dağılımlar (not: kanalda calculus ve lineer cebir ana listeleri doğrulanmıştır; olasılık ve istatistik başlıklarını kanal içinde aratarak kontrol et)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **statquest with josh starmer – statistics & probability fundamentals:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) — **[ilk izlenecek]** mle, map, kovaryans ve dağılımların en anlaşılır görsel anlatımı
  2. **mit 6.041 probabilistic systems analysis and applied probability (prof. john tsitsiklis):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLUl4u3cNGP60A3XMwZ5sep719_nh95qOe) — **[ana mühendislik dersi]** robotik, sensör gürültüsü ve durum kestirimi için olasılık temeli
  3. **harvard stat 110 – probability (prof. joe blitzstein):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — derin olasılık teorisi, şartlı beklenti ve monte carlo yöntemleri
- **📖 oku (kitap ve interaktif kaynaklar — önem sırasıyla):**
  1. **seeing theory (brown university):** [seeing-theory.brown.edu](https://seeing-theory.brown.edu/) — olasılık dağılımlarını ve bayes çıkarımını tarayıcıda interaktif deneyimleme
  2. **probabilistic machine learning: an introduction (kevin murphy):** [probml.github.io/pml-book](https://probml.github.io/pml-book/book1.html) — **[başucu kitabı]** çok değişkenli gaussian, bayesci öğrenme ve belirsizlik kestirimi (ücretsiz pdf)
  3. **think stats & think bayes (allen downey):** [greenteapress.com](https://greenteapress.com/wp/) — python kodu yazarak olasılık ve bayes filtreleme öğrenimi (ücretsiz)

#### 2.4 differential equations – diferansiyel denklemler

**temel konular:**

- [ ] ordinary differential equations (ode)
- [ ] partial differential equations (pde)
- [ ] linear differential equations
- [ ] nonlinear differential equations
- [ ] initial value problems
- [ ] boundary value problems
- [ ] numerical solutions
- [ ] stability analysis
- [ ] dynamical systems

**nerede kullanılır?**

- [ ] robot hareket modelleri
- [ ] fiziksel sistem simülasyonları
- [ ] kontrol sistemleri
- [ ] dinamik modelleme
- [ ] hareket kestirimi

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **buders boğaziçiliden özel ders:** [youtube kanalı oynatma listeleri (@buders5730)](https://www.youtube.com/@Buders) — ode, başlangıç değer problemleri ve laplace dönüşümü (kanal içinde "diferansiyel denklemler" olarak arat)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **3blue1brown – differential equations:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6) — **[ilk izlenecek]** faz uzayı (phase space), kararlılık ve dinamik sistemlerin görsel sezgisi
  2. **steve brunton – differential equations & dynamical systems:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA) — **[ana mühendislik dersi]** robot kinematiği, kontrol sistemleri ve doğrusal olmayan dinamikler için en iyi mühendislik serisi
  3. **mit 18.03 differential equations (prof. arthur mattuck):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D) — klasik mit diferansiyel denklemler müfredatı
- **📖 oku (kitap ve dokümanlar — önem sırasıyla):**
  1. **data-driven science and engineering (brunton & kutz):** [databookuw.com](https://databookuw.com/) — dinamik sistemler, kontrol ve makine öğrenmesi kesişimi (ücretsiz ders materyalleri)
  2. **paul’s online math notes – differential equations:** [tutorial.math.lamar.edu/classes/de/de.aspx](https://tutorial.math.lamar.edu/Classes/DE/DE.aspx) — pratik çözüm yöntemleri ve örnekler
  3. **nonlinear dynamics and chaos (steven strogatz):** [kitap ve ders sayfası](https://www.youtube.com/playlist?list=PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V) — doğrusal olmayan sistemler ve kararlılık analizi

#### 2.5 optimization – optimizasyon

**temel konular:**

- [ ] convex optimization
- [ ] nonlinear optimization
- [ ] linear programming
- [ ] quadratic programming
- [ ] gradient descent
- [ ] stochastic gradient descent (sgd)
- [ ] adam and adamw
- [ ] newton’s method
- [ ] constrained optimization
- [ ] lagrange multipliers
- [ ] kkt conditions (karush-kuhn-tucker)
- [ ] least squares optimization
- [ ] nonlinear least squares
- [ ] gauss-newton
- [ ] levenberg-marquardt

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **itü / odtü sayısal optimizasyon açık ders notları:** [odtü ocw](https://ocw.metu.edu.tr/) — kısıtlı/kısıtsız optimizasyon, lagrange çarpanları ve kkt koşulları
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **cyrill stachniss – least squares, gauss-newton & levenberg-marquardt (slam dersleri):** [youtube ders videoları](https://www.youtube.com/results?search_query=cyrill+stachniss+least+squares+gauss+newton) — **[ilk izlenecek]** robotik, kamera kalibrasyonu ve slam'de doğrusal olmayan en küçük karelerin nasıl çalıştığını doğrudan anlatır
  2. **stanford ee364a – convex optimization (prof. stephen boyd):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL3940DD956CDF0622) — **[ana akademik ders]** konveks optimizasyon, qp, lagrange ve kkt için dünyadaki referans ders
  3. **steve brunton – optimization bootcamp:** [youtube videoları](https://www.youtube.com/results?search_query=steve+brunton+optimization) — gradyan inişi ve mühendislik optimizasyonu özeti
- **📖 oku & 💻 repo (kitap, rehber ve kütüphaneler — önem sırasıyla):**
  1. **ceres solver tutorial (non-linear least squares):** [ceres-solver.org/nnls_tutorial.html](https://github.com/ceres-solver/ceres-solver) — **[uygulamalı c++ kütüphanesi]** google'ın slam ve bundle adjustment için geliştirdiği c++ optimizasyon kütüphanesi
  2. **convex optimization (boyd & vandenberghe):** [web.stanford.edu/~boyd/cvxbook](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — tam metin ücretsiz pdf kitap
  3. **methods for non-linear least squares problems (madsen, nielsen, tingleff – dtu):** [ücretsiz pdf rehber](https://www2.imm.dtu.dk/pubdb/edoc/imm3215.pdf) — gauss-newton ve levenberg-marquardt algoritmalarının en net 60 sayfalık matematiksel türetimi
  4. **numerical optimization (nocedal & wright):** [springer kitap sayfası](https://link.springer.com/book/10.1007/978-0-387-40065-5) — sayısal optimizasyon teorisi

#### 2.6 numerical methods – sayısal yöntemler

**temel konular:**

- [ ] numerical integration
- [ ] numerical differentiation
- [ ] root finding
- [ ] interpolation
- [ ] approximation
- [ ] numerical linear algebra
- [ ] error analysis
- [ ] numerical stability
- [ ] floating point arithmetic
- [ ] runge-kutta methods (rk4)
- [ ] euler methods
- [ ] heun’s method

**neden önemli?** matematiksel olarak tanımladığın bir sistemin bilgisayar üzerinde nasıl hesaplanacağını öğrenirsin.

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **buders boğaziçiliden özel ders:** [youtube kanalı oynatma listeleri (@buders5730)](https://www.youtube.com/@Buders) — euler, runge-kutta (rk4), kök bulma, interpolasyon ve sayısal türev/integral (kanal içinde "sayısal analiz" olarak arat)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **jeffrey chasnov – numerical methods for engineers (hkust):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLkZjai-2Jcxn35XnijUtqqEg0Wi5Sn8ab) — **[ilk izlenecek]** mühendisler için rk4, ode çözücüleri ve sayısal kararlılık
  2. **mit 18.085 computational science and engineering (prof. gilbert strang):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D) — sayısal lineer cebir ve diferansiyel denklem çözümleri
- **📖 oku (kitap ve makaleler — önem sırasıyla):**
  1. **numerical computing with matlab (cleve moler):** [mathworks.com/moler/chapters.html](https://www.mathworks.com/moler/chapters.html) — ücretsiz okunabilir bölümler (kayan nokta aritmetiği, ode çözücüleri, svd)
  2. **what every computer scientist should know about floating-point arithmetic (david goldberg):** [ücretsiz makale (oracle docs)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) — c++ ve gpu programlamada hassasiyet kaybı (fp32/fp16) ve yuvarlama hatalarını anlamak için zorunlu okuma
  3. **numerical linear algebra (trefethen & bau):** [siam kitap sayfası](https://my.siam.org/Store/Product/viewproduct/?ProductId=950) — sayısal kararlılık ve matris algoritmaları
  4. **conjugate gradient without the agonizing pain (jonathan richard shewchuk – cmu):** [cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf) — **[seyrek sistemler ve optimizasyon başyapıtı]** robotikte, slam'de (ceres/gtsam) ve fizikte büyük seyrek lineer denklem sistemlerini ve kuadratik optimizasyonu çözen konjüge gradyan (cg) yöntemini dünyada en berrak ve sezgisel anlatan kült doküman

#### 2.7 diğer matematik alanları

**temel konular:**

- [ ] discrete mathematics
- [ ] graph theory
- [ ] combinatorics
- [ ] set theory
- [ ] mathematical logic
- [ ] information theory
- [ ] signal processing mathematics
- [ ] fourier analysis
- [ ] laplace transform
- [ ] z-transform
- [ ] complex numbers
- [ ] tensor algebra
- [ ] lie groups and lie algebras ($so(3)$, $se(3)$)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları (şadi evren şeker) – ayrık matematik & graf teorisi:** [resmi site ve ders listesi (sadievrenseker.com)](https://sadievrenseker.com/) — kümeler, mantık, kombinatorik ve çizge (graf) kuramı temelleri
  2. **buders boğaziçiliden özel ders:** [youtube kanalı oynatma listeleri (@buders5730)](https://www.youtube.com/@Buders) — üniversite düzeyi ayrık matematik konuları (kanal içinde "ayrık matematik" olarak arat)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **mit 6.042j mathematics for computer science (prof. tom leighton):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLB7540DEDD482705B) — **[ilk izlenecek]** bilgisayar bilimi için ispat yöntemleri, graf teorisi ve ayrık matematik
  2. **william fiset – graph theory playlist:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) — algoritmalar ve yol planlama (path planning) öncesi en iyi görsel graf teorisi serisi
  3. **brad osgood – the fourier transform and its applications (stanford ee261):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLB24BC7956EE040CD) — görüntü işleme ve sinyal analizi için fourier dönüşümü
  4. **mit 6.003 signals and systems (prof. dennis freeman):** [mit ocw / youtube serisi](https://www.youtube.com/playlist?list=PL41692B571DD0AF9B) — laplace ve z-dönüşümü, filtreleme ve frekans uzayı
  5. **eigenchris – tensors for beginners & lie groups:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLJHszsWbB6hrkmmq57lX8BV-o-YIOFsiG) — tensör cebiri ve diferansiyel geometri
  6. **welch labs – imaginary numbers are real:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLiaHhY2iBX9g6KIvZ_703G3KJXapKkNaF) — karmaşık sayıların görsel sezgisi
- **📖 oku (kitap ve makaleler — önem sırasıyla):**
  1. **a micro lie theory for state estimation in robotics (joan solà et al.):** [arxiv:1812.01537 (ücretsiz pdf)](https://arxiv.org/pdf/1812.01537.pdf) — **[robotik & slam için zorunlu makale]** $so(3)$ ve $se(3)$ lie gruplarını mühendisler için en sade anlatan başucu makalesi
  2. **lie groups for 2d and 3d transformations (ethan eade):** [ethaneade.com/lie.pdf](https://ethaneade.com/lie.pdf) — 3b dönüşüm matrisleri ve üstel haritalama (exponential map) el kitabı
  3. **optimization on smooth manifolds (nicolas boumal):** [nicolasboumal.net/book](https://www.nicolasboumal.net/book/) — **[manifold optimizasyonunun kutsal kitabı]** lie grupları ($so(3), se(3)$), grassmannian ve riemann manifoldları üzerinde türev alma ve gradyan inişi (riemannian optimization) yapmanın dünyadaki 1 numaralı açık kaynak referans kitabı
  4. **mathematics for computer science (lehman, leighton, meyer – mit):** [ücretsiz tam kitap pdf](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) — mit'nin resmi ayrık matematik ders kitabı
  5. **the scientist and engineer's guide to digital signal processing (steven w. smith):** [dspguide.com](https://www.dspguide.com/pdfbook.htm) — sensör filtreleme ve dsp için ücretsiz pratik kitap
  6. **information theory, inference, and learning algorithms (david mackay):** [inference.org.uk/itprnn/book.pdf](https://www.inference.org.uk/itprnn/book.pdf) — bilgi teorisi (entropi, kl-divergence) ve olasılıksal çıkarım

---

### 02. scientific computing & research engineering

#### 17.1 scientific computing

- [ ] numerical computing
- [ ] scientific python
- [ ] scipy
- [ ] numpy internals
- [ ] jax
- [ ] parallel computing
- [ ] numerical optimization
- [ ] simulation
- [ ] monte carlo simulation
- [ ] computational modeling

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **steve brunton – scientific computing & data-driven engineering in python:** [youtube kanalı](https://www.youtube.com/@Eigensteve) — bilimsel hesaplama, diferansiyel çözücüler, fft ve simülasyon
- **📖 oku & 💻 doküman (önem sırasıyla):**
  1. **python scientific lecture notes (scipy lectures):** [scipy-lectures.org](https://scipy-lectures.org/) — **[ilk okunacak]** numpy iç yapısı (strides, broadcasting), scipy optimizasyon/entegrasyon ve hızlandırma rehberi
  2. **jax official documentation (autograd and xla – google):** [jax.readthedocs.io/en/latest/quickstart.html](https://jax.readthedocs.io/en/latest/quickstart.html) — gpu/tpu üzerinde otomatik türev (`grad`), vektörizasyon (`vmap`) ve jit derleme (`jit`) ile ultra-hızlı bilimsel hesaplama ve robot simülasyonu (mujoco mjx)

#### 17.2 research methodology

- [ ] scientific literature review
- [ ] paper reading
- [ ] research questions
- [ ] hypothesis formulation
- [ ] experimental design
- [ ] baseline models
- [ ] benchmarking
- [ ] ablation studies
- [ ] statistical significance
- [ ] reproducibility
- [ ] research writing (latex)
- [ ] technical documentation

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **andrew ng (stanford cs230) – career advice & reading research papers:** [youtube videosu](https://www.youtube.com/watch?v=733m6qBH-jI) — **[ilk izlenecek]** bir ai makalesini 3 geçişte (three-pass method) nasıl okuyacağın ve literatür taramasını nasıl yapacağın
  2. **overleaf official latex tutorials:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLPN-43XehstNCE7EzhxX513R2qmjbwc8K) — akademik makale ve teknik rapor yazımı
- **📖 oku (zorunlu rehberler — önem sırasıyla):**
  1. **how to read a paper (prof. s. keshav – university of waterloo):** [ccr.sigcomm.org/online/files/p83-keshava.pdf (ücretsiz 2 sayfalık pdf)](https://ccr.sigcomm.org/online/files/p83-keshavA.pdf) — **[zorunlu okuma]** makalelerde kaybolmadan çekirdek fikri ve matematiği çıkarma tekniği
  2. **learn latex in 30 minutes (overleaf documentation):** [overleaf.com/learn/latex/learn_latex_in_30_minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) — denklem, algoritma bloğu ve kaynakça (bibtex) yazımı

#### 17.3 advanced research areas

- [ ] representation learning
- [ ] geometric deep learning
- [ ] neural fields
- [ ] differentiable programming
- [ ] differentiable simulation
- [ ] physics-informed neural networks (pinn)
- [ ] neural operators
- [ ] self-supervised representation learning
- [ ] test-time adaptation
- [ ] continual learning
- [ ] robust machine learning
- [ ] uncertainty-aware ai

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **steve brunton – physics-informed machine learning (piml & pinns):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — **[ilk izlenecek]** fizik yasalarını (diferansiyel denklemleri ve korunum yasalarını) doğrudan sinir ağının loss fonksiyonuna ve mimarisine gömme
  2. **prof. michael bronstein (oxford) – geometric deep learning course:** [youtube ders serisi](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **[ileri akademik ders]** simetriler, değişmezlik (equivariance/invariance), gruplar, graflar ve 3b manifoldlar üzerinde derin öğrenme
- **📖 oku (ücretsiz kitap ve proje sayfaları — önem sırasıyla):**
  1. **geometric deep learning: grids, groups, graphs, geodesics, and gauges (bronstein, bruna, cohen, veličković):** [geometricdeeplearning.com (ücretsiz tam kitap pdf)](https://geometricdeeplearning.com/) — cnn, gnn ve transformer'ları tek bir geometrik çatı altında birleştiren başyapıt
  2. **physics-informed neural networks – pinns (maziar raissi et al.):** [maziarraissi.github.io/pinns](https://maziarraissi.github.io/PINNs/) — fizik tabanlı derin öğrenme makale ve kodları

#### 17.4 graduate-level specializations

- [ ] computer vision
- [ ] robotics
- [ ] autonomous systems
- [ ] machine learning
- [ ] artificial intelligence
- [ ] 3d computer vision
- [ ] control systems
- [ ] computer science
- [ ] embedded ai
- [ ] computational imaging

**kaynaklar (önem ve çalışma sırasına göre):**

- **📖 oku & 💻 platformlar (akademik sıralama ve makale takibi — önem sırasıyla):**
  1. **csrankings: computer science rankings (prof. emery berger):** [csrankings.org](https://csrankings.org/#/fromyear/2016/toyear/2026/index?ai&vision&mlmining&robotics&world) — **[akademik laboratuvar arama platformu]** abd, avrupa ve dünyadaki üniversiteleri doğrudan computer vision (cvpr/iccv), robotics (icra/iros/rss) ve ml (neurips/icml) yayın güçlerine göre filtreleyip hangi profesörün hangi laboratuvarı yönettiğini gösteren site
  2. **arxiv computer science (robotics`cs.ro`& computer vision`cs.cv`):** [arxiv.org/list/cs.ro/recent](https://arxiv.org/list/cs.RO/recent) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — günlük yeni araştırmaları takip etme
  3. **hugging face daily papers & connected papers:** [huggingface.co/papers](https://huggingface.co/papers) · [connectedpapers.com](https://www.connectedpapers.com/) —  bir araştırma konusundaki en etkili makalelerin atıf ağacını görsel olarak çıkarma
