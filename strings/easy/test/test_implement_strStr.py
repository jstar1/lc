#!/usr/bin/python3

import unittest
from implement_strStr import Solution


class TestImplementstrStr(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.implement_strStr

    def test_lc(self):
        haystack = "hello"
        needle = "ll"
        self.assertEqual(self.test(haystack, needle) == 2, True)

    def test_lc_one(self):
        haystack = "aaaaa"
        needle = "bba"
        self.assertEqual(self.test(haystack, needle) == -1, True)

    def test(self):
        haystack = "aalaa"
        needle = "la"
        self.assertEqual(self.test(haystack, needle) == 2, True)

    def test_one(self):
        haystack = "df"
        needle = ""
        self.assertEqual(self.test(haystack, needle) == 0, True)

    def test_two(self):
        haystack = "lddafdddd"
        needle = "dddd"
        self.assertEqual(self.test(haystack, needle) == 5, True)


if __name__ == "__main__":
    unittest.main()
