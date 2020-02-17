#!/usr/bin/python3

class Solution:
    def contains_dupes(self, nums):
        dic = {} 
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False
