from math import floor


def binary_search(indexing_data_structure, element, is_number_of_operations_needed=False):
    try:
        lower_border = 0
        upper_border = len(indexing_data_structure) - 1
    except TypeError:
        return None

    while lower_border <= upper_border:
        middle = lower_border + floor((upper_border - lower_border) / 2)
        try:
            if indexing_data_structure[middle] == element:
                return middle
            elif indexing_data_structure[middle] < element:
                lower_border = middle + 1
            else:
                upper_border = middle - 1
        except TypeError:
            return None


if __name__ == '__main__':
    pass
