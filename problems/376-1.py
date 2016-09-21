#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0:
            return 0
        last_add = True
        last_sub = True
        j = 1

        for i in xrange(1, n):

            if nums[i] > nums[i-1] and last_sub:
                last_sub = False
                last_add = True
                j += 1
            elif nums[i] < nums[i-1] and last_add:
                last_add = False
                last_sub = True
                j += 1

        return j


if __name__ == "__main__":
    # print Solution().wiggleMaxLength([1,7,4,9,2,5])
    # print Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    # print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])
    print Solution().wiggleMaxLength([0, 0])

