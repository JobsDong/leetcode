#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        if self.m == 0:
            return

        self.n = len(matrix[0])
        if self.n == 0:
            return

        self.total_matrix = []

        for i in xrange(0, self.m):
            total = 0
            l = []
            for j in xrange(0, self.n):
                total += matrix[i][j]
                l.append(total + (0 if i-1 < 0 else self.total_matrix[i-1][j]))
            self.total_matrix.append(l)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0:
            return 0

        t1 = self.total_matrix[row1-1][col2] if row1 > 0 else 0
        t2 = self.total_matrix[row2][col1-1] if col1 > 0 else 0
        t3 = self.total_matrix[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        return self.total_matrix[row2][col2] - t2 - t1 + t3



# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == "__main__":
    n = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    print n.sumRegion(2, 1, 4, 3)