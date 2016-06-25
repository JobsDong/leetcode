#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        array = []
        p_set = set()

        for i, num in enumerate(nums):
            if num != 0:
                total *= num
            else:
                p_set.add(i)

        for i in xrange(0, len(nums)):
            if i in p_set:
                if len(p_set) > 1:
                    array.append(0)
                else:
                    array.append(total)
            else:
                if len(p_set) > 0:
                    array.append(0)
                else:
                    array.append(total / nums[i])

        return array

if __name__ == "__main__":
    print Solution().productExceptSelf([0, 0])
    print Solution().productExceptSelf([1,2,3,4,0])
    print Solution().productExceptSelf([1, 2, 3, 4])