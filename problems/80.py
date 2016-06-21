#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        p1 = 0
        p2 = 1
        
        while p2 < len(nums):
            
            count = 1
            while p2 < len(nums) and nums[p1] == nums[p2]:
                count += 1
                p2 += 1
            
            if p2 >= len(nums):
                if count >= 2:
                    nums[p1+1] = nums[p2-1]
                    return p1+2
                else:
                    return p1+1
            
            if count >= 2:
                nums[p1+1] = nums[p2-1]
                nums[p1+2] = nums[p2]
                p1 += 2
                p2 += 1
            else:
                nums[p1+1] = nums[p2]
                p1 += 1
                p2 += 1
            
        return p1+1
        

if __name__ == "__main__":
    # a = [1,1,1,2,2,3]
    # a = [1, 1, 1]
    a = [1, 1, 1, 2, 3, 3, 3]
    # a = [1,1,1,1,3,3]
    print Solution().removeDuplicates(a)
    print a