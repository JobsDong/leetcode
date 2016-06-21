#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        # row
        row0 = matrix[0][0]
        for j in xrange(0, m):
            if matrix[0][j] == 0:
                print j
                row0 = 0
                break

        # col
        col0 = matrix[0][0]
        for j in xrange(0, n):
            if matrix[j][0] == 0:
                col0 = 0
                break

        for i in xrange(1, m):
            for j in xrange(0, n):
                if matrix[j][i] == 0:
                    matrix[0][i] = 0
                    break

        for i in xrange(1, n):
            for j in xrange(0, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break

        for i in xrange(n-1, -1, -1):
            for j in xrange(m-1, -1, -1):
                if i == 0:
                    if row0 == 0:
                        matrix[i][j] = 0
                if j == 0:
                    if col0 == 0:
                        matrix[i][j] = 0

                if i != 0 and j != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0


if __name__ == "__main__":
    Solution().setZeroes([[1,2,3,4],[5,0,5,2],[8,9,2,0],[5,7,2,1]])
