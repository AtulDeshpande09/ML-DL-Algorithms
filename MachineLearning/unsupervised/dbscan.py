import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

def main():
    # -------------------------------------------------------------
    # 1. Create a dummy dataset (200 samples in half-moon shapes)
    # -------------------------------------------------------------
    X, y_true = make_moons(n_samples=200, noise=0.1, random_state=42)
    print(f"Original data shape: {X.shape}")

    # -------------------------------------------------------------
    # 2. Standardize the data
    # -------------------------------------------------------------
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -------------------------------------------------------------
    # 3. Initialize and fit DBSCAN
    # -------------------------------------------------------------
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels = dbscan.fit_predict(X_scaled)

    # -------------------------------------------------------------
    # 4. Print Clustering Metrics
    # -------------------------------------------------------------
    unique_labels = set(labels)
    n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)

    print("\n--- DBSCAN Clustering Metrics ---")
    print(f"Estimated number of clusters: {n_clusters}")
    print(f"Estimated number of noise points: {n_noise}")

    # -------------------------------------------------------------
    # 5. Plot and Save the Clustered Data
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 6))
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1] # Black for noise

        class_member_mask = (labels == k)
        xy = X_scaled[class_member_mask]
        
        plt.scatter(xy[:, 0], xy[:, 1], c=[col], edgecolor='k', 
                    s=50 if k != -1 else 30,
                    label=f'Cluster {k}' if k != -1 else 'Noise')

    plt.title(f"DBSCAN Clustering (Found {n_clusters} Clusters)")
    plt.xlabel("Feature 1 (Scaled)")
    plt.ylabel("Feature 2 (Scaled)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='best')
    
    # Save the file instead of showing it
    output_filename = "dbscan_result.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    plt.close() # Frees up memory
    print(f"Plot saved successfully as '{output_filename}'")

if __name__ == "__main__":
    main()

