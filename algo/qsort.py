def quick_sort(array, reverse=False):
    if len(array) < 2:
        return array
    else:
        core_element = array[0]
        less = [i for i in array[1:] if i <= core_element]
        greater = [i for i in array[1:] if i > core_element]
        if not reverse:
            return quick_sort(less) + [core_element] + quick_sort(greater)
        else:
            return quick_sort(greater, reverse=True) + [core_element] + quick_sort(less, reverse=True)
