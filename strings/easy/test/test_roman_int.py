#!/usr/bin/python3

import unittest
from roman_int import Solution


class TestRomanInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_lc(self):
        self.assertEqual(self.solution.roman_int("III"), 3)
 
    def test_lc_one(self):
        self.assertEqual(self.solution.roman_int("IV"), 4)

    def test_lc_two(self):
        self.assertEqual(self.solution.roman_int("IX"), 9)

    def test_lc_three(self):
        self.assertEqual(self.solution.roman_int("LVIII"), 58)


if __name__ == '__main__':
    unittest.main()
