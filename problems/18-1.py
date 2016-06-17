#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def _is_duplicate(self, arrays, array):
        if len(arrays) == 0:
            return False

        i = len(arrays) - 1
        while i >= 0:
            if arrays[i][0] != array[0]:
                break
            if arrays[i][0] == array[0] and arrays[i][1] == array[1] and arrays[i][2] == array[2] and arrays[i][3] == array[3]:
                return True
            i -= 1

        return False

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        num_count = dict()
        d_nums = []

        for num in nums:
            if num in num_count:
                num_count[num] += 1
                if num_count[num] <= 4:
                    d_nums.append(num)
            else:
                num_count[num] = 1
                d_nums.append(num)

        arrays = []

        nums = sorted(d_nums)

        for i in xrange(0, len(nums)):

            for j in xrange(i+1, len(nums)):

                m = j+1
                n = len(nums)-1
                while m < n:
                    total = nums[i] + nums[j] + nums[m] + nums[n]

                    if total == target:
                        array = [nums[i], nums[j], nums[m], nums[n]]
                        if not self._is_duplicate(arrays, array):
                            arrays.append(array)
                        n -= 1
                    elif total > target:
                        n -= 1
                    else:
                        m += 1

        return arrays


if __name__ == "__main__":
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)