#!/usr/bin/python3

class Solution:
    def missing_number(self, nums):
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0

        count = nums[0]
        for i in range(1, len(nums)):
            count += 1
            if nums[i] != count:
                return count
