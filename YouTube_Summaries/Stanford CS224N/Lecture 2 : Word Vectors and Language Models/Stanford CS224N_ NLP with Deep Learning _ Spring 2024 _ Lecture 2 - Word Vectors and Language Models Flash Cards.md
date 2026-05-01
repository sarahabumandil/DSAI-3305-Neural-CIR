Here are flash cards based on the transcript. Front is the prompt (question), back is the answer.

1)
Q: What is gradient descent used for in machine learning?
A: To minimize a loss function by iteratively moving parameters in the direction opposite the gradient, often using a learning rate.

2)
Q: What is stochastic gradient descent (SGD) and why is it preferred in neural nets?
A: SGD updates parameters using the gradient from a small subset (mini-batch) of data, which is faster and often empirically more effective due to the beneficial noise.

3)
Q: Why initialize word vectors with random small numbers in word2vec?
A: To break symmetry; if all vectors start at zero, learning cannot begin because all updates would be the same.

4)
Q: What are the two main components learned in word2vec models?
A: The outside word vectors and the center (inside) word vectors, which are treated as disjoint.

5)
Q: What is the basic idea behind the skip-gram model in word2vec?
A: Given a center word, predict the surrounding context words.

6)
Q: What is the “bag of words” assumption in word2vec?
A: It ignores word order and treats the context as a set of words around the center word, focusing on which words are likely to appear in that context.

7)
Q: Why are two separate vectors (center and outside) used in word2vec instead of one?
A: To avoid quadratic terms and simplify the math; using disjoint vectors prevents the center word from predicting itself in the context in a way that complicates training.

8)
Q: What is negative sampling in word2vec?
A: An alternative to full softmax that trains the model by distinguishing the true context word from a small set of randomly sampled negative words using a logistic loss.

9)
Q: What is the purpose of sampling negative words using the unigram distribution raised to the 3/4 power?
A: To bias negative samples toward more frequent words while not sampling too common words too often, improving training efficiency and quality.

10)
Q: How does GloVe differ from Word2Vec?
A: GloVe is a log-bilinear model derived from word co-occurrence counts; it aims to make the ratios of co-occurrence probabilities linear in the word vectors, enabling linear semantic components.

11)
Q: What is intrinsic evaluation in word vector quality assessment?
A: Evaluating word vectors on tasks like word analogies or word similarity, which measure linguistic properties directly.

12)
Q: What is extrinsic evaluation in word vector quality assessment?
A: Evaluating word vectors on downstream tasks (e.g., named entity recognition) to see if they improve overall system performance.

13)
Q: How can word vectors help with named entity recognition (NER)?
A: They provide dense representations of words in context windows that feed into a classifier, improving the labeling of tokens as location, person, organization, etc.

14)
Q: What is an analogy in word vectors, and how is it computed?
A: It’s a relation like A is to B as C is to D; computed by vector arithmetic such as vec(B) - vec(A) + vec(C) and finding the nearest word to the result.

15)
Q: What happens when you combine multiple word vectors as input to a neural classifier?
A: You get a high-dimensional input (e.g., concatenated vectors) that is transformed by a neural network to produce a nonlinear, more powerful classifier.

16)
Q: In a simple neural classifier, what role does a hidden layer play?
A: It provides a nonlinear transformation that allows linear classification at the final layer to model complex patterns in the input data.

17)
Q: What is cross-entropy loss and why is it important in PyTorch?
A: Cross-entropy loss measures the difference between predicted probabilities and true labels; it’s the standard loss for classification tasks in many frameworks, including PyTorch.

18)
Q: How does a single neuron relate to logistic regression?
A: With a logistic activation, a single neuron behaves like logistic regression; multiple neurons form a network that enables nonlinear decision boundaries.

19)
Q: What is the concept of sparse coding in word vectors?
A: Reconstructing high-dimensional word vectors into a sparse set of interpretable sense components, allowing the recovery of multiple senses from a single vector.

20)
Q: How do intrinsic and extrinsic evaluations relate to word vectors?
A: Intrinsic evaluations test linguistic properties directly, while extrinsic evaluations test the impact of word vectors on real downstream tasks.

21)
Q: What is the basic intuition behind the GloVe model’s use of co-occurrence probabilities?
A: The log ratio of co-occurrence probabilities encodes semantic relationships; this ratio can be approximated linearly in the vector space to capture meaningful dimensions (like solid-liquid-gas).

22)
Q: What is the practical reason for using a windowed context in word2vec and GloVe?
A: To capture local context statistics around a target word, which informs its vector representation based on neighboring words.

23)
Q: What are the two vectors in word2vec commonly referred to as in the discussion?
A: The “center word vectors” (inside word) and the “outside word vectors” (context word vectors).

24)
Q: What is an analogy example given with King, Man, Woman, and Queen?
A: King - Man + Woman ≈ Queen; demonstrates how a linear combination of vectors can yield semantically related words.

25)
Q: Why might one want to perform dimensionality reduction on a word-context co-occurrence matrix?
A: To obtain compact word representations (lower-dimensional vectors) that are more practical and efficient than the full high-dimensional counts matrix.

26)
Q: What is a practical note about assignment readiness mentioned in the transcript?
A: Do not implement word2vec from scratch for the current quarter's assignment; wait for the updated assignment instructions.

27)
Q: What is a “superposition” in the context of word senses?
A: The single word vector can be viewed as a weighted average of sense vectors (sensors), implying multiple senses are blended in one representation.

28)
Q: What is a key takeaway about neural networks from the lecture?
A: They learn hierarchical representations through layered nonlinear transformations, enabling powerful input representations and classification.

29)
Q: What is a common practical use of word vectors in NLP pipelines?
A: As input features to classifiers (e.g., for POS tagging, NER, sentiment analysis) or as initialization for downstream tasks.

30)
Q: What is the relationship between word vector dimensionality and training speed?
A: Higher dimensional vectors capture more nuance but require more computation; demos often use 100 dimensions for speed.

These cards cover the core concepts and details discussed in the transcript.