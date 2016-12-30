import random


def generate_data(train_test_split):
    """ Generates the training and testing data from the splited data

    :param train_test_split:
        train_test_split - array[list[list]]: Contains k arrays of training and test data splices of dataset

            Example: [[[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....] , .... ,
                    [[0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]]

    :param test_index:
        test_index - int : Index of the test data to be split from the train_test_split

            Example: 5

    Yields:

    train_data:
        train_data - array[list]: Contains k arrays of train data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]

    train_data:
        test_data - array[list]: Contains k arrays of test data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]
    """
    test_index = eval(
        input("\nPlease enter the partition number to be used as test data (Press 0 for random partition): "))
    while type(test_index) != int:
        test_index = eval(input("\nPlease enter an integer values for the partition to be used as test data: "))
    split = train_test_split[:]
    if test_index != 0:
        real_index = test_index - 1
    else:
        real_index = random.randrange(0, len(split))
    test_data = split[real_index]
    split.remove(test_data)
    train_data = []
    for x in split:
        for y in x:
            train_data.append(y)
    return train_data, test_data


def split_data(train, test):
    X_train = train[0:-1]
    y_train = train[:-1]
    X_test = test[0:-1]
    y_test = test[-1]
    return X_train, y_train, X_test, y_test