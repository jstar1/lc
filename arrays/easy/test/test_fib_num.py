#!/usr/bin/python3

import unittest
from fib_num import Solution


class TestFib(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.fib

    def test_lc(self):
        self.assertEqual(self.test(2), 1)

    def test_lc_one(self):
        self.assertEqual(self.test(3), 2)

    def test_lc_two(self):
        self.assertEqual(self.test(4), 3)

    def test_mine(self):
        self.assertEqual(self.test(0), 0)

    def test_mine_one(self):
        self.assertEqual(self.test(1), 1)

    def test_mine_two(self):
        self.assertEqual(self.test(5), 5)


if __name__ == "__main__":
    unittest.main()
