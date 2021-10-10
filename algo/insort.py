def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i, element in enumerate(array):
        if element < smallest:
            smallest = element
            smallest_index = i
    return smallest_index


def find_biggest(array):
    biggest = array[0]
    biggest_index = 0
    for i, element in enumerate(array):
        if element > biggest:
            biggest = element
            biggest_index = i
    return biggest_index


def insert_sort(array, reverse=False, is_number_of_operations_needed=False):
    ARRAY_LENGTH = len(array)
    sorted_array = [0] * ARRAY_LENGTH
    for i in range(ARRAY_LENGTH):
        if reverse:
            insert_element_index = find_biggest(array)
        else:
            insert_element_index = find_smallest(array)
        sorted_array[i] = array.pop(insert_element_index)
    return sorted_array


if __name__ == '__main__':
    pass
