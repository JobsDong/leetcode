#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0

        while i < len(nums):
            if nums[i] == 0:

                if j < i+1:
                    j = i+1

                while j < len(nums) and nums[j] == 0:
                    j += 1

                if j == len(nums):
                    break

                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1
            else:
                i += 1


if __name__ == "__main__":
    Solution().moveZeroes([1, 2, 0])