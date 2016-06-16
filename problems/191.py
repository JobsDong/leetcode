#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n & 1 == 1:
            count = 1

        while n != 0:
            n >>= 1
            if n & 1 == 1:
                count += 1

        return count



if __name__ == "__main__":
    print Solution().hammingWeight(11)