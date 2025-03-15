import numpy as np


def main():
    # lists
    height_list = [1.73, 1.68, 1.71, 1.89, 1.79]
    weight_list = [65.4, 59.2, 63.6, 88.4, 68.7]

    # array
    np_height = np.array([height_list])
    np_weight = np.array([weight_list])

    bmi = np_weight / np_height ** 2
    print(bmi)


main()
