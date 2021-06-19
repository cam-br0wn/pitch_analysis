import csv


def find_mean_with_missing(array):
    tot = 0
    num_values = 0
    for item in array:
        if item != "--":
            tot += float(item)
            num_values += 1

    return tot / num_values

