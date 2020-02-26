#!/usr/bin/python3

from typing import List


class Solution:
    def array_part(self, nums: List[int]) -> int:
        return sum(x for x in sorted(nums)[::2])
