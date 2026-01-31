import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import joblib

# Load processed training data
X_train = pd.read_csv("../../Data_Preparation/processed_data/X_train.csv")

# ------------------ Elbow Method ------------------
wcss = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_train)
    wcss.append(model.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal Clusters")
plt.savefig("../../Clustering_Analysis/01_elbow_method.png")
plt.close()

# ------------------ Train KMeans ------------------
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X_train)

joblib.dump(kmeans, "../../Clustering_Analysis/02_kmeans_model.pkl")

# ------------------ Save Clustered Data ------------------
clustered_data = X_train.copy()
clustered_data["Cluster"] = clusters
clustered_data.to_csv("../../Clustering_Analysis/04_clustered_dataset.csv", index=False)

# ------------------ PCA Visualisation ------------------
pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_train)

plt.figure(figsize=(8,6))
plt.scatter(pca_data[:,0], pca_data[:,1], c=clusters, cmap="viridis")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Customer Segments (K-Means)")
plt.savefig("../../Clustering_Analysis/03_cluster_visualization.png")
plt.close()

print("Clustering analysis completed successfully")
