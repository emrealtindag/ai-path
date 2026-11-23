# computer vision

engineering curriculum, algorithmic foundations, geometric representations, and curated resources for 2d image processing, classical feature extraction, applied vision, and deep visual perception.

---

## architecture overview

```
[camera stream: bgr / nv12 frames]
                 │
                 ▼
[image preprocessing: filtering / color spaces]
                 │
                 ▼
[geometric features: orb / sift / optical flow]
                 │
                 ▼
[visual inference: object detection / segmentation]
                 │
                 ▼
[downstream tasks: tracking / visual odometry / spatial ai]
```

---

## complete checklist and resources

### 01. computer vision – bilgisayarlı görü

#### 6.1 image processing

- [ ] digital image fundamentals
- [ ] image representation
- [ ] color spaces (rgb, hsv, lab)
- [ ] image filtering
- [ ] gaussian blur
- [ ] median filtering
- [ ] edge detection
- [ ] canny
- [ ] sobel
- [ ] laplacian
- [ ] thresholding (otsu)
- [ ] morphological operations (dilation, erosion)
- [ ] histogram equalization
- [ ] image pyramids
- [ ] frequency domain processing
- [ ] fourier transform
- [ ] image restoration
- [ ] image enhancement

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe akademik ve uygulamalı kaynaklar):**
  1. **odtü ceng 483 – introduction to computer vision (prof. dr. sinan kalkan & doç. dr. emre akbaş):** [kovan lab / akademik sayfa](https://kovan.ceng.metu.edu.tr/~sinan/) — filtreleme, kenar tespiti ve görüntü temsilleri üzerine odtü müfredatı
  2. **itü blg 453e – bilgisayarlı görü (computer vision):** [itü ders katalog & içeriği](https://www.sis.itu.edu.tr/TR/ogrenci/lisans/ders-planlari/plan/BLGE/201810.html) — akademik ders izlencesi ve proje konuları
  3. **bilgisayar kavramları – görüntü işleme (image processing):** [resmi site (sadievrenseker.com)](https://sadievrenseker.com/) — temel filtreler, morfoloji ve histogram eşitleme mantığı
  4. **zafer demirkol (@zaferdemirkol):** [youtube kanalı](https://www.youtube.com/@zaferdemirkol) — genel yapay zekâ ve tensorflow söyleşileri
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **shree nayar – first principles of computer vision (columbia university):** [youtube kanalı & oynatma listeleri](https://www.youtube.com/@firstprinciplesofcomputerv3258/playlists) — **[ilk izlenecek – akademik seri]** görüntü oluşumu, filtreleme, kenar bulma ve frekans uzayını berrak görsellerle anlatan üniversite serisi
  2. **murtaza's workshop – robotics and ai (opencv python & c++):** [youtube kanalı](https://www.youtube.com/@murtazasworkshop) — **[pratik kodlama]** opencv ile görüntü işleme boru hatlarını sıfırdan hızlıca kodlamak için
- **oku & doküman (önem sırasıyla):**
  1. **opencv 4.x official image processing tutorials (python & c++):** [docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html) — canny, sobel, otsu, morfoloji ve renk uzaylarını doğrudan kodlayarak öğrenme
  2. **digital image processing (rafael c. gonzalez & richard e. woods):** [imageprocessingplace.com](http://www.imageprocessingplace.com/) — görüntü işlemenin klasik referans ders kitabı

#### 6.2 classical computer vision

- [ ] feature detection
- [ ] harris corner detector
- [ ] fast
- [ ] sift
- [ ] surf
- [ ] orb
- [ ] brief
- [ ] feature description
- [ ] feature matching
- [ ] brute force matching
- [ ] flann
- [ ] ransac
- [ ] homography
- [ ] image registration
- [ ] optical flow
- [ ] lucas-kanade
- [ ] dense optical flow (farneback)
- [ ] background subtraction
- [ ] motion detection

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe akademik kaynaklar):**
  1. **odtü ceng 483 & itü blg 453e – öznitelik çıkarımı, ransac ve optik akış modülleri:** [odtü ceng 483 sayfası](https://user.ceng.metu.edu.tr/~skalkan/)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **shree nayar – first principles of cv (features, ransac, optical flow & tracking):** [youtube oynatma listeleri](https://www.youtube.com/@firstprinciplesofcomputerv3258/playlists) — **[ilk izlenecek]** harris, sift, homografi, ransac ve lucas-kanade optik akış'ın kusursuz matematiksel anlatımı
  2. **cyrill stachniss – photogrammetry i & ii (bonn üniversitesi):** [youtube oynatma listeleri](https://www.youtube.com/@CyrillStachniss/playlists) — **[ana mühendislik dersi]** doğrudan robotik, iha haritalama ve slam perspektifinden öznitelik eşleştirme (feature matching)
- **oku & repo (kitap, doküman ve endüstriyel kodlar — önem sırasıyla):**
  1. **opencv feature detection, description & homography tutorials:** [docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html) — orb, sift, flann ve ransac ile pratik görüntü eşleştirme kodları
  2. **computer vision: algorithms and applications, 2nd ed. (richard szeliski):** [szeliski.org/book (ücretsiz tam kitap pdf)](https://szeliski.org/Book/) — **[başucu kitabı]** bölüm 7 (feature detection & matching), bölüm 8 (alignment) ve bölüm 9 (motion/optical flow)
  3. **repo – cvg/lightglue (eth zürich):** [github.com/cvg/lightglue](https://github.com/cvg/LightGlue) — klasik sift/orb'un ötesine geçen, modern derin öğrenme tabanlı ultra-hızlı yerel öznitelik eşleştirme reposu
  4. **repo – zju3dv/loftr:** [github.com/zju3dv/loftr](https://github.com/zju3dv/LoFTR) — dokusu zayıf yüzeylerde bile çalışan transformer tabanlı dedektörsüz öznitelik eşleştirme

#### 6.3 camera geometry

- [ ] pinhole camera model
- [ ] intrinsic parameters ($k$)
- [ ] extrinsic parameters ($[r \mid t]$)
- [ ] camera calibration (zhang yöntemi)
- [ ] lens distortion
- [ ] radial distortion
- [ ] tangential distortion
- [ ] perspective projection
- [ ] coordinate systems
- [ ] rotation matrices
- [ ] translation vectors
- [ ] homogeneous coordinates
- [ ] epipolar geometry
- [ ] fundamental matrix ($f$)
- [ ] essential matrix ($e$)
- [ ] stereo geometry

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **odtü ceng 483 – kamera modeli, kalibrasyon ve stereo geometri ders notları:** [odtü ceng](https://user.ceng.metu.edu.tr/~skalkan/)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **shree nayar – camera calibration & epipolar geometry (first principles of cv):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo) — **[ilk izlenecek]** iğneada (pinhole) kamera modeli, iç/dış matrisler ($k, [r\mid t]$) ve fundamental/essential matrislerin ($f, e$) en net sezgisel anlatımı
  2. **cyrill stachniss – camera calibration (zhang's method) & epipolar geometry:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y) — **[ana mühendislik dersi]** kamera kalibrasyonu ve stereo geometrinin matrislerle adım adım tahtada çözümü
  3. **prof. daniel cremers – multiple view geometry in computer vision (tum - münih teknik üniversitesi):** [youtube tam dönem ders serisi](https://www.youtube.com/playlist?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) — **[zirve akademik ders]** 3b kamera geometrisi ve görsel odometrinin matematiksel derinliği
- **oku & uygulama (kitap ve kalibrasyon rehberi — önem sırasıyla):**
  1. **opencv camera calibration and 3d reconstruction tutorials:** [docs.opencv.org/4.x/d9/db7/tutorial_py_table_of_contents_calib3d.html](https://docs.opencv.org/4.x/d9/db7/tutorial_py_table_of_contents_calib3d.html) — satranç tahtası (checkerboard) ile gerçek bir kamerayı kalibre etme ve lens distorsiyonunu giderme kodu
  2. **multiple view geometry in computer vision (richard hartley & andrew zisserman):** [robots.ox.ac.uk/~vgg/hzbook](https://www.robots.ox.ac.uk/~vgg/hzbook/) — **[birincil referans kitap]** kamera geometrisi, epipolar geometri ve 3b yeniden yapılandırmanın standart akademik referansı
  3. **an invitation to 3-d vision (yi ma, stefano soatto, jana kosecka, shankar sastry):** [ücretsiz yazar taslağı / kitap sayfası](https://link.springer.com/book/10.1007/978-0-387-21779-6) — rijit gövde hareketi ve çoklu görünüm geometrisi

#### 6.4 deep learning for vision

- [ ] cnn architectures
- [ ] lenet
- [ ] alexnet
- [ ] vgg
- [ ] resnet
- [ ] densenet
- [ ] efficientnet
- [ ] mobilenet
- [ ] convnext
- [ ] feature pyramid networks (fpn)
- [ ] attention mechanisms
- [ ] vision transformers (vit)
- [ ] swin transformer

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe akademik kaynaklar):**
  1. **odtü ceng 501 – deep learning (prof. dr. sinan kalkan):** [resmi ders sayfası](https://kovan.ceng.metu.edu.tr/~sinan/) & [github repo](https://github.com/sinankalkan/CENG501-Spring2021) — resnet, fpn, vit ve görsel derin öğrenme mimarilerinin akademik sunumları
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **stanford cs231n – deep learning for computer vision (fei-fei li, justin johnson, serena yeung):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv) & [ders notları (cs231n.github.io)](https://cs231n.github.io/) — **[temel akademik cv dersi – zorunlu]** görsel derin öğrenmeye başlayan her mühendisin bitirmesi gereken standart stanford dersi
  2. **michigan eecs 498-007 / 598-005 – deep learning for computer vision (prof. justin johnson):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r) — cs231n'in pytorch ve modern transformer (vit) eklenmiş daha güncel versiyonu
- **oku & kütüphane (makale ve kod tabanları — önem sırasıyla):**
  1. **pytorch image models (`timm`– ross wightman):** [huggingface.co/docs/timm](https://huggingface.co/docs/timm/index) & [github repo](https://github.com/huggingface/pytorch-image-models) — **[endüstri standardı kütüphane]** resnet, efficientnet, convnext, vit ve swin dahil yüzlerce omurga (backbone) modelini tek satırda kullanma
  2. **deep residual learning for image recognition – resnet (he et al., cvpr 2016):** [arxiv:1512.03385](https://arxiv.org/abs/1512.03385) — tarihin en çok atıf alan ai makalesi
  3. **swin transformer: hierarchical vision transformer using shifted windows (liu et al., iccv 2021):** [arxiv:2103.14030](https://arxiv.org/abs/2103.14030) — yoğun algılama (detection/segmentation) için standart vit omurgası
  4. **deeplearning-models: pytorch architecture implementations (sebastian raschka):** [github repo (rasbt/deeplearning-models)](https://github.com/rasbt/deeplearning-models) — **[görsel derin öğrenme modelleri kod deposu]** sebastian raschka'nın hazırladığı; lenet, alexnet, vgg, resnet, densenet, mobilenet gibi klasik ve modern cnn omurgalarını, vae/gan üretici modellerini ve eğitim numaralarını (lr warmup, gradyan biriktirme) saf pytorch ile sade jupyter notebook'lar halinde sunan 17.6k+ yıldızlı başvuru deposu

#### 6.5 object detection

- [ ] two-stage detectors
- [ ] r-cnn
- [ ] fast r-cnn
- [ ] faster r-cnn
- [ ] one-stage detectors
- [ ] ssd
- [ ] yolo architectures (v1–v11)
- [ ] retinanet (focal loss)
- [ ] detr (detection transformer)
- [ ] real-time object detection
- [ ] object tracking
- [ ] non-maximum suppression (nms)

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **odtü ceng 783 – object detection (r-cnn, yolo, detr) ders notları:** [odtü ceng](https://user.ceng.metu.edu.tr/~skalkan/DL/)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **justin johnson (michigan eecs 498) – object detection lectures (two-stage & single-stage):** [youtube ders videosu](https://www.youtube.com/watch?v=TB-fdISzpHQ) — **[ilk izlenecek]** r-cnn, fast/faster r-cnn, anchor boxes, nms ve ssd/yolo matematiğinin en net akademik anlatımı
  2. **murtaza's workshop – yolo custom object detection & real-time projects:** [youtube kanalı](https://www.youtube.com/@murtazasworkshop) — **[hızlı uygulama]** kendi veri setinle yolo eğitip gerçek zamanlı kamera üzerinde çalıştırma
  3. [**deeplearning.ai**](http://DeepLearning.AI)**– convolutional neural networks (object detection module):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF) — iou, anchor box ve non-maximum suppression (nms) temelleri
- **oku & repo (doküman, makale ve kod tabanları — önem sırasıyla):**
  1. **ultralytics yolo official documentation (yolov8 / yolov11):** [docs.ultralytics.com](https://docs.ultralytics.com/) & [github repo](https://github.com/ultralytics/ultralytics) — **[gerçek zamanlı endüstri standardı]** eğitim, doğrulama ve tensorrt/onnx dışa aktarma kılavuzu
  2. **end-to-end object detection with transformers – detr (carion et al., meta ai):** [arxiv:2005.12872](https://arxiv.org/abs/2005.12872) & [rt-detr repo](https://github.com/lyuwenyu/RT-DETR) — nms gerektirmeyen modern transformer tabanlı nesne tespiti
  3. **repo – open-mmlab/mmdetection:** [github.com/open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection) — araştırma ve karşılaştırma (benchmark) için kapsamlı modüler nesne tespiti kutusu
  4. **hugging face trending papers & arxiv computer vision (**[**cs.cv**](https://arxiv.org/list/cs.CV/recent)**):** [huggingface.co/papers/trending](https://huggingface.co/papers/trending) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — güncel sota modellerin ve makalelerin takibi (not: meta, papers with code'u temmuz 2025'te kapattığı için güncel makale takibi hugging face papers ve arxiv üzerinden yapılır)

#### 6.6 image segmentation

- [ ] semantic segmentation
- [ ] instance segmentation
- [ ] panoptic segmentation
- [ ] fcn (fully convolutional networks)
- [ ] u-net
- [ ] deeplab (v1, v2, v3, v3+)
- [ ] mask r-cnn
- [ ] segformer
- [ ] mask2former
- [ ] segment anything models (sam, sam 2)

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **odtü ceng 783 – semantic, instance & panoptic segmentation sunumları:** [odtü ceng](https://user.ceng.metu.edu.tr/~skalkan/DL/)
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **stanford cs231n / michigan eecs 498 – image segmentation (semantic & instance):** [youtube ders videosu](https://www.youtube.com/watch?v=6CCXyfvubvY) — **[ilk izlenecek]** fcn, transposed convolution, u-net ve mask r-cnn mimarilerinin teorik temeli
  2. **digitalsreeni – image segmentation with u-net, mask r-cnn & sam in python:** [youtube kanalı](https://www.youtube.com/@DigitalSreeni) — **[uygulamalı kodlama]** medikal, uydu ve endüstriyel görüntülerde adım adım segmentasyon eğitimi
- **oku & repo (makale ve kod tabanları — önem sırasıyla):**
  1. **segment anything model 2 – sam 2 (meta ai research):** [ai.meta.com/sam2](https://ai.meta.com/sam2/) & [github repo (facebookresearch/sam2)](https://github.com/facebookresearch/sam2) — **[modern görsel vakıf modeli]** hem görüntü hem videoda sıfır-atış (zero-shot) gerçek zamanlı segmentasyon
  2. **u-net: convolutional networks for biomedical image segmentation (ronneberger et al.):** [arxiv:1505.04597](https://arxiv.org/abs/1505.04597) — az veriyle piksel düzeyinde segmentasyonun en ünlü mimarisi
  3. **mask r-cnn (he et al., iccv 2017):** [arxiv:1703.06870](https://arxiv.org/abs/1703.06870) — instance segmentation ve roialign mekanizmasının temel makalesi
  4. **repo – qubvel/segmentation_models.pytorch:** [github.com/qubvel-org/segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) — u-net, deeplabv3+ ve fpn modellerini hazır omurgalarla birkaç satırda eğitme kütüphanesi

#### 6.7 visual tracking

- [ ] single object tracking (sot)
- [ ] multiple object tracking (mot)
- [ ] kalman-based tracking
- [ ] sort (simple online and realtime tracking)
- [ ] deepsort
- [ ] bytetrack
- [ ] optical flow tracking
- [ ] appearance-based tracking
- [ ] re-identification (reid)
- [ ] tracking-by-detection

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr (türkçe kaynaklar):**
  1. **teknofest savaşan iha & hava savunma takımları teknik paylaşımları:** kalman filtresi + yolo + bytetrack entegrasyonu üzerine açık kaynak türkiye topluluk repoları
- **yt (yabancı video dersler — önem sırasıyla):**
  1. **nicolai nielsen – object tracking tutorials (sort, deepsort, bytetrack, kalman filter):** [youtube kanalı](https://www.youtube.com/@NicolaiAI) — **[ilk izlenecek]** çoklu nesne takibi (mot), macar algoritması (hungarian algorithm) ve kalman kestiriminin c++/python ile pratik anlatımı
  2. **roboflow – bytetrack & supervision multi-object tracking tutorials:** [youtube kanalı](https://www.youtube.com/@Roboflow) — tespit edilen nesnelere id atama, yörünge çizme ve hız/bölge analizi
- **oku & repo (makale ve endüstriyel kodlar — önem sırasıyla):**
  1. **bytetrack: multi-object tracking by associating every detection box (zhang et al., eccv 2022):** [arxiv:2110.06864](https://arxiv.org/abs/2110.06864) & [github repo (ifzhang/bytetrack)](https://github.com/ifzhang/ByteTrack) — **[endüstri standardı çoklu nesne takipçisi]** düşük güven skorlu kutuları da kullanarak örtüşme (occlusion) altında hedefi kaybetmeyen algoritma (c++ / tensorrt kodu repoda mevcut!)
  2. **simple online and realtime tracking with a deep association metric – deepsort (wojke et al.):** [arxiv:1703.07402](https://arxiv.org/abs/1703.07402) — kalman filtresi + görsel re-id özniteliklerini birleştiren temel takip makalesi
  3. **repo – mikel-brostrom/boxmot:** [github.com/mikel-brostrom/boxmot](https://github.com/mikel-brostrom/boxmot) — bytetrack, bot-sort, deepocsort ve strongsort algoritmalarını tek çatı altında toplayan modüler takip kütüphanesi

#### 6.8 modern visual ai

- [ ] vision foundation models
- [ ] self-supervised vision
- [ ] dino
- [ ] dinov2
- [ ] dinov3
- [ ] clip (contrastive language-image pretraining)
- [ ] siglip
- [ ] sam / sam 2
- [ ] image embeddings
- [ ] visual representations
- [ ] image retrieval
- [ ] semantic similarity
- [ ] visual search
- [ ] cross-view matching
- [ ] few-shot recognition
- [ ] zero-shot recognition
- [ ] open-vocabulary detection
- [ ] open-vocabulary segmentation

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **umar jamil – coding clip & vision-language models from scratch in pytorch:** [youtube kanalı](https://www.youtube.com/@umarjamilai) — **[ilk izlenecek – kodlama]** kontrastif görüntü-metin eşleştirmesini (clip) ve görsel gömmeleri (embeddings) sıfırdan kodlama
  2. **yannic kilcher – dinov2 & clip paper explanations:** [youtube videosu (dinov2)](https://www.youtube.com/watch?v=h3ij3F3cPIk) & [youtube videosu (clip)](https://www.youtube.com/watch?v=T9XSU0pKX2E) — **[teorik derinlik]** öz-denetimli görsel vakıf modellerinin mimari analizi
  3. **ai coffee break with letitia – vision transformers, clip, dino & siglip:** [youtube kanalı](https://www.youtube.com/@AICoffeeBreak) — görsel temsil öğreniminin hızlı ve anlaşılır özetleri
- **oku & repo (makale ve resmi kod tabanları — önem sırasıyla):**
  1. **dinov2: learning robust visual features without supervision (oquab et al. – meta ai):** [arxiv:2304.07193](https://arxiv.org/abs/2304.07193) · [demo & site](https://dinov2.metademolab.com/) · [github repo (facebookresearch/dinov2)](https://github.com/facebookresearch/dinov2) — **[görsel eşleştirme & derinlik için zirve]** ince ayar (fine-tuning) yapmadan bile derinlik kestirimi, görsel arama ve çapraz görünüm eşleştirmede (cross-view matching) mucizeler yaratan temel model
  2. **learning transferable visual models from natural language supervision – clip (radford et al. – openai):** [arxiv:2103.00020](https://arxiv.org/abs/2103.00020) & [github repo (mlfoundations/open_clip)](https://github.com/mlfoundations/open_clip) — açık kelime dağarcıklı (open-vocabulary) algılamanın temeli
  3. **sigmoid loss for language image pre-training – siglip (zhai et al. – google research):** [arxiv:2303.15343](https://arxiv.org/abs/2303.15343) — clip'in daha verimli ve modern halefi

#### 6.9 advanced vision research

- [ ] robust visual recognition
- [ ] domain generalization
- [ ] domain adaptation
- [ ] visual anomaly detection
- [ ] low-light vision
- [ ] night vision algorithms
- [ ] adverse weather perception
- [ ] motion blur robustness
- [ ] image super resolution
- [ ] image restoration
- [ ] video understanding
- [ ] temporal modeling
- [ ] event-based vision

**kaynaklar (önem ve çalışma sırasına göre):**

- **yt (yabancı video dersler — önem sırasıyla):**
  1. **prof. davide scaramuzza (rpg lab, uzh) – event-based vision & agile autonomous drones:** [youtube kanalı (robotics and perception group)](https://www.youtube.com/@ailabRPG/playlists) — **[ilk izlenecek – iha & yüksek hızlı görü]** milisaniye altı gecikmeli nöromorfik olay tabanlı kameralar (event cameras) ve yüksek hızlı otonom iha algılaması
  2. **cvpr / iccv / eccv workshop kayıtları (low-light, adverse weather & robustness):** [computer vision foundation youtube](https://www.youtube.com/@ComputerVisionFoundation) — sis, yağmur, gece görüşü ve hareket bulanıklığı altında çalışan sağlam (robust) görüş algoritmaları
- **oku & repo (makale ve kütüphaneler — önem sırasıyla):**
  1. **event-based vision: a survey (gallego, scaramuzza et al. – ieee tpami):** [arxiv:1904.08405 (ücretsiz pdf)](https://arxiv.org/pdf/1904.08405.pdf) — olay tabanlı kameraların ve algoritmalarının kapsamlı derleme makalesi
  2. **repo – openvinotoolkit/anomalib:** [github.com/openvinotoolkit/anomalib](https://github.com/openvinotoolkit/anomalib) — görsel anomali ve kusur tespiti (visual anomaly detection) için endüstriyel derin öğrenme kütüphanesi
  3. **hugging face trending papers & arxiv computer vision (**[**cs.cv**](https://arxiv.org/list/cs.CV/recent)**):** [huggingface.co/papers/trending](https://huggingface.co/papers/trending) · [arxiv.org/list/cs.cv/recent](https://arxiv.org/list/cs.CV/recent) — görüntü iyileştirme (image restoration), düşük ışık (low-light) ve süper çözünürlük sota makaleleri

---

### 02. applied vision – uygulamalı bilgisayarlı görü: ocr, poz, video ve uzaktan algılama

#### 38.1 ocr & document ai – optik karakter tanıma ve belge yapay zekâsı

- [ ] text detection (east, dbnet)
- [ ] text recognition (crnn, trocr)
- [ ] scene text recognition
- [ ] document layout analysis
- [ ] layoutlm and document transformers
- [ ] donut (ocr-free document understanding)
- [ ] table structure recognition
- [ ] handwriting recognition
- [ ] document vqa
- [ ] key information extraction
- [ ] tesseract, paddleocr, easyocr

#### 38.2 face & biometrics – yüz tanıma ve biyometri

- [ ] face detection (mtcnn, retinaface)
- [ ] face alignment and landmarks
- [ ] face recognition (facenet, arcface)
- [ ] verification vs identification
- [ ] liveness and anti-spoofing
- [ ] fingerprint and iris recognition
- [ ] gait recognition
- [ ] biometric privacy and regulation

#### 38.3 human understanding – insan poz, hareket ve niyet analizi

- [ ] 2d human pose estimation (openpose, hrnet, rtmpose)
- [ ] 3d human pose and mesh recovery (smpl)
- [ ] hand pose estimation
- [ ] gaze estimation
- [ ] action recognition
- [ ] gesture recognition
- [ ] crowd counting
- [ ] pedestrian intent and trajectory prediction
- [ ] human motion prediction
- [ ] motion capture

#### 38.4 video understanding – video anlama ve optik akış

- [ ] video classification (i3d, slowfast)
- [ ] video transformers (timesformer, vivit, videomae)
- [ ] temporal action localization
- [ ] video object segmentation
- [ ] video captioning and video qa
- [ ] deep optical flow (flownet, raft)
- [ ] video prediction
- [ ] frame interpolation
- [ ] long video understanding
- [ ] video compression basics (h.264, h.265)

#### 38.5 remote sensing & aerial imagery – uzaktan algılama ve hava/uydu görüntüsü analizi

- [ ] satellite and aerial image basics
- [ ] multispectral and hyperspectral imaging
- [ ] sar (synthetic aperture radar)
- [ ] thermal and infrared imaging
- [ ] aerial object detection (small and oriented objects)
- [ ] land cover segmentation
- [ ] change detection
- [ ] georeferencing and coordinate reference systems
- [ ] gis tools (qgis, gdal)
- [ ] aerial datasets (dota, visdrone, xview)
- [ ] geospatial foundation models
- [ ] uav imagery analytics

#### 38.6 captioning, grounding & visual reasoning – görsel konumlandırma ve akıl yürütme

- [ ] image captioning
- [ ] referring expression comprehension
- [ ] visual grounding (grounding dino)
- [ ] scene graph generation
- [ ] dense captioning
- [ ] visual reasoning benchmarks

#### 38.7 image generation & editing – görüntü üretimi ve düzenleme

- [ ] inpainting and outpainting
- [ ] image-to-image translation (pix2pix, cyclegan)
- [ ] style transfer
- [ ] controlnet
- [ ] lora and dreambooth for diffusion
- [ ] ip-adapter
- [ ] instruction-based image editing
- [ ] image matting
- [ ] deblurring and denoising
- [ ] colorization
- [ ] deepfake generation and detection

**kaynaklar (önem ve çalışma sırasına göre):**

- **tr:** [itü / odtü uzaktan algılama & cbs (gis) ders notları ve açık kaynak seminerleri](https://www.itu.edu.tr/) — koordinat referans sistemleri (crs), multispektral/sar görüntüleme ve hava fotoğrafçılığı temelleri.
- **yt:**
  1. **[ilk izlenecek — optik akış & video]** [princeton vision & robotics — raft: recurrent all-pairs field transforms for optical flow](https://github.com/princeton-vl/RAFT) — derin optik akış ve hareket analizi.
  2. **[uzaktan algılama & cbs]** [qgis & gdal spatial analysis tutorials (spatial thoughts / youtube)](https://www.youtube.com/@SpatialThoughts) — georeferanslama, koordinat dönüşümleri ve raster görüntü işleme.
- **oku & repo:**
  1. [mmrotate — openmmlab oriented object detection benchmark & toolbox (github)](https://github.com/open-mmlab/mmrotate) & [ultralytics yolo obb (oriented bounding boxes)](https://docs.ultralytics.com/tasks/obb/) — iha ve uydu görüntülerinde yönelimli (döndürülmüş kutulu) ve küçük nesne tespiti için temel kod depoları.
  2. [sahi — slicing aided hyper inference (github — fatih cagatay akyon)](https://github.com/obss/sahi) — yüksek çözünürlüklü iha/hava görüntülerinde küçük nesne tespitini (visdrone, dota, xview) dilimleyerek güçlendiren açık kaynak kütüphane.
  3. [torchgeo — microsoft geospatial deep learning library (github)](https://github.com/microsoft/torchgeo) — multispektral, hiperspektral, sar ve coğrafi koordinatlı veri setlerini pytorch ile işleme standardı.
  4. [paddleocr (github)](https://github.com/PaddlePaddle/PaddleOCR) & [mmpose (github)](https://github.com/open-mmlab/mmpose) & [groundingdino (github)](https://github.com/IDEA-Research/GroundingDINO) — ocr, insan poz kestirimi ve açık kelime dağarcıklı görsel konumlandırma araçları.
