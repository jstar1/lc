#!/usr/bin/python3

from typing import List
from collections import Counter


class Solution:

    def kdiff_pairs(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        rep = 0
        for i in nums:
            if k > 0 and k + i in dic or k == 0 and dic[i] > 1:
                rep += 1
        return rep
