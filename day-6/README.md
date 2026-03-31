# training--2026
# Day 6 — Neural Network from Scratch

## What is Forward Propagation?

Forward propagation is the process of passing input data through the network layer by layer to produce an output.

Each neuron:
1. Multiplies inputs by weights
2. Adds a bias
3. Passes the result through an activation function

This output becomes the input for the next layer.

---

## What does each weight represent?

A weight represents how important a specific input feature is.

- Larger weight → stronger influence
- Smaller weight → weaker influence
- Negative weight → inverse relationship

---

## What does the bias do?

Bias shifts the output.

Without bias:
- Output is always tied directly to input
With bias:
- The neuron can activate even when inputs are zero

---

## ReLU vs Sigmoid

ReLU:
- Outputs 0 for negative values
- Fast and commonly used
- Helps with deep networks

Sigmoid:
- Squashes output between 0 and 1
- Good for probabilities
- Can suffer from vanishing gradients

---

## What is missing for learning?

This network does NOT learn.

To learn, we need:
1. Loss function (measure error)
2. Backpropagation (compute gradients)
3. Gradient descent (update weights)

Right now, weights are fixed — so outputs never improve.