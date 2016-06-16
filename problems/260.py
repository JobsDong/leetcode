#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        once_set = set()
        for num in nums:
            if num in once_set:
                once_set.remove(num)
            else:
                once_set.add(num)
        return list(once_set)