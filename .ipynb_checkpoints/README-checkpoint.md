

# 📰 Fake News Detection using PassiveAggressiveClassifier

This project focuses on detecting **fake news** using a machine learning approach. The model leverages the **PassiveAggressiveClassifier** from Scikit-learn and achieves **99% accuracy** on the test dataset.

---

## 📌 Project Overview

- **Objective**: Classify news articles as *FAKE* or *REAL*.
- **Model**: PassiveAggressiveClassifier
- **Dataset**: News articles with labeled truths (fake or real)
- **Accuracy Achieved**: ~99%
- **Confusion Matrix**:
  

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- TfidfVectorizer
- PassiveAggressiveClassifier
- Matplotlib / Seaborn (for visualizations)

---

## 🧠 How it Works

1. **Text Preprocessing**  
   - Lowercasing, stopword removal, punctuation cleaning  
   - TF-IDF Vectorization

2. **Model Training**  
   - PassiveAggressiveClassifier trained on TF-IDF features

3. **Evaluation**  
   - Accuracy Score
   - Confusion Matrix
   - Classification Report

---

## 📊 Results

- **Accuracy**: 99%
- **Confusion Matrix**:

  |           | Predicted FAKE | Predicted REAL |
  |-----------|----------------|----------------|
  | Actual FAKE | 4704           | 20             |
  | Actual REAL | 30             | 4226           |

---


