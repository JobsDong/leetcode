#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        nums = [1]
        indexes = [0] * len(primes)

        while len(nums) < n:

            min_num = None
            min_i = None

            for i, num in enumerate(primes):
                total_num = num * nums[indexes[i]]
                while total_num <= nums[-1]:
                    indexes[i] += 1
                    total_num = num * nums[indexes[i]]
                if min_num is None or total_num < min_num:
                    min_num = total_num
                    min_i = i

            nums.append(min_num)
            indexes[min_i] += 1

        return nums[n-1]


if __name__ == "__main__":
    print Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
