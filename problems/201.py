#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        max_zero_num = n
        temp = max_zero_num
        x = 0xfffffffe

        while temp >= m:
            max_zero_num = temp
            temp &= x
            x <<= 1
        return max_zero_num & m & n


if __name__ == "__main__":
    print Solution().rangeBitwiseAnd(0, 0)