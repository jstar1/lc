#!/usr/bin/python3


class Solution:
    def third_max_num(self, nums: int) -> int:
        third_num = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in third_num:
                if num > third_num[0]: third_num = [num, third_num[0], third_num[1]]
                elif num > third_num[1]: third_num = [third_num[0], num, third_num[1]]
                elif num > third_num[2]: third_num = [third_num[0], third_num[1], num]
        return max(nums) if float('-inf') in third_num else third_num[2]
