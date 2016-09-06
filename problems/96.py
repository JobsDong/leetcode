#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        nums = [1, 1]
        for i in xrange(2, n+1):
            total = 0
            for j in xrange(0, i):
                total += nums[j] * nums[i-1-j]

            nums.append(total)

        return nums[n]

if __name__ == "__main__":
    print Solution().numTrees(2)