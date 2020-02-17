#!/usr/bin/python3

import unittest
from missing_number import Solution

class TestMissNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    
    def test_lc_one(self):
        self.assertEqual(self.solution.missing_number([3,0,1]), 2)


    def test_lc_two(self):
        self.assertEqual(self.solution.missing_number([9,6,4,2,3,5,7,0,1]), 8)


    def test_lc_three(self):
        self.assertEqual(self.solution.missing_number([0]), 1)


    def test_mine_one(self):
        self.assertEqual(self.solution.missing_number([5,3,2,1]), 4)


if __name__ == '__main__':
    unittest.main()
