#!usr/bin/python3

import unittest
from find_all_num_disapp import Solution


class TestFindAllNumDisapp(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.find_all_num_disapp

    def test_lc(self):
        self.assertEqual(self.test([4,3,2,7,8,2,3,1]), [5,6])


if __name__ == '__main__':
    unittest.main()
