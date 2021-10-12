from .test_sort import BaseSortTestCases
from algo.insort import insert_sort


class TestInsertSort(BaseSortTestCases.TestSort):

    sorting_function = {'foo': insert_sort}

    def test_amount_of_operations(self):
        insert_sort_amount_operations = (self.STRING_ARRAY_AMOUNT_ELEMENTS ** 2 +
                                         self.STRING_ARRAY_AMOUNT_ELEMENTS) // 2 - 1
        sorted_array = sorted(self.STRING_ARRAY)
        result_array, amount_of_operations = self.sorting_function['foo'](self.STRING_ARRAY,
                                                                   is_number_of_operations_needed=True)
        self.assertEqual(result_array, sorted_array)
        self.assertEqual(amount_of_operations, insert_sort_amount_operations)


if __name__ == '__main__':
    pass
