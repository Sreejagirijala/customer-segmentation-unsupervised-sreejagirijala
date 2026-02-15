from src.preprocessing import load_data, clean_data, create_rfm, scale_features
from src.clustering import run_kmeans

def main():
    df = load_data("data/processed/online_retail_cleaned.csv")
    df = clean_data(df)
    rfm = create_rfm(df)
    scaled_data = scale_features(rfm)

    labels, score = run_kmeans(scaled_data, k=3)

    print("KMeans Clustering Completed")
    print("Silhouette Score:", score)

if __name__ == "__main__":
    main()

