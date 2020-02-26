#!/usr/bin/python3

import unittest
from kdiff_pairs import Solution


class TestKdiffPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.kdiff_pairs

    def test_lc(self):
        self.assertEqual(self.test([3, 1, 4, 1, 5], 2), 2)

    def test_lc_one(self):
        self.assertEqual(self.test([1, 2, 3, 4, 5], 1), 4)

    def test_lc_two(self):
        self.assertEqual(self.test([1, 3, 1, 5, 4], 0), 1)


if __name__ == '__main__':
    unittest.main()
