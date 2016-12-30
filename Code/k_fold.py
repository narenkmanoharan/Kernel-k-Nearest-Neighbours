from random import sample


def create_kfolds(dataset, k=10):
    """ Gets the dataset and generates the training and testing data splices using the K-fold cross validation

    :param dataset:
        dataset - list[list]: Dataset which contains the attributes and classes.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68, 'cp'], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08, 'pp'], .... ]

    :param k:
        k - int: numbers of fold in the K-Fold cross validation (default value = 10)

    Yields:
        train_test_split - array[list[list]]: Contains k arrays of training and test data splices of dataset

            Example: [[[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....] , .... ,
                    [[0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]]
    """
    train_test_split = []
    size = len(dataset)
    num_of_elements = int(size / k)
    for i in range(k):
        new_sample = sample(dataset, num_of_elements)
        train_test_split.append(new_sample)
        for row in new_sample:
            dataset.remove(row)
    if len(dataset) != 0:
        for rows in range(len(dataset)):
            train_test_split[rows].append(dataset[rows])
        dataset.clear()
    return train_test_split
