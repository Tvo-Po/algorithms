import unittest

from algo.insort import insert_sort


class MyTestCase(unittest.TestCase):

    NUM_ARRAY = [1, 5, 233, 123, 73, 462,
                 64, -5, 0, -69, -1, 5,
                 43, 0, 12, 73, 0, -212]

    STRING_ARRAY = ['all', 'the', 'alphabetizing', 'work',
                    'using', 'many', 'different', 'formats',
                    'words', 'separated', 'by', 'spaces', 'or',
                    'commas', 'or', 'etc', 'and', 'it', 'can',
                    'also', 'sort', 'things', 'alphabetically',
                    'line', 'by', 'line', 'if', 'you', 'need', 'it']

    STRING_ARRAY_AMOUNT_ELEMENTS = len(STRING_ARRAY)

    def test_normal_sort_with_numbers(self):
        sorted_array = sorted(self.NUM_ARRAY)
        result_array = insert_sort(self.NUM_ARRAY)
        self.assertEqual(result_array, sorted_array)

    def test_reverse_sort_with_numbers(self):
        sorted_array = sorted(self.NUM_ARRAY, reverse=True)
        result_array = insert_sort(self.NUM_ARRAY, reverse=True)
        self.assertEqual(result_array, sorted_array)

    def test_normal_sort_with_strings(self):
        sorted_array = sorted(self.STRING_ARRAY)
        result_array = insert_sort(self.STRING_ARRAY)
        self.assertEqual(result_array, sorted_array)

    def test_reverse_sort_with_strings(self):
        sorted_array = sorted(self.STRING_ARRAY, reverse=True)
        result_array = insert_sort(self.STRING_ARRAY, reverse=True)
        self.assertEqual(result_array, sorted_array)

    def test_amount_of_operations(self):
        insert_sort_amount_operations = (self.STRING_ARRAY_AMOUNT_ELEMENTS ** 2 +
                                         self.STRING_ARRAY_AMOUNT_ELEMENTS) // 2 - 1
        sorted_array = sorted(self.STRING_ARRAY)
        result_array, amount_of_operations = insert_sort(self.STRING_ARRAY, is_number_of_operations_needed=True)
        self.assertEqual(result_array, sorted_array)
        self.assertEqual(amount_of_operations, insert_sort_amount_operations)


if __name__ == '__main__':
    unittest.main()
