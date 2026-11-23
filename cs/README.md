# computer science and systems

engineering curriculum, algorithmic complexity, hardware architecture, linux infrastructure, and curated resources for data structures, memory hierarchy, operating systems, networking, and production engineering.

---

## architecture overview

```
[high-level code: modern c++ / algorithms]
                     │
                     ▼
[compiler optimization & assembly: instruction pipelining]
                     │
                     ▼
[operating system kernel: posix / threads / virtual memory]
                     │
                     ▼
[memory hierarchy: registers / l1-l2-l3 cache / dram]
                     │
                     ▼
[physical processor: cpu datapath / simd / alu execution]
```

---

## complete checklist and resources

### 01. computer science – bilgisayar biliminin temelleri

#### 3.1 data structures – veri yapıları

- [ ] arrays
- [ ] strings
- [ ] linked lists
- [ ] stacks
- [ ] queues
- [ ] hash tables
- [ ] hash maps
- [ ] sets
- [ ] trees
- [ ] binary trees
- [ ] binary search trees (bst)
- [ ] avl trees
- [ ] red-black trees
- [ ] heaps
- [ ] priority queues
- [ ] tries
- [ ] graphs (adjacency matrix, adjacency list)
- [ ] disjoint set union (dsu)
- [ ] segment trees
- [ ] fenwick trees

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları (şadi evren şeker) – veri yapıları (data structures):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJN9bckI6FbWB03HkmogKrFT) — bağlı listeler, ağaçlar, yığınlar ve hash tablolarının türkçe mantığı
  2. **kitap:** şadi evren şeker – algoritmalar (nobel akademik yayıncılık, 2021)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **cs50x – harvard introduction to computer science (david j. malan):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLhQjrBD2T381WAHyx1pq-sBfykqMBI7V4) — **[ilk izlenecek]** bellek, pointerlar ve temel veri yapılarının en kaliteli başlangıç dersi
  2. **william fiset – data structures easy to advanced course:** [freecodecamp tam video](https://www.youtube.com/watch?v=RBSGKlAvoiM) — **[ana mühendislik dersi]** dinamik dizilerden fenwick tree ve dsu'ya kadar tüm veri yapılarının animasyonlu ve kodlu anlatımı
- **oku & pratik (doküman ve görselleştirme — önem sırasıyla):**
  1. **visualgo (national university of singapore):** [visualgo.net/en](https://visualgo.net/en) — bst, avl, heap ve graf veri yapılarını adım adım animasyonla inceleme
  2. **c++ stl containers reference:** [en.cppreference.com/w/cpp/container](https://en.cppreference.com/w/cpp/container) — c++'ta veri yapılarını (`std::vector`, `std::unordered_map`, `std::priority_queue`) üretim seviyesinde kullanma kılavuzu
  3. **open data structures (in c++):** [opendatastructures.org/ods-cpp.pdf](https://opendatastructures.org/ods-cpp.pdf) — c++ implementasyonlarıyla açık kaynak veri yapıları kitabı

#### 3.2 algorithms – algoritmalar

**temel algoritmalar:**

- [ ] time complexity
- [ ] space complexity
- [ ] big o notation
- [ ] searching algorithms
- [ ] sorting algorithms
- [ ] binary search
- [ ] recursion
- [ ] backtracking
- [ ] divide and conquer
- [ ] greedy algorithms
- [ ] dynamic programming
- [ ] graph traversal
- [ ] bfs (breadth-first search)
- [ ] dfs (depth-first search)
- [ ] dijkstra
- [ ] a*
- [ ] minimum spanning trees (kruskal, prim)
- [ ] shortest path algorithms
- [ ] topological sorting
- [ ] string matching algorithms
- [ ] randomized algorithms

**ileri konular:**

- [ ] computational geometry
- [ ] approximation algorithms
- [ ] online algorithms
- [ ] parallel algorithms
- [ ] optimization algorithms

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları – algoritma analizi (algorithm analysis):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJPTWIUbZjHZMMGuZcpHUv5h) — big-o karmaşıklığı, sıralama, arama ve dinamik programlama temelleri
  2. **kitap:** şadi evren şeker – algoritmalar
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **abdul bari – algorithms course:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O) — **[ilk izlenecek]** divide & conquer, greedy, dynamic programming ve backtracking konularının tahtada en net anlatımı
  2. **mit 6.006 introduction to algorithms (erik demaine & srini devadas):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb) — **[ana akademik ders]** mit'nin efsanevi algoritma analizi, dijkstra ve dp dersi
  3. **william fiset – graph theory & shortest path algorithms:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) — robotik yol planlamanın temeli olan bfs, dfs, dijkstra, a* ve mst algoritmaları
  4. **neetcode – roadmap & leetcode çözümleri:** [youtube kanalı](https://www.youtube.com/@NeetCode) — teknik mülakatlar için algoritma problem çözme stratejileri
- **oku & pratik (kitap ve kodlama platformları — önem sırasıyla):**
  1. **neetcode 150 (uygulamalı problem listesi):** [neetcode.io/practice](https://neetcode.io/practice) — **[zorunlu pratik]** konu konu ayrılmış en kritik 150 algoritma sorusunu c++ ve python ile çöz
  2. **cp-algorithms (c++ algoritma ansiklopedisi):** [cp-algorithms.com](https://cp-algorithms.com/) — graf, geometri ve veri yapısı algoritmalarının doğrudan c++ implementasyonları
  3. **algorithms (jeff erickson – uiuc):** [jeffe.cs.illinois.edu/teaching/algorithms/book/algorithms-jeffe.pdf](https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf) — ücretsiz, modern ve çok derin algoritma ders kitabı
  4. **algorithms, 4th edition (sedgewick & wayne – princeton):** [algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/home/) — görsel ve uygulamalı algoritma referansı
  5. **kdn251/interviews (mülakat & algoritma pratiği):** [github.com/kdn251/interviews](https://github.com/kdn251/interviews) — veri yapıları, temel arama/sıralama algoritmaları ve problem kalıplarının açık kaynaklı github referansı

#### 3.3 computer architecture – bilgisayar mimarisi

- [ ] cpu architecture
- [ ] instruction set architecture (isa)
- [ ] registers
- [ ] cache hierarchy (l1/l2/l3)
- [ ] ram
- [ ] memory bus
- [ ] pipelining
- [ ] branch prediction
- [ ] simd (single instruction multiple data)
- [ ] vectorization
- [ ] gpu architecture
- [ ] memory hierarchy (global, shared, constant)
- [ ] cpu-gpu communication (pcie bant genişliği)
- [ ] cache coherence

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları – bilgisayar mimarisi (computer architecture):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLvNq8wrSYGAU6CF4UleG6HbXa9paQDsLK) — cpu, önbellek (cache), boru hattı (pipeline) ve bellek hiyerarşisi
  2. **prof. dr. onur mutlu – türkçe konferans ve seminerleri:** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=onur+mutlu+t%C3%BCrk%C3%A7e) — bellek sistemleri ve modern işlemci/gpu mimarileri üzerine vizyon konuşmaları
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **prof. dr. onur mutlu – digital design and computer architecture (eth zürich):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi_uej3aY39YB5pfW4SJ7LlN) — **[dünya zirvesi]** bir türk bilim insanının eth zürich'te verdiği, cpu/gpu mimarisi, cache, simd ve bellek sistemleri üzerine dünyadaki en iyi ders
  2. **ben eater – build an 8-bit computer from scratch:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) — register, alu, bus ve makine komutlarının donanımda nasıl çalıştığını gözünle görmek için
  3. **uc berkeley cs61c – great ideas in computer architecture:** [ders sayfası & kaynaklar](https://cs61c.org/) — c, risc-v, simd vektörizasyon ve önbellek optimizasyonu
- **oku (kitap ve teknik rehberler — önem sırasıyla):**
  1. **from nand to tetris (building a modern computer from first principles):** [nand2tetris.org](https://www.nand2tetris.org/) — sıfırdan işlemci ve derleyici tasarımı
  2. **what every programmer should know about memory (ulrich drepper):** [ücretsiz pdf](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) — **[yüksek performanslı c++ için zorunlu]** l1/l2/l3 cache, sanal bellek ve cache-friendly kod yazma rehberi
  3. **agner fog’s software optimization resources:** [agner.org/optimize](https://www.agner.org/optimize/) — c++ ve simd/avx optimizasyon kılavuzları
  4. **computer organization and design (patterson & hennessy):** [kitap sayfası](https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6) — standart ders kitabı

#### 3.4 operating systems – işletim sistemleri

- [ ] processes
- [ ] threads
- [ ] scheduling (cpu scheduling)
- [ ] concurrency
- [ ] context switching
- [ ] virtual memory
- [ ] memory management (paging, segmentation)
- [ ] file systems
- [ ] system calls
- [ ] synchronization
- [ ] mutex
- [ ] semaphore
- [ ] deadlocks
- [ ] race conditions
- [ ] interprocess communication (ipc)
- [ ] networking
- [ ] device drivers
- [ ] kernel concepts
- [ ] interrupts

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları – işletim sistemleri (operating systems):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJO9eiwfQbcA2ThMbUSkbOWf) — process, thread, deadlock, semaphore, mutex ve bellek yönetimi temelleri
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **neso academy – operating systems:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O) — **[ilk izlenecek]** işletim sistemi kavramlarının (scheduling, paging, concurrency) hızlı ve görsel anlatımı
  2. **jacob sorber – systems programming in c/c++:** [youtube kanalı](https://www.youtube.com/@JacobSorber) — **[uygulamalı kodlama]** linux üzerinde `fork`, `pthread`, `mutex`, `mmap`, `ipc` ve soketlerin c/c++ ile gerçek kodlaması
  3. **mit 6.s081 operating system engineering (xv6):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLTsf9UeqkReZHXWY9yJvTwLJWYYPcKEqK) — **[ileri akademik ders]** işletim sistemi çekirdeğini (kernel) sıfırdan inceleme
- **oku (ücretsiz başucu kitapları — önem sırasıyla):**
  1. **operating systems: three easy pieces (ostep – remzi & andrea arpaci-dusseau):** [pages.cs.wisc.edu/~remzi/ostep](https://pages.cs.wisc.edu/~remzi/OSTEP/) — **[dünyanın en iyi os kitabı – ücretsiz pdf]** virtualization, concurrency ve persistence bölümlerini mutlaka oku
  2. **beej’s guide to unix interprocess communication (ipc):** [beej.us/guide/bgipc](https://beej.us/guide/bgipc/) — shared memory, pipes ve message queues pratik rehberi
  3. **the linux programming interface (michael kerrisk):** [man7.org/tlpi](https://man7.org/tlpi/) — linux sistem çağrıları (system calls) ve çekirdek programlama ansiklopedisi

#### 3.5 computer networks – bilgisayar ağları

- [ ] tcp/ip
- [ ] udp
- [ ] http/https
- [ ] dns
- [ ] routing
- [ ] network layers
- [ ] sockets
- [ ] client-server architecture
- [ ] websockets
- [ ] network security fundamentals
- [ ] distributed communication
- [ ] message queues
- [ ] grpc
- [ ] dds (data distribution service)

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **tr: —** (doğrulanmış kapsamlı türkçe robotik ağ/dds oynatma listesi bulunmamaktadır; doğrudan aşağıdaki yt ve oku kaynaklarına geç.)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **jim kurose – computer networking: a top-down approach lectures:** [youtube ders serisi](https://www.youtube.com/playlist?list=PL1ya5dD_M8uX-BLUF1FEvUNsYWQL5_l0O) — **[ana akademik ders]** alanın en ünlü ders kitabının yazarından ağ protokolleri
  2. **hussein nasser – backend & networking fundamentals:** [youtube kanalı](https://www.youtube.com/@hnasr) — tcp, udp, websockets, grpc ve dağıtık haberleşme mimarilerinin mühendislik analizi
  3. **chris greer – wireshark & tcp/ip analysis:** [youtube kanalı](https://www.youtube.com/@ChrisGreer) — ağ paketlerini gerçek zamanlı yakalama ve hata ayıklama
- **oku & doküman (rehber ve protokoller — önem sırasıyla):**
  1. **beej’s guide to network programming (using internet sockets):** [beej.us/guide/bgnet](https://beej.us/guide/bgnet/) — **[uygulamalı c/c++ rehberi]** c/c++ ile sıfırdan tcp/udp soket programlama (iha ve robot telemetrisi için şart)
  2. **eprosima fast dds documentation:** [fast-dds.docs.eprosima.com](https://fast-dds.docs.eprosima.com/) — **[ros 2 haberleşme kalbi]** ros 2'nin altında çalışan gerçek zamanlı data distribution service (dds) mimarisi
  3. **grpc official documentation (c++ & python):** [grpc.io/docs](https://grpc.io/docs/) — mikroservisler ve ai modelleri arası yüksek hızlı rpc iletişimi
  4. **zeromq – the guide:** [zguide.zeromq.org](https://zguide.zeromq.org/) — robotik ve gömülü sistemlerde ultra-hızlı mesaj kuyruğu mimarileri

#### 3.6 software engineering – yazılım mühendisliği

- [ ] object-oriented design (ood)
- [ ] solid principles
- [ ] design patterns
- [ ] clean code
- [ ] software architecture
- [ ] modular programming
- [ ] unit testing
- [ ] integration testing
- [ ] system testing
- [ ] debugging
- [ ] profiling
- [ ] version control (git)
- [ ] code review
- [ ] ci/cd
- [ ] documentation
- [ ] api design

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **gençay yıldız – tasarım desenleri (design patterns) & solid prensipleri:** [youtube kanalı & listeler](https://www.youtube.com/@GencayYildiz/playlists) — oop, solid, clean code ve tasarım desenlerinin türkçe en kapsamlı anlatımı
  2. **bora kaşmer – yazılım ve sistem mimarisi:** [youtube kanalı](https://www.youtube.com/@BoraKasmer) — gerçek dünya yazılım mühendisliği pratikleri ve mimari kararlar
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **mit – the missing semester of your cs education:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J) & [ders sitesi](https://missing.csail.mit.edu/) — **[ilk izlenecek – zorunlu]** git, shell, vim, debugging (gdb), profiling ve yazılım araçları
  2. **arjancodes – software design in python:** [youtube kanalı](https://www.youtube.com/@ArjanCodes) — spagetti koddan kurtulup temiz, modüler ve test edilebilir ai/python kodu yazmak için en iyi kanal
  3. **cppcon – back to basics track:** [youtube oynatma listesi](https://www.youtube.com/results?search_query=cppcon+back+to+basics) — modern c++ ile yazılım tasarımı, bellek yönetimi ve birim testi (unit testing)
- **oku (standartlar ve başucu kitapları — önem sırasıyla):**
  1. [**refactoring.guru**](http://Refactoring.Guru)**(design patterns & clean code):** [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns) — hem c++ hem python kod örnekleriyle tüm tasarım desenlerinin görsel rehberi
  2. **pro git book (scott chacon & ben straub):** [git-scm.com/book/tr/v2](https://git-scm.com/book/tr/v2) — resmi ücretsiz git kitabı (türkçe çevirisi mevcut)
  3. **c++ core guidelines (bjarne stroustrup & herb sutter):** [isocpp.github.io/cppcoreguidelines/cppcoreguidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) — endüstriyel c++ kodlama standartları
  4. **software engineering at google (titus winters et al.):** [abseil.io/resources/swe-book](https://abseil.io/resources/swe-book) — büyük ölçekli mühendislik, kod inceleme (code review), test ve ci/cd kültürü (ücretsiz)

---

### 02. cloud, devops, mlops & production engineering

#### 16.1 linux & infrastructure

- [ ] linux administration
- [ ] shell scripting
- [ ] bash
- [ ] file permissions
- [ ] processes (`ps`, `top`, `htop`, `kill`)
- [ ] networking (`ip`, `netstat`, `ping`, `traceroute`)
- [ ] system monitoring
- [ ] package management (`apt`, `pacman`)
- [ ] ssh & keys
- [ ] system services (`systemd`)

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **tübitak ulakbim / akademik bilişim – gnu/linux sistem yönetimi ders notları:** [ab.org.tr](https://ab.org.tr/) — türkçe açık kaynak linux sistem yönetimi belgeleri
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **learn linux tv – linux crash course & systemd / ssh tutorials:** [youtube kanalı](https://www.youtube.com/@LearnLinuxTV) — robot ve sunucu üzerinde `systemd` servisleri yazma (iha açıldığında otonomi kodunun otomatik başlaması için şart!) ve ssh yönetimi
  2. **networkchuck – linux for beginners series:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL) — hızlı ve pratik terminal hakimiyeti
- **oku & interaktif rehber (önem sırasıyla):**
  1. **linux journey (etkileşimli linux öğrenim platformu):** [linuxjourney.com](https://linuxjourney.com/) — **[temel başlangıç sitesi]** kısa modüllerle tüm linux mimarisini öğren
  2. **the linux command line (william shotts):** [linuxcommand.org/tlcl.php (ücretsiz tam kitap pdf)](https://linuxcommand.org/tlcl.php) — komut satırı ve kabuk programlamanın kapsamlı ücretsiz kitabı

#### 16.2 devops

- [ ] git
- [ ] github
- [ ] gitlab
- [ ] docker
- [ ] docker compose
- [ ] ci/cd
- [ ] github actions
- [ ] testing automation
- [ ] build pipelines
- [ ] infrastructure as code
- [ ] terraform
- [ ] kubernetes

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **kablosuz kedi (gökhan kandemir) – a'dan z'ye docker eğitimi:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLIBhH-mHowD8zBI1WpSR2ZaXV8FSLjhvl) — dockerfile, image, container ve docker compose mantığının türkçe anlatımı
  2. **barış aslan (@barisaslan):** [youtube kanalı](https://www.youtube.com/@BarisAslan) — git/github ve sunucu yayına alma (deployment) dersleri (not: kanal ağırlıklı olarak python/django odaklıdır; ci/cd ve kubernetes için doğrudan aşağıdaki techworld with nana kanalını kullan)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **techworld with nana – docker, github actions & kubernetes tutorials for beginners:** [youtube kanalı](https://www.youtube.com/@TechWorldwithNana) — **[ilk izlenecek – standart rehber]** ai modellerini ve ros 2 düğümlerini her bilgisayarda/robotta aynı şekilde çalıştırmak için docker konteynerleştirme
  2. **kunal kushwaha – complete git, docker & devops bootcamp:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL9gnSGHSqcnoqBXdMwUTRod4Gi3eac2Ak)
- **oku (resmi rehberler — önem sırasıyla):**
  1. **docker official getting started guide:** [docs.docker.com/get-started](https://docs.docker.com/get-started/) — uygulamalı resmi docker başlangıç rehberi
  2. **pro git book (2nd ed. – türkçe & ingilizce):** [git-scm.com/book/tr/v2 (türkçe)](https://git-scm.com/book/tr/v2) · [git-scm.com/book/en/v2 (ingilizce)](https://git-scm.com/book/en/v2) — branching, rebase, submodules ve kurumsal git iş akışları
  3. **devops roadmap:** [roadmap.sh/devops](https://roadmap.sh/devops)

#### 16.3 cloud computing

- [ ] cloud fundamentals
- [ ] virtual machines
- [ ] containers
- [ ] storage (s3, blob)
- [ ] networking (vpc, subnets)
- [ ] serverless computing
- [ ] gpu instances
- [ ] distributed services
- [ ] aws
- [ ] microsoft azure
- [ ] google cloud

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **freecodecamp (andrew brown) – aws certified cloud practitioner full course:** [youtube videosu](https://www.youtube.com/watch?v=SOTamWNgDKc) — **[ilk izlenecek]** bulut sunucular (ec2 / gpu instances), depolama (s3), sanal ağlar (vpc) ve iam yetkilerinin genel mimarisi
- **oku (resmi eğitim platformları):**
  1. **aws skill builder & training:** [aws.amazon.com/training](https://aws.amazon.com/training/)
  2. **microsoft learn – azure fundamentals:** [learn.microsoft.com/en-us/training/azure](https://learn.microsoft.com/en-us/training/azure/)

#### 16.4 mlops

- [ ] experiment tracking
- [ ] model registry
- [ ] model versioning
- [ ] data versioning
- [ ] ml pipelines
- [ ] model deployment
- [ ] model monitoring
- [ ] drift detection (data drift, concept drift)
- [ ] reproducibility
- [ ] automated retraining
- [ ] model governance

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **full stack deep learning (uc berkeley / sergey karayev, josh tobin, pieter abbeel):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) & [ders sitesi (fullstackdeeplearning.com)](https://fullstackdeeplearning.com/course/2022/) — **[ilk izlenecek – temel mlops dersi]** bir ai projesini sıfırdan alıp veri yönetimi, test, ci/cd, dağıtım ve izleme (monitoring) ile gerçek ürüne dönüştürme
  2. **databricks – mlops & mlflow tutorials:** [youtube kanalı](https://www.youtube.com/@Databricks) — model kayıt defteri (model registry) ve deney takibi
- **oku & rehber (başucu kitapları — önem sırasıyla):**
  1. **made with ml (goku mohandas – uçtan uca ücretsiz mlops müfredatı):** [madewithml.com](https://madewithml.com/) — **[en iyi uygulamalı rehber]** tasarım, geliştirme, pytorch eğitimi, test ve üretim dağıtımını kodlarla gösteren interaktif platform
  2. **designing machine learning systems (chip huyen – stanford / o'reilly):** [o'reilly kitap sayfası](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) & [github notları (chiphuyen/dmls-book)](https://github.com/chiphuyen/dmls-book) — ml sistem tasarımı mülakatları ve üretim mimarisi için temel referans kitap
  3. **mlops principles:** [ml-ops.org](https://ml-ops.org/)

#### 16.5 production ai

- [ ] rest apis
- [ ] fastapi
- [ ] model serving
- [ ] scalable inference
- [ ] logging
- [ ] monitoring
- [ ] observability
- [ ] latency optimization
- [ ] reliability
- [ ] fault tolerance
- [ ] security fundamentals

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **arjancodes – building production-ready fastapi & ai services in python:** [youtube kanalı](https://www.youtube.com/@ArjanCodes) — temiz mimari ile ai modellerini rest api olarak dış dünyaya açma
  2. **sebastián ramírez (tiangolo) – fastapi official talks & tutorials:** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=sebastian+ramirez+fastapi)
- **oku (resmi rehberler — önem sırasıyla):**
  1. **fastapi official tutorial – user guide:** [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/) — **[en iyi resmi dokümantasyonlardan biri]** birkaç saat içinde asenkron, tip güvenli (pydantic) ve otomatik swagger dokümanlı ai api servisi yazmayı öğren
  2. **full stack deep learning – deployment & monitoring lectures:** [fullstackdeeplearning.com/course/2022](https://fullstackdeeplearning.com/course/2022/)

---

### 03. software architecture & large-scale engineering

#### 18.1 backend engineering

- [ ] http / https
- [ ] rest apis
- [ ] authentication (jwt, oauth)
- [ ] authorization
- [ ] database integration (orm vs raw sql)
- [ ] asynchronous programming
- [ ] message queues (rabbitmq, redis pub/sub)
- [ ] caching (redis)
- [ ] api design
- [ ] microservices

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bora kaşmer – sistem mimarisi, redis, kafka, rabbitmq ve yüksek trafikli backend tasarımı:** [youtube kanalı](https://www.youtube.com/@BoraKasmer) — dağıtık mesaj kuyrukları, önbellekleme ve gerçek dünya backend mimarisi
  2. **gençay yıldız – mikroservis mimarileri, rabbitmq ve api tasarımı:** [youtube kanalı & listeler](https://www.youtube.com/@GencayYildiz/playlists)
  3. **kablosuz kedi – backend mimarisi serileri:** [youtube kanalı](https://www.youtube.com/@kablosuzkedi)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **hussein nasser – backend engineering (http/2, http/3, grpc, websockets, postgres, redis & proxies):** [youtube kanalı](https://www.youtube.com/@hnasr) — **[ilk izlenecek]** arka uç protokollerinin ve veritabanı motorlarının kaputun altında nasıl çalıştığını anlatan en derin kanal
- **oku (yol haritası):**
  1. **backend developer roadmap:** [roadmap.sh/backend](https://roadmap.sh/backend) — adım adım kavramsal başvuru haritası

#### 18.2 system design

- [ ] scalability
- [ ] reliability
- [ ] availability
- [ ] fault tolerance
- [ ] distributed systems
- [ ] load balancing
- [ ] replication
- [ ] partitioning (sharding)
- [ ] consistency (cap teoremi)
- [ ] event-driven architecture
- [ ] distributed messaging

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **bora kaşmer – dağıtık sistemler ve yüksek trafikli mimari tasarımı:** [youtube kanalı](https://www.youtube.com/@BoraKasmer)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **bytebytego (alex xu) – visual system design explanations:** [youtube kanalı](https://www.youtube.com/@ByteByteGo) — **[ilk izlenecek]** load balancing, sharding, cap teoremi, rate limiting ve event-driven mimarilerin 10 dakikalık animasyonlu özetleri
  2. **gaurav sen – system design series:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX) — sıfırdan ölçeklenebilir sistem tasarımı temelleri
- **oku & repo (mülakat ve mimari başucu kaynakları — önem sırasıyla):**
  1. **repo – donnemartin/system-design-primer (github'ın en çok yıldız alan mühendislik repolarından biri):** [github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) — **[ücretsiz tam rehber]** büyük ölçekli sistemlerin nasıl tasarlandığını diyagramlarla anlatan açık kaynak rehber (türkçe çevirisi de repoda mevcut!)
  2. **system design interview – an insider's guide, vol. 1 & vol. 2 (alex xu):** [bytebytego.com](https://bytebytego.com/) — global teknoloji şirketlerinin sistem tasarımı mülakatları için standart kitap

#### 18.3 advanced software engineering

- [ ] design by contract
- [ ] dependency injection
- [ ] domain-driven design (ddd)
- [ ] event sourcing
- [ ] observability
- [ ] performance profiling
- [ ] memory-safe design
- [ ] secure coding
- [ ] large codebase management

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **gençay yıldız – yazılım mimarisi, design patterns, solid ve kurumsal mimari yaklaşımlar:** [youtube kanalı](https://www.youtube.com/@GencayYildiz)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **cppcon – large scale c++ software architecture & memory-safe design talks (john lakos, herb sutter, klaus iglberger):** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=cppcon+software+architecture+klaus+iglberger) — **[ilk izlenecek]** büyük c++ kod tabanlarında bağımlılık yönetimi ve modern tasarım desenleri
- **oku (her kıdemli mühendisin okuduğu 2 kitap — önem sırasıyla):**
  1. **a philosophy of software design (prof. john ousterhout – stanford):** [konuşma videosu (talks at google)](https://www.youtube.com/watch?v=bmSAYlu0NcY) & [kitap sayfası](https://web.stanford.edu/~ouster/cgi-bin/book.php) — **[mutlaka oku / izle]** karmaşıklığı (complexity) yönetme, derin modüller (deep modules) tasarlama ve soyutlama üzerine yazılmış en iyi kısa kitap
  2. **patterns of enterprise application architecture (martin fowler):** [martinfowler.com/eaacatalog](https://martinfowler.com/eaaCatalog/) — kurumsal yazılım mimarisi katalog referansı
