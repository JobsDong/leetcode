#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = bisect.bisect_left(nums, target)
        if start >= len(nums) or nums[start] != target:
            start = -1

        end = bisect.bisect_right(nums, target)
        if end== 0 or nums[end-1] != target:
            end = -1
        else:
            end -= 1
        return [start, end]


if __name__ == "__main__":
    print Solution().searchRange([2, 2], 3)