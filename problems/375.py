#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        matrix = [[0]*(n+1)]

        for j in xrange(1, n+1):
            for i in xrange(j, 0, -1):
                if i == j:
                    matrix.append([0]*(n+1))
                    matrix[i][j] = 0
                else:
                    min_matrix_i_j = max(i, i+matrix[i+1][j])
                    for k in xrange(i+1, j+1):
                        matrix_i_j = max(matrix[i][k-1]+k, (matrix[k+1][j] if k+1 <= j else 0)+k)
                        min_matrix_i_j = min(min_matrix_i_j, matrix_i_j)

                    matrix[i][j] = min_matrix_i_j

        return matrix[1][n]

if __name__ == "__main__":
    print Solution().getMoneyAmount(3)