#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)

if __name__ == "__main__":
    print Solution().searchInsert([1, 3, 5, 6], 3)
