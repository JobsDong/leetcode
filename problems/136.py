#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_1set = set()

        for num in nums:
            if num in num_1set:
                num_1set.remove(num)
            else:
                num_1set.add(num)
        return list(num_1set)[0]