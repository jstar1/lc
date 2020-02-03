#!/usr/bin/python3

class Solution:
    def remove_ele(self, nums, val):
        next = 0
        for num in nums:
            if num != val:
                nums[next] = num
                next += 1
        return next
