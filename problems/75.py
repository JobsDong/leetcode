#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        # for color in [0, 1, 2]:
        color = 0

        for color in [0, 1, 2]:

            while True:
                while i < len(nums) and nums[i] == color:
                    i += 1

                if i >= len(nums):
                    break

                j = i+1
                while j < len(nums) and nums[j] != color:
                    j += 1

                if j >= len(nums):
                    break

                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 0, 0, 1]
    Solution().sortColors(nums)