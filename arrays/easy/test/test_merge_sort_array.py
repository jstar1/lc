#!/usr/bin/python3

import unittest
from merge_sorted_array import Solution

class TestSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    

    def test_lc(self):
        self.assertEqual(self.solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])


    def test_one(self):
        self.assertEqual(self.solution.merge([2, 0], 1, [3], 1), [2,3])


    def test_two(self):
        self.assertEqual(self.solution.merge([4,7,8,0,0,0], 3, [2,3,4], 3), [2,3,4,4,7,8])


    def test_three(self):
        self.assertEqual(self.solution.merge([2,3,0,0,0], 2, [4,5,6], 3), [2,3,4,5,6])


if __name__ == "__main__":
    unittest.main()
