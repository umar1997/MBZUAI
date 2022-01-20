import numpy as np
from matplotlib import pyplot as plt


def initialize_centroids(points, k):
    """returns k centroids from the initial points"""
    centroids = points.copy()
    np.random.shuffle(centroids)
    return centroids[:k]


def closest_centroid(points, centroids):
    """returns an array containing the index to the nearest centroid for each point"""
    distances = np.sqrt(((points - centroids[:, np.newaxis]) ** 2).sum(axis=2))
    return np.argmin(distances, axis=0)


def move_centroids(points, closest, centroids):
    """returns the new centroids assigned from the points closest to them"""
    return np.array([points[closest == k].mean(axis=0) for k in range(centroids.shape[0])])


def main_km():
    points = np.vstack(((np.random.randn(150, 2) * 0.75 + np.array([1, 0])),
                        (np.random.randn(50, 2) * 0.25 + np.array([-0.5, 0.5])),
                        (np.random.randn(50, 2) * 0.5 + np.array([-0.5, -0.5]))))

    print(r'data shape', points.shape)
    c = initialize_centroids(points, 3)
    print(r'initial center ', c)
    for i in range(50):
        closest_centroid(points, c)
        c = move_centroids(points, closest_centroid(points, c), c)
        if (i+1) % 10 == 0:
            print("iteration %d" % (i+1))
            print(c)

    plt.scatter(points[:, 0], points[:, 1])
    plt.scatter(c[:, 0], c[:, 1], marker='^')
    plt.show()


if __name__ == '__main__':
    main_km()