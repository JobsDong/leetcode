#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_sum = 0
        for i in xrange(0, len(nums) + 1):
            xor_sum ^= i

        xor_sum1 = 0
        for num in nums:
            xor_sum1 ^= num

        return xor_sum1 ^ xor_sum