#!/usr/bin/python3

class Solution:
    def generate(self, num_rows):
        res = [[1]]
        for i in range(1, num_rows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
        return res[:num_rows]
