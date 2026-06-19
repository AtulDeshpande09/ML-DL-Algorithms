import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def main():

    # -------------------------------------------------------------
    # 1. Create a dummy dataset (150 samples, 4 features)
    # -------------------------------------------------------------
    
    np.random.seed(42)
    
    # Generate 3 distinct clusters to make visualization interesting
    cluster1 = np.random.normal(loc=1, scale=0.5, size=(50, 4))
    cluster2 = np.random.normal(loc=4, scale=0.8, size=(50, 4))
    cluster3 = np.random.normal(loc=7, scale=0.6, size=(50, 4))
    
    X = np.vstack([cluster1, cluster2, cluster3])
    labels = np.array([0]*50 + [1]*50 + [2]*50)
    
    print(f"Original data shape: {X.shape}")

    # -------------------------------------------------------------
    # 2. Standardize the data (Crucial step for PCA)
    # -------------------------------------------------------------
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -------------------------------------------------------------
    # 3. Initialize and fit PCA (Reducing from 4D to 2D)
    # -------------------------------------------------------------
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    print(f"Transformed data shape: {X_pca.shape}\n")

    # -------------------------------------------------------------
    # 4. Print Explained Variance Metrics
    # -------------------------------------------------------------
    
    variance_ratios = pca.explained_variance_ratio_
    total_variance = np.sum(variance_ratios)
    
    print("--- PCA Analysis Metrics ---")
    print(f"Variance explained by PC1: {variance_ratios[0]*100:.2f}%")
    print(f"Variance explained by PC2: {variance_ratios[1]*100:.2f}%")
    print(f"Total variance retained:    {total_variance*100:.2f}%")
    print(f"Component vectors:\n{pca.components_}\n")

    # -------------------------------------------------------------
    # 5. Plot the Reduced Data
    # -------------------------------------------------------------
    
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', edgecolor='k', s=50)
    
    plt.title("PCA Dimensionality Reduction (4D to 2D)")
    plt.xlabel(f"Principal Component 1 ({variance_ratios[0]*100:.1f}%)")
    plt.ylabel(f"Principal Component 2 ({variance_ratios[1]*100:.1f}%)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.colorbar(scatter, label='Cluster ID')
    
    print("Displaying plot...")
    plt.show()

if __name__ == "__main__":
    main()

