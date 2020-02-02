#!/usr/bin/python3

class Solution:
    def remove_dupes(self, nums):
        if not nums:
            return 0
    
        tail = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1
                
