import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
import random
style.use('ggplot')

dataset = {'k': [[1, 2],
                 [2, 3],
                 [3, 1]],
           'r': [[6, 5],
                 [7, 7],
                 [8, 6]]
           }


def knn(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    print(votes)

    return vote_result


if __name__ == '__main__':
    new_features = [4, 4]

    prediction = knn(dataset, new_features, k=5)
    print(prediction)

    [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
    plt.scatter(new_features[0], new_features[1], color=prediction)
    plt.show()
