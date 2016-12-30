import sys
import KNN


def display_content():
    print("\n''''''''''''''''''''''  MACHINE LEARNING - ASSIGNMENT 1  '''''''''''''''''''''''''''''''''''\n")
    filename = input("Please enter the complete filename of the csv file in the folder (with extension): ")
    return filename


def display_train_test_data(train_test_split):
    """ Gets the train test dataset from the K-fold cross validation and displays it

    :param train_test_split:
        train_test_split - array[list[list]]: Contains k arrays of training and test data splices of dataset

            Example: [[[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....] , .... ,
                    [[0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]]
    """
    index = 0
    for x in train_test_split:
        index += 1
        print("\n Size of the array no.{} is {}".format(index, len(x)))
        print("\n {} ".format(x))


def print_data(train_data, test_data):
    """ Gets the train and test dataset and displays it

    :param train_data:
        train_data - array[list]: Contains k arrays of train data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]

    :param test_data
    :
        test_data - array[list]: Contains k arrays of test data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]
    """
    print("\n''''''''''''''''''''''''''''''''''''''''''TEST DATA''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    print(test_data)
    print("\nThe size of the testing dataset is {}".format(len(test_data)))
    print("\n''''''''''''''''''''''''''''''''''''''''''TRAIN DATA'''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    print(train_data)
    print("\nThe size of the training dataset is {}".format(len(train_data)))


def display_options():
    print("\nPlease select any option listed below")
    print(" 1. KNN with Euclidean Kernel")
    print(" 2. KNN with Polynomial Kernel")
    print(" 3. KNN with RBF Kernel")
    print(" 4. Print options ")
    print(" 5. Exit program ")


def switch(option, train, test):
    if option == 1:
        print("\nKNN with Euclidean")
        KNN.KNN_Classifier(train, test)
    elif option == 2:
        print("\nKNN with Polynomial")
        KNN.KNN_Classifier(train, test, 'polynomial')
    elif option == 3:
        print("\nKNN with RBF")
        KNN.KNN_Classifier(train, test, 'RBF')
    elif option == 4:
        display_options()
    elif option == 5:
        sys.exit()
    else:
        print("\nPlease enter any one of the option above")
