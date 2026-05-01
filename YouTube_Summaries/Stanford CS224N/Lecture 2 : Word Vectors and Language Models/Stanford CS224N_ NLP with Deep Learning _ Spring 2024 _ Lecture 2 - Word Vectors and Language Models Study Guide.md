Study Guide: Word Vectors, Evaluation, and Intro to Neural Nets

1) Course content overview (what to learn)
- Optimization basics for training models
- Word representations: word2vec (skip-gram and CBOW), variants, and alternatives (e.g., co-occurrence / GloVe)
- Evaluation of word vectors: intrinsic (similarity/analogy) vs extrinsic (downstream tasks)
- Word senses and contextual representations
- Introduction to neural networks for classification
- Practical notes: assignments, office hours, and upcoming tools (e.g., PyTorch)

2) Gradient-based optimization (recap)
- Goal: minimize a loss function J(θ)
- Gradient descent idea: move parameters θ downhill using the gradient ∇J(θ)
- Learning rate α: small step size to avoid overshooting (typical values 1e-3, 1e-4, 1e-5)
- Stochastic gradient descent (SGD) / mini-batch SGD:
  - Use a small subset (e.g., 16–32 examples) to estimate the gradient
  - Much faster and often yields better performance due to beneficial noise
- Why random initialization matters:
  - Initialize vectors with small random values to avoid symmetry and enable learning
  - All-zero initialization would stall learning

3) Word vectors and word2vec (key ideas)
- Objective: learn word vectors by predicting surrounding (context) words for a center word
- Bag-of-words style: context windows, dot products, and a probability distribution over outside words
- Two main vector roles (disjoint in standard word2vec): center word vectors and outside/context word vectors
- Training signal: update vectors to improve predicting actual context words
- Results: learned vectors capture semantics and word relationships; simple math yields surprisingly strong results

4) Demonstrations and practical observations (what makes word vectors useful)
- Visualization and similarity:
  - Similar words have similar vectors (e.g., bread ≈ croissant in vector space)
  - Use simple similarity queries to find nearest neighbors (e.g., nearest words to USA)
- Analogy (vector arithmetic):
  - King - man + woman ≈ Queen
  - Examples: Australia:beer::Russia:vodka; pencil:sketching::camera:photographing
- Vector components and “senses”:
  - Words can have multiple senses (bank, jaguar, pike, etc.)
  - Common approach: a single word vector is a weighted average of sense vectors (superposition)
  - Sparse coding ideas: recover sense components from a single word vector using high-dimensional sparse representations
- Multi-sense and context:
  - Contextual word vectors (beyond this lecture) aim to handle multiple senses directly

5) Word co-occurrence and alternative approaches (co-occurrence matrices and GloVe)
- Co-occurrence idea:
  - Build a matrix of word-by-context counts (or co-occurrence counts) within a window
  - A word vector could be derived from the row/column representations, but a full 400k x 400k matrix is impractical
- Dimensionality reduction:
  - Use techniques like PCA or SVD (singular value decomposition) to reduce dimensionality
  - Latent semantic analysis (LSA) and early count-based approaches
- GloVe (Global Vectors):
  - Idea: model log co-occurrence probabilities with a bilinear model
  - Focus on linear semantic components: ratios of co-occurrence probabilities encode meaning differences
  - Log-transform and a bilinear model help produce interpretable linear directions in vector space
  - Adds bias terms and frequency handling (practical trade-offs)
- Connection between count-based and predictive models:
  - Count-based methods can produce useful vectors, and GloVe provided a bridge between co-occurrence statistics and vector space properties

6) Evaluation of word vectors (intrinsic vs extrinsic)
- Intrinsic evaluation:
  - Word analogies: how well vector arithmetic captures relationships
  - Word similarity: compare model-derived similarity scores to human judgments (correlation with human ratings)
  - Findings:
    - Simple SVD on counts can be reasonable but often underperforms newer methods
    - Word2vec CBOW/Skip-gram and GloVe typically rank higher on standard intrinsic evaluations
- Extrinsic evaluation (downstream tasks):
  - Named entity recognition (NER) as a typical task
  - Vector features fed into a classifier can boost performance
  - Intrinsic gains often correlate with improvements in downstream tasks

7) Word senses and context in practice
- Multi-sense challenge:
  - Some words have many senses; a single vector may mix senses
  - Approaches:
    - Sense-specific tokens (bank1, bank2, jaguar1, jaguar2, etc.) with separate vectors
    - Superposition (weighted average) of sense vectors to form a single word vector
    - Sparse coding to recover interpretable sense components from a single vector
- Practical takeaway:
  - For many tasks today, single-vector representations are used, with context-aware models increasingly handling sense disambiguation

8) Intro to neural networks for classification (how classifiers fit in)
- Simple classifier idea:
  - Given a window of words, use their word vectors as input
  - Concatenate vectors (e.g., 5 words × 100-dim = 500-dim input)
  - Pass through a neural network layer (or layers) with weights W and bias b
  - Apply a non-linearity (e.g., sigmoid / tanh)
  - Final linear layer produces a score; apply logistic (sigmoid) to get a probability
- End-to-end view:
  - Word vectors are learned (or fine-tuned) as part of the classifier
  - Intermediate representations (hidden layers) enable nonlinear decision boundaries
  - The final linear classifier operates on the learned internal representation
- Practical note on loss:
  - PyTorch users typically use cross-entropy loss for multi-class classification
  - If you have a single binary label (location vs not location), cross-entropy reduces to a log-likelihood style loss for the positive class
  - Conceptually: cross-entropy compares model output probabilities to true labels

9) Practicalities and tips for building models
- Training signals and losses:
  - For word2vec-style models: negative sampling or hierarchical softmax are efficient alternatives to full softmax
  - Negative sampling: maximize probability of the true context word while pushing sampled negative words away
  - Unigram distributions and sampling: use word frequencies raised to the 3/4 power to balance common and rare words
- PyTorch caveat:
  - When you implement classifiers in PyTorch, use cross-entropy loss for multi-class problems
  - For binary location/not-location tasks, cross-entropy with a single output neuron is common
- Practical reminders:
  - Start with random small-valued vectors for initialization
  - Keep learning rate small to ensure stable convergence
  - Expect gradient noise to help optimization in neural nets (SGD with mini-batches)
  - Use intrinsic tasks to gauge word vector quality, then verify improvements on extrinsic tasks (NER, web search, etc.)

10) A quick reminder about neurons and neural networks (conceptual intuition)
- Biological neurons:
  - Multiple inputs feed into a neuron; inputs are weighted and summed
  - Activation is nonlinear and can drive outputs to other neurons
  - Biological neuron spiking behavior inspired the binary/continuous activations used in neural networks
- Artificial neural networks:
  - Use multiple layers of linear transforms and nonlinear activations
  - Intermediate layers serve as learned representations that make the final classification easier
  - More layers (deeper networks) can model more complex functions and representations

11) Quick glossary of terms
- Word2vec: predictive model learning word vectors by predicting context words
- Skip-gram: predict surrounding words given the center word
- CBOW (Continuous Bag of Words): predict the center word from surrounding context
- Negative sampling: efficient approximation to softmax for training word vectors
- Softmax: normalization to produce a probability distribution over a vocabulary
- GloVe: global vectors; count-based method