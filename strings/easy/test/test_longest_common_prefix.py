#!/usr/bin/python3

import unittest
from longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.longest_common_prefix

    def test_lc(self):
        test_strings = ["flower", "flow", "flight"]
        self.assertEqual(self.test(test_strings) == "fl", True)

    def test_lc_one(self):
        test_strings = ["dog", "racecar", "car"]
        self.assertEqual(self.test(test_strings) == "", True)

    def test(self):
        test_strings = ["flow"]
        self.assertEqual(self.test(test_strings) == "flow", True)

    def test_one(self):
        test_strings = []
        self.assertEqual(self.test(test_strings) == "", True)


if __name__ == "__main__":
    unittest.main()
