from .test_sort import BaseSortTestCases
from algo.qsort import quick_sort


class QuickSortTest(BaseSortTestCases.TestSort):
    sorting_function = {'foo': quick_sort}
