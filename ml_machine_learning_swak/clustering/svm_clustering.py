"""
Support vector machines (SVMs)  are a set of supervised learning methods used for classification, regression and outliers detection.
Below is an example how to use support vector classifier to split a given dataset into different classes/clusters.
However, it is possible to not use the provided labels and split the data in the direction of the largest variance.
"""
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

import matplotlib.pyplot as plt

# Generate a 2D dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=42)

# Visualize the dataset
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('2D Dataset')
plt.show()

# Cluster the dataset using SVM
svm = SVC(kernel='linear')
svm.fit(X, y)

# Visualize the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create a grid to evaluate the model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm.decision_function(xy).reshape(XX.shape)

# Plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
ax.scatter(svm.support_vectors_[:, 0], svm.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM Clustering')

# Calculate the mean, variance, and covariance of the dataset
mean = np.mean(X, axis=0)
variance = np.var(X, axis=0)
covariance = np.cov(X.T)

# Calculate the eigenvalues and eigenvectors of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(covariance)

# Sort the eigenvalues and eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

# Select the first two eigenvectors
first_eigenvector = sorted_eigenvectors[:, 0]
second_eigenvector = sorted_eigenvectors[:, 1]

# Visualize the first two eigenvectors
plt.quiver(mean[0], mean[1], first_eigenvector[0], first_eigenvector[1], color='r', scale=3)
plt.quiver(mean[0], mean[1], second_eigenvector[0], second_eigenvector[1], color='b', scale=5)
plt.show()
