#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums)-1

        while start <= end:

            mid = (start+end)/2

            if mid == start or mid == end:
                return start if nums[start] > nums[end] else end

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid]:
                start = mid
            elif nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid

        return start

if __name__ == "__main__":
    print Solution().findPeakElement([1, 2])