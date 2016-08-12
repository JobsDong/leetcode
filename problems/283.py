#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = 0
        i = 0

        while i < len(nums) - c:
            if nums[i] == 0:
                for j in xrange(i+1, len(nums)-c):
                    nums[j-1] = nums[j]
                nums[len(nums)-c-1] = 0
                c += 1
            else:
                i += 1

if __name__ == "__main__":
    Solution().moveZeroes([0, 0, 1])