#!/usr/bin/python3

import unittest
from valid_paren import Solution


class TestValidParen(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.valid_parens

    def test_lc(self):
        test_str = "()"
        self.assertEqual(self.test(test_str), True)

    def test_lc_one(self):
        test_str = "()[]{}"
        self.assertEqual(self.test(test_str), True)

    def test_lc_two(self):
        test_str = "(]"
        self.assertEqual(self.test(test_str), False)

    def test_lc_three(self):
        test_str = "([)]"
        self.assertEqual(self.test(test_str), False)

    def test_lc_four(self):
        test_str = "{[]}"
        self.assertEqual(self.test(test_str), True)

    def test(self):
        test_str = ""
        self.assertEqual(self.test(test_str), True)


if __name__ == "__main__":
    unittest.main()
