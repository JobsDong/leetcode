#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# lte


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1, 1]

        for i in xrange(2, n+1):

            j = 1
            min_count = i
            while j * j <= i:
                if j * j == i:
                    min_count = 1
                    break
                t = l[j*j] + l[i-j*j]
                min_count = min(min_count, t)
                j += 1
            l.append(min_count)

        return l[n]

if __name__ == "__main__":
    print Solution().numSquares(100000)