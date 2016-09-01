#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])

        l1 = []
        has_obstacle = False
        for i in xrange(0, m):
            if obstacleGrid[0][i] == 1:
                has_obstacle = True
            l1.append(0 if has_obstacle else 1)

        l2 = list(l1)

        for i in xrange(1, n):
            l2[0] = l1[0] if obstacleGrid[i][0] == 0 else 0

            for j in xrange(1, m):
                l2[j] = 0 if obstacleGrid[i][j] == 1 else l2[j-1] + l1[j]

            l1 = list(l2)

        return l2[m-1]

