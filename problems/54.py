#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]

        n = len(matrix)
        m = len(matrix[0])

        i = 0

        nums = []

        while i < n / 2 and i < m / 2:
            nums += [matrix[i][j] for j in xrange(i, m-i-1)]
            nums += [matrix[j][m-i-1] for j in xrange(i, n-i-1)]
            nums += [matrix[n-i-1][j] for j in xrange(m-i-1, i, -1)]
            nums += [matrix[j][i] for j in xrange(n-i-1, i, -1)]
            i += 1

        if n % 2 == 1 and m-i > i-1 and m >= n:
            nums += [matrix[n/2][j] for j in xrange(i, m-i)]
        else:
            if m % 2 == 1 and n - i > i-1 and n > m:
                nums += [matrix[j][m/2] for j in xrange(i, n-i)]

        return nums