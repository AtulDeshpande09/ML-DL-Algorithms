# 📈 Logistic Regression

**Logistic Regression** is a classification algorithm used to predict the **probability of a binary outcome**. Despite its name, it's used for **classification**, not regression.

---

## 📐 Formula

The model uses the **sigmoid function** to map linear outputs to probabilities:

$P(y=1|x)$ $=$ $\frac{1}{1 + e^{-(w \cdot x + b)}}$

Where:
- $w$ = weights  
- $x$ = input features  
- $b$ = bias

---

## 🛠️ Use Cases

- Spam detection  
- Disease diagnosis (e.g., diabetes, cancer)  
- Customer churn prediction  

---

## 📊 Key Concepts

- **Output**: Probability between 0 and 1  
- **Threshold**: Typically 0.5 to classify  
- **Loss Function**: Binary Cross-Entropy  
  
  $\text{Loss} = - \frac{1}{n} \sum_{i=1}^{n} y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)$

---

## 🧪 Example

Given email features:  
`[contains "offer", length, has link]` → `[1, 123, 1]`

Predicted spam probability:  
`0.87 → Classified as Spam (1)`

