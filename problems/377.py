#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        totals = [0]

        for i in xrange(1, target+1):
            total = 0
            for num in nums:
                if i == num:
                    total += 1
                else:
                    total += totals[i-num] if i >= num else 0

            totals.append(total)

        return totals[target]

if __name__ == "__main__":
    print Solution().combinationSum4([4, 2, 1], 32)