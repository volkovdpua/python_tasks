import unittest
from tasks import filter_list
from tasks import find_matches
from tasks import comb_without_zip
from tasks import merge_dict
from tasks import get_extension

class tasks_test_case(unittest.TestCase):

    def setUp(self):
        pass

    def filter_list(self):
        res_list = filter_list([1, 5, 4, 3, 2], 4)
        self.assertEqual(res_list, [1, 3, 2])

    def test_find_matches(self):
        res_list = find_matches([1, 2, 3, 4], [2, 5, 7, 3])
        self.assertEqual(res_list, [2, 3])

    def test_comb_without_zip(self):
        res_list = comb_without_zip([1, 2, 5], [2, 3, 6, 7])
        self.assertEqual(res_list, [[1, 2], [2, 3], [5, 6]])

    def merge_dict(self):
        res_dict = merge_dict({1: 2, 2: 4}, {3: 6})
        self.assertEqual(res_dict, {1: 2, 2: 4, 3: 6})

    def get_extension(self):
        extension = get_extension("test_file.txt")
        self.assertEqual(extension, ".txt")


if __name__ == '__main__':
    unittest.main()
