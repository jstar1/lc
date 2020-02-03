#!/usr/bin/python3

import unittest

from remove_element import Solution

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one(self):
        # from leetcode test case, 
        self.assertEqual(self.solution.remove_ele([3,2,2,3], 3), (2, [2,2])) 


    def test_two(self):
        # empty list, return false
        self.assertEqual(self.solution.remove_ele([], None), False)


    def test_three(self):
        # remove 1 item, return 0
        self.assertEqual(self.solution.remove_ele([1], 1), (0, []))

    
    def test_four(self):
        # don't remove any< return 2
        self.assertEqual(self.solution.remove_ele([0,1], 2), (2, [0, 1]))


    def test_five(self):
        # remove ones, return 3
        self.assertEqual(self.solution.remove_ele([1,1,2,2,1,1,2], 1), (3, [2,2,2]))

 
    def test_six(self):
        # remove last, return 2
        self.assertEqual(self.solution.remove_ele([1,2,1,3,1], 1), (2, [2,3]))


if __name__ == '__main__':
    unittest.main()
