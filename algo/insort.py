def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    counter = 0
    for i, element in enumerate(array):
        counter += 1
        if element < smallest:
            smallest = element
            smallest_index = i
    return smallest_index, counter


def find_biggest(array):
    biggest = array[0]
    biggest_index = 0
    counter = 0
    for i, element in enumerate(array):
        counter += 1
        if element > biggest:
            biggest = element
            biggest_index = i
    return biggest_index, counter


def insert_sort(array, reverse=False, is_number_of_operations_needed=False):
    ARRAY_LENGTH = len(array)
    sorted_array = [0] * ARRAY_LENGTH
    total_operations = 0
    counter = 0
    for i in range(ARRAY_LENGTH):
        print(counter)
        total_operations += counter
        if reverse:
            insert_element_index, counter = find_biggest(array)
        else:
            insert_element_index, counter = find_smallest(array)
        sorted_array[i] = array.pop(insert_element_index)
    if is_number_of_operations_needed:
        return sorted_array, total_operations
    else:
        return sorted_array


if __name__ == '__main__':
    pass
