from collections import Counter
import kernel_selection
import numpy as np
import parser_module as pm


# KNN Classifier
def KNN_Classifier(train, test, dist='euclidean'):
    sigma = 0.97
    k = 3
    p = 3
    while 1:
        try:
            k = eval(input("\nPlease enter the value of K: "))
            if k >= len(train):
                print("Please enter a value of K which is less than the training dataset (i.e. {})".format(len(train)))
            else:
                break
        except:
            print("\n You need to enter a K value")
    training_data = np.array(train)
    testing_data = np.array(test)
    correct_prediction = 0
    if dist == 'polynomial':
        p = eval(input("Please input the value of p: "))
    if dist == 'RBF':
        sigma = eval(input("Please input the value of sigma (0.00 - 1.00): "))
    for x in testing_data:
        training, testing = pm.drop_last_column(training_data, x)
        distance = kernel_selection.distance(training, testing, dist, p, sigma)
        final_training_data = np.column_stack((training_data, distance))
        if dist == 'RBF':
            sorted_training_data = final_training_data[final_training_data[:, -1].argsort()[::-1]]
        else:
            sorted_training_data = final_training_data[final_training_data[:, -1].argsort()]
        top_k_training_data = sorted_training_data[0:k]
        common_class_labels = np.array(top_k_training_data[:, [-2]]).flatten()
        val = Counter(common_class_labels)
        calc_response = val.most_common()[0][0]
        actual_response = x[-1]
        if calc_response == actual_response:
            correct_prediction += 1
    accuracy = round((correct_prediction / len(testing_data)) * 100, 3)
    print('\nAccuracy = {}%'.format(accuracy))
