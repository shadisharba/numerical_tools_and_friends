import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

import matplotlib.pyplot as plt

# Generate synthetic data with four clusters
# X, y_true = make_blobs(n_samples=200, centers=4, random_state=42)
X, y_true = make_blobs(n_samples=200, centers=4, cluster_std=[1.0, 2.0, 0.5, 2.5], random_state=42)

# K-means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
kmeans_labels = kmeans.labels_

# GMM clustering
gmm = GaussianMixture(n_components=4)
gmm.fit(X)
gmm_labels = gmm.predict(X)

# Plot the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', color='red')
plt.title('K-means Clustering')

plt.subplot(1, 3, 2)
plt.scatter(X[:, 0], X[:, 1], c=gmm_labels)
plt.title('Gaussian Mixture Model Clustering')

plt.subplot(1, 3, 3)
plt.scatter(X[:, 0], X[:, 1], c=y_true)
plt.title('True Clusters')

plt.show()