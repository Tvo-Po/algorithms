import unittest
from math import ceil, log2

from algo.bisearch import binary_search


class TestBinarySearch(unittest.TestCase):

    TEST_ARRAY = ['apple', 'go', 'grass', 'loser', 'newbie',
                  'opponent', 'protect', 'punishment', 'test',
                  'unicorn', 'unit', 'useless', 'well', 'winner',
                  'work', 'zoo']

    TEST_TUPLE = ('a', 'and', 'anywhere', 'diversify', 'do',
                  'errors', 'free', 'goodbye', 'grammatical',
                  'language', 'level-up', 'say', 'that', 'to',
                  'tool', 'works', 'writing', 'you', 'your')

    SEARCH_INDEX_FOR_TUPLE = 17
    SEARCH_WORD_FOR_TUPLE = TEST_TUPLE[SEARCH_INDEX_FOR_TUPLE]
    SEARCH_INDEX_FOR_ARRAY = 4
    SEARCH_WORD_FOR_ARRAY = TEST_ARRAY[SEARCH_INDEX_FOR_ARRAY]
    ARRAY_LENGTH = len(TEST_ARRAY)

    def test_with_array(self):
        result = binary_search(self.TEST_ARRAY, self.SEARCH_WORD_FOR_ARRAY)
        self.assertEqual(self.SEARCH_INDEX_FOR_ARRAY, result)

    def test_with_tuple(self):
        result = binary_search(self.TEST_TUPLE, self.SEARCH_WORD_FOR_TUPLE)
        self.assertEqual(self.SEARCH_INDEX_FOR_TUPLE, result)

    def test_operations_interval(self):
        binary_sort_max_operations = ceil(log2(self.ARRAY_LENGTH))
        result_array, amount_of_operations = binary_search(self.TEST_ARRAY, self.SEARCH_WORD_FOR_ARRAY,
                                                           is_number_of_operations_needed=True)
        self.assertEqual(result_array, self.SEARCH_INDEX_FOR_ARRAY)
        self.assertLessEqual(amount_of_operations, binary_sort_max_operations)

