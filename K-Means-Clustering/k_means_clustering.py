from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(100, 2)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='*')
plt.title('K-Means Clustering')
plt.show()