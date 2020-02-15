#!/usr/bin/python3

import unittest
from pascals_tri import Solution

class TestPascalTri(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    
    def test_lc(self):
        self.assertEqual(self.solution.generate(5), [[1],[1,1,],[1,2,1],[1,3,3,1],[1,4,6,4,1]])


if __name__ == '__main__':
    unittest.main()
