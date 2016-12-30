import numpy as np


# To find the various distance and kernel measures
def distance(training, testing, distance_selector, p, sigma):
    dist = 0
    if distance_selector == 'euclidean':
        dist = np.sqrt(np.sum(np.square(np.add(training, np.negative(testing))), axis=1))
    elif distance_selector == 'polynomial':
        dist = np.power((1 + np.inner(training, testing)), p)
    elif distance_selector == 'RBF':
        euclidean = np.sqrt(np.sum(np.square(np.add(training, np.negative(testing))), axis=1))
        new_sigma = 2 * (sigma ** 2)
        dist = np.exp(np.negative(np.square(euclidean) / new_sigma))
    return dist
