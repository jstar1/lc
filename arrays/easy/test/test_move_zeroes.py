#!/usr/bin/python3

import unittest
from move_zeroes import Solution

class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    
    def test_lc_one(self):
        self.assertEqual(self.solution.move_zeroes([0,1,0,3,12]), [1,3,12,0,0])


    def test_one(self):
        self.assertEqual(self.solution.move_zeroes([0]), [0])


    def test_two(self):
        self.assertEqual(self.solution.move_zeroes([0,1]), [1,0])


    def test_three(self):
        self.assertEqual(self.solution.move_zeroes([1,0]), [1,0])


    def test_three(self):
        self.assertEqual(self.solution.move_zeroes([0,0,1,0,0]), [1,0,0,0,0])

    
    def test_four(self):
        self.assertEqual(self.solution.move_zeroes([1,2,3,4]), [1,2,3,4])


if __name__ == '__main__':
    unittest.main()
