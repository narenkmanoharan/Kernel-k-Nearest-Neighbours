import k_fold
import normalizer
import parser_module
import train_test_data_generator
import display_module


def assignment_2():
    # Print welcome screen
    filename = display_module.display_content()

    # Read data fom the given csv file and return the complete dataset(attributes, class)
    feature_attribute_set, dataset = parser_module.read_file(filename)

    # Separate the attribute and class set
    feature_set, class_set = parser_module.create_feature_class_set(dataset)

    # Find the maximum and minimum for the attributes
    maximum, minimum = normalizer.maximum_minimum_features(feature_set)

    # Create new normalized feature set
    normalized_feature_set = normalizer.new_feature_set(feature_set, maximum, minimum)

    # Create new normalized data set
    normalized_data_set = parser_module.create_dataset(normalized_feature_set, class_set)

    # K-Fold data set splitting
    train_test_split = k_fold.create_kfolds(normalized_data_set, 10)

    # Creating the Train and Test data split
    train, test = train_test_data_generator.generate_data(train_test_split)

    # Display the result
    option = 0
    display_module.display_options()
    while option != 8:
        option = eval(input("\nEnter Option: "))
        display_module.switch(option, train, test)


if __name__ == "__main__":
    assignment_2()
