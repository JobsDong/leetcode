#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []

        i = 0
        j = 0

        while i < m or j < n:
            num1 = nums1[i] if i < m else None
            num2 = nums2[j] if j < n else None

            if num1 is None:
                nums3.append(num2)
                j += 1
            elif num2 is None:
                nums3.append(num1)
                i += 1
            elif num1 <= num2:
                nums3.append(num1)
                i += 1
            else:
                nums3.append(num2)
                j += 1

        for i, num in enumerate([4, 5]):
            nums1[i] = num


if __name__ == "__main__":
    Solution().merge([1], 1, [], 0)