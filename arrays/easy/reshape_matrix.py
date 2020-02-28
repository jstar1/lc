#!/usr/bin/python3

from typing import List


class Solution:
    def reshape_matrix(self, matrix: List[int], r: int, c: int) -> List[int]:
        flatten = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                flatten.append(matrix[i][j])

        if len(flatten) != r * c:
            return matrix

        row = []
        reshaped = []
        counter = 0
        
        for x in range(r):
            for y in range(c):
                row.append(flatten[counter])
                counter += 1
            reshaped.append(row)
            row = []
        return reshaped
        
