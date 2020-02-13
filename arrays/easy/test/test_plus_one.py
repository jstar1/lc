#!/usr/bin/python3

import unittest
from plus_one import Solution

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_leet_one(self):
        self.assertEqual(self.solution.plus_one([1,2,3]), [1,2,4])
    
    
    def test_leet_two(self):
        self.assertEqual(self.solution.plus_one([4,3,2,1]), [4,3,2,2])


    def test_mine_one(self):
        self.assertEqual(self.solution.plus_one([9]), [1,0])

    
    def test_mine_two(self):
        self.assertEqual(self.solution.plus_one([4,3,9]), [4,4,0])

    
    def test_mine_three(self):
        self.assertEqual(self.solution.plus_one([10,2]), [1,0,3])


if __name__ == "__main__":
    unittest.main()
