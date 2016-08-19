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
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        start = 0
        end = len(matrix)-1

        while start <= end:
            mid = (start+end)/2
            if matrix[mid][0] > target:
                end = mid-1
            elif matrix[mid][-1] < target:
                start = mid+1
            else:
                i = bisect.bisect_left(matrix[mid], target)
                if matrix[mid][i] == target:
                    return True
                else:
                    return False

        return False



