# computer science and systems

engineering curriculum, algorithmic complexity, hardware architecture, and curated resources for data structures, memory hierarchy, operating systems, and networking.

---

## architecture overview

computer science bridges abstract algorithmic logic with physical silicon execution:

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

## study checklist

### 01. data structures and algorithmic complexity
- [ ] asymptotic analysis: big-o, big-omega, and big-theta notation, space vs time complexity
- [ ] linear structures: contiguous arrays, singly/doubly linked lists, array-based stacks, and queues
- [ ] hashing: hash functions, collision resolution (chaining vs open addressing), load factors, and robin hood hashing
- [ ] tree structures: binary search trees (bst), avl balanced trees, red-black trees, and b-trees
- [ ] priority queues & heaps: binary min/max heaps, d-ary heaps, and fibonacci heaps
- [ ] graph representations: adjacency matrices, adjacency lists, and edge lists
- [ ] graph traversal & shortest paths: bfs, dfs, topological sorting, dijkstra, and bellman-ford

### 02. computer architecture and memory hierarchy
- [ ] von neumann architecture: program counter, instruction register, control unit, and alu
- [ ] instruction pipelining: fetch, decode, execute, memory access, writeback, and pipeline hazards
- [ ] memory hierarchy: l1, l2, l3 cache latency, cache lines (64 bytes), spatial and temporal cache locality
- [ ] cache architectures: direct-mapped, fully associative, set-associative, and cache eviction policies (lru)
- [ ] false sharing, cache coherence protocols (mesi), and hardware prefetching
- [ ] virtual memory: memory management unit (mmu), page tables, translation lookaside buffer (tlb), and page faults

### 03. operating systems and concurrency
- [ ] processes vs threads: process control block (pcb), context switching overhead, and thread-local storage (tls)
- [ ] cpu scheduling: preemptive priority scheduling, round-robin, and completely fair scheduler (cfs)
- [ ] synchronization primitives: mutual exclusion (mutex), spinlocks, condition variables, counting semaphores
- [ ] concurrency pitfalls: race conditions, deadlocks (coffman conditions), priority inversion, and lock-free programming
- [ ] inter-process communication (ipc): pipes, posix shared memory, message queues, and unix domain sockets

### 04. networking and distributed middleware
- [ ] osi and tcp/ip models: packet encapsulation, framing, and routing
- [ ] transport protocols: tcp (reliable stream, flow control, congestion avoidance) vs udp (low-latency datagrams)
- [ ] socket programming: berkeley sockets api in c/c++, non-blocking i/o, and event multiplexing (`epoll`)
- [ ] robotics middleware: data distribution service (dds), rtps protocol, and publish-subscribe serialization

---

## curated resources

### video lectures & course series
- [harvard cs50x – introduction to computer science (david j. malan)](https://www.youtube.com/playlist?list=PLhQjrBD2T381WAHyx1pq-sBfykqMBI7V4): world-renowned foundations of memory layout, pointers, data structures, and computer science.
- [mit 6.006 – introduction to algorithms (erik demaine & srini devadas)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb): rigorous mathematical analysis of data structures, sorting, graphs, and dynamic programming.
- [william fiset – data structures easy to advanced](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu): crystal-clear animated walkthroughs of heaps, balanced trees, and graph algorithms.

### foundational books & academic materials
- [computer systems: a programmer's perspective (cs:app) (randal e. bryant & david r. o'hallaron)](https://csapp.cs.cmu.edu/): the undisputed master reference on how computer architecture, cache hierarchy, compilers, and operating systems execute code.
- [introduction to algorithms (clrs) (cormen, leiserson, rivest, stein)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/): the standard authoritative textbook on algorithms, data structures, and algorithmic proofs.
- [operating systems: three easy pieces (ostep) (remzi h. arpaci-dusseau & andrea c. arpaci-dusseau)](https://pages.cs.wisc.edu/~remzi/OSTEP/): freely available exceptional text on virtualization, concurrency, and persistence.

### open-source codebases & tools
- [neetcode-gh/leetcode](https://neetcode.io/): curated roadmap and clean implementations of fundamental algorithmic problem patterns.
- [eprosima/fast-dds](https://github.com/eProsima/Fast-DDS): industrial c++ implementation of omg dds standard powering ros 2 communication.
- [valgrind](https://valgrind.org/): instrumentation framework for building dynamic analysis tools and memory leak detection.
