from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

def run_kmeans(data, k=3):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score

def run_dbscan(data):
    model = DBSCAN(eps=0.5, min_samples=5)
    labels = model.fit_predict(data)
    return labels

def run_gmm(data, k=3):
    model = GaussianMixture(n_components=k, random_state=42)
    labels = model.fit_predict(data)
    return labels
