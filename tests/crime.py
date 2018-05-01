import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from skfuzzy import cmeans
from sklearn.cluster import KMeans

<<<<<<< HEAD:crime.py
from fcm import FCM
=======
from algorithms.fcm import FCM
from file_path_manager import FilePathManager
>>>>>>> 67ee86b0fbd317911afeb9cf3b941690df36c7e7:tests/crime.py

sns.set()

dataset_path = FilePathManager.resolve("data/crime_data.csv")
data = pd.read_csv(dataset_path)
X = data.iloc[:, 2:4].values

number_of_clusters = 4
MAX_ITER = 50
m = 2.00

cntr, _, _, _, _, _, _ = cmeans(X.transpose(), number_of_clusters, m, 1e-8, maxiter=MAX_ITER)
fcm = FCM(number_of_clusters, MAX_ITER, m)
kmeans = KMeans(n_clusters=number_of_clusters, max_iter=MAX_ITER)
cmean_centers = fcm.fit(X)
kmeans.fit(X)

plt.scatter(X[:, 0], X[:, 1], s=50, cmap='viridis')
plt.scatter(cmean_centers[:, 0], cmean_centers[:, 1], c='black', s=300, alpha=0.7)

kmeans_centers = kmeans.cluster_centers_
plt.scatter(kmeans_centers[:, 0], kmeans_centers[:, 1], c='red', s=200, alpha=0.7)

plt.scatter(cntr[:, 0], cntr[:, 1], c='green', s=100, alpha=0.7)
plt.show()