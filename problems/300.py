#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_lengths = []

        for i, num in enumerate(nums):
            max_length = 1
            for j in xrange(0, i):
                if num > nums[j] and max_lengths[j]+1 > max_length:
                    max_length = max_lengths[j]+1
            max_lengths.append(max_length)

        return max(max_lengths)

if __name__ == "__main__":
    print Solution().lengthOfLIS([])
