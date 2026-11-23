# programming and high-performance computing

systems programming, modern c++, scientific python, gpu cuda kernels, machine learning compilers, and hardware acceleration.

---

## tracks

### [modern c++](./cpp/)

foundations, memory architecture, object-oriented design, and systems engineering in modern c++:

1. **[01-variables-data-types-operators](./cpp/01-variables-data-types-operators/)**: fundamental types, byte layouts, type casting, arithmetic, standard i/o streams, and iomanip formatting.
2. **[02-conditions](./cpp/02-conditions/)**: relational operators, boolean logic, short-circuit evaluation, if-else chains, and switch-case jump tables.
3. **[03-loops](./cpp/03-loops/)**: `while`, `do-while`, `for` loops, state trace tables, loop counters, break/continue flow control, and nested loops.
4. **[04-strings](./cpp/04-strings/)**: `char` primitives, `std::string` container, memory indexing, iteration patterns, and `getline` stream reading.

---

## complete checklist and resources

### 01. programming languages – programlama dilleri

#### 4.1 python

**temel python:**

- [ ] variables and data types
- [ ] strings
- [ ] lists
- [ ] tuples
- [ ] sets
- [ ] dictionaries
- [ ] conditions
- [ ] loops
- [ ] functions
- [ ] modules
- [ ] packages
- [ ] file handling
- [ ] exception handling
- [ ] comprehensions

**ileri python:**

- [ ] object-oriented programming (oop)
- [ ] inheritance
- [ ] polymorphism
- [ ] decorators
- [ ] generators
- [ ] iterators
- [ ] context managers
- [ ] type hints
- [ ] asyncio
- [ ] multithreading
- [ ] multiprocessing
- [ ] memory management
- [ ] python internals (gil)
- [ ] profiling
- [ ] packaging

**python ekosistemi:**

- [ ] **numpy** — sayısal hesaplama
- [ ] **scipy** — bilimsel hesaplama
- [ ] **pandas** — veri işleme
- [ ] **matplotlib** — görselleştirme
- [ ] **opencv** — görüntü işleme
- [ ] **sympy** — sembolik matematik
- [ ] **scikit-learn** — klasik ml
- [ ] **pytorch** — deep learning
- [ ] **jax** — yüksek performanslı sayısal hesaplama ve ml
- [ ] **tensorboard** — eğitim takibi
- [ ] **fastapi** — ai servisleri geliştirme

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **yazılım bilimi (mustafa murat coşkun) – sıfırdan ileri seviye python:** [youtube kanalı](https://www.youtube.com/@YazilimBilimi) — temel python sözdizimi ve oop tekrarı için
  2. **murat karakaya akademi – python ve makine öğrenmesi:** [youtube kanalı](https://www.youtube.com/@MuratKarakayaAkademi) — veri yapıları ve bilimsel python uygulamaları
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **harvard cs50p – introduction to programming with python (david j. malan):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V) — **[ilk izlenecek]** temel bilgileri eksiksiz ve temiz kod disipliniyle oturtmak için
  2. **corey schafer – python oop & advanced tutorials:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **[ana pratik kaynak]** oop, decorators, generators, threading/multiprocessing
  3. **mcoding (james murphy) – advanced python & internals:** [youtube kanalı](https://www.youtube.com/@mCoding) — **[ileri seviye]** python'un c altında nasıl çalıştığı, gil, asyncio, bellek optimizasyonu ve hızlandırma teknikleri
  4. **arjancodes – python software engineering & type hints:** [youtube kanalı](https://www.youtube.com/@ArjanCodes) — üretim seviyesi (production-ready) python mimarisi
- **📖 oku (resmi doküman ve kitaplar — önem sırasıyla):**
  1. **numpy: the absolute basics for beginners:** [numpy.org/doc/stable/user/absolute_beginners.html](https://numpy.org/doc/stable/user/absolute_beginners.html) — vektörizasyon ve `ndarray` mantığı (for döngüsü yerine matris işlemleri yazmak için şart)
  2. **python scientific lecture notes (scipy lectures):** [scipy-lectures.org](https://scipy-lectures.org/) — numpy, scipy ve matplotlib'in mühendisler için ücretsiz tam rehberi
  3. **official python 3 tutorial:** [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) — dil referansı
  4. **fluent python (luciano ramalho, 2nd ed.):** [fluentpython.com](https://www.fluentpython.com/) — python'da ileri seviye dil mekaniklerini öğrenmek için temel referans kitap
  5. **real python tutorials:** [realpython.com](https://realpython.com/) — uygulamalı derinlemesine makaleler

#### 4.2 c++

**c++ fundamentals:**

- [x] variables
- [x] data types
- [x] operators
- [x] conditions
- [x] loops
- [ ] functions
- [ ] arrays
- [x] strings
- [ ] pointers
- [ ] references
- [ ] structs
- [ ] enums
- [ ] classes
- [ ] objects

**object-oriented programming:**

- [ ] encapsulation
- [ ] abstraction
- [ ] inheritance
- [ ] polymorphism
- [ ] constructors
- [ ] destructors
- [ ] virtual functions
- [ ] abstract classes
- [ ] composition

**modern c++:**

- [ ] c++11
- [ ] c++14
- [ ] c++17
- [ ] c++20
- [ ] c++23
- [ ] auto
- [ ] lambda expressions
- [ ] move semantics
- [ ] rvalue references
- [ ] smart pointers (`unique_ptr`, `shared_ptr`, `weak_ptr`)
- [ ] raii
- [ ] `constexpr`
- [ ] concepts
- [ ] ranges
- [ ] modules

**stl – standard template library:**

- [ ] `std::vector`
- [ ] `std::array`
- [ ] `std::string`
- [ ] `std::map`
- [ ] `std::unordered_map`
- [ ] `std::set`
- [ ] `std::unordered_set`
- [ ] `std::queue`
- [ ] `std::stack`
- [ ] `std::priority_queue`
- [ ] `std::algorithm`
- [ ] iterators

**advanced c++:**

- [ ] templates
- [ ] template metaprogramming
- [ ] variadic templates
- [ ] generic programming
- [ ] memory alignment
- [ ] memory allocation
- [ ] stack vs heap
- [ ] custom allocators
- [ ] exception safety
- [ ] undefined behavior
- [ ] abi (application binary interface)
- [ ] linkers
- [ ] build systems
- [ ] cmake

**concurrency & parallelism:**

- [ ] threads (`std::jthread`)
- [ ] mutexes
- [ ] locks
- [ ] condition variables
- [ ] atomic operations
- [ ] futures
- [ ] promises
- [ ] thread pools
- [ ] race conditions
- [ ] deadlocks
- [ ] lock-free programming

**high performance c++:**

- [ ] profiling (`gprof`, `valgrind`, `perf`)
- [ ] cache optimization
- [ ] simd (simd intrinsics)
- [ ] memory optimization
- [ ] cpu optimization
- [ ] parallel algorithms
- [ ] compiler optimization (compiler optimization flags)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **necati ergin – c++ programlama dili kitabı ve topluluk ders notları:** [leanpub türkçe kitap (leanpub.com/cppofplepa)](https://leanpub.com/cppofplepa) · [necati ergin github](https://github.com/necatiergin) · [topluluk c++ ders notları (mguludag/csd_cpp_notlari)](https://github.com/mguludag/csd_cpp_notlari) — standartlara (iso c++) uyumlu, kapsamlı türkçe c++ kaynağı
  2. **kitap:** şadi evren şeker – başlangıç düzeyinde c++ öğrenimine giriş
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **the cherno – c++ complete series:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb) — **[ilk izlenecek – zorunlu]** pointers, references, stack vs heap, smart pointers, move semantics ve bellek düzenini bir oyun motoru mühendisinin gözünden anlatan kapsamlı seri
  2. **cyrill stachniss & ignacio vizzo – modern c++ course for computer vision & robotics (bonn üni):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRM59sr3nSL8BmeMZR9GCIA) — **[robotik & cv odaklı c++]** doğrudan cmake, opencv, eigen, stl ve modern c++17'yi robotik mühendisliği için anlatan üniversite dersi
  3. **c++ weekly with jason turner:** [youtube kanalı](https://www.youtube.com/@cppweekly) — modern c++20/23, `constexpr` ve sıfır maliyetli soyutlamalar
  4. **cppcon (the c++ conference):** [youtube kanalı](https://www.youtube.com/@CppCon) — c++ uzmanlarının performans, eşzamanlılık (concurrency) ve mimari sunumları
- **📖 oku & 💻 araçlar (rehber, kitap ve derleyici araçları — önem sırasıyla):**
  1. [**learncpp.com**](https://www.learncpp.com/)**(baştan sona ücretsiz modern c++ müfredatı):** [learncpp.com](https://www.learncpp.com/) — **[temel yazılı eğitim sitesi]** okuldaki müfredatı beklemeden adım adım okuyup kodlayacağın, c++20/23 güncel interaktif rehber
  2. **an introduction to modern cmake:** [cliutils.gitlab.io/modern-cmake](https://cliutils.gitlab.io/modern-cmake/) — büyük c++, opencv ve ros 2 projelerini derlemek için zorunlu cmake rehberi
  3. **compiler explorer (godbolt):** [godbolt.org](https://godbolt.org/) — yazdığın c++ kodunun hangi assembly/simd komutlarına dönüştüğünü canlı inceleme aracı
  4. **c++ reference (resmi dokümantasyon):** [en.cppreference.com](https://en.cppreference.com/w/) — stl kapsayıcıları ve algoritmaları için teknik sözlük
  5. **c++ core guidelines:** [isocpp.github.io/cppcoreguidelines/cppcoreguidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) — güvenli ve modern c++ yazım kuralları
  6. **effective modern c++ (scott meyers) & c++ concurrency in action (anthony williams):** smart pointers, rvalue/move semantics ve multithreading için endüstri başucu kitapları

#### 4.3 diğer diller

- [ ] **c:** embedded systems ve düşük seviyeli yazılım (düşük seviyeli donanım sürücüleri)
- [ ] **rust:** memory safety ve sistem programlama
- [ ] **cuda c++:** gpu programlama (gpu çekirdek programlama ve tensör hesaplama hızlandırma)
- [ ] **matlab:** matematiksel modelleme ve kontrol (kontrol modelleme)
- [ ] **julia:** bilimsel hesaplama
- [ ] **sql:** veri tabanları (ilişkisel veri tabanı sorgulama)
- [ ] **bash:** linux otomasyonu (kabuk otomasyonu ve betikleme)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **coşkun taşdemir – gömülü sistemler ve c programlama:** [github profili (ctasdemir)](https://github.com/ctasdemir) — mikrodenetleyici seviyesinde c dili ve gömülü yazılım örnekleri
  2. **fehmi uyar (@fehmiuyarnet):** [youtube kanalı](https://www.youtube.com/@fehmiuyarnet) — genel programlama eğitimleri
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **mit – the missing semester (shell tools and scripting):** [youtube ders videosu](https://www.youtube.com/watch?v=Z56Jmr9Z34Q) — **[ilk izlenecek]** bash otomasyonu ve komut satırı araçları
  2. **coffeebeforearch – cuda crash course (c++ gpu programming):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLxNPSjHT5qvtYRVdNN1yDcdSl39uHV_sU) — **[gpu hızlandırma]** c++ ile cuda çekirdekleri (kernels) yazmaya giriş
  3. **gpu mode – cuda & parallel programming lectures:** [youtube kanalı](https://www.youtube.com/@GPUMODE) — derin öğrenme ve tensör hızlandırma için modern gpu programlama topluluğu
  4. **matlab tech talks (control & simulation):** [youtube kanalı](https://www.youtube.com/@MATLAB) — kontrol teorisi, kalman filtresi ve sensör füzyonu modelleme
  5. **jon gjengset – crust of rust (intermediate/advanced rust):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLqbS7AVVErFiWDOAVrPt7aYmnuuOLYvOa) — bellek güvenli sistem programlama
- **📖 oku & 💻 interaktif eğitim (önem sırasıyla):**
  1. **linux journey & wooledge bash guide:** [linuxjourney.com](https://linuxjourney.com/) · [mywiki.wooledge.org/bashguide](https://mywiki.wooledge.org/BashGuide) — linux ve bash betikleme el kitabı
  2. **sqlbolt (interactive sql lessons):** [sqlbolt.com](https://sqlbolt.com/) — tarayıcı üzerinde 2 saatte pratik sql öğrenimi
  3. **matlab onramp (ücretsiz resmi eğitim):** [matlabacademy.mathworks.com](https://matlabacademy.mathworks.com/) — 2 saatlik etkileşimli matlab simülasyon girişi
  4. **programming massively parallel processors (hwu, kirk, el hajj):** [kitap sayfası](https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) — cuda c++ için temel akademik ders kitabı
  5. **the rust programming language (official book):** [doc.rust-lang.org/book](https://doc.rust-lang.org/book/) — resmi ücretsiz rust kitabı

---

### 02. ai systems, gpu programming & performance engineering

#### 14.1 gpu computing

- [ ] cpu vs gpu
- [ ] gpu architecture
- [ ] parallel computing
- [ ] cuda programming
- [ ] cuda kernels
- [ ] memory hierarchy (global, shared, constant, registers)
- [ ] shared memory
- [ ] global memory
- [ ] thread blocks
- [ ] warps (warp divergence)
- [ ] synchronization
- [ ] streams
- [ ] kernel optimization

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **coffeebeforearch – cuda crash course (c++ gpu programming):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLxNPSjHT5qvtYRVdNN1yDcdSl39uHV_sU) — **[ilk izlenecek]** vektör toplamadan shared memory tiling ve matris çarpımına kadar c++ ile cuda çekirdekleri (kernels) yazma
  2. **gpu mode – lectures on cuda, triton & parallel computing:** [youtube kanalı](https://www.youtube.com/@GPUMODE) & [github (gpu-mode/lectures)](https://github.com/gpu-mode/lectures) — **[dünyanın en iyi gpu mühendisliği topluluğu]** pytorch ve nvidia mühendislerinin verdiği ileri seviye gpu optimizasyon dersleri
- **📖 oku (kutsal kitap ve resmi kılavuz — önem sırasıyla):**
  1. **programming massively parallel processors – pmpp, 4th ed. (wen-mei hwu, david kirk, izzat el hajj):** [kitap sayfası](https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) — **[her gpu mühendisinin başucu kitabı]** thread blocks, warps, shared memory, coalesced memory access ve paralel indirgeme (reduction) algoritmaları
  2. **nvidia cuda c++ programming guide:** [docs.nvidia.com/cuda/cuda-c-programming-guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html) — resmi başvuru dokümanı

#### 14.2 ai performance optimization

- [ ] model profiling (nsight systems, nsight compute, pytorch profiler)
- [ ] inference optimization
- [ ] quantization (ptq, qat)
- [ ] pruning (structured, unstructured)
- [ ] knowledge distillation
- [ ] mixed precision
- [ ] operator fusion
- [ ] memory optimization
- [ ] batch optimization
- [ ] kernel fusion (flashattention)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **mit 6.5940 – tinyml and efficient deep learning computing (prof. song han):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) — **[ilk izlenecek]** ptq/qat quantization, pruning, distillation ve donanım-farkındalıklı (hardware-aware) optimizasyon
  2. **tri dao – flashattention & io-aware gpu kernels (gpu mode lecture):** [youtube sunumu](https://www.youtube.com/watch?v=VPslgC9piIw) — gpu hbm ve sram bellek bant genişliği darboğazını kernel fusion ile aşma
- **📖 oku & 💻 repo (zorunlu mühendislik yazıları ve kodlar — önem sırasıyla):**
  1. **making deep learning go brrrr from first principles (horace he – pytorch ekibi):** [horace.io/brrr_intro.html](https://horace.io/brrr_intro.html) — **[temel mühendislik yazısı]** compute-bound, memory-bandwidth bound ve overhead-bound darboğazlarını ve operator fusion mantığını anlatan makale
  2. **flashattention: fast and memory-efficient exact attention with io-awareness (tri dao et al.):** [arxiv:2205.14135](https://arxiv.org/abs/2205.14135) — modern gpu çekirdek optimizasyonunun referans makalesi
  3. **repo – ggerganov/llama.cpp (`ggml`tensor library):** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) — saf c/c++ ile int4/int8 nicemleme (quantization) ve simd/cuda matris çarpımı kodları

#### 14.3 ai deployment

- [ ] onnx (open neural network exchange)
- [ ] onnx runtime
- [ ] nvidia tensorrt
- [ ] torchscript
- [ ] model serving (triton inference server, torchserve)
- [ ] inference pipelines
- [ ] batch inference
- [ ] real-time inference
- [ ] edge deployment
- [ ] model monitoring

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **nvidia developer – tensorrt & triton inference server walkthroughs:** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=nvidia+developer+tensorrt+c%2B%2B+tutorial) — pytorch modelini onnx üzerinden tensorrt motoruna (`.engine`) dönüştürme
  2. **jetsonhacks – edge ai deployment on nvidia jetson:** [youtube kanalı](https://www.youtube.com/@JetsonHacks) — gömülü gpu üzerinde gerçek zamanlı kamera ve çıkarım boru hattı kurma
- **📖 oku & 💻 repo (resmi doküman ve c++ dağıtım repoları — önem sırasıyla):**
  1. **onnx runtime official documentation (c++ & python api):** [onnxruntime.ai/docs](https://onnxruntime.ai/docs/) — modelleri python'dan bağımsız olarak c++ içinde çalıştırmanın en kolay yolu
  2. **nvidia tensorrt developer guide (c++ & python):** [docs.nvidia.com/deeplearning/tensorrt/developer-guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html) — nvidia gpu'larda en düşük gecikme (latency) ve en yüksek fps için resmi kılavuz
  3. **repo – wang-xinyu/tensorrtx:** [github.com/wang-xinyu/tensorrtx](https://github.com/wang-xinyu/tensorrtx) — **[c++ tensorrt uygulama reposu]** yolov8/v11, resnet, detr vb. modellerin saf c++ tensorrt api'si ile nasıl yazıldığını gösteren açık kaynak repo
  4. **repo – dusty-nv/jetson-inference:** [github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference) — c++ ve tensorrt ile gerçek zamanlı görüntü işleme ve algılama şablonları

#### 14.4 distributed ai

- [ ] distributed training
- [ ] data parallelism (ddp - distributed data parallel)
- [ ] model parallelism
- [ ] pipeline parallelism
- [ ] tensor parallelism (megatron-lm)
- [ ] distributed data loading
- [ ] gradient synchronization (allreduce)
- [ ] distributed inference (vllm, deepinfer, tensorrt-llm)
- [ ] expert parallelism (deepep, moe all-to-all)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **pytorch official – distributed data parallel (ddp) tutorial series:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL_lsbAsL_o2CSuhUhJIiW0IkdT5C2wGWj) — **[ilk izlenecek]** tek gpu'dan çoklu gpu eğitimine (multi-gpu ddp) geçişin resmi adım adım rehberi
  2. **tim dettmers – distributed training & 8-bit/4-bit parallelism lectures:** [youtube kanalı & konuşmaları](https://www.youtube.com/results?search_query=tim+dettmers+distributed+training) — büyük modellerde bellek ve iletişim darboğazları (allreduce)
- **📖 oku & 💻 repo (doküman ve kodlar — önem sırasıyla):**
  1. **pytorch distributed overview & ddp tutorial:** [pytorch.org/tutorials/beginner/dist_overview.html](https://pytorch.org/tutorials/beginner/dist_overview.html) — data parallelism, fsdp ve tensor parallelism resmi dokümanı
  2. **the ultra-scale playbook: training llms on gpu clusters (hugging face):** [huggingface.co/spaces/nanotron/ultrascale-playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — data, tensor, pipeline ve context parallelism kavramlarının etkileşimli görsel kitabı
  3. **dağıtık çıkarım motorları (distributed inference) – vllm & deepinfer:** [vllm (github)](https://github.com/vllm-project/vllm) & [deepseek-ai/deepinfer](https://github.com/deepseek-ai/DeepInfer) — vllm (endüstri standardı pagedattention çıkarım motoru) ve deepinfer (deepseek'in flashmla, deepgemm ve deepep entegre 26k yıldızlı büyük ölçekli üretim çıkarım altyapısı)
  4. **repo – deepseek-ai/deepep (yüksek başarımlı moe iletişim kütüphanesi):** [github.com/deepseek-ai/deepep](https://github.com/deepseek-ai/DeepEP) — **[moe & uzman paralelliği gpu çekirdekleri]** deepseek-v3 ve r1 mimarilerinde kullanılan; fp8 veri aktarımı, nvlink doğrudan ağırlık değişimi ve moe all-to-all gpu çekirdekleriyle dağıtık eğitim/çıkarım iletişim darboğazını kıran yüksek performanslı kütüphane

---

### 03. ml compilers & ai hardware – ml derleyicileri ve yapay zekâ donanımları

#### 41.1 ml compilers – makine öğrenmesi derleyicileri

- [ ] computation graphs
- [ ] graph-level optimizations
- [ ] operator fusion and lowering
- [ ] llvm
- [ ] mlir
- [ ] apache tvm
- [ ] xla
- [ ] torch.compile (dynamo, inductor)
- [ ] triton
- [ ] halide
- [ ] auto-tuning
- [ ] iree

#### 41.2 ai accelerators – yapay zekâ hızlandırıcıları

- [ ] tpu and systolic arrays
- [ ] npus
- [ ] edge accelerators (coral, hailo, qualcomm hexagon, apple neural engine)
- [ ] hbm and memory bandwidth
- [ ] interconnects (nvlink, infiniband)
- [ ] sparsity and low-precision hardware support (int4, fp8)
- [ ] dataflow architectures
- [ ] analog and in-memory computing
- [ ] power and thermal efficiency

#### 41.3 inference engines & runtimes – çıkarım motorları ve çalışma zamanları

- [ ] openvino
- [ ] tensorflow lite
- [ ] executorch
- [ ] core ml
- [ ] ncnn and mnn
- [ ] mlc-llm
- [ ] sglang
- [ ] tensorrt-llm
- [ ] deepspeed inference

#### 41.4 low-level performance engineering – düşük seviyeli performans mühendisliği

- [ ] roofline model
- [ ] arithmetic intensity
- [ ] memory-bound vs compute-bound kernels
- [ ] tiling and blocking
- [ ] tensor cores and wmma
- [ ] cutlass
- [ ] cublas and cudnn
- [ ] triton kernels
- [ ] nccl and collective communication
- [ ] nsight profiling

#### 41.5 fpga & digital design – fpga ve sayısal tasarım temelleri

- [ ] verilog / vhdl
- [ ] high-level synthesis (hls)
- [ ] vitis ai
- [ ] soc fpgas (zynq)
- [ ] real-time vision pipelines on fpga
- [ ] hardware/software co-design

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [mehmet burak aykenar — vhdl / fpga ve sayısal tasarım dersleri (youtube)](https://www.youtube.com/@MehmetBurakAykenar) — savunma ve gömülü görüntü işleme donanımlarında karşılaşılan fpga/zynq mimarisine türkçe giriş.
- ▶️ **yt:**
  1. **[ilk izlenecek — ml derleyicileri]** [tianqi chen — machine learning compilation (mlc.ai course)](https://mlc.ai/) — hesaplama grafları, operatör birleştirme (fusion), tvm ve donanım hızlandırma.
  2. **[verimli ai & donanım]** [mit 6.5940 — tinyml and efficient deep learning computing (song han — youtube)](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) — roofline modeli, aritmetik yoğunluk, nicemleme ve uç hızlandırıcılar.
- 📖 **oku & 💻 repo:**
  1. [horace he — making deep learning go brrrr from first principles (horace.io)](https://horace.io/brrr_intro.html) — bellek bant genişliği (memory-bound), hesaplama sınırı (compute-bound) ve operatör birleştirme mantığını en net anlatan mühendislik makalesi.
  2. [openai triton tutorials (triton-lang.org)](https://triton-lang.org/main/getting-started/tutorials/index.html) & [gpu mode lectures (github)](https://github.com/gpu-mode/lectures) — özel gpu çekirdekleri (kernels), `torch.compile`, cutlass ve nsight profilleme.
