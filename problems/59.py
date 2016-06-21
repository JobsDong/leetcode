#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # init
        matrix = []
        for i in xrange(0, n):
            l = list()
            for j in xrange(0, n):
                l.append(0)
            matrix.append(l)

        num = 1
        i = 0
        while i < n/2:
            for j in xrange(i, n-i-1):
                matrix[i][j] = num
                num += 1
            for j in xrange(i, n-i-1):
                matrix[j][n-i-1] = num
                num += 1
            for j in xrange(n-i-1, i, -1):
                matrix[n-i-1][j] = num
                num += 1
            for j in xrange(n-i-1, i, -1):
                matrix[j][i] = num
                num += 1
            i += 1

        if n % 2 == 1:
            matrix[n/2][n/2] = num

        return matrix
