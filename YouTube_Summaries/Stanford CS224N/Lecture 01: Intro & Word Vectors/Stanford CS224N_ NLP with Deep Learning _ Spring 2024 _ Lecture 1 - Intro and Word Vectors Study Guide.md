Study Guide: Key Concepts from the Transcript

1) Course overview and logistics
- Instructor: Christopher Manning; course focuses on deep learning methods for natural language processing (NLP) from foundations to modern techniques.
- What you’ll learn:
  - Foundations: word vectors, feedforward nets, recurrent nets, attention.
  - Core NLP methods: transformers, encoder/decoder models, large language models, pre-training and adaptation, interpretability.
  - Practical skills: building NLP systems (e.g., text classification, information extraction) via projects.
- Assessments:
  - Four assignments (about half the grade) plus a final project (two variants: custom or default scaffolding).
  - Participation contributes a small portion.
  - Emphasis on doing your own work; AI tools ok for assistance, but not to complete assignments for you.
- Course structure: starts with simple concepts (word vectors) and progresses to complex models and practical tools (PyTorch, GPUs, Google Cloud).

2) Human language, meaning, and learning goals
- Two broad aspects of language:
  - Communication and social use (language as a social tool, flexible and nuanced).
  - Cognitive scaffolding for thought and planning (language as a tool for higher-level cognition and writing).
- Writing as a cognitive tool: writing empowered knowledge sharing and long-term information transfer.
- Language change: languages are constructed and evolve with use, especially by younger speakers.
- Meaning in NLP:
  - Denotational semantics: meaning as signifier-signified pairs (word and its denotation).
  - Word sense and context: meanings depend on usage; language’s social and contextual aspects matter.
- Early NLP representations:
  - WordNet: a traditional thesaurus-like resource describing word relations; limited for computational meaning (nuance, slang, context).
  - Distributional semantics: meaning derived from context (“You shall know a word by the company it keeps” – Wittgenstein, Firth).
  - Localist vs. distributed representations:
    - Localist: each word has a single discrete representation (less flexible for nuance).
    - Distributed representations (embeddings): dense, high-dimensional vectors capturing semantic relatedness; similarity corresponds to vector proximity and direction.

3) Word vectors, embeddings, and the intuition
- Representing words as vectors:
  - One-hot encoding: each word is a unique basis vector; lacks inherent similarity structure.
  - Dense word embeddings: each word is a real-valued vector in a high-dimensional space (e.g., 300 dimensions).
- Why embeddings are useful:
  - Similar words have similar vectors; cosine similarity and dot products capture similarity.
  - High-dimensional spaces allow nuanced relationships and multiple senses to be encoded in a single vector.
- Interpretations in the embedding space:
  - Proximity of “bank” to “money” or “finance” vs. “creek” or “shore” shows semantic similarity.
  - Directions in space can encode relational structure (e.g., analogies, though not trivial to extract manually).

4) Word2vec: what it is and why it matters
- Introduced by Mikolov et al. at Google, 2013; a simple, fast method to learn word vectors from large text corpora.
- Core idea:
  - Learn a vector for each word type by predicting surrounding context words given a center word (or vice versa, depending on the exact variant).
  - Use a probabilistic objective to maximize the likelihood of observed word-context co-occurrences.
- Basic terminology:
  - Word type vs. word token: a type is a unique word form (e.g., “bank” as a type); a token is an occurrence in text.
  - Context window: a fixed number of words to the left and right of a center word (e.g., window size m = 2).
- What word2vec optimizes:
  - A probabilistic model where P(context word | center word) is defined using the dot product of their vectors.
  - The goal is to maximize the probability of observed context words for all positions in the corpus.
- Two key tricks to make the model practical:
  - Use gradient descent to minimize the negative log-likelihood.
  - Use the softmax function to convert dot products into a probability distribution over the vocabulary.
- Parameters of the model:
  - Vectors for each word type (and sometimes separate vectors for center vs. outside words to simplify math).
  - The total number of parameters is large (roughly vocab_size × vector_dim × 2, for center and context vectors).

5) How word2vec works in practice (high-level outline)
- Input: A large text corpus (a sequence of word tokens).
- For each position t in the text:
  - Treat the word at t as the center word.
  - Consider the words within a fixed window around t as context.
  - Use the vectors (center word vector and context word vectors) to compute the probability of each context word given the center word.
- Objective: Maximize the likelihood of the actual context words appearing near the center word.
- Mathematics (conceptual):
  - Represent each word type with a vector.
  - Define P(context word | center word) via a softmax over all vocabulary items, using the dot product of center and context vectors.
  - The objective is the average negative log-likelihood across all center-context pairs in the corpus.
  - Optimize by computing gradients with respect to all word vectors and updating them (stochastic gradient descent / backpropagation).
- Intuition behind the math:
  - The derivative structure often looks like observed minus expected (the difference between the actual context and the model’s predicted distribution), guiding updates to word vectors.
- Practical considerations:
  - Very large parameter space requires efficient optimization and sometimes approximations (e.g., negative sampling in many word2vec implementations, though the transcript focuses on the softmax formulation).
  - Dimensionality choices (e.g., 100, 300, up to 1000+ dimensions) impact performance and memory.

6) Important concepts and terms
- Embeddings / word vectors: dense vector representations of words in a high-dimensional space.
- Vector space properties:
  - Proximity corresponds to semantic similarity.
  - Directions and relationships can encode linguistic regularities.
- Center word vs. outside (context) word vectors: sometimes separated to simplify optimization.
- Softmax: a function that converts a vector of real numbers into a probability distribution over a discrete set (the vocabulary).
- Negative log-likelihood: the objective to minimize; equivalent to maximizing the likelihood of observed data.
- Context window: the number of surrounding words used to predict or be predicted by the center word.
- Gradient descent: the optimization method used to adjust word vectors to maximize the objective.
- Correlation between context and meaning: distributional semantics relies on co-occurrence statistics to infer meaning.

7) Common questions and conceptual clarifications (based on the Q&A in the transcript)
- Contextual meaning vs. single embeddings:
  - Word2vec learns a single embedding per word type in this setup; it does not capture context-specific senses yet. Contextual embeddings (not covered in detail here) extend this idea to represent words differently in different contexts.
- Number of dimensions:
  - Typical dimensions range from a few hundred to a few thousand; more data and model complexity can justify larger vectors.
- Distance vs. directions in the embedding space:
  - Both distance and direction carry meaning. Similar words cluster together (distance), and certain relationships are captured by vector directions (e.g., analogies or relational patterns).
- Single embedding per word vs. multiple senses:
  - In basic word2vec, a word has a single embedding. The same vector can become influenced by multiple senses (e.g., “bank” financial vs. riverbank). Contextual representations handle multiple senses more explicitly in later work.
- Normalization and bounds of embeddings:
  - Embeddings are not inherently bounded; normalization or regularization can be used, but it’s not mandatory. The optimization process tends to keep values in reasonable ranges.

8) Suggested study tasks and practice problems
- Conceptual:
  - Explain the difference between denotational semantics and distributional semantics. Why is distributional semantics more practical for NLP?
  - Describe why one-hot representations are limited for capturing word meaning.
  - Summarize how word2vec uses co-occurrence in a context window to learn word vectors.
- Technical derivation (high level, not full math):
  - Sketch how the softmax probability P(context | center) is formed from dot products of vectors.
  - Outline the idea of differentiating the average negative log-likelihood with respect to the center word vector, and why observed-context terms minus expected-context terms appear in the gradient.
  - Explain why the gradient updates move word vectors to increase the probability of observed context words.
- Practical implementation:
  - If given a small corpus, describe how you would set up the word2vec training loop (centers, contexts, loss calculation, gradient updates).
  - Compare and contrast full softmax with common approximations in practice (e.g., negative sampling) and discuss trade-offs.
- Reflection questions:
  - What are the limitations of a single embedding per word with respect to polysemy? How might contextualized embeddings address this?
  - How does the dimensionality of embeddings affect the ability to capture semantic nuances? What are signs that you should increase or decrease dimensions?
  - How do embedding spaces help with downstream tasks like synonym detection, analogy tasks, or information retrieval?

9) Quick recap
- Word2vec is a foundational method for learning word embeddings from large text corpora by predicting context words from a center word (or vice versa) using a softmax-based objective.
- Embeddings provide a dense, continuous representation of word meaning, enabling semantic similarity and relational structure to emerge from data.
- Understanding word meaning in NLP involves both how words relate to each other (distributional semantics) and how meaning is used in social and cognitive contexts.
- The course aims to build from these foundations to modern NLP techniques and practical system-building.

If you want, I can turn this into a printable checklist or condense it into a one-page cram sheet with all the key terms and formulas highlighted.