#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.totals = []

        total = 0
        for num in nums:
            total += num
            self.totals.append(total)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0

        if i == 0:
            return self.totals[j]
        else:
            return self.totals[j] - self.totals[i-1]

if __name__ == "__main__":
    n = NumArray([1, 1, 1, 1])
    print n.sumRange(1, 3)
