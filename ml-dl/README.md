# machine learning and deep learning

engineering curriculum, mathematical representations, optimization engines, and curated resources for statistical learning, neural networks, reinforcement learning, bayesian inference, and multimodal models.

---

## architecture overview

```
[dataset: features, sensors & labels]
                  │
                  ▼
[loss landscape & objective formulation: cross-entropy / mse]
                  │
                  ▼
[computational graph & backpropagation: reverse autodiff]
                  │
                  ▼
[stochastic optimization: adam / sgd / learning rate schedules]
                  │
                  ▼
[trained representations: neural policies / feature encoders]
```

---

## complete checklist and resources

### 01. machine learning – makine öğrenmesi

#### 5.1 machine learning fundamentals

- [ ] what is machine learning?
- [ ] features and labels
- [ ] training, validation and test sets
- [ ] overfitting
- [ ] underfitting
- [ ] bias-variance tradeoff
- [ ] feature engineering
- [ ] data preprocessing
- [ ] normalization
- [ ] standardization
- [ ] cross validation
- [ ] model evaluation (precision, recall, f1, roc-auc)
- [ ] hyperparameter tuning

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **murat karakaya akademi (tedü) – makine öğrenmesi ve derin öğrenme uygulamaları:** [youtube kanalı](https://www.youtube.com/@MuratKarakayaAkademi) — uygulamalı türkçe makine öğrenmesi ve keras/python dersleri (doğrulanmış akademik kanal)
  2. **bilgisayar kavramları (şadi evren şeker) – makine öğrenmesi serisi:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — overfitting, cross-validation, precision/recall/f1 kavramlarının temel mantığı
  3. **kitap:** cemalettin kubat – yapay zeka temelleri ve algoritmaları
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **statquest with josh starmer – machine learning playlist:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **[ilk izlenecek]** bias-variance, roc-auc, cross-validation ve tüm temel ml kavramlarının görsel anlatımı
  2. **andrew ng – machine learning specialization (**[**deeplearning.ai**](http://DeepLearning.AI)**/ stanford):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI) — **[ana başlangıç dersi]** makine öğrenmesi mühendisliğine standart giriş kursu
  3. **caltech cs156 – learning from data (prof. yaser abu-mostafa):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLD63A284B7615313A) — **[teorik derinlik]** öğrenme teorisi (vc dimension, genelleme sınırları) için kapsamlı üniversite dersi
- **📖 oku & 💻 kütüphane (kitap ve dokümantasyon — önem sırasıyla):**
  1. **hands-on machine learning with scikit-learn, keras, and tensorflow (aurélien géron):** [github kod deposu](https://github.com/ageron/handson-ml3) & [o'reilly kitap sayfası](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — **[temel uygulama kitabı]** uçtan uca ml boru hattı (pipeline) kurmayı öğreten başvuru kitabı
  2. **scikit-learn official user guide:** [scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html) — veri ön işleme, metrikler ve doğrulama için resmi mühendislik rehberi
  3. **the elements of statistical learning (hastie, tibshirani, friedman – stanford):** [hastie.su.domains/elemstatlearn (ücretsiz pdf)](https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf) — istatistiksel öğrenmenin matematiksel referans kitabı
  4. **machine learning with pytorch and scikit-learn & mlxtend (sebastian raschka):** [kitap reposu (rasbt/machine-learning-book)](https://github.com/rasbt/machine-learning-book) · [mlxtend kütüphanesi (rasbt/mlxtend)](https://github.com/rasbt/mlxtend) — **[scikit-learn'den pytorch'a köprü & ml araç seti]** sebastian raschka'nın yazdığı; klasik ml'den pytorch'a geçiş kodları ile karar sınırlarını görselleştiren (plot_decision_regions), bias-variance ayrışımı yapan ve modelleri istatistiksel testlerle (mcnemar, t-test) kıyaslayan 5k+ yıldızlı resmi mlxtend kütüphanesi

#### 5.2 supervised learning

- [ ] linear regression
- [ ] logistic regression
- [ ] decision trees
- [ ] random forest
- [ ] gradient boosting
- [ ] xgboost
- [ ] lightgbm
- [ ] support vector machines (svm)
- [ ] k-nearest neighbors (k-nn)
- [ ] naive bayes

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları – sınıflandırma ve regresyon algoritmaları:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — svm, karar ağaçları, random forest, k-nn ve naive bayes'in türkçe özeti
  2. **veri bilimi okulu & mustafa vahit keskin (miuul):** [veri-bilimi-okulu](https://www.veribilimiokulu.com/) & [youtube kanalı](https://www.youtube.com/@Miuul) — denetimli öğrenme ve tablosal veri modelleme pratikleri
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **statquest with josh starmer – decision trees, random forest, xgboost & svm:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **[ilk izlenecek]** özellikle gradient boosting ve xgboost'un çalışma mekanizmasını dünyada en iyi anlatan seri
  2. **cornell cs4780 – machine learning for intelligent systems (prof. kilian weinberger):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS) — **[en iyi üniversite dersi]** k-nn, svm, kernel trick, karar ağaçları ve boosting'in tahtada matematiksel türetimi
- **📖 oku & 💻 doküman (önem sırasıyla):**
  1. **xgboost official documentation & tutorials:** [xgboost.readthedocs.io](https://xgboost.readthedocs.io/en/stable/) — tablosal verilerde endüstri standardı olan kütüphanenin resmi dokümanı
  2. **pattern recognition and machine learning – prml (christopher bishop):** [ücretsiz resmi pdf (microsoft research)](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) — **[referans kitap]** bayesci regresyon, svm ve olasılıksal sınıflandırmanın en derin matematiksel kitabı

#### 5.3 unsupervised learning

- [ ] k-means
- [ ] hierarchical clustering
- [ ] dbscan
- [ ] gaussian mixture models (gmm)
- [ ] principal component analysis (pca)
- [ ] t-sne
- [ ] umap
- [ ] anomaly detection
- [ ] dimensionality reduction

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **bilgisayar kavramları – kümeleme (k-means, hiyerarşik) ve boyut indirgeme (pca):** [youtube arama bağlantısı](https://www.youtube.com/results?search_query=bilgisayar+kavramlar%C4%B1+k-means+pca) — denetimsiz öğrenme algoritmalarının türkçe mantığı
  2. **mustafa vahit keskin (miuul / veri bilimi okulu):** [youtube kanalı](https://www.youtube.com/@Miuul) — veri bilimi ve kümeleme süreçleri
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **statquest – pca, k-means, dbscan, t-sne & umap:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **[ilk izlenecek]** boyut indirgeme ve kümeleme algoritmalarının adım adım görsel analizi
  2. **stanford cs229 – machine learning (unsupervised learning, k-means, em & pca):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) — **[ana akademik ders]** gaussian mixture models (gmm) ve expectation-maximization (em) türetimleri
  3. **victor lavrenko – clustering & em algorithm lectures:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLBv09BD7ez_4e9LtmK626Evn1ion6ynrt) — gmm ve kümeleme matematiği
- **📖 oku (kitap ve dokümanlar — önem sırasıyla):**
  1. **scikit-learn unsupervised learning user guide:** [scikit-learn.org/stable/unsupervised_learning.html](https://scikit-learn.org/stable/unsupervised_learning.html) — dbscan, gmm, pca ve anomaly detection kod örnekleri ve karşılaştırma tabloları
  2. **probabilistic machine learning: an introduction (kevin murphy – bölüm 20 & 21):** [probml.github.io/pml-book/book1.html](https://probml.github.io/pml-book/book1.html) — boyut indirgeme ve kümelemenin olasılıksal temelleri (ücretsiz pdf)

#### 5.4 deep learning

- [ ] perceptron
- [ ] artificial neural networks (ann)
- [ ] activation functions (relu, gelu, sigmoid, tanh)
- [ ] loss functions (mse, binary cross-entropy, categorical cross-entropy)
- [ ] forward propagation
- [ ] backpropagation
- [ ] gradient descent
- [ ] optimizers (sgd, momentum, rmsprop, adam, adamw)
- [ ] regularization ($l_1$, $l_2$ / weight decay)
- [ ] batch normalization
- [ ] layer normalization
- [ ] dropout
- [ ] weight initialization (he, xavier/glorot)
- [ ] learning rate scheduling

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **odtü ceng 501 – deep learning (prof. dr. sinan kalkan):** [resmi ders sayfası](https://kovan.ceng.metu.edu.tr/~sinan/) & [github ders deposu (sinankalkan/ceng501-spring2021)](https://github.com/sinankalkan/CENG501-Spring2021) — sinir ağları, backpropagation, optimizasyon ve düzenlileştirme (regularization) açık ders materyalleri
  2. **murat karakaya akademi – deep learning türkçe uygulamalar:** [youtube kanalı](https://www.youtube.com/@MuratKarakayaAkademi) — uygulamalı derin öğrenme temelleri
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **3blue1brown – neural networks & backpropagation:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **[ilk izlenecek]** yapay sinir ağlarının ve geri yayılımın (backpropagation) görsel matematiği
  2. **andrej karpathy – neural networks: zero to hero (micrograd & makemore):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — **[zorunlu kodlama serisi]** hazır kütüphane kullanmadan sıfırdan kendi autograd motorunu, backpropagation'ı ve batchnorm'u kodlama
  3. **nyu deep learning ds-ga 1008 (yann lecun & alfredo canziani):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq) — pytorch üzerinden derin öğrenmenin geometrik ve enerji tabanlı yorumu
- **📖 oku & 💻 interaktif kitaplar (önem sırasıyla):**
  1. **dive into deep learning (**[**d2l.ai**](http://d2l.ai)**– aston zhang, zachary lipton, mu li, alex smola):** [d2l.ai](https://d2l.ai/) — **[uygulamalı interaktif kitap]** her matematiksel formülün hemen altında çalışan pytorch kodu bulunan ücretsiz interaktif kitap
  2. **deep learning (ian goodfellow, yoshua bengio, aaron courville):** [deeplearningbook.org](https://www.deeplearningbook.org/) — alanın teorik referans kitabı (ücretsiz)

#### 5.5 neural network architectures

- [ ] multilayer perceptrons (mlp)
- [ ] convolutional neural networks (cnn)
- [ ] recurrent neural networks (rnn)
- [ ] long short-term memory (lstm)
- [ ] gated recurrent unit (gru)
- [ ] autoencoders
- [ ] variational autoencoders (vae)
- [ ] generative adversarial networks (gan)
- [ ] transformers
- [ ] vision transformers (vit)
- [ ] graph neural networks (gnn)
- [ ] neural fields

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe akademik kaynaklar):**
  1. **odtü ceng 501 (prof. dr. sinan kalkan) & ceng 783 (derin öğrenme özel konular):** [ceng 501 ders sayfası](https://user.ceng.metu.edu.tr/~emre/Fall2026-DeepLearning.html) & [github repo](https://github.com/sinankalkan/CENG501-Spring2021) — cnn, rnn, autoencoder, gan ve vision transformer (vit) mimarileri (not: ceng 783 odtü'de dönemlik açılan lisansüstü derin öğrenme ders kodudur; prof. dr. ilkay ulusoy odtü ee bünyesinde görüntü analizi/vision çalışmaları yürütmektedir)
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **stanford cs230 – deep learning (andrew ng):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) — **[ilk izlenecek]** cnn, rnn/lstm, autoencoder ve gan mimarilerinin mühendislik perspektifi
  2. **umar jamil – transformers, vision transformers (vit) &vae from scratch in pytorch:** [youtube kanalı](https://www.youtube.com/@umarjamilai) — **[sıfırdan mimari kodlama]** makalelerdeki diyagramları açıp satır satır pytorch ile sıfırdan kodlayan en iyi kanal
  3. **yannic kilcher – deep learning architecture paper reviews:** [youtube kanalı](https://www.youtube.com/@YannicKilcher) — temel mimari makalelerin satır satır teknik analizi
- **📖 oku (temel makaleler ve görsel incelemeler — önem sırasıyla):**
  1. [**distill.pub**](http://Distill.pub)**(visualizing deep learning):** [distill.pub](https://distill.pub/) — attention, cnn öznitelikleri ve graph neural networks (gnn) üzerine etkileşimli görsel makaleler
  2. **attention is all you need (vaswani et al., 2017):** [arxiv:1706.03762](https://arxiv.org/abs/1706.03762) — modern ai dünyasını başlatan orijinal transformer makalesi
  3. **an image is worth 16x16 words: transformers for image recognition at scale (dosovitskiy et al.):** [arxiv:2010.11929](https://arxiv.org/abs/2010.11929) — orijinal vision transformer (vit) makalesi

#### 5.6 model training & research

- [ ] dataset construction
- [ ] data augmentation
- [ ] training pipelines
- [ ] loss design
- [ ] optimizer selection
- [ ] learning rate scheduling
- [ ] hyperparameter search
- [ ] distributed training
- [ ] mixed precision training (fp16/bf16)
- [ ] gradient accumulation
- [ ] checkpointing
- [ ] experiment tracking (weights & biases, mlflow)
- [ ] ablation studies
- [ ] reproducibility
- [ ] model interpretability
- [ ] robustness evaluation

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **inzva ai – deep learning & applied ai study guides:** [inzva.com](https://inzva.com/) — türkiye'deki yapay zekâ araştırma topluluğunun çalışma notları
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **umar jamil – pytorch deep dives, mixed precision & distributed training:** [youtube kanalı](https://www.youtube.com/@umarjamilai) — eğitim döngüsü (training loop) optimizasyonu ve pytorch derinlikleri
  2. **pytorch official youtube channel – distributed training & profiling series:** [youtube kanalı](https://www.youtube.com/@PyTorch) — resmi pytorch mühendislerinden ddp, torchscript ve amp anlatımları
- **📖 oku (zorunlu mühendislik rehberleri — önem sırasıyla):**
  1. **a recipe for training neural networks (andrej karpathy blog):** [karpathy.github.io/2019/04/25/recipe](https://karpathy.github.io/2019/04/25/recipe/) — **[her model eğitiminden önce okunacak]** sinir ağı eğitirken yapılan sessiz hataları (silent bugs) yakalama ve adım adım model büyütme rehberi
  2. **pytorch automatic mixed precision (amp) recipe:** [pytorch.org/tutorials/recipes/recipes/amp_recipe.html](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html) — fp16/bf16 ile gpu bellek kullanımını yarıya indirip eğitimi 2–3 kat hızlandırma
  3. **weights & biases (w&b) documentation & mlops tutorials:** [docs.wandb.ai](https://docs.wandb.ai/) — deney takibi, hiperparametre araması (sweeps) ve ablation çalışmaları

#### 5.7 advanced machine learning

- [ ] self-supervised learning
- [ ] semi-supervised learning
- [ ] contrastive learning
- [ ] metric learning
- [ ] few-shot learning
- [ ] one-shot learning
- [ ] zero-shot learning
- [ ] domain adaptation
- [ ] domain generalization
- [ ] transfer learning
- [ ] continual learning
- [ ] active learning
- [ ] federated learning
- [ ] uncertainty estimation

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **odtü ceng 501 – self-supervised & meta learning bölümleri (prof. dr. sinan kalkan):** [ders sayfası](https://kovan.ceng.metu.edu.tr/~sinan/) — etiketsiz veriden temsil öğrenimi sunumları
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **yann lecun – self-supervised learning & energy-based models (nyu):** [youtube ders videoları](https://www.youtube.com/results?search_query=yann+lecun+self+supervised+learning) — **[ilk izlenecek]** etiketsiz görsel ve sensör verisinden dünya temsili öğrenmenin felsefesi ve matematiği
  2. **stanford cs330 – deep multi-task and meta learning (prof. chelsea finn):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLoROMvodv4rMC6zfYmnD7UG3LVvwaITY5) — **[robotik & az veri için kritik]** few-shot learning, domain adaptation ve continual learning için zirve ders
- **📖 oku (makale ve teknik bloglar — önem sırasıyla):**
  1. **lilian weng’s technical ml blog (openai):** [lilianweng.github.io](https://lilianweng.github.io/) — **[referans teknik blog]** contrastive learning, self-supervised learning, meta-learning ve active learning üzerine kapsamlı matematiksel özetler
  2. **a cookbook of self-supervised learning (balestriero, lecun et al. – meta ai):** [arxiv:2304.12210](https://arxiv.org/abs/2304.12210) — öz-denetimli öğrenme yöntemlerinin el kitabı
  3. **simclr: a simple framework for contrastive learning of visual representations (chen et al.):** [arxiv:2002.05709](https://arxiv.org/abs/2002.05709) — kontrastif görsel öğrenmenin temel makalesi

---

### 02. generative ai, llm & multimodal ai

#### 13.1 natural language processing (nlp)

- [ ] tokenization (bpe, wordpiece)
- [ ] text embeddings
- [ ] word embeddings (word2vec, glove)
- [ ] language modeling
- [ ] sequence modeling
- [ ] attention mechanism
- [ ] transformers
- [ ] encoder-decoder architectures
- [ ] bert
- [ ] gpt-style architectures

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **andrej karpathy – let's build the gpt tokenizer & let's build gpt from scratch:** [youtube videosu (gpt)](https://www.youtube.com/watch?v=kCc8FmEb1nY) & [youtube videosu (tokenizer)](https://www.youtube.com/watch?v=zduSFxRajkE) — **[ilk izlenecek]** bpe tokenization, self-attention ve gpt mimarisini sıfırdan pytorch ile kodlayarak öğrenme
  2. **stanford cs224n – natural language processing with deep learning (prof. christopher manning):** [youtube ders serisi](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) — **[ana akademik ders]** word2vec, sekans modelleri, bert ve transformer'ların dilsel temeli
- **📖 oku & 💻 canlı görselleştirme (etkileşimli araçlar ve kitaplar — önem sırasıyla):**
  1. **the illustrated transformer & the illustrated word2vec (jay alammar):** [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) — attention mekanizmasının dünyadaki en ünlü görsel anlatımı
  2. **transformer explainer (georgia tech polo club – chi 2026):** [poloclub.github.io/transformer-explainer](https://poloclub.github.io/transformer-explainer/) & [github repo (poloclub/transformer-explainer)](https://github.com/poloclub/transformer-explainer) — **[tarayıcıda canlı çalışan etkileşimli transformer görselleştirici]** tarayıcı içinde canlı bir gpt modelini çalıştırarak embedding, multi-head self-attention (q, k, v), layernorm ve softmax olasılıklarını etkileşimli olarak görselleştiren 9k+ yıldızlı interaktif eğitim aracı
  3. **speech and language processing, 3rd ed. (dan jurafsky & james h. martin – stanford):** [web.stanford.edu/~jurafsky/slp3 (ücretsiz pdf)](https://web.stanford.edu/~jurafsky/slp3/) — nlp alanının standart referans ders kitabı
  4. **build a large language model from scratch (sebastian raschka – manning publications):** [github repo (rasbt/llms-from-scratch)](https://github.com/rasbt/LLMs-from-scratch) & [kitap sayfası](https://www.manning.com/books/build-a-large-language-model-from-scratch) — **[sıfırdan adım adım llm ve transformer kodlama rehberi]** sebastian raschka'nın yazdığı; bpe tokenization, multi-head self-attention matrisleri, gpt mimarisi, ön-eğitim döngüsü, instruction tuning ve lora adaptasyonunu saf pytorch ile satır satır kodlatan 108k+ yıldızlı dünya standardı başucu deposu

#### 13.2 large language models (llm)

- [ ] transformer architecture
- [ ] pretraining
- [ ] instruction tuning
- [ ] supervised fine-tuning (sft)
- [ ] preference optimization (rlhf, dpo)
- [ ] quantization (gptq, awq, gguf)
- [ ] lora (low-rank adaptation)
- [ ] qlora
- [ ] parameter-efficient fine-tuning (peft)
- [ ] model evaluation
- [ ] inference optimization
- [ ] context windows
- [ ] kv cache

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **andrej karpathy – state of gpt & let's reproduce gpt-2 (124m):** [youtube videosu (state of gpt)](https://www.youtube.com/watch?v=bZQun8Y4L2A) & [youtube videosu (gpt-2)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **[ilk izlenecek]** pretraining, sft, rlhf aşamaları ve sıfırdan yüksek hızlı eğitim
  2. **umar jamil – coding llama 2 / llama 3, kv cache & lora from scratch in pytorch:** [youtube kanalı](https://www.youtube.com/@umarjamilai) — **[mimari kodlama]** rope, grouped-query attention (gqa), kv cache ve lora'nın satır satır pytorch implementasyonu
  3. **maxime labonne & sam witteveen – llm fine-tuning, quantization & engineering:** [sam witteveen youtube](https://www.youtube.com/@samwitteveenai) & [maxime labonne llm course (github)](https://github.com/mlabonne/llm-course) — qlora, dpo, gguf/awq nicemleme (quantization) ve model birleştirme
- **📖 oku & 💻 repo (makale ve endüstriyel kod tabanları — önem sırasıyla):**
  1. **repo – ggerganov/llama.cpp:** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) — **[c++ mühendisliği için temel repo]** büyük dil modellerinin hiçbir python bağımlılığı olmadan saf c/c++, simd (avx/neon) ve cuda çekirdekleriyle uç cihazlarda nasıl çalıştırıldığını gösteren açık kaynak proje
  2. **repo – vllm-project/vllm:** [docs.vllm.ai](https://docs.vllm.ai/) & [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) — pagedattention mimarisi ile yüksek verimli (high-throughput) llm sunumu
  3. **hugging face peft documentation & lora / dpo papers:** [huggingface.co/docs/peft](https://huggingface.co/docs/peft/index) · [lora (arxiv:2106.09685)](https://arxiv.org/abs/2106.09685) · [dpo (arxiv:2305.18290)](https://arxiv.org/abs/2305.18290)

#### 13.3 retrieval-augmented generation (rag)

- [ ] embedding models
- [ ] vector databases (milvus, qdrant, chroma)
- [ ] similarity search (cosine, inner product)
- [ ] faiss (facebook ai similarity search)
- [ ] chunking strategies
- [ ] retrieval strategies
- [ ] reranking (cross-encoders)
- [ ] hybrid search (bm25 + dense vectors)
- [ ] query expansion
- [ ] rag evaluation (ragas, trulens)
- [ ] agentic rag

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **langchain – rag from scratch series (18 kısa video):** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) — **[ilk izlenecek]** chunking, indexing, query translation, routing, hybrid search ve reranking adımlarının mühendislik özeti
  2. **sam witteveen – advanced rag, vector databases & reranking:** [youtube kanalı](https://www.youtube.com/@samwitteveenai) — üretim seviyesi rag boru hatları
- **📖 oku & 💻 repo (kütüphane ve makaleler — önem sırasıyla):**
  1. **faiss (facebook ai similarity search – c++ & python):** [faiss.ai](https://faiss.ai/) & [github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss) — **[hem rag hem görsel arama için kritik]** milyonlarca gömme vektörü (image/text embeddings) arasında milisaniyede en yakın komşu araması yapan c++/gpu kütüphanesi
  2. **llamaindex & qdrant documentation:** [docs.llamaindex.ai](https://docs.llamaindex.ai/) · [qdrant.tech/documentation](https://qdrant.tech/documentation/) — veri indeksleme ve rust tabanlı vektör veritabanı mimarisi
  3. **retrieval-augmented generation for knowledge-intensive nlp tasks (lewis et al.):** [arxiv:2005.11401](https://arxiv.org/abs/2005.11401) — orijinal rag makalesi

#### 13.4 ai agents

- [ ] tool calling / function calling
- [ ] planning (react, plan-and-solve)
- [ ] memory (short-term, long-term, semantic)
- [ ] agent workflows
- [ ] multi-agent systems
- [ ] agent evaluation
- [ ] workflow orchestration
- [ ] guardrails (nemo guardrails)
- [ ] observability (langsmith, phoenix)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. [**deeplearning.ai**](http://DeepLearning.AI)**& harrison chase – ai agents in langgraph:** [kurs sayfası](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) & [langchain youtube](https://www.youtube.com/@LangChain) — **[ilk izlenecek]** döngüsel durum grafikleri (state graphs), hafıza (memory) ve araç çağırma (tool calling) ile güvenilir ajan mimarisi
  2. **sam witteveen – agentic workflows & multi-agent systems:** [youtube kanalı](https://www.youtube.com/@samwitteveenai)
- **📖 oku & 💻 repo (makale ve çerçeveler — önem sırasıyla):**
  1. **llm powered autonomous agents (lilian weng blog):** [lilianweng.github.io/posts/2023-06-23-agent](https://lilianweng.github.io/posts/2023-06-23-agent/) — planning, memory ve tool use bileşenlerinin en net mimari özeti
  2. **react: synergizing reasoning and acting in language models (yao et al.):** [arxiv:2210.03629](https://arxiv.org/abs/2210.03629) — akıl yürütme ve eylem döngüsünün temel makalesi
  3. **microsoft autogen & langgraph documentation:** [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) · [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)

#### 13.5 generative models

- [ ] autoencoders
- [ ] variational autoencoders (vae)
- [ ] gans (generative adversarial networks)
- [ ] diffusion models (ddpm, ddim)
- [ ] flow matching
- [ ] autoregressive models
- [ ] generative modeling
- [ ] latent space modeling

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **outlier – diffusion models from scratch (math & intuition):** [youtube videosu](https://www.youtube.com/watch?v=HoKDTa5jHvg) — **[ilk izlenecek]** ileri ve geri difüzyon süreçlerinin (ddpm) görsel matematiği
  2. **umar jamil – coding stable diffusion from scratch in pytorch:** [youtube videosu](https://www.youtube.com/watch?v=ZBKpAp_6TGI) — **[sıfırdan kodlama]** vae, u-net, clip ve ddpm örnekleyicisini (sampler) satır satır pytorch ile birleştirme
  3. **arash vahdat (nvidia research) – generative ai & diffusion tutorials (cvpr):** [youtube sunumu](https://www.youtube.com/watch?v=c36lUUr864M) — vae, gan, normalizing flows ve score-based diffusion modellerinin karşılaştırmalı teorisi
- **📖 oku (referans makaleler — önem sırasıyla):**
  1. **what are diffusion models? (lilian weng):** [lilianweng.github.io/posts/2021-07-11-diffusion-models](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — difüzyon denklemlerinin türetimi
  2. **understanding diffusion models: a unified perspective (calvin luo):** [arxiv:2208.11970 (ücretsiz pdf)](https://arxiv.org/pdf/2208.11970.pdf) — elbo, vae ve skor eşleştirme arasındaki matematiksel bağı en temiz kuran 25 sayfalık rehber makale

#### 13.6 multimodal ai

- [ ] vision-language models (vlm)
- [ ] image-text alignment
- [ ] contrastive multimodal learning
- [ ] audio-language models
- [ ] video-language models
- [ ] multimodal embeddings
- [ ] cross-modal retrieval
- [ ] multimodal reasoning
- [ ] visual question answering (vqa)

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **umar jamil – coding paligemma / llava (vision-language models) from scratch in pytorch:** [youtube videosu](https://www.youtube.com/watch?v=vVaRhZXovbw) — **[ilk izlenecek – kodlama]** bir vision transformer (siglip/clip) ile bir dil modelini (gemma/llama) birleştirip görüntüyü anlayan vlm kodlama
  2. **yannic kilcher – llava, flamingo & multimodal paper reviews:** [youtube kanalı](https://www.youtube.com/@YannicKilcher) — görsel-dilsel hizalama mimarilerinin analizi
- **📖 oku & 💻 repo (makale ve kütüphaneler — önem sırasıyla):**
  1. **vision-language models explained (hugging face technical blog):** [huggingface.co/blog/vlms](https://huggingface.co/blog/vlms) — modern vlm mimarilerinin kapsamlı mühendislik rehberi
  2. **visual instruction tuning – llava (liu et al., neurips 2023):** [arxiv:2304.08485](https://arxiv.org/abs/2304.08485) & [github repo (haotian-liu/llava)](https://github.com/haotian-liu/LLaVA) — açık kaynak çok modlu modellerin temel makalesi ve kodu
  3. **nanovlm: minimal & fast vision-language model training (hugging face):** [github repo (huggingface/nanovlm)](https://github.com/huggingface/nanoVLM) — **[sıfırdan vlm eğitimi için en temiz pytorch kod tabanı]** andrej karpathy'nin nanogpt felsefesiyle hugging face tarafından geliştirilen; karmaşık kütüphane soyutlamaları olmadan, bir görsel kodlayıcı (siglip/vit) ile küçük bir dil modelini (smollm/qwen2) birleştirerek tüketici gpu'larında sıfırdan çok modlu vlm eğitmeyi ve ince ayar (fine-tuning) yapmayı adım adım öğreten 5k+ yıldızlı saf pytorch reposu

#### 13.7 vision-language-action (vla) & embodied ai

- [ ] vision-language-action models (vla)
- [ ] robot foundation models (rt-1, rt-2, openvla, octo)
- [ ] language-conditioned control & imitation learning (cliport, peract)
- [ ] language-guided planning & value learning (saycan, voxposer, code as policies, autotamp)
- [ ] open-vocabulary 3d scene representations & semantics (lerf, clip-fields, nlmap)
- [ ] 6d novel object pose tracking & geometrical priors (foundationpose, bundlesdf)
- [ ] language-assisted reinforcement learning (ellm, decimer, tril)
- [ ] predictive & generative world models for autonomy (gaia-1, video-language planning)
- [ ] embodied chain-of-thought & reasoning (inner monologue, embodiedgpt)
- [ ] zero-shot / open-vocabulary segmentation for robotics (fastsam, mobilesam, track anything)
- [ ] egocentric human-to-robot learning (egoverse, meta aria, openpi)
- [ ] parameter-efficient vla fine-tuning (lora, oft, action chunking)

**kaynaklar (önem ve çalışma sırasına göre):**

- **📖 oku, 💻 repo & literatür haritası (önem sırasıyla):**
  1. **awesome robotics foundation models (ijrr 2024 / stanford, uc berkeley, princeton, google deepmind):** [awesome-robotics-foundation-models (github)](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) & [arxiv:2312.07843](https://arxiv.org/abs/2312.07843) — **[en kapsamlı literatür ve kod arşivi]** robotik vakıf modelleri, vla, taklit öğrenmesi, 3b açık sözlüklü algılama, 6d pose kestirimi ve dünya modellerini bir araya getiren başvuru kütüphanesi
  2. **openvla & openvla-oft (stanford / uc berkeley):** [openvla.github.io](https://openvla.github.io/) · [openvla/openvla](https://github.com/openvla/openvla) & [moojink/openvla-oft](https://github.com/moojink/openvla-oft) — **[açık kaynak vla ve hızlı ince ayar hattı]** kamera görüntüsü + doğal dil komutunu doğrudan 7-dof robot eylemine dönüştüren açık kaynak 7b model ve stanford'un action chunking + orthogonal fine-tuning (oft) ile tek gpu'da hızlı çıkarım ve eğitim sağlayan resmi optimizasyon deposu
  3. **rt-2: vision-language-action models transfer web knowledge to robotic control (google deepmind):** [arxiv:2307.15818](https://arxiv.org/abs/2307.15818) — vla kavramını tanımlayan kurucu makale
  4. **voxposer: composable 3d value maps for robotic manipulation (stanford asl):** [voxposer.github.io](https://voxposer.github.io/) & [github repo](https://github.com/huangwl18/VoxPoser) — llm ve vlm kullanarak 3b uzayda robot yörüngesi için değer haritaları (value maps) sentezleme
  5. **foundationpose: unified 6d pose estimation and tracking (nvidia research):** [foundationpose.github.io](https://nvlabs.github.io/FoundationPose/) — model-free ve model-based yeni nesil 6d nesne duruş kestirimi ve takibi
  6. **gaia-1: a generative world model for autonomous driving (wayve):** [wayve.ai/thinking/gaia-1](https://wayve.ai/thinking/gaia-1/) — otonom sürüş için video, metin ve eylem tabanlı üretken dünya modeli
  7. **egoverse: egocentric data for robot learning (georgia tech rl2 lab):** [gatech-rl2/egoverse (github)](https://github.com/GaTech-RL2/EgoVerse) — **[insandan robota birinci şahıs öğrenme]** insanların taktığı meta aria akıllı gözlüklerden toplanan birinci şahıs (egocentric) el hareketlerini robot manipülasyon eylemlerine dönüştürüp physical intelligence $\pi_0$ (openpi) ve lerobot ile politika eğiten açık kaynak veri ve eğitim altyapısı
- **▶️ yt (yabancı video dersler & seminerler — önem sırasıyla):**
  1. **stanford robotics & embodied ai seminars:** [youtube kanalı (stanford asl / robotics)](https://www.youtube.com/results?search_query=stanford+robotics+seminar+vla+embodied+ai) — görsel algıyı doğrudan robot eklem/hareket komutlarına (action tokens) dönüştüren vla modellerinin seminerleri
  2. **google deepmind robotics & physical intelligence presentations:** [deepmind youtube](https://www.youtube.com/@GoogleDeepMind) — rt-1, rt-2 ve genel amaçlı robot vakıf modelleri teknik sunumları

---

### 03. data engineering & data science

#### 15.1 data fundamentals

- [ ] data types
- [ ] data cleaning
- [ ] missing values
- [ ] outlier detection
- [ ] data transformation
- [ ] data normalization
- [ ] exploratory data analysis (eda)
- [ ] statistical analysis
- [ ] data visualization (matplotlib, seaborn)

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **mustafa vahit keskin (miuul / veri bilimi okulu) – python ile veri analizi ve manipülasyonu:** [youtube kanalı](https://www.youtube.com/@Miuul) & [veri bilimi okulu](https://www.veribilimiokulu.com/) — pandas, numpy, keşifsel veri analizi (eda) ve eksik/aykırı veri temizliği
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **keith galli – complete python pandas data science tutorial:** [youtube videosu](https://www.youtube.com/watch?v=vmEHCJofslg) — **[ilk izlenecek]** 1 saatte gerçek bir veri seti üzerinde pandas ile tüm temel veri manipülasyonu işlemleri
- **📖 oku (yazarından ücretsiz başucu kitabı — önem sırasıyla):**
  1. **python for data analysis, 3rd ed. (wes mckinney – pandas kütüphanesinin kurucusu):** [wesmckinney.com/book (ücretsiz tam kitap)](https://wesmckinney.com/book/) — **[temel başvuru kaynağı]** numpy, pandas, veri temizleme ve zaman serileri için resmi açık erişim kitap
  2. **pandas official user guide:** [pandas.pydata.org/docs/user_guide/index.html](https://pandas.pydata.org/docs/user_guide/index.html)

#### 15.2 data science

- [ ] statistical learning
- [ ] predictive modeling
- [ ] feature engineering
- [ ] experimental design
- [ ] hypothesis testing (a/b testing)
- [ ] time series analysis
- [ ] anomaly detection
- [ ] causal inference
- [ ] model evaluation

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **mustafa vahit keskin (miuul / veri bilimi okulu) – özellik mühendisliği ve ölçümleme problemleri:** [youtube kanalı](https://www.youtube.com/@Miuul) — a/b testleri, hipotez testleri ve özellik çıkarımı
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **statquest with josh starmer – hypothesis testing, p-values & statistical modeling:** [youtube oynatma listesi](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) — deney tasarımı ve istatistiksel anlamlılık
- **📖 oku (başucu kitabı):**
  1. **practical statistics for data scientists, 2nd ed. (peter bruce, andrew bruce, peter gedeck):** [o'reilly kitap sayfası](https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/) & [github python kodları](https://github.com/gedeck/practical-statistics-for-data-scientists) — mühendisler için gereksiz teoriden arındırılmış, doğrudan python kodlu istatistik ve veri bilimi el kitabı

#### 15.3 data engineering

- [ ] sql
- [ ] relational databases
- [ ] database design
- [ ] postgresql
- [ ] nosql databases (mongodb, redis)
- [ ] data warehousing
- [ ] data lakes
- [ ] etl
- [ ] elt
- [ ] data pipelines
- [ ] apache spark
- [ ] apache kafka
- [ ] stream processing
- [ ] distributed data processing
- [ ] data quality
- [ ] data versioning

**kaynaklar (önem ve çalışma sırasına göre):**

- **🇹🇷 tr (türkçe kaynaklar):**
  1. **bora kaşmer – dağıtık sistemler, redis, kafka, rabbitmq ve veri mimarisi:** [youtube kanalı](https://www.youtube.com/@BoraKasmer) — gerçek zamanlı veri akışı (streaming) ve önbellekleme mimarileri
- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **seattle data guy – data engineering fundamentals & pipelines:** [youtube kanalı](https://www.youtube.com/@SeattleDataGuy) — etl/elt, postgresql, spark ve kafka boru hatlarına giriş
  2. **luke barousse – sql for data science & analytics:** [youtube kanalı](https://www.youtube.com/@LukeBarousse) — pratik sql sorgulama
- **📖 oku & 💻 pratik (önem sırasıyla):**
  1. **sqlbolt – learn sql with simple, interactive exercises:** [sqlbolt.com](https://sqlbolt.com/) — **[ilk yapılacak pratik]** tarayıcıda hızlıca sql temellerini bitir
  2. **designing data-intensive applications – ddia (martin kleppmann):** [dataintensive.net](https://dataintensive.net/) — **[temel sistem ve veri mimarisi kitabı]** veritabanları, indeksleme, replikasyon, bölümleme (sharding), kafka ve dağıtık sistemlerin çalışma prensiplerini anlatan referans kitap

#### 15.4 ai dataset engineering

- [ ] dataset collection
- [ ] data annotation
- [ ] dataset curation
- [ ] data augmentation (albumentations kütüphanesi)
- [ ] data balancing
- [ ] label quality
- [ ] data versioning (dvc)
- [ ] synthetic data (simulation-based, isaac sim)
- [ ] dataset bias
- [ ] dataset evaluation
- [ ] benchmark construction

**kaynaklar (önem ve çalışma sırasına göre):**

- **▶️ yt (yabancı video dersler — önem sırasıyla):**
  1. **roboflow – computer vision dataset curation, annotation & augmentation tutorials:** [youtube kanalı](https://www.youtube.com/@Roboflow) — **[ilk izlenecek]** kamera/iha görüntülerinden veri seti toplama, otomatik etiketleme (auto-labeling) ve kalite kontrolü
  2. **mit 6.s191 / lab – data-centric ai (cleanlab):** [youtube ders serisi](https://www.youtube.com/playlist?list=PL_1TbuIu65A8NTNuLutFoD87vbMl8GL8K) & [ders sitesi (dcai.csail.mit.edu)](https://dcai.csail.mit.edu/) — hatalı etiketleri (label noise) ve veri seti yanlılığını (bias) algoritmik olarak temizleme
- **📖 oku & 💻 kütüphane (önem sırasıyla):**
  1. **albumentations official documentation (fast image augmentation library):** [albumentations.ai/docs](https://albumentations.ai/docs/) & [github repo](https://github.com/albumentations-team/albumentations) — **[her cv projesinde kullanılacak]** bounding box, mask ve keypoint'leri bozmadan görüntü çoğaltma (augmentation) yapan endüstri standardı kütüphane
  2. **dvc (data version control) documentation:** [dvc.org/doc](https://dvc.org/doc) — büyük görüntü ve sensör veri setlerini git gibi versiyonlama aracı

---

### 04. reinforcement learning – pekiştirmeli öğrenme

#### 25.1 rl foundations – pekiştirmeli öğrenme temelleri

- [ ] agent, environment, state, action, reward
- [ ] return and discount factor
- [ ] markov decision processes (mdp)
- [ ] policy (deterministic / stochastic)
- [ ] state value function $v(s)$
- [ ] action value function $q(s,a)$
- [ ] bellman expectation equation
- [ ] bellman optimality equation
- [ ] exploration vs exploitation
- [ ] episodic vs continuing tasks
- [ ] partially observable mdp (pomdp)
- [ ] reward shaping
- [ ] credit assignment problem

#### 25.2 multi-armed bandits – çok kollu haydut problemleri

- [ ] $\varepsilon$-greedy
- [ ] upper confidence bound (ucb)
- [ ] thompson sampling
- [ ] contextual bandits
- [ ] linear bandits (linucb)
- [ ] regret analysis
- [ ] dueling bandits

#### 25.3 dynamic programming & tabular rl – dinamik programlama ve tablo tabanlı rl

- [ ] policy evaluation
- [ ] policy iteration
- [ ] value iteration
- [ ] monte carlo prediction and control
- [ ] temporal difference learning (td(0))
- [ ] sarsa
- [ ] q-learning
- [ ] expected sarsa
- [ ] n-step td
- [ ] td($\lambda$) and eligibility traces
- [ ] on-policy vs off-policy learning
- [ ] importance sampling
- [ ] dyna-q

#### 25.4 function approximation – fonksiyon yaklaşımı

- [ ] linear function approximation
- [ ] tile coding
- [ ] semi-gradient methods
- [ ] the deadly triad
- [ ] feature construction
- [ ] experience replay
- [ ] target networks

#### 25.5 deep value-based rl – değer tabanlı derin rl

- [ ] dqn
- [ ] double dqn
- [ ] dueling dqn
- [ ] prioritized experience replay
- [ ] noisy networks
- [ ] distributional rl (c51, qr-dqn)
- [ ] rainbow
- [ ] recurrent dqn (r2d2)

#### 25.6 policy gradient & actor-critic – politika gradyanı ve aktör-kritik yöntemler

- [ ] policy gradient theorem
- [ ] reinforce
- [ ] baselines and advantage function
- [ ] generalized advantage estimation (gae)
- [ ] a2c / a3c
- [ ] natural policy gradient
- [ ] trpo
- [ ] ppo
- [ ] ddpg
- [ ] td3
- [ ] sac (soft actor-critic)
- [ ] entropy regularization
- [ ] impala and v-trace

#### 25.7 model-based rl & planning – model tabanlı rl ve planlama

- [ ] learned dynamics models
- [ ] dyna architecture
- [ ] mbpo
- [ ] pets
- [ ] dreamer (v1–v3)
- [ ] muzero
- [ ] monte carlo tree search (mcts)
- [ ] alphago / alphazero
- [ ] latent dynamics models
- [ ] td-mpc
- [ ] model predictive path integral (mppi)

#### 25.8 offline rl & imitation – çevrimdışı rl ve taklit öğrenme

- [ ] offline (batch) rl
- [ ] distribution shift problem
- [ ] bcq, cql, iql
- [ ] decision transformer
- [ ] behavior cloning
- [ ] dagger
- [ ] gail
- [ ] inverse rl (maxent irl)
- [ ] preference-based rl
- [ ] offline-to-online fine-tuning

#### 25.9 exploration, hierarchical & safe rl – keşif, hiyerarşik ve güvenli rl

- [ ] count-based exploration
- [ ] intrinsic motivation (icm, rnd)
- [ ] hierarchical rl (options, feudal)
- [ ] goal-conditioned rl
- [ ] hindsight experience replay (her)
- [ ] skill discovery (diayn)
- [ ] curriculum learning
- [ ] meta-rl
- [ ] multi-task rl
- [ ] constrained mdp (cmdp)
- [ ] safe rl (cpo, lagrangian methods, shielding)

#### 25.10 multi-agent rl & game theory – çok etmenli rl ve oyun teorisi

- [ ] game theory basics (nash equilibrium, zero-sum games)
- [ ] self-play
- [ ] centralized training decentralized execution (ctde)
- [ ] maddpg
- [ ] qmix
- [ ] mappo
- [ ] population-based training
- [ ] counterfactual regret minimization (cfr)
- [ ] emergent communication

#### 25.11 rl for llms – dil modelleri için rl

- [ ] rlhf pipeline
- [ ] reward models
- [ ] ppo for language models
- [ ] grpo
- [ ] rl with verifiable rewards (rlvr)
- [ ] process vs outcome rewards
- [ ] rlaif / constitutional ai
- [ ] reward hacking

#### 25.12 rl engineering & benchmarks – rl mühendisliği ve ortamlar

- [ ] gymnasium
- [ ] stable-baselines3
- [ ] cleanrl
- [ ] rllib
- [ ] isaac lab
- [ ] deepmind control suite
- [ ] atari (ale)
- [ ] vectorized environments
- [ ] hyperparameter sensitivity
- [ ] reproducibility in rl
- [ ] reward debugging
- [ ] sample efficiency metrics

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (doğrulanmış kapsamlı türkçe akademik rl serisi yok; doğrudan yt 1. sıradan başla).
- ▶️ **yt:**
  1. **[ilk izlenecek — klasik rl temeli]** [david silver — reinforcement learning course (ucl / deepmind youtube)](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) — mdp, bellman denklemleri, td öğrenme ve politika gradyanlarının temel mimarisi.
  2. **[ana akademik ders — deep rl & robotik]** [uc berkeley cs285 — deep reinforcement learning (sergey levine)](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — ppo, sac, model-based rl, offline rl ve robotik kontrol için ana lisansüstü ders.
  3. **[ücretsiz uygulamalı kurs]** [hugging face deep rl course (huggingface.co)](https://huggingface.co/learn/deep-rl-course/unit0/introduction) — q-learning'den ppo ve sac'a adım adım kodlamalı modern eğitim.
- 📖 **oku & 💻 repo:**
  1. [richard s. sutton & andrew g. barto — reinforcement learning: an introduction, 2nd ed. (ücretsiz pdf)](http://incompleteideas.net/book/the-book-2nd.html) — tabular rl, bellman denklemleri ve fonksiyon yaklaşımının temel ders kitabı.
  2. [openai spinning up in deep rl (spinningup.openai.com)](https://spinningup.openai.com/en/latest/) — reinforce, trpo, ppo, ddpg, td3 ve sac algoritmalarının açık matematiksel ve kod rehberi.
  3. [cleanrl — single-file deep rl implementations (github)](https://github.com/vwxyzjn/cleanrl) — her rl algoritmasının tek bir okunabilir python dosyasında sıfırdan pytorch implementasyonu.
  4. [stable-baselines3 (github)](https://github.com/DLR-RM/stable-baselines3) & [gymnasium (farama foundation)](https://gymnasium.farama.org/) — endüstri ve araştırmada standart rl ortam ve algoritma kütüphaneleri.

---

### 05. probabilistic & bayesian machine learning – olasılıksal ve bayesçi makine öğrenmesi

#### 26.1 probabilistic graphical models – olasılıksal grafik modeller

- [ ] bayesian networks
- [ ] d-separation
- [ ] markov random fields (mrf)
- [ ] conditional independence
- [ ] factor graphs
- [ ] variable elimination
- [ ] belief propagation (sum-product)
- [ ] junction tree algorithm
- [ ] structure learning
- [ ] parameter learning
- [ ] dynamic bayesian networks

#### 26.2 sequence & latent variable models – dizi ve gizli değişken modelleri

- [ ] hidden markov models (hmm)
- [ ] forward-backward algorithm
- [ ] viterbi algorithm
- [ ] baum-welch (em for hmm)
- [ ] linear dynamical systems
- [ ] switching linear dynamical systems
- [ ] conditional random fields (crf)
- [ ] mixture models
- [ ] expectation-maximization (em)
- [ ] probabilistic pca
- [ ] factor analysis
- [ ] independent component analysis (ica)
- [ ] topic models (lda)

#### 26.3 approximate inference – yaklaşık çıkarım yöntemleri

- [ ] importance sampling
- [ ] rejection sampling
- [ ] markov chain monte carlo (mcmc)
- [ ] metropolis-hastings
- [ ] gibbs sampling
- [ ] hamiltonian monte carlo (hmc, nuts)
- [ ] langevin dynamics
- [ ] sequential monte carlo
- [ ] variational inference (elbo)
- [ ] mean-field approximation
- [ ] stochastic variational inference
- [ ] reparameterization trick
- [ ] laplace approximation
- [ ] expectation propagation

#### 26.4 gaussian processes – gauss süreçleri

- [ ] gp regression
- [ ] kernel functions (rbf, matérn, periodic)
- [ ] marginal likelihood and hyperparameter learning
- [ ] sparse gps (inducing points)
- [ ] gp classification
- [ ] deep kernel learning
- [ ] bayesian optimization with gps
- [ ] gps in robotics (dynamics learning, mapping)

#### 26.5 bayesian deep learning & uncertainty – bayesçi derin öğrenme ve belirsizlik kestirimi

- [ ] aleatoric vs epistemic uncertainty
- [ ] bayesian neural networks
- [ ] mc dropout
- [ ] deep ensembles
- [ ] swag
- [ ] calibration (ece, temperature scaling)
- [ ] conformal prediction
- [ ] out-of-distribution (ood) detection
- [ ] evidential deep learning
- [ ] selective prediction (reject option)
- [ ] uncertainty in detection and segmentation

#### 26.6 probabilistic programming – olasılıksal programlama

- [ ] pymc
- [ ] stan
- [ ] numpyro
- [ ] pyro
- [ ] bayesian workflow
- [ ] prior and posterior predictive checks
- [ ] model comparison (waic, loo-cv)
- [ ] hierarchical models

#### 26.7 causal inference & causal ml – nedensel çıkarım ve nedensel ml

- [ ] structural causal models (scm)
- [ ] causal dags
- [ ] do-calculus
- [ ] confounding
- [ ] backdoor and frontdoor criteria
- [ ] counterfactuals
- [ ] potential outcomes framework
- [ ] propensity scores
- [ ] instrumental variables
- [ ] difference-in-differences
- [ ] regression discontinuity
- [ ] causal discovery
- [ ] uplift modeling
- [ ] causal representation learning

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [atölye / akademik seminerler & cemgil lab (boğaziçi) — olasılıksal modelleme arşivleri](https://www.youtube.com/@taylancemgil) — bayesçi çıkarım, faktör grafları ve olasılıksal modelleme üzerine türkçe ders kayıtları.
- ▶️ **yt:**
  1. **[ilk izlenecek — pgm & bayesçi çıkarım]** [tübingen probabilistic machine learning course — philipp hennig (youtube)](https://www.youtube.com/playlist?list=PL05umP7R6ij1tHaOFY96m5uX3J21a6yNd) — gaussian processes, variational inference, mcmc ve olasılıksal grafik modeller.
  2. **[ana akademik ders — pgm]** [daphne koller — probabilistic graphical models specialization (coursera)](https://www.coursera.org/specializations/probabilistic-graphical-models) — bayes ağları, markov ağları, faktör grafları ve belief propagation.
- 📖 **oku & 💻 repo:**
  1. [kevin p. murphy — probabilistic machine learning: advanced topics (mit press, ücretsiz pdf)](https://probml.github.io/pml-book/book2.html) — bölüm 26'daki tüm konuların (pgm, gp, vi, mcmc, belirsizlik, nedensellik) ana referans kitabı.
  2. [frank dellaert & michael kaess — factor graphs for robot perception (foundations and trends in robotics pdf)](https://www.cs.cmu.edu/~kaess/pub/Dellaert17fnt.pdf) — bölüm 26.1 ile bölüm 10 (slam / gtsam) arasındaki doğrudan mühendislik köprüsü.
  3. [carl edward rasmussen & christopher k. i. williams — gaussian processes for machine learning (ücretsiz pdf)](https://gaussianprocess.org/gpml/) — gp regresyonu ve çekirdek fonksiyonları için temel kaynak.

---

### 06. advanced nlp & language technologies – ileri doğal dil işleme ve dil teknolojileri

#### 28.1 linguistics & text processing – dilbilim ve metin işleme

- [ ] morphology, syntax, semantics, pragmatics
- [ ] tokenization and sentence segmentation
- [ ] stemming and lemmatization
- [ ] text normalization (unicode)
- [ ] regular expressions
- [ ] spell correction
- [ ] language identification
- [ ] corpora and annotation schemes

#### 28.2 classical nlp models – klasik nlp modelleri

- [ ] bag of words
- [ ] tf-idf
- [ ] n-gram language models
- [ ] smoothing (kneser-ney)
- [ ] naive bayes for text
- [ ] latent semantic analysis (lsa)
- [ ] topic modeling (lda)
- [ ] hmm and crf for sequence tagging

#### 28.3 core nlp tasks – temel nlp görevleri

- [ ] part-of-speech (pos) tagging
- [ ] named entity recognition (ner)
- [ ] dependency parsing
- [ ] constituency parsing
- [ ] coreference resolution
- [ ] semantic role labeling
- [ ] word sense disambiguation
- [ ] relation extraction
- [ ] entity linking
- [ ] text classification
- [ ] sentiment and emotion analysis
- [ ] keyword and keyphrase extraction

#### 28.4 generation & seq2seq tasks – metin üretimi ve diziden diziye görevler

- [ ] machine translation (statistical → neural)
- [ ] decoding strategies (greedy, beam, top-k, top-p, temperature)
- [ ] back-translation
- [ ] extractive summarization
- [ ] abstractive summarization
- [ ] paraphrasing
- [ ] grammatical error correction
- [ ] data-to-text generation
- [ ] text style transfer

#### 28.5 question answering, ir & dialogue – soru cevaplama ve diyalog sistemleri

- [ ] extractive qa (squad)
- [ ] open-domain qa
- [ ] multi-hop qa
- [ ] table qa
- [ ] dense retrieval (dpr, colbert)
- [ ] task-oriented dialogue
- [ ] open-domain dialogue
- [ ] dialogue state tracking
- [ ] conversational agents

#### 28.6 multilingual, low-resource & turkish nlp – çok dilli ve türkçe nlp

- [ ] multilingual models (mbert, xlm-r)
- [ ] cross-lingual transfer
- [ ] low-resource language techniques
- [ ] agglutinative morphology
- [ ] turkish morphological analysis
- [ ] turkish tokenization challenges
- [ ] turkish corpora and benchmarks
- [ ] code-switching
- [ ] transliteration

#### 28.7 nlp evaluation – değerlendirme metrikleri

- [ ] bleu, rouge, meteor
- [ ] bertscore
- [ ] perplexity
- [ ] human evaluation and inter-annotator agreement
- [ ] llm-as-judge
- [ ] benchmarks (glue, superglue, mmlu)
- [ ] benchmark contamination

#### 28.8 nlp tooling – nlp araçları ve kütüphaneleri

- [ ] spacy
- [ ] nltk
- [ ] hugging face transformers
- [ ] hugging face datasets and tokenizers
- [ ] gensim
- [ ] stanza

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [zemberek-nlp — türkçe doğal dil işleme kütüphanesi (github)](https://github.com/ahmetaa/zemberek-nlp) & [boun-tabi / turkish nlp resources (github)](https://github.com/boun-tabi) — türkçe sondan eklemeli morfolojik analiz ve veri setleri.
- ▶️ **yt:**
  1. **[ana akademik ders]** [stanford cs224n — natural language processing with deep learning (christopher manning)](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) — klasik ve derin öğrenme tabanlı nlp mimarileri.
  2. **[pratik araçlar]** [hugging face llm & nlp course (huggingface.co)](https://huggingface.co/learn/nlp-course/chapter1/1) — transformers, tokenizers ve datasets kütüphanelerinin uygulamalı kullanımı.
- 📖 **oku & 💻 repo:**
  1. [dan jurafsky & james h. martin — speech and language processing, 3rd ed. (ücretsiz taslak pdf)](https://web.stanford.edu/~jurafsky/slp3/) — dilbilim, klasik nlp, dizi etiketleme, ayrıştırma ve anlambilimin temel referans kitabı.

---

### 07. speech, audio & music ai – ses, konuşma ve müzik yapay zekâsı

#### 29.1 audio & signal fundamentals – ses ve sinyal işleme temelleri

- [ ] sampling and quantization
- [ ] nyquist theorem
- [ ] waveform representation
- [ ] short-time fourier transform (stft)
- [ ] spectrogram
- [ ] mel scale and mel-spectrogram
- [ ] mfcc
- [ ] pitch estimation
- [ ] psychoacoustics
- [ ] audio codecs
- [ ] resampling

#### 29.2 automatic speech recognition (asr) – otomatik konuşma tanıma

- [ ] hmm-gmm systems
- [ ] dnn-hmm hybrid systems
- [ ] connectionist temporal classification (ctc)
- [ ] rnn-transducer (rnn-t)
- [ ] attention-based encoder-decoder
- [ ] conformer
- [ ] wav2vec 2.0 and hubert
- [ ] whisper
- [ ] streaming asr
- [ ] forced alignment
- [ ] keyword spotting
- [ ] word error rate (wer)

#### 29.3 text-to-speech & voice synthesis – metinden sese ve ses sentezi

- [ ] concatenative and parametric tts
- [ ] tacotron
- [ ] fastspeech
- [ ] neural vocoders (wavenet, hifi-gan)
- [ ] vits
- [ ] diffusion-based tts
- [ ] codec language model tts (vall-e)
- [ ] voice cloning
- [ ] voice conversion
- [ ] prosody and emotional speech
- [ ] speech-to-speech translation

#### 29.4 speaker & audio understanding – konuşmacı ve ses anlama

- [ ] speaker verification and identification
- [ ] speaker embeddings (x-vector, ecapa-tdnn)
- [ ] speaker diarization
- [ ] audio classification
- [ ] sound event detection
- [ ] acoustic scene classification
- [ ] audio captioning
- [ ] speech emotion recognition
- [ ] audio deepfake and anti-spoofing

#### 29.5 speech enhancement & source separation – ses iyileştirme ve kaynak ayırma

- [ ] noise suppression
- [ ] dereverberation
- [ ] acoustic echo cancellation
- [ ] beamforming
- [ ] microphone arrays
- [ ] direction of arrival (doa) estimation
- [ ] sound source localization (robot audition)
- [ ] source separation (conv-tasnet, demucs)

#### 29.6 music ai – müzik yapay zekâsı

- [ ] music information retrieval (mir)
- [ ] beat and tempo tracking
- [ ] chord recognition
- [ ] automatic music transcription
- [ ] music tagging
- [ ] symbolic music generation
- [ ] audio music generation

#### 29.7 audio-language & spoken llms – ses-dil modelleri

- [ ] neural audio codecs and tokenizers (encodec)
- [ ] audio-text models (clap)
- [ ] speech llms
- [ ] full-duplex voice dialogue
- [ ] real-time voice agents

#### 29.8 audio tooling – ses kütüphaneleri ve araçları

- [ ] librosa
- [ ] torchaudio
- [ ] kaldi
- [ ] espnet
- [ ] nvidia nemo
- [ ] speechbrain
- [ ] whisper.cpp
- [ ] moonshine (düşük gecikmeli canlı ses & edge asr)

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (doğrudan yt 1. sıradaki ses sinyal işleme serisinden başla).
- ▶️ **yt:**
  1. **[ilk izlenecek — ses sinyal işleme & derin öğrenme]** [valerio velardo — the sound of ai: audio signal processing for ml (youtube)](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0) — stft, spectrogram, mel-spectrogram, mfcc ve librosa uygulamaları.
- 📖 **oku & 💻 repo:**
  1. [hugging face audio course (huggingface.co)](https://huggingface.co/learn/audio-course/chapter0/introduction) — ses sınıflandırma, asr (whisper) ve tts modellerine uygulamalı giriş.
  2. [whisper.cpp (github)](https://github.com/ggerganov/whisper.cpp) & [speechbrain (github)](https://github.com/speechbrain/speechbrain) — c/c++ üzerinde uç cihazda çalışan konuşma tanıma ve pytorch tabanlı ses araç seti.
  3. **moonshine: speech-to-text for live voice agents (useful sensors / moonshine ai):** [github repo (moonshine-ai/moonshine)](https://github.com/moonshine-ai/moonshine) & [arxiv:2410.15608](https://arxiv.org/abs/2410.15608) — **[canlı ses ajanları ve edge robotik için düşük gecikmeli asr]** pete warden (tensorflow mobile / tinyml kurucusu) ekibinin geliştirdiği; openai whisper'ın 30 saniyelik sabit pencere kısıtını ortadan kaldıran, ses süresiyle orantılı işlem yaparak whisper'dan 5 kat daha hızlı çalışan, raspberry pi ve jetson gibi gömülü uç cihazlarda gerçek zamanlı sesli asistan ve robot sesli komut arayüzü sunan 11.4k+ yıldızlı c++/python konuşma tanıma modeli
  4. **stanford cs224s & common voice tr:** [stanford cs224s](https://www.youtube.com/results?search_query=stanford+cs224s+spoken+language+processing) · [mozilla common voice tr](https://commonvoice.mozilla.org/tr) — modern konuşma tanıma (asr), akustik modeller, ctc ve tts mimarilerinin akademik amfi dersi ve türkçe açık ses veri kümesi.

---

### 08. time series, forecasting & sequential data – zaman serileri, tahminleme ve sıralı veriler

#### 30.1 time series fundamentals – zaman serisi temelleri

- [ ] trend, seasonality, noise
- [ ] stationarity (adf, kpss tests)
- [ ] autocorrelation (acf, pacf)
- [ ] decomposition (stl)
- [ ] differencing
- [ ] resampling and irregular sampling
- [ ] missing value handling
- [ ] walk-forward validation
- [ ] data leakage in time series

#### 30.2 statistical models – istatistiksel modeller

- [ ] ar, ma, arma
- [ ] arima and sarima
- [ ] arimax
- [ ] exponential smoothing (ets, holt-winters)
- [ ] vector autoregression (var)
- [ ] state-space models and kalman smoothing
- [ ] garch (volatility modeling)
- [ ] cointegration
- [ ] spectral analysis

#### 30.3 machine learning for time series – zaman serileri için makine öğrenmesi

- [ ] lag and rolling window features
- [ ] gradient boosting for forecasting
- [ ] multi-step forecasting strategies (direct, recursive)
- [ ] quantile and probabilistic forecasting
- [ ] hierarchical forecasting

#### 30.4 deep learning for time series – zaman serileri için derin öğrenme

- [ ] rnn and lstm forecasting
- [ ] temporal convolutional networks (tcn)
- [ ] n-beats and n-hits
- [ ] deepar
- [ ] temporal fusion transformer
- [ ] informer and autoformer
- [ ] patchtst
- [ ] time series foundation models (timesfm, chronos)

#### 30.5 time series tasks – zaman serisi problemleri ve telemetri analizi

- [ ] anomaly detection
- [ ] change point detection
- [ ] time series classification (rocket, inceptiontime)
- [ ] dynamic time warping (dtw)
- [ ] time series clustering
- [ ] imputation
- [ ] human activity recognition (imu / wearables)
- [ ] predictive maintenance
- [ ] remaining useful life (rul)
- [ ] flight and telemetry data analysis

#### 30.6 evaluation – değerlendirme metrikleri

- [ ] mae, rmse
- [ ] mape, smape
- [ ] mase
- [ ] crps
- [ ] backtesting
- [ ] prediction intervals and coverage

#### 30.7 tooling – kütüphaneler ve araçlar

- [ ] statsmodels
- [ ] sktime
- [ ] darts
- [ ] gluonts
- [ ] nixtla ecosystem
- [ ] tsfresh

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [veri bilimi okulu / miuul — zaman serileri analizi giriş notları](https://www.veribilimiokulu.com/) — durağanlık, trend, mevsimsellik ve arima/sarima temelleri.
- ▶️ **yt:**
  1. **[ilk izlenecek]** [ritvikmath — time series talk playlist (youtube)](https://www.youtube.com/playlist?list=PLvcbYUQ5t0UHOLnBzl46_Q6QKtFgfMGc3) — acf, pacf, arma, arima, durum-uzay modelleri ve zaman serisi istatistiğinin sezgisel anlatımı.
- 📖 **oku & 💻 repo:**
  1. [rob j hyndman & george athanasopoulos — forecasting: principles and practice, 3rd ed. (otexts — ücretsiz online kitap)](https://otexts.com/fpp3/) — zaman serisi analizi, istatistiksel tahminleme, çapraz doğrulama ve metrikler için standart ders kitabı.
  2. [sktime (github)](https://github.com/sktime/sktime) & [darts — unit8 (github)](https://github.com/unit8co/darts) & [nixtla (github)](https://github.com/Nixtla) — zaman serisi sınıflandırma, anomali tespiti ve tahminleme için modern python kütüphaneleri.

---

### 09. recommender systems & information retrieval – öneri sistemleri ve bilgi erişimi

#### 31.1 recommender fundamentals – öneri sistemleri temelleri

- [ ] collaborative filtering (user-based, item-based)
- [ ] content-based filtering
- [ ] hybrid systems
- [ ] explicit vs implicit feedback
- [ ] cold start problem
- [ ] sparsity
- [ ] similarity metrics

#### 31.2 matrix factorization & classical models – matris çarpanlarına ayırma

- [ ] svd and svd++
- [ ] alternating least squares (als)
- [ ] bayesian personalized ranking (bpr)
- [ ] factorization machines
- [ ] implicit matrix factorization

#### 31.3 deep recommenders – derin öğrenme tabanlı öneri modelleri

- [ ] neural collaborative filtering
- [ ] wide & deep
- [ ] deepfm
- [ ] deep & cross network (dcn)
- [ ] two-tower models
- [ ] sequential recommenders (gru4rec, sasrec, bert4rec)
- [ ] graph-based recommenders (lightgcn, pinsage)
- [ ] generative recommenders
- [ ] large embedding tables

#### 31.4 retrieval & ranking pipeline – vektör arama ve sıralama hattı

- [ ] candidate generation
- [ ] approximate nearest neighbor search (hnsw, scann, ivf)
- [ ] ranking and re-ranking
- [ ] learning to rank (ranknet, lambdamart, listwise)
- [ ] multi-task ranking (mmoe)
- [ ] diversity and novelty

#### 31.5 evaluation & experimentation – değerlendirme ve a/b testleri

- [ ] precision@k, recall@k
- [ ] map, mrr
- [ ] ndcg
- [ ] offline vs online evaluation
- [ ] a/b testing
- [ ] interleaving
- [ ] off-policy evaluation

#### 31.6 biases & responsible recommendation – yanlılık ve sorumlu öneri

- [ ] position bias
- [ ] selection and popularity bias
- [ ] feedback loops
- [ ] fairness in recommendation
- [ ] filter bubbles
- [ ] bandit-based exploration

#### 31.7 search systems – arama sistemleri

- [ ] inverted index
- [ ] bm25
- [ ] query understanding
- [ ] learned sparse retrieval (splade)
- [ ] hybrid retrieval
- [ ] elasticsearch / opensearch / lucene
- [ ] pagerank
- [ ] web crawling

#### 31.8 tooling – araçlar ve kütüphaneler

- [ ] surprise
- [ ] implicit
- [ ] lightfm
- [ ] recbole
- [ ] torchrec

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (doğrudan yt 1. sıradan ve ir kitabından ilerle).
- ▶️ **yt:**
  1. **[ilk izlenecek — arama & bilgi erişimi]** [stanford cs276 — information retrieval and web search (christopher manning & pandu nayak)](https://www.youtube.com/playlist?list=PL6397E4B26D00A269) — ters indeks (inverted index), bm25, sıralama ve bilgi erişimi temelleri.
- 📖 **oku & 💻 repo:**
  1. [christopher d. manning, prabhakar raghavan & hinrich schütze — introduction to information retrieval (ücretsiz online kitap)](https://nlp.stanford.edu/IR-book/) — arama sistemleri ve bilgi erişiminin standart ders kitabı.
  2. [faiss — facebook ai similarity search (github)](https://github.com/facebookresearch/faiss) & [recbole (github)](https://github.com/RUCAIBox/RecBole) — vektör benzerlik araması (hnsw, ivf — görsel yer tanıma ve rag için de kullanılır) ve öneri sistemleri kütüphanesi.

---

### 10. advanced deep learning – ileri derin öğrenme: mimariler, ölçekleme ve teori

#### 32.1 efficient & alternative sequence architectures – verimli ve alternatif dizi mimarileri

- [ ] linear attention
- [ ] sparse and sliding-window attention
- [ ] multi-query and grouped-query attention
- [ ] positional encodings (rope, alibi)
- [ ] structured state space models (s4, s5)
- [ ] mamba (selective ssm)
- [ ] rwkv
- [ ] retnet
- [ ] hyena
- [ ] xlstm
- [ ] hybrid attention-ssm models
- [ ] mixture of experts (moe)
- [ ] expert routing and load balancing
- [ ] speculative decoding
- [ ] early exit networks

#### 32.2 scaling & training dynamics – ölçekleme yasaları ve eğitim dinamikleri

- [ ] scaling laws (kaplan, chinchilla)
- [ ] compute-optimal training
- [ ] emergent abilities debate
- [ ] grokking
- [ ] double descent
- [ ] loss landscape geometry
- [ ] sharpness and flat minima
- [ ] lottery ticket hypothesis
- [ ] critical batch size
- [ ] maximal update parametrization ($\mu$p)
- [ ] training instabilities and loss spikes
- [ ] advanced optimizers (lion, shampoo, muon, adafactor, lamb)

#### 32.3 deep learning theory – derin öğrenme teorisi

- [ ] universal approximation
- [ ] depth vs width expressivity
- [ ] neural tangent kernel (ntk)
- [ ] infinite-width limits
- [ ] implicit bias of gradient descent
- [ ] overparameterization
- [ ] information bottleneck
- [ ] signal propagation and initialization theory
- [ ] generalization bounds for neural networks

#### 32.4 representation learning – temsil öğrenme

- [ ] contrastive learning (infonce)
- [ ] byol and simsiam
- [ ] barlow twins and vicreg
- [ ] masked autoencoders (mae)
- [ ] jepa (i-jepa, v-jepa)
- [ ] disentangled representations
- [ ] vector quantization (vq-vae, vqgan)
- [ ] sparse autoencoders
- [ ] embedding geometry

#### 32.5 generative modeling theory – üretken modelleme teorisi

- [ ] energy-based models
- [ ] score matching
- [ ] sde formulation of diffusion
- [ ] normalizing flows
- [ ] rectified flow
- [ ] consistency models
- [ ] latent diffusion
- [ ] classifier-free guidance
- [ ] diffusion transformers (dit)
- [ ] diffusion distillation
- [ ] discrete diffusion
- [ ] gan training theory (wgan, stylegan)
- [ ] generative evaluation (fid, is, clipscore)

#### 32.6 training techniques – modern eğitim teknikleri

- [ ] mixup and cutmix
- [ ] label smoothing
- [ ] self-distillation
- [ ] exponential moving average (ema)
- [ ] stochastic weight averaging (swa)
- [ ] model soups
- [ ] sharpness-aware minimization (sam)
- [ ] gradient clipping
- [ ] gradient checkpointing
- [ ] pretraining objectives (mlm, clm, span corruption)

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (ileri derin öğrenme teorisi ve ölçekleme yasaları için doğrudan ingilizce orijinal ders ve kitapları takip et).
- ▶️ **yt:**
  1. **[ilk izlenecek — üretken modeller & temsil öğrenme]** [stanford cs236 — deep generative models (stefano ermon)](https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8) — normalizing flows, vae, gan, energy-based models ve score-based diffusion matematiği.
  2. **[derin öğrenme teorisi & temsiller]** [nyu deep learning sp21 — yann lecun & alfredo canziani (youtube)](https://www.youtube.com/playlist?list=PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq) — enerji tabanlı modeller, kontrastif öğrenme ve jepa felsefesi.
- 📖 **oku & 💻 repo:**
  1. [simon j.d. prince — understanding deep learning (mit press, 2023 — ücretsiz pdf)](https://udlbook.github.io/udlbook/) — modern derin öğrenme mimarileri, difüzyon, temsil öğrenme ve eğitim dinamikleri için güncel ders kitabı.
  2. [lilian weng’s blog — contrastive representation learning, diffusion models & transformer family](https://lilianweng.github.io/) — infonce, byol, mae, score/sde difüzyon ve rope/gqa/moe mimarilerinin matematiksel özetleri.
  3. [annotated s4 & mamba — sasha rush / albert gu](https://srush.github.io/annotated-s4/) — durum uzayı modellerinin (ssm) adım adım kod ve matematik açıklaması.

---

### 11. statistical learning theory & advanced classical ml – istatistiksel öğrenme teorisi ve ileri klasik ml

#### 33.1 statistical learning theory – istatistiksel öğrenme teorisi

- [ ] pac learning
- [ ] vc dimension
- [ ] rademacher complexity
- [ ] generalization bounds
- [ ] structural risk minimization
- [ ] no free lunch theorem
- [ ] concentration inequalities (hoeffding, chernoff, bernstein)
- [ ] sample complexity
- [ ] algorithmic stability
- [ ] online learning and regret
- [ ] boosting theory (adaboost margins)

#### 33.2 kernel methods – çekirdek yöntemleri

- [ ] kernel trick
- [ ] mercer’s theorem
- [ ] reproducing kernel hilbert space (rkhs)
- [ ] kernel svm
- [ ] kernel pca
- [ ] kernel ridge regression
- [ ] random fourier features
- [ ] nyström approximation
- [ ] maximum mean discrepancy (mmd)

#### 33.3 advanced classical ml – ileri klasik makine öğrenmesi

- [ ] bagging, boosting, stacking, blending
- [ ] catboost
- [ ] extra trees
- [ ] isolation forest
- [ ] feature selection (filter, wrapper, embedded)
- [ ] lasso, ridge, elastic net
- [ ] generalized linear models (glm)
- [ ] generalized additive models (gam)
- [ ] quantile regression
- [ ] survival analysis (kaplan-meier, cox)
- [ ] imbalanced learning (smote, cost-sensitive)
- [ ] learning with noisy labels
- [ ] semi-supervised methods (label propagation)
- [ ] multi-label and ordinal classification
- [ ] structured prediction
- [ ] metric learning

#### 33.4 manifold, spectral & sparse methods – manifold, spektral ve seyrek yöntemler

- [ ] isomap
- [ ] locally linear embedding (lle)
- [ ] laplacian eigenmaps
- [ ] spectral clustering
- [ ] non-negative matrix factorization (nmf)
- [ ] sparse coding and dictionary learning
- [ ] compressed sensing
- [ ] random projections

#### 33.5 advanced optimization for ml – makine öğrenmesi için ileri optimizasyon

- [ ] convergence rates (smooth, strongly convex)
- [ ] momentum and nesterov acceleration
- [ ] adaptive methods theory
- [ ] quasi-newton (l-bfgs)
- [ ] natural gradient and k-fac
- [ ] proximal methods
- [ ] admm
- [ ] coordinate descent
- [ ] variance reduction (svrg)
- [ ] non-convex optimization and saddle points
- [ ] distributed and federated optimization (fedavg)
- [ ] bilevel optimization
- [ ] zeroth-order optimization

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [prof. dr. ethem alpaydın — yapay öğrenme (kitap) & boğaziçi ders notları](https://www.boun.edu.tr/) — klasik makine öğrenmesi, vc boyutu, çekirdek yöntemleri ve topluluk (ensemble) algoritmalarının türkçe temel kaynağı.
- ▶️ **yt:**
  1. **[ilk izlenecek — öğrenme teorisi & vc boyutu]** [caltech cs156 — learning from data (yaser abu-mostafa youtube)](https://www.youtube.com/playlist?list=PLD63A284B7615313A) — pac öğrenme, hoeffding eşitsizliği, vc boyutu, genelleme sınırları ve düzenlileştirme teorisi.
- 📖 **oku & 💻 repo:**
  1. [trevor hastie, robert tibshirani & jerome friedman — the elements of statistical learning (esl, ücretsiz pdf)](https://hastie.su.domains/ElemStatLearn/) — lasso/ridge, gam, çekirdek yöntemleri, boosting ve spektral yöntemlerin temel referans kitabı.
  2. [shai shalev-shwartz & shai ben-david — understanding machine learning: from theory to algorithms (ücretsiz pdf)](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) — pac, vc boyutu, rademacher karmaşıklığı ve istatistiksel öğrenme teorisi.
  3. [stephen boyd & lieven vandenberghe — convex optimization (stanford ücretsiz pdf)](https://web.stanford.edu/~boyd/cvxbook/) — ileri optimizasyon, l-bfgs, admm ve yakınsama analizleri.

---

### 12. ai safety, interpretability, fairness & governance – yapay zekâ güvenliği, açıklanabilirlik ve yönetişim

#### 34.1 explainable ai (xai) – açıklanabilir yapay zekâ

- [ ] saliency maps
- [ ] grad-cam
- [ ] integrated gradients
- [ ] shap
- [ ] lime
- [ ] permutation importance
- [ ] partial dependence and ice plots
- [ ] attention visualization
- [ ] probing classifiers
- [ ] concept-based explanations (tcav)
- [ ] counterfactual explanations
- [ ] influence functions
- [ ] faithfulness evaluation of explanations

#### 34.2 mechanistic interpretability – mekanistik yorumlanabilirlik

- [ ] circuits
- [ ] features and superposition
- [ ] sparse autoencoders for features
- [ ] activation patching
- [ ] logit lens
- [ ] induction heads
- [ ] steering vectors / representation engineering
- [ ] model editing (rome, memit)

#### 34.3 fairness & bias – adillik ve yanlılık analizi

- [ ] sources of bias
- [ ] group fairness (demographic parity, equalized odds)
- [ ] individual fairness
- [ ] fairness impossibility results
- [ ] bias mitigation (pre-, in-, post-processing)
- [ ] dataset and representation bias
- [ ] fairness in vision and language models
- [ ] fairlearn and aif360

#### 34.4 alignment & frontier ai safety – hizalanma ve ileri ai güvenliği

- [ ] specification gaming
- [ ] reward hacking
- [ ] goal misgeneralization
- [ ] inner vs outer alignment
- [ ] scalable oversight
- [ ] constitutional ai
- [ ] debate and amplification
- [ ] deceptive alignment
- [ ] dangerous capability evaluations
- [ ] red teaming
- [ ] model cards and system cards

#### 34.5 safety-critical & robust ai – emniyet kritik ve dayanıklı sistemler

- [ ] distribution shift and ood robustness
- [ ] formal verification of neural networks
- [ ] certified robustness
- [ ] runtime monitoring and safety monitors
- [ ] functional safety (iso 26262, iec 61508)
- [ ] sotif (iso 21448)
- [ ] aviation software standards (do-178c)
- [ ] autonomous system assurance (ul 4600)
- [ ] fail-safe and fail-operational design
- [ ] simulation-based safety testing
- [ ] safe rl and safe control (control barrier functions)

#### 34.6 responsible ai & governance – sorumlu ai, mevzuat ve etik

- [ ] eu ai act
- [ ] nist ai risk management framework
- [ ] iso/iec 42001
- [ ] kvkk and gdpr
- [ ] copyright and data licensing
- [ ] datasheets for datasets
- [ ] algorithmic accountability and auditing
- [ ] dual-use risks
- [ ] ethics of autonomous weapons
- [ ] environmental cost of ai (green ai)
- [ ] human oversight (human-in-the-loop)

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** [kvkk — yapay zeka alanında kişisel verilerin korunmasına dair rehber (kvkk.gov.tr)](https://www.kvkk.gov.tr/) — türkiye'de veri gizliliği ve mevzuat çerçevesi.
- ▶️ **yt:**
  1. **[ilk izlenecek — güvenli kontrol & cbf]** [aaron ames (caltech) — control barrier functions for safety-critical autonomous systems (youtube)](https://www.youtube.com/watch?v=ZC3T_P_8xpE) — robotik ve otonom araçlarda matematiksel güvenlik garantileri (cbf).
  2. **[ai safety & dayanıklılık]** [dan hendrycks — introduction to ai safety, ethics, and society (youtube & course)](https://www.aisafetybook.com/) — ood dayanıklılığı, hizalanma, emniyet mühendisliği ve yönetişim.
- 📖 **oku & 💻 repo:**
  1. [christoph molnar — interpretable machine learning (ücretsiz online kitap)](https://christophm.github.io/interpretable-ml-book/) — shap, lime, permutation importance, saliency ve grad-cam için standart uygulama rehberi.
  2. [captum — model interpretability for pytorch (github)](https://github.com/pytorch/captum) & [pytorch-grad-cam (github)](https://github.com/jacobgil/pytorch-grad-cam) — görsel ve derin modellerde açıklanabilirlik analiz araçları.
  3. [ul 4600 & iso 21448 (sotif) overview — edge case research](https://users.ece.cmu.edu/~koopman/ul4600/) — otonom araçlar ve iha'larda fonksiyonel güvenlik (iso 26262), algı belirsizliği güvenliği (sotif) ve do-178c standartlarına mühendislik bakışı.

---

### 13. adversarial ml, security & privacy – çekişmeli makine öğrenmesi, güvenlik ve gizlilik

#### 35.1 adversarial attacks – çekişmeli saldırılar ve sensör aldatma

- [ ] evasion attacks
- [ ] fgsm
- [ ] pgd
- [ ] carlini-wagner attack
- [ ] autoattack
- [ ] black-box and transfer attacks
- [ ] universal adversarial perturbations
- [ ] physical-world attacks (adversarial patches)
- [ ] attacks on detection and segmentation
- [ ] sensor spoofing (gps, lidar, camera)
- [ ] attacks on speech models
- [ ] attacks on rl agents

#### 35.2 defenses – savunma yöntemleri

- [ ] adversarial training
- [ ] randomized smoothing
- [ ] input preprocessing defenses
- [ ] adversarial example detection
- [ ] certified defenses
- [ ] gradient masking pitfalls
- [ ] robustness benchmarks (robustbench)

#### 35.3 data & model attacks – veri zehirleme ve model saldırıları

- [ ] data poisoning
- [ ] backdoor / trojan attacks
- [ ] model extraction
- [ ] model inversion
- [ ] membership inference
- [ ] training data extraction
- [ ] supply chain attacks (malicious model files)
- [ ] model watermarking
- [ ] model fingerprinting

#### 35.4 llm & agent security – dil modeli ve etmen güvenliği

- [ ] prompt injection (direct and indirect)
- [ ] jailbreaks
- [ ] data exfiltration via tools
- [ ] agent hijacking
- [ ] rag poisoning
- [ ] excessive agency
- [ ] guardrails and output filtering
- [ ] owasp top 10 for llm applications
- [ ] deepfake and synthetic media detection
- [ ] content provenance (c2pa)

#### 35.5 privacy-preserving ml – gizlilik koruyucu makine öğrenmesi

- [ ] differential privacy (dp-sgd)
- [ ] federated learning
- [ ] secure aggregation
- [ ] homomorphic encryption
- [ ] secure multi-party computation
- [ ] trusted execution environments
- [ ] split learning
- [ ] machine unlearning
- [ ] anonymization (k-anonymity)

#### 35.6 secure ai engineering – güvenli yapay zekâ mühendisliği

- [ ] threat modeling for ml (stride, mitre atlas)
- [ ] mlsecops
- [ ] secure boot and secure ota for edge devices
- [ ] model encryption on edge
- [ ] dependency and package vulnerabilities

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (doğrudan aşağıdaki pratik eğitim ve standart kütüphanelerden ilerle).
- ▶️ **yt:**
  1. **[ilk izlenecek — adversarial robustness]** [zico kolter & aleksander madry — adversarial robustness: theory and practice (neurips tutorial)](https://adversarial-ml-tutorial.org/) — fgsm, pgd, adversarial training ve sertifikalı dayanıklılık matematiği ve pytorch kodu.
- 📖 **oku & 💻 repo:**
  1. [robustbench (github & leaderboard)](https://github.com/RobustBench/robustbench) & [autoattack (github)](https://github.com/fra31/auto-attack) — görüntü modellerinin çekişmeli (adversarial) ve bozulma dayanıklılığını ölçen standart kıyaslama araçları.
  2. [adversarial robustness toolbox (art) — linux foundation ai (github)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) — sınıflandırma ve nesne tespiti modellerine yönelik saldırı (yama, spoofing) ve savunma kütüphanesi.
  3. [mitre atlas (atlas.mitre.org)](https://atlas.mitre.org/) & [owasp top 10 for llm applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — yapay zeka sistemleri için tehdit modelleme matrisi.

---

### 14. automl, evolutionary computation & optimization heuristics – automl, evrimsel hesaplama ve sezgisel optimizasyon

#### 36.1 automl & hyperparameter optimization – otomatik ml ve hiperparametre optimizasyonu

- [ ] grid and random search
- [ ] bayesian optimization (tpe)
- [ ] hyperband and asha
- [ ] bohb
- [ ] population-based training
- [ ] optuna
- [ ] ray tune
- [ ] neural architecture search (nas)
- [ ] darts and one-shot nas
- [ ] hardware-aware nas (once-for-all)
- [ ] autogluon, auto-sklearn, flaml

#### 36.2 evolutionary computation – evrimsel hesaplama

- [ ] genetic algorithms
- [ ] genetic programming
- [ ] evolution strategies (cma-es)
- [ ] differential evolution
- [ ] neuroevolution (neat)
- [ ] quality-diversity (map-elites)
- [ ] multi-objective optimization (nsga-ii)
- [ ] co-evolution
- [ ] symbolic regression
- [ ] open-ended evolution

#### 36.3 swarm & bio-inspired optimization – sürü ve biyo-esinli optimizasyon

- [ ] particle swarm optimization (pso)
- [ ] ant colony optimization
- [ ] artificial bee colony
- [ ] simulated annealing
- [ ] tabu search
- [ ] memetic algorithms
- [ ] artificial immune systems
- [ ] cellular automata
- [ ] artificial life

#### 36.4 fuzzy logic & soft computing – bulanık mantık ve esnek hesaplama

- [ ] fuzzy sets and membership functions
- [ ] fuzzy inference (mamdani, sugeno)
- [ ] fuzzy control
- [ ] anfis
- [ ] rough sets
- [ ] neuro-fuzzy systems
- [ ] type-2 fuzzy systems

#### 36.5 combinatorial & operations research optimization – kombinatoryal optimizasyon ve yöneylem araştırması

- [ ] linear and integer programming (milp)
- [ ] constraint programming
- [ ] branch and bound
- [ ] traveling salesman problem (tsp)
- [ ] vehicle routing problem (vrp)
- [ ] scheduling problems
- [ ] google or-tools
- [ ] neural combinatorial optimization
- [ ] learning to optimize

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (uygulamada doğrudan optuna ve google or-tools dokümantasyonunu kullan).
- ▶️ **yt:**
  1. **[automl & hpo]** [automl seminar series & freiburg/hannover automl lectures (frank hutter — youtube)](https://www.youtube.com/@automl-freiburg-edu) — bayesçi optimizasyon, hyperband, bohb ve nas temelleri.
- 📖 **oku & 💻 repo:**
  1. [optuna — hyperparameter optimization framework (optuna.org & github)](https://github.com/optuna/optuna) — derin öğrenme deneylerinde tpe ve budama (pruning) tabanlı hiperparametre optimizasyonu standardı.
  2. [google or-tools — combinatorial optimization (developers.google.com)](https://developers.google.com/optimization) — rotalama (vrp/tsp), çizelgeleme ve tamsayılı programlama (milp) için c++/python çözücüsü.
  3. [pycma — cma-es implementation (github)](https://github.com/CMA-ES/pycma) — türevsiz sürekli optimizasyon ve robotik yörünge/kontrol parametre araması için evrim stratejisi kütüphanesi.

---

### 15. neuroscience-inspired, neuromorphic & cognitive ai – nörobilim esinli, nöromorfik ve bilişsel yapay zekâ

#### 37.1 computational neuroscience basics – hesaplamalı sinirbilim temelleri

- [ ] neuron models (hodgkin-huxley, lif, izhikevich)
- [ ] synaptic plasticity (hebbian, stdp)
- [ ] neural coding (rate, temporal, population)
- [ ] hopfield networks
- [ ] boltzmann machines
- [ ] predictive coding
- [ ] free energy principle and active inference
- [ ] hippocampus and memory models
- [ ] dendritic computation

#### 37.2 spiking neural networks & neuromorphic computing – darbeli sinir ağları ve nöromorfik hesaplama

- [ ] spiking neural networks (snn)
- [ ] surrogate gradient training
- [ ] ann-to-snn conversion
- [ ] event-driven processing
- [ ] snntorch, norse, brian2
- [ ] neuromorphic chips (loihi, spinnaker)
- [ ] memristors and in-memory computing

#### 37.3 cognitive science & agi concepts – bilişsel bilim ve genel yapay zekâ kavramları

- [ ] symbolic vs connectionist debate
- [ ] compositionality and systematic generalization
- [ ] intuitive physics
- [ ] theory of mind
- [ ] common sense reasoning
- [ ] developmental and curiosity-driven learning
- [ ] embodied cognition
- [ ] memory-augmented networks (ntm, dnc)
- [ ] catastrophic forgetting
- [ ] measuring intelligence (arc-agi)

#### 37.4 human-ai interaction – insan-yapay zekâ etkileşimi ve paylaşımlı otonomi

- [ ] human-in-the-loop ml
- [ ] interactive machine learning
- [ ] trust calibration
- [ ] shared autonomy
- [ ] social and assistive robot interaction
- [ ] affective computing
- [ ] gesture and gaze interfaces

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (nöromorfik hesaplama ve snn — özellikle bölüm 19.4 event camera ile birleştiğinde — aşağıdaki dokümantasyon üzerinden takip edilir).
- ▶️ **yt:**
  1. **[hesaplamalı sinirbilim]** [neuromatch academy — computational neuroscience course (youtube & neuromatch.io)](https://compneuro.neuromatch.io/) — nöron modelleri, kodlama ve beyin esinli hesaplama.
- 📖 **oku & 💻 repo:**
  1. [jason k. eshraghian — snntorch tutorials: deep learning with spiking neural networks (snntorch.readthedocs.io)](https://snntorch.readthedocs.io/en/latest/tutorials/index.html) — pytorch üzerinde spiking neural networks (snn) ve vekil gradyan (surrogate gradient) eğitimi.
  2. [wulfram gerstner et al. — neuronal dynamics: from single neurons to networks and models of cognition (epfl ücretsiz online kitap)](https://neuronaldynamics.epfl.ch/) — lif, hodgkin-huxley ve stdp modelleri için temel referans.
  3. **artem kirsanov & active inference:** [artem kirsanov (youtube)](https://www.youtube.com/@ArtemKirsanov) · [active inference (mit press)](https://mitpress.mit.edu/9780262045353/) — hesaplamalı sinirbilim, nöron modelleri (hodgkin-huxley, lif) ve biyolojik sistemler ile otonom robotların serbest enerji prensibiyle (active inference) karar verme mekanizmasının görsel ve matematiksel temeli.

---

### 16. ai for healthcare, biology & science – sağlık, biyoloji ve bilim için yapay zekâ

#### 39.1 medical imaging ai – tıbbi görüntüleme yapay zekâsı

- [ ] modalities (x-ray, ct, mri, ultrasound, pathology)
- [ ] dicom and nifti formats
- [ ] medical image segmentation (nnu-net)
- [ ] medical image classification and detection
- [ ] image registration
- [ ] 3d medical networks
- [ ] whole-slide image analysis
- [ ] medical foundation models
- [ ] evaluation metrics (dice, hd95)
- [ ] regulatory pathways (ce, fda, samd)
- [ ] monai

#### 39.2 clinical & health data ai – klinik veri ve biyosinyal analizi

- [ ] electronic health record (ehr) modeling
- [ ] clinical nlp
- [ ] ecg and eeg signal analysis
- [ ] wearable sensor data
- [ ] clinical risk prediction
- [ ] clinical validation of ml models
- [ ] health data privacy (kvkk, hipaa)

#### 39.3 bioinformatics & genomics – biyoenformatik ve genomik

- [ ] sequence alignment (blast)
- [ ] variant calling
- [ ] gene expression analysis
- [ ] single-cell analysis
- [ ] dna and rna language models
- [ ] genome-wide association studies (gwas)
- [ ] biological databases

#### 39.4 structural biology & drug discovery – yapısal biyoloji ve ilaç keşfi

- [ ] protein structure prediction (alphafold)
- [ ] protein language models (esm)
- [ ] protein design (rfdiffusion)
- [ ] molecular graph neural networks
- [ ] molecular generation
- [ ] molecular docking
- [ ] qsar and admet prediction
- [ ] cheminformatics (rdkit)
- [ ] equivariant networks (egnn, se(3)-transformers)

#### 39.5 scientific machine learning – bilimsel makine öğrenmesi ve fizik bilgili ağlar

- [ ] physics-informed neural networks (pinns)
- [ ] neural operators (fno, deeponet)
- [ ] surrogate modeling
- [ ] weather and climate models (graphcast)
- [ ] materials discovery
- [ ] learned physics simulators
- [ ] equation discovery (sindy)
- [ ] digital twins

#### 39.6 other application domains – diğer sektörel uygulama alanları

- [ ] agriculture ai (crop disease, yield prediction)
- [ ] energy ai (load forecasting, smart grid)
- [ ] industrial ai (predictive maintenance, quality control)
- [ ] cybersecurity ai (intrusion and malware detection)
- [ ] education ai (adaptive learning, tutoring)
- [ ] legal nlp

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (medikal görüntüleme ve bilimsel ml — olası bir b planı sektör geçişinde — aşağıdaki endüstri standartları üzerinden öğrenilir).
- ▶️ **yt:**
  1. **[bilimsel ml & pinns]** [steve brunton — physics-informed machine learning & sindy (youtube)](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — fizik bilgili sinir ağları, dinamik sistem keşfi ve dijital ikizler.
- 📖 **oku & 💻 repo:**
  1. [monai — medical open network for ai (monai.io & github)](https://github.com/Project-MONAI/MONAI) & [nnu-net (github)](https://github.com/MIC-DKFZ/nnUNet) — 3b medikal görüntü (dicom/nifti) segmentasyonu ve tespiti için küresel açık kaynak standartları.
  2. [geometric deep learning blueprint — bronstein et al. (geometricdeeplearning.com)](https://geometricdeeplearning.com/) — se(3)/e(3) eşdeğerli (equivariant) ağların hem 3b nokta bulutları hem de moleküler yapılarla ortak matematiksel temeli.

---

### 17. advanced llm engineering – ileri llm mühendisliği: eğitim sonrası, akıl yürütme ve kod ai

#### 42.1 pretraining data & infrastructure – ön eğitim veri hatları ve altyapısı

- [ ] web-scale data collection
- [ ] deduplication (minhash)
- [ ] quality filtering and classifiers
- [ ] tokenizer training
- [ ] data mixtures and curricula
- [ ] synthetic data generation
- [ ] benchmark decontamination
- [ ] deepspeed zero and fsdp
- [ ] megatron-lm
- [ ] large-scale checkpointing and fault recovery

#### 42.2 post-training – eğitim sonrası ince ayar ve hizalama

- [ ] sft data curation
- [ ] preference data collection
- [ ] dpo variants (ipo, kto, orpo, simpo)
- [ ] rejection sampling and best-of-n
- [ ] distillation from larger models
- [ ] model merging (ties, dare, slerp)
- [ ] safety tuning
- [ ] chat templates
- [ ] function-calling fine-tuning

#### 42.3 reasoning models – akıl yürütme modelleri

- [ ] chain-of-thought
- [ ] self-consistency
- [ ] tree-of-thoughts
- [ ] process reward models
- [ ] test-time compute scaling
- [ ] long chain-of-thought and reasoning rl
- [ ] verifiers
- [ ] search-based decoding (mcts for llms)
- [ ] program-aided reasoning
- [ ] self-reflection and self-refinement

**kaynaklar (önem ve çalışma sırasına göre):**

- **📖 oku & 💻 repo (adım adım kodlama & açık kaynak araştırma):**
  1. **reasoning from scratch: implement a reasoning llm in pytorch (sebastian raschka):** [github repo (rasbt/reasoning-from-scratch)](https://github.com/rasbt/reasoning-from-scratch) — **[sıfırdan akıl yürüten model kodlama standardı]** openai o1/o3 ve deepseek-r1 ekolünü satır satır öğreten; düşünce zinciri (chain-of-thought / cot), rejection sampling ile akıl yürütme verisi toplama, akıl yürütme sft'si, kural tabanlı rl / grpo (group relative policy optimization) ve çıkarım zamanı arama (test-time search / mcts) mekanizmalarını saf pytorch ile sıfırdan inşa eden 5.8k+ yıldızlı modern açık kaynak rehberi

#### 42.4 context & memory – uzun bağlam ve bellek mimarisi

- [ ] long-context extension (yarn, ntk-aware rope scaling)
- [ ] kv cache compression
- [ ] lost-in-the-middle problem
- [ ] prompt caching
- [ ] retrieval vs long context
- [ ] external memory for agents
- [ ] context engineering

#### 42.5 inference serving – yüksek performanslı model sunumu

- [ ] continuous batching
- [ ] prefix caching
- [ ] speculative decoding in serving
- [ ] disaggregated prefill / decode
- [ ] constrained decoding (grammar, json schema)
- [ ] model routing and cascades
- [ ] latency and cost optimization

#### 42.6 llm evaluation – dil modeli değerlendirme ve kıyaslama

- [ ] benchmarks (mmlu, gsm8k, humaneval, swe-bench)
- [ ] llm-as-judge pitfalls
- [ ] arena-style elo evaluation
- [ ] lm-evaluation-harness
- [ ] hallucination measurement
- [ ] agent evaluation
- [ ] building private domain eval sets
- [ ] calibration of llms

#### 42.7 code ai – kod üreten yapay zekâ ve yazılım ajanları

- [ ] code language models
- [ ] code completion and infilling
- [ ] program synthesis
- [ ] automated program repair
- [ ] test generation
- [ ] software engineering agents
- [ ] execution feedback and sandboxing
- [ ] formal proof assistants with llms (lean)

#### 42.8 advanced agents – ileri etmen sistemleri ve robotik entegrasyon

- [ ] model context protocol (mcp) and tool protocols
- [ ] computer-use and gui agents
- [ ] browser agents
- [ ] multi-agent frameworks
- [ ] agent reliability and failure modes
- [ ] prompt engineering
- [ ] llm-driven robot control (saycan, code-as-policies)
- [ ] human-in-the-loop agent design

**kaynaklar (önem ve çalışma sırasına göre):**

- 🇹🇷 **tr:** — (genel kültür ve takip bütçesi dahilinde aşağıdaki açık kitapçık ve konuşmaları inceleyebilirsin).
- ▶️ **yt:**
  1. **[ilk izlenecek]** [andrej karpathy — deep dive into llms (youtube)](https://www.youtube.com/watch?v=7xTGNNLPyMI) — pretraining, sft, rlhf ve akıl yürütme (reasoning rl) aşamalarının uçtan uca özeti.
- 📖 **oku & 💻 repo:**
  1. [hugging face — the ultra-scale playbook: training llms on gpu clusters (huggingface.co)](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — zero, fsdp, veri hatları ve büyük ölçekli eğitim mimarisi.
  2. [eleutherai — lm-evaluation-harness (github)](https://github.com/EleutherAI/lm-evaluation-harness) & [model context protocol (modelcontextprotocol.io)](https://modelcontextprotocol.io/) — standart model değerlendirme çatısı ve ajan-araç protokolü.
  3. [code as policies: language model programs for embodied control (code-as-policies.github.io)](https://code-as-policies.github.io/) — dil modellerinin robotik kontrol politikası üretmek için kullanılması.
