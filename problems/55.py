#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        results = [False] * n
        results[0] = True
        p = 1

        for i in xrange(0, n):
            if results[i]:
                for j in xrange(p, nums[i]+i+1):
                    if j >= n:
                        break
                    results[j] = True
                p = min(nums[i]+i, n-1)
            else:
                p = i+1

        return results[n-1]

if __name__ == "__main__":
    print Solution().canJump([6,2,1,4,3,2,1,4,3])