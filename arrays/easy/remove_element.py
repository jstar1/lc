#!/usr/bin/python3

class Solution:
    def remove_ele(self, nums, val):
        if not nums: return False
        nums = [item for item in nums if item != val]

        return len(nums), nums 

