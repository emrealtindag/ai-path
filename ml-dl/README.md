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

### 01. machine learning

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

**resources:**

- **turkish resources:**
  1. **murat karakaya academy – applied machine learning & deep learning:** [youtube channel](https://www.youtube.com/@MuratKarakayaAkademi) — turkish applied ml and keras/python lectures
  2. **bilgisayar kavramları (şadi evren şeker) – machine learning series:** [youtube playlist](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — turkish intro to overfitting, cross-validation, and evaluation metrics
  3. **book (turkish):** cemalettin kubat – fundamentals and algorithms of artificial intelligence
- **video lectures:**
  1. **statquest with josh starmer – machine learning:** [youtube playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — visual guide to bias-variance, roc-auc, cross-validation, and core ml concepts
  2. **andrew ng – machine learning specialization (deeplearning.ai / stanford):** [youtube lecture series](https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI) — classic beginner-friendly intro to machine learning
  3. **caltech cs156 – learning from data (prof. yaser abu-mostafa):** [youtube lecture series](https://www.youtube.com/playlist?list=PLD63A284B7615313A) — university course on statistical learning theory, vc dimension, and generalization
- **books, papers & repositories:**
  1. **hands-on machine learning (aurélien géron):** [github code repo](https://github.com/ageron/handson-ml3) & [o'reilly book page](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — hands-on textbook for building end-to-end ml pipelines
  2. **scikit-learn official user guide:** [scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html) — official guide on preprocessing, metrics, and model validation
  3. **the elements of statistical learning (hastie, tibshirani, friedman):** [free pdf](https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf) — classic math reference for statistical learning
  4. **machine learning with pytorch and scikit-learn & mlxtend (sebastian raschka):** [book repo](https://github.com/rasbt/machine-learning-book) · [mlxtend library](https://github.com/rasbt/mlxtend) — practical code bridging scikit-learn to pytorch along with tools for plotting decision boundaries and running statistical tests

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

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları – classification & regression algorithms:** [youtube playlist](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) — turkish overview of svm, decision trees, random forest, k-nn, and naive bayes
  2. **veri bilimi okulu & miuul:** [veribilimiokulu.com](https://www.veribilimiokulu.com/) & [youtube channel](https://www.youtube.com/@Miuul) — turkish tutorials on supervised learning and tabular modeling
- **video lectures:**
  1. **statquest with josh starmer – decision trees, random forest, xgboost & svm:** [youtube playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — crystal-clear step-by-step explanation of gradient boosting and xgboost
  2. **cornell cs4780 – machine learning for intelligent systems (prof. kilian weinberger):** [youtube lecture series](https://www.youtube.com/playlist?list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS) — whiteboard math derivations for k-nn, svm, kernel trick, trees, and boosting
- **books, papers & repositories:**
  1. **xgboost official documentation & tutorials:** [xgboost.readthedocs.io](https://xgboost.readthedocs.io/en/stable/) — official docs for gradient boosting on tabular data
  2. **pattern recognition and machine learning – prml (christopher bishop):** [free official pdf](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) — foundational math textbook on bayesian regression, svm, and classification

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

**resources:**

- **turkish resources:**
  1. **bilgisayar kavramları – clustering & pca:** [youtube search](https://www.youtube.com/results?search_query=bilgisayar+kavramlar%C4%B1+k-means+pca) — turkish tutorials on k-means, hierarchical clustering, and pca
  2. **mustafa vahit keskin (miuul):** [youtube channel](https://www.youtube.com/@Miuul) — turkish tutorials on data science and clustering
- **video lectures:**
  1. **statquest – pca, k-means, dbscan, t-sne & umap:** [youtube playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — clear visual guide to dimensionality reduction and clustering
  2. **stanford cs229 – machine learning (unsupervised learning):** [youtube lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) — derivations of gaussian mixture models (gmm), em algorithm, and pca
  3. **victor lavrenko – clustering & em algorithm:** [youtube playlist](https://www.youtube.com/playlist?list=PLBv09BD7ez_4e9LtmK626Evn1ion6ynrt) — clear walkthroughs on gmm and clustering math
- **books, papers & repositories:**
  1. **scikit-learn unsupervised learning user guide:** [scikit-learn.org/stable/unsupervised_learning.html](https://scikit-learn.org/stable/unsupervised_learning.html) — code examples and comparisons for dbscan, gmm, pca, and anomaly detection
  2. **probabilistic machine learning: an introduction (kevin murphy – chapters 20 & 21):** [free pdf](https://probml.github.io/pml-book/book1.html) — probabilistic foundations of dimensionality reduction and clustering

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

**resources:**

- **turkish resources:**
  1. **metu ceng 501 – deep learning (prof. dr. sinan kalkan):** [official course page](https://kovan.ceng.metu.edu.tr/~sinan/) & [github course repo](https://github.com/sinankalkan/CENG501-Spring2021) — open course materials on neural networks, backprop, optimization, and regularization
  2. **murat karakaya academy – applied deep learning:** [youtube channel](https://www.youtube.com/@MuratKarakayaAkademi) — turkish deep learning tutorials
- **video lectures:**
  1. **3blue1brown – neural networks & backpropagation:** [youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — visual explanation of neural networks and backpropagation math
  2. **andrej karpathy – neural networks: zero to hero:** [youtube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — build autograd, backpropagation, and batchnorm from scratch without libraries
  3. **nyu deep learning ds-ga 1008 (yann lecun & alfredo canziani):** [youtube lecture series](https://www.youtube.com/playlist?list=PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq) — geometric and energy-based perspective on deep learning in pytorch
- **books, papers & repositories:**
  1. **dive into deep learning (d2l.ai):** [d2l.ai](https://d2l.ai/) — free interactive book pairing math formulas directly with runnable pytorch code
  2. **deep learning (ian goodfellow, yoshua bengio, aaron courville):** [deeplearningbook.org](https://www.deeplearningbook.org/) — free classic theoretical reference textbook

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

**resources:**

- **turkish resources:**
  1. **metu ceng 501 & ceng 783 (deep learning architectures):** [ceng 501 course page](https://user.ceng.metu.edu.tr/~emre/Fall2026-DeepLearning.html) & [github repo](https://github.com/sinankalkan/CENG501-Spring2021) — cnns, rnns, autoencoders, gans, and vision transformers
- **video lectures:**
  1. **stanford cs230 – deep learning (andrew ng):** [youtube lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) — practical engineering view of cnns, rnns/lstms, autoencoders, and gans
  2. **umar jamil – coding transformers & vit from scratch in pytorch:** [youtube channel](https://www.youtube.com/@umarjamilai) — step-by-step pytorch implementations straight from paper diagrams
  3. **yannic kilcher – paper reviews:** [youtube channel](https://www.youtube.com/@YannicKilcher) — detailed technical walkthroughs of key deep learning architecture papers
- **books, papers & repositories:**
  1. [**distill.pub**](https://distill.pub/) **(visualizing deep learning):** [distill.pub](https://distill.pub/) — interactive visual articles on attention, cnn features, and graph neural networks
  2. **attention is all you need (vaswani et al., 2017):** [arxiv:1706.03762](https://arxiv.org/abs/1706.03762) — original transformer architecture paper
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

**resources:**

- **turkish resources:**
  1. **inzva ai – deep learning study guides:** [inzva.com](https://inzva.com/) — turkish ai community study notes and guides
- **video lectures:**
  1. **umar jamil – pytorch deep dives & mixed precision:** [youtube channel](https://www.youtube.com/@umarjamilai) — training loop optimization and pytorch internals
  2. **pytorch official channel – distributed training & profiling:** [youtube channel](https://www.youtube.com/@PyTorch) — ddp, torchscript, and amp tutorials by pytorch engineers
- **books, papers & repositories:**
  1. **a recipe for training neural networks (andrej karpathy):** [karpathy.github.io/2019/04/25/recipe](https://karpathy.github.io/2019/04/25/recipe/) — practical checklist to catch silent neural network bugs and scale training step by step
  2. **pytorch automatic mixed precision (amp) recipe:** [pytorch.org/tutorials/recipes/recipes/amp_recipe.html](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html) — halve gpu memory usage and speed up training 2-3x using fp16/bf16
  3. **weights & biases (w&b) documentation:** [docs.wandb.ai](https://docs.wandb.ai/) — experiment tracking, hyperparameter sweeps, and ablation studies

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

**resources:**

- **turkish resources:**
  1. **metu ceng 501 – self-supervised & meta learning (prof. dr. sinan kalkan):** [course page](https://kovan.ceng.metu.edu.tr/~sinan/) — lecture slides on learning representations without labels
- **video lectures:**
  1. **yann lecun – self-supervised learning & energy-based models (nyu):** [youtube search](https://www.youtube.com/results?search_query=yann+lecun+self+supervised+learning) — learning world representations from unlabeled visual and sensor data
  2. **stanford cs330 – deep multi-task & meta learning (prof. chelsea finn):** [youtube lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rMC6zfYmnD7UG3LVvwaITY5) — graduate course on few-shot learning, domain adaptation, and continual learning
- **books, papers & repositories:**
  1. **lilian weng’s technical ml blog:** [lilianweng.github.io](https://lilianweng.github.io/) — clear technical summaries on contrastive, self-supervised, and meta-learning
  2. **a cookbook of self-supervised learning (balestriero, lecun et al.):** [arxiv:2304.12210](https://arxiv.org/abs/2304.12210) — practical handbook of self-supervised learning methods
  3. **simclr (chen et al.):** [arxiv:2002.05709](https://arxiv.org/abs/2002.05709) — core paper on contrastive learning of visual representations

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

**resources:**

- **video lectures:**
  1. **andrej karpathy – build gpt & tokenizer from scratch:** [gpt video](https://www.youtube.com/watch?v=kCc8FmEb1nY) & [tokenizer video](https://www.youtube.com/watch?v=zduSFxRajkE) — coding bpe tokenization, self-attention, and gpt from scratch in pytorch
  2. **stanford cs224n – nlp with deep learning (prof. christopher manning):** [youtube lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) — word2vec, sequence models, bert, and transformers
- **books, papers & repositories:**
  1. **the illustrated transformer & word2vec (jay alammar):** [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) — clear illustrated guide to attention mechanisms
  2. **transformer explainer (georgia tech):** [live demo](https://poloclub.github.io/transformer-explainer/) & [github repo](https://github.com/poloclub/transformer-explainer) — interactive browser tool visualizing live gpt embeddings, q/k/v attention, and probabilities
  3. **speech and language processing, 3rd ed. (jurafsky & martin):** [free pdf](https://web.stanford.edu/~jurafsky/slp3/) — standard reference textbook for nlp
  4. **build a large language model from scratch (sebastian raschka):** [github repo](https://github.com/rasbt/LLMs-from-scratch) & [book page](https://www.manning.com/books/build-a-large-language-model-from-scratch) — step-by-step pytorch code for tokenization, self-attention, pretraining, and lora fine-tuning

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

**resources:**

- **video lectures:**
  1. **andrej karpathy – state of gpt & reproduce gpt-2 (124m):** [state of gpt video](https://www.youtube.com/watch?v=bZQun8Y4L2A) & [gpt-2 video](https://www.youtube.com/watch?v=l8pRSuU81PU) — pretraining, sft, rlhf, and reproducing gpt-2 from scratch
  2. **umar jamil – coding llama 2/3, kv cache & lora from scratch:** [youtube channel](https://www.youtube.com/@umarjamilai) — pytorch code from scratch for rope, gqa, kv cache, and lora
  3. **maxime labonne & sam witteveen – llm fine-tuning & quantization:** [sam witteveen youtube](https://www.youtube.com/@samwitteveenai) & [llm course (github)](https://github.com/mlabonne/llm-course) — qlora, dpo, gguf/awq quantization, and model merging
- **books, papers & repositories:**
  1. **ggerganov/llama.cpp:** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) — pure c/c++ inference for large models using simd and cuda without python dependencies
  2. **vllm-project/vllm:** [docs.vllm.ai](https://docs.vllm.ai/) & [github repo](https://github.com/vllm-project/vllm) — high-throughput llm serving using pagedattention
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

**resources:**

- **video lectures:**
  1. **langchain – rag from scratch series:** [youtube playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) — concise engineering guide to chunking, indexing, hybrid search, and reranking
  2. **sam witteveen – advanced rag & vector databases:** [youtube channel](https://www.youtube.com/@samwitteveenai) — building production rag pipelines
- **books, papers & repositories:**
  1. **faiss (c++ & python):** [faiss.ai](https://faiss.ai/) & [github repo](https://github.com/facebookresearch/faiss) — c++/gpu library for fast nearest-neighbor search across millions of image or text embeddings
  2. **llamaindex & qdrant documentation:** [docs.llamaindex.ai](https://docs.llamaindex.ai/) · [qdrant.tech/documentation](https://qdrant.tech/documentation/) — data indexing frameworks and rust-based vector database architecture
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

**resources:**

- **video lectures:**
  1. **deeplearning.ai & harrison chase – ai agents in langgraph:** [course page](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) & [langchain youtube](https://www.youtube.com/@LangChain) — stateful agent graphs, memory, and tool calling
  2. **sam witteveen – agentic workflows & multi-agent systems:** [youtube channel](https://www.youtube.com/@samwitteveenai)
- **books, papers & repositories:**
  1. **llm powered autonomous agents (lilian weng):** [blog post](https://lilianweng.github.io/posts/2023-06-23-agent/) — clean overview of planning, memory, and tool-use architecture
  2. **react: synergizing reasoning and acting (yao et al.):** [arxiv:2210.03629](https://arxiv.org/abs/2210.03629) — core paper combining chain-of-thought reasoning with tool actions
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

**resources:**

- **video lectures:**
  1. **outlier – diffusion models from scratch:** [youtube video](https://www.youtube.com/watch?v=HoKDTa5jHvg) — visual math behind forward and reverse diffusion processes (ddpm)
  2. **umar jamil – coding stable diffusion from scratch in pytorch:** [youtube video](https://www.youtube.com/watch?v=ZBKpAp_6TGI) — putting together vae, u-net, clip, and ddpm sampler in pure pytorch
  3. **arash vahdat (nvidia research) – diffusion tutorials (cvpr):** [youtube talk](https://www.youtube.com/watch?v=cS6JQpEY9cs) — comparing vae, gan, normalizing flows, and score-based diffusion theory
- **books, papers & repositories:**
  1. **what are diffusion models? (lilian weng):** [blog post](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — clear mathematical derivation of diffusion models
  2. **understanding diffusion models: a unified perspective (calvin luo):** [arxiv:2208.11970 (free pdf)](https://arxiv.org/pdf/2208.11970.pdf) — clean 25-page tutorial connecting elbo, vae, and score matching

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

**resources:**

- **video lectures:**
  1. **umar jamil – coding paligemma / llava from scratch:** [youtube video](https://www.youtube.com/watch?v=vAmKB7iPkWw) — connecting siglip/clip vision encoders with gemma/llama language models in pytorch
  2. **yannic kilcher – llava, flamingo & multimodal reviews:** [youtube channel](https://www.youtube.com/@YannicKilcher) — architecture breakdowns of vision-language models
- **books, papers & repositories:**
  1. **vision-language models explained (hugging face):** [huggingface.co/blog/vlms](https://huggingface.co/blog/vlms) — practical overview of modern vlm architectures
  2. **visual instruction tuning – llava (liu et al., neurips 2023):** [arxiv:2304.08485](https://arxiv.org/abs/2304.08485) & [github repo](https://github.com/haotian-liu/LLaVA) — open-source multimodal instruction tuning paper and codebase
  3. **nanovlm: minimal & fast vlm training (hugging face):** [github repo](https://github.com/huggingface/nanoVLM) — clean minimal pytorch codebase for training a vision-language model from scratch on consumer gpus

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

**resources:**

- **books, papers & repositories:**
  1. **awesome robotics foundation models:** [github repo](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) & [arxiv:2312.07843](https://arxiv.org/abs/2312.07843) — curated paper list on robotics foundation models, vlas, imitation learning, and 6d pose estimation
  2. **openvla & openvla-oft (stanford / uc berkeley):** [openvla.github.io](https://openvla.github.io/) · [openvla/openvla](https://github.com/openvla/openvla) & [moojink/openvla-oft](https://github.com/moojink/openvla-oft) — open-source 7b vision-language-action model converting camera images and text directly into 7-dof robot actions
  3. **rt-2: vision-language-action models (google deepmind):** [arxiv:2307.15818](https://arxiv.org/abs/2307.15818) — foundational paper introducing vision-language-action (vla) policies
  4. **voxposer: composable 3d value maps (stanford asl):** [voxposer.github.io](https://voxposer.github.io/) & [github repo](https://github.com/huangwl18/VoxPoser) — synthesizing 3d robot trajectory value maps using llms and vlms
  5. **foundationpose: unified 6d pose estimation & tracking (nvidia):** [project page](https://nvlabs.github.io/FoundationPose/) — unified model-free and model-based 6d object pose estimation and tracking
  6. **gaia-1: generative world model for autonomous driving (wayve):** [arxiv paper](https://arxiv.org/abs/2309.17080) — generative world model using video, text, and actions for driving
  7. **egoverse: egocentric data for robot learning (georgia tech):** [github repo](https://github.com/GaTech-RL2/EgoVerse) — converting first-person human hand tracking data into robot manipulation actions for $\pi_0$ and lerobot
- **video lectures:**
  1. **stanford robotics & embodied ai seminars:** [youtube search](https://www.youtube.com/results?search_query=stanford+robotics+seminar+vla+embodied+ai) — seminar talks on vision-language-action (vla) policies
  2. **google deepmind robotics & physical intelligence:** [deepmind youtube](https://www.youtube.com/@GoogleDeepMind) — technical presentations on rt-1, rt-2, and general-purpose robot foundation models

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

**resources:**

- **turkish resources:**
  1. **mustafa vahit keskin (miuul) – python data analysis:** [youtube channel](https://www.youtube.com/@Miuul) & [veribilimiokulu.com](https://www.veribilimiokulu.com/) — turkish course on pandas, numpy, eda, and data cleaning
- **video lectures:**
  1. **keith galli – complete python pandas tutorial:** [youtube video](https://www.youtube.com/watch?v=vmEHCJofslg) — 1-hour hands-on pandas walkthrough on a real dataset
- **books, papers & repositories:**
  1. **python for data analysis, 3rd ed. (wes mckinney):** [wesmckinney.com/book (free book)](https://wesmckinney.com/book/) — open-access book by the creator of pandas covering numpy, data cleaning, and time series
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

**resources:**

- **turkish resources:**
  1. **mustafa vahit keskin (miuul) – feature engineering & measurement:** [youtube channel](https://www.youtube.com/@Miuul) — turkish tutorials on a/b testing, hypothesis tests, and feature extraction
- **video lectures:**
  1. **statquest with josh starmer – hypothesis testing & statistical modeling:** [youtube playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) — experiment design, p-values, and statistical significance
- **books, papers & repositories:**
  1. **practical statistics for data scientists, 2nd ed.:** [o'reilly book page](https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/) & [github python code](https://github.com/gedeck/practical-statistics-for-data-scientists) — applied statistics handbook with python examples

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

**resources:**

- **turkish resources:**
  1. **bora kaşmer – distributed systems, redis & kafka:** [youtube channel](https://www.youtube.com/@BoraKasmer) — turkish talks on real-time streaming and caching architectures
- **video lectures:**
  1. **seattle data guy – data engineering fundamentals:** [youtube channel](https://www.youtube.com/@SeattleDataGuy) — practical intro to etl/elt, postgresql, spark, and kafka pipelines
  2. **luke barousse – sql for data science & analytics:** [youtube channel](https://www.youtube.com/@LukeBarousse) — practical sql querying
- **books, papers & repositories:**
  1. **sqlbolt – interactive sql exercises:** [sqlbolt.com](https://sqlbolt.com/) — quick interactive browser practice for sql basics
  2. **designing data-intensive applications (martin kleppmann):** [dataintensive.net](https://dataintensive.net/) — classic systems book on databases, indexing, replication, sharding, kafka, and distributed systems

#### 15.4 ai dataset engineering

- [ ] dataset collection
- [ ] data annotation
- [ ] dataset curation
- [ ] data augmentation (albumentations library)
- [ ] data balancing
- [ ] label quality
- [ ] data versioning (dvc)
- [ ] synthetic data (simulation-based, isaac sim)
- [ ] dataset bias
- [ ] dataset evaluation
- [ ] benchmark construction

**resources:**

- **video lectures:**
  1. **roboflow – computer vision dataset tutorials:** [youtube channel](https://www.youtube.com/@Roboflow) — collecting camera/uav datasets, auto-labeling, and data quality checks
  2. **mit – data-centric ai (cleanlab):** [youtube lecture series](https://www.youtube.com/playlist?list=PL_1TbuIu65A8NTNuLutFoD87vbMl8GL8K) & [course site](https://dcai.csail.mit.edu/) — detecting noisy labels and cleaning dataset bias
- **books, papers & repositories:**
  1. **albumentations documentation:** [albumentations.ai/docs](https://albumentations.ai/docs/) & [github repo](https://github.com/albumentations-team/albumentations) — fast image augmentation keeping bounding boxes, masks, and keypoints aligned
  2. **dvc (data version control) documentation:** [dvc.org/doc](https://dvc.org/doc) — version control tool for large image and sensor datasets

---

### 04. reinforcement learning

#### 25.1 rl foundations

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

#### 25.2 multi-armed bandits

- [ ] $\varepsilon$-greedy
- [ ] upper confidence bound (ucb)
- [ ] thompson sampling
- [ ] contextual bandits
- [ ] linear bandits (linucb)
- [ ] regret analysis
- [ ] dueling bandits

#### 25.3 dynamic programming & tabular rl

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

#### 25.4 function approximation

- [ ] linear function approximation
- [ ] tile coding
- [ ] semi-gradient methods
- [ ] the deadly triad
- [ ] feature construction
- [ ] experience replay
- [ ] target networks

#### 25.5 deep value-based rl

- [ ] dqn
- [ ] double dqn
- [ ] dueling dqn
- [ ] prioritized experience replay
- [ ] noisy networks
- [ ] distributional rl (c51, qr-dqn)
- [ ] rainbow
- [ ] recurrent dqn (r2d2)

#### 25.6 policy gradient & actor-critic

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

#### 25.7 model-based rl & planning

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

#### 25.8 offline rl & imitation

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

#### 25.9 exploration, hierarchical & safe rl

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

#### 25.10 multi-agent rl & game theory

- [ ] game theory basics (nash equilibrium, zero-sum games)
- [ ] self-play
- [ ] centralized training decentralized execution (ctde)
- [ ] maddpg
- [ ] qmix
- [ ] mappo
- [ ] population-based training
- [ ] counterfactual regret minimization (cfr)
- [ ] emergent communication

#### 25.11 rl for llms

- [ ] rlhf pipeline
- [ ] reward models
- [ ] ppo for language models
- [ ] grpo
- [ ] rl with verifiable rewards (rlvr)
- [ ] process vs outcome rewards
- [ ] rlaif / constitutional ai
- [ ] reward hacking

#### 25.12 rl engineering & benchmarks

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

**resources:**

- **video lectures:**
  1. **david silver — reinforcement learning course (ucl / deepmind):** [youtube playlist](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) — core lectures on mdps, bellman equations, td learning, and policy gradients
  2. **uc berkeley cs285 — deep reinforcement learning (sergey levine):** [youtube playlist](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — graduate course on ppo, sac, model-based rl, offline rl, and robot control
  3. [hugging face deep rl course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) — free hands-on coding course from q-learning to ppo and sac
- **books, papers & repositories:**
  1. [richard s. sutton & andrew g. barto — reinforcement learning: an introduction, 2nd ed. (free pdf)](http://incompleteideas.net/book/the-book-2nd.html) — classic textbook on tabular rl, bellman equations, and function approximation
  2. [openai spinning up in deep rl](https://spinningup.openai.com/en/latest/) — clear math and code guide for reinforce, trpo, ppo, ddpg, td3, and sac
  3. [cleanrl — single-file deep rl implementations (github)](https://github.com/vwxyzjn/cleanrl) — readable single-file pytorch implementations of rl algorithms
  4. [stable-baselines3 (github)](https://github.com/DLR-RM/stable-baselines3) & [gymnasium](https://gymnasium.farama.org/) — standard reinforcement learning environments and algorithm libraries

---

### 05. probabilistic & bayesian machine learning

#### 26.1 probabilistic graphical models

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

#### 26.2 sequence & latent variable models

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

#### 26.3 approximate inference

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

#### 26.4 gaussian processes

- [ ] gp regression
- [ ] kernel functions (rbf, matérn, periodic)
- [ ] marginal likelihood and hyperparameter learning
- [ ] sparse gps (inducing points)
- [ ] gp classification
- [ ] deep kernel learning
- [ ] bayesian optimization with gps
- [ ] gps in robotics (dynamics learning, mapping)

#### 26.5 bayesian deep learning & uncertainty

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

#### 26.6 probabilistic programming

- [ ] pymc
- [ ] stan
- [ ] numpyro
- [ ] pyro
- [ ] bayesian workflow
- [ ] prior and posterior predictive checks
- [ ] model comparison (waic, loo-cv)
- [ ] hierarchical models

#### 26.7 causal inference & causal ml

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

**resources:**

- **turkish resource:** [cemgil lab (boğaziçi university) — probabilistic modeling archive](https://www.youtube.com/@taylancemgil) — turkish lecture recordings on bayesian inference and factor graphs
- **video lectures:**
  1. [tübingen probabilistic machine learning course — philipp hennig (youtube)](https://www.youtube.com/playlist?list=PL05umP7R6ij1tHaOFY96m5uX3J21a6yNd) — gaussian processes, variational inference, mcmc, and graphical models
  2. [daphne koller — probabilistic graphical models (coursera)](https://www.coursera.org/specializations/probabilistic-graphical-models) — bayesian networks, markov networks, factor graphs, and belief propagation
- **books, papers & repositories:**
  1. [kevin p. murphy — probabilistic machine learning: advanced topics (free pdf)](https://probml.github.io/pml-book/book2.html) — core reference covering graphical models, gp, vi, mcmc, and uncertainty
  2. [frank dellaert & michael kaess — factor graphs for robot perception (free pdf)](https://www.cs.cmu.edu/~kaess/pub/Dellaert17fnt.pdf) — practical monograph connecting graphical models to slam and gtsam
  3. [rasmussen & williams — gaussian processes for machine learning (free pdf)](https://gaussianprocess.org/gpml/) — core book on gaussian process regression and kernel functions

---

### 06. advanced nlp & language technologies

#### 28.1 linguistics & text processing

- [ ] morphology, syntax, semantics, pragmatics
- [ ] tokenization and sentence segmentation
- [ ] stemming and lemmatization
- [ ] text normalization (unicode)
- [ ] regular expressions
- [ ] spell correction
- [ ] language identification
- [ ] corpora and annotation schemes

#### 28.2 classical nlp models

- [ ] bag of words
- [ ] tf-idf
- [ ] n-gram language models
- [ ] smoothing (kneser-ney)
- [ ] naive bayes for text
- [ ] latent semantic analysis (lsa)
- [ ] topic modeling (lda)
- [ ] hmm and crf for sequence tagging

#### 28.3 core nlp tasks

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

#### 28.4 generation & seq2seq tasks

- [ ] machine translation (statistical → neural)
- [ ] decoding strategies (greedy, beam, top-k, top-p, temperature)
- [ ] back-translation
- [ ] extractive summarization
- [ ] abstractive summarization
- [ ] paraphrasing
- [ ] grammatical error correction
- [ ] data-to-text generation
- [ ] text style transfer

#### 28.5 question answering, ir & dialogue

- [ ] extractive qa (squad)
- [ ] open-domain qa
- [ ] multi-hop qa
- [ ] table qa
- [ ] dense retrieval (dpr, colbert)
- [ ] task-oriented dialogue
- [ ] open-domain dialogue
- [ ] dialogue state tracking
- [ ] conversational agents

#### 28.6 multilingual, low-resource & turkish nlp

- [ ] multilingual models (mbert, xlm-r)
- [ ] cross-lingual transfer
- [ ] low-resource language techniques
- [ ] agglutinative morphology
- [ ] turkish morphological analysis
- [ ] turkish tokenization challenges
- [ ] turkish corpora and benchmarks
- [ ] code-switching
- [ ] transliteration

#### 28.7 nlp evaluation

- [ ] bleu, rouge, meteor
- [ ] bertscore
- [ ] perplexity
- [ ] human evaluation and inter-annotator agreement
- [ ] llm-as-judge
- [ ] benchmarks (glue, superglue, mmlu)
- [ ] benchmark contamination

#### 28.8 nlp tooling

- [ ] spacy
- [ ] nltk
- [ ] hugging face transformers
- [ ] hugging face datasets and tokenizers
- [ ] gensim
- [ ] stanza

**resources:**

- **turkish resource:** [zemberek-nlp (github)](https://github.com/ahmetaa/zemberek-nlp) & [boun-tabi turkish nlp resources (github)](https://github.com/boun-tabi) — open-source turkish morphological analysis tools and datasets
- **video lectures:**
  1. [stanford cs224n — natural language processing with deep learning](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) — classical and deep learning nlp architectures
  2. [hugging face llm & nlp course](https://huggingface.co/learn/nlp-course/chapter1/1) — hands-on tutorials for transformers, tokenizers, and datasets libraries
- **books, papers & repositories:**
  1. [dan jurafsky & james h. martin — speech and language processing, 3rd ed. (free pdf)](https://web.stanford.edu/~jurafsky/slp3/) — standard textbook on linguistics, parsing, sequence tagging, and semantics

---

### 07. speech, audio & music ai

#### 29.1 audio & signal fundamentals

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

#### 29.2 automatic speech recognition (asr)

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

#### 29.3 text-to-speech & voice synthesis

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

#### 29.4 speaker & audio understanding

- [ ] speaker verification and identification
- [ ] speaker embeddings (x-vector, ecapa-tdnn)
- [ ] speaker diarization
- [ ] audio classification
- [ ] sound event detection
- [ ] acoustic scene classification
- [ ] audio captioning
- [ ] speech emotion recognition
- [ ] audio deepfake and anti-spoofing

#### 29.5 speech enhancement & source separation

- [ ] noise suppression
- [ ] dereverberation
- [ ] acoustic echo cancellation
- [ ] beamforming
- [ ] microphone arrays
- [ ] direction of arrival (doa) estimation
- [ ] sound source localization (robot audition)
- [ ] source separation (conv-tasnet, demucs)

#### 29.6 music ai

- [ ] music information retrieval (mir)
- [ ] beat and tempo tracking
- [ ] chord recognition
- [ ] automatic music transcription
- [ ] music tagging
- [ ] symbolic music generation
- [ ] audio music generation

#### 29.7 audio-language & spoken llms

- [ ] neural audio codecs and tokenizers (encodec)
- [ ] audio-text models (clap)
- [ ] speech llms
- [ ] full-duplex voice dialogue
- [ ] real-time voice agents

#### 29.8 audio tooling

- [ ] librosa
- [ ] torchaudio
- [ ] kaldi
- [ ] espnet
- [ ] nvidia nemo
- [ ] speechbrain
- [ ] whisper.cpp
- [ ] moonshine (low-latency live speech & edge asr)

**resources:**

- **video lectures:**
  1. [valerio velardo — audio signal processing for machine learning (youtube)](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0) — practical guides on stft, spectrograms, mfcc, and librosa
- **books, papers & repositories:**
  1. [hugging face audio course](https://huggingface.co/learn/audio-course/chapter0/introduction) — applied tutorials on audio classification, asr (whisper), and tts models
  2. [whisper.cpp (github)](https://github.com/ggerganov/whisper.cpp) & [speechbrain (github)](https://github.com/speechbrain/speechbrain) — c/c++ edge speech recognition and pytorch audio toolkit
  3. **moonshine (useful sensors / moonshine ai):** [github repo](https://github.com/moonshine-ai/moonshine) & [arxiv:2410.15608](https://arxiv.org/abs/2410.15608) — fast speech-to-text model for live edge devices like raspberry pi and jetson without whisper's 30s fixed window overhead
  4. **stanford cs224s & mozilla common voice tr:** [stanford cs224s](https://www.youtube.com/results?search_query=stanford+cs224s+spoken+language+processing) · [common voice tr](https://commonvoice.mozilla.org/tr) — university course on spoken language processing (asr/tts) plus open turkish speech dataset

---

### 08. time series, forecasting & sequential data

#### 30.1 time series fundamentals

- [ ] trend, seasonality, noise
- [ ] stationarity (adf, kpss tests)
- [ ] autocorrelation (acf, pacf)
- [ ] decomposition (stl)
- [ ] differencing
- [ ] resampling and irregular sampling
- [ ] missing value handling
- [ ] walk-forward validation
- [ ] data leakage in time series

#### 30.2 statistical models

- [ ] ar, ma, arma
- [ ] arima and sarima
- [ ] arimax
- [ ] exponential smoothing (ets, holt-winters)
- [ ] vector autoregression (var)
- [ ] state-space models and kalman smoothing
- [ ] garch (volatility modeling)
- [ ] cointegration
- [ ] spectral analysis

#### 30.3 machine learning for time series

- [ ] lag and rolling window features
- [ ] gradient boosting for forecasting
- [ ] multi-step forecasting strategies (direct, recursive)
- [ ] quantile and probabilistic forecasting
- [ ] hierarchical forecasting

#### 30.4 deep learning for time series

- [ ] rnn and lstm forecasting
- [ ] temporal convolutional networks (tcn)
- [ ] n-beats and n-hits
- [ ] deepar
- [ ] temporal fusion transformer
- [ ] informer and autoformer
- [ ] patchtst
- [ ] time series foundation models (timesfm, chronos)

#### 30.5 time series tasks

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

#### 30.6 evaluation

- [ ] mae, rmse
- [ ] mape, smape
- [ ] mase
- [ ] crps
- [ ] backtesting
- [ ] prediction intervals and coverage

#### 30.7 tooling

- [ ] statsmodels
- [ ] sktime
- [ ] darts
- [ ] gluonts
- [ ] nixtla ecosystem
- [ ] tsfresh

**resources:**

- **turkish resource:** [veribilimiokulu / miuul — time series analysis notes](https://www.veribilimiokulu.com/) — turkish intro to stationarity, trend, seasonality, and arima/sarima
- **video lectures:**
  1. [ritvikmath — time series talk playlist (youtube)](https://www.youtube.com/playlist?list=PLvcbYUQ5t0UHOLnBzl46_Q6QKtFgfMGc3) — intuitive tutorials on acf, pacf, arima, and state-space models
- **books, papers & repositories:**
  1. [hyndman & athanasopoulos — forecasting: principles and practice, 3rd ed. (free online book)](https://otexts.com/fpp3/) — standard textbook on forecasting, cross-validation, and time series metrics
  2. [sktime (github)](https://github.com/sktime/sktime) · [darts (github)](https://github.com/unit8co/darts) · [nixtla (github)](https://github.com/Nixtla) — python libraries for time series forecasting and anomaly detection

---

### 09. recommender systems & information retrieval

#### 31.1 recommender fundamentals

- [ ] collaborative filtering (user-based, item-based)
- [ ] content-based filtering
- [ ] hybrid systems
- [ ] explicit vs implicit feedback
- [ ] cold start problem
- [ ] sparsity
- [ ] similarity metrics

#### 31.2 matrix factorization & classical models

- [ ] svd and svd++
- [ ] alternating least squares (als)
- [ ] bayesian personalized ranking (bpr)
- [ ] factorization machines
- [ ] implicit matrix factorization

#### 31.3 deep recommenders

- [ ] neural collaborative filtering
- [ ] wide & deep
- [ ] deepfm
- [ ] deep & cross network (dcn)
- [ ] two-tower models
- [ ] sequential recommenders (gru4rec, sasrec, bert4rec)
- [ ] graph-based recommenders (lightgcn, pinsage)
- [ ] generative recommenders
- [ ] large embedding tables

#### 31.4 retrieval & ranking pipeline

- [ ] candidate generation
- [ ] approximate nearest neighbor search (hnsw, scann, ivf)
- [ ] ranking and re-ranking
- [ ] learning to rank (ranknet, lambdamart, listwise)
- [ ] multi-task ranking (mmoe)
- [ ] diversity and novelty

#### 31.5 evaluation & experimentation

- [ ] precision@k, recall@k
- [ ] map, mrr
- [ ] ndcg
- [ ] offline vs online evaluation
- [ ] a/b testing
- [ ] interleaving
- [ ] off-policy evaluation

#### 31.6 biases & responsible recommendation

- [ ] position bias
- [ ] selection and popularity bias
- [ ] feedback loops
- [ ] fairness in recommendation
- [ ] filter bubbles
- [ ] bandit-based exploration

#### 31.7 search systems

- [ ] inverted index
- [ ] bm25
- [ ] query understanding
- [ ] learned sparse retrieval (splade)
- [ ] hybrid retrieval
- [ ] elasticsearch / opensearch / lucene
- [ ] pagerank
- [ ] web crawling

#### 31.8 tooling

- [ ] surprise
- [ ] implicit
- [ ] lightfm
- [ ] recbole
- [ ] torchrec

**resources:**

- **video lectures:**
  1. **stanford cs276 — information retrieval & web search:** [course page](https://web.stanford.edu/class/cs276/) & [youtube lectures](https://www.youtube.com/playlist?list=PLaZQkZp6WhWwoDuD6pQCmgVyDbUWl_ZUi) — inverted indexes, bm25, ranking, and search fundamentals
- **books, papers & repositories:**
  1. [manning, raghavan & schütze — introduction to information retrieval (free online book)](https://nlp.stanford.edu/IR-book/) — standard reference textbook on search engines and retrieval
  2. [faiss (github)](https://github.com/facebookresearch/faiss) & [recbole (github)](https://github.com/RUCAIBox/RecBole) — fast vector similarity search (hnsw/ivf) and recommender systems toolkit

---

### 10. advanced deep learning

#### 32.1 efficient & alternative sequence architectures

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

#### 32.2 scaling & training dynamics

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

#### 32.3 deep learning theory

- [ ] universal approximation
- [ ] depth vs width expressivity
- [ ] neural tangent kernel (ntk)
- [ ] infinite-width limits
- [ ] implicit bias of gradient descent
- [ ] overparameterization
- [ ] information bottleneck
- [ ] signal propagation and initialization theory
- [ ] generalization bounds for neural networks

#### 32.4 representation learning

- [ ] contrastive learning (infonce)
- [ ] byol and simsiam
- [ ] barlow twins and vicreg
- [ ] masked autoencoders (mae)
- [ ] jepa (i-jepa, v-jepa)
- [ ] disentangled representations
- [ ] vector quantization (vq-vae, vqgan)
- [ ] sparse autoencoders
- [ ] embedding geometry

#### 32.5 generative modeling theory

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

#### 32.6 training techniques

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

**resources:**

- **video lectures:**
  1. [stanford cs236 — deep generative models (stefano ermon)](https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8) — normalizing flows, vae, gan, energy-based models, and score-based diffusion
  2. [nyu deep learning sp21 — yann lecun & alfredo canziani (youtube)](https://www.youtube.com/playlist?list=PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq) — energy-based models, contrastive learning, and jepa
- **books, papers & repositories:**
  1. [simon j.d. prince — understanding deep learning (free pdf)](https://udlbook.github.io/udlbook/) — clear modern textbook covering deep learning architectures, diffusion, and training dynamics
  2. [lilian weng’s blog](https://lilianweng.github.io/) — math summaries of infonce, byol, mae, score/sde diffusion, rope, gqa, and moe
  3. [annotated s4 & mamba (sasha rush / albert gu)](https://srush.github.io/annotated-s4/) — line-by-line code and math walkthrough of state space models

---

### 11. statistical learning theory & advanced classical ml

#### 33.1 statistical learning theory

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

#### 33.2 kernel methods

- [ ] kernel trick
- [ ] mercer’s theorem
- [ ] reproducing kernel hilbert space (rkhs)
- [ ] kernel svm
- [ ] kernel pca
- [ ] kernel ridge regression
- [ ] random fourier features
- [ ] nystrom approximation
- [ ] maximum mean discrepancy (mmd)

#### 33.3 advanced classical ml

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

#### 33.4 manifold, spectral & sparse methods

- [ ] isomap
- [ ] locally linear embedding (lle)
- [ ] laplacian eigenmaps
- [ ] spectral clustering
- [ ] non-negative matrix factorization (nmf)
- [ ] sparse coding and dictionary learning
- [ ] compressed sensing
- [ ] random projections

#### 33.5 advanced optimization for ml

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

**resources:**

- **turkish resource:** [prof. dr. ethem alpaydın — introduction to machine learning (turkish textbook & boğaziçi notes)](https://www.boun.edu.tr/) — turkish reference book covering vc dimension, kernel methods, and ensembles
- **video lectures:**
  1. [caltech cs156 — learning from data (yaser abu-mostafa)](https://www.youtube.com/playlist?list=PLD63A284B7615313A) — pac learning, hoeffding inequality, vc dimension, generalization bounds, and regularization
- **books, papers & repositories:**
  1. [hastie, tibshirani & friedman — the elements of statistical learning (free pdf)](https://hastie.su.domains/ElemStatLearn/) — standard math book covering lasso/ridge, kernel methods, boosting, and spectral methods
  2. [shalev-shwartz & ben-david — understanding machine learning (free pdf)](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) — pac learning, vc dimension, rademacher complexity, and statistical learning theory
  3. [stephen boyd & lieven vandenberghe — convex optimization (free pdf)](https://web.stanford.edu/~boyd/cvxbook/) — convex optimization, l-bfgs, admm, and convergence analysis

---

### 12. ai safety, interpretability, fairness & governance

#### 34.1 explainable ai (xai)

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

#### 34.2 mechanistic interpretability

- [ ] circuits
- [ ] features and superposition
- [ ] sparse autoencoders for features
- [ ] activation patching
- [ ] logit lens
- [ ] induction heads
- [ ] steering vectors / representation engineering
- [ ] model editing (rome, memit)

#### 34.3 fairness & bias

- [ ] sources of bias
- [ ] group fairness (demographic parity, equalized odds)
- [ ] individual fairness
- [ ] fairness impossibility results
- [ ] bias mitigation (pre-, in-, post-processing)
- [ ] dataset and representation bias
- [ ] fairness in vision and language models
- [ ] fairlearn and aif360

#### 34.4 alignment & frontier ai safety

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

#### 34.5 safety-critical & robust ai

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

#### 34.6 responsible ai & governance

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

**resources:**

- **turkish resource:** [kvkk — personal data protection guidelines for ai](https://www.kvkk.gov.tr/) — turkish data privacy regulations and guidelines
- **video lectures:**
  1. [aaron ames (caltech) — control barrier functions for safety-critical systems (youtube)](https://www.youtube.com/watch?v=ZC3T_P_8xpE) — formal mathematical safety guarantees (cbfs) for robotics and autonomous systems
  2. [dan hendrycks — introduction to ai safety, ethics, and society (course)](https://www.aisafetybook.com/) — ood robustness, alignment, safety engineering, and governance
- **books, papers & repositories:**
  1. [christoph molnar — interpretable machine learning (free online book)](https://christophm.github.io/interpretable-ml-book/) — practical guide to shap, lime, permutation importance, and grad-cam
  2. [captum for pytorch (github)](https://github.com/pytorch/captum) & [pytorch-grad-cam (github)](https://github.com/jacobgil/pytorch-grad-cam) — interpretability tools for vision and deep learning models
  3. [ul 4600 & iso 21448 (sotif) safety overview (prof. philip koopman)](https://users.ece.cmu.edu/~koopman/ul4600/) — engineering standards for functional safety (iso 26262), sotif, and do-178c in autonomous vehicles and uavs

---

### 13. adversarial ml, security & privacy

#### 35.1 adversarial attacks

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

#### 35.2 defenses

- [ ] adversarial training
- [ ] randomized smoothing
- [ ] input preprocessing defenses
- [ ] adversarial example detection
- [ ] certified defenses
- [ ] gradient masking pitfalls
- [ ] robustness benchmarks (robustbench)

#### 35.3 data & model attacks

- [ ] data poisoning
- [ ] backdoor / trojan attacks
- [ ] model extraction
- [ ] model inversion
- [ ] membership inference
- [ ] training data extraction
- [ ] supply chain attacks (malicious model files)
- [ ] model watermarking
- [ ] model fingerprinting

#### 35.4 llm & agent security

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

#### 35.5 privacy-preserving ml

- [ ] differential privacy (dp-sgd)
- [ ] federated learning
- [ ] secure aggregation
- [ ] homomorphic encryption
- [ ] secure multi-party computation
- [ ] trusted execution environments
- [ ] split learning
- [ ] machine unlearning
- [ ] anonymization (k-anonymity)

#### 35.6 secure ai engineering

- [ ] threat modeling for ml (stride, mitre atlas)
- [ ] mlsecops
- [ ] secure boot and secure ota for edge devices
- [ ] model encryption on edge
- [ ] dependency and package vulnerabilities

**resources:**

- **video lectures:**
  1. [zico kolter & aleksander madry — adversarial robustness (neurips tutorial)](https://adversarial-ml-tutorial.org/) — math and pytorch code for fgsm, pgd, adversarial training, and certified robustness
- **books, papers & repositories:**
  1. [robustbench (github)](https://github.com/RobustBench/robustbench) & [autoattack (github)](https://github.com/fra31/auto-attack) — standard benchmarks for adversarial and corruption robustness in vision models
  2. [adversarial robustness toolbox (art, github)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) — library for adversarial attacks (patches, spoofing) and defenses on detection models
  3. [mitre atlas](https://atlas.mitre.org/) & [owasp top 10 for llm applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — threat modeling matrix and security checklists for ai systems

---

### 14. automl, evolutionary computation & optimization heuristics

#### 36.1 automl & hyperparameter optimization

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

#### 36.2 evolutionary computation

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

#### 36.3 swarm & bio-inspired optimization

- [ ] particle swarm optimization (pso)
- [ ] ant colony optimization
- [ ] artificial bee colony
- [ ] simulated annealing
- [ ] tabu search
- [ ] memetic algorithms
- [ ] artificial immune systems
- [ ] cellular automata
- [ ] artificial life

#### 36.4 fuzzy logic & soft computing

- [ ] fuzzy sets and membership functions
- [ ] fuzzy inference (mamdani, sugeno)
- [ ] fuzzy control
- [ ] anfis
- [ ] rough sets
- [ ] neuro-fuzzy systems
- [ ] type-2 fuzzy systems

#### 36.5 combinatorial & operations research optimization

- [ ] linear and integer programming (milp)
- [ ] constraint programming
- [ ] branch and bound
- [ ] traveling salesman problem (tsp)
- [ ] vehicle routing problem (vrp)
- [ ] scheduling problems
- [ ] google or-tools
- [ ] neural combinatorial optimization
- [ ] learning to optimize

**resources:**

- **video lectures:**
  1. [automl seminar series (frank hutter — youtube)](https://www.youtube.com/@automl-freiburg-edu) — bayesian optimization, hyperband, bohb, and neural architecture search
- **books, papers & repositories:**
  1. [optuna (github)](https://github.com/optuna/optuna) — tpe and pruning-based hyperparameter optimization framework
  2. [google or-tools](https://developers.google.com/optimization) — c++/python solver for routing (vrp/tsp), scheduling, and mixed-integer linear programming
  3. [pycma — cma-es (github)](https://github.com/CMA-ES/pycma) — derivative-free evolutionary optimization for tuning trajectory and control parameters

---

### 15. neuroscience-inspired, neuromorphic & cognitive ai

#### 37.1 computational neuroscience basics

- [ ] neuron models (hodgkin-huxley, lif, izhikevich)
- [ ] synaptic plasticity (hebbian, stdp)
- [ ] neural coding (rate, temporal, population)
- [ ] hopfield networks
- [ ] boltzmann machines
- [ ] predictive coding
- [ ] free energy principle and active inference
- [ ] hippocampus and memory models
- [ ] dendritic computation

#### 37.2 spiking neural networks & neuromorphic computing

- [ ] spiking neural networks (snn)
- [ ] surrogate gradient training
- [ ] ann-to-snn conversion
- [ ] event-driven processing
- [ ] snntorch, norse, brian2
- [ ] neuromorphic chips (loihi, spinnaker)
- [ ] memristors and in-memory computing

#### 37.3 cognitive science & agi concepts

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

#### 37.4 human-ai interaction

- [ ] human-in-the-loop ml
- [ ] interactive machine learning
- [ ] trust calibration
- [ ] shared autonomy
- [ ] social and assistive robot interaction
- [ ] affective computing
- [ ] gesture and gaze interfaces

**resources:**

- **video lectures:**
  1. [neuromatch academy — computational neuroscience course](https://compneuro.neuromatch.io/) — neuron models, neural coding, and brain-inspired computing
- **books, papers & repositories:**
  1. [snntorch tutorials: spiking neural networks in pytorch](https://snntorch.readthedocs.io/en/latest/tutorials/index.html) — training spiking neural networks (snns) with surrogate gradients
  2. [wulfram gerstner et al. — neuronal dynamics (epfl free online book)](https://neuronaldynamics.epfl.ch/) — reference book on lif, hodgkin-huxley, and stdp neuron models
  3. **artem kirsanov & active inference:** [youtube channel](https://www.youtube.com/@ArtemKirsanov) · [book page](https://mitpress.mit.edu/9780262045353/) — clear visual explanations of neuron models and active inference decision-making in biology and robotics

---

### 16. ai for healthcare, biology & science

#### 39.1 medical imaging ai

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

#### 39.2 clinical & health data ai

- [ ] electronic health record (ehr) modeling
- [ ] clinical nlp
- [ ] ecg and eeg signal analysis
- [ ] wearable sensor data
- [ ] clinical risk prediction
- [ ] clinical validation of ml models
- [ ] health data privacy (kvkk, hipaa)

#### 39.3 bioinformatics & genomics

- [ ] sequence alignment (blast)
- [ ] variant calling
- [ ] gene expression analysis
- [ ] single-cell analysis
- [ ] dna and rna language models
- [ ] genome-wide association studies (gwas)
- [ ] biological databases

#### 39.4 structural biology & drug discovery

- [ ] protein structure prediction (alphafold)
- [ ] protein language models (esm)
- [ ] protein design (rfdiffusion)
- [ ] molecular graph neural networks
- [ ] molecular generation
- [ ] molecular docking
- [ ] qsar and admet prediction
- [ ] cheminformatics (rdkit)
- [ ] equivariant networks (egnn, se(3)-transformers)

#### 39.5 scientific machine learning

- [ ] physics-informed neural networks (pinns)
- [ ] neural operators (fno, deeponet)
- [ ] surrogate modeling
- [ ] weather and climate models (graphcast)
- [ ] materials discovery
- [ ] learned physics simulators
- [ ] equation discovery (sindy)
- [ ] digital twins

#### 39.6 other application domains

- [ ] agriculture ai (crop disease, yield prediction)
- [ ] energy ai (load forecasting, smart grid)
- [ ] industrial ai (predictive maintenance, quality control)
- [ ] cybersecurity ai (intrusion and malware detection)
- [ ] education ai (adaptive learning, tutoring)
- [ ] legal nlp

**resources:**

- **video lectures:**
  1. [steve brunton — physics-informed machine learning & sindy (youtube)](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — physics-informed neural networks, dynamical system discovery, and digital twins
- **books, papers & repositories:**
  1. [monai (github)](https://github.com/Project-MONAI/MONAI) & [nnu-net (github)](https://github.com/MIC-DKFZ/nnUNet) — open-source tools for 3d medical image segmentation and detection (dicom/nifti)
  2. [geometric deep learning blueprint](https://geometricdeeplearning.com/) — unified math of $se(3)/e(3)$ equivariant networks across 3d point clouds and molecules

---

### 17. advanced llm engineering

#### 42.1 pretraining data & infrastructure

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

#### 42.2 post-training

- [ ] sft data curation
- [ ] preference data collection
- [ ] dpo variants (ipo, kto, orpo, simpo)
- [ ] rejection sampling and best-of-n
- [ ] distillation from larger models
- [ ] model merging (ties, dare, slerp)
- [ ] safety tuning
- [ ] chat templates
- [ ] function-calling fine-tuning

#### 42.3 reasoning models

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

**resources:**

- **books, papers & repositories:**
  1. **reasoning from scratch (sebastian raschka):** [github repo](https://github.com/rasbt/reasoning-from-scratch) — line-by-line pytorch guide implementing chain-of-thought reasoning, rejection sampling, grpo rl, and test-time search

#### 42.4 context & memory

- [ ] long-context extension (yarn, ntk-aware rope scaling)
- [ ] kv cache compression
- [ ] lost-in-the-middle problem
- [ ] prompt caching
- [ ] retrieval vs long context
- [ ] external memory for agents
- [ ] context engineering

#### 42.5 inference serving

- [ ] continuous batching
- [ ] prefix caching
- [ ] speculative decoding in serving
- [ ] disaggregated prefill / decode
- [ ] constrained decoding (grammar, json schema)
- [ ] model routing and cascades
- [ ] latency and cost optimization

#### 42.6 llm evaluation

- [ ] benchmarks (mmlu, gsm8k, humaneval, swe-bench)
- [ ] llm-as-judge pitfalls
- [ ] arena-style elo evaluation
- [ ] lm-evaluation-harness
- [ ] hallucination measurement
- [ ] agent evaluation
- [ ] building private domain eval sets
- [ ] calibration of llms

#### 42.7 code ai

- [ ] code language models
- [ ] code completion and infilling
- [ ] program synthesis
- [ ] automated program repair
- [ ] test generation
- [ ] software engineering agents
- [ ] execution feedback and sandboxing
- [ ] formal proof assistants with llms (lean)

#### 42.8 advanced agents

- [ ] model context protocol (mcp) and tool protocols
- [ ] computer-use and gui agents
- [ ] browser agents
- [ ] multi-agent frameworks
- [ ] agent reliability and failure modes
- [ ] prompt engineering
- [ ] llm-driven robot control (saycan, code-as-policies)
- [ ] human-in-the-loop agent design

**resources:**

- **video lectures:**
  1. [andrej karpathy — deep dive into llms (youtube)](https://www.youtube.com/watch?v=7xTGNNLPyMI) — end-to-end overview of pretraining, sft, rlhf, and reasoning models
- **books, papers & repositories:**
  1. [hugging face — ultra-scale playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — zero, fsdp, data pipelines, and large-scale gpu cluster training
  2. [eleutherai — lm-evaluation-harness (github)](https://github.com/EleutherAI/lm-evaluation-harness) & [model context protocol](https://modelcontextprotocol.io/) — standard llm evaluation harness and agent tool-calling protocol
  3. [code as policies](https://code-as-policies.github.io/) — generating robotic control policy code directly with language models
