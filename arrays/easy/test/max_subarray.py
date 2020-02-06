#!/usr/bin/python3

import unittest
from test_max_subarray import Solution

class TestMaxSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_leet_one(self):
        assertEqual(self.solution.max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    
    def test_two(self):
        assertEqual(self.solution.max_subarray([]), False)


    def test_three(self):
        assertEqual(self.solution.max_subarray([0,1]), 1)


    def test_four(self):
        assertEqual(self.solution.max_subarray([1,3,-5,2,5,-3,1,6]), 7)


    def test_five(self):
        assertEqual(self.solution.max_subarray(1,-3,2,1,-5,-6,2]), 1)


if __name__ == '__main__':
    unittest.main()
    

