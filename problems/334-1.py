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

        small = nums[0]
        for i in xrange(1, n-1):
            if small < nums[i]:
                if nums[i] < max(nums[i+1:]):
                    return True
            else:
                small = nums[i]

        return False

if __name__ == "__main__":
    print Solution().increasingTriplet([1, 2, 3, 4, 5])
    print Solution().increasingTriplet([5, 4, 3, 2, 1])
    print Solution().increasingTriplet([5, 2, 1, 4, 3])
    print Solution().increasingTriplet([5, 1, 2, 3, 3])