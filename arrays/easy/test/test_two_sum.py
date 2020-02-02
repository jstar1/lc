#!/usr/bin/python3

import unittest
from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_empty(self):
        self.assertEqual(self.solution.two_sum([], 0), False)
    

    def test_case_one(self):
        self.assertEqual(self.solution.two_sum([5,6,3,2], 9), [1,2])


    def test_case_two(self):
        self.assertEqual(self.solution.two_sum([5,5], 10), [0,1])


    def test_case_three(self):
        self.assertEqual(self.solution.two_sum([3,4,5,8], 11), [0,3])    


    def test_case_four(self):
        self.assertEqual(self.solution.two_sum([3,2,1,4], 3), [1,2])


if __name__ == '__main__':
    unittest.main()
