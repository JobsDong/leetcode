#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        if size == 0:
            return nums

        i = size-1
        while i >= 1:
            if nums[i] > nums[i-1]:
                break

            i -= 1

        if i - 1 >= 0:
            # insert
            t = nums[i-1]

            j = size-1
            while j >= i:
                if nums[j] > t:
                    nums[i-1] = nums[j]
                    nums[j] = t
                    break
                j -= 1

        # reverse
        m = i
        n = size-1
        while m < n:
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
            m += 1
            n -= 1


if __name__ == "__main__":
    Solution().nextPermutation([1, 3, 2])


