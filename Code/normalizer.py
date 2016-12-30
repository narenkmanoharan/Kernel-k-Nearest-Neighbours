def maximum_minimum_features(feature_set):
    """ Gets the feature set and generates the maximum and minimum lists of all the attributes.

    :param feature_set:
        features_set - list[list]: Feature set which contains the feature/attribute values.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....]

    Yields:
        maximum - list[float]: The maximum values of the attributes.

            Example: [0.1, 0.23, 0.21, 0.34, 0.13, 0.69]

        minimum - list[float]: The minimum values of the attributes.

            Example: [0.91, 0.63, 0.31, 0.74, 0.23, 0.89]
    """
    size = len(feature_set[0])
    temp_list = []
    maximum = []
    minimum = []
    for x in range(size):
        for y in feature_set:
            temp_list.append(y[x])
        max_val = max(temp_list)
        min_val = min(temp_list)
        temp_list.clear()
        maximum.append(max_val)
        minimum.append(min_val)
    return maximum, minimum


def new_feature_set(feature_set, maximum, minimum):
    """ Gets the feature set, maximum list, minimum and returns the normalized attribute set.

    :param feature_set:
        features_set - list[list]: Feature set which contains the feature/attribute values.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....]

    :param maximum:
        maximum - list[float]: The maximum values of the attributes.

            Example: [0.1, 0.23, 0.21, 0.34, 0.13, 0.69]

    :param minimum:
        minimum - list[float]: The minimum values of the attributes.

            Example: [0.91, 0.63, 0.31, 0.74, 0.23, 0.89]

    Yields:
        new_features_set - list[list]: Feature set which contains the normalized feature/attribute values.

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....]
    """
    size = len(feature_set[0])
    for x in range(size):
        for y in feature_set:
            temp_max = float(maximum[x])
            temp_min = float(minimum[x])
            old_value = float(y[x])
            new_value = round((old_value - temp_min) / (temp_max - temp_min), 2)
            y[x] = new_value
    return feature_set
