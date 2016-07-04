#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        i = bisect.bisect_left(matrix[n-1], target)
        if 0 <= i - 1 < m and matrix[n-1][i-1] >= target:
            col = i-1
        elif 0 <= i < m and matrix[n-1][i] >= target:
            col = i
        elif 0 <= i+1 < m and matrix[n-1][i+1] >= target:
            col = i+1
        else:
            return False

        j = bisect.bisect_left([matrix[x][col] for x in xrange(0, n)], target)
        if 0 <= j+1 < n and matrix[j+1][col] <= target:
            row = j+1
        elif 0 <= j < n and matrix[j][col] <= target:
            row = j
        elif 0 <= j-1 < n and matrix[j-1][col] <= target:
            row = j-1
        else:
            return False

        for i in xrange(row, -1, -1):
            if matrix[i][m-1] < target:
                break

            p = bisect.bisect_left(matrix[i][col:], target)
            if matrix[i][p+col] == target:
                return True

        return False

if __name__ == "__main__":
    # print Solution().searchMatrix([[-5]], -2)
    print Solution().searchMatrix([[-1, 3]], 3)
    print Solution().searchMatrix([[1, 3, 5]], 5)
    print Solution().searchMatrix([[-1, 3]], 3)
    print Solution().searchMatrix([[-5]], -5)
    print Solution().searchMatrix([[1,  4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
    print Solution().searchMatrix([[1, 4], [2, 5]], 2)
    print Solution().searchMatrix([[1,3,5]], 1)
    print Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 19)