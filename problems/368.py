#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        sorted_nums = sorted(nums)

        # 包含i元素的最长value
        max_lens = [1, ]
        max_trackback = [None, ]

        for i in xrange(1, n):
            max_len = 0
            max_trackback.append(None)
            for j in xrange(0, i):
                if sorted_nums[i] % sorted_nums[j] == 0:
                    if max_lens[j]+1 >= max_len:
                        max_len = max_lens[j]+1
                        max_trackback[i] = j
            max_lens.append(max_len)

        l = []
        max_len = 0
        max_len_pos = -1
        for k, t in enumerate(max_lens):
            if t > max_len:
                max_len = t
                max_len_pos = k

        while max_len_pos is not None:
            l.append(sorted_nums[max_len_pos])
            max_len_pos = max_trackback[max_len_pos]

        return l[-1::-1]

if __name__ == "__main__":
    print Solution().largestDivisibleSubset([1,2,3])
    # Solution().largestDivisibleSubset([1,2,4,8])