# Deep Learning

A collection of Deep Learning implementations ranging from foundational neural networks to classic Convolutional Neural Network (CNN) architectures. This repository focuses on understanding core deep learning concepts through hands-on implementations using **Keras**, along with pure Python implementations of basic neural network logic.

## 📂 Folder Structure

```text
DeepLearning/
│
├── AlexNet.ipynb
├── ANN.ipynb
├── CNN_mnist.ipynb
├── LeNet5.ipynb
├── VGG16.ipynb
│
├── XOR/
│   ├── and_gate.py
│   ├── or_gate.py
│   └── xor_nn.py
│
└── ActivationFunction/
    ├── Linear_activation.ipynb
    ├── relu.py
    ├── sigmoid.ipynb
    ├── softmax.py
    └── tanh.py
```

---

## 🚀 Technologies Used

* Python
* Keras
* TensorFlow Backend
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 📚 Implemented Models

### 1. Artificial Neural Network (ANN)

Basic feed-forward neural network implementation using Keras.

**Concepts Covered**

* Dense layers
* Forward propagation
* Backpropagation
* Loss functions
* Model training and evaluation

---

### 2. CNN for MNIST Digit Classification

Convolutional Neural Network trained on the MNIST handwritten digit dataset.

**Concepts Covered**

* Convolution layers
* Pooling layers
* Feature extraction
* Image classification

---

### 3. LeNet-5

Implementation of the classic LeNet-5 architecture proposed by Yann LeCun.

**Concepts Covered**

* Early CNN architecture
* Convolution and subsampling
* Digit recognition

---

### 4. AlexNet

Implementation inspired by the AlexNet architecture that revolutionized deep learning in computer vision.

**Concepts Covered**

* Deep CNNs
* ReLU activation
* Dropout regularization
* Image classification

---

### 5. VGG16

Implementation of the VGG16 architecture using Keras.

**Concepts Covered**

* Deep convolutional networks
* Small convolution filters (3×3)
* Transfer learning concepts
* Feature extraction

---

## 🧠 XOR Neural Network (Pure Python)

The `XOR` folder contains neural network implementations without using deep learning frameworks.

### Implementations

#### AND Gate

Basic perceptron implementation for the AND logic gate.

#### OR Gate

Basic perceptron implementation for the OR logic gate.

#### XOR Problem

Neural network architecture demonstrating how XOR can be solved using hidden layers.

**Concepts Covered**

* Perceptrons
* Logic gates
* Hidden layers
* Non-linear decision boundaries

---

## ⚡ Activation Functions

The `ActivationFunction` folder demonstrates commonly used activation functions in neural networks.

### Linear Activation

Simple linear activation function.

### ReLU (Rectified Linear Unit)

```python
f(x) = max(0, x)
```

### Sigmoid

```python
f(x) = 1 / (1 + e^(-x))
```

### Tanh

```python
f(x) = tanh(x)
```

### Softmax

Used for multi-class classification problems.

**Concepts Covered**

* Activation function behavior
* Output ranges
* Use cases in neural networks
* Visualization of activation curves

---

## 🎯 Learning Objectives

This collection helps in understanding:

* Fundamentals of Deep Learning
* Neural Network Architecture Design
* Convolutional Neural Networks (CNNs)
* Activation Functions
* Image Classification
* Logic Gate Modeling
* Solving Non-linear Problems using Neural Networks
* Deep Learning with Keras

---

This project is intended for educational and learning purposes.
