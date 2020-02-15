#!/usr/bin/python3

import unittest
from majority_ele import Solution

class TestMajorityEle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_lc_one(self):
        self.assertEqual(self.solution.majority_ele([3,2,3]), 3) 


    def test_lc_two(self):
        self.assertEqual(self.solution.majority_ele([2,2,1,1,1,2,2]), 2)


if __name__ == '__main__':
    unittest.main()
