#!/usr/bin/python3

import unittest
from contains_dupes import Solution

class TestContainsDupes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    
    def test_lc_one(self):
        self.assertEqual(self.solution.contains_dupes([1,2,3,1]), True)


    def test_lc_two(self):
        self.assertEqual(self.solution.contains_dupes([1,2,3,4]), False)


    def test_lc_three(self):
        self.assertEqual(self.solution.contains_dupes([1,1,1,3,3,4,3,2,4,2]), True)


    def  test_mine_one(self):
        self.assertEqual(self.solution.contains_dupes([1,0,2,1]), True)


if __name__ == '__main__':
    unittest.main()
