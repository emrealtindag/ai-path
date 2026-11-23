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

### 01. computer science

#### 3.1 data structures

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

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları (şadi evren şeker) – data structures:** [youtube playlist](https://www.youtube.com/playlist?list=PLh9ECzBB8tJN9bckI6FbWB03HkmogKrFT) — turkish lectures covering linked lists, trees, stacks, and hash tables
  2. **book (turkish):** şadi evren şeker – algorithms (nobel akademik yayıncılık, 2021)
- **video lectures:**
  1. **cs50x – harvard introduction to computer science (david j. malan):** [youtube lecture series](https://www.youtube.com/playlist?list=PLhQjrBD2T381WAHyx1pq-sBfykqMBI7V4) — beginner-friendly lectures on memory, pointers, and core data structures
  2. **william fiset – data structures easy to advanced course:** [freecodecamp full video](https://www.youtube.com/watch?v=RBSGKlAvoiM) — animated code walkthroughs from dynamic arrays to fenwick trees and union-find
- **books, papers & repositories:**
  1. **visualgo (national university of singapore):** [visualgo.net/en](https://visualgo.net/en) — step-by-step animations of bst, avl trees, heaps, and graph structures
  2. **c++ stl containers reference:** [en.cppreference.com/w/cpp/container](https://en.cppreference.com/w/cpp/container) — official reference for `std::vector`, `std::unordered_map`, `std::priority_queue`, and stl internals
  3. **open data structures (in c++):** [opendatastructures.org/ods-cpp.pdf](https://opendatastructures.org/ods-cpp.pdf) — open-source textbook with full c++ implementations

#### 3.2 algorithms

**core algorithms:**

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

**advanced topics:**

- [ ] computational geometry
- [ ] approximation algorithms
- [ ] online algorithms
- [ ] parallel algorithms
- [ ] optimization algorithms

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları – algorithm analysis:** [youtube playlist](https://www.youtube.com/playlist?list=PLh9ECzBB8tJPTWIUbZjHZMMGuZcpHUv5h) — turkish lectures on big-o complexity, sorting, searching, and dynamic programming
  2. **book (turkish):** şadi evren şeker – algorithms
- **video lectures:**
  1. **abdul bari – algorithms course:** [youtube playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O) — whiteboard explanations of divide & conquer, greedy algorithms, dp, and backtracking
  2. **mit 6.006 introduction to algorithms (erik demaine & srini devadas):** [youtube lecture series](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb) — mit course on algorithm analysis, dijkstra, and dynamic programming
  3. **william fiset – graph theory & shortest path algorithms:** [youtube playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P) — bfs, dfs, dijkstra, a*, and minimum spanning tree algorithms used in path planning
  4. **neetcode – roadmap & solutions:** [youtube channel](https://www.youtube.com/@NeetCode) — coding interview strategies and algorithm walkthroughs
- **books, papers & repositories:**
  1. **neetcode 150 (practice list):** [neetcode.io/practice](https://neetcode.io/practice) — 150 core algorithm problems grouped by topic to solve in c++ and python
  2. **cp-algorithms:** [cp-algorithms.com](https://cp-algorithms.com/) — c++ implementations for graph, geometry, and data structure algorithms
  3. **algorithms (jeff erickson – uiuc):** [jeffe.cs.illinois.edu/teaching/algorithms/book/algorithms-jeffe.pdf](https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf) — free, clear algorithms textbook
  4. **algorithms, 4th edition (sedgewick & wayne – princeton):** [algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/home/) — visual and practical algorithms reference
  5. **kdn251/interviews:** [github.com/kdn251/interviews](https://github.com/kdn251/interviews) — open-source guide to data structures, search/sort algorithms, and interview patterns

#### 3.3 computer architecture

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
- [ ] cpu-gpu communication (pcie bandwidth)
- [ ] cache coherence

**resources:**

- **turkish resources:**
  1. **prof. dr. oğuz ergin – computer architecture (bilgisayar mimarisi):** [youtube playlist](https://www.youtube.com/playlist?list=PLvNq8wrSYGAU6CF4UleG6HbXa9paQDsLK) — turkish lectures on cpus, caches, pipelines, and memory hierarchy
  2. **prof. dr. onur mutlu – turkish talks & seminars:** [youtube search](https://www.youtube.com/results?search_query=onur+mutlu+t%C3%BCrk%C3%A7e) — turkish seminars on memory systems and modern cpu/gpu architectures
- **video lectures:**
  1. **prof. dr. onur mutlu – digital design and computer architecture (eth zürich):** [youtube lecture series](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi_uej3aY39YB5pfW4SJ7LlN) — university lectures on cpu/gpu architecture, caches, simd, and memory systems
  2. **ben eater – build an 8-bit computer from scratch:** [youtube playlist](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) — see how registers, alu, buses, and machine instructions work in physical hardware
  3. **uc berkeley cs61c – great ideas in computer architecture:** [course page](https://cs61c.org/) — c, risc-v, simd vectorization, and cache optimization
- **books, papers & repositories:**
  1. **from nand to tetris (building a modern computer from first principles):** [nand2tetris.org](https://www.nand2tetris.org/) — build a cpu, assembler, and compiler from logic gates
  2. **what every programmer should know about memory (ulrich drepper):** [free pdf](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) — essential guide on l1/l2/l3 caches, virtual memory, and writing cache-friendly c++ code
  3. **agner fog’s software optimization resources:** [agner.org/optimize](https://www.agner.org/optimize/) — practical c++ and simd/avx optimization manuals
  4. **computer organization and design (patterson & hennessy):** [book page](https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6) — standard computer architecture textbook

#### 3.4 operating systems

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

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları – operating systems:** [youtube playlist](https://www.youtube.com/playlist?list=PLh9ECzBB8tJO9eiwfQbcA2ThMbUSkbOWf) — turkish lectures on processes, threads, deadlocks, semaphores, and mutexes
- **video lectures:**
  1. **neso academy – operating systems:** [youtube playlist](https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O) — clear visual tutorials on scheduling, paging, and concurrency
  2. **jacob sorber – systems programming in c/c++:** [youtube channel](https://www.youtube.com/@JacobSorber) — hands-on linux coding for `fork`, `pthread`, `mutex`, `mmap`, `ipc`, and sockets in c/c++
  3. **mit 6.s081 operating system engineering (xv6):** [youtube lecture series](https://www.youtube.com/playlist?list=PLTsf9UeqkReZHXWY9yJvTwLJWYYPcKEqK) — study a real unix-like os kernel from scratch
- **books, papers & repositories:**
  1. **operating systems: three easy pieces (ostep – remzi & andrea arpaci-dusseau):** [pages.cs.wisc.edu/~remzi/ostep](https://pages.cs.wisc.edu/~remzi/OSTEP/) — free textbook covering virtualization, concurrency, and persistence
  2. **beej’s guide to unix interprocess communication (ipc):** [beej.us/guide/bgipc](https://beej.us/guide/bgipc/) — practical guide to shared memory, pipes, and message queues
  3. **the linux programming interface (michael kerrisk):** [man7.org/tlpi](https://man7.org/tlpi/) — comprehensive reference for linux system calls and kernel programming

#### 3.5 computer networks

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

**resources:**

- **turkish resources:**
- **video lectures:**
  1. **jim kurose – computer networking: a top-down approach:** [youtube lecture series](https://www.youtube.com/playlist?list=PL1ya5dD_M8uX-BLUF1FEvUNsYWQL5_l0O) — networking protocols taught by the textbook author
  2. **hussein nasser – backend & networking fundamentals:** [youtube channel](https://www.youtube.com/@hnasr) — engineering deep dives into tcp, udp, websockets, and grpc
  3. **chris greer – wireshark & tcp/ip analysis:** [youtube channel](https://www.youtube.com/@ChrisGreer) — capturing and debugging network packets in real time
- **books, papers & repositories:**
  1. **beej’s guide to network programming:** [beej.us/guide/bgnet](https://beej.us/guide/bgnet/) — practical guide to tcp/udp socket programming in c/c++ for robot and uav telemetry
  2. **eprosima fast dds documentation:** [fast-dds.docs.eprosima.com](https://fast-dds.docs.eprosima.com/) — real-time data distribution service (dds) middleware powering ros 2
  3. **grpc official documentation (c++ & python):** [grpc.io/docs](https://grpc.io/docs/) — high-speed rpc communication between microservices and ai models
  4. **zeromq – the guide:** [zguide.zeromq.org](https://zguide.zeromq.org/) — lightweight message queue patterns for robotics and embedded systems

#### 3.6 software engineering

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

**resources:**

- **turkish resources:**
  1. **gençay yıldız – design patterns & solid:** [youtube playlists](https://www.youtube.com/@GencayYildiz/playlists) — turkish course on oop, solid principles, clean code, and design patterns
  2. **bora kaşmer – software & system architecture:** [youtube channel](https://www.youtube.com/@BoraKasmer) — turkish talks on real-world software engineering and architecture decisions
- **video lectures:**
  1. **mit – the missing semester of your cs education:** [youtube playlist](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J) & [course site](https://missing.csail.mit.edu/) — essential developer tools: git, shell, vim, gdb debugging, and profiling
  2. **arjancodes – software design in python:** [youtube channel](https://www.youtube.com/@ArjanCodes) — writing clean, modular, and testable python code
  3. **cppcon – back to basics track:** [youtube search](https://www.youtube.com/results?search_query=cppcon+back+to+basics) — modern c++ software design, memory management, and unit testing
- **books, papers & repositories:**
  1. [**refactoring.guru**](https://refactoring.guru/design-patterns) **(design patterns & clean code):** [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns) — visual guide to design patterns with c++ and python examples
  2. **pro git book (scott chacon & ben straub):** [git-scm.com/book/en/v2](https://git-scm.com/book/en/v2) · [turkish](https://git-scm.com/book/tr/v2) — free official git book
  3. **c++ core guidelines (bjarne stroustrup & herb sutter):** [isocpp.github.io/cppcoreguidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) — standard coding guidelines for safe modern c++
  4. **software engineering at google (titus winters et al.):** [abseil.io/resources/swe-book](https://abseil.io/resources/swe-book) — free book on large-scale engineering, code review, testing, and ci/cd

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

**resources:**

- **turkish resources:**
  1. **tübitak ulakbim / akademik bilişim – gnu/linux system administration:** [ab.org.tr](https://ab.org.tr/) — turkish open-source linux administration lecture notes
- **video lectures:**
  1. **learn linux tv – linux, systemd & ssh tutorials:** [youtube channel](https://www.youtube.com/@LearnLinuxTV) — writing `systemd` services for robots/uavs and managing ssh servers
  2. **networkchuck – linux for beginners series:** [youtube playlist](https://www.youtube.com/playlist?list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL) — practical linux terminal basics
- **books, papers & repositories:**
  1. **linux journey:** [linuxjourney.com](https://linuxjourney.com/) — interactive platform to learn linux fundamentals step by step
  2. **the linux command line (william shotts):** [linuxcommand.org/tlcl.php (free pdf)](https://linuxcommand.org/tlcl.php) — free comprehensive book on shell scripting and command-line tools

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

**resources:**

- **turkish resources:**
  1. **kablosuz kedi (gökhan kandemir) – docker from a to z:** [part 1 video](https://www.youtube.com/watch?v=4XVfmGE1F_w) & [devops playlist](https://www.youtube.com/playlist?list=PL_f2F0Oyaj48lF-6Wr2d95dAMaye8RX0d) — turkish course on dockerfile, images, containers, and docker compose
  2. **barış aslan (@barisaslan):** [youtube channel](https://www.youtube.com/@BarisAslan) — turkish tutorials on git/github and server deployment
- **video lectures:**
  1. **techworld with nana – docker, github actions & kubernetes:** [youtube channel](https://www.youtube.com/@TechWorldwithNana) — packaging ai models and ros 2 nodes consistently with docker containers
  2. **kunal kushwaha – complete git, docker & devops bootcamp:** [youtube playlist](https://www.youtube.com/playlist?list=PL9gnSGHSqcnoqBXdMwUTRod4Gi3eac2Ak)
- **books, papers & repositories:**
  1. **docker official getting started guide:** [docs.docker.com/get-started](https://docs.docker.com/get-started/) — hands-on official docker beginner guide
  2. **pro git book (2nd ed.):** [english](https://git-scm.com/book/en/v2) · [turkish](https://git-scm.com/book/tr/v2) — branching, rebasing, submodules, and git workflows
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

**resources:**

- **video lectures:**
  1. **freecodecamp (andrew brown) – aws cloud practitioner course:** [youtube video](https://www.youtube.com/watch?v=SOTamWNgDKc) — overview of cloud gpu instances (ec2), s3 storage, vpc networking, and iam
- **books, papers & repositories:**
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

**resources:**

- **video lectures:**
  1. **full stack deep learning (uc berkeley):** [youtube lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) & [course site](https://fullstackdeeplearning.com/course/2022/) — end-to-end mlops: data pipelines, testing, ci/cd, deployment, and monitoring
  2. **databricks – mlops & mlflow tutorials:** [youtube channel](https://www.youtube.com/@Databricks) — experiment tracking and model registry workflows
- **books, papers & repositories:**
  1. **made with ml (goku mohandas):** [madewithml.com](https://madewithml.com/) — free interactive course covering ml design, pytorch training, testing, and production deployment
  2. **designing machine learning systems (chip huyen):** [o'reilly book page](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) & [github notes](https://github.com/chiphuyen/dmls-book) — practical book on ml system design and production architecture
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

**resources:**

- **video lectures:**
  1. **arjancodes – building production fastapi & ai services:** [youtube channel](https://www.youtube.com/@ArjanCodes) — serving ai models as clean rest apis in python
  2. **sebastián ramírez (tiangolo) – fastapi talks & tutorials:** [youtube search](https://www.youtube.com/results?search_query=sebastian+ramirez+fastapi)
- **books, papers & repositories:**
  1. **fastapi official tutorial:** [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/) — learn to build async, type-safe ai apis with pydantic and swagger docs
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

**resources:**

- **turkish resources:**
  1. **bora kaşmer – backend architecture, redis, kafka & rabbitmq:** [youtube channel](https://www.youtube.com/@BoraKasmer) — turkish tutorials on distributed message queues, caching, and backend design
  2. **gençay yıldız – microservices, rabbitmq & api design:** [youtube playlists](https://www.youtube.com/@GencayYildiz/playlists) — turkish backend series
  3. **kablosuz kedi – backend architecture series:** [youtube channel](https://www.youtube.com/@kablosuzkedi) — turkish backend architecture tutorials
- **video lectures:**
  1. **hussein nasser – backend engineering:** [youtube channel](https://www.youtube.com/@hnasr) — deep dives on http/2, grpc, websockets, postgres, redis, and proxies
- **books, papers & repositories:**
  1. **backend developer roadmap:** [roadmap.sh/backend](https://roadmap.sh/backend) — step-by-step backend engineering reference map

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

**resources:**

- **turkish resources:**
  1. **bora kaşmer – distributed systems & high-traffic architecture:** [youtube channel](https://www.youtube.com/@BoraKasmer)
- **video lectures:**
  1. **bytebytego (alex xu) – visual system design:** [youtube channel](https://www.youtube.com/@ByteByteGo) — animated breakdowns of load balancing, sharding, cap theorem, and event-driven systems
  2. **gaurav sen – system design series:** [youtube playlist](https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX) — scalable system design fundamentals from scratch
- **books, papers & repositories:**
  1. **donnemartin/system-design-primer:** [github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) — free illustrated guide on designing large-scale systems
  2. **system design interview, vol. 1 & vol. 2 (alex xu):** [bytebytego.com](https://bytebytego.com/) — practical preparation book for system design interviews

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

**resources:**

- **turkish resources:**
  1. **gençay yıldız – software architecture, design patterns & solid:** [youtube channel](https://www.youtube.com/@GencayYildiz)
- **video lectures:**
  1. **cppcon – large-scale c++ software architecture talks:** [youtube search](https://www.youtube.com/results?search_query=cppcon+software+architecture+klaus+iglberger) — dependency management and design patterns in large c++ codebases
- **books, papers & repositories:**
  1. **a philosophy of software design (prof. john ousterhout):** [talk video](https://www.youtube.com/watch?v=bmSAYlu0NcY) & [book page](https://web.stanford.edu/~ouster/cgi-bin/book.php) — short practical book on managing complexity and designing clean modules
  2. **patterns of enterprise application architecture (martin fowler):** [martinfowler.com/eaacatalog](https://martinfowler.com/eaaCatalog/) — reference catalog for software architecture patterns
