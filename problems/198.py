#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        max_l0 = nums[0]
        max_l1 = max(nums[0], nums[1])

        for i in xrange(2, len(nums)):
            t = nums[i] + max_l0
            max_l0 = max_l1
            max_l1 = max(t, max_l0)

        return max_l1

if __name__ == "__main__":
    print Solution().rob([2, 1, 1, 2])