#!/usr/bin/python3

import unittest
from shortest_unsorted import Solution


class TestShortestUnsorted(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.shortest_unsorted

    def test_lc(self):
        self.assertEqual(self.test([2, 6, 4, 8, 10, 9, 15]), 5)

    def test(self):
        self.assertEqual(self.test([2, 4, 6, 10, 8, 15]), 2)

    def test_one(self):
        self.assertEqual(self.test([4, 6, 7, 8, 9, 10, 11]), 2)


if __name__ == "__main__":
    unittest.main()
