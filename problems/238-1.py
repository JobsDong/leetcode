#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_a = []

        total_l = 1
        for num in nums:
            total_l *= num
            l_a.append(total_l)

        total_r = 1
        r_a = [0 for i in xrange(0, len(nums))]
        for i in xrange(len(nums)-1, -1, -1):
            total_r *= nums[i]
            r_a[i] = total_r

        array = []
        for i in xrange(0, len(nums)):
            if i-1 >= 0:
                l = l_a[i-1]
            else:
                l = 1

            if i+1 >= len(nums):
                r = 1
            else:
                r = r_a[i+1]

            array.append(l * r)

        return array

if __name__ == "__main__":
    print Solution().productExceptSelf([0, 0])
    print Solution().productExceptSelf([1,2,3,4,0])
    print Solution().productExceptSelf([1, 2, 3, 4])