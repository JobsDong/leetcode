#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1

        l1 = [1] * m
        l2 = [1] * m
        for i in xrange(1, n):
            for j in xrange(0, m):
                l2[j] = sum(l1[0:j+1])

            l1 = list(l2)

        return l2[m-1]

if __name__ == "__main__":
    print Solution().uniquePaths(4, 2)