#!/usr/bin/python3

class Solution:
    def max_subarray(self, nums):

        if not nums:
            return 0

        cur_sum = max_sum = nums[0]

        for i in nums[1:]:
            # I got stuck here 
            cur_sum = max(i, cur_sum + i)
            max_sum = max(max_sum, cur_sum)

        return max_sum

