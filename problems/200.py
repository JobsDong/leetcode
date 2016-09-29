#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        line1 = [0] * n
        total = 0
        new_flag = 1

        for i in xrange(0, m):
            line2 = []
            for j in xrange(0, n):
                if grid[i][j] == '0':
                    line2.append(0)
                else:
                    if (grid[i-1][j] == '0' or i-1 < 0) and (grid[i][j-1] == '0' or j-1 < 0):
                        line2.append(new_flag)
                        new_flag += 1
                        total += 1
                    elif i-1 >= 0 and grid[i-1][j] == '1' and j-1 >= 0 and grid[i][j-1] == '1':
                        if line1[j] == line2[j-1]:
                            pass
                        else:
                            t = line1[j]
                            for k in xrange(0, n):
                                if k <= j-1 and line2[k] == t:
                                    line2[k] = line2[j-1]
                                elif k >= j and line1[k] == t:
                                    line1[k] = line2[j-1]
                            total -= 1

                        line2.append(line2[j-1])
                    else:
                        if j-1 >= 0 and grid[i][j-1] == '1':
                            line2.append(line2[j-1])
                        else:
                            line2.append(line1[j])

            line1 = line2

        return total

if __name__ == "__main__":
    print Solution().numIslands(["1", "1"])