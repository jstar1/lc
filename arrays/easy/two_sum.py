#!/usr/bin/python

class Solution(object):
    def two_sum(self, nums, target):
        print(nums)
        if len(nums) <= 1:
            return False
        rev_table = {}
        for i in range(len(nums)):
            second_addend = target - nums[i]
            if second_addend in rev_table:
                return [rev_table[second_addend], i]
            else:
                rev_table[nums[i]] = i
