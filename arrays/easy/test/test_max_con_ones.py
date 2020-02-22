#!/usr/bin/python3

import unittest
from max_con_ones import Solution


class TestMaxConOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.max_con_ones

    def test_lc(self):
        self.assertEqual(self.test([1, 1, 0, 1, 1, 1]), 3)

    def test_one(self):
        self.assertEqual(self.test([1]), 1)

    def test_three(self):
        self.assertEqual(self.test([1, 1, 1, 0, 0, 1, 1, 0, 1]), 3)


if __name__ == "__main__":
    unittest.main()
