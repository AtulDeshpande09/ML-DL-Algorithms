# ⚡ Activation Functions – Deep Learning Essentials

This directory contains implementations of commonly used **activation functions** in neural networks. Activation functions introduce **non-linearity** into models, enabling them to learn complex patterns.

Each script/notebook here demonstrates how a specific activation function behaves and how it's applied in neural networks.

---

## 🧮 Included Activation Functions

### 🔹 1. Linear Activation
- **File**: `Linear_activation.py`

#### 📖 Description
The **linear activation function** is simply the identity function. It returns the input as is.

#### 📐 Formula
$f(x) = x$

#### 📍 Use Case
- Used in **regression** problems (output layer of neural networks for continuous values).
- Not commonly used in hidden layers (as it doesn’t introduce non-linearity).

#### 🧪 Example
Input:  
`[2.5, -1.0, 0.0, 4.2]`  
Output:  
`[2.5, -1.0, 0.0, 4.2]`

---

### 🔹 2. Sigmoid Activation
- **File**: `sigmoid.ipynb`

#### 📖 Description
The **sigmoid function** squashes input values into a range between **0 and 1**, making it suitable for representing **probabilities**.

#### 📐 Formula
$f(x) = \frac{1}{1 + e^{-x}}$

#### 📍 Use Case
- Commonly used in **binary classification** (output layer).
- Historically used in hidden layers (but mostly replaced by ReLU today).

#### 🧪 Example
Input:  
`[0.0, 2.0, -1.0]`  
Output:  
`[0.5, 0.8808, 0.2689]`

---

### 🔹 3. ReLU (Rectified Linear Unit)
- **File**: `relu.py`

#### 📖 Description
**ReLU** is one of the most widely used activation functions. It introduces non-linearity while avoiding the vanishing gradient problem seen in sigmoid/tanh.

#### 📐 Formula
$f(x) = \max(0, x)$

#### 📍 Use Case
- Commonly used in **hidden layers** of deep neural networks.
- Helps models learn faster and perform better.

#### 🧪 Example
Input:  
`[-3, -1, 0, 2, 5]`  
Output:  
`[0, 0, 0, 2, 5]`

---

### 🔹 4. Softmax Activation
- **File**: `softmax.py`

#### 📖 Description
**Softmax** converts raw logits (scores) into **probability distributions**. The output values are in the range (0, 1) and sum to 1.

#### 📐 Formula
$f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}$

#### 📍 Use Case
- Used in the **output layer of multi-class classification models**.

#### 🧪 Example
Input (logits):  
`[1.3, 5.1, 2.2, 0.7, 1.1]`  
Output (probabilities):  
`[0.02, 0.90, 0.05, 0.01, 0.02]`

Here, the second class (`5.1`) has the highest score and is assigned the highest probability.

---

### 🔹 5. Tanh Activation
- **File**: `tanh.py`

#### 📖 Description
**Tanh** is a scaled version of the sigmoid function. It maps input values to the range **[-1, 1]**, centering the data at 0.

#### 📐 Formula
$f(x) = \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

#### 📍 Use Case
- Previously popular in RNNs and hidden layers before ReLU became dominant.
- Still useful when data is centered around zero.

#### 🧪 Example
Input:  
`[-2, -1, 0, 1, 2]`  
Output:  
`[-0.964, -0.761, 0.0, 0.761, 0.964]`


---

> 💡 Activation functions are the **non-linear heartbeat** of neural networks. Mastering them means mastering how your model learns.

