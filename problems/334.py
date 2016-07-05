#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        if n <= 2:
            return False

        min_nums = [nums[0]]
        for i in xrange(1, n):
            if nums[i] < min_nums[i-1]:
                min_nums.append(nums[i])
            else:
                min_nums.append(min_nums[i-1])

        max_nums = list(nums)
        for i in xrange(n-2, -1, -1):
            if nums[i] > max_nums[i+1]:
                max_nums[i] = nums[i]
            else:
                max_nums[i] = max_nums[i+1]

        for i in xrange(1, n-1):
            if min_nums[i-1] < nums[i] < max_nums[i+1]:
                return True
        return False

if __name__ == "__main__":
    print Solution().increasingTriplet([1, 2, 3, 4, 5])
    print Solution().increasingTriplet([5, 4, 3, 2, 1])
    print Solution().increasingTriplet([5, 2, 1, 4, 3])