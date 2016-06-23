#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)

        i = 0
        array = []

        while i < n:
            b = nums[i]

            j = i
            e = nums[j]

            while j < n:

                if nums[j] != e and nums[j] != e+1:
                    break

                e = nums[j]
                j += 1

            array.append("%d" % b if b==e else "%d->%d" % (b, e))

            i = j

        return array

if __name__ == "__main__":
    print Solution().summaryRanges([0, 1, 2, 4, 5, 7])