#!/usr/bin/python3

import unittest

from search_insert_pos import Solution

class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_leet_one(self):
        self.assertEqual(self.solution.search_pos([1,3,5,6], 2), 1)

    
    def test_leet_two(self):
        self.assertEqual(self.solution.search_pos([1,3,5,6], 7), 4)

    
    def test_leet_three(self):
        self.assertEqual(self.solution.search_pos([1,3,5,6], 0), 0)


if __name__ == '__main__':
    unittest.main()          
