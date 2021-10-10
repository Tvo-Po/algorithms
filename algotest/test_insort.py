import unittest

from algo.insort import insert_sort


class MyTestCase(unittest.TestCase):

    def test_normal_sort_with_numbers(self):

        array = [1, 5, 233, 123, 73, 462,
                 64, -5, 0, -69, -1, 5,
                 43, 0, 12, 73, 0, -212]

        sorted_array = [-212, -69, -5, -1, 0,
                        0, 0, 1, 5, 5, 12, 43,
                        64, 73, 73, 123, 233, 462]

        result_array = insert_sort(array)
        self.assertEqual(result_array, sorted_array)

    def test_reverse_sort_with_numbers(self):

        array = [1, 5, 233, 123, 73, 462,
                 64, -5, 0, -69, -1, 5,
                 43, 0, 12, 73, 0, -212]

        sorted_array = [462, 233, 123, 73, 73,
                        64, 43, 12, 5, 5, 1, 0,
                        0, 0, -1, -5, -69, -212]

        result_array = insert_sort(array, reverse=True)
        self.assertEqual(result_array, sorted_array)

    def test_normal_sort_with_strings(self):

        array = ['all', 'the', 'alphabetizing', 'work',
                 'using', 'many', 'different', 'formats',
                 'words', 'separated', 'by', 'spaces', 'or',
                 'commas', 'or', 'etc', 'and', 'it', 'can',
                 'also', 'sort', 'things', 'alphabetically',
                 'line', 'by', 'line', 'if', 'you', 'need', 'it']

        sorted_array = ['all', 'alphabetically', 'alphabetizing',
                        'also', 'and', 'by', 'by', 'can', 'commas',
                        'different', 'etc', 'formats', 'if', 'it',
                        'it', 'line', 'line', 'many', 'need', 'or',
                        'or', 'separated', 'sort', 'spaces', 'the',
                        'things', 'using', 'words', 'work', 'you']

        result_array = insert_sort(array)
        self.assertEqual(result_array, sorted_array)

    def test_reverse_sort_with_strings(self):

        array = ['all', 'the', 'alphabetizing', 'work',
                 'using', 'many', 'different', 'formats',
                 'words', 'separated', 'by', 'spaces', 'or',
                 'commas', 'or', 'etc', 'and', 'it', 'can',
                 'also', 'sort', 'things', 'alphabetically',
                 'line', 'by', 'line', 'if', 'you', 'need', 'it']

        sorted_array = ['you', 'work', 'words', 'using', 'things',
                        'the', 'spaces', 'sort', 'separated', 'or',
                        'or', 'need', 'many', 'line', 'line', 'it',
                        'it', 'if', 'formats', 'etc', 'different',
                        'commas', 'can', 'by', 'by', 'and', 'also',
                        'alphabetizing', 'alphabetically', 'all']

        result_array = insert_sort(array, reverse=True)
        self.assertEqual(result_array, sorted_array)


if __name__ == '__main__':
    unittest.main()
