Here are Q&As distilled from the lecture transcript.

1) Q: What is the basic idea of gradient descent?
   A: Start with a loss function J, compute its gradient (the direction of steepest ascent), and move a small step opposite to the gradient (scaled by a learning rate alpha) to walk downhill toward a minimum.

2) Q: Why are small learning rates important?
   A: To avoid overshooting the minimum. Too large a step can land you far away or at a worse point; too small a step makes optimization slow.

3) Q: What is stochastic/mini-batch gradient descent and why is it used?
   A: Instead of computing the gradient over the entire dataset, you compute it on a small subset (mini-batch), which is a noisy, approximate gradient. This is much faster and, in neural nets, the added noise often helps optimization.

4) Q: How are word vectors initialized and why is random initialization important?
   A: Word vectors are initialized with small random numbers. If you start with zeros, you get symmetry breaking problems and learning stalls.

5) Q: What is the basic idea behind word2vec?
   A: Treat each word as a vector and learn to predict surrounding context words from a center word (or vice versa) using a simple probabilistic model. The learned vectors capture semantic relationships.

6) Q: Why are there two sets of vectors in word2vec (inside vs outside words)?
   A: The two vectors (center word and context word) make the math simpler and avoid a quadratic term that would arise if they were the same. In practice, the two vectors are often learned separately and then averaged for each word.

7) Q: What is skip-gram vs CBOW in word2vec?
   A: Skip-gram predicts context words given a center word; CBOW predicts the center word from its context. Skip-gram is typically simpler and works well.

8) Q: What is negative sampling and why is it used?
   A: Instead of a full softmax over the entire vocabulary, negative sampling trains the model to distinguish the true context word from a few randomly chosen negative samples. It’s faster and often effective.

9) Q: How are negative samples chosen?
   A: Sampled from the unigram distribution, often adjusted by raising probabilities to the 3/4 power to balance frequent and rare words, which gives a bit more emphasis to less frequent words than pure frequency.

10) Q: What is GloVe and how does it relate to word vectors?
    A: GloVe (Global Vectors) is a count-based model that uses ratios of co-occurrence probabilities and a log-bilinear formulation to produce word vectors with linear semantic components. It combines ideas from co-occurrence counts with a vector space representation.

11) Q: What is intrinsic vs extrinsic evaluation in word vectors?
    A: Intrinsic evaluation tests the vector properties themselves (e.g., analogies, word similarity) and is fast but may not translate to downstream tasks. Extrinsic evaluation tests how vectors improve performance on real tasks (e.g., named entity recognition).

12) Q: How is word similarity typically evaluated intrinsically?
    A: Humans rate word similarities (e.g., plane vs. car, tiger vs. tiger) and model predictions are correlated with human judgments to measure quality.

13) Q: How are word vectors used in named entity recognition (NER)?
    A: Word vectors are used as inputs to a window classifier or neural network. The window around a word provides context; the model learns to classify the center word (e.g., whether it is a location, person, etc.) using the vector representations.

14) Q: How does a neural classifier differ from a linear classifier?
    A: A neural classifier uses distributed representations (learned word vectors) that move through one or more nonlinear layers, allowing the final linear classifier to operate on a transformed internal representation, enabling more complex decision boundaries.

15) Q: What is cross-entropy loss and how is it used in PyTorch?
    A: Cross-entropy loss measures the difference between the true distribution (often a one-hot label) and the model’s predicted distribution. In the simple case of a single correct class, it reduces to the log likelihood of the correct class. In PyTorch, this is typically implemented as cross-entropy loss for multi-class classification tasks.

16) Q: How does a biological neuron inspire artificial neural networks?
    A: A neuron sums many inputs, applies a nonlinearity, and produces an output that can feed into many other neurons. In deep networks, multiple layers of such nonlinear transformations allow learning complex functions. The end result is a linear classifier in the final hidden representation, even though the internal representations are learned through nonlinearities.

17) Q: Why do word vectors often use a nonlinear network rather than a simple linear model?
    A: The nonlinear hidden layers create powerful internal representations that make it easier to separate classes or predict targets, with the final layer often acting linearly on the learned internal representation.

18) Q: What is a “sparse coding” approach in word representations, and how does it relate to senses?
    A: Sparse coding attempts to decompose a single word vector into multiple sparse components corresponding to different senses. This can recover distinct sense vectors from one vector, though contemporary practice often uses contextualized representations to handle sense more dynamically.

19) Q: What is contextual word representation, and how does it differ from single-vector word representations?
    A: Contextual representations account for the word’s meaning in a specific context (e.g., different senses of “bank” depending on surrounding words). They can be decomposed or understood via sparse/coding approaches, but modern methods often build dynamic vectors conditioned on context.

20) Q: What should you do if you’re working on word2vec in this course?
    A: For this course, word2vec implementation is not required in Spring quarter; you should wait for the updated assignment. The lecture covers the core ideas, initialization, and training methods (e.g., skip-gram, negative sampling) to understand how word vectors are learned.

If you’d like, I can tailor these into flashcards or convert them into a printable Q&A sheet.