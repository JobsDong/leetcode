#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        j = 1

        while j < len(nums):

            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            if j >= len(nums):
                return i+1

            nums[i+1] = nums[j]
            i += 1
            j += 1
        return i+1