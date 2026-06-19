# From Scratch Implementations

This directory contains educational implementations of fundamental Machine Learning algorithms, preprocessing techniques, and evaluation metrics built entirely from scratch using Python and NumPy, without relying on high-level machine learning libraries such as Scikit-Learn.

The goal of these implementations is to provide a deeper understanding of the mathematical foundations and inner workings of common machine learning components.

---

## Repository Structure

```text
from-scratch-implementation/
│
├── Metrics/
│   ├── MAE
│   ├── MSE
│   ├── Accuracy
│   ├── Precision
│   ├── Recall
│   ├── F1 Score
│   └── Confusion Matrix
│
├── preprocessing/
│   ├── encoding/
│   │   ├── OneHotEncoder
│   │   └── OrdinalEncoder
│   │
│   └── featurescaling/
│       ├── Normalization
│       ├── StandardScaler
│       ├── MinMaxScaler
│       ├── RobustScaler
│       └── AbsoluteMaximumScaler
│
├── supervised/
│   ├── Linear Regression
│   └── Logistic Regression
│
└── unsupervised/
    └── Latent Dirichlet Allocation (LDA)
```

---

## Metrics

Implementation of commonly used machine learning evaluation metrics from scratch.

### Regression Metrics

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**

### Classification Metrics

* **Accuracy**
* **Precision**
* **Recall**
* **F1 Score**
* **Confusion Matrix**

These implementations help demonstrate how model performance is measured without relying on external libraries.

---

## Preprocessing

Data preprocessing techniques implemented from first principles.

### Encoding

#### One-Hot Encoder

Transforms categorical variables into binary vectors.

Example:

```text
Color
Red
Blue
Green
```

↓

```text
Red  Blue  Green
1     0      0
0     1      0
0     0      1
```

#### Ordinal Encoder

Converts categorical values into integer labels.

Example:

```text
Small  → 0
Medium → 1
Large  → 2
```

---

### Feature Scaling

#### Normalization

Scales values to unit norm.

#### Standard Scaling

Transforms data using:

```text
z = (x - μ) / σ
```

#### Min-Max Scaling

Rescales features to a specified range, typically [0, 1].

```text
x_scaled = (x - min) / (max - min)
```

#### Robust Scaling

Uses median and interquartile range (IQR), making it less sensitive to outliers.

#### Absolute Maximum Scaling

Scales features by dividing by the maximum absolute value.

```text
x_scaled = x / max(|x|)
```

---

## Supervised Learning

### Linear Regression

A complete implementation of Linear Regression using **Gradient Descent** optimization.

Features:

* Parameter initialization
* Cost function computation
* Gradient calculation
* Iterative optimization
* Prediction functionality

Objective:

```text
Minimize Mean Squared Error (MSE)
```

---

### Logistic Regression

Binary classification model implemented from scratch using Gradient Descent.

Features:

* Sigmoid activation
* Binary cross-entropy loss
* Gradient updates
* Probability prediction
* Class prediction

Objective:

```text
P(y=1|x) = 1 / (1 + e^(-z))
```

---

## Unsupervised Learning

### Latent Dirichlet Allocation (LDA)

Implementation of **Latent Dirichlet Allocation (LDA)** using **Gibbs Sampling** for topic modeling.

Features:

* Random topic initialization
* Gibbs sampling updates
* Topic-word distributions
* Document-topic distributions
* Topic extraction

Applications:

* Topic Modeling
* Document Clustering
* Text Analysis
* Information Retrieval

---

## Learning Objectives

These implementations are intended to:

* Understand machine learning algorithms at a deeper level
* Learn the mathematics behind popular ML techniques
* Explore optimization methods such as Gradient Descent
* Build intuition for preprocessing pipelines
* Study probabilistic topic modeling with LDA
* Practice implementing algorithms without relying on high-level libraries


