#!/usr/bin/python3

class Solution:
    def rotate_array(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
     
