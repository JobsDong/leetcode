#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        k = n-k

        count = 0

        i = 0
        while count < n:

            j = i
            tp = j
            t = nums[j]

            while count < n:
                if (j+k) % n == tp:
                    nums[j%n] = t
                    count += 1
                    break

                nums[j % n] = nums[(j+k) % n]
                count += 1
                j += k

            i += 1

if __name__ == "__main__":
    Solution().rotate([1, 2, 3, 4, 5, 6], 2)


