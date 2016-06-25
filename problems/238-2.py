#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_a = [1]

        total_l = nums[0]
        for i in xrange(1, len(nums)):
            l_a.append(total_l)
            total_l *= nums[i]

        total_r = 1
        for i in xrange(len(nums)-1, -1, -1):
            l_a[i] *= total_r
            total_r *= nums[i]

        return l_a

if __name__ == "__main__":
    print Solution().productExceptSelf([0, 0])
    print Solution().productExceptSelf([1,2,3,4,0])
    print Solution().productExceptSelf([1, 2, 3, 4])