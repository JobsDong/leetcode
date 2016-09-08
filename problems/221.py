#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        l1 = [int(item) for item in matrix[0]]
        max_length = max(l1)

        for i in xrange(1, m):

            t0 = l1[0]
            l1[0] = int(matrix[i][0])
            max_length = l1[0] if l1[0] > max_length else max_length

            for j in xrange(1, n):
                t1 = l1[j]
                if matrix[i][j] == '1':
                    l1[j] = min(l1[j], l1[j-1], t0) + 1
                    max_length = l1[j] if l1[j] > max_length else max_length
                else:
                    l1[j] = 0
                t0 = t1
        return max_length * max_length

if __name__ == "__main__":
    # print Solution().maximalSquare(["10100","10111","11111","10010"])
    print Solution().maximalSquare(["1111","1111","1111"])