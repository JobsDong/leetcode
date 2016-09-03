#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        l1 = []
        total = 0
        for i in xrange(0, m):
            total += grid[0][i]
            l1.append(total)

        l2 = list(l1)
        for i in xrange(1, n):
            l2[0] = l1[0] + grid[i][0]

            for j in xrange(1, m):
                l2[j] = min(l2[j-1]+grid[i][j], l1[j]+grid[i][j])

            l1 = list(l2)

        return l2[m-1]

if __name__ == "__main__":
    # print Solution().minPathSum([[3, 2, 1],[5, 4, 3]])
    print Solution().minPathSum([[1,2],[1,1]])