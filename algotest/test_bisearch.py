import unittest

from algo.bisearch import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_with_array(self):

        test_array = ['apple', 'go', 'grass', 'loser', 'newbie',
                      'opponent', 'protect', 'punishment', 'test',
                      'unicorn', 'unit', 'useless', 'well', 'winner',
                      'work', 'zoo']

        search_word = 'opponent'
        search_word_index = 5

        result = binary_search(test_array, search_word)
        self.assertEqual(search_word_index, result)

    def test_with_tuple(self):

        test_tuple = ('a', 'and', 'anywhere', 'diversify', 'do',
                      'errors', 'free', 'goodbye', 'grammatical',
                      'language', 'level-up', 'say', 'that', 'to',
                      'tool', 'works', 'writing', 'you', 'your')

        search_word = 'writing'
        search_word_index = 16

        result = binary_search(test_tuple, search_word)
        self.assertEqual(search_word_index, result)
