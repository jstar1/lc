#!/usr/bin/python3

class Solution:
    def majority_ele(self, nums):
        track = {}
        for i in nums:
            if i not in track:
                track[i] = 1
            if track[i] > len(nums)//2:
                return i
            else:
                track[i] += 1
        
