#!/usr/bin/python3

import unittest
from max_profit import Solution


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_lc_one(self):
        self.assertEqual(self.solution.max_profit([7,1,5,3,6,4]), 5)

if __name__ == '__main__':
    unittest.main()
