# 📚 Latent Dirichlet Allocation (LDA)

This project demonstrates a manual implementation of **Latent Dirichlet Allocation (LDA)** for **topic modeling**, using **Gibbs Sampling** for inference.

---

## 🧠 What is LDA?

**LDA** is a **generative probabilistic model** for discovering the **hidden thematic structure** in a collection of documents. It assumes:

- Each document is a **mixture of topics**
- Each topic is a **distribution over words**

LDA is unsupervised — it learns the topics **without any labels**.

---

## 🔁 Generative Process

For each document:
1. Choose topic distribution $\theta_d \sim \text{Dirichlet}(\alpha)$
2. For each word $w_n$:
   - Choose a topic $z_n \sim \text{Multinomial}(\theta_d)$
   - Choose a word $w_n \sim \text{Multinomial}(\beta_{z_n})$

Where:
- $\alpha$ controls **document-topic distribution** sparsity
- $\beta$ (or $\eta$) controls **topic-word distribution** sparsity

---

## 🔄 Gibbs Sampling (for Inference)

Since exact inference is intractable, **Gibbs Sampling** is used to approximate the posterior distribution.

### 🎯 Key Steps:
1. Initialize topic assignments randomly
2. For each word $w_{di}$ in each document:
   - Temporarily remove its topic assignment
   - Compute the conditional probability:


$P(z_i = k \mid z_{-i}, w) \propto \frac{n_{dk}^{-i} + \alpha}{\sum_k (n_{dk}^{-i} + \alpha)} \cdot \frac{n_{kw}^{-i} + \beta}{\sum_w (n_{kw}^{-i} + \beta)}$

Where:
- $n_{dk}^{-i}$ = number of words in document $d$ assigned to topic $k$, excluding current word
- $n_{kw}^{-i}$ = number of times word $w$ assigned to topic $k$, excluding current word

3. Repeat until convergence (or max iterations)

---

## 📊 Output

- Top N keywords per topic
- Topic distribution for each document

---

## 🧪 Example

For a small corpus like:

```text
["apple orange banana",
 "dog cat lion",
 "apple cat orange",
 "lion tiger elephant"]
````

LDA might find:

* Topic 0: \["apple", "orange", "banana"]
* Topic 1: \["dog", "cat", "lion", "tiger", "elephant"]

---

## 🛠️ Use Cases

* Topic modeling for document collections
* News categorization
* Customer feedback clustering
* Research paper grouping

---

## 🧾 Notes

* This is a **manual implementation using Gibbs Sampling**, not using `sklearn` or `gensim`
* Ideal for **learning the internals** of LDA

---

> 🧩 LDA reveals the structure beneath the surface — making sense of unlabelled text data.
