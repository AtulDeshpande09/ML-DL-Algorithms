import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def main():
    # -------------------------------------------------------------
    # 1. Create a dummy dataset (300 samples with 3 isotropic centers)
    # -------------------------------------------------------------
    # KMeans works best with spherical, well-separated clusters
    X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)
    print(f"Original data shape: {X.shape}")

    # -------------------------------------------------------------
    # 2. Standardize the data
    # -------------------------------------------------------------
    # Essential because KMeans uses Euclidean distance to calculate variance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -------------------------------------------------------------
    # 3. Initialize and fit KMeans
    # -------------------------------------------------------------
    # n_clusters: Number of centroids to generate
    # random_state: Assures deterministic centroid initialization
    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(X_scaled)
    centroids = kmeans.cluster_centers_

    # -------------------------------------------------------------
    # 4. Print Clustering Metrics
    # -------------------------------------------------------------
    # Inertia is the sum of squared distances of samples to their closest centroid
    print("\n--- KMeans Clustering Metrics ---")
    print(f"Final Inertia (Within-cluster sum of squares): {kmeans.inertia_:.2f}")

    # -------------------------------------------------------------
    # 5. Plot and Save the Clustered Data
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 6))
    
    # Plot the cluster assignments
    scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', edgecolor='k', s=50, label='Data Points')
    
    # Plot the calculated centroids as distinct red 'X' markers
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, edgecolor='black', linewidth=1.5, label='Centroids')

    plt.title("KMeans Clustering (k=3)")
    plt.xlabel("Feature 1 (Scaled)")
    plt.ylabel("Feature 2 (Scaled)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='best')
    
    # Save the file to the current directory
    output_filename = "kmeans_result.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Plot saved successfully as '{output_filename}'")

if __name__ == "__main__":
    main()

