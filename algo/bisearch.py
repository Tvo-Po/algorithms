from math import floor


def binary_search(indexing_data_structure, element, is_number_of_operations_needed=False):
    try:
        counter = 0
        lower_border = 0
        upper_border = len(indexing_data_structure) - 1
    except TypeError:
        if is_number_of_operations_needed:
            return None, None
        else:
            return None

    while lower_border <= upper_border:
        counter += 0
        middle = lower_border + floor((upper_border - lower_border) / 2)
        try:
            if indexing_data_structure[middle] == element:
                if is_number_of_operations_needed:
                    return middle, counter
                else:
                    return middle
            elif indexing_data_structure[middle] < element:
                lower_border = middle + 1
            else:
                upper_border = middle - 1
        except TypeError:
            if is_number_of_operations_needed:
                return None, None
            else:
                return None


if __name__ == '__main__':
    pass
