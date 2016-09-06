#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0

        n = len(triangle)
        min_totals = [triangle[0][0]]

        for i in xrange(1, n):
            t = min_totals[0]
            min_totals[0] += triangle[i][0]

            for j in xrange(1, i):
                t1 = min_totals[j]
                min_totals[j] = min(t+triangle[i][j], min_totals[j]+triangle[i][j])
                t = t1
            min_totals.append(t+triangle[i][i])

        return min(min_totals)

if __name__ == "__main__":
    print Solution().minimumTotal([[1], [2, 3], [3, 4, 5]])