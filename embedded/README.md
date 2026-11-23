# embedded systems and real-time computing

engineering curriculum, hardware interfacing, firmware architecture, and curated resources for microcontrollers, bare-metal c/c++, real-time operating systems, and edge ai deployment.

---

## architecture overview

embedded systems connect software intelligence to physical sensors and actuators with strict real-time determinism:

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

## study checklist

### 01. microcontroller architecture and bare-metal programming
- [ ] arm cortex-m series (m4, m7): core registers, memory map, flash memory, and sram layout
- [ ] bare-metal c and modern embedded c++: `volatile`, memory-mapped i/o, bitwise operations, and memory alignment
- [ ] linker scripts, crt0 startup code, vector table, and stack/heap memory boundaries
- [ ] hardware timers, pulse width modulation (pwm), input capture, and analog-to-digital conversion (adc)

### 02. interrupt handling and high-speed communication buses
- [ ] nested vectored interrupt controller (nvic): interrupt priorities, preemption, and isr latency
- [ ] direct memory access (dma): circular buffer management, zero-copy peripheral transfers
- [ ] serial protocols: uart/usart with dma, spi (serial peripheral interface), and i2c (two-wire interface)
- [ ] controller area network (can bus / can-fd): differential physical layer, message framing, arbitration, and error handling

### 03. real-time operating systems (rtos)
- [ ] freertos kernel architecture: preemptive priority-based scheduling and context switching
- [ ] task states, deterministic deadlines, task starvation, and priority inversion (priority inheritance)
- [ ] inter-task communication (ipc): thread-safe queues, binary/counting semaphores, mutexes, and direct-to-task notifications
- [ ] software timers, tickless idle mode, memory allocation schemes (heap_4), and watchdog timers (iwdg/wwdg)

### 04. edge ai and hardware accelerators
- [ ] tinyml on microcontrollers: arm cmsis-nn library and tflite-micro execution
- [ ] embedded companion computers (nvidia jetson orin): nv12/rgb zero-copy unified memory architecture
- [ ] deep learning model optimization: post-training quantization (fp16, int8 with entropy calibration), pruning, and layer fusion
- [ ] tensorrt c++ runtime: custom plugins, cuda streams, and low-latency inference pipelines (< 4 ms)

---

## curated resources

### video lectures & course series
- [ben eater – serial communication protocols & computer architecture](https://www.youtube.com/@BenEater): crystal-clear oscilloscope-level explanations of clock signals, uart, spi, i2c, and hardware registers.
- [phil's lab – stm32 pcb design, hardware interfacing & firmware](https://www.youtube.com/@PhilsLab): industry-grade hardware schematic design, mixed-signal routing, and bare-metal c firmware tutorials.
- [mit 6.5940 – tinyml and efficient deep learning computing (prof. song han)](https://hanlab.mit.edu/courses/2024-fall-65940): world-leading academic course on model quantization, neural network compression, and hardware acceleration.
- [jetsonhacks – nvidia jetson edge ai and tensorrt guides](https://www.youtube.com/@JetsonHacks): pragmatic setup, camera interfacing, and real-time inference optimization on embedded jetson hardware.

### foundational books & academic materials
- [the definitive guide to arm cortex-m3 and cortex-m4 processors (joseph yiu)](https://www.elsevier.com/books/the-definitive-guide-to-arm-cortex-m3-and-cortex-m4-processors/yiu/978-0-12-408082-9): authoritative architecture reference for instruction sets, nvic, and memory management.
- [mastering freertos: a hands-on tutorial guide (richard barry)](https://www.freertos.org/Documentation/RTOS_book.html): official comprehensive guide by the creator of freertos covering scheduling and concurrency.
- [nvidia tensorrt developer guide and c++ api reference](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html): official documentation for building high-throughput low-latency inference engines.

### open-source codebases & tools
- [freertos/freertos](https://github.com/FreeRTOS/FreeRTOS): market-leading real-time operating system for microcontrollers.
- [stmicroelectronics/stm32cubeg4](https://github.com/STMicroelectronics/STM32CubeG4): official hal and ll firmware drivers for arm cortex-m4 microcontrollers.
- [dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference): premier c++ library for real-time edge vision and deep learning inference on nvidia jetson.
