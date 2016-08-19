#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            while start+1 <= end and nums[start] == nums[start+1]:
                start += 1
            while start <= end-1 and nums[end] == nums[end-1]:
                end -= 1

            if start != end and nums[start] == nums[end]:
                start += 1

            mid = (start+end)/2

            if nums[start] > nums[end]:
                if mid == start:
                    return nums[end]

                if nums[mid] >= nums[start]:
                    start = mid
                elif nums[mid] <= nums[end]:
                    end = mid
            else:
                return nums[start]

        return nums[start]

if __name__ == "__main__":
    print Solution().findMin([1,2,2,2,0,1,1])