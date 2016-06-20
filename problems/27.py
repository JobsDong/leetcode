#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        j = 0
        size = len(nums)

        while True:

            while j < size and val == nums[j]:
                j += 1

            if j == size:
                return i
            nums[i] = nums[j]

            i += 1
            j += 1

if __name__ == "__main__":
    a = [3, 3]
    print Solution().removeElement(a, 3)
    print a