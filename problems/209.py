#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        total = 0
        k = 0
        while k < n:
            total += nums[k]
            if total >= s:
                break
            k += 1

        if total < s:
            return 0

        a = [total]
        min_s = k+1
        b = [k]

        for i in xrange(1, n):
            j = b[i-1]
            total = a[i-1] - nums[i-1] - nums[j]

            while j < n:
                total += nums[j]
                if total >= s:
                    if j - i + 1 < min_s:
                        min_s = j - i + 1
                    break
                j += 1

            if total < s:
                break

            b.append(j)
            a.append(total)

        return min_s