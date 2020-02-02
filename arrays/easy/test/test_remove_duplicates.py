#!/usr/bin/python3

import unittest

from remove_duplicates import Solution

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()        


    def test_empty(self):
        # test empty
        self.assertEqual(self.solution.remove_dupes([]), False)


    def test_case_one(self):
        # test no dupes
        self.assertEqual(self.solution.remove_dupes([0,1,2]), 3)


    def test_case_two(self):
        # test all are same
        self.assertEqual(self.solution.remove_dupes([0,0,0]), 1)

    
    def test_case_three(self):
        # test case from leetcode
        self.assertEqual(self.solution.remove_dupes([0,0,1,1,1,2,2,3,3,4]), 5)
