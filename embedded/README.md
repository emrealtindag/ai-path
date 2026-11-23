# embedded systems and real-time computing

engineering curriculum, hardware interfacing, firmware architecture, and curated resources for microcontrollers, bare-metal c/c++, real-time operating systems, and edge ai deployment.

---

## architecture overview

```
[application algorithms: control loops / edge ai models]
                             │
                             ▼
  [real-time operating system: freertos / tasks / queues]
                             │
                             ▼
  [hardware abstraction layer: stm32 hal / register drivers]
                             │
                             ▼
[communication buses: can bus / spi / i2c / uart / dma]
                             │
                             ▼
   [hardware peripherals: sensors / bldc escs / telemetry]
```

---

## complete checklist and resources

### 12.1 embedded fundamentals

- [ ] microcontrollers
- [ ] microprocessors
- [ ] gpio
- [ ] timers
- [ ] interrupts
- [ ] adc (analog-to-digital converter)
- [ ] dac (digital-to-analog converter)
- [ ] pwm (pulse width modulation)
- [ ] uart
- [ ] spi
- [ ] i2c
- [ ] can bus
- [ ] serial communication

**resources:**

- **turkish resources:**
  1. **coşkun taşdemir:** [github profile (ctasdemir)](https://github.com/ctasdemir) — turkish embedded systems and microcontroller study notes
- **video lectures:**
  1. **ben eater – serial protocols & hardware interrupts:** [youtube channel](https://www.youtube.com/@BenEater) — oscilloscope and breadboard walkthroughs of clock signals, uart, spi, and i2c
  2. **stmicroelectronics official tutorials:** [youtube channel](https://www.youtube.com/@stmicroelectronics) — hardware peripherals and microcontroller configuration guides
- **books, papers & repositories:**
  1. **sparkfun communication protocol tutorials:** [learn.sparkfun.com/tutorials](https://learn.sparkfun.com/tutorials) — clean diagrams explaining uart, spi, i2c, can bus, and pwm
  2. **the art of electronics (horowitz & hill):** [artofelectronics.net](https://artofelectronics.net/) — classic reference book on electronics and hardware design

### 12.2 embedded programming

- [ ] embedded c
- [ ] embedded c++
- [ ] memory constraints
- [ ] firmware architecture
- [ ] device drivers
- [ ] hardware abstraction layers (hal)
- [ ] peripheral programming
- [ ] debugging
- [ ] jtag
- [ ] swd

**resources:**

- **turkish resources:**
- **video lectures:**
  1. **miro samek – modern embedded systems programming:** [youtube playlist](https://www.youtube.com/playlist?list=PLPW8O6W-1chwyTzI3BHwBLbGQoPFxPAPM) — hands-on course from hardware registers and interrupts to state machines in c/c++
  2. **low level – systems & kernel programming:** [youtube channel](https://www.youtube.com/@lowleveldevel1712) — practical videos on low-level c, memory safety, and embedded linux
  3. **cppcon – modern c++ in embedded systems:** [youtube search](https://www.youtube.com/results?search_query=cppcon+modern+c%2B%2B+embedded+systems) — writing zero-cost abstractions and no-heap `constexpr` code for microcontrollers
- **books, papers & repositories:**
  1. **making embedded systems (elecia white):** [book page](https://www.oreilly.com/library/view/making-embedded-systems/9781098151539/) — hal design, driver architectures, and embedded software patterns
  2. **barr-c embedded c coding standard (michael barr):** [free pdf](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — coding rules for writing reliable, bug-resistant embedded c firmware

### 12.3 real-time systems

- [ ] real-time operating systems (rtos)
- [ ] freertos, zephyr rtos
- [ ] task scheduling (preemptive, cooperative)
- [ ] priority scheduling
- [ ] priority inversion
- [ ] interrupt latency
- [ ] deterministic execution
- [ ] deadline management
- [ ] timing analysis
- [ ] concurrency
- [ ] synchronization

**resources:**

- **turkish resources:**
  1. **tr: —**
- **video lectures:**
  1. **shawn hymel – introduction to rtos with freertos:** [youtube playlist](https://www.youtube.com/playlist?list=PLEBQazB0HUyQ4hAPU1cJED6t3DU0h34bz) — 12-part practical series on scheduling, queues, mutexes, semaphores, and deadlocks
- **books, papers & repositories:**
  1. **mastering the freertos real time kernel:** [official book](https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book) — free official freertos engineering guide
  2. **zephyr rtos documentation:** [docs.zephyrproject.org](https://docs.zephyrproject.org/latest/index.html) — modern open-source rtos widely adopted in robotics and embedded iot hardware

### 12.4 hardware-software integration

- [ ] sensor interfaces
- [ ] actuator interfaces
- [ ] communication protocols
- [ ] firmware integration
- [ ] hardware abstraction layers (hal)
- [ ] system diagnostics
- [ ] fault detection
- [ ] reliability engineering
- [ ] px4 autopilot architecture (uorb & ros 2 micro-xrce-dds)
- [ ] ardupilot ap_hal & mavlink telemetry protocol
- [ ] qgroundcontrol (qgc) & gcs mission planning
- [ ] uav 6-dof flight dynamics & cascaded autopilot control (beard & mclain)
- [ ] geometric uav tracking control on se(3) (taeyoung lee)

**resources:**

- **video lectures:**
  1. **phil's lab – hardware design & flight controller firmware in c/c++:** [youtube channel](https://www.youtube.com/@PhilsLab) — designing custom stm32 + imu flight controller pcbs and writing sensor drivers and kalman filters in c
- **books, papers & repositories:**
  1. **px4 autopilot architecture & companion integration:** [docs.px4.io](https://docs.px4.io/main/en/concept/architecture.html) & [github repo](https://github.com/PX4/PX4-Autopilot) — how sensor drivers connect via `uorb` to ekf2, flight controllers, and ros 2 (`uxrce_dds`) on a companion computer
  2. **ardupilot architecture & ap_hal:** [ardupilot.org](https://ardupilot.org/) · [github repo](https://github.com/ArduPilot/ardupilot) & [mavproxy](https://github.com/ArduPilot/MAVProxy) — hardware abstraction layer (ap_hal) on chibios rtos with 24-state ekf3 and mavlink support for copter, plane, and vtol
  3. **qgroundcontrol (mavlink ground control station):** [qgroundcontrol.com](http://qgroundcontrol.com/) & [github repo](https://github.com/mavlink/qgroundcontrol) — c++/qt ground control software for waypoint mission planning, calibration, parameter tuning, and live telemetry
  4. **small unmanned aircraft: theory and practice (beard & mclain):** [uavbook.byu.edu](http://uavbook.byu.edu/) & [magicc lab](https://magicc.byu.edu/) — core textbook explaining the 6-dof flight dynamics, aerodynamics, and cascaded pid loops behind ardupilot and px4
  5. **geometric tracking control of a quadrotor uav on se(3) (taeyoung lee et al.):** [arxiv:1003.2005](https://arxiv.org/abs/1003.2005) — seminal paper eliminating euler gimbal lock by tracking quadrotor trajectories directly on $so(3)$ and $se(3)$

### 12.5 embedded ai

- [ ] tinyml
- [ ] edge inference
- [ ] model quantization (int8, fp8)
- [ ] model pruning
- [ ] knowledge distillation
- [ ] hardware acceleration
- [ ] neural processing units (npu)
- [ ] embedded gpu computing (nvidia jetson architecture)

**resources:**

- **video lectures:**
  1. **jetsonhacks – nvidia jetson edge ai & tensorrt:** [youtube channel](https://www.youtube.com/@JetsonHacks) & [github](https://github.com/JetsonHacksNano) — guides for camera drivers, cuda, and c++ tensorrt setups on nvidia jetson
  2. **mit 6.5940 – tinyml & efficient deep learning computing (song han):** [youtube lecture series](https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB) & [course site](https://hanlab.mit.edu/courses/2024-fall-65940) — quantization (int8/fp8/int4), pruning, distillation, and hardware-aware efficiency
  3. **shawn hymel – introduction to embedded machine learning:** [youtube playlist](https://www.youtube.com/playlist?list=PL7VEa1KauMQqZFj_nWRfsCZNXaBbkuurG) — running neural network inference on microcontrollers
- **books, papers & repositories:**
  1. **dusty-nv/jetson-inference:** [github repo](https://github.com/dusty-nv/jetson-inference) & [nvidia jetson ai lab](https://www.jetson-ai-lab.com/) — official c++/python tensorrt tutorials for real-time detection, segmentation, and pose estimation
  2. **wang-xinyu/tensorrtx:** [github repo](https://github.com/wang-xinyu/tensorrtx) — shows how to convert models like yolov8/v11, resnet, and detr from pytorch and write them from scratch using the pure c++ tensorrt api
  3. **tinyml (pete warden & daniel situnayake):** [o'reilly book page](https://www.oreilly.com/library/view/tinyml/9781492052036/) — practical reference for machine learning on arduino and ultra-low-power microcontrollers
