import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', header=None)
data = pd.DataFrame(df).to_numpy()
centroids = 3


def centroids_init(data, num_of_clusters):
    num_examples = data.shape[0]
    random_ids = np.random.permutation(num_examples)
    centroid = data[random_ids[:num_of_clusters], :]
    return centroid


def centroids_find_closest(centroid, data):
    distance = np.zeros((data.shape[0], centroid.shape[0]))
    for i in range(data.shape[0]):
        for j in range(centroid.shape[0]):
            distance[i][j] = np.linalg.norm(data[i] - centroid[j], 1)
    return np.argmin(distance, axis=1)


def k_mean(data, num_of_clusters):
    # init centroid
    centroid = [centroids_init(data, num_of_clusters)]
    while True:
        distance = centroids_find_closest(centroid[-1], data)

        new_centroid = np.zeros_like(centroid[-1])

        for i in range(num_of_clusters):
            new_centroid[i] = np.average(data[distance == i], axis=0)

        if np.array_equal(new_centroid, centroid[-1]):
            print("Quá trình phân cụm dừng lại vì các tâm mới đều không đổi")
            break
        centroid.append(new_centroid)

    return centroid[-1]


print(f"Centroids of {centroids} clusters: ", k_mean(data, centroids))
