- Q: What course topic was highlighted as recently taught and popular again?
  A: Word vectors and neural representations for language, specifically word2vec as an introductory system.

- Q: Who is the instructor introducing the course?
  A: Christopher Manning.

- Q: What is the main technical topic of today's content?
  A: The word2vec algorithm and learning word vector representations.

- Q: What year was word2vec introduced?
  A: 2013.

- Q: What are word vectors also called?
  A: Embeddings or neural word representations.

- Q: What is the core idea behind embeddings?
  A: Represent each word as a dense real-valued vector such that words with similar meanings have similar vectors.

- Q: What is a key limitation of one-hot word representations?
  A: They don't encode semantic similarity between words (e.g., motel and hotel would be orthogonal).

- Q: What linguistic concept contrasts denotational semantics with distributional semantics?
  A: Denotational semantics assigns an explicit meaning/denotation to a word; distributional semantics uses the company a word keeps (its context) to infer meaning.

- Q: What phrase summarizes the distributional approach to meaning (often attributed to J.R. Firth)?
  A: "You shall know a word by the company it keeps."

- Q: Why are high-dimensional word vector spaces useful?
  A: They capture nuanced similarities and relations among many words in many dimensions, not just simple, obvious features.

- Q: What is the typical dimensionality for word vectors in practice?
  A: Common sizes are 100, 300, up to 1,000 or 2,000 dimensions in modern models.

- Q: What two types of word vectors are used in word2vec training?
  A: A center word vector and an outside (context) word vector.

- Q: What is the basic training objective of word2vec described in the talk?
  A: Maximize the probability of observing context words given a center word (equivalently minimize the average negative log likelihood across the corpus).

- Q: In word2vec, how is the probability of a context word given a center word computed?
  A: Using a softmax over the dot products of the center word vector with each outside word vector.

- Q: What mathematical transformation helps turn dot product scores into probabilities?
  A: The softmax function (exponentiate and normalize).

- Q: How are word vectors learned in word2vec?
  A: By starting with random vectors and using gradient-based optimization to adjust them so the predicted context probabilities fit the observed text.

- Q: Why are two vectors per word (center and outside) used in the model?
  A: It simplifies the math and often improves the quality of learned representations by separating roles for center vs. context usage.

- Q: What is a common way to visualize high-dimensional embeddings?
  A: Dimensionality reduction like t-SNE (versus PCA).

- Q: What is meant by "localist" versus "distributed" representations in the talk?
  A: Localist: each word has a single point in the space; Distributed (embeddings): words are represented by vectors in a high-dimensional space with similarities encoded in distances and directions.

- Q: How is similarity between words like "bank" (financial institution) and "bank" (river bank) captured in embeddings?
  A: They share contextual usage, so their vectors become similar due to being embedded based on their contexts, despite multiple senses.

- Q: What is an example of a context window size mentioned in the talk?
  A: A window size of 2 to the left and 2 to the right (context words around a center word).

- Q: What is the endpoint of the lecture regarding math details?
  A: Derive gradients for the word vectors to minimize the average negative log likelihood; computers typically perform these derivatives automatically.

- Q: What is a practical takeaway about implementing word2vec?
  A: It’s a tractable optimization problem with a large parameter space (word vectors); modern frameworks compute gradients automatically and handle large vocabularies.

- Q: How do practitioners handle the problem of many parameters in word2vec?
  A: Use large-scale optimization on GPUs and libraries that implement automatic differentiation; training is feasible with big corpora.

- Q: What upcoming topics did the lecturer promise to cover after today?
  A: More details on the math, optimization, and practical IPython notebook explorations of word2vec and its uses.