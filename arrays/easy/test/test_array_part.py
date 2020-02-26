#!/usr/bin/python3

import unittest
from array_part import Solution


class TestArrayType(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.array_part

    def test_lc(self):
        self.assertEqual(self.test([1, 4, 3, 2]), 4)


if __name__ == "__main__":
    unittest.main()
