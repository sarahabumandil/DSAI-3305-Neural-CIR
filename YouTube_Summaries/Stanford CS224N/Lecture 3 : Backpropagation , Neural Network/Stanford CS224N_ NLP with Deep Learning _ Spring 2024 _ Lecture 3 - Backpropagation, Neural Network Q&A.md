Here are Q&A pairs distilled from the lecture transcript.

1) Q: What are the two main purposes of Assignment 2?
   A: (1) To build understanding of what neural networks compute and how they compute it (the math and gradients), and (2) To introduce dependency parsing (language structure) and start using PyTorch for deep learning.

2) Q: Why does the lecture emphasize the cascade of small logistic units in neural networks?
   A: Because neural networks are built from layers of simple units (logistic regressions) that learn useful intermediate representations to feed downstream computations, not just a single flat logistic regression.

3) Q: What does a neural network layer do in terms of x, W, b, and activation?
   A: It computes z = W x + b, then applies a nonlinearity f to produce the next layer: h = f(z). This is typically summarized as a matrix multiplication followed by a bias addition and a nonlinear activation.

4) Q: Why are nonlinear activation functions necessary in neural networks?
   A: Because without nonlinearities (just linear transforms), stacked layers collapse to a single linear transform and lose representational power. Nonlinearities allow the network to approximate complex functions.

5) Q: What was the historical progression of activation functions discussed?
   A: Early thresholds had zero slope (bad for learning). Sigmoid/logistic and tanh introduced gradients. ReLU became dominant due to simple gradient in the positive region and good practical performance, with later variants like leaky ReLU, PReLU, and swish/gelu used in newer models.

6) Q: What is the purpose of gradients in training neural networks?
   A: Gradients tell us the slope of the loss with respect to parameters so we can perform gradient-based optimization (e.g., stochastic gradient descent) to minimize the loss.

7) Q: What is the Jacobian, and when does it appear?
   A: The Jacobian is the matrix of all partial derivatives of outputs with respect to inputs. It appears when you have a function with multiple inputs and outputs (e.g., a layer with weight matrix W mapping an input vector to an output vector).

8) Q: How is the chain rule applied in neural networks with vector/matrix inputs?
   A: Through matrix calculus: when composing functions (layers), you multiply Jacobians (or their appropriate shapes) to propagate gradients backward (the core idea behind backpropagation).

9) Q: What is the Hadamard product?
   A: The Hadamard product is elementwise multiplication of two vectors (or tensors) of the same shape, used frequently when combining upstream gradients with local derivatives.

10) Q: What is the practical “shape convention” for derivatives in this course?
    A: Derivatives with respect to matrices (e.g., ds/dW) are reshaped to have the same shape as the parameter they correspond to (e.g., an n-by-m matrix for ds/dW). This makes subtraction and parameter updates straightforward in code.

11) Q: What are the forward and backward passes in a computation graph?
    A: Forward pass (forward propagation) computes the function values from inputs to outputs. Backward pass (backpropagation) traverses the graph in reverse, applying the chain rule to compute gradients with respect to all parameters.

12) Q: How are gradients propagated through a computation graph with branching operations like plus and max?
    A: Through the chain rule: for plus, gradients are distributed to both inputs; for max, the gradient is routed to the input that was the maximum (the other input gets zero); for multiplication, gradients are distributed according to the local derivatives (involving the forward multipliers).

13) Q: What are automatic differentiation frameworks actually doing?
    A: They manage a computation graph, perform forward evaluation, and automatically compute backward gradients by applying the chain rule to each node. In practice, frameworks require you to implement forward and local gradient parts for custom layers, but they automate the graph traversal and gradient accumulation.

14) Q: Why is numerical gradient checking still useful?
    A: To verify that your analytic (hand-derived) gradients are correct. You compare the analytic gradient with a numerical estimate obtained by small perturbations (e.g., (f(x+h) − f(x−h)) / (2h)). It’s slow, so mainly for checking implementations.

15) Q: What is the takeaway about backpropagation and its role in learning?
    A: Backpropagation is gradient-based learning implemented efficiently by reusing shared computations and applying the chain rule across a computation graph. It’s the backbone of training, enabling scalable learning without recomputing everything from scratch for each parameter.

16) Q: Why might someone still prefer using high-level frameworks instead of computing all math by hand?
    A: Modern frameworks automate forward/backward passes and provide reusable building blocks (layers, activations). You can assemble models quickly like LEGO pieces, focusing on modeling rather than re-deriving gradients. However, understanding the underlying math is valuable for debugging and advanced models.

17) Q: What is the key intuition behind the multilevel representations in neural networks?
    A: Intermediate layers learn representations that are useful for downstream tasks. Each layer extracts progressively higher-level features, enabling complex function approximation beyond what a single linear transform could achieve.

18) Q: What is the educational goal of this lecture with respect to math and neural nets?
    A: To give students a grounding in the math of neural networks (multivariable calculus, Jacobians, chain rule) so they can read, reason about, and implement parts of networks, not just use them as black boxes.