from math import floor


def binary_search(array, element, is_number_of_operations_needed=False):
    lower_border = 0
    upper_border = len(array) - 1
    while lower_border <= upper_border:
        middle = lower_border + floor((upper_border - lower_border) / 2)
        if array[middle] == element:
            return middle
        elif array[middle] < element:
            lower_border = middle + 1
        else:
            upper_border = middle - 1


