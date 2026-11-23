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

### 01. programming languages

#### 4.1 python

**core python:**

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

**advanced python:**

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

**python ecosystem:**

- [ ] **numpy** — numerical computing
- [ ] **scipy** — bilimsel hesaplama
- [ ] **pandas** — data manipulation
- [ ] **matplotlib** — data visualization
- [ ] **opencv** — image processing
- [ ] **sympy** — sembolik matematik
- [ ] **scikit-learn** — klasik ml
- [ ] **pytorch** — deep learning
- [ ] **jax** — high-performance numerical computing and ml
- [ ] **tensorboard** — training tracking and visualization
- [ ] **fastapi** — building fast ai web apis

**resources:**

- **turkish resources:**
  1. **yazılım bilimi (mustafa murat coşkun) – python programming:** [youtube channel](https://www.youtube.com/@YazilimBilimi) — turkish course covering python basics and oop
  2. **murat karakaya academy – python & ml:** [youtube channel](https://www.youtube.com/@MuratKarakayaAkademi) — turkish lectures on data structures and scientific python
- **video lectures:**
  1. **harvard cs50p – introduction to programming with python (david j. malan):** [youtube playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V) — clean coding foundations in python
  2. **corey schafer – python oop & advanced tutorials:** [youtube playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — oop, decorators, generators, threading/multiprocessing
  3. **mcoding (james murphy) – advanced python & internals:** [youtube channel](https://www.youtube.com/@mCoding) — how python works under the hood: cpython, gil, asyncio, and speedup tips
  4. **arjancodes – python software engineering & type hints:** [youtube channel](https://www.youtube.com/@ArjanCodes) — production-ready python architecture and design
- **books, papers & repositories:**
  1. **numpy: the absolute basics for beginners:** [numpy.org/doc/stable/user/absolute_beginners.html](https://numpy.org/doc/stable/user/absolute_beginners.html) — vectorization and `ndarray` indexing instead of slow python loops
  2. **python scientific lecture notes (scipy lectures):** [scipy-lectures.org](https://scipy-lectures.org/) — free complete guide to numpy, scipy, and matplotlib
  3. **official python 3 tutorial:** [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) — official language reference
  4. **fluent python (luciano ramalho, 2nd ed.):** [fluentpython.com](https://www.fluentpython.com/) — deep guide to idiomatic and advanced python internals
  5. **real python tutorials:** [realpython.com](https://realpython.com/) — practical python guides and tutorials

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

**resources:**

- **turkish resources:**
  1. **necati ergin – c++ programming book & lecture notes:** [turkish book](https://leanpub.com/cppofplepa) · [github](https://github.com/necatiergin) · [community c++ notes](https://github.com/mguludag/csd_cpp_notlari) — thorough iso-compliant turkish c++ resources
  2. **book (turkish):** şadi evren şeker – introduction to c++ programming
- **video lectures:**
  1. **the cherno – c++ complete series:** [youtube playlist](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb) — pointers, stack vs heap, smart pointers, move semantics, and memory layout explained clearly
  2. **cyrill stachniss & ignacio vizzo – modern c++ for computer vision & robotics:** [youtube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRM59sr3nSL8BmeMZR9GCIA) — modern c++17, cmake, eigen, opencv, and stl taught specifically for robotics engineers
  3. **c++ weekly with jason turner:** [youtube channel](https://www.youtube.com/@cppweekly) — short episodes on modern c++20/23, `constexpr`, and zero-cost abstractions
  4. **cppcon (the c++ conference):** [youtube channel](https://www.youtube.com/@CppCon) — talks on c++ performance, concurrency, and software architecture
- **books, papers & repositories:**
  1. [**learncpp.com**](https://www.learncpp.com/) **(free modern c++ curriculum):** [learncpp.com](https://www.learncpp.com/) — complete step-by-step interactive guide covering modern c++20/23
  2. **an introduction to modern cmake:** [cliutils.gitlab.io/modern-cmake](https://cliutils.gitlab.io/modern-cmake/) — practical cmake guide for building large c++, opencv, and ros 2 projects
  3. **compiler explorer (godbolt):** [godbolt.org](https://godbolt.org/) — live tool to inspect assembly and simd instructions generated by c++ code
  4. **c++ reference:** [en.cppreference.com](https://en.cppreference.com/w/) — official standard library, stl containers, and language reference
  5. **c++ core guidelines:** [isocpp.github.io/cppcoreguidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) — rules and best practices for writing safe modern c++
  6. **effective modern c++ (scott meyers) & c++ concurrency in action (anthony williams):** essential reference books for smart pointers, move semantics, and multithreading

#### 4.3 other languages

- [ ] **c:** embedded systems and low-level hardware drivers
- [ ] **rust:** memory-safe systems programming
- [ ] **cuda c++:** gpu kernel programming and tensor acceleration
- [ ] **matlab:** mathematical modeling and control simulation
- [ ] **julia:** bilimsel hesaplama
- [ ] **sql:** relational database querying
- [ ] **bash:** linux shell scripting and automation

**resources:**

- **turkish resources:**
  1. **coşkun taşdemir – embedded systems & c programming:** [github profile (ctasdemir)](https://github.com/ctasdemir) — turkish microcontroller c programming notes and firmware examples
  2. **fehmi uyar (@fehmiuyarnet):** [youtube channel](https://www.youtube.com/@fehmiuyarnet) — general programming tutorials in turkish
- **video lectures:**
  1. **mit – the missing semester (shell tools & scripting):** [youtube lecture video](https://www.youtube.com/watch?v=Z56Jmr9Z34Q) — bash scripting and command-line tools
  2. **coffeebeforearch – cuda crash course (c++ gpu programming):** [youtube playlist](https://www.youtube.com/playlist?list=PLxNPSjHT5qvtYRVdNN1yDcdSl39uHV_sU) — introduction to writing cuda kernels in c++
  3. **gpu mode – cuda & parallel programming lectures:** [youtube channel](https://www.youtube.com/@GPUMODE) — practical community talks on gpu programming, triton, and tensor optimization
  4. **matlab tech talks (control & simulation):** [youtube channel](https://www.youtube.com/@MATLAB) — short clear talks on control theory, kalman filtering, and sensor fusion
  5. **jon gjengset – crust of rust:** [youtube playlist](https://www.youtube.com/playlist?list=PLqbS7AVVErFiWDOAVrPt7aYmnuuOLYvOa) — intermediate and advanced memory-safe systems programming in rust
- **books, papers & repositories:**
  1. **linux journey & wooledge bash guide:** [linuxjourney.com](https://linuxjourney.com/) · [mywiki.wooledge.org/bashguide](https://mywiki.wooledge.org/BashGuide) — practical guides for linux and bash scripting
  2. **sqlbolt (interactive sql lessons):** [sqlbolt.com](https://sqlbolt.com/) — quick interactive browser lessons to learn sql fundamentals
  3. **matlab onramp (free official course):** [matlabacademy.mathworks.com](https://matlabacademy.mathworks.com/) — 2-hour interactive intro to matlab simulation
  4. **programming massively parallel processors (hwu, kirk, el hajj):** [book page](https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) — core textbook for learning cuda c++ and gpu architecture
  5. **the rust programming language (official book):** [doc.rust-lang.org/book](https://doc.rust-lang.org/book/) — free official rust programming book

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

**resources:**

- **video lectures:**
  1. **coffeebeforearch – cuda crash course (c++ gpu programming):** [youtube playlist](https://www.youtube.com/playlist?list=PLxNPSjHT5qvtYRVdNN1yDcdSl39uHV_sU) — writing cuda kernels in c++ from vector addition to shared memory tiling and matrix multiplication
  2. **gpu mode – lectures on cuda, triton & parallel computing:** [youtube channel](https://www.youtube.com/@GPUMODE) & [github (gpu-mode/lectures)](https://github.com/gpu-mode/lectures) — practical gpu optimization talks by pytorch and nvidia engineers
- **books, papers & repositories:**
  1. **programming massively parallel processors – pmpp, 4th ed. (hwu, kirk, el hajj):** [book page](https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) — covers thread blocks, warps, shared memory, coalesced access, and parallel reduction
  2. **nvidia cuda c++ programming guide:** [docs.nvidia.com/cuda/cuda-c-programming-guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html) — official cuda c++ programming reference

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

**resources:**

- **video lectures:**
  1. **mit 6.5940 – tinyml and efficient deep learning computing (prof. song han):** [youtube lecture series](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) — ptq/qat quantization, pruning, distillation, and hardware-aware model optimization
  2. **tri dao – flashattention & io-aware gpu kernels (gpu mode):** [youtube talk](https://www.youtube.com/watch?v=VPslgC9piIw) — overcoming gpu memory bandwidth bottlenecks using kernel fusion
- **books, papers & repositories:**
  1. **making deep learning go brrrr from first principles (horace he):** [horace.io/brrr_intro.html](https://horace.io/brrr_intro.html) — clear explanation of compute-bound vs memory-bound bottlenecks and operator fusion
  2. **flashattention: fast and memory-efficient exact attention with io-awareness (tri dao et al.):** [arxiv:2205.14135](https://arxiv.org/abs/2205.14135) — core paper on io-aware gpu kernel optimization
  3. **ggerganov/llama.cpp (`ggml` tensor library):** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) — int4/int8 quantization and simd/cuda matrix multiplication in pure c/c++

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

**resources:**

- **video lectures:**
  1. **nvidia developer – tensorrt & triton inference server walkthroughs:** [youtube search](https://www.youtube.com/results?search_query=nvidia+developer+tensorrt+c%2B%2B+tutorial) — converting pytorch models via onnx to tensorrt `.engine` files
  2. **jetsonhacks – edge ai deployment on nvidia jetson:** [youtube channel](https://www.youtube.com/@JetsonHacks) — setting up real-time camera and inference pipelines on embedded nvidia jetson
- **books, papers & repositories:**
  1. **onnx runtime official documentation (c++ & python api):** [onnxruntime.ai/docs](https://onnxruntime.ai/docs/) — straightforward guide to running models in c++ without python
  2. **nvidia tensorrt developer guide (c++ & python):** [docs.nvidia.com/deeplearning/tensorrt/developer-guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html) — official guide for low-latency high-fps inference on nvidia gpus
  3. **wang-xinyu/tensorrtx:** [github.com/wang-xinyu/tensorrtx](https://github.com/wang-xinyu/tensorrtx) — open-source repo showing how to take models like yolov8/v11, resnet, and detr from pytorch and write them from scratch using the pure c++ tensorrt api
  4. **dusty-nv/jetson-inference:** [github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference) — real-time computer vision and inference templates using c++ and tensorrt

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

**resources:**

- **video lectures:**
  1. **pytorch official – distributed data parallel (ddp) series:** [youtube playlist](https://www.youtube.com/playlist?list=PL_lsbAsL_o2CSuhUhJIiW0IkdT5C2wGWj) — step-by-step official guide for scaling from single-gpu to multi-gpu training
  2. **tim dettmers – distributed training & 8-bit/4-bit parallelism:** [youtube search](https://www.youtube.com/results?search_query=tim+dettmers+distributed+training) — memory and communication bottlenecks (allreduce) in large-scale training
- **books, papers & repositories:**
  1. **pytorch distributed overview & ddp tutorial:** [pytorch.org/tutorials/beginner/dist_overview.html](https://pytorch.org/tutorials/beginner/dist_overview.html) — official docs for data parallelism, fsdp, and tensor parallelism
  2. **the ultra-scale playbook: training llms on gpu clusters (hugging face):** [huggingface.co/spaces/nanotron/ultrascale-playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — visual handbook covering data, tensor, pipeline, and context parallelism
  3. **distributed inference engines – vllm & deepinfer:** [vllm (github)](https://github.com/vllm-project/vllm) & [deepseek-ai/deepinfer](https://github.com/deepseek-ai/DeepInfer) — high-throughput llm serving engines using pagedattention, flashmla, and deepgemm
  4. **deepseek-ai/deepep (moe communication library):** [github.com/deepseek-ai/deepep](https://github.com/deepseek-ai/DeepEP) — gpu kernels for fp8 transfer, nvlink routing, and moe all-to-all communication

---

### 03. ml compilers & ai hardware

#### 41.1 ml compilers

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

#### 41.2 ai accelerators

- [ ] tpu and systolic arrays
- [ ] npus
- [ ] edge accelerators (coral, hailo, qualcomm hexagon, apple neural engine)
- [ ] hbm and memory bandwidth
- [ ] interconnects (nvlink, infiniband)
- [ ] sparsity and low-precision hardware support (int4, fp8)
- [ ] dataflow architectures
- [ ] analog and in-memory computing
- [ ] power and thermal efficiency

#### 41.3 inference engines & runtimes

- [ ] openvino
- [ ] tensorflow lite
- [ ] executorch
- [ ] core ml
- [ ] ncnn and mnn
- [ ] mlc-llm
- [ ] sglang
- [ ] tensorrt-llm
- [ ] deepspeed inference

#### 41.4 low-level performance engineering

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

#### 41.5 fpga & digital design

- [ ] verilog / vhdl
- [ ] high-level synthesis (hls)
- [ ] vitis ai
- [ ] soc fpgas (zynq)
- [ ] real-time vision pipelines on fpga
- [ ] hardware/software co-design

**resources:**

- **turkish resource:** [mehmet burak aykenar — vhdl / fpga & digital design lectures (youtube)](https://www.youtube.com/@MehmetBurakAykenar) — turkish introduction to fpga and zynq hardware design for embedded vision
- **video lectures:**
  1. **ml compilers:** [tianqi chen — machine learning compilation (mlc.ai course)](https://mlc.ai/) — computation graphs, operator fusion, tvm, and hardware acceleration
  2. [mit 6.5940 — tinyml and efficient deep learning computing (song han — youtube)](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) — roofline model, arithmetic intensity, quantization, and edge accelerators
- **books, papers & repositories:**
  1. [horace he — making deep learning go brrrr from first principles (horace.io)](https://horace.io/brrr_intro.html) — straightforward engineering article on memory-bound vs compute-bound kernels and operator fusion
  2. [openai triton tutorials (triton-lang.org)](https://triton-lang.org/main/getting-started/tutorials/index.html) & [gpu mode lectures (github)](https://github.com/gpu-mode/lectures) — custom gpu kernels, `torch.compile`, cutlass, and nsight profiling
