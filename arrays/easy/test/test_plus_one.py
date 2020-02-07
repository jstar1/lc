#!/usr/bin/python3

import unittest
from plus_one import Solution

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_leet_one(self):
        assertEqual(self.solution.plus_one([1,2,3]), [1,2,4])
    
    
    def test_leet_two(self):
        assertEqual(self.solution.plus_one([4,3,2,1]), [4,3,2,2])


    def test_mine_one(self):
        assertEqual(self.solution.plus([9]), [1,0])


if __name__ == "__main__":
    unittest.main()
