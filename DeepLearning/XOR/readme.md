# 🧠 Neural Networks for Logic Gates

This project demonstrates how neural networks can be used to model **basic logic gates** like **AND**, **OR**, and most importantly, **XOR**.

---

## 🔍 Problem Overview

While **AND** and **OR** gates can be solved with a **single-layer perceptron**, the **XOR** gate cannot be learned by a linear model. This is because XOR is **not linearly separable**.

To solve XOR, we use a **multi-layer neural network** with a **non-linear activation function (ReLU)**.

---

## 📁 Files

- `and.py` → Solves AND gate using a single-layer feedforward network
- `or.py` → Solves OR gate using a single-layer feedforward network
- `xor.py` → Solves XOR gate using a multi-layer feedforward neural network with **ReLU**

---

## 🔁 XOR Truth Table

| Input A | Input B | XOR Output |
|---------|---------|------------|
|   0     |    0    |     0      |
|   0     |    1    |     1      |
|   1     |    0    |     1      |
|   1     |    1    |     0      |

A single-layer perceptron fails to solve XOR because no straight line can separate the output classes. Hence, we need at least **one hidden layer** and a **non-linear activation**.

---

## ⚙️ XOR Network Architecture

- **Input Layer**: 2 neurons (A, B)
- **Hidden Layer**: 2 neurons
- **Activation**: ReLU
- **Output Layer**: 1 neuron (binary classification)
- **Loss Function**: Binary Cross-Entropy
- **Optimizer**: Gradient Descent or Adam

---

## 🧠 Key Insight

- AND/OR = Linearly separable → Simple feedforward network suffices
- XOR = Non-linearly separable → Needs hidden layer + ReLU

---

## 📌 Why ReLU?

ReLU introduces non-linearity, allowing the network to **learn decision boundaries that are not straight lines** — perfect for XOR.

$f(x) = \max(0, x)$

---

> 💡 XOR is the "Hello World" of neural network theory — and solving it shows the real power of deep learning.

