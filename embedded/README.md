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

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe gömülü sistem kaynakları):**
  1. **coşkun taşdemir:** [github profili (ctasdemir)](https://github.com/ctasdemir) — gömülü sistemler ve mikrodenetleyici notları
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **ben eater – serial communication protocols (uart, spi, i2c) & hardware interrupts:** [youtube kanalı](https://www.youtube.com/@BenEater) — **[ilk izlenecek]** osiloskop ve breadboard üzerinde saat sinyali (clock), bit kaydırma ve protokollerin fiziksel seviyesini gözle görme
  2. **stmicroelectronics & microchip official getting started series:** [stmicroelectronics youtube](https://www.youtube.com/@stmicroelectronics) — endüstriyel mikrodenetleyici çevre birimleri (peripherals)
- **oku (pratik kılavuzlar ve kitaplar — önem sırasıyla):**
  1. **sparkfun communication protocol tutorials (uart, spi, i2c, can bus, pwm):** [learn.sparkfun.com/tutorials](https://learn.sparkfun.com/tutorials) — **[görsel kılavuz]** sensör ve motor sürücü haberleşme protokollerinin diyagramlarla özeti
  2. **the art of electronics (paul horowitz & winfield hill):** [artofelectronics.net](https://artofelectronics.net/) — donanım ve elektronik dünyasının temel başvuru kitabı

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

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **miro samek (quantum leaps) – modern embedded systems programming course in c/c++:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLPW8O6W-1chwyTzI3BHwBLbGQoPFxPAPM) — **[temel gömülü yazılım dersi – zorunlu]** register seviyesinden başlayıp pointerlar, `volatile`, startup kodu, kesmeler, oop ve durum makinelerini (state machines) mikrodenetleyici üzerinde gösteren kapsamlı seri
  2. **low level learning – c, memory safety, embedded linux & kernel programming:** [youtube kanalı](https://www.youtube.com/@lowleveldevel1712) — düşük seviyeli sistem programlama ve bellek güvenliği pratikleri
  3. **andreas fertig & jason turner (cppcon) – zero-cost abstractions & modern c++ in embedded systems:** [youtube sunumu](https://www.youtube.com/results?search_query=cppcon+modern+c%2B%2B+embedded+systems) — bellek kısıtlı (no-heap) donanımlarda `constexpr` ve şablonlarla (templates) yüksek hızlı c++ yazımı
- **oku (kitap ve standartlar — önem sırasıyla):**
  1. **making embedded systems: design patterns for great software (elecia white – o'reilly):** [o'reilly kitap sayfası](https://www.oreilly.com/library/view/making-embedded-systems/9781098151539/) — hal (hardware abstraction layer), sürücü mimarisi ve gömülü tasarım desenleri
  2. **barr-c:2018 embedded c coding standard (michael barr):** [barrgroup.com (ücretsiz pdf)](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — hataya dayanıklı gömülü kodlama standartları

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

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **tr: —**
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **shawn hymel (digikey) – introduction to rtos (real-time operating system) with freertos:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLEBQazB0HUyQ4hAPU1cJED6t3DU0h34bz) — **[ilk izlenecek – referans seri]** preemptive & priority scheduling, queue, mutex, semaphore, priority inversion ve deadlock kavramlarını 12 bölümde uygulamalı öğreten seri
- **oku & doküman (önem sırasıyla):**
  1. **mastering the freertos real time kernel (official hands-on tutorial guide):** [freertos.org/documentation/02-kernel/07-books-and-manual/01-rtos_book](https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book) — ücretsiz resmi freertos mühendislik kitabı
  2. **zephyr project (modern linux foundation rtos) documentation:** [docs.zephyrproject.org](https://docs.zephyrproject.org/latest/index.html) — modern robotik ve endüstriyel iot kartlarında hızla yaygınlaşan yeni nesil rtos

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
