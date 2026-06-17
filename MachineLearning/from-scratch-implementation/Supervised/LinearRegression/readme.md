# 📉 Linear Regression

**Linear Regression** is a fundamental algorithm used for **predicting continuous outcomes**. It models the relationship between independent variables ($X$) and a continuous target variable ($y$) by fitting a linear equation.

---

## 📐 Formula

The model is represented by:


$y = w_0 + w_1x_1 + w_2x_2 + \dots + w_nx_n$


Or in vector form:

$\hat{y} = Xw + b$

Where:
- $X$ = feature matrix  
- $w$ = weights (coefficients)  
- $b$ = bias (intercept)

---

## 🛠️ Use Cases

- Predicting house prices  
- Stock price forecasting  
- Sales prediction  

---

## 📊 Key Concepts

- **Loss Function**: Mean Squared Error (MSE)  
  
  $\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2$
  
- **Optimization**: Gradient Descent (or Normal Equation)

---

## 🧪 Example

Given study hours: `[2, 4, 6, 8]`  
Predicted scores might be: `[50, 60, 70, 80]`  
The model finds the best-fit line to minimize prediction error.

