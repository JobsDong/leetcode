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
            min_nums.append(min(nums[i], min_nums[i-1]))

        bigger = nums[n-1]
        for i in xrange(n-2, 0, -1):
            if nums[i] > bigger:
                bigger = nums[i]
            else:
                if min_nums[i-1] < nums[i] < bigger:
                    return True
        return False


if __name__ == "__main__":
    print Solution().increasingTriplet([1, 2, 3, 4, 5])
    print Solution().increasingTriplet([5, 4, 3, 2, 1])
    print Solution().increasingTriplet([5, 2, 1, 4, 3])
    print Solution().increasingTriplet([5, 1, 2, 3, 3])