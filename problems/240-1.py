#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m-1

        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


if __name__ == "__main__":
    print Solution().searchMatrix([[-5]], -2)
    print Solution().searchMatrix([[-1, 3]], 3)
    print Solution().searchMatrix([[1, 3, 5]], 5)
    print Solution().searchMatrix([[-1, 3]], 3)
    print Solution().searchMatrix([[-5]], -5)
    print Solution().searchMatrix([[1,  4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
    print Solution().searchMatrix([[1, 4], [2, 5]], 2)
    print Solution().searchMatrix([[1,3,5]], 1)
    print Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 19)