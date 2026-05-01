Sure! Here are flash cards extracted from the transcript. Each card has a question (Q) and an answer (A).

1)
Q: What are the two main purposes of Assignment 2 in the lecture?
A: (1) To understand what neural networks compute mathematically and how they compute it, and (2) To learn about dependency parsing and start using PyTorch for implementing neural nets (with PyTorch tutorials).

2)
Q: Why is PyTorch introduced in Assignment 2?
A: PyTorch is a leading deep learning framework; it helps you implement neural nets, and later assignments (e.g., Assignment 3) are scaffolded to show basic usage.

3)
Q: What is the key difference between a neural network’s middle layer computations and a single logistic regression model?
A: Neural networks stack cascades of small logistic regressions, allowing intermediate representations to be learned by the network itself, not just predefined features.

4)
Q: What is the main idea behind using layers with nonlinear activations in neural networks?
A: Nonlinear activations allow the network to learn complex, nonlinear functions; linear multi-layer compositions would only yield a linear transformation, which has no extra representational power.

5)
Q: Name three activation functions discussed and a key property of each.
A: Sigmoid (maps to probabilities, non-negative outputs); Tanh (values in [-1, 1], a scaled sigmoid); ReLU (rectified linear unit: 0 for negative, linear for positive, easy gradient flow).

6)
Q: Why did ReLU become a popular default activation function for a while?
A: It provides simple, always-present gradients in the positive region and often yields good practical learning performance, despite units being “dead” when inactive.

7)
Q: What are some ReLU variants mentioned?
A: Leaky ReLU (small slope in the negative region), Parametric ReLU (learnable negative slope), and more recent swish and gelu nonlinearities.

8)
Q: What is the core idea of gradient-based learning in neural networks?
A: Use gradients (derivatives) of the loss with respect to parameters to guide optimization, typically via stochastic gradient descent.

9)
Q: In the context of neural nets, what does the Jacobian represent?
A: The Jacobian is the matrix of partial derivatives, representing how each output component changes with respect to each input component (generalization of a derivative to vectors/matrices).

10)
Q: What is the Hadamard product?
A: Elementwise multiplication of two vectors (or matrices) of the same shape, producing a vector (or matrix) of the same shape.

11)
Q: When computing ds/dW in a neural network layer, why is the outer product used?
A: To align with the shape convention so the gradient has the same shape as W (n by m); ds/dW is delta times dz/dW, which ends up as delta^T x^T, an outer product giving the correct matrix shape.

12)
Q: What is the shape convention vs. Jacobian form, and why can this be confusing?
A: Jacobian form aligns with chain-rule math (matrices of derivatives), while the shape convention aligns with how gradients are stored in code (so they can be subtracted from parameters). People choose different representations for practical reasons; frameworks often prefer the shape convention.

13)
Q: What are forward and backward passes in a computation graph?
A: Forward pass computes the output values by applying functions topologically from inputs to outputs; backward pass uses the chain rule to propagate gradients from the output back to inputs.

14)
Q: What are the two essential components of backpropagation mentioned?
A: (1) Use the chain rule to compute gradients, and (2) store intermediate results to avoid recomputing them (dynamic programming-like efficiency).

15)
Q: How does automatic differentiation relate to backpropagation?
A: Automatic differentiation uses the same chain-rule principles to compute gradients automatically, enabling efficient backward passes through complex computation graphs.

16)
Q: What is topological sorting in the context of neural networks?
A: A way to order computations in a DAG so that every variable is computed only after all its dependencies, enabling a correct forward pass.

17)
Q: Why is gradient checking with numeric gradients useful?
A: It helps verify that the analytic gradients (backpropagation) are implemented correctly by comparing them to finite-difference estimates.

18)
Q: Why is numeric gradient checking typically not used for training, despite being useful for validation?
A: It is very slow because it requires evaluating the function many times for each parameter, making it impractical for training large models.

19)
Q: What is the educational value of understanding the “under the hood” math of neural nets, according to the lecture?
A: It helps diagnose issues like exploding/vanishing gradients, understand why models work, and enables deeper learning beyond using frameworks as black boxes.

20)
Q: What is the general computation graph requirement for backpropagation to work?
A: The graph must be a DAG (no cycles) so a topological order can be established for forward and backward passes.

21)
Q: What is the core goal of the backpropagation algorithm when computing a gradient for a parameter like W?
A: To compute the derivative of the loss with respect to W efficiently by reusing shared intermediate gradients (the upstream gradient) and applying the local gradient at each node.

22)
Q: How does the lecture describe the practical role of deep learning frameworks today?
A: They automate the forward and backward passes over a computation graph, but require you to implement the local derivatives for custom layers/functions; they provide structure and speed for training rather than solving all math automatically.

23)
Q: What is the “shape convention” in practice when implementing a neural network layer?
A: Gradients are reshaped to match the parameter shapes (e.g., ds/dW as an n-by-m matrix) so they can be subtracted from the corresponding parameters during optimization.

24)
Q: In the context of a neural network layer, what is the typical form of ds/dx if x is an input vector?
A: It is computed as the upstream gradient delta times the local gradient with respect to x; when x is an input to a linear layer, dz/dW and dz/dx contribute to the final gradient via the chain rule.

25)
Q: What is the takeaway about the computational complexity of backward vs. forward passes?
A: If done correctly, the backward pass has the same Big-O complexity as the forward pass, since it reuses computations and avoids recomputation.

These cards should cover the core concepts and details from the lecture. If you want more, I can add or tailor cards to specific topics (e.g., a deeper dive into a particular activation function or a more detailed worked example).