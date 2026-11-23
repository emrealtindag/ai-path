# machine learning and deep learning

engineering curriculum, mathematical representations, optimization engines, and curated resources for statistical learning, neural networks, and physical robot learning.

---

## architecture overview

machine learning models extract functional representations from statistical data through mathematical optimization:

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

## study checklist

### 01. statistical learning fundamentals
- [ ] empirical risk minimization (erm), generalization error, and bias-variance decomposition
- [ ] linear regression, ordinary least squares (ols), and regularized objectives (ridge l2, lasso l1)
- [ ] logistic regression, maximum likelihood estimation (mle), and maximum a posteriori (map)
- [ ] evaluation metrics: precision, recall, f1-score, roc-auc, and pr-auc under class imbalance
- [ ] classical methods: decision trees, random forests, gradient boosting (xgboost, lightgbm), and support vector machines (svm)

### 02. deep learning foundations and autograd from scratch
- [ ] dynamic computational graphs and reverse-mode automatic differentiation (backpropagation)
- [ ] multi-layer perceptrons (mlp), universal approximation theorem, and activation functions (relu, gelu, silu)
- [ ] weight initialization strategies (xavier/glorot, he/kaiming) and numerical stability
- [ ] loss functions: mean squared error, categorical cross-entropy, focal loss, and contrastive loss (infonce)
- [ ] optimization algorithms: momentum, rmsprop, adam, and adamw with cosine annealing learning rate schedules

### 03. neural network architectures
- [ ] convolutional neural networks (cnn): 2d convolution operations, receptive fields, dilations, and residual connections (resnet)
- [ ] sequence models and attention: scaled dot-product self-attention, multi-head attention, and transformer encoders
- [ ] vision transformers (vit) and patch embeddings for visual feature representation
- [ ] self-supervised representation learning: contrastive learning (simclr), masked autoencoders (mae), and dinov2

### 04. physics-informed and robot learning
- [ ] physics-informed neural networks (pinns): embedding differential equations and boundary conditions into loss formulations
- [ ] reinforcement learning (rl) foundations: markov decision processes (mdp), bellman equations, and value iteration
- [ ] deep policy gradient methods: proximal policy optimization (ppo) and soft actor-critic (sac)
- [ ] robot imitation learning: behavioral cloning (bc), dataset aggregation (dagger), and modern diffusion policies

---

## curated resources

### video lectures & course series
- [andrej karpathy – neural networks: zero to hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ): the undisputed best walkthrough on building micrograd (autograd from scratch), makemore, and transformers from raw python.
- [statquest with josh starmer – machine learning](https://www.youtube.com/playlist?list=PLblh5JKO9Y6qC5p3_ZqfV9i6s1u9V3S1F): clear visual breakdowns of linear regression, cross-entropy, decision trees, and gradient boosting.
- [mit 6.s191 – introduction to deep learning](https://www.youtube.com/playlist?list=PLtBw6njKVU-P7P6sLqY_3Q4K4GZ4_XwL1): fast-paced university lecture series covering cnns, transformers, and generative models.
- [stanford cs231n – deep learning for computer vision](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv): premier graduate course on convolutional networks, optimization, and visual architectures.

### foundational books & academic materials
- [the elements of statistical learning (trevor hastie, robert tibshirani, jerome friedman)](https://hastie.su.domains/ElemStatLearn/): the standard authoritative mathematical textbook for statistical learning and classical ml.
- [deep learning (ian goodfellow, yoshua bengio, aaron courville)](https://www.deeplearningbook.org/): comprehensive theoretical foundations of deep learning architectures and optimization.
- [patterns, predictions, and actions: a story about machine learning (moritz hardt & benjamin recht)](https://mlstory.org/): exceptional modern textbook connecting machine learning with causal inference, feedback loops, and control theory.

### open-source codebases & tools
- [pytorch/pytorch](https://github.com/pytorch/pytorch): premier open-source deep learning framework with dynamic computational graphs.
- [karpathy/micrograd](https://github.com/karpathy/micrograd): tiny 100-line scalar autograd engine implementing backpropagation from scratch.
- [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn): definitive library for classical machine learning algorithms, preprocessing, and evaluation metrics.
- [cleanrl/cleanrl](https://github.com/vwxyzjn/cleanrl): single-file, transparent implementations of deep reinforcement learning algorithms (ppo, sac).
