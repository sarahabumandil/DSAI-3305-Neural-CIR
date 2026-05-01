Study Guide: Foundations of Neural Networks and Backpropagation (based on the lecture)

1) Big picture
- Neural networks are cascades of simple units (neurons) that learn useful intermediate representations.
- Core idea: learn by gradient-based optimization (backpropagation) using the chain rule.
- Two practical aims of Assignment 2:
  - Deepen understanding of what neural networks compute (the math).
  - Introduce dependency parsing (language structure) and start using PyTorch (a deep learning framework).

2) Network structure and computations
- Basic building block: a layer that combines inputs with weights, adds a bias, and applies a nonlinearity.
  - For a layer: z = Wx + b
  - Activation: h = f(z) applied elementwise
  - Final score or output: s = u^T h (or another downstream computation)
- Vector/matrix view:
  - Forward pass is a sequence of matrix multiplications, additions, and nonlinearities.
  - Activation functions operate elementwise on vectors.
- Nonlinearities (why they matter):
  - Linear transforms alone (stacks of linear layers) have no extra representational power.
  - Nonlinearities introduce the ability to approximate complex functions.
- Common activation functions (progression overview):
  - Sigmoid (logistic): maps to [0, 1], has gradient but can saturate.
  - Tanh: similar to sigmoid but centered at 0.
  - ReLU (Rectified Linear Unit): f(x) = max(0, x). Fast gradient in positive region; “dead” for negative inputs (no gradient there).
  - Leaky ReLU / Parametric ReLU: allow small slope in negative region.
  - Swish / GELU (used in recent transformers): smooth, near-linear for large x with a nonlinearity on the side.
- Practical takeaway: activation function choice affects gradient flow and learning dynamics.

3) Why nonlinearities and gradient-based learning
- Goal: fit highly nonlinear functions (mapping inputs to outputs like meaning extraction or language structure).
- Gradient-based learning (backprop) relies on having nonzero gradients to propagate error signals back through the network.
- Gradient intuition: gradients tell you how the output changes when inputs/change parameters. Steeper regions provide stronger guidance for learning.

4) Gradients and multivariable calculus (key concepts)
- From single-variable to multivariable:
  - For a function f: R^n -> R (n inputs, 1 output), gradient is a vector of partial derivatives:
    ∇f = [∂f/∂x1, ∂f/∂x2, ..., ∂f/∂xn]^T
  - For a function f: R^n -> R^m (n inputs, m outputs), the Jacobian is an m x n matrix of partials.
- Composition and chain rule in vector/matrix form:
  - If z = g(x) and h = f(z), then ∂h/∂x = (∂h/∂z) · (∂z/∂x)
  - In neural nets: multiple layers correspond to compositions of functions; gradients are computed by multiplying Jacobians along the path of dependence.
- Important practical identities (activation layer examples):
  - For a layer z = Wx + b, with h = f(z):
    - ∂z/∂x = W
    - ∂z/∂W = x (shape must be matched to parameter layout; typically you reshape to match weight matrix shape)
    - ∂h/∂z = diag(f'(z)) if f is applied elementwise
  - For the componentwise activation, the Jacobian is diagonal with entries f'(zi).
- Hadamard (elementwise) product:
  - When combining gradients with elementwise operations, you often use the Hadamard product (A ⊙ B), i.e., elementwise multiplication.

5) Backpropagation: efficient gradient computation
- Forward pass (the “computational graph”)
  - Compute all intermediate values from inputs to outputs.
  - This is the forward evaluation of the network.
- Backward pass (the gradient flow)
  - Start with the upstream gradient at the output (often 1 for a scalar loss).
  - Traverse the graph in reverse topological order, applying the local gradient at each node and chaining them with the upstream gradient.
  - For each node, compute downstream gradients with respect to its inputs using the local derivative and the upstream gradient.
- Core ideas to implement:
  - Reuse shared partial computations (do not recompute the same component multiple times).
  - For operations with multiple outputs/branches (e.g., additions, multiplications), gradients may flow to multiple inputs; sum gradients where paths merge.
  - For graph nodes with multiple inputs (e.g., Wx + b): compute gradients with respect to each input using the same upstream gradient and the local Jacobians, then propagate further.
- Shape convention vs. Jacobian form
  - In practice, you store derivatives in shapes that match parameter shapes (e.g., ds/dW as an n x m matrix) for convenient parameter updates.
  - Jacobian form is mathematically correct; shape convention is for practical implementation.

6) Practical details for implementation
- Computation graph and automatic differentiation
  - Modern frameworks (e.g., PyTorch) build and manage computation graphs, handle forward/backward passes, and perform automatic differentiation.
  - You still need to provide forward calculations and local gradients for custom layers, but the framework handles the graph traversal and gradient accumulation.
- Forward pass vs. backward pass
  - Forward pass: compute the actual values.
  - Backward pass: compute gradients using the chain rule and stored intermediates.
- Automatic differentiation vs. symbolic differentiation
  - Theano-like symbolic autodiff attempted to differentiate entire graphs automatically; in practice, frameworks require explicit local gradient definitions for custom components and automate the rest.
- Gradient checking
  - A useful debugging technique: numerically estimate gradients by finite differences and compare to analytic gradients from your backward pass.
  - Method: for each parameter θ, compute (f(θ + h) - f(θ - h)) / (2h) and compare to ∂f/∂θ.
  - Use small h (~ 1e-4). Two-sided differences are more stable than one-sided.
  - This is slow (checks every parameter) but valuable to verify correctness of your gradient implementations.
- Computational complexity
  - The backward pass should have similar asymptotic complexity to the forward pass.
  - Properly implemented backprop avoids recomputing shared components; this is the main efficiency gain.

7) Practical takeaways and advice
- If you’re using a framework (e.g., PyTorch), you can treat most layers as given blocks and focus on building models by composing them, not on deriving all gradients by hand.
- If you implement a new layer or activation yourself, you must provide:
  - Forward function (how the layer computes its output)
  - Local gradient(s) (the derivative of the layer with respect to its inputs for backprop)
- Shape conventions are crucial for efficient updates:
  - Match the gradient shape to the parameter shapes to simplify SGD updates (e.g., ds/dW should match the shape of W).
- Common blockers
  - Misaligning shapes when computing gradients (row vs. column vectors, transposes).
  - Forgetting to propagate gradients through branches (summing gradients at merge points).
  - Incorrect local gradients for non-linearities.
- Intent behind math
  - The handwritten gradient math is to illustrate chain rule in a multivariable setting.
  - The computational approach (backprop) is about efficiently applying chain rule across graphs and reusing computations.

8) Language-structure and reading suggestions
- Today’s plan: math foundations (derivatives, Jacobians, chain rule) and backprop basics.
- Thursday will cover language and linguistics (dependency parsing, language structure).
- Recommended readings:
  - Short tutorials/reviews on matrix calculus and linear algebra relevant to neural networks.
  - Look at a recommended reading list and pick one that fits your background.
- PyTorch tutorial
  - Friday session in Gates B01 (and recorded) to help students get started with PyTorch before assignment 2.

9) Quick recap (checklist)
- Understand the neural network as a stack of linear transforms and nonlinearities.
- Know why nonlinearities are essential for expressive power.
- Be comfortable with:
  - Forward pass: compute outputs
  - Backward pass: compute gradients via chain rule
  - Jacobians and Hadamard product (elementwise)
  - Shape conventions for derivatives
  - Computation graphs and topological ordering
  - Automatic differentiation concept and practical constraints in frameworks
  - Gradient checking as a debugging tool
- Be ready to implement or verify a simple layer’s forward and backward computations, and to reason about gradient flow through a computation graph.

10) Suggested practice problems
- Derive by hand the backward pass for:
  - A linear layer z = Wx + b followed by a sigmoid activation
  - A linear layer followed by tanh activation
- Compute and compare Jacobians for:
  - An elementwise activation function f(z) applied to a vector z
  - The Wx + b layer with respect to x and with respect to W
- Work through a small two-branch computation graph (as in the example with sum and max) and perform forward and backward passes manually to confirm gradientflow.
- Implement a tiny custom layer (forward + backward) and verify gradients with gradient checking.
- Use PyTorch to implement a small network with one hidden layer, then perform a manual gradient check on a subset of parameters.

If you need a quick reference, keep this structure in mind:
- Forward pass: functional computation through the network
- Backward pass: propagate gradients using chain rule and local derivatives
- Gradients with respect to parameters: ds/dW, ds/db, ds/dx, using delta (upstream gradient) and local derivatives
- Practical concerns: shape alignment, reuse of intermediate results, and gradient checking as a sanity check

End note: This material is the under-the-hood machinery of neural networks. Modern frameworks automate much of it, but understanding these foundations helps you debug, design new architectures, and interpret learning dynamics (e.g., why gradients might explode/vanish in deeper networks).