# 📏 Absolute Maximum Scaling (Feature Scaling)

This mini-project demonstrates the implementation of **Absolute Maximum Scaling** from scratch, along with a visual comparison of its effects on data.

---

## 📌 What is Absolute Maximum Scaling?

Absolute Maximum Scaling transforms the data by dividing each feature by its **maximum absolute value**. This results in values scaled between **-1 and 1**.

It is a simple and fast method, but like min-max scaling, it's **sensitive to outliers**.

---

## 🧮 Formula

$X_{\text{scaled}} = \frac{X}{\max(|X|)}$

Where:
- $\max(|X|)\$ is the maximum **absolute** value in the feature.

---

