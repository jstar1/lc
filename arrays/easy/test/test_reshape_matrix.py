#!/usr/bin/python3

import unittest
from reshape_matrix import Solution


class TestReshapeMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test = self.solution.reshape_matrix

    def test_lc(self):
        self.assertEqual(self.test([[1,2],[3,4]], 1, 4,), [[1,2,3,4]])    

    def test_lc_one(self):
        self.assertEqual(self.test([[1,2],[3,4]], 2, 4), [[1,2],[3,4]])
    
    def test(self):
        self.assertEqual(self.test([[1,2],[3,4],[5,6],[7,8]], 2, 4), [[1,2,3,4],[5,6,7,8]])

if __name__ == '__main__':
    unittest.main()
