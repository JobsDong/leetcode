#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x,y: x ^ y, nums)

        temp = 0x1
        while (temp & xor) == 0:
            temp <<= 1

        result0 = 0
        result1 = 0
        for num in nums:
            if num & temp == 0:
                result0 ^= num
            else:
                result1 ^= num

        return result0, result1