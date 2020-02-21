#!/usr/bin/python3
from typing import List


class Solution:
    def find_all_num_disapp(self, nums: List[int]) -> List[int]:
        marked = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in marked]
