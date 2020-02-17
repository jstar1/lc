#!/usr/bin/python3

class Solution:
    def move_zeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1 
        return nums
