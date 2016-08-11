#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) % 2 == 0:
            end = len(nums) / 2
        else:
            end = (len(nums) + 1) / 2

        t1 = nums[0:end]
        t2 = nums[end:]

        j = len(t1)-1
        k = len(t2)-1
        for i in xrange(0, len(nums)):
            if i % 2 == 0:
                nums[i] = t1[j]
                j -= 1
            else:
                nums[i] = t2[k]
                k -= 1

        return nums



if __name__ == "__main__":
    # print Solution().wiggleSort([1,3,2,2,3,1])
    # print Solution().wiggleSort([1,1,2,1,2,2,1])
    # print Solution().wiggleSort([1, 5, 1, 1, 6])
    # print Solution().wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2])
    print Solution().wiggleSort([4, 5, 5, 6])