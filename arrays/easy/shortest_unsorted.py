#!/usr/bin/python3

from typing import List


class Solution:
    def shortest_unsorted(self, nums: List[int]):
        count = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if prev > nums[i]:
                count += 1

        return count if count > 1 else 2
