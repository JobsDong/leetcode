#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = dict()
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        for key, value in num_count.iteritems():
            if value > len(nums) / 2:
                return key

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 1])