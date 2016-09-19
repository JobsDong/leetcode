#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1

        total = 0

        while i < j:
            if height[i] >= height[j]:
                total = max(total, height[j]*(j-i))
                j -= 1
            else:
                total = max(total, height[i]*(j-i))
                i += 1

        return total
