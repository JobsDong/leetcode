#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        max_num = nums[0]
        prev_max_num = max_num

        for i in xrange(1, len(nums)):
            now_max_num = max(nums[i], nums[i]+prev_max_num)
            prev_max_num = now_max_num
            if now_max_num > max_num:
                max_num = now_max_num

        return max_num

if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

