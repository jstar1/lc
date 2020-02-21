#!/usr/bin/python3

import unittest
from third_max_num import Solution


class TestThirdMaxNum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lc_one(self):
        self.assertEqual(self.solution.third_max_num([3,2,1]), 1)

    def test_lc_two(self):
        self.assertEqual(self.solution.third_max_num([1,2]), 2)

    def test_lc_three(self):
        self.assertEqual(self.solution.third_max_num([2,2,3,1]), 1)

    def test_one(self):
        self.assertEqual(self.solution.third_max_num([1]), 1)

    def test_two(self):
        self.assertEqual(self.solution.third_max_num([2,2,2,1]), 2)

    def test_three(self):
        self.assertEqual(self.solution.third_max_num([6,8,9,2,5,6,2,7,10]), 8)

if __name__ == '__main__':
    unittest.main()
