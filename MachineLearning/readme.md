# Machine Learning

A collection of Machine Learning implementations ranging from **mathematical implementations built from scratch** to **practical implementations using Scikit-Learn and PyTorch**.

This repository is designed as a learning resource that covers the complete machine learning workflow:

* Core algorithms implemented from first principles
* Data preprocessing techniques
* Evaluation metrics
* Supervised learning
* Unsupervised learning
* Classical machine learning models
* Neural networks with PyTorch

---

# Repository Structure

```text
Machine Learning/
│
├── from-scratch-implementation/
│   ├── Metrics/
│   ├── preprocessing/
│   ├── supervised/
│   └── unsupervised/
│
├── supervised/
│   ├── Classification/
│   └── Regression/
│
└── unsupervised/
    ├── DBSCAN.ipynb
    ├── KMeans.ipynb
    ├── PCA.ipynb
    └── Plot Images
```

---

# 1. From Scratch Implementations

Implementations built entirely from scratch using Python and NumPy without relying on machine learning libraries such as Scikit-Learn.

### Included Topics

#### Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

#### Preprocessing

**Encoding**

* One-Hot Encoder
* Ordinal Encoder

**Feature Scaling**

* Normalization
* Standard Scaling
* Min-Max Scaling
* Robust Scaling
* Absolute Maximum Scaling

#### Supervised Learning

* Linear Regression (Gradient Descent)
* Logistic Regression (Gradient Descent)

#### Unsupervised Learning

* Latent Dirichlet Allocation (LDA)
* Gibbs Sampling Implementation

### Goal

Understand how machine learning algorithms work internally by implementing them from first principles.

---

# 2. Supervised Learning

Practical implementations using modern machine learning libraries such as **Scikit-Learn** and **PyTorch**.

The notebooks demonstrate:

* Dataset generation
* Training pipelines
* Model evaluation
* Visualization
* Hyperparameter experimentation

Synthetic datasets are generated using:

```python
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
```

---

## Classification Models

Located in:

```text
supervised/Classification/
```

Implemented algorithms:

| Model                           | Library      |
| ------------------------------- | ------------ |
| Logistic Regression             | Scikit-Learn |
| K-Nearest Neighbors (KNN)       | Scikit-Learn |
| Decision Tree                   | Scikit-Learn |
| Random Forest                   | Scikit-Learn |
| Support Vector Machine (SVM)    | Scikit-Learn |
| Naive Bayes                     | Scikit-Learn |
| Artificial Neural Network (ANN) | PyTorch      |

### Topics Covered

* Data generation
* Train/Test splitting
* Feature scaling
* Model training
* Prediction
* Performance evaluation
* Decision boundary visualization (where applicable)

---

## Regression Models

Located in:

```text
supervised/Regression/
```

Implemented algorithms:

| Model                           | Library      |
| ------------------------------- | ------------ |
| Linear Regression               | Scikit-Learn |
| K-Nearest Neighbors Regressor   | Scikit-Learn |
| Decision Tree Regressor         | Scikit-Learn |
| Random Forest Regressor         | Scikit-Learn |
| Support Vector Regressor (SVR)  | Scikit-Learn |
| Artificial Neural Network (ANN) | PyTorch      |

### Topics Covered

* Synthetic regression data generation
* Training and testing pipelines
* Error metrics
* Prediction visualization
* Model comparison

---

# 3. Unsupervised Learning

Located in:

```text
unsupervised/
```

Contains notebook implementations and visualizations for popular unsupervised learning techniques.

---

## K-Means Clustering

Implementation of centroid-based clustering.

### Concepts

* Cluster assignment
* Centroid updates
* Inertia
* Cluster visualization

---

## DBSCAN

Density-Based Spatial Clustering of Applications with Noise.

### Concepts

* Core points
* Border points
* Noise points
* Density-based clustering

Advantages:

* No need to specify the number of clusters
* Can detect arbitrarily shaped clusters
* Handles outliers effectively

---

## Principal Component Analysis (PCA)

Dimensionality reduction technique used for feature extraction and visualization.

### Concepts

* Covariance Matrix
* Eigenvalues
* Eigenvectors
* Principal Components
* Variance Explained

Applications:

* Visualization
* Noise Reduction
* Feature Compression

---

## Visualizations

The unsupervised learning section includes generated plots demonstrating:

* K-Means cluster formation
* DBSCAN clustering behavior
* PCA dimensionality reduction results

These visualizations help illustrate how each algorithm transforms and interprets data.

---

# Technologies Used

### Core Libraries

* NumPy
* Pandas
* Matplotlib

### Machine Learning

* Scikit-Learn

### Deep Learning

* PyTorch

### Development Environment

* Jupyter Notebook

---

# Learning Path

A recommended order for exploring this repository:

1. Start with **from-scratch-implementation**
2. Learn preprocessing techniques and metrics
3. Explore Linear and Logistic Regression implementations
4. Move to supervised learning notebooks
5. Compare classical machine learning algorithms
6. Study ANN implementations using PyTorch
7. Explore clustering and dimensionality reduction techniques

---

# Purpose of This Repository

This repository serves as:

* A machine learning study guide
* A reference for algorithm implementations
* A practical notebook collection
* A resource for understanding ML fundamentals and applications

It bridges the gap between:

```text
Mathematical Understanding
            ↓
Implementation from Scratch
            ↓
Scikit-Learn & PyTorch Usage
            ↓
Practical Machine Learning Workflows
```

