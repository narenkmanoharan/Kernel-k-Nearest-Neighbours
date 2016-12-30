import csv
import numpy as np


def read_file(filename):
    """ Read file gets an input file(csv) from the same directory and generates a features and dataset.

    :param filename:
        filename - string: The filename of the csv file in the folder.

            Example: ecoli.csv

    Yields:
        feature_attribute_set: Generates the various attributes of dataset

        dataset - list[list]: Dataset which contains the attributes and classes.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68, 'cp'], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08, 'pp'], .... ]
    """
    with open(filename, 'r') as data:
        data_vals = []
        reader = csv.reader(data)
        for row in reader:
            data_vals.append(row)
        dataset = data_vals[1:]
        data_vals[0].pop()
        feature_attribute_set = data_vals[0]
    return feature_attribute_set, dataset


def create_feature_class_set(dataset):
    """ Gets the dataset and generates a feature set and class set.

    :param dataset:
        dataset - list[list]: The dataset which contains the attributes and classes.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68, 'cp'], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08, 'pp'], .... ]

    Yields:
        features_set - list[list]: Feature set which contains the feature/attribute values.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....]

        class_set - list[list]: Class set which contains the class values.

            Example: ['cp', 'pp', ....]
    """
    feature_set = []
    class_set = []
    for row in dataset:
        size = len(row) - 1
        feature_set.append(row[:size])
        class_set.append(''.join(row[size:]))
    return feature_set, class_set


def create_dataset(feature_set, class_set):
    """ Gets the feature and class set to generate the dataset.

    :param feature_set:
        features_set - list[list]: Feature set which contains the feature/attribute values.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....]

    :param class_set:
        class_set - list[list]: Class set which contains the class values.

            Example: ['cp', 'pp', ....]

    Yields:
        dataset - list[list]: The dataset which contains the attributes and classes.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68, 'cp'], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08, 'pp'], .... ]
    """
    for index in range(len(feature_set)):
        feature_set[index].append(class_set[index])
    return feature_set


# Drops the class labels from the dataset
def drop_last_column(train, test):
    dist_train = np.asarray(np.delete(train, len(train[0]) - 1, axis=1), dtype=float)
    dist_test = np.asarray(test[0:-1], dtype=float)
    return dist_train, dist_test
