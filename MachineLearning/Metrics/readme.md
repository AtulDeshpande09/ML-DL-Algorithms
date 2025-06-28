# 📊 Evaluation Metrics – Measuring Model Performance

This document explains essential **evaluation metrics** used in machine learning to assess the performance of classification and regression models.

---

## 🔹 1. Accuracy Score

**Accuracy** measures the proportion of correct predictions over total predictions.

### 📐 Formula

$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$


Where:
- $TP$: True Positives  
- $TN$: True Negatives  
- $FP$: False Positives  
- $FN$: False Negatives  

### 📌 Use Case
- Best used when classes are **balanced**.
- Can be misleading in imbalanced datasets.

### 🧪 Example
If a model correctly predicts 90 out of 100 samples:  
$\text{Accuracy} = \frac{90}{100} = 0.90$

---

## 🔹 2. Confusion Matrix

The **confusion matrix** is a table that shows the breakdown of actual vs. predicted classifications.

### 📌 Format

|              | Predicted Positive | Predicted Negative |
|--------------|--------------------|--------------------|
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |

### 📌 Use Case
- Helps diagnose **where** the model is making mistakes.
- Foundation for many other metrics (precision, recall, etc.)

---

## 🔹 3. Precision

**Precision** tells us how many predicted positives are actually correct.

### 📐 Formula

$\text{Precision} = \frac{TP}{TP + FP}$

### 📌 Use Case
- Important when **false positives** are costly (e.g., spam filter).

### 🧪 Example
If 100 emails are predicted as spam, and 90 of them are actually spam:  
$\text{Precision} = \frac{90}{100} = 0.90$

---

## 🔹 4. Recall (Sensitivity)

**Recall** measures how many actual positives were correctly identified.

### 📐 Formula

$\text{Recall} = \frac{TP}{TP + FN}$


### 📌 Use Case
- Crucial when **false negatives** are costly (e.g., cancer detection).

### 🧪 Example
If there are 100 real spam emails, and the model catches 85:  
$\text{Recall} = \frac{85}{100} = 0.85$

---

## 🔹 5. F1 Score

**F1 Score** is the **harmonic mean** of precision and recall.

### 📐 Formula

$F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

### 📌 Use Case
- Useful when you need a balance between precision and recall.
- Great for **imbalanced datasets**.

### 🧪 Example
If precision = 0.9 and recall = 0.8:  
$F1 = 2 \cdot \frac{0.9 \cdot 0.8}{0.9 + 0.8} \approx 0.847$

---

## 🔹 6. Mean Squared Error (MSE)

Used for **regression**, MSE calculates the average of the **squared differences** between predicted and actual values.

### 📐 Formula

$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2$

### 📌 Use Case
- Penalizes **larger errors** more than smaller ones.

### 🧪 Example
True: $[3, 5, 2]$, Predicted: $[2, 5, 4]$  
MSE = $\frac{(1^2 + 0^2 + (-2)^2)}{3} = \frac{5}{3} \approx 1.67$

---

## 🔹 7. Mean Absolute Error (MAE)

MAE is the average of the **absolute differences** between predictions and actual values.

### 📐 Formula

$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |\hat{y}_i - y_i|$

### 📌 Use Case
- Easier to interpret than MSE.
- Less sensitive to **outliers** than MSE.

### 🧪 Example
True: $[3, 5, 2]$, Predicted: $[2, 5, 4]$  
MAE = $\frac{1 + 0 + 2}{3} = 1.0$

---

## ✅ Summary Table

| Metric       | Type         | Best For                                      |
|--------------|--------------|-----------------------------------------------|
| Accuracy     | Classification | Balanced datasets                             |
| Precision    | Classification | Reducing false positives                      |
| Recall       | Classification | Reducing false negatives                      |
| F1 Score     | Classification | Balancing precision & recall                  |
| MSE          | Regression     | Penalizing large errors                       |
| MAE          | Regression     | Simpler error interpretation, less sensitive  |
| Confusion Matrix | Classification | Visual error breakdown                    |

---

> 🎯 Choose the metric that best fits your problem — there's no one-size-fits-all!
