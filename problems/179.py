#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        sorted_nums = sorted(nums, cmp=lambda x,y: cmp(int(str(x)+str(y)),
                                                       int((str(y)+str(x)))), reverse=True)
        if len(sorted_nums) == 0 or sorted_nums[0] == 0:
            return "0"
        else:
            return "".join([str(i) for i in sorted_nums])

if __name__ == "__main__":
    print Solution().largestNumber([0, 0, 0, 0, 9])