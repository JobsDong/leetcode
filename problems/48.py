#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        i = 0
        while i < n/2:

            temp1 = [matrix[i][y] for y in xrange(0, n)]
            temp2 = [matrix[y][n-i-1] for y in xrange(0, n)]
            temp3 = [matrix[n-i-1][y] for y in xrange(n-1, -1, -1)]
            temp4 = [matrix[y][i] for y in xrange(n-1, -1, -1)]

            for j in xrange(i, n-i):
                matrix[i][j] = temp4[j]

            for k in xrange(i, n-i):
                matrix[k][n-i-1] = temp1[k]

            for m in xrange(i, n-i):
                matrix[n-i-1][n-m-1] = temp2[m]

            for x in xrange(i, n-i):
                matrix[n-x-1][i] = temp3[x]
            i += 1

if __name__ == "__main__":
    Solution().rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

